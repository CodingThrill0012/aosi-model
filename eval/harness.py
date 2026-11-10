"""DAIRM boundary-attributed diagnosis: measured fault-injection study.

Components (see README.md):
  L6  client          - this process, closed-loop workers
  L5  gateway         - this process: guardrail, CTX call, template, tokenize
  CTX context service - ctx_service.py (HTTP, TF-IDF retrieval)
  L4  serving engine  - llama.cpp llama-server (HTTP, continuous batching)
  L3-L1               - llama.cpp CPU backend on the host CPU (not separable
                        on this hardware; host CPU pressure is the device signal)

For each repetition the harness measures a baseline, then each condition
(one injected fault, or none), runs the automated triage of DAIRM-TR-0001
§7.5 against the baseline, runs the isolation test the triage selects, and
writes raw per-request records, telemetry samples, OpenTelemetry spans and
attribution results to results/. The triage never reads the fault label or
the CTX injected-delay header; those are kept only for scoring."""
import argparse, csv, http.client, json, os, platform, random, re, signal
import statistics as st, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExporter, SpanExportResult

import corpus

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
L4_PORT, CTX_PORT = 8091, 8092

# ---- workload (fixed before any measurement) ---------------------------------
N_REQ = int(os.environ.get("DAIRM_N_REQ", "24"))  # measured requests per condition
CONC = 3            # closed-loop client concurrency
N_PRED = 96         # output tokens per request (ignore_eos -> fixed length)
TOP_K = 2
WARMUP = 3
CTX_DELAY_MS = 1000  # injected CTX fault
HOG_PROCS = 4       # injected compute contention: busy-loop processes pinned to the engine cores
ENGINE_CPUS = "0-3"  # llama-server (L4-L1) cores; harness + CTX run on the others (run_all.sh)
SLOTS_BASE, SLOTS_FAULT = 4, 1
CTX_PER_SLOT = 4096

# ---- triage thresholds (fixed a priori, not tuned on results) ----------------
REL = 0.25
FLOOR = {"ttft": 30.0, "tpot": 1.5, "l5_own": 30.0, "ctx": 30.0,
         "l4_queue": 30.0, "prefill": 30.0, "decode_tok": 1.5,
         "prompt_tokens": 20.0, "deferred": 0.5, "stall": 0.10}

SYSTEM = ("You are an internal policy assistant. Answer only from the policy "
          "passages provided, cite the passage id, and be brief.")
HISTORY_TURNS = [(f"Earlier question {i}: what does the policy say about item {i}?",
                  f"Earlier answer {i}: " + "the relevant section requires approval, "
                  "logging and review by the named role within the stated window. " * 3)
                 for i in range(10)]
SUMMARY = "Summary of earlier conversation: the user asked about several access and approval rules."


# ---- OpenTelemetry: spans written as JSON lines ------------------------------
class JsonlExporter(SpanExporter):
    def __init__(self, path):
        self.f = open(path, "a")
        self.lock = threading.Lock()

    def export(self, spans):
        with self.lock:
            for s in spans:
                self.f.write(json.dumps(json.loads(s.to_json())) + "\n")
            self.f.flush()
        return SpanExportResult.SUCCESS


provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("dairm.eval")


def ns(t):  # perf_counter seconds -> epoch ns for explicit span times
    return int((t - PC0 + WALL0) * 1e9)


PC0, WALL0 = time.perf_counter(), time.time()


# ---- HTTP helpers -------------------------------------------------------------
def http_json(port, method, path, body=None, timeout=600):
    c = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    c.request(method, path, body=json.dumps(body) if body is not None else None,
              headers={"Content-Type": "application/json"})
    r = c.getresponse()
    data = r.read()
    hdr = dict(r.getheaders())
    c.close()
    return json.loads(data) if data else {}, hdr


def tokenize(text):
    out, _ = http_json(L4_PORT, "POST", "/tokenize", {"content": text})
    return len(out.get("tokens", []))


