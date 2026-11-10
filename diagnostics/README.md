# Diagnostics

Practitioner material derived from the **diagnostic method** in [DAIRM-TR-0001 §7](../docs/DAIRM-TR-0001.md#7-diagnostic-method): boundary-attributed tracing, latency decomposition, and isolation tests that attribute a symptom to one DAIRM layer (L1–L6) or plane (Context Services, Build/Deploy, Management).

A small, measured CPU-only study of the §7.5 triage procedure is in [`../eval/`](../eval/README.md) (DAIRM-TR-0001 §7.6).

**Planned contents** (contributions welcome through the `diagnostic-pattern` issue type; see [CONTRIBUTING.md](../CONTRIBUTING.md)):

| Planned item | Purpose |
|---|---|
| Runbooks per layer and plane (`L1`–`L6`, `CTX`, `BUILD`) | Step-by-step isolation tests and remediations |
| Telemetry mappings | Mapping of serving-engine metrics (e.g., vLLM `vllm:kv_cache_usage_perc`), OpenTelemetry spans and device counters (e.g., DCGM, with the DCGM version pinned) to DAIRM layers and planes |
| `dairm.*` attribute profiles | Reference instrumentation for the attributes in DAIRM-TR-0001 Appendix B, including `dairm.layer`, `dairm.plane`, `dairm.data_state` and `dairm.ctx.*` |
| Sample dashboards | TTFT/TPOT decomposition views joining L4 metrics with L1 device telemetry, with Context Services spans shown separately |
| GPU case study | A vLLM + RAG deployment on GPUs with injected faults (slow retrieval, KV-cache pressure, bandwidth-bound decode) to test DAIRM-TR-0001 §7.3 (see §9 item 5) |

All thresholds in this directory are **illustrative** unless accompanied by reproducible evidence. Licensed under CC-BY-4.0, © 2026 Divyendu Bhatt.
