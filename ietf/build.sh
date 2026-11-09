#!/usr/bin/env bash
# Rebuild the Internet-Draft from the kramdown-rfc source.
# Requires: kramdown-rfc (Ruby gem) and xml2rfc (Python package) on PATH.
set -euo pipefail
cd "$(dirname "$0")"
DRAFT=draft-bhatt-dairm
REV=00
OUT="${DRAFT}-${REV}"

# 1. Markdown -> RFCXML v3
kramdown-rfc --v3 "${DRAFT}.md" > "${OUT}.raw.xml"

# 2. Normalize to canonical RFCXML v3
xml2rfc --v2v3 "${OUT}.raw.xml" -o "${OUT}.v3.xml"
rm -f "${OUT}.raw.xml"

# 3. Strip source-line processing instructions and the empty author
#    <organization/> element (no organization is listed for the author)
python3 - "${OUT}.v3.xml" "${OUT}.xml" <<'PY'
import re, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
s = re.sub(r"[ \t]*<\?line -?\d+\?>\n?", "", s)
front, rest = s.split("</front>", 1)
front = re.sub(r"(<author [^>]*>\s*)<organization/>\s*", r"\1", front, count=1)
open(dst, "w", encoding="utf-8").write(front + "</front>" + rest)
PY
rm -f "${OUT}.v3.xml"

# 4. Render text and HTML
xml2rfc --v3 --text --html "${OUT}.xml"
echo "Built ${OUT}.xml, ${OUT}.txt, ${OUT}.html"
