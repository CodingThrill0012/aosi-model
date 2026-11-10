# IETF Internet-Draft: draft-bhatt-dairm-00

This folder holds the IETF Internet-Draft version of DAIRM. It is derived from the technical report [DAIRM-TR-0001 v2.0.0](../docs/DAIRM-TR-0001.md), archived under the Zenodo concept DOI [10.5281/zenodo.24073121](https://doi.org/10.5281/zenodo.24073121). It replaces the earlier v1.2.1 draft source, which was never submitted.

**Status: NOT SUBMITTED.** Nothing in this folder has been uploaded to the IETF Datatracker.

| Field | Value |
|---|---|
| Draft name | `draft-bhatt-dairm-00` |
| Title | DAIRM: Divyendu's Data-State-Aware AI Reference Model for Generative AI Inference Systems |
| Author | Divyendu Bhatt (Divyendu.bhatt@gmail.com) |
| Intended status | Informational |
| Stream | Independent Submission (`submissionType="independent"`) |
| IPR | `trust200902` |
| Date | 2026-11-09 (expires 2027-05-13) |
| Length | 30 pages (text rendering) |

## Files

| File | Purpose |
|---|---|
| `draft-bhatt-dairm.md` | The source, in [kramdown-rfc](https://github.com/cabo/kramdown-rfc) Markdown. Edit this file. |
| `draft-bhatt-dairm-00.xml` | RFCXML v3 generated from the source. This is the file you would upload to the Datatracker. |
| `draft-bhatt-dairm-00.txt` | Plain-text rendering (xml2rfc). |
| `draft-bhatt-dairm-00.html` | HTML rendering (xml2rfc). |
| `build.sh` | Rebuilds the XML, TXT and HTML from the Markdown source. |

The draft has the same technical content as DAIRM-TR-0001 v2.0.0, adapted to Internet-Draft constraints:
- Diagrams are redrawn as ASCII art, because Internet-Drafts cannot carry images or Mermaid.
- Wide tables are restructured as lists.
- The troubleshooting matrix is condensed.
- The IETF-required sections are added: Security Considerations, IANA Considerations (no actions) and references.

The draft uses no BCP 14 requirement keywords. "DAIRM-TR-0001" is a technical-report identifier, not an RFC number.

## Rebuilding

```sh
gem install kramdown-rfc      # Ruby
pip install xml2rfc           # Python
./build.sh
```

`build.sh` does the following:
1. Runs `kramdown-rfc --v3`.
2. Normalizes the result with `xml2rfc --v2v3`.
3. Strips the source-line processing instructions and the empty author `<organization/>` element.
4. Renders `.txt` and `.html`.

## Validation (2026-11-10)

| Tool | Result |
|---|---|
| xml2rfc 3.35.0 | 0 errors, 0 warnings |
| idnits 3 (XML and text) | PASS, no nits found |

Only idnits 3 (the Node.js rewrite) was run. The classic idnits 2.x script was not run, because it failed to start in the build environment (it needs GNU awk). The Datatracker runs its own checks at upload.

## How to submit (later, only after review)

Submission is public and permanent.

**Re-date before upload.** The source carries `date: 2026-11-09`. Change `date:` in `draft-bhatt-dairm.md` to the upload date and rebuild, so that the draft's date and its six-month expiry are correct.

1. Go to <https://datatracker.ietf.org/submit/>.
2. Upload `draft-bhatt-dairm-00.xml`. The XML alone is enough; the Datatracker generates the text and HTML.
3. The Datatracker runs idnits and shows the extracted metadata. Check the name, title, author and email, then submit.
4. Confirm the submission from the email that the Datatracker sends to Divyendu.bhatt@gmail.com. The draft then appears at <https://datatracker.ietf.org/doc/draft-bhatt-dairm/>.
5. To publish it as an RFC in the Independent Submission stream, ask the Independent Submissions Editor for review, as described at <https://www.rfc-editor.org/about/independent/>. The ISE decides whether to publish it. An RFC number is assigned only at publication.

An Internet-Draft expires after six months. To revise it, increase `REV` in `build.sh` and `docname` in the source (for example to `-01`), then rebuild and upload again.

## License note

The repository content is licensed CC-BY-4.0. Submitting the draft to the IETF grants the IETF Trust the rights described in BCP 78 and BCP 79 (`ipr="trust200902"`). The author keeps copyright and the CC-BY-4.0 license on the original document.
