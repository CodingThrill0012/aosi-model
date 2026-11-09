# **Contributing to the AOSI Reference Model**

**Repository:** `aosi-model` · **Specification:** [AOSI-RFC-0001](rfc/RFC-0001-AOSI-Model.md) · **Conceptual Architect:** Divyendu Bhatt

AOSI-RFC-0001 is a **Proposed Standard | Draft for Public Comment**. This document defines how engineers, researchers and MLOps practitioners review the specification, raise issues, propose amendments to layer definitions and take part in architectural debate. The goal is a reference model that is precise, technology-neutral and defensible under scrutiny from every layer of the stack — from application developers to silicon architects.

---

## **Table of Contents**

1. [Who Should Contribute](#1-who-should-contribute)
2. [Governance Model](#2-governance-model)
3. [Reviewing the RFC](#3-reviewing-the-rfc)
4. [Submitting GitHub Issues](#4-submitting-github-issues)
5. [Proposing Layer Amendments (LAP Process)](#5-proposing-layer-amendments-lap-process)
6. [Participating in Architectural Debates](#6-participating-in-architectural-debates)
7. [Pull Requests, Style and Sign-Off](#7-pull-requests-style-and-sign-off)
8. [Code of Conduct](#8-code-of-conduct)
9. [Licensing of Contributions](#9-licensing-of-contributions)

---

## **1. Who Should Contribute**

| Contributor profile | Most valuable review focus |
|---|---|
| **Application and platform engineers** | L7 and L6 boundaries: API payloads, streaming, gateways, guardrail placement |
| **Search and data engineers** | L5: retrieval semantics, index lifecycle, grounding data states |
| **MLOps and inference engineers** | L4: scheduling, batching, KV-cache management, serving metrics, the Diagnostic Matrix (§7) |
| **ML researchers** | L3: architectural generality (dense, MoE, multimodal, state-space and hybrid models), numerical representation |
| **Compiler and systems engineers** | L2: IR definitions, kernel and collective boundaries, parallelism |
| **Hardware and infrastructure engineers** | L1: accelerator, memory, interconnect, power and cooling characterization |
| **Security architects** | §8 Security Considerations: threat placement and control coverage per layer |
| **SRE and observability practitioners** | §7 and Appendix B: telemetry attributes, trace propagation, triage procedure |

---

## **2. Governance Model**

### **2.1 Roles**

| Role | Responsibilities |
|---|---|
| **Conceptual Architect** (Divyendu Bhatt) | Owns the conceptual integrity of the model. Holds final decision authority on layer definitions, numbering, scope and status transitions of RFCs. |
| **Editors** | Appointed by the Conceptual Architect. Triage issues, shepherd amendment proposals, maintain editorial consistency, and record decisions. |
| **Layer Reviewers** | Practitioners recognized for sustained, high-quality review of a specific layer. Provide expert assessment on amendments affecting that layer. |
| **Contributors** | Anyone who files issues, comments, or submits pull requests under this document. |

### **2.2 Decision principles**

1. **Technical merit over volume.** Decisions are made on argument and evidence, not on the number of supporting comments.
2. **Rough consensus, then decision.** Editors seek rough consensus among participants. Where consensus cannot be reached, **the Conceptual Architect decides**, and the rationale is recorded.
3. **Stability of the core.** The seven-layer structure and the canonical data-state chain (*JSON Payload → Enriched Prompt → Vector Chunks → Batched Tensors → Hidden States → Tensor IR → Silicon Voltages*) change only through the Layer Amendment Proposal process (§5) and with an explicit compatibility analysis.
4. **Neutrality.** No contribution may make a layer definition depend on a specific vendor, product or accelerator. Products appear only as illustrative examples.
5. **Transparency.** All substantive decisions are recorded in the issue tracker with the outcome and its reasoning.

### **2.3 Document status lifecycle**

| Status | Meaning |
|---|---|
| **Draft** | Work in progress; may change without notice. |
| **Proposed Standard \| Draft for Public Comment** | Current status of RFC-0001. Open for review; normative content may change in response to comments. |
| **Last Call** | Fixed review window before stabilization; only errata and blocking objections are considered. |
| **Stable** | Normative content frozen for the version; changes require a new version via the LAP process. |
| **Superseded / Withdrawn** | Replaced by a later RFC or withdrawn by the Conceptual Architect. |

---

## **3. Reviewing the RFC**

A useful review is specific, located and falsifiable. When reviewing [AOSI-RFC-0001](rfc/RFC-0001-AOSI-Model.md), please:

1. **Read the normative sections first:** §2 (Conventions), §3 (Design Principles), §5 (Layer-by-Layer Specification).
2. **Test the boundaries.** For each layer, ask:
   - Is the **Purpose & Scope** single and unambiguous (Principle P1)?
   - Is the **data state** at each boundary precisely defined and observable (P2)?
   - Can a real component you operate be placed in exactly one layer — or, if it spans layers, can its parts be separated cleanly?
   - Are the listed **failure modes** and **observability signals** correct and complete for production systems?
3. **Test the diagnostics.** Apply §7 to a real or reconstructed incident. Does the decomposition (TTFT vs TPOT) and the triage procedure lead to the correct layer? Where does it mislead?
4. **Test the security mapping.** Does §8 place each threat at the layer where it materializes? Are controls missing?
5. **Check precision.** Flag imprecise terminology, inconsistent naming, or claims that require qualification.
6. **Cite precisely.** Reference section numbers and, where possible, line numbers or permalinks.

**Review standards.**
- Claims about performance behaviour SHOULD be accompanied by a reproducible description (hardware class, software versions, workload shape) or a public reference.
- Do not submit proprietary or confidential data. Abstract it or describe it qualitatively.
- Thresholds proposed for the Diagnostic Matrix MUST be labelled as illustrative unless supported by reproducible evidence.

---

## **4. Submitting GitHub Issues**

Open issues at **https://github.com/CodingThrill0012/aosi-model/issues**. Search existing issues first to avoid duplicates. Use exactly one **type label** and one or more **layer labels**.

### **4.1 Issue types**

| Type label | Use for | Required content |
|---|---|---|
| `review-comment` | General technical feedback on a section | Section reference; the concern; suggested direction |
| `clarification` | Ambiguous or under-specified text | Quoted text; the competing interpretations; proposed wording |
| `erratum` | Factual, typographical, link or formatting error | Location; what is wrong; correction |
| `layer-amendment` | Change to a layer's scope, components, data state, interfaces, metrics or failure modes | Must follow the LAP template (§5) |
| `diagnostic-pattern` | New or corrected row for the Diagnostic & Troubleshooting Matrix | Symptom; suspected layer; telemetry/tool; isolation test; remediation; evidence |
| `security` | Additions or corrections to §8 | Threat; layer of materialization; controls; references. **Do not disclose live vulnerabilities in third-party products** — report those to the affected vendor. |
| `roadmap` | Input on Layer 8, Layer 9 or Global Optimization | Problem statement; candidate data state; boundary with existing layers |
| `governance` | Changes to this document or the process | Problem with current process; proposed change |

### **4.2 Layer labels**

`layer-7`, `layer-6`, `layer-5`, `layer-4`, `layer-3`, `layer-2`, `layer-1`, `cross-layer`, `layer-8-proposed`, `layer-9-proposed`.

### **4.3 Issue template (general)**

```markdown
**Type:** review-comment | clarification | erratum | diagnostic-pattern | security | roadmap | governance
**Layer(s):** L_
**RFC section:** §_._

### Summary
One or two sentences stating the issue.

### Detail
Precise description, quoting the current text where relevant.

### Proposed change
Replacement text, new table row, or direction.

### Evidence / references
Reproducible observations, public documentation, or reasoning.
```

### **4.4 Triage service levels**

Editors aim to acknowledge and label new issues promptly during the public-comment period. These are goals, not guarantees. Issues lacking required content may be labelled `needs-info` and closed if not completed.

---

## **5. Proposing Layer Amendments (LAP Process)**

Any change to a layer's **Purpose & Scope, Core Components (beyond illustrative examples), Data State, Interfaces, Key Metrics or Failure Modes**, or to the number and ordering of layers, requires a **Layer Amendment Proposal (LAP)**.

### **5.1 Required sections of a LAP**

```markdown
# LAP-NNNN: <Short title>

**Author(s):** 
**Affected layer(s):** L_
**Affected RFC sections:** §_._
**Type:** Scope change | Data-state change | Interface change | New layer | Layer merge/split | Observability | Failure modes

## 1. Motivation
What problem in the current model does this solve? Which real systems are mis-described today?

## 2. Current text
Quote the normative text being changed.

## 3. Proposed text
Exact replacement text, tables and diagrams.

## 4. Boundary analysis
Effect on adjacent-layer interfaces and on the canonical data-state chain.
Demonstrate that Principles P1–P7 (RFC-0001 §3) still hold.

## 5. Technology neutrality check
Show that the change holds for at least two independent technology stacks
(e.g., different serving engines, frameworks, or accelerator families).

## 6. Diagnostic impact
Changes required to §7 (matrix rows, triage procedure, telemetry attributes).

## 7. Security impact
Changes required to §8 (threat placement, controls).

## 8. Compatibility
Does any existing description that claims AOSI alignment become invalid? Migration guidance.

## 9. Alternatives considered
Other designs and why they were rejected.
```

### **5.2 LAP lifecycle**

| State | Entry criteria | Exit |
|---|---|---|
| **Submitted** | Issue opened with `layer-amendment` label and complete template | Editor triage |
| **Under Review** | Editor confirms completeness; Layer Reviewers assigned | Review period closes (announced on the issue) |
| **Revision Requested** | Substantive objections or gaps identified | Author revises → *Under Review*, or no response → *Withdrawn* |
| **Final Comment Period** | Editors judge rough consensus is reached; outcome proposed | Fixed window for final objections |
| **Accepted** | Conceptual Architect approves | Pull request merged; RFC version incremented; revision history updated |
| **Rejected** | Conceptual Architect declines, with recorded rationale | May be resubmitted only with materially new evidence |
| **Withdrawn** | Author withdraws, or inactivity | — |
| **Deferred** | Valid but out of scope for current version (e.g., Layer 8/9 material) | Revisited at next roadmap review |

### **5.3 Versioning**

- **Patch (x.y.Z):** errata, clarifications and illustrative-example updates with no normative change.
- **Minor (x.Y.z):** accepted LAPs that add or refine normative content compatibly.
- **Major (X.y.z):** changes to layer count, ordering or the canonical data-state chain.

---

## **6. Participating in Architectural Debates**

Disagreement about layer boundaries is expected and valuable. Debates take place in the open on GitHub Issues (or Discussions, if enabled) so that the reasoning is preserved.

### **6.1 Norms**

1. **Argue the model, not the person.** Address claims, evidence and consequences.
2. **State the boundary question precisely.** For example: "Does prefix caching belong to L4 (serving policy) or L2 (runtime memory management)?" — not "the layers are wrong".
3. **Use the principles as the yardstick.** Arguments SHOULD reference Design Principles P1–P7 and the data-state chain.
4. **Bring counter-examples.** The strongest argument against a boundary is a real system it fails to describe. Describe the system concretely.
5. **Separate normative from illustrative.** Disputes over which product is listed as an example are editorial, not architectural.
6. **Disclose interests.** If you are affiliated with a vendor whose product is affected by a proposal, say so.
7. **Converge.** Summarize positions periodically. Editors may close a debate by recording the options and escalating to a decision.

### **6.2 Decision process**

1. Editors summarize the positions and the trade-offs in the issue.
2. If rough consensus exists, editors propose the outcome and open a **Final Comment Period**.
3. If not, the **Conceptual Architect makes the decision** and records the rationale.
4. Decisions may be revisited only through a new LAP containing materially new evidence.

---

## **7. Pull Requests, Style and Sign-Off**

### **7.1 Pull requests**

- Reference the issue or LAP the PR implements (`Closes #NN`). Normative changes without an accepted LAP will not be merged.
- Keep each PR to a single logical change.
- Update the RFC **Revision History** and version for any normative change.

### **7.2 Style**

- Use RFC 2119 / RFC 8174 keywords (in capitals) only for normative requirements.
- Refer to layers as **L1–L7** and boundaries as **L5/L4**.
- Use the canonical layer names exactly as defined in RFC-0001 §4.2.
- Name products only as illustrative examples; do not make performance claims about specific products without reproducible evidence.
- Do not present illustrative thresholds as normative values.
- Diagrams SHOULD be authored in Mermaid where possible; binary figures go in `/assets` with their source file.
- Ensure Markdown tables have consistent column counts and that Mermaid blocks render on GitHub.

### **7.3 Developer Certificate of Origin (DCO)**

All commits MUST be signed off, certifying the [Developer Certificate of Origin 1.1](https://developercertificate.org/):

```bash
git commit -s -m "L4: clarify KV-cache preemption failure mode (#NN)"
```

This appends `Signed-off-by: Your Name <your.email@example.com>` to the commit message. Pull requests with unsigned commits will not be merged.

---

## **8. Code of Conduct**

All participants are expected to:

- be respectful and professional, regardless of seniority, affiliation or background;
- engage in good faith and assume good faith in others;
- avoid harassment, personal attacks, discriminatory language and sustained disruption;
- refrain from promotional content and unsolicited vendor marketing;
- respect confidentiality: do not post proprietary, personal or security-sensitive information.

Editors may hide comments, lock threads, or restrict participation for violations. Concerns may be raised privately with the Conceptual Architect via the contact listed in RFC-0001.

---

## **9. Licensing of Contributions**

The AOSI specification and documentation are licensed under the **Creative Commons Attribution 4.0 International License (CC-BY-4.0)**, crediting **Divyendu Bhatt** as Conceptual Architect of the AOSI Reference Model. See [LICENSE](LICENSE).

By submitting a contribution (issue text proposed for inclusion, pull request, LAP or diagram), you:

1. confirm that you have the right to submit it under the DCO;
2. agree that it is licensed under **CC-BY-4.0** and may be incorporated into the AOSI specification; and
3. acknowledge that contributors are credited through the repository history and, for accepted LAPs, in the RFC revision history.

---

© Divyendu Bhatt. Licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
