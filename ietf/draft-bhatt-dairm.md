---
title: "DAIRM: Divyendu's Data-State-Aware AI Reference Model for Generative AI Inference Systems"
abbrev: "DAIRM"
docname: draft-bhatt-dairm-00
category: info
submissiontype: independent
ipr: trust200902
date: 2026-11-09
v: 3
keyword:
  - generative AI
  - reference model
  - inference serving
  - observability
  - data state

stand_alone: yes
pi: [toc, sortrefs, symrefs]

author:
  -
    ins: D. Bhatt
    name: Divyendu Bhatt
    email: Divyendu.bhatt@gmail.com

informative:
  DAIRM-TR-0001:
    title: "DAIRM-TR-0001: DAIRM: Divyendu's Data-State-Aware AI Reference Model for Generative AI Inference Systems, Version 2.0.0"
    author:
      fullname: Divyendu Bhatt
    date: 2026-11
    seriesinfo:
      DOI: 10.5281/zenodo.24073121
    target: https://github.com/CodingThrill0012/dairm
  AOSI-V121:
    title: "AOSI-RFC-0001: The AI Open Systems Interconnection (AOSI) Reference Model: A 7-Layer Stack for Generative AI Execution, Version 1.2.1 (superseded by DAIRM-TR-0001 Version 2.0.0; 'RFC' was a project label, not an IETF RFC)"
    author:
      fullname: Divyendu Bhatt
    date: 2026-11-09
    seriesinfo:
      DOI: 10.5281/zenodo.24073122
    target: https://doi.org/10.5281/zenodo.24073122
  ISO7498-1:
    title: "Information technology - Open Systems Interconnection - Basic Reference Model: The Basic Model"
    author:
      org: ISO/IEC
    date: 1994
    seriesinfo:
      ISO/IEC: 7498-1:1994
    target: https://www.iso.org/standard/20269.html
  X.200:
    title: "Information technology - Open Systems Interconnection - Basic Reference Model: The basic model"
    author:
      org: ITU-T
    date: 1994-07
    seriesinfo:
      ITU-T Recommendation: X.200
    target: https://www.itu.int/rec/T-REC-X.200-199407-I/en
  ISO22989:
    title: "Information technology - Artificial intelligence - Artificial intelligence concepts and terminology"
    author:
      org: ISO/IEC
    date: 2022
    seriesinfo:
      ISO/IEC: 22989:2022
    target: https://www.iso.org/standard/74296.html
  ISO23053:
    title: "Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML)"
    author:
      org: ISO/IEC
    date: 2022
    seriesinfo:
      ISO/IEC: 23053:2022
    target: https://www.iso.org/standard/74438.html
  NIST-AI-RMF:
    title: "Artificial Intelligence Risk Management Framework (AI RMF 1.0)"
    author:
      org: National Institute of Standards and Technology
    date: 2023-01
    seriesinfo:
      NIST: AI 100-1
      DOI: 10.6028/NIST.AI.100-1
    target: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
  NIST-AI-600-1:
    title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile"
    author:
      org: National Institute of Standards and Technology
    date: 2024-07
    seriesinfo:
      NIST: AI 600-1
      DOI: 10.6028/NIST.AI.600-1
    target: https://doi.org/10.6028/NIST.AI.600-1
  NIST-AML:
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations"
    author:
      org: National Institute of Standards and Technology
    date: 2025
    seriesinfo:
      NIST: AI 100-2 E2025
    target: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
  A16Z-LLM:
    title: "Emerging Architectures for LLM Applications"
    author:
      -
        fullname: Matt Bornstein
      -
        fullname: Rajko Radovanovic
    date: 2023-06-20
    target: https://a16z.com/emerging-architectures-for-llm-applications/
  GOOGLE-MLOPS:
    title: "MLOps: Continuous delivery and automation pipelines in machine learning"
    author:
      org: Google Cloud
    date: false
    target: https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
  MLPERF-INF:
    title: "MLPerf Inference: Datacenter"
    author:
      org: MLCommons
    date: false
    target: https://mlcommons.org/benchmarks/inference-datacenter/
  PAGEDATTENTION:
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    author:
      -
        fullname: Woosuk Kwon
      -
        fullname: et al.
    date: 2023-10
    seriesinfo:
      DOI: 10.1145/3600006.3613165
      arXiv: "2309.06180"
    target: https://arxiv.org/abs/2309.06180
  ROOFLINE:
    title: "LLM Inference Unveiled: Survey and Roofline Model Insights"
    author:
      -
        fullname: Zhihang Yuan
      -
        fullname: et al.
    date: 2024
    seriesinfo:
      arXiv: "2402.16363"
    target: https://arxiv.org/abs/2402.16363
  OWASP-LLM:
    title: "OWASP Top 10 for LLM Applications 2025"
    author:
      org: OWASP GenAI Security Project
    date: 2024-11
    target: https://genai.owasp.org/llm-top-10/
  MITRE-ATLAS:
    title: "ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems"
    author:
      org: The MITRE Corporation
    date: false
    target: https://atlas.mitre.org/
  SAIF:
    title: "Secure AI Framework (SAIF)"
    author:
      org: Google
    date: false
    target: https://saif.google/
  ACE:
    title: "Conceptual Framework for Autonomous Cognitive Entities"
    author:
      -
        fullname: David Shapiro
      -
        fullname: et al.
    date: 2023-10
    seriesinfo:
      arXiv: "2310.06775"
    target: https://arxiv.org/abs/2310.06775
  OSI-AGENTIC:
    title: "Toward an OSI-Inspired Stack for Agentic AI: From Fragmented Frameworks to Open Standards"
    author:
      fullname: Francisco-Javier Rodrigo-Gines
    date: 2025-09
    seriesinfo:
      DOI: 10.5281/zenodo.17099409
    target: https://doi.org/10.5281/zenodo.17099409
  REILLY-AOSI:
    title: "AOSI Reference Model for Artificial Intelligence (AOSI = AI Open Systems Interconnection), version 1.0"
    author:
      fullname: Shawn Reilly
    date: 2025-12-28
    target: https://github.com/kahalewai/aosi
  LIANG:
    title: "AI Compute Architecture and Evolution Trends"
    author:
      fullname: Bor-Sung Liang
    date: 2025-08
    seriesinfo:
      arXiv: "2508.21394"
    target: https://arxiv.org/abs/2508.21394
  IOA-LAYERS:
    title: "A Layered Protocol Architecture for the Internet of Agents"
    author:
      -
        fullname: Charles Fleming
      -
        fullname: Luca Muscariello
      -
        fullname: Vijoy Pandey
      -
        fullname: Ramana Kompella
    date: 2025-11
    seriesinfo:
      arXiv: "2511.19699"
    target: https://arxiv.org/abs/2511.19699
  MAESTRO:
    title: "Agentic AI Threat Modeling Framework: MAESTRO"
    author:
      fullname: Ken Huang
    date: 2025-02-06
    target: https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro
  CHANDER:
    title: "How LLMs Actually Work: A Seven-Layer Map"
    author:
      fullname: C. P. Chander
    date: 2026-09-19
    target: https://cpchander.com/blog/how-llms-work-seven-layer-map
  AI-LAYER-MODEL:
    title: "The AI Layer Model: a shared map for AI systems"
    author:
      fullname: Logan Smith
    date: 2026-10-20
    target: https://logansmith.us/post-ai-layer-model.html
  AILIS:
    title: "AILIS: A Proposed Layer Model for AI Systems, Version 0.2.0"
    author:
      fullname: Mick Darling
      org: Dollhouse Research
    date: 2025
    target: https://ailis.dollhouseresearch.com/
  TSAIH:
    title: "The AI Tech-Stack Model"
    author:
      -
        fullname: Rua-Huan Tsaih
      -
        fullname: Hsin-Lu Chang
      -
        fullname: Chih-Chun Hsu
      -
        fullname: David C. Yen
    date: 2023-03
    seriesinfo:
      DOI: 10.1145/3568026
      "Communications of the ACM": "66(3), 69-77"
  ZHANG-LAYERED:
    title: "A Layered Architecture for Developing and Enhancing Capabilities in Large Language Model-based Software Systems"
    author:
      -
        fullname: Dawen Zhang
      -
        fullname: Xiwei Xu
      -
        fullname: Chen Wang
      -
        fullname: Zhenchang Xing
      -
        fullname: Robert Mao
    date: 2024-11
    seriesinfo:
      arXiv: "2411.12357"
    target: https://arxiv.org/abs/2411.12357
  BUCAIONI:
    title: "A Functional Software Reference Architecture for LLM-Integrated Systems"
    author:
      -
        fullname: Alessio Bucaioni
      -
        fullname: et al.
    date: 2025
    seriesinfo:
      arXiv: "2501.12904"
    target: https://arxiv.org/abs/2501.12904
  GRESHAKE:
    title: "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"
    author:
      -
        fullname: Kai Greshake
      -
        fullname: et al.
    date: 2023
    seriesinfo:
      arXiv: "2302.12173"
    target: https://arxiv.org/abs/2302.12173
  EMB-INVERSION:
    title: "Text Embeddings Reveal (Almost) As Much As Text"
    author:
      -
        fullname: John X. Morris
      -
        fullname: et al.
    date: 2023
    seriesinfo:
      arXiv: "2310.06816"
    target: https://arxiv.org/abs/2310.06816
  TIMING-SC:
    title: "The Early Bird Catches the Leak: Unveiling Timing Side Channels in LLM Serving Systems"
    author:
      -
        fullname: Linke Song
      -
        fullname: et al.
    date: 2024
    seriesinfo:
      arXiv: "2409.20002"
    target: https://arxiv.org/abs/2409.20002
  TRACE-CONTEXT:
    title: "Trace Context"
    author:
      org: W3C
    date: 2021-11-23
    target: https://www.w3.org/TR/trace-context/
  OTEL-GENAI:
    title: "Semantic conventions for generative AI"
    author:
      org: OpenTelemetry
    date: false
    target: https://github.com/open-telemetry/semantic-conventions-genai
  VLLM-METRICS:
    title: "vLLM Metrics"
    author:
      org: vLLM project
    date: false
    target: https://docs.vllm.ai/en/latest/usage/metrics.html
  DCGM-FIELDS:
    title: "DCGM API: Field IDs"
    author:
      org: NVIDIA
    date: false
    target: https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html

