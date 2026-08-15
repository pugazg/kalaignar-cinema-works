# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **in-progress — scenes 1–45 complete, 680/680 current units verified**

This directory contains interpretive English derivatives. Nothing here may repair, normalize, expand or overwrite the verified Tamil source.

## Files

- `schema.json` — source-linked translation-unit schema.
- `index.json` — translation progress / verification checkpoint.
- `records/scene-XX.json` — scene-sharded English translation units.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every unit is source-linked.** Preserve canonical scene, dialogue-record or song-occurrence ID where available, and PDF/printed-page provenance.
3. **Exact Tamil speaker labels stay exact metadata.** Character normalization does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the verified scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material must not receive invented speakers or dialogue-record IDs.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **No external text substitution.** Film subtitles, dubbed dialogue, later editions and familiar quotations do not replace this source-linked translation.

## Unit kinds

The schema supports `dialogue`, `stage-direction`, `song`, `song-reference`, `chant`, and `written-text` so source-visible structures do not have to be forced into labelled dialogue.

## Verified coverage

Scenes **1–45** are translated and verified in canonical order.

- scenes 1–5 — **81 units**
- scenes 6–10 — **43 units**
- scenes 11–15 — **63 units**
- scenes 16–20 — **66 units**
- scenes 21–25 — **28 units**
- scenes 26–30 — **100 units**
- scenes 31–35 — **85 units**
- scenes 36–40 — **122 units**
- scenes 41–45 — **92 units**
- total — **680 verified / 0 review / 0 draft**

Current kinds: **529 dialogue / 138 stage-direction / 7 song-reference / 1 chant / 5 written-text**.

Current cross-page English units are:

- `tirumbippaar-en-s001-u008` — PDF 9→10
- `tirumbippaar-en-s026-u002` — PDF 31→32
- `tirumbippaar-en-s041-u001` — PDF 52→53
- `tirumbippaar-en-s041-u046` — PDF 56→57
- `tirumbippaar-en-s045-u018` — PDF 59→60

## Source-sensitive cases through scene 45

Earlier source-sensitive choices remain documented inside their scene records. The translation layer continues to preserve source-only performance references, unlabelled speech and irregular wording rather than filling gaps from film knowledge.

Scene 41 preserves the source-visible Sivasakthi Mills cash bundle, the four-name amount slip and the newspaper strike headline as separate source-linked structures. Poomaal's labelled accusation `tirumbippaar-s041-d034` remains one cross-page English unit across PDF 56→57; the irregular printed phrase `காமல ஜீவவியத்தைக்` is transliterated conservatively rather than silently reconstructed.

Scenes 42–43 are linked to verified song occurrences `tirumbippaar-song-007` and `tirumbippaar-song-008`. Scene 42 translates only the printed fragment `கலப்படம் கலப்படம்`; scene 43 records only that the office boy sings the same song. No unprinted lyric body is supplied.

Scene 43 remains a **zero-dialogue source scene**. Paranthaman's angry muttering of `பாண்டியன்` occurs inside the narrative description and is not promoted to an invented dialogue record.

Scene 44 contains an important unlabelled continuation after the direction describing Garudan's anger. The continuation is retained as `tirumbippaar-en-s044-u004` with null speaker metadata and no dialogue-record ID, even though the surrounding scene context indicates continuation of the platform speech.

Scene 45 preserves Usha's medicine metaphor (`இருதயம்`, `இரக்கம்`, `சமதர்மம்`, `சமத்துவம்`) and Pandiyan's `மஞ்சம் / பஞ்சம் / லஞ்சம்` sound-play. The latter crosses PDF 59→60 as a single source-labelled unit; the semantic contrast is translated while the non-portable Tamil rhyme is documented in a note.

No canonical Tamil, scene derivative, dialogue record, character record or song inventory was modified by this batch.

## Song constraint carried into translation

The completed song gate found that this booklet does not print a complete lyric body for either source-named soundtrack song. English translation may translate only the source-visible title, fragment or performance reference. There will be no reconstructed English lyric where the Tamil source itself is absent.

## Next activity

Translate and verify **scenes 46–50**. Continue immutable dialogue-record linking, source-unlabelled material without invented speakers, genuine cross-page provenance, and source-visible song/performance material only to the printed extent.
