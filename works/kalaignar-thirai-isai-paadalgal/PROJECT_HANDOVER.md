# Project handover — கலைஞர் திரை இசைப் பாடல்கள்

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work path: `works/kalaignar-thirai-isai-paadalgal/`

## Mandatory startup

Read current `README.md`, `metadata.yaml`, `PROGRESS.md`, `AUDIT.md`, `notes/FULL_PDF_SONG_PAGE_SCAN.md`, `songs/page-map.json`, `songs/index.json`, and the latest page-batch review before changing this work. Current GitHub `main` is authoritative.

## Controlling source

`TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`

- 194 physical PDF pages;
- SHA-256 `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- image-only source;
- rendered scan controls.

## Critical rule — this PDF only

Process only actual numbered lyric pages/direct continuations. Ignore every non-song page for lyric-file creation. Multi-page lyrics remain one song file. Never import absent lyrics from elsewhere.

The full PDF was already visually classified: **62 song-bearing / 132 ignored pages / 54 numbered songs**. Use `songs/page-map.json`; do not revert to film-section batching.

## Current checkpoint

- draft: `001–003` — **3**;
- verified: `004–024` — **21**;
- review: **0**;
- not started: `025–054` — **30**.

Latest review: `notes/PAGE_BATCH_062_063_REVIEW.md`.

Latest verified page run:

- PDF 62–63 → song 024.

Safeguards for song 024:

- one cross-page record across PDF 62–63;
- music `டி.ஆர்.பாப்பா`;
- voice `சி.எஸ்.ஜெயராமன்`;
- retain `(பொதுநலம்)` cues;
- preserve source forms including `மிகபுனிதமான`, `நம்நாடு`, `நந்நாடு`, `மனிதனுக்குயிர்`, `திருவோடேந்தும்`, `நடைபிணத்துக்குயிர்`, and `கடமைகளுக்கொளி`;
- do not normalize source hyphenation.

## Exact next activity

Process **PDF 64 → song 025**, then continue strictly by the page whitelist.

Do not begin English translation until the relevant Tamil song is verified.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
