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
- verified: `004–025` — **22**;
- review: **0**;
- not started: `026–054` — **29**.

Latest review: `notes/PAGE_BATCH_064_REVIEW.md`.

Latest verified page run:

- PDF 64 → song 025.

Safeguards for song 025:

- one single-page record from PDF/printed 64;
- music `டி.ஆர்.பாப்பா`;
- voice `டி.வி. ரத்னம்`;
- retain the repeated `மாயக்காரா`, `ஜாலக்காரா`, `பகவானே` wording and parenthesized refrain;
- preserve source hyphenation and source-visible forms including `ஆடவாராய்`, `காணக்கிடைக்கா`, `தேனுறும்`, and `வேலைப் பழிக்கும்`;
- do not normalize from soundtrack familiarity or import absent verses.

## Exact next activity

Process **PDF 65 → song 026**, then continue strictly by the page whitelist.

Do not begin English translation until the relevant Tamil song is verified.

## Repository boundary

Work only inside `pugazg/kalaignar-cinema-works` unless explicitly instructed otherwise.
