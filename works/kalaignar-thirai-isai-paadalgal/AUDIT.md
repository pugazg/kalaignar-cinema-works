# Audit — கலைஞர் திரை இசைப் பாடல்கள்

## Scope

This checkpoint covers the **complete 194-page song-presence scan** and line-level Tamil lyric verification through numbered song **025**.

The rendered scan is authoritative. The full-PDF scan classifies pages; a song is marked verified only after its own song-bearing page(s) are visually checked.

## Full-PDF page classification

**PASS — 194/194 pages scanned.**

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs located: **54/54**;
- final song-bearing page: **130**.

Authoritative ledger: `notes/FULL_PDF_SONG_PAGE_SCAN.md`  
Machine map: `songs/page-map.json`

## Lyric fidelity status

- draft: **3** (`001–003`);
- verified: **22** (`004–025`);
- review: **0**;
- not started: **29** (`026–054`).

Verified page runs:

- PDF 33–41 → songs 004–011;
- PDF 44–50 → songs 012–018;
- PDF 53–59 → songs 019–023;
- PDF 62–63 → song 024;
- PDF 64 → song 025.

Latest detailed review: `notes/PAGE_BATCH_064_REVIEW.md`.

### Latest fidelity dispositions

- Song 025 is a single-page numbered lyric on PDF/printed page 64.
- Music `டி.ஆர்.பாப்பா` and voice `டி.வி. ரத்னம்` are taken directly from the numbered lyric page.
- Repeated `மாயக்காரா`, `ஜாலக்காரா`, `பகவானே`, the page's parenthesized refrain and source hyphenation are preserved.
- Source-visible forms including `ஆடவாராய்`, `காணக்கிடைக்கா`, `தேனுறும்`, and `வேலைப் பழிக்கும்` are not silently normalized.
- No external recording, lyric website or alternate edition supplied text.

## PDF-specific processing rule

For this PDF only, process actual numbered lyric pages/direct continuations and ignore every other page for lyric-file creation. Do not import missing lyrics from elsewhere.

## Next

Resume at **PDF 65 / song 026** and continue only through the whitelist.

Songs 001–003 still require their dedicated fidelity recheck before the Tamil corpus can become contiguous-complete.
