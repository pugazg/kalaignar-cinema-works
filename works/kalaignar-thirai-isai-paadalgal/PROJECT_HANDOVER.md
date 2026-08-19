# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup in a new chat

Read completely before changing this work:

1. `works/kalaignar-thirai-isai-paadalgal/README.md`
2. `works/kalaignar-thirai-isai-paadalgal/metadata.yaml`
3. `works/kalaignar-thirai-isai-paadalgal/notes/FULL_PDF_SONG_PAGE_SCAN.md`
4. `works/kalaignar-thirai-isai-paadalgal/songs/page-map.json`
5. `works/kalaignar-thirai-isai-paadalgal/PROGRESS.md`
6. `works/kalaignar-thirai-isai-paadalgal/AUDIT.md`
7. `works/kalaignar-thirai-isai-paadalgal/songs/README.md`
8. `works/kalaignar-thirai-isai-paadalgal/songs/index.json`
9. `works/kalaignar-thirai-isai-paadalgal/notes/BATCH_004_011_REVIEW.md`
10. `works/kalaignar-thirai-isai-paadalgal/notes/PAGE_BATCH_044_050_REVIEW.md`

Then inspect current GitHub `main`. Current repository state is authoritative over older status text.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- size: `130427193` bytes;
- SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- physical PDF pages: **194**;
- image-only source;
- rendered scan controls;
- do not use OCR or soundtrack memory as authority.

## Critical PDF-specific rule — do not generalize

The user explicitly instructed that **only for this PDF** the work must be page-driven:

1. scan/render the page;
2. if an actual song lyric body is present, create/process the song file;
3. if not, ignore the page;
4. title lists, film metadata, prose mentions, photographs, contents, history/biography, bibliography, notes and back matter do not generate song files;
5. a multi-page lyric remains one song file;
6. do not import missing lyrics from any outside source.

Do **not** revert to film-section batching as the work driver.

## Full 194-page scan checkpoint

The full PDF has already been visually scanned.

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs represented: **54 (`001–054`)**;
- final song-bearing page: **130**.

Song-bearing whitelist:

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

Human-readable scan ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Current lyric checkpoint

- `001–003`: draft;
- `004–018`: verified;
- `019–054`: not started.

Totals:

- verified: **15**;
- draft: **3**;
- review: **0**;
- not started: **36**.

Latest verified page batch: `notes/PAGE_BATCH_044_050_REVIEW.md`.

### PDF 44–50 safeguards

- Seven song-bearing pages produced songs 012–018.
- All seven pages print music `டி.ஆர்.பாப்பா`.
- None prints a separate `குரல்` line; do not infer singers.
- Preserve source role/performance labels and refrain cues exactly.
- Song 014 and song 015 are separate numbered records; song 015 is the source-marked sorrow version.
- Preserve source-visible forms including `உன்செயல்`, `விண்ண முதே`, `வெறுங்`, and `மான் தோல்`.

## Attribution rule

This is a 2024 anthology. Default item attribution is `anthology-attributed` unless separately strengthened by original-film evidence. Page-driven processing changes **what pages are processed**, not the evidentiary standard for authorship.

## Exact next activity

**Skip PDF 51–52.** They are non-song pages.

Resume at **PDF 53–54 / song 019** and continue strictly through `songs/page-map.json` in ascending page order.

For every whitelist entry:

- inspect the rendered page(s);
- create/update the corresponding `song-NNN.md`;
- visually verify before marking `verified`;
- skip every intervening non-song page completely.

Do not begin English translation until the relevant Tamil lyric is verified.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless the user explicitly requests another repository.
