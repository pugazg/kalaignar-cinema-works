# மனோகரா — English translation layer

**Canonical authority:** verified Tamil transcription, complete scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **pilot-verified — archival scene 1 / 57, 12/12 pilot units verified**

This directory contains an interpretive English derivative of the verified Tamil source. Nothing here repairs, normalizes, expands or overwrites the canonical Tamil.

The booklet prints **no scene numbers**. Translation identifiers such as `manohara-en-s001-u001` therefore use the archive's existing 57-scene navigation segmentation only; they must never be presented as source scene numbering.

## Files

- `schema.json` — scene-sharded source-linked translation schema adapted to Manohara's unnumbered-source structure.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `records/scene-001.json` — verified English pilot for `manohara-s001`.

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

The rendered scan for PDF **7–8 / logical printed pp.6–7** was reinspected before the pilot was closed. The pilot contains **12 verified units**:

- **10 dialogue units**, linked exactly once to `manohara-s001-d001` through `manohara-s001-d010`;
- **2 stage-direction units**;
- **1 genuine cross-page dialogue unit**, `manohara-en-s001-u006`, corresponding to `manohara-s001-d004` across PDF 7→8;
- **0 invented units** for the opening decorative star or the next scene's transition line.

The pilot deliberately keeps the source's heightened theatrical register. Examples of the adopted policy include retaining the repeated `Victory`, the harvest metaphor, `Gurudeva` / `Swami`, Kesari Varman's accelerating catalogue of invective, `Bhadrakali`, and the `kovvai-red lips` image rather than smoothing them into neutral modern English.

All **10/10** immutable dialogue records in the pilot scene are linked exactly once. No Tamil dialogue, scene, character or song record was modified by the English work.

## Scaling rule

The verified pilot is the style and provenance template for subsequent batches. Before a scene is marked `verified`, its English must be checked against both the verified scene derivative and the underlying dialogue/source provenance. The rendered scan should be reinspected whenever typography, a page break, an address term, an unusual image, or rhetorical force is uncertain.

For normal progress, translate in meaningful scene batches rather than one line or one record at a time. The next batch is **`manohara-s002` through `manohara-s005`**.

## Current coverage

- archival scenes expected: **57**;
- scenes translated/verified: **1/57**;
- verified English units: **12**;
- verified dialogue links: **10/10** for completed scenes;
- cross-page English units: **1**;
- review/draft units: **0**;
- canonical Tamil modified: **no**;
- immutable dialogue records modified: **no**.

## Next activity

Translate and verify **`manohara-s002`–`manohara-s005`** with the same source-linked model and voice-preservation rules. Preserve Kalaignar's language in English rather than reducing it to generic fluent dialogue.
