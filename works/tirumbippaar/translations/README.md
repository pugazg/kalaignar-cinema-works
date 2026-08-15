# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **in-progress — scenes 1–15 complete, 187/187 current units verified**

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

Scenes **1–15** are translated and verified in canonical order.

- scenes 1–5 — **81 units**;
- scenes 6–10 — **43 units**;
- scenes 11–15 — **63 units**;
- total — **187 verified / 0 review / 0 draft**.

Current kinds: **147 dialogue / 36 stage-direction / 4 song-reference**.

The only cross-page English unit so far remains `tirumbippaar-en-s001-u008`, linked to dialogue record `tirumbippaar-s001-d006` across PDF 9→10 / printed pp.1→2.

## Source-sensitive cases through scene 15

Scene 2 and scene 6 preserve only the source-visible facts that song performance/teaching occurs; neither occurrence gains an invented title or lyric body.

Scene 5 contains the source-unlabelled spoken line `ஏ பையா! கூடா ஒரு கப் காபி கொண்டாந்து கொடு.` It remains direct source-linked dialogue with `speaker_label: null` and no invented dialogue-record ID. The anomalous exact label `குரு` on `பக்தா!` remains unchanged metadata.

Scene 10 has no labelled dialogue. Its entire source-visible content is translated as one stage-direction unit: Bama's tears fall into her hand, become a waterfall and then a river.

Scene 11 is another zero-dialogue source scene. Its boat movement is a stage-direction, while the fact that Paranthaman and an unnamed woman sing as they travel is a `song-reference` linked to `tirumbippaar-song-003`. The woman is not identified and absent lyrics remain absent.

Scene 12 preserves the source's irregular rhetoric rather than silently repairing it. The unusual `குதுவாதறியாத` phrase is translated conservatively and explicitly noted; `முகாரி` remains `Mukhari` to retain the source's music/lament reference. The closing child's `நாய் வால் நிமிர்க்க முடியாதாம்` line is translated literally without editorial explanation.

Scene 13 ends with `புத்தகத்தைப் பிரித்துப் பாடல்`. Because that line gives no title, lyrics or explicit performer and is not a separately inventoried song occurrence, the English keeps it as the direct stage/performance direction `(The book is opened; a song follows.)` rather than inventing song metadata.

Scene 14 links the source-only stage-song reference to `tirumbippaar-song-004`; no absent lyrics are supplied. Pandiyan's speech keeps the contrast among `வாழு`, `வாழாதே`, and `வாழு வாழ விடு`, and renders `பகுத்தறிவு` as `rationalism` rather than weakening the ideological vocabulary.

Scene 15 contains a second source-unlabelled spoken line: `என்னடா இது ஒவ்வொரு சலவைக்கு ஒவ்வொரு பாக்கெட்டா திங்கிறான்......`. It remains direct scene-linked dialogue with `speaker_label: null` and no invented dialogue-record ID. Its odd pocket/laundry image is translated literally.

No canonical Tamil, scene derivative, dialogue record, character record or song record was modified by this English batch.

## Song constraint carried into translation

The completed song gate found that this booklet does not print a complete lyric body for either source-named soundtrack song. English scene translation may translate only the source-visible title, fragment or performance reference. There will be no reconstructed English lyric where the Tamil source itself is absent.

## Next activity

Translate and verify **scenes 16–20**. Continue exact dialogue-record linking, direct scene linking for stage/unlabelled material, source-visible performance material only to its printed extent, and page provenance for every unit.
