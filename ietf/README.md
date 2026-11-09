# IETF Internet-Draft: draft-bhatt-aosi-reference-model-00

This folder holds the IETF Internet-Draft version of the AOSI Reference
Model, derived from [AOSI-RFC-0001 v1.2.1](../rfc/RFC-0001-AOSI-Model.md)
(archived at [doi:10.5281/zenodo.24073122](https://doi.org/10.5281/zenodo.24073122)).

| Field | Value |
|---|---|
| Draft name | `draft-bhatt-aosi-reference-model-00` |
| Title | The AI Open Systems Interconnection (AOSI) Reference Model: A Seven-Layer Stack for Generative AI Execution |
| Author | Divyendu Bhatt (Divyendu.bhatt@gmail.com) |
| Intended status | Informational |
| Stream | Independent Submission (`submissionType="independent"`) |
| IPR | `trust200902` |
| Date | 2026-11-09 (expires 2027-05-13) |
| Length | 43 pages (text rendering) |

## Files

| File | Purpose |
|---|---|
| `draft-bhatt-aosi-reference-model.md` | Source, in [kramdown-rfc](https://github.com/cabo/kramdown-rfc) Markdown. Edit this file. |
| `draft-bhatt-aosi-reference-model-00.xml` | RFCXML v3 generated from the source. **This is the file to upload to the Datatracker.** |
| `draft-bhatt-aosi-reference-model-00.txt` | Plain-text rendering (xml2rfc). |
| `draft-bhatt-aosi-reference-model-00.html` | HTML rendering (xml2rfc). |
| `build.sh` | Rebuilds the XML, TXT and HTML from the Markdown source. |

The draft is the same technical content as AOSI-RFC-0001 v1.2.1. Diagrams
are redrawn as ASCII art (Internet-Drafts cannot carry images or Mermaid),
wide tables are restructured as lists, and the IETF-required sections
(Security Considerations, IANA Considerations, references) are added.
"AOSI-RFC-0001" is a project label only; an RFC number is assigned by the
RFC Editor only if the draft is approved for publication.

## Rebuilding

```sh
gem install kramdown-rfc      # Ruby
pip install xml2rfc           # Python
./build.sh
```

`build.sh` runs `kramdown-rfc --v3`, normalizes the result with
`xml2rfc --v2v3`, strips source-line processing instructions and the empty
author `<organization/>` element, and renders `.txt` and `.html`.

## Validation (2026-11-09)

| Tool | Result |
|---|---|
| xml2rfc 3.35.0 | 0 errors, 0 warnings |
| idnits 2.x (text) | 0 errors, 0 flaws, 1 warning: "Couldn't figure out when the document was first submitted" (expected for a -00 draft) |
| idnits 3.3.0 (XML and text) | 0 errors, 0 warnings, 1 comment: one no-break space inside the standard BCP 14 boilerplate |

## How to submit

Do this only when you are ready; submission is public and permanent.

1. Go to <https://datatracker.ietf.org/submit/>.
2. Upload `draft-bhatt-aosi-reference-model-00.xml` (the XML alone is enough;
   the Datatracker generates the text and HTML).
3. The Datatracker runs idnits and shows the extracted metadata. Check the
   name, title, author and email, then submit.
4. Confirm the submission from the email the Datatracker sends to
   Divyendu.bhatt@gmail.com. The draft then appears at
   <https://datatracker.ietf.org/doc/draft-bhatt-aosi-reference-model/>.
5. For publication as an RFC in the Independent Submission stream, request
   review by the Independent Submissions Editor as described at
   <https://www.rfc-editor.org/about/independent/>. The ISE decides whether
   to publish and arranges review; an RFC number is assigned only at
   publication.

An Internet-Draft expires after six months. To keep it alive or revise it,
increase `REV` in `build.sh` and `docname` in the source (for example to
`-01`), rebuild, and upload again.

After submission, add the Datatracker URL to the Zenodo record as a related
identifier ("is variant form of" / "is published in"), and later the RFC
number if one is assigned.

## License note

The repository content is licensed CC-BY-4.0. Submitting the draft to the
IETF grants the IETF Trust the rights described in BCP 78 and BCP 79
(`ipr="trust200902"`); the author keeps copyright and the CC-BY-4.0 license
on the original document.
