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
14. the current batch's live Tamil scene files and immutable dialogue shards.

## Permanent source rules

- rendered scan evidence controls disputed characters;
- OCR/parsed PDF/comparison text are candidate readings only;
- preserve user-reviewed occurrence-specific source verdicts and exact source speaker labels;
- source-unlabelled speech remains unlabelled;
- non-canonical ownership/library stamps are not screenplay text;
- no global normalization or silent reconstruction;
- translation never repairs Tamil or upgrades song authorship.

## Final source-review state — fully closed

There are now **no review/source-blocked pages or scenes**.

The final direct user scan verdicts are durable:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; canonical screenplay continues directly `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Durable record: `works/raja-rani/notes/final-source-review-resolution.md`.

Current source census:

- verified source pages: **79/79**;
- verified screenplay pages: **70/70**;
- archival scenes: **58/58 verified**, blocked **0**;
- immutable dialogue records: **1,076** across all 58 scenes;
- zero-dialogue scenes: **16**;
- genuine cross-page dialogue records: **12**;
- exact speaker labels: **80/80**;
- entities / roles / collectives: **44**, all verified;
- numbered songs: **11/11 Tamil derivatives**; screenplay singing refs **4**; total occurrences **15**;
- song authorship: **5 later-anthology Kalaignar attributions / 6 unresolved**.

The final unblock added source scene/dialogue shards for `s011`–`s013`, `s039`, and `s053`–`s055`. Five new exact labels entered the complete dialogue census: `மனம்`, `நிழல்`, `ஞானக்கண் குரல்`, `ராஜாவின் குரல்`, and `சமரசம் குரல்`. `மனம்` and `நிழல்` are preserved as source-personified dramatic roles; the three explicit voice labels map downstream to established characters.

## Correction 005 — closed

The late old-glyph/source correction campaign is reconciled through canonical Tamil, scenes, dialogue records, character labels/entities, affected song derivatives/metadata and the English records that existed during that gate. Durable record: `works/raja-rani/notes/correction-005-reconciliation.md`.

Do not revert permanent forms such as PDF 72 `சாக்ரடீசின்`, scene-17 exact label `தர்யம்`, scene-34 corrected `ராணி` ownership, final PDF 76–79 manual adjudications, or any of the final source-review verdicts above.

## English translation — current durable checkpoint

User production policy: **process 10 verified untranslated scenes per iteration in source order**.

Completed verified translation scenes:

**1–10, 14–32, 34**

Current totals after `BATCH_024_034_REVIEW.md`:

- translated scenes: **30 / 58**;
- verified English units: **715**;
- immutable dialogue links: **622 / 622 expected in translated scenes**;
- source-unlabelled spoken units: **11**;
- genuine cross-page translation units: **6**;
- translated screenplay performance occurrences: **2**;
- unit mix: **633 dialogue / 78 stage direction / 2 performance cue / 2 written text**;
- front-matter numbered song translations started: **0/11**.

The previous batch translated `s024`–`s032` plus `s034`. Scenes that were blocked at that historical checkpoint are now eligible; do not skip them.

## Exact next activity — 10 scenes

Translate, in source order:

1. `raja-rani-s011`
2. `raja-rani-s012`
3. `raja-rani-s013`
4. `raja-rani-s033`
5. `raja-rani-s035`
6. `raja-rani-s036`
7. `raja-rani-s037`
8. `raja-rani-s038`
9. `raja-rani-s039`
10. `raja-rani-s040`

There is **no source-review skip**.

For every scene:

- link each explicitly labelled source utterance to its immutable dialogue record exactly once;
- preserve exact `speaker_label` metadata;
- keep source-unlabelled speech null-speaker/null-record;
- keep stage directions/performance/written material as distinct source structures;
- retain genuine physical page crossings in one unit with provenance/page segments;
- do not invent speakers, lyrics, authorship or scene endings.

After the 10 scenes are translated, create one batch review, verify exact cumulative counts, and synchronize translation index/README, metadata, work README, this handover and the next-chat prompt before starting another iteration.

## Shared repository mirrors

`data/works.json` and root `README.md` may lag the work-local checkpoint. Do not let stale shared mirrors override the Raja Rani-local indexes/metadata/handover.
