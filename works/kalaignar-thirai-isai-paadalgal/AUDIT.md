# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Audit scope

This checkpoint covers **source intake + full 194-page song-presence scan + Tamil lyric work through numbered song 011**.

The full-PDF scan is a **page-classification audit**, not a claim that every lyric line in all 54 songs has already been transcribed or verified.

## Source binary

- filename: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`;
- size: 130,427,193 bytes;
- SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- physical PDF pages: **194**;
- source mode: image-only / rendered scan controls.

## Full-PDF song-page classification

**PASS — all 194 physical PDF pages were visually scanned.**

Work-specific definition: a page is song-bearing only when it contains an actual numbered lyric body or is a direct continuation of one. Pages containing only title lists, film information, prose, photographs, contents, history/biography, bibliography, notes or back matter do not qualify.

Result:

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs represented: **54 (`001–054`)**;
- final song-bearing page: **PDF 130**;
- no numbered lyric page occurs on PDF 131–194.

Song-bearing whitelist:

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

Full ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

Important exclusion: PDF 25's prose mention of the censored/prohibited `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` is **not** treated as a song page because the lyric body is not printed there.

## Current lyric fidelity status

### Draft songs 001–003

Songs 001–003 remain **draft** pending dedicated line-by-line verification.

### Verified songs 004–011

**PASS — 8/8 records verified against their song-bearing pages PDF 33–41.**

Detailed review: `notes/BATCH_004_011_REVIEW.md`.

Current totals:

- inventory: **54/54**;
- verified: **8** (`004–011`);
- draft: **3** (`001–003`);
- review: **0**;
- not started: **43** (`012–054`).

## Processing-policy change

For this PDF only, film-section batching is no longer the work driver. Future processing must:

1. follow `songs/page-map.json` in ascending PDF order;
2. process song-bearing pages only;
3. skip all non-song pages without creating files;
4. keep a multi-page lyric in one song file;
5. never create a file from a title-list/prose mention alone;
6. never import absent lyrics from elsewhere.

## Authorship / attribution

The 2024 anthology remains evidence for what this edition attributes. Default status stays `anthology-attributed`; nothing in the page-scan policy upgrades item authorship to original-film primary-source verification.

## Open work

1. line-by-line fidelity recheck for songs 001–003;
2. continue from the next unprocessed song-bearing page, **PDF 44 / song 012**;
3. proceed only through the page whitelist until PDF 130;
4. whole-corpus reconciliation after all 54 song files exist;
5. English translation only after the relevant Tamil lyric is verified.
