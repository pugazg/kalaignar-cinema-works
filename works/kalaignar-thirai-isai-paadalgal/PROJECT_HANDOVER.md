# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `songs/page-map.json`, `songs/index.json`, `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, all scaled batch reviews through `translations/BATCH_047_054_REVIEW.md`, `editions/en/PREFLIGHT_QA_REPORT.md`, `editions/en/audit_probe.py`, and `docs/SONG_TRANSLATION_GUIDE.md` before changing this work. Current GitHub `main` is authoritative.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 194 physical PDF pages;
- SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- image-only source;
- rendered scan controls Tamil readings.

## Critical Tamil rule — this PDF only

Process only actual numbered lyric pages/direct continuations. Ignore every non-song page for lyric-file creation. Multi-page lyrics remain one song file. Never import absent lyrics from elsewhere.

The full PDF is classified at **62 song-bearing / 132 ignored pages / 54 numbered songs**. Tamil lyric-file work is complete; do not reopen film-section batching as the processing driver.

## Closed source-linked layers

### Tamil

- verified `001–054`: **54/54**;
- draft/review/not-started: **0/0/0**;
- Tamil song transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- unresolved Tamil song readings: **0**.

### English translation

- translated: **54/54 complete-verified**;
- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft/review/not-started: **0/0/0**;
- mode: **`semantic-poetic-source-faithful`**;
- attribution state: **54/54 `anthology-attributed`**.

Do not revise the verified English corpus into smoother generic lyric English. Retain Kalaignar's repetition, rhetoric, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary, performance terms and documented source pressure points.

## Reader/export preflight checkpoint

**PASS — complete.**

Authoritative report: `editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `editions/en/audit_probe.py`  
Workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

Latest passing automated run:

- head commit audited: `f919d3b177c5114b6bc32eb64318207f2a6773c5`;
- workflow run: `32274775152`;
- Python: 3.12;
- audit warnings/errors: **0/0**.

Verified by the preflight:

1. exactly **54** translation records, ordered `001–054` with no gaps;
2. exactly **54** verified Tamil source links;
3. item statuses remain **3 `pilot-verified` + 51 `verified`**;
4. all **54** records remain `anthology-attributed`;
5. mapped Tamil/English line-cue totals are **1,105 / 1,105** with **0** count mismatches;
6. no duplicate anthology number, translation ID, song ID or record path;
7. no source-page, Tamil-title or film-title mismatch;
8. no translation-mode or attribution drift;
9. exactly eight cross-page records retain complete provenance: `009` 38–39, `019` 53–54, `023` 58–59, `024` 62–63, `036` 86–87, `037` 90–91, `051` 121–122, `052` 123–124.

The preflight changed no Tamil or English source-linked record.

## Exact next activity

Generate the deterministic English reader/export package from `translations/records/song-001.json` through `song-054.json`.

Required outputs under `editions/en/`:

1. `reader-edition.md` — publication-facing anthology-order Markdown;
2. `reader-edition.html` — standalone HTML carrying the same 54 songs;
3. `reader-edition.json` — machine-readable reader/export derivative;
4. `QA_REPORT.md` — generated-output reconciliation;
5. `manifest.json` — deterministic input/output hashes and package checkpoint;
6. a deterministic build script, preferably `build.py`, modeled on the repository's established reader/export pattern.

Generation rules:

- input is the complete-verified English translation layer; do **not** edit translations during export;
- preserve anthology order `001–054` exactly once;
- preserve Tamil title, English title, film title, source PDF page array, source-song path, item status and `anthology-attributed` state;
- preserve every English line/cue exactly as stored in the translation records;
- preserve section/turn labels and refrain structure;
- retain the 3 `pilot-verified` / 51 `verified` distinction;
- retain all eight cross-page source arrays;
- generated QA must detect missing/extra/duplicate song IDs and line/cue loss or duplication;
- deterministic manifest must hash authoritative inputs and all generated outputs;
- do not begin downstream Reading Room integration until generated-output QA passes.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
