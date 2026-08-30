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

- `reader-edition.md` — **123,907 bytes**, SHA-256 `30c807ede63949b5c600a6ab3a2d3cbe49eeb6f1b42f1dcd9538a0b3c9939b8c`;
- `reader-edition.html` — **187,731 bytes**, SHA-256 `690bea2680cdd6d0e6c0ab0eb4785d3cefebb319619e96a90915563ae96dda99`;
- `reader-edition.json` — **354,314 bytes**, SHA-256 `f7b0143c8b02618ddb78f0d0b6c5c22ffb542ee1b230529442d8ab7026ead344`;
- `QA_REPORT.md` — generated-output QA **PASS**;
- `manifest.json` — deterministic checkpoint across **110 authoritative inputs** and all publication outputs.

Generated-output QA confirms **54/54 songs**, **1,105/1,105 English lines/cues**, **8/8 cross-page records**, the **3 pilot-verified / 51 verified** distinction, and **54/54 anthology-attributed** states with zero missing/extra/duplicate IDs, zero text drift, and **0 warnings / 0 errors**.

Kalaignar-language English is copied exactly from the verified records; the reader build performs no stylistic smoothing.

## Reading Room integration payload

A deterministic, source-linked Reading Room payload has been prepared under `integrations/reading-room/`.

QA status: **PASS**.

- film groups: **23/23**;
- songs: **54/54**;
- paired Tamil/English lines-cues: **1,105/1,105**;
- cross-page songs: **8/8**;
- item status history: **3 pilot-verified + 51 verified**;
- attribution: **54/54 anthology-attributed**;
- Tamil text drift: **0**;
- English text drift: **0**;
- warnings/errors: **0/0**;
- payload SHA-256: `8ec0e25f7fc1f1a9750d370ccbef5dd07caa66629a3dfacb8425bbeebd08fcce`.

The payload groups songs by the anthology's 23 film sections while preserving canonical song order `001–054`. It carries source pages, exact archival IDs/paths, printed film/year/music/voice metadata where available, section labels and every verified Tamil/English line.

The public-site implementation itself remains **not applied**; this repository has prepared and verified the downstream contract only.

## Next activity

Apply the complete-verified payload in the separate Kalaignar Digital Library / Reading Room implementation repository **only when that repository is explicitly authorized for modification**. No Tamil, translation, reader/export or integration-payload text should be rewritten for UI convenience.