def chatml(messages):
    s = ""
    for role, content in messages:
        s += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    return s + "<|im_start|>assistant\n"


# ---- L5 gateway ---------------------------------------------------------------
class Gateway:
    def __init__(self):
        self.history_policy = "summary"   # fault: "full"
        self.ctx_mode = "live"            # isolation: "bypass"
        self.fixed_passages = None

    def handle(self, question, parent_ctx, rec):
        t_in = time.perf_counter()
        with tracer.start_as_current_span("l5.gateway", context=parent_ctx) as gw:
            gw.set_attribute("dairm.layer", 5)
            gw.set_attribute("dairm.plane", "request_path")
            # input guardrail
            g0 = time.perf_counter()
            blocked = bool(re.search(r"(ignore previous|system prompt)", question, re.I))
            g1 = time.perf_counter()
            rec["l5_guard_in_ms"] = (g1 - g0) * 1e3
            # context services call
            c0 = time.perf_counter()
            with tracer.start_as_current_span("ctx.retrieve") as cs:
                cs.set_attribute("dairm.plane", "context_services")
                cs.set_attribute("dairm.ctx.service", "retrieval")
                cs.set_attribute("gen_ai.operation.name", "retrieval")
                cs.set_attribute("dairm.data_state", "retrieved_passages")
                if self.ctx_mode == "bypass":
                    passages, hdr = self.fixed_passages, {}
                else:
                    out, hdr = http_json(CTX_PORT, "GET", f"/search?q={quote(question)}&k={TOP_K}")
                    passages = out["passages"]
                cs.set_attribute("dairm.ctx.top_k", TOP_K)
                cs.set_attribute("dairm.ctx.passages_returned", len(passages))
            c1 = time.perf_counter()
            rec["ctx_ms"] = (c1 - c0) * 1e3
            rec["ctx_embed_ms"] = float(hdr.get("X-Embed-ms", "nan"))
            rec["ctx_search_ms"] = float(hdr.get("X-Search-ms", "nan"))
            rec["gt_ctx_injected_ms"] = float(hdr.get("X-Injected-ms", "nan"))  # scoring only
            rec["ctx_mode"] = self.ctx_mode
            # template (enriched prompt)
            t0 = time.perf_counter()
            ctx_text = "\n".join(f"[{p['id']} v{p['version']}] {p['text']}" for p in passages)
            msgs = [("system", SYSTEM)]
            if self.history_policy == "full":
                for q, a in HISTORY_TURNS:
                    msgs += [("user", q), ("assistant", a)]
            else:
                msgs += [("system", SUMMARY)]
            msgs += [("user", f"Policy passages:\n{ctx_text}\n\nQuestion: {question}")]
            prompt = chatml(msgs)
            t1 = time.perf_counter()
            # L5 pre-tokenizes for budgeting (documented L5->L4 coupling, P3)
            n_prompt = tokenize(prompt)
            n_ctx = tokenize(ctx_text)
            t2 = time.perf_counter()
            rec["l5_template_ms"] = (t1 - t0) * 1e3
            rec["l5_tokenize_ms"] = (t2 - t1) * 1e3
            rec["prompt_tokens"] = n_prompt
            rec["ctx_tokens"] = n_ctx
            rec["history_policy"] = self.history_policy
            gw.set_attribute("dairm.l5.prompt_tokens_enriched", n_prompt)
            gw.set_attribute("dairm.data_state", "enriched_prompt")
            gw.set_attribute("dairm.l5.guardrail.verdict", "block" if blocked else "allow")
            # call L4 (streaming)
            s0 = time.perf_counter()
            self._generate(prompt, rec, s0)
            s_end = time.perf_counter()
            rec["l5_own_ms"] = ((s0 - t_in) - (c1 - c0)) * 1e3
            rec["l5_total_ms"] = (s_end - t_in) * 1e3

    def _generate(self, prompt, rec, s0):
        body = {"prompt": prompt, "n_predict": N_PRED, "temperature": 0.0,
                "ignore_eos": True, "cache_prompt": False, "stream": True}
        c = http.client.HTTPConnection("127.0.0.1", L4_PORT, timeout=900)
        c.request("POST", "/completion", body=json.dumps(body),
                  headers={"Content-Type": "application/json"})
        r = c.getresponse()
        t_tokens, timings, buf = [], None, b""
        while True:
            line = r.readline()
            if not line:
                break
            line = line.strip()
            if not line.startswith(b"data:"):
                continue
            ev = json.loads(line[5:])
            if ev.get("content") or (not ev.get("stop") and "content" in ev):
                t_tokens.append(time.perf_counter())
            if ev.get("stop"):
                timings = ev.get("timings", {})
                rec["l4_prompt_n"] = ev.get("tokens_evaluated")
                break
        c.close()
        t_end = time.perf_counter()
        first = t_tokens[0] if t_tokens else t_end
        rec["_first"] = first
        rec["l4_ttft_ms"] = (first - s0) * 1e3
        rec["n_tokens"] = len(t_tokens)
        rec["tpot_ms"] = ((t_tokens[-1] - t_tokens[0]) / (len(t_tokens) - 1) * 1e3
                          if len(t_tokens) > 1 else float("nan"))
        rec["l4_prefill_ms"] = timings.get("prompt_ms", float("nan"))
        rec["l4_decode_ms"] = timings.get("predicted_ms", float("nan"))
        rec["l4_predicted_n"] = timings.get("predicted_n", 0)
        rec["l4_decode_tok_ms"] = timings.get("predicted_per_token_ms", float("nan"))
        # queue + engine overhead before prefill, derived (L5-observed TTFT minus prefill)
        rec["l4_queue_ms"] = max(0.0, rec["l4_ttft_ms"] - rec["l4_prefill_ms"])
        # explicit-time L4 child spans reconstructed from engine timings
        q_end = s0 + rec["l4_queue_ms"] / 1e3
        p_end = q_end + rec["l4_prefill_ms"] / 1e3
        with tracer.start_as_current_span("l4.generate", start_time=ns(s0), end_on_exit=False) as sp:
            sp.set_attribute("dairm.layer", 4)
            sp.set_attribute("dairm.plane", "request_path")
            sp.set_attribute("dairm.data_state", "token_stream")
            sp.set_attribute("dairm.l4.queue_time", rec["l4_queue_ms"] / 1e3)
            sp.set_attribute("gen_ai.usage.input_tokens", int(rec.get("l4_prompt_n") or 0))
            sp.set_attribute("gen_ai.usage.output_tokens", int(rec["l4_predicted_n"]))
            for name, a, b in (("l4.queue", s0, q_end), ("l4.prefill", q_end, p_end),
                               ("l4.decode", p_end, t_end)):
                ch = tracer.start_span(name, start_time=ns(a))
                ch.set_attribute("dairm.layer", 4)
                ch.end(end_time=ns(b))
            sp.end(end_time=ns(t_end))


