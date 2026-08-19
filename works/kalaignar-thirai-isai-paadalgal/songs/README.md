# Song layer — கலைஞர் திரை இசைப் பாடல்கள்

This directory stores song files created from the supplied anthology **only when the rendered PDF page contains an actual numbered lyric body or a direct continuation of one**.

## PDF-specific operating rule

This rule applies only to `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`.

The entire 194-page PDF has been visually scanned. The authoritative whitelist is stored in `page-map.json` and documented in `../notes/FULL_PDF_SONG_PAGE_SCAN.md`.

- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs represented: **54 (`001–054`)**.

A page containing only a song title, film metadata, prose mention, photograph, contents/list, historical text, bibliography, note or back matter does **not** create a song file.

## Song-bearing page whitelist

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

Machine-readable map: `page-map.json`.

## Authority

Each `song-NNN.md` is a transcription derivative of the corresponding numbered lyric page(s) in this supplied 2024 anthology.

The anthology controls the numbered lyric text, song number, source-visible music/voice metadata, singer/character/turn labels, refrain/stanza labels, punctuation, lineation and source spellings.

Default authorship status remains `anthology-attributed`; this anthology is not silently treated as an original film-era source.

## Page-driven transcription rules

1. Follow `page-map.json` in ascending PDF-page order.
2. Open/render the page before creating or changing a song file.
3. Process only the listed song-bearing pages.
4. Skip all other pages without creating files.
5. Multi-page songs remain one `song-NNN.md` file.
6. Preserve source line order, labels, punctuation, ellipses, colloquial forms and unusual spellings.
7. Do not import missing verses from recordings, websites or another publication.
8. Keep uncertain readings visible until the rendered scan supports verification.

## Current state

- inventory/page map: **54/54 songs located**;
- draft: **001–003** — 3 songs;
- verified: **004–018** — 15 songs;
- review: **0**;
- not started: **019–054** — 36 songs;
- latest review: `../notes/PAGE_BATCH_044_050_REVIEW.md`;
- next unprocessed song-bearing page: **PDF 53–54 / song 019**.

PDF 51–52 are non-song pages and must be skipped.

English translation remains blocked until the relevant Tamil lyric is verified.
