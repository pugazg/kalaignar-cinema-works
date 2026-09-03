# Next Chat Prompt — Raja Rani English Translation — Next 10 Eligible Scenes

Continue directly in:

`pugazg/kalaignar-cinema-works`

Branch: `main`

Active work: `works/raja-rani/` — **ராஜா ராணி**

Controlling full source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve any newer durable state. Do not reset, repeat or overwrite later work because this prompt contains an older checkpoint.

Source identity:

- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- screenplay/dialogue: PDF **10–79**, printed pp. **9–78**
- PDF 80: unnumbered back cover

## Mandatory startup

Before any write, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. `docs/HANDOVER_RAJA_RANI.md`
7. this `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/notes/post-fidelity-corrections.md`
10. `works/raja-rani/notes/correction-005-reconciliation.md`
11. `works/raja-rani/translations/README.md`
12. `works/raja-rani/translations/index.json`
13. the live Tamil scene files and immutable dialogue shards for the next 10 eligible scenes.

## Source/reconciliation state

Correction 005 is reconciled. Do **not** reopen the completed manual correction campaign merely because an older document says it was pending.

Current synchronized source/derivative census:

- dialogue: **892 records / 50 eligible scenes / 8 blocked**;
- character mapping: **75/75 exact labels / 42 entities**;
- songs/performance: **11 numbered songs + 4 screenplay references = 15 occurrences**; authorship remains 5 later-anthology Kalaignar-attributed / 6 unresolved;
- English translation: **30/50 eligible scenes / 715 verified units / 622/622 immutable dialogue links**.

Permanent source forms include PDF 72 `சாக்ரடீசின்`, scene-17 exact label `தர்யம்`, corrected scene-34 `ராணி` ownership, and the final manually adjudicated PDF 76–79 forms. Do not normalize or revert them.

Review/source-limited pages remain PDF **27, 48, 57 and 74**. Blocked scenes remain:

- `s011`–`s013`;
- `s033`;
- `s039`;
- `s053`–`s055`.

## USER-REQUESTED BATCH POLICY

Process **10 eligible verified scenes in each translation iteration**.

A blocked scene does **not** count toward the 10. Skip it and continue forward until 10 eligible scenes have been translated.

## EXACT NEXT ACTIVITY — 10 eligible scenes

Translate, in source order:

1. `raja-rani-s035`
2. `raja-rani-s036`
3. `raja-rani-s037`
4. `raja-rani-s038`
5. **skip blocked `raja-rani-s039`**
6. `raja-rani-s040`
7. `raja-rani-s041`
8. `raja-rani-s042`
9. `raja-rani-s043`
10. `raja-rani-s044`
11. `raja-rani-s045`

This produces exactly **10 eligible translated scenes**.

For every scene:

- use the verified Tamil scene derivative as translation authority;
- link every explicitly source-labelled utterance to its immutable dialogue record exactly once;
- preserve exact source `speaker_label` metadata;
- keep source-unlabelled speech null-speaker/null-record instead of inferring ownership;
- represent source-visible stage directions separately;
- retain genuine cross-page units as one translation unit with page provenance / page segments;
- keep written text, chants and performance cues structurally distinct when present;
- link song/performance occurrences only where the verified song layer supports the relation and only to the extent printed;
- do not invent missing lyrics, speakers, scene endings or authorship;
- do not modify canonical Tamil, scenes, immutable dialogue IDs, character entities or song authorship to make English smoother.

## Current translation checkpoint before this iteration

Completed verified scenes:

**1–10, 14–32, 34**

Totals:

- scenes: **30/50**;
- translation units: **715 verified**;
- dialogue units: **633**;
- stage-direction units: **78**;
- performance-cue units: **2**;
- written-text units: **2**;
- immutable dialogue links: **622/622**;
- source-unlabelled spoken units: **11**;
- cross-page translation units: **6**.

Latest review: `works/raja-rani/translations/BATCH_024_034_REVIEW.md`.

After completing all 10 eligible scenes in this iteration:

1. verify sequential unit IDs and exact dialogue-link coverage scene by scene;
2. record all new source-unlabelled, cross-page, written/performance units;
3. create one batch review for the 10 eligible scenes;
4. synchronize `translations/index.json` and `translations/README.md` with exact cumulative counts;
5. synchronize `works/raja-rani/metadata.yaml`, work README, handover and this prompt;
6. set the following activity to the next 10 eligible verified scenes.

## Old-glyph/source rule remains active

If a source reading becomes disputed while translating, English fluency is not evidence for changing Tamil. Rendered scan evidence and already-recorded user manual verdicts control. Preserve occurrence-specific forms and never silently modernize them.
