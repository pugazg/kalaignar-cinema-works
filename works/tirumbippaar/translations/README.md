# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **in-progress — scenes 1–20 complete, 253/253 current units verified**

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

The schema supports `dialogue`, `stage-direction`, `song`, `song-reference`, `chant`, and `written-text` so later scenes can preserve source-visible structures without forcing everything into labelled dialogue.

## Verified coverage

Scenes **1–20** are translated and verified in canonical order.

- scenes 1–5 — **81 units**;
- scenes 6–10 — **43 units**;
- scenes 11–15 — **63 units**;
- scenes 16–20 — **66 units**;
- total — **253 verified / 0 review / 0 draft**.

Current kinds: **203 dialogue / 46 stage-direction / 4 song-reference**.

The only cross-page English unit so far remains `tirumbippaar-en-s001-u008`, linked to dialogue record `tirumbippaar-s001-d006` across PDF 9→10 / printed pp.1→2.

## Source-sensitive cases through scene 20

Earlier source-sensitive cases remain documented in their scene records. Scenes 2, 6, 11 and 14 preserve source-visible song/performance references without importing absent lyrics. Scenes 5 and 15 preserve source-unlabelled speech with null speaker metadata. Scene 10 remains a zero-dialogue visual scene.

Scene 16 preserves the wedding invitation only through its printed cutoff at `தங்கள் சுற்றமும் ....`; the English does not complete the conventional invitation wording. Garudan's interrupted accusation likewise remains unfinished.

Scene 17 preserves Paranthaman's elaborate mythological and romantic rhetoric rather than flattening it. Tilottama and Menaka remain named references; `காயகல்பம்` is represented as `kayakalpa`. The source's unusual forms around `குழந்தைக்கார லோகம்`, `குணப்பக்காரன்`, and the printed age expression are not used to alter canonical Tamil.

Scene 18 keeps the colloquial `அவாள்னா இவாள்னா` generic rather than assigning identities absent from the source. The final report that the bride has run away remains an unlabelled stage action whispered to Punnakodi, not invented dialogue.

Scene 19 preserves the exact generic speaker label `பெண்`; the student is not given a name. `அம்மா` is translated as the address `amma` where relationship would otherwise be inferred.

Scene 20 keeps the book title `வாழு வாழவிடு` visibly connected to its Tamil form through transliteration. Pandiyan's repeated `நானு தவறு செய்யவில்லை` frames his long humiliation speech in English as it does in the source, while the unusual `கள்ளி பொறுத்தி` insult is translated conservatively and explicitly noted rather than silently modernized.

No canonical Tamil, scene derivative, dialogue record, character record or song record was modified by this English batch.

## Song constraint carried into translation

The completed song gate found that this booklet does not print a complete lyric body for either source-named soundtrack song. English scene translation may translate only the source-visible title, fragment or performance reference. There will be no reconstructed English lyric where the Tamil source itself is absent.

## Next activity

Translate and verify **scenes 21–25**. Continue exact dialogue-record linking, direct scene linking for stage/unlabelled material, source-visible performance material only to its printed extent, and page provenance for every unit.
