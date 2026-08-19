# Song layer — கலைஞர் திரை இசைப் பாடல்கள்

Song files are created only from actual numbered lyric pages/direct continuation pages in the supplied PDF. This page-driven rule applies only to this PDF.

Authoritative page map: `page-map.json`.  
Full scan ledger: `../notes/FULL_PDF_SONG_PAGE_SCAN.md`.

## Current state

- songs located: **54/54**;
- draft: **0**;
- verified: **001–054 — 54**;
- review: **0**;
- not started: **0**;
- Tamil transcription: **complete-verified**;
- Tamil fidelity audit: **complete**;
- latest Tamil review: `../notes/FINAL_DRAFT_001_003_REVIEW.md`;
- next unprocessed song-bearing page: **none**.

Every numbered lyric record has been transcribed and visually verified from its mapped song-bearing page(s).

## Rules

- Render before transcription.
- Preserve exact source line order, labels, punctuation, ellipses, colloquial/unusual spellings and music/voice lines.
- Keep multi-page songs in one file.
- Do not create files from metadata/title-list/prose pages.
- Do not infer absent singers or import missing lyrics.
- Default attribution remains `anthology-attributed` unless stronger source evidence is separately established.

## Final Tamil gate

Songs `001–003` were the final pilot drafts. Direct reinspection of PDF 26, 29 and 30 closed that gate:

- `001`: `அறியான்டி` confirmed as the source spelling; `வேணசெல்வம்`, `பெண்ணி`, `ஏழைக்கிக்` retained;
- `002`: no lyric correction required;
- `003`: uncertainty markers resolved as `வந்தேன் தவழ்ந்தாய்?` and `பாழான`.

The Tamil corpus is therefore **54/54 complete-verified** and must be treated as immutable translation input.

## English derivative

English translation lives separately under `../translations/`:

- status: **in progress**;
- translated: **39/54**;
- pilot-verified: **001–003**;
- verified: **004–039**;
- draft/review: **0/0**;
- not started: **040–054 — 15 songs**;
- mode: **`semantic-poetic-source-faithful`**;
- governing guide: `../../../docs/SONG_TRANSLATION_GUIDE.md`;
- scaled reviews: `../translations/BATCH_004_011_REVIEW.md`, `../translations/BATCH_012_018_REVIEW.md`, `../translations/BATCH_019_025_REVIEW.md`, `../translations/BATCH_026_032_REVIEW.md`, `../translations/BATCH_033_039_REVIEW.md`;
- next English batch: **040–046**.

The English layer must retain Kalaignar's language and must never rewrite these verified Tamil song files for smoothness, rhyme or singability. Multi-page English records `036` (PDF 86–87) and `037` (PDF 90–91) now retain their complete source-page provenance alongside the earlier cross-page records.
