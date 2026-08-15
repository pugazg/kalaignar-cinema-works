# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **pilot-verified — scene 1 complete, 10/10 units verified**

This directory contains interpretive English derivatives. Nothing here may repair, normalize, expand or overwrite the verified Tamil source.

## Files

- `schema.json` — source-linked translation-unit schema.
- `index.json` — translation progress / verification checkpoint.
- `records/scene-XX.json` — scene-sharded English translation units.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every unit is source-linked.** Preserve canonical scene, source path, dialogue-record or song-occurrence ID where available, and PDF/printed-page provenance.
3. **Exact Tamil speaker labels stay exact metadata.** Character normalization does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the verified scene actually supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Where useful, `english_page_segments` mirrors the canonical source break.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled written structures remain unlabelled.** Letters, newspaper blocks, advertisements, chants and other source-visible material must not receive invented speakers.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **No external text substitution.** Film subtitles, dubbed dialogue, later editions and familiar quotations do not replace this source-linked translation.

## Unit kinds

The schema supports `dialogue`, `stage-direction`, `song`, `song-reference`, `chant`, and `written-text` so later scenes can preserve source-visible structures without forcing everything into dialogue. A kind identifies the archival form of the source unit; it does not add content that is absent from the booklet.

## Verified pilot — scene 1

`records/scene-01.json` translates the complete opening court scene into **10 source-linked units**:

- **8 dialogue** units linked directly to `dialogues/records/scene-01.json`;
- **2 stage-direction** units linked directly to `scenes/scene-01.md`;
- **10 verified / 0 review / 0 draft**;
- one cross-page unit: `tirumbippaar-en-s001-u008`, linked to dialogue record `tirumbippaar-s001-d006` across PDF 9→10 / printed pp.1→2.

The pilot deliberately preserves Poomaal's repeated denial (`கொலை செய்ய வில்லை—கொலை செய்யவில்லை`) as repeated English rather than smoothing it into one sentence. It also preserves the unfinished narrative pivot at the end of scene 1 instead of completing the flashback transition from inference.

No canonical Tamil, scene derivative, dialogue record, character record or song record was modified by the English pilot.

## Song constraint carried into translation

The completed song gate found that this booklet does not print a complete lyric body for either source-named soundtrack song. Future English scene translation may translate only the source-visible title, fragment or performance reference. There will be no reconstructed English lyric where the Tamil source itself is absent.

## Next activity

Scale out from the verified pilot to **scenes 2–5**. Translate every source-visible unit in canonical order, link labelled dialogue to immutable dialogue-record IDs, retain unlabelled stage/performance material without invented speakers, and perform a verification pass before marking the batch complete.
