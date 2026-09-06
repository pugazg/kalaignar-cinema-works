# Ammayappan — Reading Room integration payload

This directory contains the deterministic **source-linked data payload** prepared for the Kalaignar Digital Library / Reading Room.

It does **not** modify or deploy the separate public-site implementation repository.

## Authority

Direct inputs are the complete-verified Ammayappan reader/export, all 63 verified scene derivatives, the closed 1,025-record dialogue/source-role authority and the five-occurrence song/performance inventory. The integration layer does not become textual authority.

## Navigation semantics

The source booklet prints **no scene numbers**. All 63 `ammaiyappan-sNNN` ordinals are archival navigation only and must never be presented as printed source scene numbering.

## Language model

Tamil and English are both available. `ta`, `en`, and parallel display are presentation modes only; stored source/translation text must not be rewritten by the site.

## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- payload: `reading-room.json`;
- payload bytes: **1,551,865**;
- payload SHA-256: `f00efb816edf08b43702a3a1a9d71ed9cc54fd1a803b8881bc6e2c6466de1f8c`;
- scenes: **63**;
- English units: **1,210**;
- dialogue/source-role links: **1,025**;
- cross-page units: **28**;
- occurrence identities / source-span links: **5 / 7**;
- QA: `QA_REPORT.md` — **PASS**;
- site application: **not-applied**.

The payload is ready for the separate public-site implementation repository only when that repository is explicitly authorized for modification.

## Outputs

- `build.py` — deterministic payload builder and validator;
- `reading-room.json` — machine-readable integration payload;
- `QA_REPORT.md` — payload QA checkpoint;
- `manifest.json` — reproducibility/integrity hashes.
