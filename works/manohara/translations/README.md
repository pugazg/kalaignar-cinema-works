# மனோகரா — English translation layer

**Canonical authority:** verified Tamil transcription, complete scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **verified in progress — archival scenes 1–10 / 57, 204/204 units verified**

This directory contains an interpretive English derivative of the verified Tamil source. Nothing here repairs, normalizes, expands or overwrites the canonical Tamil.

The booklet prints **no scene numbers**. Translation identifiers such as `manohara-en-s001-u001` therefore use the archive's existing 57-scene navigation segmentation only; they must never be presented as source scene numbering.

## Files

- `schema.json` — scene-sharded source-linked translation schema adapted to Manohara's unnumbered-source structure.
- `index.json` — translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — verified review record for archival scenes 2–5.
- `BATCH_006_010_REVIEW.md` — verified review record for archival scenes 6–10.
- `records/scene-001.json` through `records/scene-010.json` — verified English scene records.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing a verified Tamil reading.
2. **Kalaignar's rhetoric must survive translation.** Repetition, verbal escalation, parallel clauses, insults, metaphor, theatrical pauses, questions and abrupt sentence rhythm are preserved where English can carry them.
3. **Every source-labelled utterance remains linked to its immutable dialogue record.** Exact Tamil `speaker_label` metadata is never normalized or replaced by character names.
4. **Stage directions do not gain action or identity.** Translate only what the verified scene supplies.
5. **Character voice is not homogenized.** Formal courtly speech, colloquial speech, reverential address, comic diction and heightened invective should remain distinguishable in English.
6. **Culturally specific images are not automatically domesticated.** Terms such as `Gurudeva`, `Swami`, `Bhadrakali`, `Athaan`, `Rakshasi`, `Chandali` and the `கொவ்வை` colour-image may be retained or lightly glossed when replacement would flatten the source.
7. **Cross-page source utterances remain one English unit.** Page provenance and English page segments preserve the physical source boundary.
8. **Song/performance material is limited to what this booklet prints.** No absent lyric is imported from recordings, web pages, record catalogs, subtitles or another booklet.
9. **Source-unlabelled speech remains unlabelled.** Translation must not manufacture a speaker or dialogue-record ID, even where surrounding stage context makes a likely speaker apparent.
10. **Decorative `★` separators remain structural.** They are not converted into invented prose such as `(Scene ends.)`.
11. **External authorship metadata is not translation text.** The song evidence layer may identify or qualify an occurrence, but cannot supply missing words.
12. **The play-within-the-play remains structurally distinct.** Translation must not collapse nested-play identities into outer-story identities.

## Verified pilot — `manohara-s001`

The rendered scan for PDF **7–8 / logical printed pp.6–7** was reinspected before the pilot was closed. The pilot contains **12 verified units: 10 dialogue + 2 stage direction**. `manohara-en-s001-u006` preserves the genuine PDF 7→8 source crossing as one English unit with page-segment provenance.

The pilot establishes the voice template: repeated `Victory`, the harvest metaphor, `Gurudeva` / `Swami`, Kesari Varman's accelerating invective, `Bhadrakali`, and `kovvai-red lips` remain visible rather than being flattened into neutral modern English.

## Verified batch — `manohara-s002`–`manohara-s005`

PDF **8–10 / logical printed pp.7–9** was reinspected for this batch. Four additional archival scenes add **26 verified units: 21 dialogue / 4 stage direction / 1 song-reference**.

The batch preserves Vasantha Sena's escalating ambition, the recurring `சந்தேகமில்லே` wordplay, Padmavathi's pleading register and the nested-play aliases. The translated song reference in scene 3 links only to `manohara-song-001`; no absent lyrics are supplied.

## Verified batch — `manohara-s006`–`manohara-s010`

PDF **10–23 / logical printed pp.9–22** was directly reinspected. Five additional archival scenes add **166 verified units: 141 dialogue-kind / 24 stage direction / 1 song-reference**. All **133/133 immutable labelled dialogue records** in these scenes are linked exactly once.

Scene 8 exercises the most complex source structure so far. It retains the play-within-the-play as a separate dramatic layer, keeps the unresolved exact label `வர்மா` unchanged, and translates six source-empty speaker passages without inventing speaker metadata. Two new genuine cross-page English units are preserved: `manohara-en-s008-u008` across PDF 13→14 and `manohara-en-s008-u077` across PDF 18→19.

The source-visible scene-8 love-song reference `நிலாவிலே ! சல்லாபமே!!` is linked to `manohara-song-002`. Only the printed title/refrain reference is translated; no lyric body is reconstructed.

Across scenes 6–10, the English preserves Vasanthan's comic Pillaiyar/Parvati comparison, Manoharan's tortoise/warrior contrast, Kamalavathi's `javvadhu` / `Chandali` / `Rati-devi` imagery, Devasena's `Athaan` / `Rakshasi` register, Vasantha Sena's renunciation performance, Kesari's `brazen lie` / `syrupy speech` contrast, and Manoharan's festering-wound / civet-perfume alliterative image sequence. Scene 10 also preserves the `roll up and seize / be rolled up and crushed` wordplay rather than reducing it to a generic threat.

`BATCH_006_010_REVIEW.md` records the batch-level decisions and integrity checks.

## Current coverage

- archival scenes expected: **57**;
- scenes translated/verified: **10/57**;
- verified English units: **204**;
- unit mix: **172 dialogue / 30 stage direction / 2 song-reference**;
- immutable dialogue links: **164/164** for completed scenes;
- direct source-unlabelled spoken units: **8**, all with null speaker metadata;
- translated song occurrences: **2 — `manohara-song-001`, `manohara-song-002`**;
- cross-page English units: **3**;
- review/draft units: **0**;
- structural stars translated as prose: **0**;
- canonical Tamil modified: **no**;
- immutable dialogue records modified: **no**.

## Next activity

Translate and verify **`manohara-s011`–`manohara-s015`** with the same source-linked model and voice-preservation rules. Reinspect the rendered scan whenever a proclamation/chant boundary, unlabelled speech, courtly register, comic phrase, page crossing or rhetorical image is uncertain.
