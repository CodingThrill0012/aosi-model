#!/usr/bin/env bash
# Reproduce the DAIRM fault-injection study (CPU only).
# Usage: LLAMA_DIR=/path/to/llama-b12239 MODEL=/path/to/qwen2.5-0.5b-instruct-q4_k_m.gguf ./run_all.sh [REPS]
set -euo pipefail
cd "$(dirname "$0")"
: "${LLAMA_DIR:?set LLAMA_DIR to the unpacked llama.cpp release (b12239, ubuntu-x64)}"
: "${MODEL:?set MODEL to qwen2.5-0.5b-instruct-q4_k_m.gguf}"
PY=${PY:-python3}
REPS=${1:-3}
# Harness and CTX service on cores 4-7; llama-server (and the injected
# contention) on cores 0-3, set inside harness.py.
taskset -c 4-7 "$PY" harness.py --llama-dir "$LLAMA_DIR" --model "$MODEL" --threads 4 --reps "$REPS"
"$PY" analyze.py
