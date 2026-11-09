# Contributing to DAIRM

**Repository:** `dairm` · **Document:** [DAIRM-TR-0001](docs/DAIRM-TR-0001.md) · **Author and maintainer:** Divyendu Bhatt

DAIRM-TR-0001 is a **Technical Report / Working Draft** (version 2.0.0) published for public review. It is not an IETF RFC and not a standard. This document explains how engineers, researchers and MLOps practitioners can review it, raise issues, propose changes and take part in design discussions. The goal is a reference model that is precise, technology-neutral and defensible under scrutiny from every part of the stack.

---

## Contents

1. [Who Should Contribute](#1-who-should-contribute)
2. [Governance](#2-governance)
3. [Reviewing the Technical Report](#3-reviewing-the-technical-report)
4. [Submitting GitHub Issues](#4-submitting-github-issues)
5. [DAIRM Change Proposals (DCP)](#5-dairm-change-proposals-dcp)
6. [Design Discussions](#6-design-discussions)
7. [Pull Requests, Style and Sign-Off](#7-pull-requests-style-and-sign-off)
8. [Code of Conduct](#8-code-of-conduct)
9. [Licensing of Contributions](#9-licensing-of-contributions)

---

## 1. Who Should Contribute

| Contributor profile | Most valuable review focus |
|---|---|
| **Application and platform engineers** | L6 and L5: payloads, streaming, gateways, guardrail placement, agent loops |
| **Search and data engineers** | Context Services plane: retrieval semantics, index lifecycle, the retrieved-passages state |
| **MLOps and inference engineers** | L4: scheduling, batching, KV-cache management, serving metrics, the diagnostic method (§7) |
| **ML and compiler engineers** | L3 and the Build/Deploy plane: graph execution, kernels, compiled artifacts, quantization ownership |
| **Systems and hardware engineers** | L2 and L1: drivers, memory, interconnect, power and thermal behaviour |
| **Security architects** | §8 Security Considerations: threat placement and control coverage per layer and plane |
| **SRE and observability practitioners** | §7 and Appendix B: telemetry attributes, trace propagation, triage procedure |
| **Researchers** | §10: prior art we missed, and evidence for or against the three contribution claims |

---

## 2. Governance

### 2.1 Roles

| Role | Responsibilities |
|---|---|
| **Author / maintainer** (Divyendu Bhatt) | Owns the conceptual integrity of the model and decides on layer and plane definitions, boundary data states, scope and document status. |
| **Editors** | Appointed by the maintainer. Triage issues, shepherd change proposals, keep the text consistent and record decisions. |
| **Reviewers** | Practitioners recognized for sustained, high-quality review of a layer or plane. |
| **Contributors** | Anyone who files issues, comments or pull requests under this document. |

### 2.2 Decision principles

1. **Technical merit over volume.** Decisions rest on argument and evidence, not on the number of comments.
2. **Rough consensus, then decision.** Editors seek rough consensus. If none is reached, the maintainer decides and records the reasoning.
3. **Stability of the core.** The layers, planes and boundary data states change only through a DAIRM Change Proposal (§5) with a compatibility analysis.
4. **Neutrality.** No layer definition may depend on a specific vendor, product or accelerator. Products appear only as examples.
5. **Credit for prior work.** If a proposal draws on someone else's published work, cite it. Reports of missed prior art are always in scope.
6. **Transparency.** Substantive decisions are recorded in the issue tracker with their reasoning.

### 2.3 Document status

| Status | Meaning |
|---|---|
| **Working Draft** | Current status of DAIRM-TR-0001. Open for review; content may change in response to comments. |
| **Review Draft** | A fixed review window before stabilizing a version; only errata and blocking objections are considered. |
| **Stable** | Content frozen for the version; changes need a new version through a DCP. |
| **Superseded / Withdrawn** | Replaced by a later version or withdrawn by the maintainer. |

These are project labels only. They do not imply review or adoption by any standards body.

---

## 3. Reviewing the Technical Report

A useful review is specific, located and falsifiable. When reviewing [DAIRM-TR-0001](docs/DAIRM-TR-0001.md):

1. **Read the core sections first:** §2 (Terminology), §3 (Design Principles), §4 (Architecture Overview) and §5 (Layer and Plane Descriptions).
2. **Test the boundaries.** For each layer and plane, ask:
   - Is its purpose single and unambiguous (P1)?
   - Is the data state at each boundary defined, per request, and observable (P2)?
   - Can a component you operate be placed in one layer or plane, or, if it spans several, can its parts be separated cleanly?
   - Are the failure modes and observability signals correct and complete?
3. **Test the diagnostics.** Apply §7 to a real or reconstructed incident. Does the decomposition and triage lead to the right layer or plane? Where does it mislead?
4. **Test the security mapping.** Does §8 place each threat where it materializes?
5. **Check related work.** Is any relevant prior work missing or described unfairly in §10?
6. **Cite precisely.** Give section numbers and, where possible, permalinks.

**Review standards.**
- Claims about performance should come with a reproducible description (hardware class, software versions, workload shape) or a public reference.
- Do not submit proprietary or confidential data.
- Thresholds proposed for the diagnostic method must be labelled illustrative unless supported by reproducible evidence.

---

## 4. Submitting GitHub Issues

Open issues at **https://github.com/CodingThrill0012/dairm/issues**. Search existing issues first. Use one **type label** and one or more **scope labels**.

### 4.1 Issue types

| Type label | Use for | Required content |
|---|---|---|
| `review-comment` | General technical feedback on a section | Section reference; the concern; suggested direction |
| `clarification` | Ambiguous or under-specified text | Quoted text; the competing readings; proposed wording |
| `erratum` | Factual, typographical, link or formatting error | Location; what is wrong; correction |
| `change-proposal` | Change to a layer, plane, boundary data state, interface, telemetry attribute or failure mode | Must follow the DCP template (§5) |
| `diagnostic-pattern` | New or corrected row for the troubleshooting matrix | Symptom; suspected layer or plane; telemetry; isolation test; remediation; evidence |
| `prior-art` | Related work that is missing or misdescribed | Citation with link and date; how it relates to DAIRM |
| `security` | Additions or corrections to §8 | Threat; where it materializes; controls; references. **Do not disclose live vulnerabilities in third-party products**; report those to the vendor. |
| `governance` | Changes to this document or the process | Problem with the current process; proposed change |

### 4.2 Scope labels

`layer-6`, `layer-5`, `layer-4`, `layer-3`, `layer-2`, `layer-1`, `plane-context-services`, `plane-build-deploy`, `plane-management`, `cross-layer`, `telemetry`.

### 4.3 Issue template

```markdown
**Type:** review-comment | clarification | erratum | diagnostic-pattern | prior-art | security | governance
**Layer(s) / plane(s):** L_ / CTX / BUILD / MGMT
**Section:** §_._

### Summary
One or two sentences stating the issue.

### Detail
Precise description, quoting the current text where relevant.

### Proposed change
Replacement text, new table row, or direction.

### Evidence / references
Reproducible observations, public documentation, or reasoning.
```

### 4.4 Triage

Editors aim to acknowledge and label new issues promptly. These are goals, not guarantees. Issues lacking required content may be labelled `needs-info` and closed if not completed.

---

## 5. DAIRM Change Proposals (DCP)

Any change to a layer's or plane's purpose, components (beyond illustrative examples), boundary data states, interfaces, telemetry attributes or failure modes, or to the number and order of layers, needs a **DAIRM Change Proposal (DCP)**.

### 5.1 Required sections of a DCP

```markdown
# DCP-NNNN: <Short title>

**Author(s):**
**Affected layer(s) / plane(s):**
**Affected sections:** §_._
**Type:** Scope change | Data-state change | Interface change | New layer or plane | Merge/split | Telemetry | Failure modes

## 1. Motivation
What problem does this solve? Which real systems are mis-described today?

## 2. Current text
Quote the text being changed.

## 3. Proposed text
Exact replacement text, tables and diagrams.

## 4. Boundary analysis
Effect on adjacent interfaces and on the boundary data states.
Show that principles P1-P7 (DAIRM-TR-0001 §3) still hold.

## 5. Technology neutrality check
Show that the change holds for at least two independent technology stacks.

## 6. Diagnostic impact
Changes needed in §7 and Appendix B.

## 7. Security impact
Changes needed in §8.

## 8. Prior art
Related published work, with citations.

## 9. Compatibility
Does any existing DAIRM-aligned description become invalid? Migration guidance.

## 10. Alternatives considered
Other designs and why they were rejected.
```

### 5.2 DCP lifecycle

| State | Entry criteria | Exit |
|---|---|---|
| **Submitted** | Issue opened with the `change-proposal` label and a complete template | Editor triage |
| **Under Review** | Editor confirms completeness; reviewers assigned | Review period closes (announced on the issue) |
| **Revision Requested** | Substantive objections or gaps found | Author revises → *Under Review*, or no response → *Withdrawn* |
| **Final Comment Period** | Editors judge rough consensus is reached; outcome proposed | Fixed window for final objections |
| **Accepted** | Maintainer approves | Pull request merged; version incremented; revision history updated |
| **Rejected** | Maintainer declines, with recorded reasoning | May be resubmitted only with materially new evidence |
| **Withdrawn** | Author withdraws, or inactivity | — |
| **Deferred** | Valid but out of scope for the current version | Revisited at the next planning review |

### 5.3 Versioning

- **Patch (x.y.Z):** errata, clarifications and example updates with no change to the model.
- **Minor (x.Y.z):** accepted DCPs that add or refine content compatibly.
- **Major (X.y.z):** changes to the layers, planes or boundary data states.

---

## 6. Design Discussions

Disagreement about boundaries is expected and valuable. Discussions happen in the open on GitHub Issues (or Discussions, if enabled) so the reasoning is preserved.

1. **Argue the model, not the person.**
2. **State the boundary question precisely.** For example: "Does prefix caching belong to L4 (serving policy) or L2 (device memory management)?", not "the layers are wrong".
3. **Use the principles as the yardstick.** Refer to P1–P7 and the boundary data states.
4. **Bring counter-examples.** The strongest argument against a boundary is a real system it fails to describe.
5. **Separate the model from the examples.** Disputes over which product is listed as an example are editorial.
6. **Disclose interests.** If you are affiliated with a vendor affected by a proposal, say so.
7. **Converge.** Editors may close a discussion by recording the options and asking the maintainer to decide.

---

## 7. Pull Requests, Style and Sign-Off

### 7.1 Pull requests

- Reference the issue or DCP the PR implements (`Closes #NN`). Changes to the model without an accepted DCP will not be merged.
- Keep each PR to one logical change.
- Update the revision history and version for any change to the model.

### 7.2 Style

- DAIRM-TR-0001 uses no BCP 14 requirement keywords; write in plain language.
- Refer to layers as **L1–L6**, planes as **CTX**, **BUILD** and **MGMT**, and boundaries as **L5/L4** or **CTX/L5**.
- Use the canonical names from DAIRM-TR-0001 §4.
- Name products only as examples; do not make performance claims about specific products without reproducible evidence.
- Do not present illustrative thresholds as recommended values.
- Author diagrams in Mermaid where possible; put rendered figures in `/assets` with their source. Do not add AI-generated images, and disclose AI assistance in preparing any figure.
- Make sure Markdown tables have consistent column counts and Mermaid blocks render on GitHub.

### 7.3 Developer Certificate of Origin (DCO)

All commits must be signed off, certifying the [Developer Certificate of Origin 1.1](https://developercertificate.org/):

```bash
git commit -s -m "L4: clarify KV-cache preemption failure mode (#NN)"
```

This appends `Signed-off-by: Your Name <your.email@example.com>` to the commit message. Pull requests with unsigned commits will not be merged.

---

## 8. Code of Conduct

All participants are expected to:

- be respectful and professional, regardless of seniority, affiliation or background;
- engage in good faith and assume good faith in others;
- avoid harassment, personal attacks, discriminatory language and sustained disruption;
- refrain from promotional content and unsolicited vendor marketing;
- respect confidentiality: do not post proprietary, personal or security-sensitive information.

Editors may hide comments, lock threads or restrict participation for violations. Concerns may be raised privately with the maintainer at the contact listed in DAIRM-TR-0001.

---

## 9. Licensing of Contributions

DAIRM and its documentation are licensed under the **Creative Commons Attribution 4.0 International License (CC-BY-4.0)**, crediting **Divyendu Bhatt**. See [LICENSE](LICENSE).

By submitting a contribution (issue text proposed for inclusion, pull request, DCP or diagram), you:

1. confirm that you have the right to submit it under the DCO;
2. agree that it is licensed under **CC-BY-4.0** and may be incorporated into DAIRM; and
3. acknowledge that contributors are credited through the repository history and, for accepted DCPs, in the revision history.

---

© 2026 Divyendu Bhatt. Licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
