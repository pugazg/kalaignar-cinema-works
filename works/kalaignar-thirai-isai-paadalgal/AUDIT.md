# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This audit covers:

1. the complete PDF-specific song-presence scan;
2. line-level Tamil lyric verification for all **54 numbered songs**;
3. the initial source-linked English translation pilot for songs **001–003**.

The rendered scan controls Tamil. Verified Tamil song files control the English derivative. No external recording, lyric website, subtitle, alternate edition, or soundtrack-memory reconstruction is used to repair either layer.

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

The Tamil song corpus is **complete-verified**.

Final draft-gate review: `notes/FINAL_DRAFT_001_003_REVIEW.md`.  
Final formerly not-started batch review: `notes/FINAL_PAGE_BATCH_065_130_REVIEW.md`.

The last Tamil gate directly resolved the early pilot records without outside text: song `001` corrected `அறியாண்டி` → source-visible `அறியான்டி`; song `002` required no lyric correction; song `003` resolved `வந்தேன் தவழ்ந்தாய்?` and `பாழான எந்தன் வயிற்றில் பிறந்தாய் ராஜா!` from PDF 30.

## Cross-page Tamil records

The following verified songs span more than one song-bearing page and remain one file each:

- `009` — PDF 38–39;
- `019` — PDF 53–54;
- `023` — PDF 58–59;
- `024` — PDF 62–63;
- `036` — PDF 86–87;
- `037` — PDF 90–91;
- `051` — PDF 121–122;
- `052` — PDF 123–124.

## PDF-specific Tamil processing rule

For this PDF only, process actual numbered lyric pages/direct continuations and ignore every other page for lyric-file creation. Do not import missing lyrics from elsewhere.

## English pilot gate

**PASS — songs 001–003 are `pilot-verified`.**

Translation authority and structure:

- guide: `docs/SONG_TRANSLATION_GUIDE.md`;
- schema: `translations/schema.json`;
- index: `translations/index.json`;
- detailed review: `translations/PILOT_REVIEW.md`;
- records: `translations/records/song-001.json` through `song-003.json`.

Pilot checks passed:

- all three source Tamil song files were already verified;
- each English record preserves song ID, anthology number and PDF provenance;
- every Tamil lyric line/cue in the pilot has an explicit English mapping;
- exact source turn/performance labels remain traceable and are not expanded by guess;
- no Tamil source file was modified during translation;
- no external lyric or audio source was imported;
- attribution remains `anthology-attributed` and is not strengthened merely because the English is reviewed.

## Kalaignar-language fidelity in English

The approved mode is **`semantic-poetic-source-faithful`**.

The pilot specifically verifies that English does not flatten Kalaignar's language:

- song `001`: rustic `di`, buffalo-calf refrain, seven-storey-mansion/begging contrast and leader/wealth satire remain audible;
- song `002`: lamp/flame repetition, young-peacock image, `sugarcane-Tamil`, `flower where dew sleeps`, `magnetic statue` and `live like honey` remain concrete;
- song `003`: splendour/roots reversal, ruined-womb image, repeated `Why were you born?`, bird/food image, `crores upon crores` and poor/grandee contrast remain intact.

The difficult verified source `வந்தேன் தவழ்ந்தாய்?` is not silently emended in translation; the pilot preserves its visible subject shift and documents the pressure point.

## Current gate result

- Tamil transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- English translation: **pilot-verified — 3/54**;
- English remaining: **51 songs**;
- reader/export: **not started**.

Next translation batch: **004–011** (`நாம்`), using the approved Kalaignar-language pilot rules.