--- abstract

A generative AI request passes through a client application, an
orchestration gateway, context services such as retrieval and tools,
an inference-serving engine, a model-execution runtime, device
drivers, and accelerator hardware.  Each tier has its own tools,
telemetry, and vocabulary, and it is often hard to say where a
latency regression, a quality failure, or a security threat
originates.

This document describes DAIRM (Divyendu's Data-State-Aware AI
Reference Model), an informational reference model for the request
path of generative AI inference serving.  DAIRM defines a six-layer
request path with three planes beside it (Context Services,
Build/Deploy, and Management); a named, observable data state at
every boundary of that path; and a boundary-attributed diagnostic
method, with a set of proposed telemetry attributes, that separates
context-service delay, serving-engine queueing or KV-cache pressure,
and memory-bandwidth-bound decode.  DAIRM does not claim the
layered-stack idea or the OSI analogy as new; earlier OSI-inspired
models for AI are acknowledged.  The model defines no protocol.

--- middle

# Introduction

## The Problem

Serving one generative request involves several engineering
disciplines that are usually separated by team (application,
platform, machine learning, and infrastructure), by tooling
(application performance monitoring, MLOps dashboards, accelerator
profilers, and data-centre monitoring), and by vocabulary ("prompt",
"batch", "graph", "kernel", "rail").  This causes four recurring
problems:

1. Non-attributable performance: end-to-end latency is the sum of
   gateway work, context-service calls, queueing, prefill, decode,
   kernel execution, and memory transfer.  Without a decomposition, a
   regression in one tier shows up only as an aggregate symptom
   somewhere else.

2. Implicit contracts: what a "prompt" contains when it reaches the
   serving engine, what a "batch" hands to the runtime, and what the
   runtime hands to the device are defined by individual products,
   not by a stable reference.

3. Mis-located controls: security and governance controls are often
   specified as generic "AI controls" without stating the tier at
   which a threat materializes.

4. Non-transferable expertise: engineers lack a common frame for
   saying where a behavior originates, which slows incident response
   and design review.

## Contributions

Layered reference models such as the OSI Basic Reference Model
{{ISO7498-1}} {{X.200}} showed the value of ordered layers with
service boundaries and named data units.  DAIRM borrows that method,
not the OSI layers, and applies it to generative AI inference.  It
does not claim the layered-stack idea, the number of layers, or the
OSI analogy as new ({{related}}).  Its contributions are limited to
three items:

1. A named, observable data state at every boundary of the inference
   request path ({{states}}).  Each state can be captured or
   measured.  Above the serving engine a state is scoped to one
   request; from the serving engine down, where batching mixes
   requests, it is scoped to one scheduler step or device and is
   joined to its requests through a step identifier.  This makes
   each boundary a checkpoint for attributing cause.

2. A boundary-attributed latency diagnostic method ({{diag}}) that
   separates context-service delay, serving-engine queueing or
   KV-cache pressure, and memory-bandwidth-bound decode, using a
   latency decomposition, per-layer trace attribution, and
   single-variable isolation tests.

3. A layer-indexed set of proposed telemetry attributes ("dairm.*",
   {{attrs}}) that makes the method executable on distributed traces
   and is designed to sit alongside the OpenTelemetry semantic
   conventions for generative AI {{OTEL-GENAI}}.

The per-layer security mapping ({{security}}) is included as useful
content, not as a claim of novelty; per-layer threat mapping already
exists, for example in CSA MAESTRO {{MAESTRO}}.

This document is derived from the technical report DAIRM-TR-0001,
Version 2.0.0 {{DAIRM-TR-0001}}, by the same author; see
{{provenance}}.

## Scope and Non-Goals

In scope: the request path of generative AI inference serving, from
the client request to the hardware execution of each token, and back
as a streamed response.  DAIRM targets autoregressive transformer
language models first, and multimodal models by extension.

Out of scope:

* Training, fine-tuning, data pipelines, evaluation, and the model
  registry.  They enter DAIRM only through the Build/Deploy plane
  ({{build}}), as artifacts that the request path loads and executes.

* Cluster and resource orchestration, operating systems,
  virtualization, and containers.  These are named in the Management
  plane but not detailed.

* The network between the client and the gateway, which is treated
  as transport for the L6/L5 boundary; its internals are the domain
  of the OSI model and of IETF protocols.

* Any wire protocol, API schema, or certification regime.

* Endorsement of any product.  Named technologies are illustrative
  examples of components that occupy a layer or plane.

# Terminology

This document defines no protocol and does not use the requirement
key words of BCP 14.  {{alignment}} lists what a description of a
system contains when it is called "DAIRM-aligned".