# ---- telemetry sampler (L4 engine metrics + host CPU as the device signal) ----
class Sampler(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.label, self.rows, self.stop_ev = None, [], threading.Event()

    @staticmethod
    def _cpu():
        f = open("/proc/stat").readline().split()[1:]
        v = list(map(int, f))
        idle = v[3] + v[4]
        return sum(v), idle

    @staticmethod
    def _psi():
        for line in open("/proc/pressure/cpu"):
            if line.startswith("some"):
                return int(line.split("total=")[1])
        return 0

    def run(self):
        tot0, idle0 = self._cpu()
        psi0, t0 = self._psi(), time.perf_counter()
        while not self.stop_ev.wait(0.25):
            tot1, idle1 = self._cpu()
            psi1, t1 = self._psi(), time.perf_counter()
            busy = 1 - (idle1 - idle0) / max(1, tot1 - tot0)
            stall = (psi1 - psi0) / 1e6 / (t1 - t0)
            tot0, idle0, psi0, t0 = tot1, idle1, psi1, t1
            m = {}
            try:
                c = http.client.HTTPConnection("127.0.0.1", L4_PORT, timeout=2)
                c.request("GET", "/metrics")
                for line in c.getresponse().read().decode().splitlines():
                    if line.startswith("llamacpp:"):
                        k, v = line.split()
                        m[k.split(":")[1]] = float(v)
                c.close()
            except Exception:
                pass
            if self.label:
                self.rows.append({"label": self.label, "t": t1 - PC0,
                                  "dairm.device_id": platform.node() + ":cpu",
                                  "host_cpu_busy": round(busy, 4),
                                  "host_cpu_stall": round(stall, 4),
                                  "requests_processing": m.get("requests_processing"),
                                  "requests_deferred": m.get("requests_deferred"),
                                  "busy_slots_per_decode": m.get("n_busy_slots_per_decode")})


# ---- process management -------------------------------------------------------
class Stack:
    def __init__(self, llama_dir, model, threads):
        self.llama_dir, self.model, self.threads = llama_dir, model, threads
        self.llama = self.ctx = None
        self.hogs = []

    def start_llama(self, slots):
        self.stop_llama()
        env = dict(os.environ, LD_LIBRARY_PATH=self.llama_dir)
        cmd = ["taskset", "-c", ENGINE_CPUS, os.path.join(self.llama_dir, "llama-server"), "-m", self.model,
               "-np", str(slots), "-c", str(CTX_PER_SLOT * slots),
               "-t", str(self.threads), "-tb", str(self.threads),
               "--metrics", "--no-webui", "--host", "127.0.0.1", "--port", str(L4_PORT)]
        self.llama = subprocess.Popen(cmd, env=env, stdout=open(os.path.join(RES, "llama-server.log"), "a"),
                                      stderr=subprocess.STDOUT)
        self.slots = slots
        for _ in range(240):
            try:
                if http_json(L4_PORT, "GET", "/health", timeout=2)[0].get("status") == "ok":
                    return
            except Exception:
                pass
            time.sleep(0.5)
        raise RuntimeError("llama-server did not start")

    def stop_llama(self):
        if self.llama:
            self.llama.terminate()
            self.llama.wait(30)
            self.llama = None

    def start_ctx(self):
        self.ctx = subprocess.Popen([sys.executable, os.path.join(HERE, "ctx_service.py"), str(CTX_PORT)])
        for _ in range(60):
            try:
                http_json(CTX_PORT, "POST", "/admin/delay?ms=0", timeout=2)
                return
            except Exception:
                time.sleep(0.25)

    def ctx_delay(self, ms):
        http_json(CTX_PORT, "POST", f"/admin/delay?ms={ms}")

    def start_hog(self):
        code = "while True: pass"
        self.hogs = [subprocess.Popen(["taskset", "-c", ENGINE_CPUS, sys.executable, "-c", code])
                     for _ in range(HOG_PROCS)]
        time.sleep(1.0)

    def stop_hog(self):
        for p in self.hogs:
            p.kill()
            p.wait()
        self.hogs = []

    def shutdown(self):
        self.stop_hog()
        self.stop_llama()
        if self.ctx:
            self.ctx.terminate()


# ---- one measurement ------------------------------------------------------------
def run_batch(gw, sampler, rep, label, phase, questions, conc, writer):
    for q in questions[:WARMUP]:          # warm-up, discarded
        gw.handle(q, None, {})
    sampler.label = f"{rep}|{label}|{phase}"
    recs = []
    lock = threading.Lock()

    def one(i_q):  # one L6 request
        i, q = i_q
        rec = {"rep": rep, "condition": label, "phase": phase, "req": i,
               "conc": conc, "slots": STACK.slots}
        t0 = time.perf_counter()
        with tracer.start_as_current_span("l6.request") as root:
            root.set_attribute("dairm.layer", 6)
            root.set_attribute("dairm.plane", "request_path")
            root.set_attribute("dairm.data_state", "request_payload")
            root.set_attribute("dairm.eval.condition", label)
            root.set_attribute("dairm.eval.rep", rep)
            gw.handle(q, None, rec)
        t1 = time.perf_counter()
        rec["e2e_ms"] = (t1 - t0) * 1e3
        rec["ttft_ms"] = (rec.pop("_first") - t0) * 1e3   # L6-start to first token
        rec["t_start"] = t0 - PC0
        with lock:
            recs.append(rec)
    with ThreadPoolExecutor(conc) as ex:
        list(ex.map(one, list(enumerate(questions[WARMUP:WARMUP + N_REQ]))))
    sampler.label = None
    for r in recs:
        writer.writerow({k: r.get(k) for k in FIELDS})
    return recs


FIELDS = ["rep", "condition", "phase", "req", "conc", "slots", "t_start", "e2e_ms", "ttft_ms",
          "tpot_ms", "l5_own_ms", "l5_guard_in_ms", "l5_template_ms", "l5_tokenize_ms",
          "ctx_ms", "ctx_embed_ms", "ctx_search_ms", "ctx_mode", "history_policy",
          "prompt_tokens", "ctx_tokens", "l4_prompt_n", "l4_ttft_ms", "l4_queue_ms",
          "l4_prefill_ms", "l4_decode_ms", "l4_predicted_n", "l4_decode_tok_ms", "n_tokens",
          "gt_ctx_injected_ms"]


# ---- triage (DAIRM-TR-0001 §7.5, automated) ---------------------------------------
def med(recs, k):
    v = [r[k] for r in recs if r.get(k) is not None and r[k] == r[k]]
    return st.median(v) if v else float("nan")


def samp_mean(rows, label, k):
    v = [r[k] for r in rows if r["label"] == label and r.get(k) is not None]
    return st.mean(v) if v else 0.0


def summarize(recs, rows, label):
    return {"ttft": med(recs, "ttft_ms"), "tpot": med(recs, "tpot_ms"),
            "l5_own": med(recs, "l5_own_ms"), "ctx": med(recs, "ctx_ms"),
            "l4_queue": med(recs, "l4_queue_ms"), "prefill": med(recs, "l4_prefill_ms"),
            "decode_tok": med(recs, "l4_decode_tok_ms"),
            "prompt_tokens": med(recs, "prompt_tokens"),
            "deferred": samp_mean(rows, label, "requests_deferred"),
            "stall": samp_mean(rows, label, "host_cpu_stall")}


def sig(base, cond, k):
    d = cond[k] - base[k]
    return d > FLOOR[k] and d > REL * abs(base[k]) if k not in ("deferred", "stall") else d > FLOOR[k]


def triage(base, cond):
    steps = []
    moved = [k for k in ("ttft", "tpot") if sig(base, cond, k)]
    steps.append(f"decompose: moved={moved or 'none'}")
    if not moved:
        return "none", "none", steps
    order = [("L5", "l5_own"), ("CTX", "ctx"), ("L4", "l4_queue"), ("L4", "prefill"), ("L4", "decode_tok")]
    cand = next(((loc, k) for loc, k in order if sig(base, cond, k)), None)
    steps.append(f"walk top-down: candidate={cand}")
    if cand is None:
        return "unattributed", "unattributed", steps
    loc, k = cand
    if loc in ("L5", "CTX"):
        return loc, loc, steps
    if sig(base, cond, "prompt_tokens"):
        steps.append("boundary state L5/L4: enriched-prompt tokens grew -> layer above")
        return "L5", "L4", steps
    steps.append("boundary state L5/L4 unchanged")
    if sig(base, cond, "deferred"):
        steps.append("engine: deferred requests rose -> L4 admission/capacity")
        return "L4", "L4", steps
    if sig(base, cond, "stall"):
        steps.append("device: host CPU stall rose, engine normal -> below L4")
        return "L2/L1", "L4", steps
    return "L3", "L4", steps


def recovered(base, iso, k):
    return not sig(base, iso, k)


# ---- main ---------------------------------------------------------------------------
STACK = None


def main():
    global STACK
    ap = argparse.ArgumentParser()
    ap.add_argument("--llama-dir", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    os.makedirs(RES, exist_ok=True)
    for f in ("requests.csv", "samples.csv", "spans.jsonl", "attribution.csv", "llama-server.log"):
        p = os.path.join(RES, f)
        if os.path.exists(p):
            os.remove(p)
    provider.add_span_processor(SimpleSpanProcessor(JsonlExporter(os.path.join(RES, "spans.jsonl"))))
    STACK = Stack(a.llama_dir, a.model, a.threads)
    sampler = Sampler()
    sampler.start()
    fcsv = open(os.path.join(RES, "requests.csv"), "w", newline="")
    w = csv.DictWriter(fcsv, fieldnames=FIELDS)
    w.writeheader()
    acsv = open(os.path.join(RES, "attribution.csv"), "w", newline="")
    aw = csv.DictWriter(acsv, fieldnames=["rep", "condition", "truth_root", "attributed_root",
                                          "attributed_manifestation", "correct", "isolation_test",
                                          "isolation_confirms", "steps", "base", "cond", "iso"])
    aw.writeheader()
    truth = {"none_control": "none", "ctx_delay": "CTX", "l5_history": "L5",
             "l4_slots": "L4", "host_contention": "L2/L1"}
    env = {"started": time.strftime("%Y-%m-%d %H:%M:%S %Z"), "cpu": open("/proc/cpuinfo").read().split("model name")[1].split("\n")[0].strip(": "),
           "nproc": os.cpu_count(), "mem_gb": round(os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2**30, 1),
           "kernel": platform.release(), "python": sys.version.split()[0], "model": os.path.basename(a.model),
           "llama_server_version": subprocess.run([os.path.join(a.llama_dir, "llama-server"), "--version"],
                                                  capture_output=True, text=True,
                                                  env=dict(os.environ, LD_LIBRARY_PATH=a.llama_dir)).stderr.strip(),
           "threads": a.threads, "reps": a.reps, "seed": a.seed, "N_REQ": N_REQ, "CONC": CONC,
           "N_PRED": N_PRED, "TOP_K": TOP_K, "CTX_DELAY_MS": CTX_DELAY_MS, "HOG_PROCS": HOG_PROCS, "ENGINE_CPUS": ENGINE_CPUS,
           "SLOTS_BASE": SLOTS_BASE, "SLOTS_FAULT": SLOTS_FAULT, "CTX_PER_SLOT": CTX_PER_SLOT,
           "REL": REL, "FLOOR": FLOOR}
    json.dump(env, open(os.path.join(RES, "env.json"), "w"), indent=2)
    try:
        STACK.start_ctx()
        STACK.start_llama(SLOTS_BASE)
        gw = Gateway()
        fixed = http_json(CTX_PORT, "GET", f"/search?q={quote('What is the rule for remote access?')}&k={TOP_K}")[0]["passages"]
        gw.fixed_passages = fixed
        rnd = random.Random(a.seed)
        for rep in range(a.reps):
            qs = corpus.questions(WARMUP + N_REQ, seed=a.seed + rep)
            base_recs = run_batch(gw, sampler, rep, "baseline", "measure", qs, CONC, w)
            base = summarize(base_recs, sampler.rows, f"{rep}|baseline|measure")
            micro_q = ["Summarise the policy on API keys."] * (WARMUP + 8)
            mr = run_batch(gw, sampler, rep, "baseline", "micro", micro_q, 1, w)
            MICRO[rep] = summarize(mr, sampler.rows, f"{rep}|baseline|micro")
            conds = list(truth)
            rnd.shuffle(conds)
            for c in conds:
                print(f"[rep {rep}] condition {c}", flush=True)
                # inject
                if c == "ctx_delay":
                    STACK.ctx_delay(CTX_DELAY_MS)
                elif c == "l5_history":
                    gw.history_policy = "full"
                elif c == "l4_slots":
                    STACK.start_llama(SLOTS_FAULT)
                elif c == "host_contention":
                    STACK.start_hog()
                recs = run_batch(gw, sampler, rep, c, "measure", qs, CONC, w)
                cond = summarize(recs, sampler.rows, f"{rep}|{c}|measure")
                root, manif, steps = triage(base, cond)
                # isolation test selected by the attribution (fault still active)
                iso_name, iso_ok, iso = "none", None, {}
                if root == "CTX":
                    iso_name = "replay with CTX bypassed (fixed passages)"
                    gw.ctx_mode = "bypass"
                    ir = run_batch(gw, sampler, rep, c, "isolation", qs, CONC, w)
                    gw.ctx_mode = "live"
                    iso = summarize(ir, sampler.rows, f"{rep}|{c}|isolation")
                    iso_ok = recovered(base, iso, "ttft")
                elif root == "L5":
                    iso_name = "replay with history truncated to summary"
                    saved, gw.history_policy = gw.history_policy, "summary"
                    ir = run_batch(gw, sampler, rep, c, "isolation", qs, CONC, w)
                    gw.history_policy = saved
                    iso = summarize(ir, sampler.rows, f"{rep}|{c}|isolation")
                    iso_ok = recovered(base, iso, "ttft")
                elif root == "L4":
                    iso_name = "replay at concurrency 1"
                    ir = run_batch(gw, sampler, rep, c, "isolation", qs, 1, w)
                    iso = summarize(ir, sampler.rows, f"{rep}|{c}|isolation")
                    iso_ok = recovered(base, iso, "l4_queue")
                elif root in ("L2/L1", "L3"):
                    iso_name = "single-request fixed-prompt micro-benchmark vs baseline micro"
                    ir = run_batch(gw, sampler, rep, c, "isolation", micro_q, 1, w)
                    iso = summarize(ir, sampler.rows, f"{rep}|{c}|isolation")
                    iso_ok = sig(summarize_micro(rep), iso, "decode_tok")
                # remove fault
                if c == "ctx_delay":
                    STACK.ctx_delay(0)
                elif c == "l5_history":
                    gw.history_policy = "summary"
                elif c == "l4_slots":
                    STACK.start_llama(SLOTS_BASE)
                elif c == "host_contention":
                    STACK.stop_hog()
                aw.writerow({"rep": rep, "condition": c, "truth_root": truth[c],
                             "attributed_root": root, "attributed_manifestation": manif,
                             "correct": root == truth[c], "isolation_test": iso_name,
                             "isolation_confirms": iso_ok, "steps": " | ".join(steps),
                             "base": json.dumps(base), "cond": json.dumps(cond), "iso": json.dumps(iso)})
                acsv.flush(); fcsv.flush()
                print(f"   truth={truth[c]} attributed={root} (manifest {manif}) iso={iso_name}:{iso_ok}", flush=True)
    finally:
        STACK.shutdown()
        sampler.stop_ev.set()
        with open(os.path.join(RES, "samples.csv"), "w", newline="") as f:
            sw = csv.DictWriter(f, fieldnames=list(sampler.rows[0].keys()) if sampler.rows else ["label"])
            sw.writeheader()
            sw.writerows(sampler.rows)
        env["finished"] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
        json.dump(env, open(os.path.join(RES, "env.json"), "w"), indent=2)


MICRO = {}


def summarize_micro(rep):
    return MICRO[rep]


if __name__ == "__main__":
    main()
