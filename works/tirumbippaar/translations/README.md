# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **in-progress — scenes 1–10 complete, 124/124 current units verified**

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
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material must not receive invented speakers or record IDs.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **No external text substitution.** Film subtitles, dubbed dialogue, later editions and familiar quotations do not replace this source-linked translation.

## Unit kinds

The schema supports `dialogue`, `stage-direction`, `song`, `song-reference`, `chant`, and `written-text` so later scenes can preserve source-visible structures without forcing everything into labelled dialogue. A kind identifies the archival form of the source unit; it does not add content that is absent from the booklet.

## Verified coverage

Scenes **1–10** are translated and verified in canonical order:

- scene 1 — **10 units**;
- scene 2 — **17 units**;
- scene 3 — **4 units**;
- scene 4 — **18 units**;
- scene 5 — **32 units**;
- scene 6 — **17 units**;
- scene 7 — **15 units**;
- scene 8 — **6 units**;
- scene 9 — **4 units**;
- scene 10 — **1 unit**;
- total — **124 verified / 0 review / 0 draft**.

Current kinds: **97 dialogue / 25 stage-direction / 2 song-reference**.

The only cross-page English unit so far remains `tirumbippaar-en-s001-u008`, linked to dialogue record `tirumbippaar-s001-d006` across PDF 9→10 / printed pp.1→2.

## Source-sensitive cases through scene 10

Scene 2 opens with Poomaal teaching children moral instruction through song. This is represented as `song-reference` linked to `tirumbippaar-song-001`; the booklet prints no song title or lyric body, so the English supplies none.

Scene 3 preserves the comic source word association `அன்பு...தொண்டு...அவரைக்காய்...` without fabricating a different English pun. Scene 4 retains the visibly broken banana/child comparison with an explanatory note rather than silently reconstructing a modern sentence.

Scene 5 contains the source-unlabelled spoken line `ஏ பையா! கூடா ஒரு கப் காபி கொண்டாந்து கொடு.` It remains direct source-linked dialogue with `speaker_label: null` and no invented dialogue-record ID. The anomalous exact speaker label `குரு` on `பக்தா!` likewise remains unchanged metadata.

Scene 6 opens immediately after Bama's song has ended. The performance reference is linked to `tirumbippaar-song-002`, but the source prints no title or lyric body, so no English lyrics are reconstructed. Paranthaman's `சுருக்கு` / marriage-cord wordplay and the storm/breeze/volcano imagery are preserved as rhetoric rather than flattened into a summary.

Scene 7 retains the period colour joke and the source phrase `கவர் கவிதை` as deliberately odd `cover-poetry`; it is not silently normalized into a different joke. Scene 8 preserves the hurried `முகூர்த்தநேரம்` exchange as the search for the missing bridegroom begins.

Scene 10 correctly has **no dialogue record**. Its entire source-visible content is the visual transformation of Bama's tears into a waterfall and then a river, so it is represented as one direct scene-linked `stage-direction` unit rather than receiving invented dialogue or interpretation.

No canonical Tamil, scene derivative, dialogue record, character record or song record was modified by this English batch.

## Song constraint carried into translation

The completed song gate found that this booklet does not print a complete lyric body for either source-named soundtrack song. English scene translation may translate only the source-visible title, fragment or performance reference. There will be no reconstructed English lyric where the Tamil source itself is absent.

## Next activity

Translate and verify **scenes 11–15**. Continue exact dialogue-record linking, direct scene linking for stage/unlabelled material, source-visible song references only to their printed extent, and page provenance for every unit.