Layer (Ln):
: A tier of the request path, from L1 (closest to hardware) to L6
  (closest to the user).  Every request that reaches model execution
  passes through every layer; a request answered from a cache or
  rejected at L5 stops early.

Plane:
: A set of functions beside the request path.  Planes are called by,
  or supply, layers but are not themselves on the path.  DAIRM has
  three: Context Services (CTX), Build/Deploy (BUILD), and
  Management (MGMT).

Boundary:
: The interface between two adjacent layers, written L5/L4, or
  between a layer and a plane, written CTX/L5.

Data state:
: The representation of a request or response as it crosses a
  boundary.  It can be captured or measured at a stated scope: per
  request (L6/L5, CTX/L5, L5/L4, and the up-path), per scheduler step
  (L4/L3 and L3/L2), or per device and sampling interval (L2/L1).
  Step- and device-scoped states are shared by the requests batched
  together and are joined to them by "dairm.l4.step_id" and
  "dairm.device_id".

Resident state:
: Per-request state held in device memory across steps rather than
  handed between layers: activations (hidden states) and the KV
  cache.

Artifact:
: A build-time or deploy-time product loaded by the request path:
  weights, model architecture and configuration, tokenizer and chat
  template, compiled graph or kernel intermediate representation
  (IR), kernels, and engine plans.

Down-path and up-path:
: Request processing from L6 toward L1, and result processing from
  L1 toward L6.

Prefill:
: The forward pass over all prompt tokens that fills the KV cache and
  produces the first logits.  Typically compute-bound.

Decode:
: The forward passes after prefill, one token per step (or several
  with speculative decoding).  Usually memory-bandwidth-bound at the
  batch sizes common in serving, because each step reads the weights
  and the KV cache for little arithmetic {{ROOFLINE}}.

KV cache:
: Per-sequence storage of attention keys and values for prior tokens,
  managed by L4 and resident in device memory.

TTFT:
: Time to first token: from request receipt to the first output token
  delivered to the client.

TPOT and ITL:
: Time per output token (TPOT) is the mean decode time per output
  token of one request, (E2E - TTFT) / (N_out - 1).  Inter-token
  latency (ITL) is the distribution of individual gaps between
  successive output tokens, which exposes stalls that a mean hides.

Goodput:
: Throughput of requests that meet their latency objectives.

Span:
: A unit of traced work in a distributed trace.  DAIRM-aligned
  tracing attributes each span to exactly one layer or plane.

Provider boundary:
: The boundary below which a consumer of a hosted model API cannot
  observe the system ({{provider}}).

# Design Principles

P1 Single responsibility per layer:
: Each layer has one primary function.  A product that spans layers
  (for example, a serving engine with its own kernels) is described
  once for each layer it occupies.

P2 Named, observable data state at every boundary:
: Every boundary has a defined data state that can be captured,
  inspected, or measured, per request or, where the serving engine
  batches requests, per scheduler step or device, and that can be
  joined to the requests it served.  Metaphors and build-time
  artifacts do not qualify.

P3 Adjacency of interfaces:
: A layer interacts with its immediate neighbors and with the
  planes.  Any other shortcut (for example, an application pinning a
  device, or orchestration pre-tokenizing for budgeting) is
  documented as an explicit cross-layer coupling.

P4 Observability by construction:
: Each layer and plane emits telemetry at its boundaries that is
  attributable to it, so that the method in {{diag}} can be applied.

P5 Technology neutrality:
: Layer definitions do not depend on a vendor, framework, or
  accelerator.

P6 Where cost and latency sit:
: Compute, data movement, and energy concentrate in the lower layers.
  Semantic and policy complexity concentrate in the upper layers.
  Latency can originate at any layer, so it is attributed per
  boundary, not assumed.

P7 Security at the point of materialization:
: Controls are placed at the layer or plane where a threat
  materializes, with defense in depth elsewhere where justified.

# Architecture Overview {#arch}

## Request Path and Planes

~~~ ascii-art
 +------------------------------------+
 | L6 Application                     |
 | client, UX, streaming render       |
 +------------------------------------+
       |
       v request payload
 +------------------------------------+     +----------------------+
 | L5 Orchestration & Gateway         |     | Context Services     |
 | auth, policy, guardrails,          |<--->| (CTX): retrieval,    |
 | templates, routing, agent loop     |     | vector DB, tools     |
 +------------------------------------+     +----------------------+
       |
       v enriched prompt
 +------------------------------------+     +----------------------+
 | L4 Serving Engine                  |     | Build/Deploy (BUILD) |
 | admission, scheduling, batching,   |<....| weights, tokenizer,  |
 | KV cache, tokenize, sample         |     | graph IR (to L4, L3) |
 +------------------------------------+     +----------------------+
       |
       v token-ID batch + KV block table
 +------------------------------------+
 | L3 Model Execution Runtime         |
 | framework, kernels, collectives    |
 +------------------------------------+
       |
       v kernel launch stream
 +------------------------------------+     +----------------------+
 | L2 Device & Driver                 |     | Management (MGMT)    |
 | driver, allocator, launch, streams |.....| placement, scaling   |
 +------------------------------------+     +----------------------+
       |
       v device instr. & memory transactions
 +------------------------------------+
 | L1 Physical Compute & Interconnect |
 | accelerator, HBM, links, power     |
 +------------------------------------+

 <--->  call and return (L5/CTX).  <.... and ..... : artifacts
        and management, which are not per-request data.
 Up-path: logits -> sampled token IDs -> text deltas -> chunks.
