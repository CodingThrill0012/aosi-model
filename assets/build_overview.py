#!/usr/bin/env python3
"""Generate assets/dairm-overview.svg from the definitions below.

The figure is drawn entirely from this source (no image generation).
Run:  python3 assets/build_overview.py
CC-BY-4.0, (c) 2026 Divyendu Bhatt.
"""
from pathlib import Path
from xml.sax.saxutils import escape

LAYERS = [  # (id, name, owns, colour)
    ("L6", "Application", "client, UX, streaming render", "#3B4A6B"),
    ("L5", "Orchestration & Gateway", "auth, policy, guardrails, templating, routing, agent loop", "#2F6DB5"),
    ("L4", "Serving Engine", "admission, scheduling, batching, KV cache, tokenization, sampling", "#4E9F3D"),
    ("L3", "Model Execution Runtime", "executes the model graph: framework, kernels, collectives", "#C98A14"),
    ("L2", "Device & Driver", "driver, allocator, kernel launch, streams", "#D9692B"),
    ("L1", "Physical Compute & Interconnect", "accelerator, HBM, NVLink/IB, power, thermals", "#C0392B"),
]
# Data state on the boundary below each layer (down-path).
# Each state is (label, capture scope); see DAIRM-TR-0001 section 4.3.
STATES = [
    ("request payload", "per request"),
    ("enriched prompt", "per request"),
    ("token-ID batch + KV-cache block table", "per scheduler step"),
    ("kernel launch stream", "per scheduler step"),
    ("device instruction & memory-transaction stream", "per device"),
]
PLANES = [  # (title, lines, y-anchor layer index, colour)
    ("Context Services plane", ["retrieval/RAG, vector stores, rerankers,", "tools/MCP, memory, semantic caches"], 1, "#2E9C8F"),
    ("Build/Deploy plane", ["weights, architecture, tokenizer,", "chat template, compiled graph / kernel IR"], 2.5, "#7A5BA6"),
    ("Management plane", ["cluster orchestration, placement,", "autoscaling, OS/containers, config"], 4.5, "#6B7785"),
]

W, LX, LW, LH, GAP, TOP = 1080, 40, 560, 62, 34, 92
PX, PW = 750, 300


def text(x, y, s, size=14, weight="normal", fill="#1d1d1f", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def main():
    out = []
    ys = [TOP + i * (LH + GAP) for i in range(len(LAYERS))]
    H = ys[-1] + LH + 112
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
               'font-family="Helvetica, Arial, sans-serif">')
    out.append('<defs><marker id="a" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
               '<path d="M0,0 L10,4 L0,8 z" fill="#444"/></marker>'
               '<marker id="b" markerWidth="10" markerHeight="8" refX="1" refY="4" orient="auto">'
               '<path d="M10,0 L0,4 L10,8 z" fill="#444"/></marker></defs>')
    out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    out.append(text(W / 2, 34, "DAIRM v2.0.0: request path, boundary data states and planes", 20, "bold", anchor="middle"))
    out.append(text(W / 2, 60, "Divyendu's Data-State-Aware AI Reference Model for Generative AI Inference Systems",
                    13, fill="#555", anchor="middle"))
    for i, (lid, name, owns, col) in enumerate(LAYERS):
        y = ys[i]
        out.append(f'<rect x="{LX}" y="{y}" width="{LW}" height="{LH}" rx="6" fill="{col}"/>')
        out.append(text(LX + 14, y + 26, f"{lid}  {name}", 16, "bold", "#ffffff"))
        out.append(text(LX + 14, y + 48, owns, 12.5, fill="#f2f2f2"))
        if i < len(STATES):
            y1, y2 = y + LH, ys[i + 1]
            ax = LX + 40
            out.append(f'<line x1="{ax}" y1="{y1 + 2}" x2="{ax}" y2="{y2 - 3}" stroke="#444" stroke-width="2" marker-end="url(#a)"/>')
            label, scope = STATES[i]
            out.append(f'<text x="{ax + 14}" y="{(y1 + y2) / 2 + 5}" font-size="13" font-weight="bold" fill="#222">'
                       f'{escape(label)}<tspan font-weight="normal" fill="#666">  ({escape(scope)})</tspan></text>')
    for title, lines, idx, col in PLANES:
        y = TOP + idx * (LH + GAP) - 6
        out.append(f'<rect x="{PX}" y="{y}" width="{PW}" height="76" rx="6" fill="#ffffff" stroke="{col}" stroke-width="2.5"/>')
        out.append(text(PX + 12, y + 24, title, 14.5, "bold", col))
        for j, ln in enumerate(lines):
            out.append(text(PX + 12, y + 44 + j * 17, ln, 12, fill="#333"))
    # Connectors: CTX <-> L5 (solid, call/return); BUILD -> L4/L3 (dashed, artifacts); MGMT (dotted).
    cy = TOP + 1 * (LH + GAP) + 31
    out.append(f'<line x1="{PX - 2}" y1="{cy}" x2="{LX + LW + 4}" y2="{cy}" stroke="#2E9C8F" stroke-width="2.5" marker-start="url(#b)" marker-end="url(#a)"/>')
    out.append(text((PX + LX + LW) / 2, cy - 22, "query /", 11.5, fill="#2E9C8F", anchor="middle"))
    out.append(text((PX + LX + LW) / 2, cy - 8, "retrieved passages", 11.5, fill="#2E9C8F", anchor="middle"))
    by = TOP + 2.5 * (LH + GAP) + 32
    for tgt in (2, 3):
        ty = ys[tgt] + LH / 2
        out.append(f'<line x1="{PX - 2}" y1="{by}" x2="{LX + LW + 4}" y2="{ty}" stroke="#7A5BA6" stroke-width="2" stroke-dasharray="7,5" marker-end="url(#a)"/>')
    out.append(text(PX - 30, by + 6, "model artifact", 11.5, fill="#7A5BA6", anchor="end"))
    my = TOP + 4.5 * (LH + GAP) + 32
    out.append(f'<line x1="{PX - 2}" y1="{my}" x2="{LX + LW + 4}" y2="{my}" stroke="#6B7785" stroke-width="2" stroke-dasharray="2,4"/>')
    fy = ys[-1] + LH + 34
    out.append(text(LX, fy, "Up-path: logits -> sampled token IDs -> detokenized text deltas -> streamed response chunks.",
                    13, fill="#333"))
    out.append(text(LX, fy + 22, "Step- and device-scoped states are joined to requests by dairm.l4.step_id and dairm.device_id.",
                    12, fill="#555"))
    out.append(text(LX, fy + 44, "Activations and the KV cache are resident device-memory state; artifacts are not per-request data.",
                    12, fill="#555"))
    out.append(text(W - 20, H - 12, "CC-BY-4.0  (c) 2026 Divyendu Bhatt  |  generated by assets/build_overview.py",
                    10, fill="#888", anchor="end"))
    out.append("</svg>")
    Path(__file__).with_name("dairm-overview.svg").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
