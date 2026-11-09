---
title: "The AI Open Systems Interconnection (AOSI) Reference Model: A Seven-Layer Stack for Generative AI Execution"
abbrev: "AOSI Reference Model"
docname: draft-bhatt-aosi-reference-model-00
category: info
submissiontype: independent
ipr: trust200902
date: 2026-11-09
v: 3
keyword:
  - generative AI
  - reference model
  - inference
  - observability
  - layered architecture

stand_alone: yes
pi: [toc, sortrefs, symrefs]

author:
  -
    ins: D. Bhatt
    name: Divyendu Bhatt
    email: Divyendu.bhatt@gmail.com

informative:
  AOSI-RFC-0001:
    title: "AOSI-RFC-0001: The AI Open Systems Interconnection (AOSI) Reference Model: A 7-Layer Stack for Generative AI Execution, Version 1.2.1"
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
    target: https://www.itu.int/rec/T-REC-X.200
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
    target: https://doi.org/10.6028/NIST.AI.100-1
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
    target: https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
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
        fullname: Wangfan Li
      -
        fullname: Manuel Delaflor
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
    date: 2025
    seriesinfo:
      DOI: 10.5281/zenodo.17099409
    target: https://doi.org/10.5281/zenodo.17099409
  TRACE-CONTEXT:
    title: "Trace Context"
    author:
      org: W3C
    date: 2021-11-23
    target: https://www.w3.org/TR/trace-context/
  OTEL-GENAI:
    title: "Semantic Conventions for Generative AI Systems"
    author:
      org: OpenTelemetry
    date: false
    target: https://opentelemetry.io/docs/specs/semconv/gen-ai/

--- abstract

Generative AI systems execute across a deep, heterogeneous stack:
client applications and APIs, orchestration gateways, retrieval
pipelines, inference-serving engines, transformer model
architectures, compiler and runtime frameworks, and accelerator
hardware.  Each tier has its own abstractions, tooling, and
telemetry, but there is no shared reference model that names the
tiers, defines the data state exchanged at each boundary, and assigns
responsibility for performance, correctness, and security.

This document describes the AI Open Systems Interconnection (AOSI)
Reference Model, a seven-layer conceptual stack for generative AI
execution, from silicon (Layer 1) to the application (Layer 7).  For
each layer, it defines purpose and scope, core components, the
data-state transformation performed, interfaces to adjacent layers,
observability signals, and characteristic failure modes.  It also
describes a layer-oriented diagnostic method for isolating
bottlenecks, places security considerations at the layer where each
threat materializes, and outlines future work on agentic workflows,
distributed inference, and cross-layer optimization.  The model is
informational; it defines no protocol.

--- middle

# Introduction

## Architectural Fragmentation in Generative AI

The execution of a single generative request traverses at least seven
distinct engineering disciplines.  In practice, these disciplines are
separated by organizational boundaries (application, platform,
machine learning, and infrastructure teams), by tooling boundaries
(application performance monitoring, MLOps dashboards, GPU profilers,
and data-centre monitoring), and by vocabulary boundaries ("prompt",
"batch", "graph", "kernel", "rail").

This fragmentation produces four systemic deficiencies:

1. Non-attributable performance: End-to-end latency is the
   composition of queueing, retrieval, prefill, decode, kernel
   execution, and memory transfer.  Without a layered decomposition,
   a regression in one tier is observed only as an aggregate symptom
   in another.

2. Implicit contracts: The interfaces between tiers (what a "prompt"
   contains when it reaches the serving engine, what a "batch"
   guarantees to the model, what a "graph" promises to the device)
   are defined by individual products rather than by a stable
   reference.

3. Mis-located controls: Security, privacy, and governance controls
   are frequently specified as "AI controls" without regard to the
   tier at which the threat materializes.  This leaves gaps (for
   example, grounding-data integrity) and duplications (for example,
   output filtering at several tiers with inconsistent policy).

4. Non-transferable expertise: Engineers lack a common frame to
   describe where a behaviour originates, which slows incident
   response and design review.

## Contribution of This Document

The OSI Basic Reference Model {{ISO7498-1}} {{X.200}} demonstrated
that a layered decomposition, with explicit service boundaries and
named protocol data units, enables independent evolution of layers,
precise fault localization, and a shared professional vocabulary.
AOSI applies the same method to generative AI execution.
Specifically, this document:

* defines seven layers with explicit scope boundaries
  ({{layers}});

* defines a canonical data-state chain (JSON Payload, Enriched
  Prompt, Vector Chunks, Batched Tensors, Hidden States, Tensor IR,
  Silicon Voltages), analogous to OSI protocol data units
  ({{chain}});

* describes a request lifecycle down and up the stack
  ({{lifecycle}});

* describes a layer-isolation diagnostic method ({{diag}});

* places security considerations at the layer where each threat
  materializes ({{security}});

* positions AOSI against prior reference models, industry stack
  models, and security frameworks ({{related}}); and

* reserves Layers 8 and 9 and a cross-layer optimization plane for
  future work ({{roadmap}}).

This document is derived from AOSI-RFC-0001, Version 1.2.1
{{AOSI-RFC-0001}}, a self-published document by the same author;
see {{origin}}.

## Scope and Non-Goals

In scope: inference-time execution of generative models (primarily
autoregressive transformer language models and, by extension,
multimodal models) from client request to device execution and back.

Out of scope for this revision:

* Training and fine-tuning pipelines, except where they share Layers
  1-3 (see {{l9}}).

* Data governance processes upstream of the Layer 5 index; ingestion
  pipelines are referenced only at their interface.

* Any wire protocol, API schema, or certification regime.  AOSI is
  a reference model, not a protocol.

* Endorsement of any product.  Named technologies are illustrative
  examples of components that occupy a layer.

# Conventions and Terminology

## Requirements Language

{::boilerplate bcp14-tagged}

In this document, these key words apply to descriptions and
implementations that claim alignment with AOSI, not to any product.

## Terminology {#terminology}

Layer (Ln):
: A tier of the AOSI stack with a defined scope, data state, and set
  of interfaces.  L1 is closest to silicon; L7 is closest to the
  user.

Data State:
: The canonical representation of a request (or response) as it
  crosses a layer boundary.  Analogous to an OSI protocol data unit.

Boundary:
: The interface between two adjacent layers, written Ln/Ln-1.  A
  boundary is where a data state is handed off and where telemetry
  SHOULD be emitted.

Down-path:
: Transformation of a request from L7 toward L1 (request ingestion,
  retrieval, prefill dispatch).

Up-path:
: Transformation of results from L1 toward L7 (logits, sampling,
  detokenization, streaming).

Prefill:
: The forward pass over all prompt tokens that populates the KV
  cache and produces the first output logits.  Typically
  compute-bound.

Decode:
: The iterative forward passes after prefill, producing one token
  per step (or k tokens per step with speculative decoding).
  Typically memory-bandwidth-bound at low batch sizes.

KV cache:
: Per-sequence storage of attention key and value tensors for prior
  tokens, which avoids recomputation during decode.

TTFT:
: Time to First Token: the time from request receipt to the first
  output token emitted to the client.

TPOT / ITL:
: Time per Output Token / Inter-Token Latency: the mean (or
  distribution) of intervals between successive output tokens.

E2E latency:
: End-to-end request latency, approximately
  TTFT + (N_output - 1) x TPOT for a streamed response.

Goodput:
: Throughput of requests that meet their latency service-level
  objectives (SLOs).

Span:
: An OpenTelemetry unit of traced work.  AOSI-aligned tracing
  attributes each span to exactly one layer.

Tensor IR:
: Any intermediate representation of a computation graph or kernel
  below the framework API (for example, TorchFX/Inductor graphs,
  StableHLO, MLIR dialects, or PTX).

## Notation

Layer references use the form L1-L7.  A boundary is written L5/L4.
Thresholds given as "illustrative" in {{diag}} are examples for
exposition, not recommended values.

