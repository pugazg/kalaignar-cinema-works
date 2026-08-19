# Progress — கலைஞர் திரை இசைப் பாடல்கள்

## Current phase

**English reader/export — complete-verified; generated-output QA PASS.**

Both immutable source-linked content layers remain closed:

- Tamil songs: **54/54 complete-verified**;
- English translations: **54/54 complete-verified**.

The whole-corpus preflight passed, and deterministic Markdown, standalone HTML and machine-readable JSON reader derivatives have now been generated and reconciled without rewriting the verified English.

## Source/Tamil checkpoint

- physical PDF pages scanned: **194/194**;
- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs mapped: **54/54**;
- Tamil song files verified: **54/54**;
- Tamil draft/review/not-started: **0/0/0**;
- unresolved Tamil song readings: **0**.

## English translation checkpoint

- translated: **54/54**;
- pilot-verified: **3** (`001–003`);
- verified: **51** (`004–054`);
- draft/review/not-started: **0/0/0**;
- mode: **`semantic-poetic-source-faithful`**.

## Reader/export preflight

Automated preflight: **PASS**.

Report: `editions/en/PREFLIGHT_QA_REPORT.md`  
Probe: `editions/en/audit_probe.py`  
Workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

Passing checks include:

- **54/54** translation record files and **54/54** verified Tamil source links;
- anthology order **001–054** with no gaps;
- **3** `pilot-verified` + **51** `verified` statuses preserved;
- **54/54** records remain `anthology-attributed`;
- **1,105** mapped Tamil lyric lines/cues and **1,105** mapped English lines/cues;
- **0** line-count mismatches;
- **0** duplicate song numbers, translation IDs, song IDs or record paths;
- **0** source-page, Tamil-title or film-title mismatches;
- **0** translation-mode or attribution drift;
- exactly **8** cross-page records, matching the verified page map: `009`, `019`, `023`, `024`, `036`, `037`, `051`, `052`;
- **0 warnings / 0 errors**.

The preflight does not rewrite Tamil or English. Kalaignar-language decisions already fixed in the translation reviews remain immutable reader input.

## Deterministic reader/export package

Generated under `editions/en/`:

- `reader-edition.md` — **124,018 bytes**, SHA-256 `42e13ad7a171b4304ef4b1b8b424fa7f50ebace8510c7ea864f49c31dc9cc209`;
- `reader-edition.html` — **187,842 bytes**, SHA-256 `d48bd5476ba3cbdc540334abaf743b4481d0a1b7cae37d5bc4198f15adebc034`;
- `reader-edition.json` — **354,382 bytes**, SHA-256 `8e9782ca160e07bd9f45be38931d3d3ad07c3a126a0be6755b67e7e7fdec1ed8`;
- `QA_REPORT.md` — generated-output QA **PASS**;
- `manifest.json` — deterministic checkpoint across **110 authoritative inputs** and all publication outputs.

Generated-output QA confirms **54/54 songs**, **1,105/1,105 English lines/cues**, **8/8 cross-page records**, the **3 pilot-verified / 51 verified** distinction, and **54/54 anthology-attributed** states with zero missing/extra/duplicate IDs, zero text drift, and **0 warnings / 0 errors**.

Kalaignar-language English is copied exactly from the verified records; the reader build performs no stylistic smoothing.

## Next activity

No required repository-internal transcription, translation, preflight, or reader/export work remains. The work is ready for **downstream Kalaignar Digital Library / Reading Room integration**, preserving anthology order, provenance, item-status history, attribution discipline and the source-faithful English.

