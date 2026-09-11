# Maruthanattu Ilavarasi — deterministic English reader/export

This directory is the downstream publication-facing reader/export layer for the complete-verified English translation of `மருதநாட்டு இளவரசி`.

## Authority

Inputs are the ten verified English translation shards, the complete translation index, the immutable-dialogue checkpoint, the Phase 8 zero-item song/performance checkpoint and work metadata. Tamil source derivatives remain linked by path and remain upstream authority.

## Source-structure rule

The source contains an **unnumbered opening** followed by source-numbered scenes **2–10**. No Scene 1 is invented.

## Completion checkpoint

Status: **complete-verified — QA PASS**.

- derivative units: **10/10**;
- English units: **228**;
- immutable dialogue links: **208/208 exactly once**;
- non-dialogue units: **20**;
- cross-page units: **5/5 exact**;
- performance records/units: **0/0**;
- Markdown SHA-256: `b8b16d8a0ae91c7d78e6202264f31057ff80cddebd71ac0255f3957fd1a8d26c`;
- HTML SHA-256: `821f2c4bdc52beda89c860db2d8bba6fcfd2657193a40d1de2d5cc4fa11c03bb`;
- JSON SHA-256: `57a649b47ba0cd51647f14a480cc33cf5aa89d29645555465546445a8edb32e9`.

## Outputs

- `build.py` — deterministic reader builder/validator;
- `reader-edition.md` — English Markdown reader;
- `reader-edition.html` — standalone English HTML reader;
- `reader-edition.json` — machine-readable source-linked reader payload;
- `QA_REPORT.md` — generated-output QA;
- `manifest.json` — reproducibility/integrity hashes.

No PDF or EPUB is created. The preferred next destination is the Kalaignar Digital Library / Reading Room, where Tamil and English may be combined as presentation layers without rewriting either source.
