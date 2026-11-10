"""Summarise the DAIRM fault-injection study (results/ -> figures/ and results/summary.md).

Reads only files written by harness.py. Every number in summary.md is computed
here from those files; nothing is typed in by hand.
"""
import csv
import json
import statistics as st
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
RES = HERE / "results"
FIG = HERE / "figures"
ORDER = ["none_control", "ctx_delay", "l5_history", "l4_slots", "host_contention"]
LABEL = {"none_control": "No fault\n(control)", "ctx_delay": "CTX delay", "l5_history": "L5 history\ngrowth",
         "l4_slots": "L4 slots\n4 -> 1", "host_contention": "Engine-core\ncontention", "baseline": "Baseline"}
ROOTS = ["none", "CTX", "L5", "L4", "L3", "L2/L1"]


def load_requests():
    with open(RES / "requests.csv") as f:
        return list(csv.DictReader(f))


def load_attr():
    with open(RES / "attribution.csv") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in ("base", "cond", "iso"):
            r[k] = json.loads(r[k]) if r[k] else {}
    return rows


def med(xs):
    return st.median(xs) if xs else float("nan")


def main():
    FIG.mkdir(exist_ok=True)
    reqs = load_requests()
    attr = load_attr()
    env = json.loads((RES / "env.json").read_text())
    reps = sorted({int(r["rep"]) for r in attr})

    # Per (condition, rep) medians of the measured phase; baseline per rep.
    by = defaultdict(list)
    for r in reqs:
        if r["phase"] == "measure":
            by[(r["condition"], int(r["rep"]))].append(r)
    cols = ["ttft_ms", "tpot_ms", "l5_own_ms", "ctx_ms", "l4_queue_ms", "l4_prefill_ms", "l4_decode_tok_ms",
            "prompt_tokens", "e2e_ms"]
    per = {}
    for (c, rep), rs in by.items():
        per[(c, rep)] = {k: med([float(x[k]) for x in rs]) for k in cols} | {"n": len(rs)}

    def agg(c, k):
        vals = [per[(c, rep)][k] for rep in reps if (c, rep) in per]
        return med(vals), (min(vals) if vals else float("nan")), (max(vals) if vals else float("nan"))

    # Figure 1: TTFT decomposition. Means are used for the stack because means of
    # components add up to the mean total, whereas medians do not; TPOT panel uses
    # the median over reps of per-rep medians, with the range over reps.
    pooled = defaultdict(list)
    for (c, rep), rs in by.items():
        pooled[c].extend(rs)

    def mean(c, k):
        return st.mean(float(x[k]) for x in pooled[c])
    conds = ["baseline"] + ORDER
    parts = [("l5_own_ms", "L5 gateway (own)", "#2F6DB5"), ("ctx_ms", "CTX retrieval", "#2E9C8F"),
             ("l4_queue_ms", "L4 queue", "#4E9F3D"), ("l4_prefill_ms", "Prefill (L3-L1)", "#C98A14")]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [2.2, 1]})
    x = range(len(conds))
    bottom = [0.0] * len(conds)
    for k, lab, col in parts:
        v = [mean(c, k) / 1000 for c in conds]
        ax1.bar(x, v, bottom=bottom, color=col, label=lab, width=0.65)
        bottom = [b + vi for b, vi in zip(bottom, v)]
    ax1.plot(list(x), [mean(c, "ttft_ms") / 1000 for c in conds], "k_", markersize=22, mew=2,
             label="Client TTFT (mean)")
    ax1.set_xticks(list(x), [LABEL[c] for c in conds], fontsize=8)
    ax1.set_ylabel("seconds")
    ax1.set_title("Mean TTFT and its span decomposition (all requests, 3 reps)", fontsize=10)
    ax1.legend(fontsize=7, loc="upper left")
    tp = [agg(c, "tpot_ms") for c in conds]
    ax2.bar(x, [t[0] for t in tp], color="#6B7785", width=0.65,
            yerr=[[t[0] - t[1] for t in tp], [t[2] - t[0] for t in tp]], capsize=4)
    ax2.set_xticks(list(x), [LABEL[c].replace("\n", " ") for c in conds], fontsize=7, rotation=40, ha="right")
    ax2.set_ylabel("ms per output token")
    ax2.set_title("Median TPOT (range over reps)", fontsize=10)
    fig.suptitle(f"DAIRM CPU study: {len(reps)} reps x {env['N_REQ']} requests per condition "
                 f"(Qwen2.5-0.5B Q4_K_M, llama.cpp b12239, {env['threads']} engine threads)", fontsize=9)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(FIG / f"decomposition.{ext}", dpi=160)
    plt.close(fig)

    # Figure 2: attribution confusion matrix.
    truths = [t for t in ROOTS if any(a["truth_root"] == t for a in attr)]
    preds = ROOTS
    M = [[sum(1 for a in attr if a["truth_root"] == t and a["attributed_root"] == p) for p in preds] for t in truths]
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.imshow(M, cmap="Blues")
    for i, row in enumerate(M):
        for j, v in enumerate(row):
            ax.text(j, i, str(v), ha="center", va="center", color="white" if v > max(map(max, M)) / 2 else "black")
    ax.set_xticks(range(len(preds)), preds)
    ax.set_yticks(range(len(truths)), truths)
    ax.set_xlabel("Root-cause layer attributed by the automated triage")
    ax.set_ylabel("Injected fault (ground truth)")
    ax.set_title("Attribution outcomes (one cell count = one rep)", fontsize=9)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(FIG / f"attribution.{ext}", dpi=160)
    plt.close(fig)

    # summary.md
    L = []
    L.append("# DAIRM CPU fault-injection study: measured results\n")
    L.append("Generated by `analyze.py` from `results/`. Do not edit by hand.\n")
    L.append(f"- Started: {env['started']}; host: {env['cpu'].strip(': \t')}, {env['nproc']} vCPU, "
             f"{env['mem_gb']} GB RAM, Linux {env['kernel']}, Python {env['python']}")
    L.append(f"- Engine: {env['llama_server_version'].splitlines()[0]}; model {env['model']}; "
             f"{env['threads']} threads pinned to CPUs {env['ENGINE_CPUS']}")
    L.append(f"- Design: {len(reps)} reps x {len(ORDER)} conditions (+ baseline per rep), {env['N_REQ']} measured "
             f"requests per condition at closed-loop concurrency {env['CONC']}, {env['N_PRED']} output tokens each")
    L.append(f"- Thresholds fixed before the main run: relative change > {env['REL']:.0%} and absolute floors {env['FLOOR']}\n")
    correct = sum(1 for a in attr if a["correct"] == "True")
    faults = [a for a in attr if a["truth_root"] != "none"]
    iso_ok = sum(1 for a in faults if a["isolation_confirms"] == "True")
    L.append(f"**Root-cause attribution correct in {correct} of {len(attr)} condition-reps** "
             f"({sum(1 for a in faults if a['correct'] == 'True')} of {len(faults)} injected faults; "
             f"{sum(1 for a in attr if a['truth_root'] == 'none' and a['correct'] == 'True')} of "
             f"{sum(1 for a in attr if a['truth_root'] == 'none')} no-fault controls). "
             f"The isolation test confirmed the attribution in {iso_ok} of {len(faults)} fault runs.\n")
    L.append("## Attribution per condition and rep\n")
    L.append("| Rep | Condition | Injected at | Attributed root | Manifestation | Correct | Isolation test | Confirms |")
    L.append("|---|---|---|---|---|---|---|---|")
    for a in sorted(attr, key=lambda a: (int(a["rep"]), ORDER.index(a["condition"]))):
        L.append(f"| {a['rep']} | {a['condition']} | {a['truth_root']} | {a['attributed_root']} | "
                 f"{a['attributed_manifestation']} | {a['correct']} | {a['isolation_test']} | {a['isolation_confirms']} |")
    L.append("\n## Median metrics per condition (median over reps of per-rep medians; [min, max] over reps)\n")
    L.append("| Condition | TTFT ms | TPOT ms | L5 own ms | CTX ms | L4 queue ms | Prefill ms | Prompt tokens |")
    L.append("|---|---|---|---|---|---|---|---|")
    for c in conds:
        cells = []
        for k in ["ttft_ms", "tpot_ms", "l5_own_ms", "ctx_ms", "l4_queue_ms", "l4_prefill_ms", "prompt_tokens"]:
            m, lo, hi = agg(c, k)
            cells.append(f"{m:.0f} [{lo:.0f}, {hi:.0f}]" if k != "tpot_ms" else f"{m:.1f} [{lo:.1f}, {hi:.1f}]")
        L.append(f"| {c} | " + " | ".join(cells) + " |")
    L.append("\n## Triage trace per condition-rep\n")
    for a in sorted(attr, key=lambda a: (int(a["rep"]), ORDER.index(a["condition"]))):
        L.append(f"- rep {a['rep']} {a['condition']}: {a['steps']}")
    (RES / "summary.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:12]))


if __name__ == "__main__":
    main()
