# Progress — கலைஞர் திரை இசைப் பாடல்கள்

## Current phase

**Tamil song transcription and fidelity verification — page-driven mode.**

The user has set a work-specific rule for this PDF: scan the page; if it contains an actual song lyric body, create/process the song file; otherwise ignore the page. This rule applies only to `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`.

## Full-PDF song-page scan

The complete **194-page PDF has now been visually scanned** for actual song-bearing pages.

- physical pages scanned: **194**;
- song-bearing pages: **62**;
- non-song pages ignored for song-file creation: **132**;
- numbered songs represented: **54 (`001–054`)**;
- last song-bearing page: **PDF 130**.

Authoritative page whitelist:

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

See:

- `notes/FULL_PDF_SONG_PAGE_SCAN.md`
- `songs/page-map.json`

Pages containing only film metadata, song-title lists, photographs, prose mentions, historical/biographical material, bibliography, notes or back matter are ignored for lyric-file creation. In particular, PDF 25's prose mention of `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` does not create a song file because no lyric body is printed there.

## Counts

| Item | Status |
|---|---:|
| Physical PDF pages | 194 |
| Song-bearing PDF pages | 62 |
| Ignored PDF pages | 132 |
| Numbered songs | 54/54 mapped |
| Draft song files | 3 |
| Verified song files | 8 |
| Review song files | 0 |
| Not-started song files | 43 |
| English translations | 0 |

## Existing lyric files

### Draft — songs 001–003

1. `001` — PDF 26 — draft;
2. `002` — PDF 29 — draft;
3. `003` — PDF 30 — draft.

These remain draft pending their dedicated line-by-line verification pass.

### Verified — songs 004–011

The song-bearing pages PDF **33–41** were transcribed and visually checked:

- `004` — PDF 33 — verified;
- `005` — PDF 34 — verified;
- `006` — PDF 35 — verified;
- `007` — PDF 36 — verified;
- `008` — PDF 37 — verified;
- `009` — PDF 38–39 — verified;
- `010` — PDF 40 — verified;
- `011` — PDF 41 — verified.

Batch review: `notes/BATCH_004_011_REVIEW.md`.

## Page-driven processing rule

From this checkpoint onward:

1. follow `songs/page-map.json` in ascending PDF-page order;
2. open the rendered page before doing anything;
3. if it is a song-bearing page, create/update the corresponding `song-NNN.md`;
4. if it is not song-bearing, skip it completely for this activity;
5. multi-page lyrics remain one song file;
6. do not use film-section boundaries as the processing unit;
7. do not create files from title lists or prose mentions;
8. do not import missing lyrics from outside the PDF.

## Next activity

The next unprocessed song-bearing page is **PDF 44**, corresponding to **song 012**.

Continue from PDF 44 using the page whitelist only. After PDF 50, jump directly to PDF 53; skip PDF 51–52. Continue this way through the final song-bearing page, PDF 130.

Do not begin English translation before the relevant Tamil lyric is verified.
