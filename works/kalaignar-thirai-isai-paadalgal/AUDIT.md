# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers the complete PDF-specific song-presence scan, line-level Tamil lyric verification for all **54 numbered songs**, the complete source-linked English translation corpus, and the whole-corpus English reader/export preflight.

The rendered scan controls Tamil. Verified Tamil song files control the English derivative. The complete-verified English translation records then control reader/export generation. No external recording, lyric website, subtitle, alternate edition, campaign text, commentary, or soundtrack-memory reconstruction is used to repair any layer.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Final Tamil lyric fidelity status

- draft: **0**;
- verified: **54** (`001–054`);
- review: **0**;
- not started: **0**;
- unresolved Tamil song readings: **0**.

The Tamil song corpus is **complete-verified** and immutable derivative input.

## English translation gate

The source-linked English translation corpus is **54/54 complete-verified** under `semantic-poetic-source-faithful` mode.

- `001–003`: **3 pilot-verified**;
- `004–054`: **51 verified**;
- draft/review/not-started: **0/0/0**;
- all 54 records remain `anthology-attributed`.

The approved English retains Kalaignar's language, rhetoric, repetition, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary and source-specific constructions. It is not a singable adaptation.

## Cross-page source records

The following eight songs span more than one song-bearing page and remain one record each across the Tamil, translation and reader-preflight layers:

- `009` — PDF 38–39;
- `019` — PDF 53–54;
- `023` — PDF 58–59;
- `024` — PDF 62–63;
- `036` — PDF 86–87;
- `037` — PDF 90–91;
- `051` — PDF 121–122;
- `052` — PDF 123–124.

## English reader/export preflight

**PASS.**

Authoritative report: `editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `editions/en/audit_probe.py`  
Workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

The automated run checks the translation records independently against `translations/index.json`, `songs/page-map.json`, and all 54 verified Tamil song files.

PASS results:

- translation record files: **54/54**;
- source-linked Tamil song files: **54/54**;
- anthology order: **001–054, no gaps**;
- item status distribution: **3 pilot-verified / 51 verified**;
- `anthology-attributed`: **54/54**;
- mapped Tamil lyric lines/cues: **1,105**;
- mapped English lines/cues: **1,105**;
- Tamil/English line-count mismatches: **0**;
- duplicate anthology song numbers: **0**;
- duplicate translation IDs: **0**;
- duplicate song IDs: **0**;
- duplicate translation record paths: **0**;
- source-page mismatches against the verified page map: **0**;
- Tamil-title mismatches: **0**;
- film-title mismatches: **0**;
- attribution drift: **0**;
- translation-mode drift: **0**;
- cross-page provenance mismatches: **0**;
- warnings/errors: **0/0**.

The preflight explicitly preserves the distinction between `pilot-verified` and `verified`, and it does not promote anthology attribution into original-film primary-source verification.

## Final gate result

- Tamil transcription: **complete-verified — 54/54**;
- Tamil fidelity audit: **complete**;
- English translation: **complete-verified — 54/54**;
- English reader/export preflight: **complete-pass**;
- deterministic reader/export package: **complete-verified**;
- generated-output QA: **PASS**;
- generated songs: **54/54**;
- generated English lines/cues: **1,105/1,105**;
- cross-page records: **8/8**;
- generated-output warnings/errors: **0/0**.

**PASS — the source-linked Tamil and English layers and the deterministic English reader/export derivative are all closed at their verified checkpoints.**

## Generated-output integrity

`editions/en/QA_REPORT.md` confirms that Markdown, standalone HTML and machine-readable JSON each retain the complete 54-song anthology order and all 1,105 English lines/cues. There are zero missing/extra/duplicate song IDs, translation IDs or line IDs, zero source-page/status/attribution drift and zero English text drift in the machine-addressable outputs.

`editions/en/manifest.json` hashes **110 authoritative inputs** and the generated Markdown, HTML, JSON and QA report. Output SHA-256 values are recorded in `metadata.yaml`.

## Reading Room integration payload gate

**PASS — payload complete-verified; site application not applied.**

`integrations/reading-room/QA_REPORT.md` independently verifies **23 film groups**, **54 songs**, **1,105 paired Tamil/English lines-cues**, all **8 cross-page songs**, the **3 pilot-verified / 51 verified** status history, and **54/54 anthology-attributed** records with zero source-page, Tamil-text, English-text, status or attribution drift.

The generated payload SHA-256 is `8ec0e25f7fc1f1a9750d370ccbef5dd07caa66629a3dfacb8425bbeebd08fcce`. Its manifest hashes the complete-verified reader payload, reader manifest, song index, page map, translation index and integration builder.

The downstream public-site repository has not been modified by this gate.

## Next activity

Actual Reading Room site application is the only remaining downstream action. It requires explicit authorization for the separate implementation repository. The archive and integration payload must remain immutable inputs to that UI work.

