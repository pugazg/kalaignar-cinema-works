# மனோகரா — English translation layer

**Canonical authority:** verified Tamil transcription, complete scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **verified in progress — archival scenes 1–5 / 57, 38/38 units verified**

This directory contains an interpretive English derivative of the verified Tamil source. Nothing here repairs, normalizes, expands or overwrites the canonical Tamil.

The booklet prints **no scene numbers**. Translation identifiers such as `manohara-en-s001-u001` therefore use the archive's existing 57-scene navigation segmentation only; they must never be presented as source scene numbering.

## Files

- `schema.json` — scene-sharded source-linked translation schema adapted to Manohara's unnumbered-source structure.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — verified review record for archival scenes 2–5.
- `records/scene-001.json` through `records/scene-005.json` — verified English scene records.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing a verified Tamil reading.
2. **Kalaignar's rhetoric must survive translation.** Repetition, verbal escalation, parallel clauses, insults, metaphor, theatrical pauses, questions and abrupt sentence rhythm are preserved where English can carry them.
3. **Every source-labelled utterance remains linked to its immutable dialogue record.** Exact Tamil `speaker_label` metadata is never normalized or replaced by character names.
4. **Stage directions do not gain action or identity.** Translate only what the verified scene supplies.
5. **Character voice is not homogenized.** Formal courtly speech, colloquial speech, reverential address, comic diction and heightened invective should remain distinguishable in English.
6. **Culturally specific images are not automatically domesticated.** Terms such as `Gurudeva`, `Swami`, `Bhadrakali` and the `கொவ்வை` colour-image may be retained or lightly glossed when replacement would flatten the source.
7. **Cross-page source utterances remain one English unit.** Page provenance and English page segments preserve the physical source boundary.
8. **Song/performance material is limited to what this booklet prints.** No absent lyric is imported from recordings, web pages, record catalogs, subtitles or another booklet.
9. **Source-unlabelled speech remains unlabelled.** Translation must not manufacture a speaker or dialogue-record ID.
10. **Decorative `★` separators remain structural.** They are not converted into invented prose such as `(Scene ends.)`.
11. **External authorship metadata is not translation text.** The song evidence layer may identify or qualify an occurrence, but cannot supply missing words.
12. **The play-within-the-play remains structurally distinct.** Translation must not collapse nested-play identities into outer-story identities.

## Verified pilot — `manohara-s001`

The rendered scan for PDF **7–8 / logical printed pp.6–7** was reinspected before the pilot was closed. The pilot contains **12 verified units: 10 dialogue + 2 stage direction**. `manohara-en-s001-u006` preserves the genuine PDF 7→8 source crossing as one English unit with page-segment provenance.

The pilot establishes the voice template: repeated `Victory`, the harvest metaphor, `Gurudeva` / `Swami`, Kesari Varman's accelerating invective, `Bhadrakali`, and `kovvai-red lips` remain visible rather than being flattened into neutral modern English.

## Verified batch — `manohara-s002`–`manohara-s005`

PDF **8–10 / logical printed pp.7–9** was reinspected for this batch. Four additional archival scenes add **26 verified units: 21 dialogue / 4 stage direction / 1 song-reference**.

Key dispositions:

- scene 2 preserves Vasantha Sena's escalating boast, including `living corpses`, `chief queen`, the throne and realm-at-her-feet imagery;
- scene 3 preserves the repeated `சந்தேகமில்லே` wordplay and links the translated source-visible song reference to `manohara-song-001` without adding absent lyrics;
- scene 4 retains Padmavathi's repeated `Swami!`, rhetorical pleading and the parental `உச்சி மோந்து` image as `kiss the crown`;
- scene 5 keeps the nested-play aliases distinct, translates `போர்வாள்` as `The Sword of War`, retains `Shabash`, and follows the pilot's `Gurudeva` register.

All **21/21** immutable dialogue records in scenes 2–5 are linked exactly once. `BATCH_002_005_REVIEW.md` records the batch-level fidelity decisions.

## Current coverage

- archival scenes expected: **57**;
- scenes translated/verified: **5/57**;
- verified English units: **38**;
- unit mix: **31 dialogue / 6 stage direction / 1 song-reference**;
- immutable dialogue links: **31/31** for completed scenes;
- translated song occurrences: **1 — `manohara-song-001`**;
- cross-page English units: **1**;
- review/draft units: **0**;
- structural stars translated as prose: **0**;
- canonical Tamil modified: **no**;
- immutable dialogue records modified: **no**.

## Next activity

Translate and verify **`manohara-s006`–`manohara-s010`** with the same source-linked model and voice-preservation rules. Reinspect the rendered scan whenever a page boundary, courtly expression, nested-play identity, comic phrase or rhetorical image is uncertain.