# Design Principles

P1 - Single responsibility per layer:
: Each layer MUST have one primary function.  A component that spans
  layers (for example, a serving engine with built-in kernels)
  SHOULD be described as occupying each layer separately.

P2 - Named data state at every boundary:
: Every boundary MUST have a defined data state, so that it can be
  captured, inspected, and measured.

P3 - Adjacency of interfaces:
: A layer SHOULD interact only with its immediate neighbours.
  Cross-layer shortcuts (for example, an application pinning a GPU)
  MUST be documented as explicit cross-layer couplings.

P4 - Observability by construction:
: Each layer SHOULD emit telemetry at its boundaries that is
  attributable to that layer, enabling isolation ({{diag}}).

P5 - Technology neutrality:
: Layer definitions MUST NOT depend on a specific vendor, framework,
  or accelerator.

P6 - Cost gradient awareness:
: Latency and computational cost increase toward lower layers;
  semantic abstraction and policy surface increase toward upper
  layers.  Optimizations SHOULD be evaluated against this gradient.

P7 - Security at the point of materialization:
: Controls SHOULD be placed at the layer where a threat
  materializes, with defense in depth at adjacent layers where
  justified.

# Architecture Overview

## The Stack

{{fig-stack}} shows the seven layers, their primary functions, and
the data state each layer produces on the down-path.

~~~~ ascii-art
       +-----------------------------------------------+
       | Future work: L8 Agentic Workflows;            |
       | L9 Distributed Inference / Federated          |
       | Learning; Global Optimization                 |
       +-----------------------------------------------+
                              :
 Down-path +-----------------------------------------+ Up-path
 (request) | L7 Application Layer                    | (response)
     |     |   End-user interaction, UI rendering    |     ^
     |     |   Data state: JSON Payload              |     |
     |     +-----------------------------------------+     |
     |     | L6 Orchestration and Gateway            |     |
     |     |   Routing, safety, state, context       |     |
     |     |   Data state: Enriched Prompt           |     |
     |     +-----------------------------------------+     |
     |     | L5 Retrieval and Knowledge (RAG)        |  (L5 not
     |     |   Context injection, semantic search    |  on the
     |     |   Data state: Vector Chunks             |  up-path)
     |     +-----------------------------------------+     |
     |     | L4 Inference and Serving                |     |
     |     |   Model execution, caching, scheduling  |     |
     |     |   Data state: Batched Tensors           |     |
     |     +-----------------------------------------+     |
     |     | L3 Model and Weight Architecture        |     |
     |     |   Mathematical representation of tokens |     |
     |     |   Data state: Hidden States             |     |
     |     +-----------------------------------------+     |
     |     | L2 Framework and Runtime                |     |
     |     |   Math ops, graph compilation, parallel |     |
     |     |   Data state: Tensor IR                 |     |
     |     +-----------------------------------------+     |
     v     | L1 Physical Infrastructure              |     |
           |   Power, silicon math, interconnects    |
           |   Data state: Silicon Voltages          |
           +-----------------------------------------+

 Latency and computational cost increase toward lower layers.
 Semantic abstraction and policy surface increase toward upper
 layers.
