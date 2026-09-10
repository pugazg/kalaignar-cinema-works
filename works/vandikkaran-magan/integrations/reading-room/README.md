# வண்டிக்காரன் மகன் — Reading Room integration payload

This directory contains the deterministic **source-linked data payload** prepared for the Kalaignar Digital Library / Reading Room.

It does **not** modify or deploy the separate public-site implementation repository.

## Authority

Direct inputs are the complete-verified `வண்டிக்காரன் மகன்` reader/export, the 72 verified source-numbered scene derivatives, the reconciled 773-record immutable dialogue authority, and the closed nine-occurrence song/performance inventory. This integration layer does not become textual authority.

## Navigation semantics

The booklet **does print scene headings**. The payload therefore preserves the exact source scene IDs (`1`, suffix forms such as `4-எ`, and combined `45-46`) while retaining archive ordinals 1–72 only as stable ordering keys.

## Language model

Tamil and English are both available. `ta`, `en`, and parallel display are presentation modes only; stored source/translation text must not be rewritten by the site.

## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- payload: `reading-room.json`;
- payload bytes: **1,610,402**;
- payload SHA-256: `1d1b611c1261eac75577c8c0499123c260406005f26448bb9aac5f6df22339ba`;
- scenes / Tamil scene texts: **72 / 72**;
- English units: **1,181**;
- immutable dialogue links: **773**;
- source-unlabelled spoken units: **27**;
- cross-page units: **58**;
- performance occurrence identities / linked English units: **9 / 66**;
- item-level lyric authorship remains **0 source-attributed / 6 unresolved / 3 not-applicable**;
- QA: `QA_REPORT.md` — **PASS**;
- site application: **not-applied**.

The payload is ready for the separate public-site implementation repository only when that repository is explicitly authorized for modification.

## Outputs

- `build.py` — deterministic payload builder and validator;
- `reading-room.json` — machine-readable integration payload;
- `QA_REPORT.md` — payload QA checkpoint;
- `manifest.json` — reproducibility/integrity hashes.
