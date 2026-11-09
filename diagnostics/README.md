# **Diagnostics**

Practitioner material derived from the **Diagnostic & Troubleshooting Matrix** in [AOSI-RFC-0001 §7](../rfc/RFC-0001-AOSI-Model.md#7-diagnostic--troubleshooting-matrix): the "Wireshark for AI" method for isolating bottlenecks to a single AOSI layer.

**Planned contents** (contributions welcome via the `diagnostic-pattern` issue type; see [CONTRIBUTING.md](../CONTRIBUTING.md)):

| Planned item | Purpose |
|---|---|
| Layer runbooks (`L1`–`L7`) | Step-by-step isolation tests and remediations per layer |
| Telemetry mappings | Mapping of serving-engine metrics, OpenTelemetry spans and device counters (e.g., DCGM) to AOSI layers |
| `aosi.*` attribute profiles | Reference instrumentation for the attributes proposed in RFC-0001 Appendix B |
| Sample dashboards | TTFT/TPOT decomposition views joining L4 metrics with L1 device telemetry |

All thresholds in this directory are **illustrative** unless accompanied by reproducible evidence. Licensed under CC-BY-4.0, © Divyendu Bhatt.
