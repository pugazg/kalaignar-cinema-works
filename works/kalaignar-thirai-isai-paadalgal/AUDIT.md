# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Audit scope

This checkpoint covers **source intake + full 194-page song-presence scan + Tamil lyric work through numbered song 018**.

The full-PDF scan is a **page-classification audit**. Line-level verification is performed only when each song-bearing page is processed.

## Source binary

- filename: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`;
- size: 130,427,193 bytes;
- SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- physical PDF pages: **194**;
- source mode: image-only / rendered scan controls.

## Full-PDF song-page classification

**PASS — all 194 physical PDF pages were visually scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs represented: **54 (`001–054`)**;
- final song-bearing page: **PDF 130**;
- PDF 131–194 contains no numbered lyric page.

Song-bearing whitelist:

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

Full ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Current lyric fidelity status

### Draft songs 001–003

Songs 001–003 remain **draft** pending their dedicated line-by-line verification.

### Verified songs 004–011

**PASS — 8/8 records verified against PDF 33–41.**  
Detailed review: `notes/BATCH_004_011_REVIEW.md`.

### Verified songs 012–018

**PASS — 7/7 records verified against the next consecutive song-bearing pages PDF 44–50.**  
Detailed review: `notes/PAGE_BATCH_044_050_REVIEW.md`.

Important dispositions from PDF 44–50:

- all seven lyric pages print music `டி.ஆர்.பாப்பா`;
- none prints a separate `குரல்` line, so no singer was inferred;
- source role/performance labels remain exact where printed;
- song 014 and song 015 are separate numbered records even though they share the `காதல் துறையே புதுமைக் கனவே` material; song 015 is explicitly the sorrow version;
- source forms such as `உன்செயல்`, `விண்ண முதே`, `வெறுங்`, `மான் தோல்`, ellipses and refrain cues remain unnormalized.

Current totals:

- inventory: **54/54**;
- verified: **15** (`004–018`);
- draft: **3** (`001–003`);
- review: **0**;
- not started: **36** (`019–054`).

## Processing-policy rule

For this PDF only:

1. follow `songs/page-map.json` in ascending PDF order;
2. inspect and process song-bearing pages only;
3. skip non-song pages without creating files;
4. keep a multi-page lyric in one song file;
5. never create a file from a title-list/prose mention alone;
6. never import absent lyrics from elsewhere.

## Authorship / attribution

The 2024 anthology remains evidence for what this edition attributes. Default status stays `anthology-attributed`; page-driven processing does not upgrade item authorship to original-film primary-source verification.

## Open work

1. line-by-line fidelity recheck for songs 001–003;
2. **skip PDF 51–52**;
3. continue at **PDF 53–54 / song 019**;
4. proceed only through the whitelist until PDF 130;
5. whole-corpus reconciliation after all 54 song files exist;
6. English translation only after the relevant Tamil lyric is verified.
