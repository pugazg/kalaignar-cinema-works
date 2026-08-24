# ராஜா ராணி — Scene-Layer Completion / Dialogue Initialization Checkpoint

## Purpose

This checkpoint closes the verified scene-text derivative phase, reconciles repository-level bookkeeping, and opens the immutable dialogue-index phase without changing canonical Tamil.

## Scene-layer completion

The source-supported scene segmentation remains:

- archival navigation segments: **58**
- verified scene-text eligible segments: **50**
- blocked source-review segments: **8**

Verified scene-text production is complete:

- completed verified scene files: **50/50 eligible**
- remaining eligible scene files: **0**
- latest/final scene batch: `notes/scene-text-batch-010.md`

Blocked scene IDs remain:

- `raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013` — PDF 27
- `raja-rani-s033` — PDF 48
- `raja-rani-s039` — PDF 57
- `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055` — PDF 74

No verified scene derivative exists for those eight segments. Their source-review status has not been weakened to complete the scene phase.

## Global bookkeeping reconciliation — complete

Raja Rani had matured inside `works/raja-rani/` while remaining absent from the repository-level `data/works.json` registry and root README status sections. That bookkeeping drift is now corrected.

Completed reconciliation:

- `data/works.json` now contains a `raja-rani` registry entry;
- root `README.md` now contains a `## ராஜா ராணி status` section;
- the global entry and root status reflect the established work-local state rather than restarting or downgrading the work.

Reconciled state:

- source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- source SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- 80 PDF pages
- canonical screenplay: PDF 10–79 / printed pp.9–78
- source pages audited: 79/79
- source pages verified/review: 75/4
- screenplay pages verified/review: 66/4
- review pages: PDF 27, 48, 57, 74
- source-numbered screenplay scenes: none
- archival scene segments: 58
- verified scene-text files: 50/50 eligible
- blocked scene-text segments: 8

## Dialogue phase opened

The immutable dialogue-index layer is initialized under `dialogues/` with:

- `dialogues/README.md`
- `dialogues/schema.json`
- `dialogues/index.json`

Initial dialogue state:

- eligible verified scenes: **50**
- blocked scenes: **8**
- dialogue records: **0**
- completed dialogue scenes: **0/50**

Only explicitly speaker-labelled utterances from verified scene derivatives may become dialogue records. Source-unlabelled speech, narrative text, stage directions, decorative separators, written letters and performance/song cues do not receive inferred speakers.

Exact source-visible speaker-label variation must remain immutable here. Character normalization belongs only to the later character/entity layer.

## Next activity

Dialogue Batch 001: process verified `scene-001.md` through `scene-010.md` in source order, then stop before blocked `s011`–`s013`.

For every created record preserve exact speaker label, exact printed delimiter, exact utterance text, scene provenance, PDF/printed-page provenance and cross-page continuity.
