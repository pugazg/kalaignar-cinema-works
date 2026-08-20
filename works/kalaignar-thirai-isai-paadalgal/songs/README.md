# Song layer — கலைஞர் திரை இசைப் பாடல்கள்

Song files are created only from actual numbered lyric pages/direct continuation pages in the supplied PDF. This page-driven rule applies only to the completed 2024 source witness.

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

Every numbered lyric record in the completed 2024 source track has been transcribed and visually verified from its mapped song-bearing page(s).

## 1989 source-witness deduplication

The additional first-edition witness `TVA_BOK_0065773` contains **40 numbered source sections**. Before adding anything to this folder, all 40 were checked against the existing verified song layer.

**All 40 are already represented here. No new lyric file was added.**

- source sections checked: **40/40**;
- distinct existing song records matched: **39**;
- new unique songs found: **0**;
- existing song files modified: **0**;
- `index.json` additions: **0**.

The count is 39 distinct existing records because the 1989 source separately numbers sections **4** and **13**, while the completed 2024 source preserves both portions together in `song-009.md`.

Detailed mapping and the non-obvious lyric-level checks are recorded in `SOURCE_WITNESS_0065773_DEDUP.md`.

Source-witness differences in wording, role labels, segmentation or omissions are not merged into these verified 2024 files. They remain source-level evidence under `../sources/tva-bok-0065773/`.

## Rules

- Render before transcription.
- Preserve exact source line order, labels, punctuation, ellipses, colloquial/unusual spellings and music/voice lines.
- Keep multi-page songs in one file.
- Do not create files from metadata/title-list/prose pages.
- Do not infer absent singers or import missing lyrics.
- Default attribution remains `anthology-attributed` unless stronger source evidence is separately established.
- When another witness contains the same underlying song, do **not** create a duplicate song file merely because its heading, segmentation or wording varies.

## Final Tamil gate

The 2024 corpus is **54/54 complete-verified** and is immutable source input for derivatives.

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

## Downstream derivative status

The English translation and deterministic English reader/export package are both complete-verified. Generated-output QA passes for **54/54 songs** and **1,105/1,105 English lines/cues** with no alteration to this Tamil source layer.

No further source-layer song addition is required from the 1989 witness under the current no-duplicate rule. Downstream Reading Room integration may proceed from the verified derivatives.
