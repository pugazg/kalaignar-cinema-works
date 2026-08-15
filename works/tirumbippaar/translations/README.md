# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **in-progress — scenes 1–40 complete, 588/588 current units verified**

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
6. **Cross-page source units remain one English unit.** Where useful, page provenance mirrors the canonical source break.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material must not receive invented speakers or record IDs.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **No external text substitution.** Film subtitles, dubbed dialogue, later editions and familiar quotations do not replace this source-linked translation.

## Unit kinds

The schema supports `dialogue`, `stage-direction`, `song`, `song-reference`, `chant`, and `written-text` so source-visible structures can be preserved without forcing everything into labelled dialogue.

## Verified coverage

Scenes **1–40** are translated and verified in canonical order.

- scenes 1–5 — **81 units**;
- scenes 6–10 — **43 units**;
- scenes 11–15 — **63 units**;
- scenes 16–20 — **66 units**;
- scenes 21–25 — **28 units**;
- scenes 26–30 — **100 units**;
- scenes 31–35 — **85 units**;
- scenes 36–40 — **122 units**;
- total — **588 verified / 0 review / 0 draft**.

Current kinds: **463 dialogue / 116 stage-direction / 5 song-reference / 1 chant / 3 written-text**.

Verified cross-page English units so far are `tirumbippaar-en-s001-u008` and `tirumbippaar-en-s026-u002`.

## Source-sensitive cases through scene 40

Earlier source-sensitive cases remain documented in their scene records. Scenes 2, 6, 11, 14 and 31 preserve only the song/performance material actually printed by the booklet; absent lyrics are never reconstructed. Scenes 5 and 15 preserve source-unlabelled speech with null speaker metadata. Scenes 10, 11, 25 and 26 are zero-dialogue source scenes represented through their actual non-dialogue structures.

Scene 29 preserves the standalone labour `கோஷம்` as an unattributed chant rather than assigning it to a named character. Scene 30 preserves the source's `பொன்னகை / புன்னகை` wordplay through a translation note rather than silently replacing the Tamil rhetoric.

Scene 31 translates only the printed reference to `பாண்டியன் என் சொல்லை`; no lyric body is supplied. Scenes 32–33 retain the satire of Paranthaman's pro-worker rhetoric against his treatment and manipulation of workers. Scene 33's `ஆ...மோதிக்கிறேன் / மோதிக்கிட்டேங்க` joke is noted because its sound-play does not transfer literally to English.

Scene 35 keeps Pandiyan's incomplete poetic utterance incomplete rather than reconstructing the missing syntax.

Scene 36 preserves Poomaal's creeper/plant metaphor for the competing loves without replacing it with an explicit editorial explanation. Scene 37 retains the age, horoscope and `போதை` exchanges, including Punnakodi's final literal drinking retort to Pandiyan's figurative `போதை`. Scene 38 preserves the recurring contest-arena/earthquake imagery and Poomaal's explicit sacrifice of her love for Kumudha.

Scenes 39–40 preserve the political satire in source order: Paranthaman privately accepts money to stop the strike, arranges to buy over Punnakodi, then publicly declares victory and asks the workers to return to work. The English layer does not add motives or commentary beyond what the source makes visible.

No canonical Tamil, scene derivative, dialogue record, character record or song record was modified by this English batch.

## Song constraint carried into translation

The completed song gate found that this booklet does not print a complete lyric body for either source-named soundtrack song. English scene translation may translate only the source-visible title, fragment or performance reference. There will be no reconstructed English lyric where the Tamil source itself is absent.

## Next activity

Translate and verify **scenes 41–45**. Continue exact dialogue-record linking, direct scene linking for stage/unlabelled material, source-visible performance material only to its printed extent, and page provenance for every unit.