~~~
{: #fig-arch title="The DAIRM request path and planes"}

L2 and L1 are kept separate because the diagnostics distinguish
driver and runtime faults (for example, device error events, launch
overhead, and allocator fragmentation) from physical limits (memory
bandwidth ceilings, clock-event reasons, and thermal and power
capping).

## Boundary Data States {#states}

This is the core of DAIRM.  Each state can be captured or measured
at the scope given below.  Request-scoped states belong to one
request.  Step-scoped states (L4/L3 and L3/L2) describe one scheduler
iteration that serves every request in the batch, and the
device-scoped state (L2/L1) is sampled per device and interval; both
are joined to requests through "dairm.l4.step_id" and
"dairm.device_id".  Caches can end the path early: a gateway
response cache answers at L5, and a prefix-cache hit at L4 skips
part of prefill, so not every request produces every state.  The
value in parentheses is the proposed "dairm.data_state" attribute
value ({{attrs}}).

L6 -> L5: Request payload ("request_payload"):
: JSON or HTTP request with messages, tools, sampling parameters, and
  stream flag.  Scope: request.  Observable as request body, size,
  and schema validity.

CTX -> L5: Retrieved passages ("retrieved_passages"):
: Text with scores and provenance, or tool results.  The query
  embedding stays inside the context service.  Scope: request.
  Observable as passage count, tokens contributed, and source
  identifiers.

L5 -> L4: Enriched prompt ("enriched_prompt"):
: Templated messages or text, tool schemas, sampling parameters, and
  priority.  Scope: request.  Observable as prompt tokens after
  enrichment.

L4 -> L3: Token-ID batch + block table ("token_batch"):
: The scheduled batch plus its KV-cache block table: token IDs,
  positions, and sequence-to-block mappings.  Scope: scheduler step.
  Observable as batch size, tokens per step, and KV blocks used.

L3 -> L2: Kernel launch stream ("kernel_stream"):
: Operator and kernel invocations with tensor arguments.  Scope:
  scheduler step.  Observable as kernel traces and launch counts.

L2 -> L1: Device instruction stream ("device_stream"):
: The device instruction and memory-transaction stream.  Scope:
  device, per sampling interval.  Observable only through hardware
  counters: compute and tensor-pipe activity, device-memory bytes,
  and link bytes.

Up-path: Token stream ("token_stream"):
: Logits, then sampled token IDs, then detokenized text deltas, then
  streamed response chunks.  Scope: request.  Observable as
  inter-token latency and stream events.

Resident state:
: Hidden states (activations) and the KV cache are resident
  device-memory state.  They are not messages handed from one layer
  to another; they are produced and consumed in place by L3 kernels
  executing on L1, under the block management of L4.

Artifacts are not data states:
: Weights, model architecture, tokenizer, chat template, and compiled
  graph or kernel IR are produced at build, compile, or warm-up time
  (BUILD) and loaded by L4 and L3.  They are drawn beside the path,
  not on it.

Two properties make these states useful.  First, each has a
measurable size that propagates downward: enriched-prompt tokens at
L5/L4 determine prefill work below, passages contributed at CTX/L5
determine part of that count, and batch composition at L4/L3
determines the arithmetic intensity seen at L1.  Second, each is a
checkpoint for blame, used as a heuristic rather than a rule: if the
state entering a layer is unchanged and the span of that layer grew,
that layer is the first suspect; if the incoming state changed, the
layer above is suspected.  Contention from co-located work, or a
degraded lower layer, can lengthen a span while its input stays the
same, so the heuristic is always followed by lower-layer checks and
an isolation test ({{triage}}).

## Planes {#planes}

Context Services (CTX):
: Called by L5 with a query and returning retrieved passages or tool
  results with scores and provenance.  Retrieval keeps its own spans,
  metrics, and diagnostics, attributed to CTX rather than to a layer.
  If a context service itself calls a serving engine (for example,
  for embeddings or reranking), that call is a nested trace through
  L4 to L1.

Build/Deploy (BUILD):
: Produces and supplies artifacts.  Training and fine-tuning sit
  upstream of this plane and are out of scope.

Management (MGMT):
: Cluster and resource orchestration, placement, autoscaling, model
  loading, operating systems, containers, and configuration.  Not per
  request.

## Ownership of Cross-Layer Concerns

Tokenizer and chat template:
: Artifact in BUILD, executed at L4.  L5 may pre-tokenize for
  budgeting; this is a documented cross-layer coupling (P3).

Quantization:
: The format is stored in the BUILD artifact, selected at deploy time
  by L4 configuration, and realized by L3 kernels.

KV cache:
: Managed by L4 (blocks, eviction, prefix reuse), computed by L3, and
  held in L1 memory.  KV precision is an L4 deploy choice realized by
  L3 kernels.

Agents:
: The agent loop (planning, tool and function calling, and
  agent-protocol clients) is part of L5.  Tools and memory are
  exposed through CTX.  Agents are not a layer above L6.

## Provider Boundary {#provider}

When a consumer uses a hosted model API, L4 to L1 (and often parts of
L5) sit behind the provider boundary.  What stays observable to the
consumer is client-side TTFT and inter-token latency (L6); the
consumer's own orchestration and context-service spans (L5, CTX);
prompt and completion token usage returned by the API; and any
provider-reported latency, queue, or cache fields.

The diagnostic method still applies with only these signals: the
decomposition separates the consumer's own L5 and CTX time from time
spent behind the provider boundary, and isolation tests (bypass
context services, fix prompt length, vary concurrency) can show
whether a regression is inside or outside the boundary, even if they
cannot attribute it to a specific provider-side layer.

# Layer and Plane Descriptions {#layers}

Each layer is described by purpose and scope, components, data-state
transformation, observability signals, and failure modes.  Components
are illustrative.  The technical report {{DAIRM-TR-0001}} also gives
per-layer interfaces and a technology-to-layer mapping.

## L6 Application

Purpose and scope:
: User interaction, request serialization, and rendering of streamed
  output, including citations and tool outputs.  Prompt construction
  belongs to L5.

Components:
: Chat interfaces, IDE assistants, web and mobile applications; API
  clients and SDKs issuing JSON requests; streaming transports
  (Server-Sent Events, WebSockets, gRPC streams); cancellation.

Data state:
: Down: user intent to request payload.  Up: streamed response chunks
  to rendered output.

Observability:
: Client-perceived TTFT and inter-token latency; time to render; error
  rate by status class; cancellation and abandonment rate; payload
  size.

Failure modes:
: Client timeouts shorter than server objectives; buffering proxies
  that defeat streaming; malformed or oversized payloads; retry
  storms; rendering stalls misattributed to the model.

## L5 Orchestration and Gateway

Purpose and scope:
: The policy enforcement point and the home of orchestration.  L5
  authenticates and authorizes the caller, enforces quotas, selects
  the model endpoint, applies templates and system policy, maintains
  conversation state, runs the agent loop (planning, tool and
  function calling, agent-protocol clients), calls Context Services
  when grounding or tools are needed, and applies input and output
  guardrails.

Components:
: API and AI gateways (authentication, rate limiting, routing,
  failover, response caching); orchestration frameworks; prompt
  templates; guardrails (input classifiers, redaction of personal
  data, prompt-injection detection, output moderation, structured
  output validation); session stores; model routers; agent runtimes.

Data state:
: Down: request payload, plus retrieved passages from CTX, to
  enriched prompt.  Up: detokenized text deltas from L4 to
  policy-filtered, schema-validated response chunks.

Observability:
: Gateway overhead; guardrail latency (input and output); routing
  decisions; response-cache hit rate; refusal and policy-violation
  rates; prompt tokens after enrichment; agent steps per request.

Failure modes:
: Prompt growth from unbounded history (pushing load onto L4
  prefill); guardrail latency dominating TTFT; output moderation that
  buffers the stream; routing to an overloaded endpoint; template
  mismatch with the chat template of the artifact; prompt injection
  passing policy checks; runaway agent loops.

## L4 Serving Engine

Purpose and scope:
: Model execution as a service: admission, queueing, scheduling,
  continuous (iteration-level) batching, KV-cache management, prefix
  caching, tokenization and detokenization (executing the tokenizer
  of the artifact), and sampling.  L4 turns many independent prompts
  into a sequence of batched forward passes executed by L3.

Components:
: Inference-serving engines and inference servers; schedulers
  (iteration-level batching, chunked prefill, priority and
  preemption, prefill/decode disaggregation); KV-cache managers
  (paged KV memory {{PAGEDATTENTION}}, prefix caching, eviction and
  swap); speculative and constrained decoding; deploy-time
  configuration (parallel degrees, quantization selection, KV
  precision).

Data state:
: Down: enriched prompt to token-ID batch and KV-cache block table.
  Up: logits to sampled token IDs to detokenized text deltas.

Observability:
: Queue time; server-side TTFT; TPOT; prefill and decode throughput;
  running and waiting requests; KV-cache usage; prefix-cache hit
  rate; preemptions; batch size per iteration; speculative-decoding
  acceptance.  Engine metric names vary by product and version; for
  example, the vLLM documentation {{VLLM-METRICS}} (accessed 9
  November 2026) lists "vllm:kv_cache_usage_perc" and
  "vllm:num_preemptions".

Failure modes:
: KV-cache exhaustion leading to preemption, recomputation, or
  swapping, and therefore TPOT spikes; head-of-line blocking from
  long prefills; over-batching beyond latency objectives; low
  prefix-cache hit rate from non-deterministic L5 prefixes; tokenizer
  or chat-template mismatch with the artifact.

## L3 Model Execution Runtime

Purpose and scope:
: Executes the model graph supplied by BUILD for each scheduled
  batch: embedding lookup, transformer blocks (attention, MLP or
  mixture-of-experts, normalization), and the output projection, as
  framework operators and kernels, plus collective communication when
  the model is sharded.  L3 is where the model artifact runs; the
  artifact itself is not a layer.

Components:
: Framework runtimes, inference runtimes, kernel libraries (matrix
  multiplication and attention kernels), and collective
  communication libraries.

Data state:
: Down: token-ID batch and block table to kernel launch stream;
  activations and KV tensors are produced in place as resident state.
  Up: kernel results to logits for L4.

Observability:
: Kernel time breakdown (matrix multiplication, attention,
  communication); host-side launch gaps; achieved occupancy and
  arithmetic intensity (roofline position {{ROOFLINE}}); collective
  time and overlap; recompilation events; numerical health of logits.

Failure modes:
: Recompilation or graph breaks causing jitter; unfused kernels;
  launch-bound execution at small batch; collective stalls from
  topology-unaware placement; numerical instability in low precision;
  expert imbalance in mixture-of-experts models.

## L2 Device and Driver

Purpose and scope:
: The driver and device runtime: memory allocation, kernel launch and
  streams, graph replay, device partitioning, and error reporting.

Data state:
: Down: kernel launch stream to device instruction and
  memory-transaction stream.  Up: completion events, error codes,
  and counters.

Observability:
: Launch overhead; allocator fragmentation and out-of-memory events;
  device error events; driver resets.

Failure modes:
: Driver and runtime version incompatibility; out-of-memory despite
  free capacity (fragmentation); device resets; noisy neighbors
  under partitioning.

## L1 Physical Compute and Interconnect

Purpose and scope:
: The accelerators that execute instructions, the memory hierarchy
  that feeds them, the intra-node and inter-node fabrics that connect
  them, and the power and thermal envelope that limits them.

Data state:
: The device instruction and memory-transaction stream is executed
  and is observable only as hardware counters (compute and
  tensor-pipe activity, device-memory bytes, link bytes), power, and
  temperature.

Observability:
: Device profiling fields.  For example, the NVIDIA DCGM field list
  {{DCGM-FIELDS}} (accessed 9 November 2026) includes
  "DCGM_FI_PROF_SM_UTIL_RATIO", "DCGM_FI_PROF_TENSOR_UTIL_RATIO",
  "DCGM_FI_PROF_DRAM_UTIL_RATIO", "DCGM_FI_PROF_NVLINK_TX_BYTES", and
  "DCGM_FI_DEV_CLOCKS_EVENT_REASONS".  Earlier versions used other
  names, so implementers pin the version when relying on exact names.

Failure modes:
: Memory bandwidth usually bounds decode speed {{ROOFLINE}}; that is
  a property of the workload, not a fault.  Faults include thermal or
  power capping reducing clocks; link degradation; memory errors and hardware faults;
  capacity exhaustion forcing offload to slower tiers.

## Context Services Plane (CTX) {#ctx}

Purpose and scope:
: Supplies context and capabilities to L5 by call and return:
  retrieval-augmented generation, vector stores and approximate
  nearest-neighbor indexes, embedding models and rerankers, tools,
  memory stores, semantic caches, and web search.  Index construction
  belongs to the data pipeline and is referenced only at its
  interface.

Data state:
: Query (text plus filters), then an internal query embedding and
  candidate set, then retrieved passages (text, score, source URI,
  version, access-control tag) returned to L5.

Observability:
: Embedding, search, and rerank latency; tool-call latency and error
  rate; recall against an evaluation set; empty-result rate; tokens
  contributed to the prompt; index freshness.

Failure modes:
: Retrieval lag (index not memory-resident, cold caches, remote
  hops); low recall from embedding or chunking mismatch; context
  dilution from excessive passage counts; stale index; cross-tenant
  access-control leakage; poisoned documents; slow or failing tools.

## Build/Deploy Plane (BUILD) {#build}

Purpose and scope:
: Produces and supplies the artifacts that L4 and L3 load: weights
  and their format (including quantized formats and adapters), model
  architecture and configuration (for example, attention variant,
  positional-encoding scaling, context length), tokenizer and chat
  template, and compiled graph or kernel IR.  Compilation may happen
  ahead of time or at warm-up; either way the result is an artifact,
  not per-request data.

Observability:
: Artifact identity and digest; quantization format; build and
  compile time; warm-up and recompilation events; evaluation deltas
  against a reference precision.

Failure modes:
: Configuration mismatch with serving (for example, wrong
  positional-encoding scaling or chat template); quality regression
  from aggressive quantization; tampered or unsigned artifacts; stale
  compiled plans after a driver or runtime upgrade.

# Request Lifecycle {#lifecycle}

Down the path:

1. L6 issues a request payload with streaming enabled.

2. L5 authenticates, enforces quota, selects an endpoint, runs input
   guardrails, loads session history, applies the template, and
   decides grounding is needed.

3. CTX embeds the query, searches the index with tenant filters,
   reranks, and returns retrieved passages with provenance.  L5 builds
   the enriched prompt.

4. L4 tokenizes, checks the prefix cache, allocates KV blocks, and
   admits the sequence into the next iteration, forming a token-ID
   batch and block table.

5. L3 executes the prefill forward pass as a kernel launch stream;
   activations and KV entries are written in place in device memory.

6. L2 launches kernels and copies; L1 executes them, observable as
   hardware counters.  Prefill is mostly compute-bound.

Up the path:

7. L3 returns logits for the last position; L4 samples the first
   token.  TTFT is fixed here, plus up-path transit.

8. The token is detokenized and streamed through L5 output guardrails
   to L6.

9. For each further token, L4 schedules a decode iteration and L3 runs
   a one-token forward pass that reads the weights and the KV cache
   from device memory.  At the batch sizes common in serving, decode
   is usually memory-bandwidth-bound {{ROOFLINE}}, so TPOT depends
   largely on L4 batching and KV behavior, L3 attention-kernel cost (which grows
   with context), and L1 memory bandwidth.

10. At completion, L4 frees or retains KV blocks for prefix reuse, L5
    records usage and policy outcomes, and L6 renders the final state.

# Diagnostic Method {#diag}

## Boundary-Attributed Tracing

The method works by decomposition: every request produces a trace in
which each span is attributed to exactly one layer or plane, and each
boundary hand-off is timestamped together with its data state.  A
DAIRM-aligned deployment:

1. propagates one trace context {{TRACE-CONTEXT}} from L6 through L4
   and into CTX calls;

2. tags every span with "dairm.layer" or "dairm.plane" and with
   "dairm.data_state" ({{attrs}}), alongside the OpenTelemetry
   generative AI attributes such as "gen_ai.operation.name", model
   name, and token usage {{OTEL-GENAI}} (those conventions are at
   Development stability);

3. exports L4 engine metrics and L1 device metrics on a common time
   base, labeled with node, device, and replica identifiers, so that
   spans can be joined to device telemetry; and

4. captures L3 profiles on demand for representative requests.

## Latency Decomposition {#decomp}

~~~
E2E  ~= TTFT + (N_out - 1) * TPOT

TTFT ~= t_L6_client + t_L5_gateway + t_L5_guard_in + t_CTX
        + t_L4_queue + t_L4_tokenize + t_prefill(L3..L1)
        + t_up_first_token

TPOT ~= t_L4_schedule + t_decode_step(L3..L1)
        + t_L5_guard_out_per_chunk
~~~

TTFT inflated, TPOT normal:
: The cause is upper-layer time (L5 gateway or guardrails, CTX
  calls), or L4 queueing, or prefill compute for longer prompts.
  These are separated by the L5 and CTX spans, by the L4 queue span
  versus the prefill span, and by the prompt-token count at L5/L4.

TPOT inflated, TTFT normal:
: Look at L4 decode (KV-cache pressure, preemption, batch growth), L3
  kernels (attention cost grows with context; collective stalls), L1
  (memory bandwidth, clock events), or buffering output guardrails at
  L5.

Both inflated:
: Systemic causes: overload (L4 queue), device degradation (L2, L1),
  or retry storms (L6).

## Separating Three Commonly Confused Causes {#discrim}

Context-service delay, L4 KV-cache pressure, and
memory-bandwidth-bound decode each look like "the model is slow".
The signatures below follow from mechanism {{PAGEDATTENTION}}
{{ROOFLINE}}.  They are hypotheses to be calibrated per deployment,
not measured thresholds.

Context-service (CTX) delay:
: TTFT rises while TPOT is unchanged.  The CTX span (embed, search,
  rerank) grows before any L4 span; L4 queue and KV usage are normal.
  Isolation test: replay with CTX bypassed and an equal-length fixed
  context.  If TTFT recovers, CTX is implicated.  Remediate in CTX
  (index residency, co-location, embedding caches, fewer passages) or
  in L5 (parallel CTX calls).

L4 KV-cache pressure:
: TPOT rises and is spiky; TTFT also rises if admission blocks.  The
  L4 queue span grows and decode shows preemption or recomputation
  gaps; KV usage is near capacity and preemption counts rise.
  Isolation test: replay with lower concurrency or a larger KV
  budget.  If the spikes disappear, L4 is implicated.  Remediate in
  L4 (prefix caching, KV quantization, admission limits, a larger KV
  budget, more replicas).  Chunked prefill and disaggregation address
  prefill interference, not KV capacity.

Memory-bandwidth-bound decode:
: TPOT rises smoothly with batch size and context length; the L4
  decode span grows uniformly per step without extra queueing;
  device-memory utilization stays high during decode while tensor-pipe
  utilization is comparatively low.  Isolation test: sweep context
  length at a fixed batch size, and batch size at a fixed context
  length.  If TPOT tracks bytes read per step while memory
  utilization stays high, the result
  is consistent with memory-bandwidth-bound decode.  Remediate through
  BUILD or L4 (weight or KV quantization, speculative decoding) or
  MGMT (scale-out).

The third case is deliberately hedged.  TPOT growth with context
length is also caused by attention-kernel cost at L3 and by KV reads,
so the sweeps show behavior consistent with memory-bandwidth-bound
decode; it does not by itself prove an L1 fault.  High memory
bandwidth use during decode is usually a property of the arithmetic
intensity of the workload, not a hardware defect.

## Troubleshooting Patterns

The technical report {{DAIRM-TR-0001}} contains a sixteen-row
troubleshooting matrix.  Representative entries, written as symptom,
then suspected location, then isolation test:

* Response arrives all at once despite streaming: L6 or L5.  Call L5
  directly, bypassing proxies.

* TTFT high with constant overhead for all prompts: L5.  Disable the
  guardrail chain on a test route.

* Prompt tokens grow with each turn: L5.  Replay with history
  truncated.

* TTFT high only for grounded requests: CTX.  Replay with CTX
  bypassed ({{discrim}}).

* Grounded answers cite wrong or stale sources: CTX.  Query a
  known-answer set and check index freshness.

* TTFT high under load, low at idle: L4.  Replay at lower
  concurrency.

* Intermittent TPOT spikes: L4.  Lower concurrency or enlarge the KV
  budget ({{discrim}}).

* Low prefix-cache hit rate despite a shared system prompt: L5
  coupled to L4.  Compare tokenized prefixes.

* Quality regression after deployment with normal latency: BUILD.
  Compare against a reference-precision artifact.

* Latency jitter after a framework or engine upgrade: L3 or BUILD.
  Warm up and replay with fixed shapes.

* Low device utilization at small batch: L3 or L2.  Profile one
  decode step for host-side launch gaps.

* TPOT rises smoothly with batch and context: L1 (workload property)
  or L3.  Context sweep at fixed batch and batch sweep at fixed
  context ({{discrim}}).

* Throughput drops after sustained load: L1.  Correlate the drop
  with clock-event reasons, power, and temperature.

* Sporadic failures on one node: L2 or L1.  Drain the node and run
  device diagnostics.

## Triage Procedure {#triage}

Attribute top-down, confirm bottom-up:

1. Quantify the symptom as a change in TTFT, TPOT, end-to-end
   latency, error rate, goodput, or quality, with percentile and
   window.

2. Decompose it ({{decomp}}): did TTFT, TPOT, or both move?

3. Walk the trace top-down (L6, then L5 and CTX, then L4) against a
   baseline.  The first layer or plane whose span distribution
   shifted is the candidate.

4. Check the boundary data state entering the candidate (prompt
   tokens at L5/L4, passages and tokens contributed at CTX/L5, batch
   size at L4/L3).  As a heuristic, not a rule: if the incoming
   state changed, suspect the layer above, even if the time is spent
   below; if it did not, suspect the candidate.  Contention or a
   degraded lower layer can lengthen a span with an unchanged input,
   so steps 5 to 7 always follow.

5. Correlate with lower-layer telemetry (L4 metrics, L3 profiles, L2
   and L1 counters), joined on time, replica, node, and device.

6. Run the isolation test for the candidate, changing one variable.

7. Confirm bottom-up that the lower layers are healthy under the
   test.

8. Remediate at the owning layer or plane, then re-measure the
   original symptom.

9. Record the incident with its root-cause layer and its
   manifestation layer.

# Proposed Telemetry Attributes {#attrs}

The following attributes are proposed for community review.  They
are designed to complement, not replace, the OpenTelemetry semantic
conventions for generative AI {{OTEL-GENAI}}, which are at
Development stability and may change.  Where those conventions
already define an attribute or metric (for example
"gen_ai.operation.name" with values such as "retrieval" and
"execute_tool", or the "gen_ai.server.time_to_first_token" and
"gen_ai.server.time_per_output_token" metrics), it takes precedence,
and "dairm.*" adds only layer, plane, data state, and join keys.
Durations are in seconds, following OpenTelemetry practice.  This
document does not register these attributes anywhere ({{iana}}).

"dairm.layer" (integer, 1 to 6):
: Layer to which a request-path span is attributed.

"dairm.plane" (string):
: One of "request_path", "context_services", "build_deploy", or
  "management".

"dairm.data_state" (string):
: One of "request_payload", "retrieved_passages", "enriched_prompt",
  "token_batch", "kernel_stream", "device_stream", or
  "token_stream" ({{states}}).

"dairm.l5.prompt_tokens_enriched" (integer):
: Prompt tokens after templating, history, and retrieved passages.

"dairm.l5.guardrail.verdict" (string):
: Outcome of a guardrail check.

"dairm.l5.agent.step" (integer):
: Step index within an agent loop.

"dairm.ctx.service" (string):
: One of "retrieval", "tool", "memory", "cache", or "search".
  Optional where "gen_ai.operation.name" already identifies the
  operation.

"dairm.ctx.top_k" (integer):
: Passages requested.

"dairm.ctx.passages_returned" (integer):
: Passages returned after filtering and reranking.

"dairm.ctx.tokens_contributed" (integer):
: Tokens the returned passages add to the prompt.

"dairm.l4.queue_time" (double, seconds):
: Time from admission request to first scheduling.

"dairm.l4.step_id" (string):
: Identifier of a scheduler step (iteration).  Recorded on the L4
  spans of each request for the steps it took part in, and on
  step-scoped records, so that step- and device-scoped states can be
  joined to requests.

"dairm.l4.prefix_cache_hit_tokens" (integer):
: Prompt tokens served from the prefix cache.

"dairm.l4.preempted" (boolean):
: Whether the sequence was preempted at least once.

"dairm.l4.batch_size_at_prefill" (integer):
: Running batch size when prefill executed.

"dairm.l4.kv_blocks_used" (integer):
: KV-cache blocks held by the sequence at completion.

"dairm.device_id" (string):
: Device identifier, used as a join key to device telemetry.

"dairm.artifact.id" (string):
: Identifier or digest of the model artifact used.

# Independent Development and Related Work {#related}

## Independent Development {#indep}

DAIRM was developed independently by the author.  A review of related
work after the first public release (as "AOSI", version 1.2.1, 9
November 2026 {{AOSI-V121}}) identified several earlier OSI-inspired
layer models for AI.  These include:

* Reilly, "AOSI (AI Open Systems Interconnection) Reference Model"
  (GitHub, 28 December 2025) {{REILLY-AOSI}}, which uses the same name
  and a seven-layer framing with different layers;

* Liang, a seven-layer AI compute model from hardware to application
  (August 2025) {{LIANG}};

* Rodrigo-Gines, an OSI-inspired stack for agentic AI (September
  2025) {{OSI-AGENTIC}};

* Cisco Research, proposed agent layers L8 and L9 above OSI (Fleming
  et al., November 2025) {{IOA-LAYERS}}; and

* CSA MAESTRO, a seven-layer threat model for agentic AI (February
  2025) {{MAESTRO}}.

To avoid confusion with the work of Reilly, this model was renamed
DAIRM in version 2.0.0.  DAIRM does not claim the layered-stack idea
or the OSI analogy as novel, and it does not claim priority over any
of these works.  Its contributions are (1) a named, observable data
state at every boundary of the inference request path, (2) a
boundary-attributed latency diagnostic method that separates
context-service delay, serving-engine queueing or KV-cache pressure,
and memory-bandwidth-bound decode, and (3) a layer-indexed telemetry
attribute set ("dairm.*") that makes the method executable on
distributed traces.

## Other Layered and OSI-Inspired AI Models

Reilly, AOSI {{REILLY-AOSI}}:
: Seven layers (Infrastructure, Model, Data, Orchestration,
  Communication, Interface, Application).  Same former name and OSI
  framing with different layers.  It states what each layer provides
  to the one above but defines no boundary data states or
  diagnostic method.

Liang {{LIANG}}:
: A seven-layer AI compute model (Physical, Link, Neural Network,
  Context, Agent, Orchestrator, Application).  Same
  hardware-to-application span with different cuts; covers the KV
  cache and disaggregation inside layers; no boundary data states or
  diagnostic method.

Rodrigo-Gines {{OSI-AGENTIC}}:
: A seven-level interoperability stack for agentic AI, concerned with
  interoperability between agents; DAIRM covers the inference path
  within one request.

Fleming et al. {{IOA-LAYERS}}:
: L8 Agent Communication and L9 Agent Semantic layers above OSI.  This
  is the reason DAIRM dropped its own earlier L8/L9 roadmap; agent
  communication is outside the scope of DAIRM.

CSA MAESTRO {{MAESTRO}}:
: A seven-layer threat-modeling framework for agentic AI.  Per-layer
  threat mapping predates DAIRM; the security mapping in this
  document is content, not a novelty claim.

Chander {{CHANDER}}:
: Seven OSI-modeled layers for how language models work, including
  data and training.  It places retrieval inside orchestration and
  argues that training and serving need separate views; DAIRM adopts
  both points (the CTX and BUILD planes).

Smith, AI Layer Model {{AI-LAYER-MODEL}}:
: Nine layers in Substrate, Cognition, and Systems planes; an
  OSI-inspired responsibility map for placing AI components, without
  boundary states or latency diagnostics.

Darling, AILIS v0.2.0 {{AILIS}}:
: A vocabulary of sixteen or more layers from facilities to
  application.  It asks adopters to name the hand-offs between
  layers but defines none itself.  DAIRM is narrower (the inference
  request path) and defines boundary states and diagnostics.

Shapiro et al., ACE {{ACE}}:
: A six-layer cognitive architecture for autonomous agents; it layers
  agent reasoning, not the execution path.

Bucaioni et al. {{BUCAIONI}}:
: A functional software reference architecture for LLM-integrated
  systems, validated on open-source systems; DAIRM has not yet reached
  a comparable level of validation.

Zhang et al. {{ZHANG-LAYERED}}:
: Model, inference, and application layers of LLM-based software,
  with desired capabilities mapped to layers; a design-time view
  without per-boundary data states or latency attribution.

Tsaih et al. {{TSAIH}}:
: An AI tech-stack model for the management and technology
  challenges of AI-enabled application projects; an organizational
  view of the stack rather than a request-path model.

## Standards, Industry Stacks, and Security Frameworks

The OSI Basic Reference Model {{ISO7498-1}} {{X.200}} is the source
of the method DAIRM borrows: layers, service boundaries, and named
data units.  The ISO abstract for ISO/IEC 7498-1 says that the model
"does not intend to serve as an implementation specification", and
ITU-T X.200 states the same intent in its own words.  DAIRM likewise
defines no protocol and is not an extension of OSI.

ISO/IEC 22989 {{ISO22989}} sets AI concepts and terminology; where a
DAIRM term overlaps, the ISO/IEC definition takes precedence.
ISO/IEC 23053 {{ISO23053}} describes the components of ML-based AI
systems across the lifecycle; DAIRM is narrower and operational.  The
NIST AI RMF {{NIST-AI-RMF}} and its Generative AI Profile
{{NIST-AI-600-1}} are organizational risk frameworks to which DAIRM
can supply a technical location.

Industry stack descriptions {{A16Z-LLM}} cover the application tier
(roughly L6, L5, and CTX) and treat the model as a hosted API.  MLOps
architectures {{GOOGLE-MLOPS}} sit upstream of the BUILD plane.
Benchmark suites {{MLPERF-INF}} measure outcomes; the DAIRM
decomposition is meant to explain which layer drives a result.
Serving-systems research {{PAGEDATTENTION}} and roofline analysis
{{ROOFLINE}} show that L4, L3, and L1 have distinct bottlenecks, which
supports separating them.

The OWASP Top 10 for LLM Applications {{OWASP-LLM}}, MITRE ATLAS
{{MITRE-ATLAS}}, NIST AI 100-2 {{NIST-AML}}, and Google SAIF {{SAIF}}
describe risks, adversary techniques, and practices; DAIRM can serve
as a location index for mapping them ({{security}}).

## Limitations

DAIRM is a single-author, informational model.  It has not been
adopted by ISO/IEC, ITU-T, the IETF, NIST, or any other body.  The
boundaries and discriminating signals are argued from mechanism and
the cited literature.  The only measurement so far is a small
CPU-only study in the technical report {{DAIRM-TR-0001}} (Section
7.6): an automated encoding of the triage procedure ({{triage}})
attributed 12 of 12 injected single faults (at CTX, L5, L4, and the
execution hardware) to the location where they were injected, with
no false attributions in 3 no-fault controls, on one small model and
one machine.  It did not test the KV-pressure or memory-bandwidth
discriminators ({{discrim}}), which need accelerator counters.
Training is out of scope.  Counter-examples, missed prior art, and
evidence for or against each claim are welcome.

# Applying the Model {#applying}

None of the following constitutes certification.

* Architecture review: list the components in each layer and plane
  and the data state at each boundary, and find missing controls and
  undocumented cross-layer couplings.

* Observability design: instrument boundaries and tag spans with
  "dairm.layer" or "dairm.plane" so that {{diag}} can be executed.

* Incident management: classify incidents by root-cause and
  manifestation layer to find recurring weak points.

* Security architecture: map threats and controls per {{security}}.

## Alignment Checklist {#alignment}

A description of a system can be called DAIRM-aligned if it
contains:

1. a component inventory per layer (L1 to L6) and plane (CTX, BUILD,
   MGMT), noting which layers sit behind a provider boundary;

2. the boundary data states it records, using the "dairm.data_state"
   values in {{attrs}};

3. spans tagged with "dairm.layer" or "dairm.plane", with one trace
   context propagated from L6 through L4 and into CTX calls;

4. the per-layer and per-plane security controls ({{security}}); and

5. any documented cross-layer couplings (P3).

# Future Work

Version 1.2.1 reserved "Layer 8" and "Layer 9" above the stack.
These were removed in version 2.0.0 because Fleming et al. had
already proposed L8 and L9 agent layers above OSI {{IOA-LAYERS}}, and
reusing those numbers would cause confusion.  Agentic workflows are
modeled inside L5 and CTX instead.  Planned work:

1. Agent traces: model multi-step agent executions as repeated passes
   through the request path, with nested L5 spans per step, tool
   call, and model call.

2. Distributed and disaggregated inference: model prefill/decode
   disaggregation and multi-node serving inside L4 to L1, adding an
   inter-node KV-transfer boundary state.

3. A training and build view that meets the request path at the BUILD
   artifact.

4. Cross-layer efficiency metrics, such as energy per output token.

5. An empirical case study on accelerators: an open-source serving
   engine with a retrieval service, device counters, and traces
   tagged with "dairm.layer", with injected faults (slow retrieval,
   KV-cache pressure, bandwidth-bound decode), measuring whether
   {{discrim}} attributes each fault correctly.  A small CPU-only
   study of the triage procedure is reported in the technical
   report.

# Security Considerations {#security}

This document defines a reference model, not a protocol, and
introduces no new protocol mechanism.  Under principle P7, DAIRM
places each threat at the layer or plane where it materializes;
controls elsewhere provide defense in depth.  The mapping below is
the author's and is offered as content, not as a novelty claim.

L6:
: Direct prompt injection and jailbreak attempts; session hijacking;
  abuse; leakage of output to unauthorized users.  Controls: end-user
  authentication, input size limits, abuse detection, and rendering
  that never executes untrusted content.

L5:
: Prompt injection, both direct and indirect through tool or
  retrieved content {{GRESHAKE}}; system-prompt disclosure; insecure
  tool invocation and excessive agency; quota bypass; cross-tenant
  state leakage.  Controls: input and output guardrails; separation
  of system, user, and retrieved content; least-privilege tool
  scopes; human approval gates; per-tenant isolation; audit logging.

CTX:
: Corpus or index poisoning; injected instructions in documents;
  access-control bypass; embedding inversion that recovers source
  text from stored vectors {{EMB-INVERSION}}; malicious tools.
  Controls: ingestion provenance and integrity checks, server-side
  access-control filtering, content scanning, access control and
  encryption for vector stores, and tool allow-lists.

L4:
: Model extraction by high-volume querying; cross-request leakage
  through shared prefix or KV caches via timing side channels
  {{TIMING-SC}}; denial of service through long prompts or unbounded
  generation.  Controls: rate limiting and anomaly detection,
  per-tenant cache isolation where confidentiality requires it, token
  and time budgets, and a policy on exposing log-probabilities.

L3:
: Unsafe deserialization of model files; compromised kernels or
  runtime libraries.  Controls: safe serialization formats; pinned,
  verified dependencies; software bills of materials.

L2:
: Driver or firmware compromise; memory residue between tenants under
  partitioning.  Controls: firmware attestation and updates, memory
  scrubbing between tenants, and hardware partitioning.

L1:
: Hardware side channels (timing, power); physical access.  Controls:
  dedicated devices or partitioning, confidential-computing
  capabilities where available, and physical security.

BUILD:
: Backdoored or tampered weights; supply-chain compromise of
  frameworks and compilers; membership inference and training-data
  extraction.  Controls: signed, hash-verified artifacts; provenance
  attestation; isolated build pipelines; red-team evaluation before
  promotion.

Mapped onto these locations, the OWASP Top 10 for LLM Applications
(2025) {{OWASP-LLM}} falls as follows: LLM01 Prompt Injection at L5
(arriving via L6 or CTX); LLM02 Sensitive Information Disclosure at
L5, CTX, and BUILD; LLM03 Supply Chain at BUILD and L3; LLM04 Data
and Model Poisoning at BUILD (weights) and CTX (corpus); LLM05
Improper Output Handling at L5 and L6; LLM06 Excessive Agency at L5
(agent loop) and CTX (tools); LLM07 System Prompt Leakage at L5;
LLM08 Vector and Embedding Weaknesses at CTX; LLM09 Misinformation at
CTX, BUILD, and L6; and LLM10 Unbounded Consumption at L4 and L5.

A DAIRM-aligned description states, per layer and plane, which
threats are in scope and which controls apply, and does not rely on
one layer (for example, L5 guardrails alone) as the only control for
threats that materialize in CTX, BUILD, or below L5.

The telemetry proposed in {{attrs}} can itself expose sensitive
information, such as prompt sizes, tenant identifiers, retrieval
provenance, and timing that may assist side-channel inference.
Operators apply the same access control and data minimization to
this telemetry as to the request data it describes.

# IANA Considerations {#iana}

This document has no IANA actions.  The "dairm.*" telemetry
attributes in {{attrs}} are proposals for community review and are
not registered in any IANA registry.

--- back

# Provenance and AI-Assistance Disclosure {#provenance}
{:numbered="false"}

This document is derived from the technical report DAIRM-TR-0001,
Version 2.0.0 {{DAIRM-TR-0001}}, maintained at
https://github.com/CodingThrill0012/dairm and archived on Zenodo under
the concept DOI 10.5281/zenodo.24073121 (Version 2.0.0:
10.5281/zenodo.24123645).  Version 2.0.0 supersedes
the earlier release of the same work under the name "AOSI", version
1.2.1 {{AOSI-V121}}.  The technical report carries additional
material: per-layer interfaces, a full troubleshooting matrix, a
technology-to-layer mapping, Mermaid diagrams, and a revision
history.

Drafting, editing, formatting, and figure preparation were assisted
by AI tools.  The conceptual model, design decisions, and final
content are the author's, and the author takes full responsibility
for them.

# Acknowledgments
{:numbered="false"}

The author thanks the authors of the related models listed in
{{related}}, whose earlier work shaped the revision of this model.
