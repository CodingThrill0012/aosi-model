"""Context Services plane (CTX): a small TF-IDF retrieval service over the
synthetic corpus. The query embedding stays inside this service; it returns
retrieved passages with scores and provenance. A fault-injection endpoint adds
a fixed delay to every search (POST /admin/delay?ms=N)."""
import json, math, re, sys, time, threading
from collections import Counter
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import corpus

TOK = re.compile(r"[a-z0-9]+")
DOCS = corpus.build()
DF = Counter()
VECS = []
for d in DOCS:
    tf = Counter(TOK.findall(d["text"].lower()))
    DF.update(tf.keys())
    VECS.append(tf)
N = len(DOCS)
IDF = {t: math.log((N + 1) / (df + 1)) + 1 for t, df in DF.items()}


def embed(text):
    tf = Counter(TOK.findall(text.lower()))
    v = {t: c * IDF.get(t, 0.0) for t, c in tf.items()}
    norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {t: x / norm for t, x in v.items()}


DOC_EMB = [embed(d["text"]) for d in DOCS]
STATE = {"delay_ms": 0.0}
LOCK = threading.Lock()


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj, headers=None):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        u = urlparse(self.path)
        if u.path == "/admin/delay":
            with LOCK:
                STATE["delay_ms"] = float(parse_qs(u.query).get("ms", ["0"])[0])
            self._send(200, STATE)
        else:
            self._send(404, {})

    def do_GET(self):
        u = urlparse(self.path)
        if u.path != "/search":
            self._send(404, {})
            return
        q = parse_qs(u.query)
        query = q.get("q", [""])[0]
        k = int(q.get("k", ["3"])[0])
        t0 = time.perf_counter()
        qe = embed(query)                       # query embedding (internal)
        t1 = time.perf_counter()
        scores = []
        for i, de in enumerate(DOC_EMB):
            s = sum(w * de.get(t, 0.0) for t, w in qe.items())
            scores.append((s, i))
        scores.sort(reverse=True)
        top = scores[:k]
        t2 = time.perf_counter()
        with LOCK:
            delay = STATE["delay_ms"]
        if delay:
            time.sleep(delay / 1000.0)          # injected fault
        t3 = time.perf_counter()
        passages = [{"id": DOCS[i]["id"], "score": round(s, 4),
                     "version": DOCS[i]["version"], "text": DOCS[i]["text"]}
                    for s, i in top]
        self._send(200, {"passages": passages},
                   {"X-Embed-ms": f"{(t1-t0)*1e3:.3f}",
                    "X-Search-ms": f"{(t2-t1)*1e3:.3f}",
                    "X-Injected-ms": f"{(t3-t2)*1e3:.3f}"})


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8092
    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
