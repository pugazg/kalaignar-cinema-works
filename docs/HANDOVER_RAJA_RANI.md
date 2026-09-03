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

Comparison extracts such as `r1.md`–`r4.md` and split PDFs are review aids only. The rendered source scan controls canonical Tamil.

## Mandatory startup in a fresh chat

Read completely before changing anything:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. this `docs/HANDOVER_RAJA_RANI.md`
7. `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/notes/post-fidelity-corrections.md`
10. `works/raja-rani/notes/correction-005-reconciliation.md`
11. `works/raja-rani/translations/README.md`
12. `works/raja-rani/translations/index.json`
13. the current batch's Tamil scene files and immutable dialogue shards.

## Permanent source rules

- rendered scan evidence controls disputed characters;
- OCR, parsed PDF text and comparison transcriptions are candidate readings only;
- do not prefer modern/familiar spelling because it seems linguistically more natural;
- preserve user-reviewed occurrence-specific source verdicts;
- preserve exact source speaker-label variants;
- source-unlabelled speech remains unlabelled;
- no global normalization;
- no silent reconstruction of obscured source text;
- translation never repairs Tamil uncertainty or upgrades song authorship.

The bounded source limitations remain PDF **27, 48, 57 and 74**. Their blocked archival scenes remain outside translation production:

- `s011`–`s013` — PDF 27;
- `s033` — PDF 48;
- `s039` — PDF 57;
- `s053`–`s055` — PDF 74.

## Correction 005 — closed

The late user-led old-glyph/source-correction campaign has been reconciled through canonical Tamil, affected scene derivatives, immutable dialogue records, exact-label character metadata, affected song derivatives/metadata and all English records that existed at the time.

Durable record:

`works/raja-rani/notes/correction-005-reconciliation.md`

Important forms that must not be reverted include PDF 52 `ராணி:` for the corrected dialogue occurrence, PDF 72 `சாக்ரடீசின்`, scene-17 exact label `தர்யம்`, and the final user-adjudicated PDF 76–79 forms.

Current source/derivative census:

- verified source pages: **75/79**; review pages: **4/79**;
- archival scene segments: **58**;
- eligible verified scene derivatives: **50**; blocked: **8**;
- immutable dialogue records: **892**;
- dialogue cross-page records: **11**;
- exact source speaker labels: **75/75**;
- character entities / roles / collectives: **42**;
- numbered songs / verified Tamil song derivatives: **11/11**;
- screenplay singing references: **4**;
- total song/performance occurrences: **15**;
- numbered songs anthology-attributed to Kalaignar: **5** — 3, 5, 6, 7, 8;
- numbered songs with unresolved lyricist: **6** — 1, 2, 4, 9, 10, 11.

## English translation — current durable checkpoint

Translation is source-linked and scene-sharded under `works/raja-rani/translations/`.

Completed verified scenes:

**1–10, 14–23**

Current totals after `BATCH_019_023_REVIEW.md`:

- translated eligible scenes: **20 / 50**;
- verified English units: **483**;
- immutable dialogue links: **424 / 424 expected**;
- source-unlabelled spoken units: **8**;
- genuine cross-page translation units: **6**;
- translated screenplay performance occurrences: **2**;
- unit mix: **432 dialogue / 47 stage direction / 2 performance cue / 2 written text**;
- front-matter numbered song translations started: **0/11**.

Batch 019–023 added:

- **96** verified units;
- **86/86** immutable dialogue links;
- **10** stage directions;
- **2** new cross-page units;
- **0** invented speakers/song units.

Batch-specific decisions:

- scenes 19, 20 and 22 are stage-only source segments; no dialogue was manufactured;
- scene 21 retains the repeated source `நீ` as `nee`, exact speaker-label variants, and the peace/quarrel signboard wordplay; its pigeon stage action crosses PDF 35→36 and `raja-rani-s021-d048` crosses PDF 37→38;
- scene 23 preserves source-visible `டேட்`, `ட்ராமா, கீமா`, and the `பாடம்` / `பணம்` contrast.

Authoritative translation checkpoint files:

- `works/raja-rani/translations/index.json`
- `works/raja-rani/translations/README.md`
- `works/raja-rani/translations/BATCH_019_023_REVIEW.md`
- `works/raja-rani/translations/records/scene-019.json` through `scene-023.json`

## Exact next activity

Translate verified archival scenes:

**`raja-rani-s024` through `raja-rani-s028`**

Before creating English records, read the five live Tamil scene derivatives and their dialogue shards completely. Work in source order.

Preserve:

- every immutable dialogue record exactly once with stable source record ID;
- exact source `speaker_label` metadata;
- source-unlabelled speech as null-speaker units;
- stage directions, written material and performance structures as distinct unit kinds;
- genuine cross-page source units as one English unit with physical provenance and page segments;
- rhetoric, colloquial timing, code-switching and source irregularities.

Scene **27** legitimately has **zero immutable dialogue records**; do not manufacture dialogue from its non-dialogue source material.

Do not invent speakers, lyrics, authorship, scene endings or text from review-source pages.

After scenes 24–28 are translated:

1. verify sequential unit IDs and exact dialogue-link coverage;
2. record all new source-unlabelled and cross-page units;
3. create `BATCH_024_028_REVIEW.md`;
4. update `translations/index.json` and `translations/README.md` with exact cumulative counts;
5. synchronize `works/raja-rani/metadata.yaml`, work README, this handover and `NEXT_CHAT_PROMPT_RAJA_RANI.md` before advancing.

## Shared repository mirrors

`data/works.json` and root `README.md` are shared repository mirrors and may lag the work-local checkpoint. Do not let a stale shared mirror override the live Raja Rani indexes/metadata/handover. Update those shared files only when they can be safely rewritten without risking unrelated works.

Canonical scan fidelity remains more important than derivative consistency. If future direct scan evidence changes canonical Tamil, correct the source first and explicitly reconcile only affected downstream material before continuing.
