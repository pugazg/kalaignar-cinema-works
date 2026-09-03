# Raja Rani — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Active work: `works/raja-rani/` — **ராஜா ராணி**

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first in every fresh chat. Preserve any newer durable state. Do not reset, repeat or reopen completed work merely because this handover records an older checkpoint.

## Controlling source

- filename: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- canonical screenplay/dialogue range: PDF **10–79**, printed pp. **9–78**
- PDF 80: unnumbered back cover

Comparison files `r1.md`–`r4.md`, OCR and parsed PDF text are candidate/navigation aids only. The rendered source scan and recorded direct user scan verdicts control canonical Tamil.

## Mandatory startup

Read completely before changing anything:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. this handover
7. `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/notes/final-source-review-resolution.md`
10. `works/raja-rani/notes/post-fidelity-corrections.md`
11. `works/raja-rani/notes/correction-005-reconciliation.md`
12. `works/raja-rani/translations/README.md`
13. `works/raja-rani/translations/index.json`
14. `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`
15. `works/raja-rani/songs/index.json`
16. `works/raja-rani/songs/inventory.json`
17. the verified Tamil song derivatives for the numbered-song batch.

## Permanent source rules

- rendered scan evidence controls disputed characters;
- OCR/parsed PDF/comparison text are candidate readings only;
- preserve user-reviewed occurrence-specific source verdicts and exact source speaker labels;
- source-unlabelled speech remains unlabelled;
- non-canonical ownership/library stamps are not screenplay text;
- no global normalization or silent reconstruction;
- translation never repairs Tamil or upgrades song authorship.

## Final source-review state — fully closed

There are **no review/source-blocked pages or scenes**.

Durable direct-scan verdicts include:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; canonical screenplay continues directly `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Current source census:

- verified source pages: **79/79**;
- verified screenplay pages: **70/70**;
- archival scenes: **58/58 verified**, blocked **0**;
- unique immutable dialogue records: **1,071** across all 58 scenes;
- zero-dialogue scenes: **16**;
- genuine cross-page dialogue records: **12**;
- exact speaker labels: **80/80**;
- entities / roles / collectives: **44**, all verified;
- numbered songs: **11/11 Tamil derivatives**; screenplay singing refs **4**; total occurrences **15**;
- song authorship: **5 later-anthology Kalaignar attributions / 6 unresolved**.

## T055 / T056 boundary correction — closed

Final English QA caught a derivative segmentation error: the older scene-55 derivative duplicated the complete `(முன்)` flashback that belongs to scene 56. This has been corrected without changing canonical page transcription.

Final disposition:

- scene 55 dialogue shard: **25 records**;
- scene 56 dialogue shard: **5 records**;
- corrected corpus dialogue census: **1,071**;
- no duplicate T055 source IDs remain eligible for English linkage.

Durable QA: `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Correction 005 — closed

The late old-glyph/source correction campaign is reconciled through canonical Tamil, scenes, dialogue records, character labels/entities, affected song derivatives/metadata and English. Durable record: `works/raja-rani/notes/correction-005-reconciliation.md`.

Do not revert permanent forms such as PDF 72 `சாக்ரடீசின்`, scene-17 exact label `தர்யம்`, scene-34 corrected `ராணி` ownership, final PDF 76–79 manual adjudications, or any final source-review verdict above.

## English screenplay translation — COMPLETE

All **58/58 archival scenes** have verified English records.

Final totals:

- translated scenes: **58/58**;
- verified English units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- source-unlabelled spoken units: **19**;
- genuine cross-page English units: **15**;
- screenplay performance/singing occurrences represented: **4/4**;
- unit mix: **1,090 dialogue / 137 stage direction / 4 performance cue / 5 written text**;
- draft/review screenplay units: **0**.

Final content reviews:

- `works/raja-rani/translations/BATCH_011_040_REVIEW.md`
- `works/raja-rani/translations/BATCH_041_058_REVIEW.md`
- `works/raja-rani/translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`

Do **not** reopen screenplay translation production merely because an older shared mirror says 30/58 or 715 units.

## Numbered-song English translation — exact next activity

The 11 front-matter numbered song bodies have verified Tamil derivatives but **0/11 English song translations**.

Translate **songs 1–11 in source order** through a dedicated source-linked song translation layer.

For every numbered song:

- use the verified Tamil song derivative as textual authority;
- preserve source PDF/printed-page provenance;
- use semantic-poetic English, retaining image, rhetorical force, repetition and unusual source wording;
- do not change canonical Tamil to improve the English;
- keep screenplay performance links only where already supported by the song inventory;
- never infer lyricist identity from translation, style or context;
- preserve authorship tiers exactly.

Current authorship dispositions:

- **later-anthology Kalaignar-attributed:** songs **3, 5, 6, 7, 8**;
- **unresolved lyricist:** songs **1, 2, 4, 9, 10, 11**;
- original-booklet item-level lyricist credits: **0**.

Scene 58's performance association with song 11 remains **review-level**. Do not upgrade it while translating the song body.

Before defining the English song schema/files, inspect the live `songs/schema.json`, `songs/index.json`, `songs/inventory.json`, and existing Tamil derivative naming conventions. Do not force song translations into screenplay scene IDs.

After all 11 numbered songs are translated, create a dedicated numbered-song English QA/review and only then mark the overall bilingual Raja Rani work complete.

## Shared repository mirrors

`data/works.json` and root `README.md` may lag the work-local checkpoint. Do not let stale shared mirrors override Raja Rani-local indexes, metadata, reviews or this handover.
