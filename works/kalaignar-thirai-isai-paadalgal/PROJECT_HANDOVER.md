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
10. repository source/transcription guides as needed.

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

Important exclusions:

- PDF 25 mentions `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` in prose but does not print its lyric body; do not create a song file from that page.
- PDF 131–194 contains no numbered lyric sheet under this scan and is ignored for lyric-file creation.

## Current lyric checkpoint

- `001–003`: draft;
- `004–011`: verified;
- `012–054`: not started.

Totals:

- verified: **8**;
- draft: **3**;
- review: **0**;
- not started: **43**.

Latest verified batch: `notes/BATCH_004_011_REVIEW.md`.

## Attribution rule

This is a 2024 anthology. Default item attribution is `anthology-attributed` unless separately strengthened by original-film evidence. The page-driven processing rule changes **what pages are processed**, not the evidentiary standard for authorship.

## Exact next activity

Start at **PDF 44 / song 012**.

Then continue strictly through `songs/page-map.json` in ascending page order:

- process the lyric page(s);
- create/update the corresponding `song-NNN.md`;
- visually verify before marking `verified`;
- skip every non-song page completely;
- after PDF 50 jump to PDF 53; after PDF 59 jump to PDF 62; continue according to the whitelist through PDF 130.

Do not perform film-section metadata work unless it is needed to interpret text printed directly on a song-bearing page. Do not begin English translation until the relevant Tamil lyric is verified.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless the user explicitly requests another repository.
