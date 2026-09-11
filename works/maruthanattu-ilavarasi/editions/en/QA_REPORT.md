# Maruthanattu Ilavarasi English reader/export — QA report

Status: **PASS**

## Input checkpoint

- derivative units: **10/10**
- English units: **228/228**
- immutable dialogue links: **208/208**
- non-dialogue source-linked units: **20/20**
- cross-page units: **5/5**
- retained performance records: **0/0**

## Structural QA

- unnumbered opening remains unnumbered: **PASS**
- source-numbered scenes remain exactly **2–10**: **PASS**
- synthetic Scene 1: **0**
- immutable dialogue links complete and unique: **PASS**
- source-unlabelled material has no invented speaker/dialogue ID: **PASS**
- cross-page unit list exact: **PASS**
- Phase 8 zero-item performance state unchanged: **PASS**
- synthetic `(Scene ends.)` / placeholder leakage: **0**

## Generated-output QA

- Markdown renders each of the **228** unit IDs exactly once: **PASS**
- HTML renders each of the **228** unit IDs exactly once: **PASS**
- machine JSON contains each unit ID exactly once: **PASS**

## Reproducibility

- build version: **1**
- authoritative inputs: **14**
- authoritative-input aggregate SHA-256: `74f5f36f8a962d2b5ebd95d4852715741fdcd814457c30c50cddf33a3fed6f84`
- Markdown SHA-256: `b8b16d8a0ae91c7d78e6202264f31057ff80cddebd71ac0255f3957fd1a8d26c`
- HTML SHA-256: `821f2c4bdc52beda89c860db2d8bba6fcfd2657193a40d1de2d5cc4fa11c03bb`
- JSON SHA-256: `57a649b47ba0cd51647f14a480cc33cf5aa89d29645555465546445a8edb32e9`

No canonical Tamil, scene derivative, immutable dialogue record, character mapping, Phase 8 gate record or English translation record is modified by reader generation.