~~~~
{: #fig-stack title="The AOSI Seven-Layer Stack"}

L5 is normally traversed on the down-path only.  On the up-path,
results from L4 return to L6 for output policy and then to L7 for
delivery.

## Summary Table

| Layer | Name | Primary Function | Data State (down-path output) |
|:---:|---|---|---|
| L7 | Application Layer | End-user interaction and UI rendering | JSON Payload |
| L6 | Orchestration and Gateway | Routing, safety, state, and context management | Enriched Prompt |
| L5 | Retrieval and Knowledge (RAG) | Context injection, semantic search, grounding | Vector Chunks |
| L4 | Inference and Serving | Model execution, API caching, scheduling | Batched Tensors |
| L3 | Model and Weight Architecture | Mathematical representation of tokens and language | Hidden States |
| L2 | Framework and Runtime | Low-level math operations, graph compilation, parallelism | Tensor IR |
| L1 | Physical Infrastructure | Raw power, silicon math, interconnects | Silicon Voltages |
{: #tab-summary title="AOSI Layer Summary"}

Illustrative core components for each layer are listed in
{{layers}} and in {{mapping}}.

## The Canonical Data-State Chain {#chain}

~~~~ ascii-art
 L7  JSON Payload
       {"model": ..., "messages": [...], "stream": true}
        |
 L6  Enriched Prompt
       system policy + template + session state + user turn
       (policy-checked)
        |
 L5  Vector Chunks
       query embedding -> top-k retrieved chunks (+ scores,
       provenance) merged into context
        |
 L4  Batched Tensors
       token IDs, position IDs, attention metadata,
       KV-cache block tables, batch slots
        |
 L3  Hidden States
       per-layer activations [batch x seq x d_model]
       -> logits [batch x vocab] -> probabilities
        |
 L2  Tensor IR
       lowered/fused graph -> kernels (GEMM, attention, norm)
       + collective schedule
        |
 L1  Silicon Voltages
       MAC operations on tensor cores, HBM transactions,
       link signalling, power draw
~~~~
{: #fig-chain title="The AOSI Data-State Chain"}

# Layer-by-Layer Description {#layers}

Each layer is described with six subsections: Purpose and Scope, Core
Components, Data-State Transformation, Interfaces, Key Metrics and
Observability Signals, and Failure Modes.  Layers are presented from
L7 down to L1, following the down-path of a request.

## Layer 7: Application Layer

### Purpose and Scope

L7 is the point of end-user interaction and UI rendering.  It
captures user intent, serializes it into a machine request, and
renders the streamed response.  L7 owns user experience, client-side
session handling, authentication of the end user to the application,
and presentation of results (including citations and tool outputs).
L7 MUST NOT embed model-specific prompt construction logic that
belongs to L6.

### Core Components

* Chat UIs, IDE assistants, web and mobile applications, copilots,
  and end-user-facing agents.

* API clients and SDKs issuing OpenAI-compatible (or equivalent)
  JSON requests.

* Streaming transports: Server-Sent Events (SSE), WebSockets, and
  gRPC streams.

* Client-side rendering: Markdown and code rendering, citation
  display, partial-output handling, and cancellation.

### Data-State Transformation

Down-path:
: Input is user intent (text, files, images, UI actions).  Output is
  the JSON Payload, for example {model, messages, tools,
  temperature, max_tokens, stream}.

Up-path:
: Input is streamed response chunks (token deltas, tool-call deltas,
  finish reason, usage).  Output is rendered output to the user.

### Interfaces

* L7 to L6: HTTP(S) or gRPC request carrying the JSON Payload,
  end-user identity, and session identifiers.

* L6 to L7: Stream of response chunks, terminal status
  (finish_reason), usage accounting, and policy outcomes (for
  example, refusal codes).

### Key Metrics and Observability Signals

Client-perceived TTFT; client-perceived inter-token latency; time to
render; request error rate by status class; cancellation and
abandonment rate; payload size; client-side span (aosi.layer=7).

### Failure Modes

Client timeouts shorter than server SLOs; buffering proxies that
defeat streaming (whole-response delivery); malformed or oversized
payloads; retry storms amplifying load on lower layers; rendering
stalls misattributed to model latency.

## Layer 6: Orchestration and Gateway

### Purpose and Scope

L6 governs routing, safety, state, and context management.  It
authenticates and authorizes the calling application, enforces
quotas, selects the target model or endpoint, applies prompt
templates and system policy, maintains conversation state and memory,
invokes L5 when grounding is required, and applies input and output
guardrails.  L6 is the policy enforcement point of the stack.

### Core Components

* API gateways and AI gateways (authentication, rate limiting,
  quota, routing, failover, semantic or response caching).

* Orchestration frameworks such as LangChain, LlamaIndex, and
  equivalent workflow engines.

* Prompt templates and chat templates; system-prompt management.

* Guardrails: input classifiers, PII redaction, jailbreak and
  prompt-injection detection, output moderation, and schema
  validation for structured output.

* Session and memory stores (conversation history, summarization of
  long histories).

* Model routers (cost-, latency-, or capability-based selection).

### Data-State Transformation

Down-path:
: Input is the JSON Payload.  Output is the Enriched Prompt: an
  ordered message sequence of system policy, template, session state
  or memory, an optional grounding slot, and the user turn, with the
  routing decision and policy verdicts attached.

Up-path:
: Input is the detokenized text stream from L4.  Output is
  policy-filtered, schema-validated response chunks to L7.

### Interfaces

* L6 to L5: Retrieval query (raw or rewritten), tenant or ACL filter,
  top-k, and score thresholds.

* L5 to L6: Ranked Vector Chunks with provenance metadata.

* L6 to L4: Final prompt (text or pre-templated messages), sampling
  parameters, priority or SLO class, and routing target.

* L4 to L6: Token or text stream, usage, and finish reason.

### Key Metrics and Observability Signals

Gateway overhead latency; guardrail latency (input and output);
routing decisions by model; response or semantic cache hit rate;
policy-violation and refusal rates; prompt token count after
enrichment; rate-limit rejections; span aosi.layer=6 with child spans
per guardrail and template step.

### Failure Modes

Prompt bloat from unbounded history (pushing load onto L4 prefill);
guardrail latency dominating TTFT; streaming defeated by output
moderation that buffers the full response; routing to an overloaded
or wrong-capability endpoint; template mismatch with the model's chat
template causing quality regressions; prompt injection passing policy
checks.

## Layer 5: Retrieval and Knowledge (RAG)

### Purpose and Scope

L5 performs context injection, semantic search, and grounding.  It
converts a query into an embedding, searches one or more indexes,
reranks and filters candidates, and returns chunks that L6 merges
into the Enriched Prompt.  L5 owns the retrieval index at query time
and the integrity of grounding data as served.  Index construction
(ingestion, chunking, and embedding at write time) is referenced at
its interface only.

### Core Components

* Vector databases and approximate-nearest-neighbour (ANN) indexes
  (for example, Pinecone or Milvus; HNSW, IVF, or PQ index types).

* Embedding models (query and document encoders).

* Chunkers and document parsers (write-path interface).

* Hybrid retrieval (lexical BM25 plus dense), metadata filters, and
  ACL-aware retrieval.

* Rerankers (cross-encoders) and context compressors.

### Data-State Transformation

Down-path:
: Input is the retrieval query from the Enriched Prompt (text and
  filters).  Output is Vector Chunks: query embedding, top-k
  candidate vectors, and reranked retrieved chunks (text, score,
  source URI, version, ACL tag), merged into the prompt context.

### Interfaces

* L6 to L5: Query, filters, k, and budget (tokens or time).

* L5 to L6: Ordered chunks with scores and provenance; empty-result
  signal.

* L5 to L4 (embedding inference, optional): Embedding models MAY
  themselves be served by an L4 engine; such calls MUST be traced as
  nested L4 spans within the L5 span.

### Key Metrics and Observability Signals

Embedding latency; ANN search latency (p50/p95/p99); rerank latency;
recall@k or nDCG against an evaluation set; empty-result rate;
retrieved-token count contributed to the prompt; index freshness
(age of the newest indexed document); span aosi.layer=5.

### Failure Modes

Retrieval lag under load (ANN index not memory-resident, cold caches,
network hops to a managed service); low recall from embedding-model
mismatch or poor chunking; context dilution from excessive k; stale
index; ACL leakage across tenants; poisoned or adversarial documents
(see {{security}}).

## Layer 4: Inference and Serving

### Purpose and Scope

L4 manages model execution as a service: tokenization, admission
control, scheduling, batching, KV-cache management, API-level
caching (for example, prefix caching), and sampling orchestration.
L4 converts many independent prompts into a sequence of batched
forward-pass invocations on L3 and returns tokens as they are
produced.  L4 is where request-level concurrency meets device-level
parallelism.

### Core Components

* Serving engines such as vLLM, TensorRT-LLM, Hugging Face TGI, and
  NVIDIA Triton Inference Server (and equivalents).

* Tokenizers and detokenizers (BPE, SentencePiece).

* Schedulers: continuous (iteration-level) batching, chunked
  prefill, priority and preemption policies, and prefill/decode
  disaggregation.

* KV-cache managers: PagedAttention block allocation
  {{PAGEDATTENTION}}, prefix caching, eviction and swap, and KV
  quantization.

* Decoding accelerators: speculative decoding (draft models,
  multi-token heads) and constrained or structured decoding.

* Model replicas and parallelism configuration (tensor, pipeline, or
  expert parallel degree) exposed to L2.

### Data-State Transformation

Down-path:
: Input is the Enriched Prompt (text or messages).  Output is
  Batched Tensors: token-ID tensors, position IDs, attention metadata
  (sequence lengths, causal masks), KV-cache block tables, batch-slot
  assignments, and sampling parameters.

Up-path:
: Input is logits or probabilities per sequence from L3.  Output is
  sampled token IDs, detokenized into text deltas and streamed to L6.

### Interfaces

* L6 to L4: Prompt, sampling parameters, maximum tokens, and
  priority.

* L4 to L3: Per-iteration batch descriptor and input tensors;
  KV-cache pointers.

* L3 to L4: Logits (or sampled tokens if sampling is fused); updated
  KV-cache state.

### Key Metrics and Observability Signals

Queue time (time waiting before first scheduling); server-side TTFT;
TPOT/ITL; prefill and decode throughput (tokens/s); running and
waiting request counts; KV-cache utilization; prefix-cache hit rate;
preemption and swap counts; batch size per iteration;
speculative-decoding acceptance rate; span aosi.layer=4 with child
spans for queue, prefill, and decode.  Engine metric names vary by
product and version.

### Failure Modes

KV-cache exhaustion leading to preemption, recomputation, or swapping
and therefore TPOT spikes; head-of-line blocking from long prefills
interfering with decode (mitigated by chunked prefill or
disaggregation); over-batching that trades TPOT for throughput beyond
the SLO; low prefix-cache hit rate due to non-deterministic prompt
prefixes from L6; tokenizer mismatch with the model.

## Layer 3: Model and Weight Architecture

### Purpose and Scope

L3 is the mathematical representation of tokens and language: the
model architecture and its learned parameters.  It defines what
computation is performed for a given batch: embedding lookup, a stack
of transformer blocks (attention, MLP or mixture-of-experts,
normalization, residual connections), and the output projection to
vocabulary logits.  L3 owns numerical representation choices
(precision and quantization of weights, activations, and KV cache)
as properties of the model artifact.

### Core Components

* Token and positional embeddings (for example, rotary position
  embeddings).

* Transformer blocks: multi-head, grouped-query, or multi-query
  attention; attention heads; feed-forward/MLP layers; MoE routers
  and experts; normalization (LayerNorm, RMSNorm); activations (for
  example, GELU or SwiGLU).

* Weights and their formats: FP16/BF16, FP8, INT8, and INT4
  (weight-only or weight-and-activation quantization); adapters (for
  example, LoRA).

* Output head and logit-processing hooks (temperature, top-p/top-k,
  repetition penalties) where defined by the model contract.

### Data-State Transformation

Down-path:
: Input is Batched Tensors (token IDs, positions, KV pointers).
  Output is Hidden States: per-block activations of shape (batch,
  seq, d_model), attention outputs, expert-routed activations, and
  the final hidden state.

Up-path:
: Input is the final Hidden States.  Output is logits of shape
  (batch, vocab), converted to probabilities (softmax) and returned
  to L4 for sampling.

### Interfaces

* L4 to L3: Forward-pass invocation with batch descriptor.

* L3 to L2: The model expressed as a framework program (module graph)
  with parameter tensors and parallelism annotations.

* L3 to L4: Logits or probabilities and KV-cache writes.

### Key Metrics and Observability Signals

Parameter count and active parameters per token (MoE); FLOPs per
token (prefill versus decode); weight and KV-cache bytes per token;
quantization error or perplexity delta versus reference precision;
expert load balance (MoE); logit statistics (entropy, NaN/Inf
detection); output quality evaluations.

### Failure Modes

Numerical instability (overflow in low precision, NaN propagation);
quality regression from aggressive quantization; MoE expert imbalance
causing stragglers; context-length extrapolation failure beyond the
trained range; architecture or weights mismatch with the serving
configuration (for example, wrong RoPE scaling).

## Layer 2: Framework and Runtime

### Purpose and Scope

L2 provides low-level math operations, graph compilation, and
parallelism.  It lowers the L3 model program into executable kernels
and collective communication schedules for the target device, manages
device memory allocation and streams, and implements tensor,
pipeline, data, and expert parallelism.  L2 is where model math
becomes device programs.

### Core Components

* Frameworks: PyTorch (eager and torch.compile/Inductor) and JAX.

* Compilers and IRs: XLA/StableHLO, MLIR, the Triton compiler,
  TensorRT builders, and TVM-class compilers.

* Kernel libraries: cuBLAS/cuBLASLt, CUTLASS, cuDNN, FlashAttention,
  and ROCm equivalents (rocBLAS, MIOpen).

* Device runtimes and drivers: CUDA, ROCm, and vendor runtimes for
  TPUs and other accelerators; CUDA Graphs.

* Collective communication: NCCL and RCCL; parallelism frameworks
  such as DeepSpeed and Megatron-LM.

### Data-State Transformation

Down-path:
: Input is the Hidden-State computation (module graph and weights).
  Output is Tensor IR: the captured or lowered graph (for example,
  FX/Inductor IR, StableHLO, MLIR, PTX/SASS), fused kernels (GEMM,
  attention, norm, activation), launch configurations, and collective
  schedules (all-reduce, all-gather, all-to-all).

Up-path:
: Input is kernel completion and device buffers.  Output is output
  tensors materialized for L3.

### Interfaces

* L3 to L2: Framework program and parameters.

* L2 to L1: Kernel launches, memory copies, collective operations
  over the device interconnect, and driver calls.

* L1 to L2: Completion events, error codes, and hardware counters.

### Key Metrics and Observability Signals

Kernel time breakdown (GEMM versus attention versus communication);
kernel launch overhead and CPU-side gaps; achieved occupancy and
arithmetic intensity (roofline position); collective-communication
time and overlap with compute; compilation and recompilation events
(graph breaks); allocator fragmentation.  Typical tools include NVIDIA
Nsight Systems and Nsight Compute, PyTorch Profiler, JAX/XLA
profilers, and ROCm profilers.

### Failure Modes

Graph breaks and recompilation causing latency jitter; unfused or
sub-optimal kernels; launch-bound execution at small batch sizes
(mitigated by CUDA Graphs); collective stalls from topology-unaware
placement; memory fragmentation leading to out-of-memory despite free
capacity; driver or runtime version incompatibility.

## Layer 1: Physical Infrastructure

### Purpose and Scope

L1 supplies raw power, silicon math, and interconnects.  It comprises
the accelerators that execute multiply-accumulate operations, the
memory hierarchy that feeds them, the intra-node and inter-node
fabrics that connect them, and the power and cooling envelope that
constrains them.  L1 is where every abstraction above is paid for in
joules, bytes, and nanoseconds.

### Core Components

* Accelerators: GPUs (for example, NVIDIA H100-class or AMD
  Instinct-class), TPUs, and other AI ASICs; tensor cores and matrix
  engines.

* Memory: HBM (for example, HBM3/HBM3e), on-chip SRAM and caches,
  host DRAM, and NVMe tiers (for KV or weight offload).

* Interconnects: NVLink/NVSwitch (intra-node), PCIe, InfiniBand and
  RoCE Ethernet (inter-node), and NICs/DPUs.

* Facility: power delivery, power capping, air or liquid cooling, and
  rack and cluster topology.

### Data-State Transformation

Down-path:
: Input is Tensor IR as executable kernels and transfers.  Output is
  Silicon Voltages: switching activity in tensor cores (MAC
  operations), HBM read and write transactions, and link signalling,
  measurable as power draw and heat.

Up-path:
: Input is physical computation results.  Output is bits in device
  memory, completion events, and hardware counters exposed to L2.

### Interfaces

* L2 to L1: Kernel launches, DMA transfers, and collective traffic.

* L1 to L2: Results, interrupts and events, error signals (ECC and
  Xid-class errors), and telemetry counters.

### Key Metrics and Observability Signals

Streaming-multiprocessor or compute-unit activity; tensor-pipe
activity; HBM (DRAM) bandwidth utilization; memory capacity used;
NVLink, PCIe, and InfiniBand throughput and errors; power draw versus
cap; temperature; clock-throttle reasons; ECC and hardware error
counts.  Typical tools include NVIDIA DCGM, nvidia-smi, rocm-smi,
fabric managers, and facility BMS/DCIM systems.

### Failure Modes

HBM bandwidth saturation during decode (memory-bound regime); thermal
or power throttling reducing clocks; link degradation causing
collective slowdowns; ECC or hardware faults; noisy neighbours under
device partitioning (for example, MIG) or shared fabrics; capacity
exhaustion forcing offload to slower tiers.

# Request Lifecycle {#lifecycle}

## Down the Stack: Ingestion, Grounding, and Prefill

1. L7: The user submits a question in a chat UI.  The client issues
   a JSON Payload with "stream": true.

2. L6: The gateway authenticates the application, enforces quota,
   selects a model endpoint, runs input guardrails, loads session
   history, and applies the prompt template.  It determines that
   grounding is required.

3. L5: The query is embedded, the vector index is searched with
   tenant ACL filters, candidates are reranked, and the top-k chunks
   with provenance are returned.  L6 merges them into the Enriched
   Prompt.

4. L4: The serving engine tokenizes the prompt, checks the prefix
   cache, allocates KV-cache blocks, and admits the sequence into the
   next scheduling iteration, forming Batched Tensors with other
   in-flight sequences.

5. L3: The prefill forward pass computes Hidden States for all prompt
   tokens across all transformer blocks and writes keys and values
   into the KV cache.

6. L2: The runtime executes the corresponding Tensor IR: fused
   attention and GEMM kernels, plus collectives if the model is
   sharded.

7. L1: Tensor cores, HBM, and the interconnect execute the work as
   Silicon Voltages; prefill is predominantly compute-bound.

## Up the Stack: Decode and Token Streaming

1. L3 to L4: Final hidden states are projected to logits; L4 samples
   the first token.  TTFT is fixed at this point (plus up-path
   transit).

2. L4 to L6 to L7: The token is detokenized and streamed through
   output guardrails to the client.

3. Decode loop: For each subsequent token, L4 schedules a decode
   iteration; L3, L2, and L1 execute a single-token forward pass that
   reads the full KV cache and the weights from HBM.  At typical
   batch sizes, decode is memory-bandwidth-bound, so TPOT is governed
   primarily by L1 memory bandwidth and L4 batching and KV-cache
   behaviour.

4. Completion: On a stop condition, L4 frees KV-cache blocks (or
   retains them for prefix reuse), L6 records usage and policy
   outcomes, and L7 renders the final state.

## Sequence Diagram

~~~~ ascii-art
  L7      L6      L5      L4      L3      L2      L1
  |       |       |       |       |       |       |
  |--(1)->|       |       |       |       |       |
  |       |-(2)   |       |       |       |       |
  |       |--(3)->|       |       |       |       |
  |       |<-(4)--|       |       |       |       |
  |       |------(5)----->|       |       |       |
  |       |       |       |-(6)   |       |       |
  |       |       |       |--(7)->|       |       |
  |       |       |       |       |--(8)->|       |
  |       |       |       |       |       |--(9)->|
  |       |       |       |       |       |<(10)--|
  |       |       |       |       |<(11)--|       |
  |       |       |       |<(12)--|       |       |
  |       |<-----(13)-----|       |       |       |
  |<(14)--|       |       |       |       |       |
  |       |       |       |       |       |       |
  | +-- loop: decode until stop condition --------+
  | |     |       |       |-(15)->|-(16)->|-(17)->|
  | |     |       |       |<------------(18)------|
  | |     |<-----(19)-----|       |       |       |
  |<(20)--|       |       |       |       |       |
  | +---------------------------------------------+
  |       |<-----(21)-----|       |       |       |
  |<(22)--|       |       |       |       |       |

 (1)  JSON Payload with "stream": true
 (2)  Auth, quota, routing, input guardrails, template
 (3)  Retrieval query with ACL filters
 (4)  Vector Chunks with provenance
 (5)  Enriched Prompt and sampling parameters
 (6)  Tokenize, prefix cache, KV allocation, schedule
 (7)  Batched Tensors for prefill
 (8)  Forward-pass program
 (9)  Tensor IR as kernels and collectives
 (10) Results and counters
 (11) Output tensors
 (12) Logits for first token
 (13) First token delta
 (14) First chunk streamed (TTFT)
 (15) Batched Tensors for one decode step
 (16) Single-token forward pass
 (17) KV and weight reads from HBM
 (18) Logits (via L2 and L3)
 (19) Token delta
 (20) Streamed chunk (TPOT interval)
 (21) Finish reason and usage
 (22) Final chunk
~~~~
{: #fig-seq title="Request Lifecycle Sequence"}

# Diagnostic and Troubleshooting Method {#diag}

## Layer-Attributed Tracing

Packet analysers make network faults tractable by decoding each
captured packet layer by layer, so that an engineer can assert which
layer misbehaved.  AOSI applies the same discipline to generative AI:
every request SHOULD produce a trace in which each span is attributed
to exactly one AOSI layer and each boundary hand-off is timestamped.
Diagnosis then proceeds by decomposition rather than intuition.

An AOSI-aligned deployment SHOULD:

1. Propagate a single trace context (W3C Trace Context
   {{TRACE-CONTEXT}}, for example via OpenTelemetry) from L7 through
   L4.

2. Tag every span with aosi.layer ({{telemetry}}) and, where
   available, OpenTelemetry generative AI semantic-convention
   attributes {{OTEL-GENAI}} (for example, model name and input and
   output token usage).

3. Export L4 engine metrics and L1 device metrics on a common time
   base, labelled with node, device, and replica identifiers, so that
   request spans can be joined to device telemetry.

4. Capture L2 profiles on demand for representative requests.

## Latency Decomposition {#decomp}

End-to-end latency for a streamed request decomposes as shown in
{{fig-latency}}.

~~~~
E2E  ~= TTFT + (N_out - 1) x TPOT

TTFT ~= t_L7_client + t_L6_gateway + t_L6_guardrails_in
        + t_L5_retrieval + t_L4_queue + t_L4_tokenize
        + t_L4_prefill(L3/L2/L1) + t_up_path_first_token

TPOT ~= t_L4_schedule_iteration + t_decode_step(L3/L2/L1)
        + t_L6_guardrails_out_per_chunk
~~~~
{: #fig-latency title="Latency Decomposition"}

The two components isolate different layers:

* TTFT inflated, TPOT normal: look above L4 compute, at L6 overhead,
  L5 retrieval lag, L4 queueing, or long-prompt prefill.

* TPOT inflated, TTFT normal: look at or below L4 decode, at
  KV-cache pressure or preemption (L4), batch-size growth (L4), HBM
  bandwidth saturation (L1), throttling (L1), collective stalls
  (L2/L1), or buffering output guardrails (L6).

* Both inflated: systemic causes such as overload (L4 queue), device
  degradation (L1), or retry storms (L7).

## Distinguishing Retrieval Lag, KV-Cache Latency, and Memory Bandwidth Saturation {#isolate}

These three causes are routinely confused because each surfaces as
"the model is slow".  They are separable with the signals below.
Thresholds are illustrative only and MUST be calibrated per
deployment.

### L5 Retrieval Lag

Latency signature:
: TTFT rises; TPOT is unchanged.

Trace:
: The aosi.layer=5 span (embed, ANN search, rerank) grows before any
  L4 span starts.

L4 engine metrics:
: Queue and KV-cache usage are normal.

L1 device metrics:
: Normal.

Isolation test:
: Bypass retrieval (use a fixed cached context of equal token length)
  and replay.  If TTFT recovers, L5 is confirmed.

Illustrative trigger:
: L5 span p95 greater than 30% of TTFT.

Remediation:
: Keep the ANN index memory-resident; co-locate the vector database;
  cache query embeddings; reduce k or rerank depth; parallelize
  retrieval with other L6 work.

### L4 KV-Cache Latency

Latency signature:
: TPOT rises and is spiky (and TTFT rises if admission is blocked).

Trace:
: The L4 queue span grows; decode iterations show preemption or
  recompute gaps.

L4 engine metrics:
: KV-cache utilization is near capacity; preemption and swap counters
  rise; waiting requests rise.

L1 device metrics:
: Not necessarily saturated; utilization may drop during preemption
  and recompute churn.

Isolation test:
: Replay with reduced maximum concurrent sequences or a larger KV
  budget.  If the TPOT spikes disappear, L4 is confirmed.

Illustrative trigger:
: KV-cache utilization greater than 90% with non-zero preemptions per
  minute.

Remediation:
: Enable and size prefix caching; quantize the KV cache (for example,
  FP8); tune batch and admission limits; use chunked prefill or
  prefill/decode disaggregation; add replicas.

### L1 HBM Bandwidth Saturation

Latency signature:
: TPOT rises smoothly, tracking batch size and context length.

Trace:
: The L4 decode span grows uniformly per step; there is no extra
  queueing.

L4 engine metrics:
: KV-cache usage may be moderate; the running batch is large;
  tokens/s per GPU plateaus.

L1 device metrics:
: DRAM activity (memory bandwidth utilization) stays near its ceiling
  during decode; tensor-pipe activity is comparatively low.

Isolation test:
: Replay at a fixed batch with growing context length or batch size.
  If TPOT scales roughly with bytes read per step while DRAM activity
  stays pinned, L1 is confirmed.

Illustrative trigger:
: DRAM activity greater than 0.8 sustained during decode windows.

Remediation:
: Quantize weights or KV cache to reduce bytes per token; use
  speculative decoding (more tokens per weight read); use GQA/MQA
  models (L3); scale out via tensor parallelism; move to
  higher-bandwidth memory parts.

## Troubleshooting Matrix

Each entry gives the symptom, the suspected layer, the telemetry to
inspect, an isolation test, and a remediation.

1. Response arrives all at once despite streaming being requested.
   Layer: L7/L6.  Telemetry: client timing of first byte versus first
   rendered chunk; proxy logs.  Test: call L6 directly, bypassing CDN
   or proxy.  Remediation: disable response buffering on proxies; use
   streaming-compatible output guardrails.

2. Client timeouts while the server reports success.  Layer: L7.
   Telemetry: client versus server span durations.  Test: compare the
   client timeout with server p99 E2E latency.  Remediation: align
   timeouts with the SLO; implement cancellation propagation.

3. TTFT high, with constant overhead across all prompts.  Layer: L6.
   Telemetry: gateway and guardrail spans.  Test: disable the
   guardrail chain in a test route.  Remediation: parallelize
   guardrails; use smaller classifier models; cache policy verdicts.

4. Prompt token count grows with each conversation turn.  Layer: L6.
   Telemetry: Enriched Prompt token count per request.  Test: replay
   with history truncated.  Remediation: history summarization,
   windowing, or memory retrieval instead of full replay.

5. TTFT high only for grounded requests.  Layer: L5.  Telemetry: L5
   span breakdown (embed, search, rerank).  Test: replay with
   retrieval bypassed ({{isolate}}).  Remediation: index residency,
   co-location, embedding cache, lower k.

6. Grounded answers cite wrong or stale sources.  Layer: L5.
   Telemetry: retrieval evaluation (recall@k); index freshness.
   Test: query a known-answer set against the index.  Remediation:
   re-chunk; re-embed with a matched model; refresh the index; add a
   reranker.

7. TTFT high under load but low at idle.  Layer: L4.  Telemetry:
   queue-time span; waiting-request gauge.  Test: replay at reduced
   concurrency.  Remediation: autoscale replicas; priority classes;
   admission control.

8. Intermittent TPOT spikes.  Layer: L4.  Telemetry: KV-cache
   utilization; preemption and swap counters.  Test: reduce
   concurrency or increase the KV budget ({{isolate}}).  Remediation:
   prefix caching, KV quantization, chunked prefill, disaggregation.

9. Low prefix-cache hit rate despite a shared system prompt.  Layer:
   L6 to L4.  Telemetry: prefix-cache hit rate; prompt diffs.  Test:
   compare tokenized prefixes across requests.  Remediation: make L6
   templates deterministic; place variable content after the shared
   prefix.

10. Quality regression after deployment with normal latency.  Layer:
    L3.  Telemetry: evaluation-suite deltas; logit entropy;
    quantization configuration.  Test: A/B against reference-precision
    weights.  Remediation: revisit the quantization scheme; verify the
    chat template and RoPE scaling.

11. NaN or garbage output on long contexts.  Layer: L3/L2.
    Telemetry: logit NaN/Inf checks; activation statistics.  Test:
    run the same input at higher precision.  Remediation: change
    precision for unstable operations; verify the context-length
    configuration.

12. Latency jitter after a model or framework upgrade.  Layer: L2.
    Telemetry: compilation and recompilation logs; profiler timeline.
    Test: warm up and replay with fixed shapes.  Remediation:
    eliminate graph breaks; shape bucketing; CUDA Graphs.

13. Low GPU utilization at small batch with high latency.  Layer: L2.
    Telemetry: profiler view of CPU launch gaps between kernels.
    Test: profile one decode step.  Remediation: CUDA Graphs; kernel
    fusion; larger effective batch.

14. Multi-GPU replica slower than expected.  Layer: L2/L1.
    Telemetry: collective timing; NVLink/InfiniBand throughput
    counters.  Test: run collective benchmarks on the node.
    Remediation: topology-aware placement; adjust parallel degrees;
    repair degraded links.

15. TPOT rises smoothly with batch size and context length.  Layer:
    L1.  Telemetry: DRAM activity; tensor-pipe activity.  Test:
    fixed-batch context sweep ({{isolate}}).  Remediation:
    quantization; speculative decoding; scale-out; higher-bandwidth
    parts.

16. Throughput drops after sustained load.  Layer: L1.  Telemetry:
    power versus cap; temperature; clock-throttle reasons.  Test:
    correlate the drop with throttle events.  Remediation: cooling
    remediation; power-cap policy; load spreading.

17. Sporadic request failures on one node.  Layer: L1.  Telemetry:
    Xid and ECC error counters; driver logs.  Test: drain the node
    and run device diagnostics.  Remediation: replace or reset the
    device; exclude the node from scheduling.

## Layer-by-Layer Triage Procedure

Diagnosis SHOULD proceed top-down for attribution and bottom-up for
confirmation:

1. Define the symptom quantitatively, as a change in TTFT, TPOT,
   E2E, error rate, goodput, or quality, with percentile and time
   window.

2. Decompose the latency ({{decomp}}).  Determine whether TTFT, TPOT,
   or both moved.

3. Walk the trace top-down (L7 to L4).  Compare span durations per
   layer against a baseline window.  The first layer whose span
   distribution shifted is the candidate layer.

4. Check the boundary data state.  Verify that the data state
   entering the candidate layer is unchanged (for example, prompt
   token count at L6/L4, k and chunk sizes at L5/L6, batch size at
   L4/L3).  A changed input implicates the layer above.

5. Correlate with lower-layer telemetry (L4 metrics, then L2
   profiles, then L1 counters), joining on time, replica, node, and
   device identifiers.

6. Run the isolation test for the candidate layer, changing exactly
   one variable.

7. Confirm bottom-up.  Ensure that the lower layers are healthy under
   the isolation test, ruling out a masked L1 or L2 cause.

8. Remediate at the owning layer, then re-measure against the
   original symptom definition.

9. Record the incident with its AOSI layer attribution, enabling
   layer-level reliability metrics over time.

{{fig-triage}} summarizes the first decisions of this procedure.

~~~~ ascii-art
Symptom quantified: which moved?
|
+-- TTFT only: inspect L7, L6, L5, and L4 queue spans
|     |
|     +-- L5 span grew?
|           +-- yes: L5 retrieval lag (run bypass test)
|           +-- no:  L4 queue grew?
|                      +-- yes: L4 admission and capacity
|                      +-- no:  L6 overhead or prompt growth
|
+-- TPOT only: inspect L4 decode, KV cache, L2 profile,
|   L1 counters
|     |
|     +-- KV usage high and preemptions present?
|           +-- yes: L4 KV-cache latency (concurrency test)
|           +-- no:  DRAM activity pinned?
|                      +-- yes: L1 HBM bandwidth saturation
|                      |        (context sweep)
|                      +-- no:  L2 kernels or collectives,
|                               or L1 throttling
|
+-- Both: check L4 overload, L1 device health, L7 retries
~~~~
{: #fig-triage title="Triage Decision Tree"}

# Future Work {#roadmap}

The following extensions are reserved.  They are informative in this
revision and may be specified in future documents.

## Layer 8: Agentic Workflows

Scope: self-correcting planning and multi-agent orchestration above
L7, that is, agents that decompose goals into plans, invoke tools,
observe results, critique and revise, and coordinate with other
agents.

Open questions:

* The canonical data state for L8 (candidate: "Plan Graph" or "Task
  State"), and how it maps onto multiple L7 requests.

* Boundaries between L8 planning and L6 orchestration (tool routing,
  memory).

* Observability: trace models for long-running, branching,
  multi-agent executions; attribution of cost and latency to plan
  steps.

* Security: authority delegation, tool-permission scoping, loop and
  runaway-cost controls, and inter-agent trust.

## Layer 9: Distributed Inference and Federated Learning {#l9}

Scope: cross-region and federated serving and learning, that is,
inference spanning multiple clusters or regions, disaggregated
prefill and decode across sites, edge-cloud split execution, and
federated learning or adaptation where data cannot leave its
jurisdiction.

Open questions:

* Whether L9 is a layer or a cross-cutting plane that spans L1-L4
  across sites.

* Data states for cross-site KV-cache transfer and federated
  parameter updates.

* Data residency and regulatory constraints as first-class
  architectural inputs.

* Consistency, failover, and model-version coherence across regions.

## Global Optimization

Scope: a cross-layer optimization plane targeting energy efficiency
and low-latency token delivery, through joint tuning of L6 routing,
L4 scheduling, L3 precision, L2 compilation, and L1 power and
placement against SLOs and energy budgets.

Open questions:

* Common metrics (for example, energy per output token and goodput
  per watt) and how to measure them consistently across layers.

* Feedback interfaces from L1 telemetry to L4 and L6 control
  decisions.

* Guardrails ensuring that global optimization does not violate
  per-layer security or quality constraints.

# Related Work {#related}

AOSI is not the first layered description of AI systems, and it is
not intended to replace any of the works below.  This section records
the prior work the model builds on, how AOSI relates to each, and
what AOSI does and does not claim as new.

## Layered Reference Models and AI Standards

OSI Basic Reference Model {{ISO7498-1}} {{X.200}}:
: AOSI borrows its method from OSI: a fixed number of layers, a
  service boundary between adjacent layers, a named data unit at each
  boundary, and a model that is not intended to serve as an
  implementation specification.  AOSI applies that method to a
  different domain (generative AI execution on one or more
  accelerators).  It does not define wire protocols, and it is not an
  extension of OSI.

ISO/IEC 22989 {{ISO22989}}:
: This document sets out vocabulary and concepts for AI.  AOSI does
  not redefine general AI terms.  Where a term in {{terminology}}
  overlaps with ISO/IEC 22989, the ISO/IEC definition takes
  precedence, and future revisions of this document are expected to
  align their terminology with it.

ISO/IEC 23053 {{ISO23053}}:
: This document describes the components and functions of ML-based
  AI systems in a technology-neutral way, covering the whole ML
  system.  AOSI is narrower and more operational: it covers
  inference-time execution of generative models, splits that
  execution into seven layers from the API payload down to device
  execution, and names the data state at each boundary.  ISO/IEC
  23053 helps describe what an ML system consists of; AOSI helps
  locate where in the serving path a behaviour, cost, or fault
  occurs.

NIST AI RMF and Generative AI Profile {{NIST-AI-RMF}} {{NIST-AI-600-1}}:
: These are organizational risk-management frameworks (Govern, Map,
  Measure, Manage), not technical layer models.  AOSI complements
  them by giving a technical location for the measurements and
  controls that the RMF calls for.  For example, the Measure and
  Manage activities for a retrieval system can be scoped to L5.

## Industry AI and LLM Stack Models

Emerging Architectures for LLM Applications {{A16Z-LLM}}:
: This reference architecture describes the components of an LLM
  application: data pipelines, embedding models, vector databases,
  orchestration, APIs and plugins, LLM caches, logging and
  validation, and app hosting.  Its focus is the application tier,
  which roughly corresponds to AOSI L5-L7.  It does not break down
  serving, model, framework, or hardware tiers, and it does not
  define boundary data states.

MLOps continuous delivery {{GOOGLE-MLOPS}}:
: This reference describes MLOps maturity levels and pipeline
  components for training, validating, and deploying models.  It is
  organized around the ML lifecycle, not around the layers that one
  inference request passes through.  AOSI's out-of-scope training
  concerns are where lifecycle models such as this apply.

MLPerf Inference {{MLPERF-INF}}:
: This is a benchmark suite, not a layer model.  It measures
  system-level inference performance that, in AOSI terms, depends
  jointly on L1-L4.  AOSI's latency decomposition is intended to
  explain which layer drives a benchmark result.

Serving-system research {{PAGEDATTENTION}}:
: Work such as PagedAttention shows that bottlenecks at the serving
  tier (KV-cache memory management) can dominate throughput.  That
  evidence supports treating L4 as a layer distinct from L3 (model
  architecture) and L1 (memory hardware).

## Security Frameworks for AI Systems

The OWASP Top 10 for LLM Applications {{OWASP-LLM}} is a ranked list
of risk categories for LLM applications.  It does not assign a
location in the stack.  {{security}} can be read as a placement of
these categories by layer, as shown in {{tab-owasp}}.

| OWASP LLM Top 10 (2025) | Primary AOSI Layer(s) |
|---|---|
| LLM01 Prompt Injection | L6 (direct via L7; indirect via L5 content) |
| LLM02 Sensitive Information Disclosure | L6, L5, L3 |
| LLM03 Supply Chain | L2, L3 |
| LLM04 Data and Model Poisoning | L3 (weights), L5 (retrieval corpus) |
| LLM05 Improper Output Handling | L6, L7 |
| LLM06 Excessive Agency | L6 (and future L8) |
| LLM07 System Prompt Leakage | L6 |
| LLM08 Vector and Embedding Weaknesses | L5 |
| LLM09 Misinformation | L5, L7 (cross-layer) |
| LLM10 Unbounded Consumption | L4, L6 |
{: #tab-owasp title="OWASP LLM Top 10 Mapped to AOSI Layers"}

MITRE ATLAS {{MITRE-ATLAS}} is a knowledge base of adversary tactics
and techniques against AI-enabled systems.  NIST AI 100-2
{{NIST-AML}} gives a taxonomy and terminology of adversarial
machine-learning attacks and mitigations.  Both describe what an
adversary does; AOSI adds where the technique materializes, so that
detection and controls can be placed at a specific layer under
principle P7.

The Secure AI Framework {{SAIF}} is a conceptual framework of
security practices for AI systems.  AOSI is compatible with it and
can serve as the layer index for mapping SAIF-style controls.

## Other OSI-Inspired AI Layer Models

Conceptual Framework for Autonomous Cognitive Entities {{ACE}}:
: A six-layer cognitive architecture for autonomous agents, running
  from an Aspirational Layer down to Task Prosecution.  It layers an
  agent's reasoning and control, not the execution path of a request.
  It is relevant to the future L8 (Agentic Workflows).

OSI-Inspired Stack for Agentic AI {{OSI-AGENTIC}}:
: A seven-layer interoperability stack for multi-agent systems, from
  physical infrastructure and runtime up to agent-to-agent
  communication, coordination, and governance.  Its main concern is
  interoperability between agents; AOSI's concern is the execution
  path within one generative inference request.

AOSI does not claim to be the first OSI analogy for AI.  Its scope
(single-request generative inference execution) and its emphasis on
boundary data states and diagnostics distinguish it from these
models.

## Contribution and Limitations

On the evidence reviewed above, AOSI claims the following specific
contributions:

1. An end-to-end, named data-state chain for generative inference
   ({{chain}}).  None of the works reviewed define a named data state
   at every boundary from the API down to the device.

2. A full-depth split of the serving path, placing the application,
   orchestration, retrieval, serving, model, framework/compiler, and
   hardware tiers in one ordered stack.  Industry stack diagrams
   usually stop at the model API (application view) or start at the
   accelerator (infrastructure view).

3. Per-layer diagnostics ({{diag}}): a layer-isolation method and a
   troubleshooting matrix that attribute latency and failures to a
   single layer, with proposed telemetry attributes
   ({{telemetry}}).

4. Cross-layer security placement ({{security}}): each threat is
   assigned to the layer where it materializes, turning existing
   threat catalogues into a layer-indexed control map.

Limitations: AOSI is a conceptual, informational model.  It has not
been adopted or endorsed by ISO/IEC, ITU-T, the IETF, NIST, or any
other body.  Its layer boundaries have not yet been validated
empirically across many production deployments.  Training pipelines
are out of scope for this revision.  Counter-examples, overlapping
prior art, and evidence for or against each claim are welcome.

# Applying the Model

AOSI is intended for the following uses.  None constitutes
certification.

Architecture design and review:
: Describe a system by listing the components occupying each layer
  and the data states at each boundary; identify missing layers (for
  example, no L5 integrity controls) and cross-layer couplings (P3).

Observability design:
: Instrument boundaries and tag spans with aosi.layer
  ({{telemetry}}) so that the method in {{diag}} can be executed.

Incident management:
: Classify incidents by AOSI layer to identify recurring weak layers.

Security architecture:
: Map threats and controls per {{security}} and verify defense in
  depth.

Education:
: Provide a common vocabulary across application, platform, ML, and
  infrastructure roles.

A description of a system claiming AOSI alignment SHOULD include: (a)
the component inventory per layer; (b) the boundary data states; (c)
the telemetry emitted per layer; (d) the security controls per layer;
and (e) any documented cross-layer couplings.

# Security Considerations {#security}

This document defines a conceptual reference model and no protocol;
it introduces no new security mechanisms.  However, a principal use
of the model is to place security controls.  Consistent with
principle P7, AOSI places each threat at the layer where it
materializes; controls at adjacent layers provide defense in depth.

L7 (Application):
: Threats: direct prompt injection and jailbreak attempts; session
  hijacking; abuse and automation; leakage of sensitive output to
  unauthorized users.  Controls: strong end-user authentication;
  input size limits; abuse detection; output rendering that does not
  execute untrusted content (for example, HTML/Markdown
  sanitization).

L6 (Orchestration and Gateway):
: Threats: prompt injection (direct, and indirect via tool or
  retrieved content); system-prompt disclosure; insecure tool or
  function invocation; quota bypass; cross-tenant state leakage.
  Controls: a policy enforcement point with input and output
  guardrails; strict separation of system, user, and retrieved
  content; least-privilege tool scopes; per-tenant session isolation;
  audit logging.

L5 (Retrieval and Knowledge):
: Threats: data poisoning of the corpus or index; indirect prompt
  injection embedded in documents; ACL bypass leading to unauthorized
  retrieval; embedding inversion leaking source text.  Controls:
  provenance and integrity checks on ingested documents; ACL-filtered
  retrieval enforced server-side; content scanning for injected
  instructions; access control on the vector store; encryption at
  rest.

L4 (Inference and Serving):
: Threats: model extraction via high-volume querying; cross-request
  leakage through shared prefix or KV caches (timing side channels);
  denial of service via long prompts or unbounded generation.
  Controls: rate limiting and anomaly detection; per-tenant cache
  isolation or partitioning where confidentiality requires it; token
  and time budgets; a policy on exposure of log-probabilities.

L3 (Model and Weights):
: Threats: backdoored or tampered weights; membership inference and
  training-data extraction; unsafe behaviour introduced by
  fine-tuning or adapters.  Controls: signed and hash-verified model
  artifacts; model provenance (supply-chain attestation); red-team
  evaluation before promotion.

L2 (Framework and Runtime):
: Threats: supply-chain compromise of frameworks, kernels, or
  compilers; unsafe deserialization of model files.  Controls: pinned
  and verified dependencies; software bills of materials; safe
  serialization formats (for example, safetensors); isolated build
  pipelines.

L1 (Physical Infrastructure):
: Threats: hardware side channels (timing, power, memory residue
  between tenants); firmware compromise; physical access.  Controls:
  device isolation (dedicated devices or hardware partitioning);
  memory scrubbing between tenants; firmware attestation and updates;
  confidential-computing capabilities where available; physical
  security.

Implementations claiming AOSI alignment SHOULD document, per layer,
which threats are in scope and which controls are applied, and MUST
NOT rely on a single layer (for example, L6 guardrails alone) as the
sole control for threats that materialize at L5 or below.

The telemetry recommended in {{diag}} and {{telemetry}} can itself
expose sensitive information (prompt sizes, tenant identifiers,
retrieval provenance, and timing that may enable side-channel
inference).  Telemetry pipelines SHOULD apply the same access control
and data-minimization policies as the request data they describe.

# IANA Considerations

This document has no IANA actions.

--- back

# Technology-to-Layer Mapping {#mapping}

This appendix is informative.  Many products span layers; each entry
lists the layer or layers at which the named capability operates.

| Technology or Technique | Layer(s) | Notes |
|---|:---:|---|
| OpenAI-compatible chat/completions JSON API | L7/L6 | Request format at L7; terminated and enforced at L6 |
| Server-Sent Events, WebSockets | L7 | Token streaming transport |
| API/AI gateways, rate limiters | L6 | Policy enforcement point |
| LangChain, LlamaIndex | L6 (invoking L5) | Orchestration; retrieval components operate at L5 |
| Guardrail frameworks, moderation classifiers | L6 | Input and output policy |
| Pinecone, Milvus, other vector databases | L5 | ANN search over embeddings |
| Embedding models, rerankers | L5 (served via L4) | Retrieval-time inference |
| vLLM, TensorRT-LLM, TGI, Triton Inference Server | L4 (with L2 kernels) | Serving, scheduling, batching |
| PagedAttention, prefix caching | L4 | KV-cache management |
| Continuous batching, chunked prefill | L4 | Scheduling |
| Speculative decoding | L4 (with L3 draft model) | Decoding strategy |
| Transformer blocks, GQA/MQA, MoE | L3 | Model architecture |
| FP16/BF16/FP8/INT8/INT4 weights, LoRA adapters | L3 | Numerical representation of the artifact |
| FlashAttention | L2 | Attention kernel implementation |
| PyTorch, JAX, torch.compile, XLA, MLIR, Triton compiler | L2 | Framework and compilation |
| CUDA, ROCm, cuBLAS, CUTLASS, CUDA Graphs | L2 | Runtime and kernel libraries |
| NCCL/RCCL, DeepSpeed, Megatron-LM | L2 | Collectives and parallelism |
| Nsight Systems/Compute, PyTorch Profiler | L2 (observing L1) | Profiling |
| DCGM, nvidia-smi, rocm-smi | L1 | Device telemetry |
| H100-class GPUs, TPUs, AI ASICs, HBM3e | L1 | Compute and memory |
| NVLink/NVSwitch, PCIe, InfiniBand, RoCE | L1 | Interconnect |
| OpenTelemetry | Cross-layer | Trace and metric transport; see {{telemetry}} |
{: #tab-mapping title="Technology-to-Layer Mapping"}

# Proposed Telemetry Attributes {#telemetry}

This appendix is informative.  The attributes below are proposed for
community review and are complementary to the OpenTelemetry
generative AI semantic conventions {{OTEL-GENAI}}, not a replacement.
No registry is requested.

| Attribute | Type | Layer(s) | Description |
|---|---|:---:|---|
| aosi.layer | int (1-9) | All | AOSI layer to which the span is attributed |
| aosi.data_state | string | All | Data state produced at the span's boundary (e.g., enriched_prompt) |
| aosi.l6.prompt_tokens_enriched | int | L6 | Prompt tokens after templating, history, and grounding |
| aosi.l6.guardrail.verdict | string | L6 | Outcome of a guardrail check |
| aosi.l5.top_k | int | L5 | Number of chunks requested |
| aosi.l5.chunks_returned | int | L5 | Number of chunks returned after filtering and reranking |
| aosi.l4.queue_time_ms | double | L4 | Time from admission request to first scheduling |
| aosi.l4.prefix_cache_hit_tokens | int | L4 | Prompt tokens served from the prefix cache |
| aosi.l4.preempted | bool | L4 | Whether the sequence was preempted at least once |
| aosi.l4.batch_size_at_prefill | int | L4 | Running batch size when prefill executed |
| aosi.l1.device_id | string | L1 (join key) | Device identifier for joining spans to device telemetry |
{: #tab-telemetry title="Proposed Telemetry Attributes"}

# Origin of This Document {#origin}
{:numbered="false"}

This Internet-Draft is derived from AOSI-RFC-0001, "The AI Open
Systems Interconnection (AOSI) Reference Model: A 7-Layer Stack for
Generative AI Execution", Version 1.2.1, dated 2026-11-09 and
originally drafted 2023-10-26, by the same author.  That document is
self-published and archived at {{AOSI-RFC-0001}} (the concept DOI
covering all versions is 10.5281/zenodo.24073121).  It is maintained
at <https://github.com/CodingThrill0012/aosi-model>.  Its identifier
"AOSI-RFC-0001" is a project label and does not denote a document
published by the RFC Editor.

Relative to Version 1.2.1, this draft converts diagrams to ASCII
figures, restructures wide tables into lists, removes the
document-level license and citation sections (superseded by the IETF
boilerplate), and adds the sections that Internet-Drafts require.
The technical content is otherwise unchanged.

Discussion of this draft is welcome on the repository issue tracker
at <https://github.com/CodingThrill0012/aosi-model/issues>.
