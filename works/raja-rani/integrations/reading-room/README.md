# Raja Rani — Reading Room integration payload

This directory contains the deterministic **source-linked data payload** prepared for the Kalaignar Digital Library / Reading Room.

It does **not** modify or deploy the separate public-site implementation repository.

## Authority

The direct integration input is the QA-PASS deterministic bilingual reader model:

- `works/raja-rani/editions/en/reader-edition.json`
- `works/raja-rani/editions/en/manifest.json`

Those reader files are themselves generated from 200 verified Raja Rani source/derivative inputs. The integration layer does not become a textual authority.

## Navigation semantics

The payload preserves two different source structures:

- **11 numbered front-matter songs** — actual source numbering;
- **58 archival screenplay scenes** — repository navigation only because the booklet prints no screenplay scene numbers.

The site must never display archival scene ordinals as if they were printed source scene numbers.

## Language model

Tamil and English are both available. `ta`, `en`, and parallel display are presentation modes only; stored source/translation text must not be rewritten by the site.

## Outputs

- `build.py` — deterministic payload builder and validator;
- `reading-room.json` — machine-readable integration payload;
- `QA_REPORT.md` — payload QA checkpoint;
- `manifest.json` — reproducibility/integrity hashes.

`site_application_status` remains `not-applied` until the separate Reading Room implementation repository is explicitly authorized and changed.