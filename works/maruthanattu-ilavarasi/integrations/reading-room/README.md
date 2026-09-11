# Maruthanattu Ilavarasi — Reading Room integration payload

This directory contains the deterministic **source-linked data payload** prepared for the Kalaignar Digital Library / Reading Room.

It does **not** modify or deploy the separate public-site implementation repository.

## Authority

Inputs:

- QA-PASS English reader model: `editions/en/reader-edition.json`;
- QA-PASS reader manifest: `editions/en/manifest.json`;
- verified Tamil source derivatives: `scenes/opening.md` and `scene-002.md` through `scene-010.md`.

The integration layer does not become a textual authority.

## Navigation semantics

The payload preserves the actual booklet structure:

- one **unnumbered opening**;
- source-numbered scenes **2–10**;
- no synthetic Scene 1.

## Language model

Tamil and English are available as `ta`, `en`, and parallel presentation modes. Switching language is presentation only; stored Tamil and English text must not be rewritten.

## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- segments: **10/10**;
- English units: **228/228**;
- immutable dialogue links: **208/208**;
- non-dialogue units: **20/20**;
- cross-page units: **5/5**;
- retained performance records: **0**;
- site application: **not-applied**;
- payload bytes: **236,481**;
- payload SHA-256: `25715b161b9df7e47d158871aab56f479be226d7bde624e45e5c3f50724acbb2`.

## Outputs

- `build.py` — deterministic payload builder/validator;
- `reading-room.json` — machine-readable integration payload;
- `QA_REPORT.md` — payload QA checkpoint;
- `manifest.json` — reproducibility/integrity hashes.

The next step, if separately authorized, is application of this payload in the public Reading Room implementation repository.
