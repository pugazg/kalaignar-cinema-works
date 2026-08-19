# கலைஞர் திரை இசைப் பாடல்கள்

Source-led archival work for the supplied anthology **`கலைஞர் திரை இசைப் பாடல்கள்`**, compiled by **நெல்லை ஜெயந்தா** and published by **தமிழ்நாடு இயல் இசை நாடக மன்றம்**.

This is a **song anthology work**, not a screenplay/dialogue-booklet work.

## Source checkpoint

- source filename: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`;
- archive identifier: `TVA_BOK_0065867`;
- physical PDF pages: **194**;
- source SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`;
- printed title: **`கலைஞர் திரை இசைப் பாடல்கள்`**;
- compiler: **`நெல்லை ஜெயந்தா`**;
- First Edition: **June 2024**;
- printed `No of pages`: **192**;
- ISBN: **978-81-961205-2-8**;
- publisher: **தமிழ்நாடு இயல் இசை நாடக மன்றம்**.

The rendered scan controls. OCR is navigation only.

## New PDF-specific page rule

The user has explicitly changed the operating method **for this PDF only**:

> Scan the page. If it contains a song, create/process the song file. Otherwise ignore it.

The entire **194-page PDF has now been visually scanned first**, before further lyric work.

For this work, a page counts as song-bearing only when it contains an actual numbered lyric body or directly continues one. A song title in a list, prose mention, film metadata, photograph, contents page, historical/biographical page, bibliography or back matter does not qualify.

### Full scan result

- pages scanned: **194/194**;
- song-bearing pages: **62**;
- ignored pages: **132**;
- numbered songs represented: **54 (`001–054`)**;
- final song-bearing page: **PDF 130**.

Song-bearing page whitelist:

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

Authoritative documents:

- `notes/FULL_PDF_SONG_PAGE_SCAN.md` — human-readable full scan ledger;
- `songs/page-map.json` — machine-readable song number → PDF page map.

The older film-section map remains descriptive metadata only. It no longer decides what gets processed.

## Current lyric status

- song locations mapped: **54/54**;
- draft lyric records: **3** (`001–003`);
- verified lyric records: **8** (`004–011`);
- review: **0**;
- not started: **43** (`012–054`);
- English translation: **not started**;
- reader/export: **not started**.

Songs 004–011 were visually verified from their actual lyric pages PDF 33–41. Song 009 is a two-page lyric across PDF 38–39.

The first three records remain draft pending their dedicated fidelity pass.

## Important exclusions

- PDF 25's prose mention of `ஆளப்பிறந்தவன் தமிழன் அவன்தானே` does **not** generate a song file because the lyric body is absent.
- Metadata/list pages such as PDF 27–28, 31–32 and 42–43 are ignored for lyric-file creation.
- PDF 131–194 contains no numbered lyric sheet and is ignored under this workflow.

## Attribution rule

This 2024 anthology controls what this edition prints and attributes. Default attribution status remains **`anthology-attributed`**. Do not silently promote that to original-film `primary-source-verified` authorship without separate evidence.

## Key documents

- `metadata.yaml`
- `mapping.md`
- `PROGRESS.md`
- `AUDIT.md`
- `PROJECT_HANDOVER.md`
- `notes/FULL_PDF_SONG_PAGE_SCAN.md`
- `notes/BATCH_004_011_REVIEW.md`
- `songs/README.md`
- `songs/page-map.json`
- `songs/index.json`

## Exact next activity

Resume at **PDF 44 / song 012**, the next unprocessed song-bearing page.

From there, process only pages in `songs/page-map.json`, in ascending PDF order. Skip every intervening non-song page without creating a file. Do not begin English translation yet.
