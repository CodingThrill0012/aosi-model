# Measured study: boundary-attributed diagnosis on a CPU-only stack

This folder holds a small, reproducible fault-injection study of the DAIRM diagnostic method (DAIRM-TR-0001 §7). It asks one narrow question:

> On a real, instrumented inference stack, does an automated version of the §7.5 triage, which uses only DAIRM spans, the L5/L4 boundary state and engine/host telemetry, attribute single injected faults to the layer or plane where they were injected?

It is **not** a validation of DAIRM in general. It runs on CPU only, so it cannot separate L3, L2 and L1, and it cannot test the memory-bandwidth discriminator of §7.3 (that needs GPUs with DCGM counters). See [Limitations](#limitations).

Measured results are in [`results/summary.md`](results/summary.md), generated from the raw files by `analyze.py`. Figures are in [`figures/`](figures/).

## Result in brief (3 repetitions, 24 measured requests per condition and repetition)

- The automated triage attributed the root cause correctly in **15 of 15** condition-repetitions: 12 of 12 injected faults and 3 of 3 no-fault controls. The isolation test it selected confirmed the attribution in 12 of 12 fault runs.
- In 6 of the 12 fault runs (all `l5_history` and all `host_contention` runs), the first span that moved was an L4 span (prefill or queue), although the fault was injected at L5 or below L4. Attributing by "the first span that grew" alone would have blamed L4 in those runs; the L5/L4 boundary-state check (prompt tokens: median 288 at baseline vs 1118 under `l5_history`) and the host stall signal moved the attribution to the injected location.
- Median TTFT (median over repetitions of per-repetition medians): baseline 1812 ms; CTX delay 2819 ms, with the CTX span at 1002 ms; L5 history 7038 ms; L4 slots 4132 ms, with L4 queue 3551 ms; engine-core contention 4459 ms, with TPOT 159.6 ms against 23.5 ms at baseline.
- Latency distributions have heavy tails under contention: the slowest single request in `host_contention` had a TTFT of about 111 s, and one `none_control` request about 9.7 s. The triage uses medians, so these outliers did not drive attributions, but they inflate means (`figures/decomposition.*` shows means, because means of the span components add up to the mean TTFT).

These numbers describe this setup only; see [Limitations](#limitations).

## Stack

| DAIRM location | Component in this study |
|---|---|
| L6 Application | Closed-loop client threads in `harness.py` (streaming consumer) |
| L5 Orchestration & Gateway | `Gateway` in `harness.py`: regex input guardrail, CTX call, ChatML template, conversation-history policy, token counting through the engine's `/tokenize` (a documented P3 coupling) |
| CTX Context Services | `ctx_service.py`: HTTP retrieval service with TF-IDF search over a synthetic policy corpus (`corpus.py`) |
| L4 Serving Engine | llama.cpp `llama-server` (release b12239), continuous batching over parallel slots, `/metrics` enabled |
| L3–L1 | llama.cpp CPU backend on the host CPU; not separable here |
| BUILD | `Qwen2.5-0.5B-Instruct` GGUF, Q4_K_M quantization |

Every request produces OpenTelemetry spans (`l6.request`, `l5.gateway`, `ctx.retrieve`, `l4.generate` with `l4.queue`, `l4.prefill` and `l4.decode` children) tagged with `dairm.layer`, `dairm.plane`, `dairm.data_state`, `dairm.l5.prompt_tokens_enriched`, `dairm.ctx.*`, `dairm.l4.queue_time` (seconds) and `gen_ai.operation.name` where it applies. Spans are written to `results/spans.jsonl`. Spans also carry `dairm.eval.condition` and `dairm.eval.rep`, study-only labels used for scoring; they are not proposed attributes, and the triage does not read spans. The L4 child spans are reconstructed from the timings that `llama-server` returns with each completion (`prompt_ms`, `predicted_ms`), and L4 queue time is derived as engine time-to-first-token minus `prompt_ms`.

A sampler records, every 0.25 s, host CPU busy fraction, the Linux PSI CPU "some" stall fraction (`/proc/pressure/cpu`), and the engine's `llamacpp:requests_processing` and `llamacpp:requests_deferred` gauges.

## Conditions

Each repetition measures a baseline, then runs these conditions in a seeded random order. Exactly one variable changes per condition.

| Condition | Injected at | What changes |
|---|---|---|
| `none_control` | none | Nothing (negative control) |
| `ctx_delay` | CTX | The retrieval service adds a fixed 1000 ms delay per call |
| `l5_history` | L5 | The gateway replays ten earlier conversation turns instead of a one-line summary |
| `l4_slots` | L4 | The engine restarts with 1 parallel slot instead of 4, at the same offered load and the same KV budget per slot |
| `host_contention` | L2/L1 (here: the CPU that executes the model) | Four busy-loop processes are pinned to the four engine cores |

The engine runs on CPUs 0–3; the client, gateway and CTX service run on CPUs 4–7 (`run_all.sh`), so the injected contention hits the execution hardware and not the upper layers.

## Triage (automated, thresholds fixed in code)

`triage()` in `harness.py` encodes TR §7.5 steps 2–5 against the same repetition's baseline. A metric "moved" if its median changed by more than 25% **and** by more than an absolute floor (`FLOOR`). The triage:

1. checks whether TTFT or TPOT moved; if neither, it reports no fault;
2. walks the spans top-down (L5 own time, CTX, L4 queue, prefill, decode per token) and takes the first that moved as the candidate;
3. if the candidate is at L4 or below, checks the L5/L4 boundary state: if enriched-prompt tokens grew, the root cause is attributed to L5 with manifestation at L4;
4. otherwise, if the engine's deferred-request gauge rose, attributes to L4; if host CPU stall rose, attributes below L4 (L2/L1); otherwise to L3.

It then runs the isolation test that the attribution selects, with the fault still active: CTX bypass with fixed passages; history truncated; concurrency 1; or a single-request fixed-prompt micro-benchmark compared with the baseline micro-benchmark. The triage never reads the condition label or the CTX service's injected-delay header; they are used only to score the result.

## Reproduce

```bash
# Dependencies (not committed): llama.cpp release b12239 and the model file
curl -LO https://github.com/ggml-org/llama.cpp/releases/download/b12239/llama-b12239-bin-ubuntu-x64.tar.gz
#   sha256 99441b638862cebe8b223079b02a7c8a650e2fd57048cd4379fbe769a014892d
curl -LO https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf
#   sha256 74a4da8c9fdbcd15bd1f6d01d621410d31c6fc00986f5eb687824e7b93d7a9db
python3 -m venv venv && venv/bin/pip install -r requirements.txt
LLAMA_DIR=/path/to/llama-b12239 MODEL=/path/to/qwen2.5-0.5b-instruct-q4_k_m.gguf PY=venv/bin/python ./run_all.sh 3
```

A full run of three repetitions took about 61 minutes on the machine below (2026-11-10, 06:54–07:55 IST). Timings vary between machines; attributions should not, if the method is robust, but that has only been checked on one machine.

## Environment of the reported run

Recorded automatically in `results/env.json`: a cloud VM with 8 vCPUs ("Intel(R) Xeon(R) Processor"), 15.6 GB RAM, Linux 6.12, Python 3.13.5, llama.cpp `llama-server` 0.9.0-dev (build 12239, commit 26d52b0f9), 4 engine threads, OpenTelemetry SDK 1.45.2. No GPU.

## Pilots and changes made before the reported run

Two short pilot runs (1 repetition each) were used to check the plumbing. Both used the same thresholds as the reported run; only workload parameters changed afterwards:

1. Pilot 1 (6 requests per condition, 32 output tokens, 3 passages, 400 ms CTX delay): the `l4_slots` fault was **missed**. With short outputs, serializing requests barely changed TTFT on CPU, because prefill already shared the CPU in the baseline. The output length was raised to 96 tokens and passages cut to 2, which makes queueing behind other requests' decode visible.
2. Pilot 2 (8 requests per condition, same as above with 96 tokens): the 400 ms `ctx_delay` fault was **missed** because TTFT rose 18%, under the 25% threshold, while baseline TTFT varied by roughly ±30% between batches. The injected delay was raised to 1000 ms. Pilot 2's raw records are kept in `pilot/` for transparency; pilot 1's were not kept.

Both changes make faults larger relative to noise; neither changes the triage logic or its thresholds. A reader should treat the reported accuracy as conditional on fault magnitudes that clear the noise floor.

## Limitations

- **CPU only; L3, L2 and L1 are one block.** The "L2/L1" fault is CPU contention on the cores that run the model, and the signal the triage uses for it (PSI CPU stall) is close to the injection mechanism itself. This checks the ordering logic of the procedure, not the discriminating power of real device counters.
- **The memory-bandwidth-bound decode discriminator and KV-cache pressure (§7.3) are not tested.** `llama-server` exposes no KV-usage or preemption metric, and the CPU has no DCGM-style DRAM counters. The L4 fault here is slot capacity (queueing), not KV-cache pressure.
- **Small and synthetic.** One model, one machine, a synthetic corpus, three repetitions, single faults of fixed size. Accuracy on combined or subtle faults is unknown.
- **The same author wrote the faults, the triage and the analysis.** Ground truth was known when the pilot changes were made. An independent replication with faults chosen by someone else would be stronger evidence.
- **It measures the procedure, not people.** Whether DAIRM helps practitioners diagnose faster (study 4 in the paper's evaluation plan) is untested.

## Files

| File | Content |
|---|---|
| `harness.py` | Stack control, L5 gateway, L6 client, sampler, fault injection, triage, isolation tests |
| `ctx_service.py`, `corpus.py` | CTX retrieval service and deterministic synthetic corpus |
| `analyze.py` | Builds `results/summary.md` and `figures/` from the raw results |
| `run_all.sh`, `requirements.txt` | Reproduction entry point and Python dependencies |
| `results/requests.csv` | One row per request: timings per span, token counts, engine timings |
| `results/samples.csv` | Telemetry samples (host CPU, PSI stall, engine gauges) |
| `results/spans.jsonl.gz` | OpenTelemetry spans with `dairm.*` attributes (the harness writes `spans.jsonl`; it was gzipped for the repository) |
| `results/attribution.csv` | Per condition and repetition: injected location, triage result and steps, isolation test outcome |
| `results/env.json`, `results/llama-server.log` | Environment record and engine log |
| `pilot/` | Pilot 2 raw records |

Licensed under CC-BY-4.0 (text and data) like the rest of the repository; © 2026 Divyendu Bhatt.
