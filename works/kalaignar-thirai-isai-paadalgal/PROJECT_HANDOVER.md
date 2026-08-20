# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Treat current GitHub `main` and current workflow state as authoritative over stale SHAs/status prose. Read completely before changing this work:

- `PROJECT_HANDOVER.md`
- `CONTINUATION_GUIDELINES.md`
- `NEXT_CHAT_PROMPT.md`
- `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`
- `notes/FULL_PDF_SONG_PAGE_SCAN.md`
- `songs/page-map.json`, `songs/index.json`
- `translations/README.md`, `translations/index.json`, `translations/PILOT_REVIEW.md`, all batch reviews through `BATCH_047_054_REVIEW.md`
- `editions/en/PREFLIGHT_QA_REPORT.md`, `editions/en/QA_REPORT.md`, `editions/en/manifest.json`, `editions/en/audit_probe.py`, `editions/en/build.py`
- `integrations/reading-room/README.md`, `integrations/reading-room/build.py`, `integrations/reading-room/sync_status.py`
- `docs/SONG_TRANSLATION_GUIDE.md`
- `.github/workflows/kalaignar-song-anthology-english-preflight.yml`

Then inspect current `main`, recent commits and the latest workflow run before acting.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 194 physical PDF pages;
- SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- image-only source;
- rendered scan controls Tamil readings.

Process only actual numbered lyric pages/direct continuations. The full PDF classification is **62 song-bearing / 132 ignored pages / 54 numbered songs**. Never import absent lyrics from elsewhere.

## Closed source-linked layers — do not restart

### Tamil

- verified `001–054`: **54/54**;
- Tamil transcription: **complete-verified**;
- fidelity audit: **complete**;
- unresolved readings: **0**.

### English

- translated: **54/54 complete-verified**;
- **3 pilot-verified + 51 verified**;
- mode: `semantic-poetic-source-faithful`;
- attribution: **54/54 `anthology-attributed`**;
- mapped Tamil/English line cues: **1,105 / 1,105**.

Do not smooth the verified English into generic lyric English. Retain Kalaignar's repetition, rhetoric, political/social force, concrete imagery, colloquial energy, culture-bearing vocabulary, performance terms and documented source pressure points.

Exactly eight songs are cross-page and must retain complete provenance: `009` 38–39, `019` 53–54, `023` 58–59, `024` 62–63, `036` 86–87, `037` 90–91, `051` 121–122, `052` 123–124.

## Reader/export checkpoint

English preflight and deterministic reader/export are **complete-verified / PASS**. The reader contains 54 songs and 1,105 paired line cues with 0 warnings/errors at the completed checkpoint. Generated reader files must not be hand-edited; rebuild from authoritative structured inputs.

## Reading Room integration checkpoint

Repository-internal integration preparation is now active.

Created under `integrations/reading-room/`:

- `README.md` — downstream authority/navigation/language/search/attribution/provenance contract;
- `build.py` — deterministic Reading Room payload builder and QA;
- `sync_status.py` — repository status synchronizer.

The existing workflow `.github/workflows/kalaignar-song-anthology-english-preflight.yml` has been extended so the verified English reader gate is followed by Reading Room payload build/QA and status synchronization.

The payload contract expects:

- **23 film groups** in first-appearance order;
- **54 songs** in anthology order `001–054`;
- **1,105** paired Tamil/English line cues;
- Tamil/English titles and lyrics unchanged from verified layers;
- printed film year/music/voice metadata where available;
- exact source PDF page arrays;
- immutable source paths and archival IDs;
- `3 pilot-verified + 51 verified` history;
- `54/54 anthology-attributed` status;
- presentation guidance for film → song navigation and Tamil/English/parallel display.

The public website remains downstream. Search normalization must not overwrite stored text, and `anthology-attributed` must not be promoted to primary-source-verified original-film authorship without separate upstream evidence.

## Recent implementation commits

The integration-preparation sequence introduced/refined the Reading Room builder, synchronizer and workflow, including the workflow checkpoint commit `0b8d833bf4696b30e7a0d1a16679105aa0c4c026` (`Build Reading Room payload after reader QA`). Continuation documents were then added/refreshed. Do not treat these SHAs as more authoritative than live `main` in a future chat.

## Exact next activity

1. Inspect live `main` and the latest workflow run.
2. Check whether these generated outputs now exist:
   - `integrations/reading-room/reading-room.json`
   - `integrations/reading-room/QA_REPORT.md`
   - `integrations/reading-room/manifest.json`
3. If present, verify QA **PASS**, expected 23/54/1,105 totals, anthology order, attribution/status history, all eight cross-page provenance arrays, manifest integrity and synchronized status.
4. If absent or the workflow failed, diagnose/fix the integration build/workflow without reopening verified Tamil/English layers merely for UI convenience.
5. When payload QA is PASS, mark the **repository-internal Reading Room integration-preparation gate complete** and refresh status/handover documents.
6. Only after that, and only when explicitly in scope, apply the verified payload to the separate Kalaignar Digital Library / Reading Room implementation repository.

## Repository boundary

This handover does **not** claim that `nenjukkuneethi.org/read` has been updated. Work only inside `pugazg/kalaignar-cinema-works` until the Reading Room implementation repository is explicitly brought into scope.
