# Progress — கலைஞர் திரை இசைப் பாடல்கள்

## Current phase

**Tamil song transcription and fidelity verification — page-driven mode.**

The user has set a work-specific rule for this PDF: scan the page; if it contains an actual song lyric body, create/process the song file; otherwise ignore the page. This rule applies only to `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`.

## Full-PDF song-page scan

The complete **194-page PDF has been visually scanned** for actual song-bearing pages.

- physical pages scanned: **194**;
- song-bearing pages: **62**;
- non-song pages ignored for song-file creation: **132**;
- numbered songs represented: **54 (`001–054`)**;
- last song-bearing page: **PDF 130**.

Authoritative page whitelist:

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

See `notes/FULL_PDF_SONG_PAGE_SCAN.md` and `songs/page-map.json`.

## Counts

| Item | Status |
|---|---:|
| Physical PDF pages | 194 |
| Song-bearing PDF pages | 62 |
| Ignored PDF pages | 132 |
| Numbered songs | 54/54 mapped |
| Draft song files | 3 |
| Verified song files | 15 |
| Review song files | 0 |
| Not-started song files | 36 |
| English translations | 0 |

## Existing lyric files

### Draft — songs 001–003

- `001` — PDF 26 — draft;
- `002` — PDF 29 — draft;
- `003` — PDF 30 — draft.

These remain draft pending their dedicated line-by-line verification pass.

### Verified — songs 004–018

Previously verified:

- `004`–`011` — PDF 33–41, with `009` spanning PDF 38–39.

New page-driven checkpoint:

- `012` — PDF 44 — verified;
- `013` — PDF 45 — verified;
- `014` — PDF 46 — verified;
- `015` — PDF 47 — verified;
- `016` — PDF 48 — verified;
- `017` — PDF 49 — verified;
- `018` — PDF 50 — verified.

Latest page review: `notes/PAGE_BATCH_044_050_REVIEW.md`.

## Page-driven processing rule

1. follow `songs/page-map.json` in ascending PDF-page order;
2. inspect the rendered page before transcription;
3. if it is song-bearing, create/update the corresponding `song-NNN.md`;
4. if it is not song-bearing, skip it completely for lyric-file work;
5. multi-page lyrics remain one song file;
6. do not create files from title lists, film metadata or prose mentions;
7. do not import missing lyrics from outside the PDF.

## Next activity

**Skip PDF 51–52.** They are classified as non-song pages.

Resume at the next whitelist entry:

- **PDF 53–54 → song 019**.

Then continue only through subsequent song-bearing pages.

Do not begin English translation before the relevant Tamil lyric is verified.
