# வண்டிக்காரன் மகன் — deterministic English reader/export

This directory is the publication-facing downstream reader/export layer for the complete-verified `வண்டிக்காரன் மகன்` English textual archive.

## Authority

The reader is generated only from verified structured repository data: 72 scene translation records, the reconciled 773-record immutable dialogue corpus, verified scene metadata, and the 9-record source-visible song/performance inventory. The scanned publication and verified canonical Tamil remain upstream authorities.

## Completion checkpoint

Status: **complete-verified — QA PASS**.

- source-numbered archive scenes: **72/72**;
- English translation units: **1,181**;
- immutable dialogue links: **773/773**;
- source-unlabelled spoken units: **27**, with **0 inferred speakers**;
- cross-page units: **58**;
- performance occurrence identities: **9/9** across **66** linked English units;
- generated Markdown SHA-256: `1acd577e7b5e42b5b4f9c09e40668e7b01daa82b6b150fc02caddfa74e14e41a`;
- generated HTML SHA-256: `7a23b8f0f8b35692dd15f10708b87f857c8b4c2b3c82ce104ac9926853015330`;
- generated JSON SHA-256: `d7d9736b80a33d6d85bc911d0fe815219e1c6bf8d93d725fc4f3b56d9c1ad7ab`;
- generated-output QA: `QA_REPORT.md` — **PASS**.

## Outputs

- `build.py` — deterministic reader/export builder and executable whole-work QA;
- `PREFLIGHT_QA_REPORT.md` — authoritative-input checkpoint;
- `reader-edition.md` — English Markdown reader;
- `reader-edition.html` — standalone English HTML reader;
- `reader-edition.json` — machine-readable reader payload;
- `QA_REPORT.md` — generated-output QA;
- `manifest.json` — reproducibility/integrity hashes.

No PDF or EPUB is created by default. The preferred downstream public destination remains the Kalaignar Digital Library / Reading Room.
