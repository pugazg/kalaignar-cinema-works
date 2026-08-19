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

The Tamil corpus is **54/54 complete-verified** and is immutable source input for derivatives.

## English derivative

English translation lives separately under `../translations/`:

- status: **complete-verified**;
- translated: **54/54**;
- pilot-verified: **001–003**;
- verified: **004–054**;
- draft/review/not-started: **0/0/0**;
- mode: **`semantic-poetic-source-faithful`**;
- governing guide: `../../../docs/SONG_TRANSLATION_GUIDE.md`;
- final review: `../translations/BATCH_047_054_REVIEW.md`.

The English layer retains Kalaignar's language and does not rewrite these verified Tamil song files for smoothness, rhyme or singability. All eight multi-page songs retain complete source-page provenance in the translation index, including final-batch records `051` (PDF 121–122) and `052` (PDF 123–124).

## Next derivative activity

Run whole-corpus English reader/export preflight across all 54 source-linked translation records without altering the complete-verified Tamil or English source layers.
