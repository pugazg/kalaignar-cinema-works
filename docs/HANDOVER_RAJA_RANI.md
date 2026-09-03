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

Comparison extracts and OCR are review/navigation aids only. The rendered source scan controls canonical Tamil.

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
9. `works/raja-rani/notes/post-fidelity-corrections.md`
10. `works/raja-rani/notes/correction-005-reconciliation.md`
11. `works/raja-rani/translations/README.md`
12. `works/raja-rani/translations/index.json`
13. the current batch's live Tamil scene files and immutable dialogue shards.

## Permanent source rules

- rendered scan evidence controls disputed characters;
- OCR/parsed PDF/comparison text are candidate readings only;
- preserve user-reviewed occurrence-specific source verdicts and exact source speaker labels;
- source-unlabelled speech remains unlabelled;
- no global normalization or silent reconstruction;
- translation never repairs Tamil uncertainty or upgrades song authorship.

## Current bounded source limitations

Only **three** review pages remain:

- PDF 27 / printed p.26;
- PDF 57 / printed p.56;
- PDF 74 / printed p.73.

Blocked scenes are therefore now only `s011`–`s013`, `s039`, `s053`–`s055`.

### PDF 48 / scene 33 — resolved

The user directly rechecked PDF 48 and authoritatively resolved the two previously insecure spans immediately before `சமரசம் வீடு` as:

- `வந்தனா`
- `திடீர்னு`

PDF 48 is now **verified**. `raja-rani-s033` is now a complete verified scene derivative with **57 immutable dialogue records**, including one genuine PDF 48→49 cross-page record. It introduces no new exact speaker-label string or character entity.

Current non-translation census:

- verified source pages: **76/79**, review: **3/79**;
- verified screenplay pages: **67/70**, review: **3/70**;
- archival scenes: **58**; eligible verified: **51**; blocked: **7**;
- immutable dialogue records: **949**; cross-page: **12**;
- exact speaker labels: **75/75**; entities/roles/collectives: **42**;
- numbered songs: **11/11 Tamil derivatives**; screenplay singing refs: **4**; total song/performance occurrences: **15**;
- song authorship: **5 later-anthology Kalaignar attributions / 6 unresolved**.

## Correction 005 — closed

The late source-correction campaign has been reconciled through canonical Tamil, scenes, dialogue records, character labels/entities, affected song derivatives/metadata and all English records that predated reconciliation. Durable record: `works/raja-rani/notes/correction-005-reconciliation.md`.

Do not revert permanent source forms such as PDF 52's corrected `ராணி:` occurrence, PDF 72 `சாக்ரடீசின்`, scene-17 exact label `தர்யம்`, the final manually adjudicated PDF 76–79 forms, or the newly resolved PDF-48 forms `வந்தனா` / `திடீர்னு`.

## English translation — current durable checkpoint

Production policy requested by the user: **process 10 eligible verified scenes per iteration**. When a blocked scene is encountered, skip it and keep counting eligible scenes until the iteration contains 10 translated scenes.

Completed verified translation scenes:

**1–10, 14–32, 34**

Current totals after `BATCH_024_034_REVIEW.md`:

- translated eligible scenes: **30 / 51**;
- verified English units: **715**;
- immutable dialogue links: **622 / 622 expected in translated scenes**;
- source-unlabelled spoken units: **11**;
- genuine cross-page translation units: **6**;
- translated screenplay performance occurrences: **2**;
- unit mix: **633 dialogue / 78 stage direction / 2 performance cue / 2 written text**;
- front-matter numbered song translations started: **0/11**.

The previous 10-scene iteration translated `s024`–`s032` plus `s034`. Scene 33 was correctly skipped at that time because PDF 48 was still review; it is now the first scene in the next batch.

## Exact next activity — next 10 eligible scenes

Translate in source order:

1. `raja-rani-s033`
2. `raja-rani-s035`
3. `raja-rani-s036`
4. `raja-rani-s037`
5. `raja-rani-s038`
6. **skip blocked `raja-rani-s039`**
7. `raja-rani-s040`
8. `raja-rani-s041`
9. `raja-rani-s042`
10. `raja-rani-s043`
11. `raja-rani-s044`

This is **10 eligible translated scenes** because s039 is excluded.

For every scene:

- link each explicitly labelled source utterance to its immutable dialogue record exactly once;
- preserve exact `speaker_label` metadata;
- keep source-unlabelled speech null-speaker/null-record;
- keep stage directions/performance/written material as distinct source structures;
- retain genuine physical page crossings in one unit with provenance/page segments;
- do not invent speakers, lyrics, authorship or scene endings.

After all 10 eligible scenes are translated, create one batch review, update exact cumulative counts, and synchronize translation index/README, metadata, work README, this handover and the next-chat prompt before starting another iteration.

## Shared repository mirrors

`data/works.json` and root `README.md` may lag the work-local checkpoint. Do not let stale shared mirrors override the Raja Rani-local indexes/metadata/handover.
