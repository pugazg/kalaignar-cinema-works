# Full-PDF song-page scan — கலைஞர் திரை இசைப் பாடல்கள்

Source: `TVA_BOK_0065867_கலைஞர்_திரை_இசைப்_பாடல்கள்.pdf`  
Physical PDF pages scanned: **1–194**  
Source SHA-256: `f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05`

## Work-specific rule from this checkpoint

This rule applies **only to this supplied PDF**.

From now on, processing is **page-driven**:

1. inspect the rendered PDF page;
2. if the page contains an actual numbered song lyric body, or is a direct continuation of one, process it into the corresponding `songs/song-NNN.md` file;
3. if the page contains only cover/front matter, prose, film metadata, a song-title list, photograph, contents, biography/history, bibliography, notes or back matter, ignore it for song-file creation;
4. a mere song title or prose mention is **not** enough to create a song file;
5. never import missing lyrics from outside this PDF.

The older film-section batching remains useful as descriptive metadata, but it no longer determines what gets processed.

## Full scan result

**PASS — all 194 physical PDF pages were visually scanned for song-bearing content.**

- physical pages scanned: **194**;
- song-bearing pages: **62**;
- non-song pages to ignore for song-file creation: **132**;
- numbered songs represented: **54 (`001–054`)**;
- last song-bearing page: **PDF 130**;
- PDF 131–194 contains no numbered lyric page and is out of scope for song-file creation under this rule.

### Song-bearing PDF pages

`26, 29–30, 33–41, 44–50, 53–59, 62–67, 70, 73–74, 77, 80, 83–84, 86–87, 90–94, 97, 100, 103, 106, 109–110, 113, 116–117, 120–124, 127, 130`

### Non-song PDF pages — ignore for song-file creation

`1–25, 27–28, 31–32, 42–43, 51–52, 60–61, 68–69, 71–72, 75–76, 78–79, 81–82, 85, 88–89, 95–96, 98–99, 101–102, 104–105, 107–108, 111–112, 114–115, 118–119, 125–126, 128–129, 131–194`

## Song number → actual lyric page map

| Song | PDF page(s) |
|---|---:|
| 001 | 26 |
| 002 | 29 |
| 003 | 30 |
| 004 | 33 |
| 005 | 34 |
| 006 | 35 |
| 007 | 36 |
| 008 | 37 |
| 009 | 38–39 |
| 010 | 40 |
| 011 | 41 |
| 012 | 44 |
| 013 | 45 |
| 014 | 46 |
| 015 | 47 |
| 016 | 48 |
| 017 | 49 |
| 018 | 50 |
| 019 | 53–54 |
| 020 | 55 |
| 021 | 56 |
| 022 | 57 |
| 023 | 58–59 |
| 024 | 62–63 |
| 025 | 64 |
| 026 | 65 |
| 027 | 66 |
| 028 | 67 |
| 029 | 70 |
| 030 | 73 |
| 031 | 74 |
| 032 | 77 |
| 033 | 80 |
| 034 | 83 |
| 035 | 84 |
| 036 | 86–87 |
| 037 | 90–91 |
| 038 | 92 |
| 039 | 93 |
| 040 | 94 |
| 041 | 97 |
| 042 | 100 |
| 043 | 103 |
| 044 | 106 |
| 045 | 109 |
| 046 | 110 |
| 047 | 113 |
| 048 | 116 |
| 049 | 117 |
| 050 | 120 |
| 051 | 121–122 |
| 052 | 123–124 |
| 053 | 127 |
| 054 | 130 |

Machine-readable equivalent: `../songs/page-map.json`.

## Important exclusions established by the scan

- PDF 25 mentions the censored/prohibited `ஆளப்பிறந்தவன் தமிழன் அவன்தானே`, but it does not print a numbered lyric body. **No song file is created from PDF 25.**
- Film-information pages and song-list pages such as PDF 27–28, 31–32, 42–43, etc. are metadata/context only. They are ignored for song-file creation.
- Later historical/biographical sections PDF 131–194 contain no numbered lyric sheets. They are ignored for this activity.

## Existing files at this checkpoint

Already present:

- `001–003` — draft;
- `004–011` — verified.

No new lyric file was created during this full-PDF scan checkpoint. The purpose of this activity was only to establish the authoritative page whitelist before continuing.

## Exact next processing rule

Resume at the **next unprocessed song-bearing page, PDF 44 (`012`)**. Process song-bearing pages only, in ascending PDF order. Skip all intervening non-song pages without creating files or doing film-section work.
