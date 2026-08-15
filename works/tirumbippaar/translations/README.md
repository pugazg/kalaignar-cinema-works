# திரும்பிப்பார்! — English translation layer

**Canonical authority:** verified Tamil transcription, completed scene derivatives and immutable dialogue records  
**Target language:** English (`en`)  
**Status:** **complete-verified — scenes 1–93, 1,330/1,330 units verified**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the verified Tamil source.

## Files

- `schema.json` — schema for the 93 scene-sharded source-linked translation records; it supports both the richer early units and the later compact units.
- `index.json` — completed translation / integrity checkpoint.
- `records/scene-XX.json` — 93 scene-sharded English translation records.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every source-labelled utterance is linked.** All 1,040 immutable dialogue records are represented exactly once in the completed English layer.
3. **Exact Tamil speaker labels stay exact metadata.** Character normalization does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the verified scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material do not receive invented speakers or dialogue-record IDs.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **The printed `★` is structural.** It is not translated into an invented `(Scene ends.)` unit.

## Final verified coverage

All canonical scenes **1–93** are translated and verified.

- scenes 1–5 — **81 units**
- scenes 6–10 — **43 units**
- scenes 11–15 — **63 units**
- scenes 16–20 — **66 units**
- scenes 21–25 — **28 units**
- scenes 26–30 — **100 units**
- scenes 31–35 — **85 units**
- scenes 36–40 — **122 units**
- scenes 41–45 — **92 units**
- scenes 46–50 — **84 units**
- scenes 51–55 — **46 units**
- scenes 56–60 — **111 units**
- scenes 61–65 — **50 units**
- scenes 66–70 — **67 units**
- scenes 71–75 — **44 units**
- scenes 76–80 — **81 units**
- scenes 81–85 — **49 units**
- scenes 86–90 — **82 units**
- scenes 91–93 — **36 units**
- **total — 1,330 verified / 0 review / 0 draft**

Final kinds: **1,047 dialogue / 263 stage-direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song units**.

The 1,047 dialogue-kind units consist of the **1,040 immutable source dialogue records plus 7 source-visible unlabelled spoken units**. The latter intentionally have null speaker/dialogue-record metadata.

## Cross-page English units

Twelve source units genuinely span canonical page boundaries and remain single English units:

- `tirumbippaar-en-s001-u008` — PDF 9→10
- `tirumbippaar-en-s026-u002` — PDF 31→32
- `tirumbippaar-en-s041-u001` — PDF 52→53
- `tirumbippaar-en-s041-u046` — PDF 56→57
- `tirumbippaar-en-s045-u018` — PDF 59→60
- `tirumbippaar-en-s061-u001` — PDF 78→79
- `tirumbippaar-en-s063-u004` — PDF 79→80
- `tirumbippaar-en-s072-u002` — PDF 87→88
- `tirumbippaar-en-s076-u014` — PDF 91→92
- `tirumbippaar-en-s080-u024` — PDF 96→97
- `tirumbippaar-en-s080-u032` — PDF 97→98
- `tirumbippaar-en-s083-u002` — PDF 100→101

## Source-unlabelled spoken units

These seven source-visible spoken passages remain `dialogue` units without invented speaker metadata or dialogue-record IDs:

- `tirumbippaar-en-s005-u026`
- `tirumbippaar-en-s015-u018`
- `tirumbippaar-en-s044-u004`
- `tirumbippaar-en-s051-u003`
- `tirumbippaar-en-s084-u002`
- `tirumbippaar-en-s088-u004`
- `tirumbippaar-en-s091-u014`

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — are nevertheless represented from their source-visible narrative/performance/written material.

## Song/performance constraint

Seven translated song references are linked to verified source occurrences `tirumbippaar-song-001`, `002`, `003`, `004`, `006`, `007` and `008`. Scene 31 is explicitly linked to `tirumbippaar-song-006`, whose scan-visible title is **`பாண்டியன் என் சொல்லை`**. Scenes 42–43 link the source-visible `கலப்படம்` material to occurrences `007` and `008`.

The booklet prints no complete lyric body for either source-named soundtrack song, so this layer contains **zero reconstructed full-song translations**. The scene-29 labour slogan and scene-86 begging chant remain chants, not fabricated soundtrack lyrics.

## Final reconciliation findings

The completion audit reconciled scene records against the immutable dialogue layer and source-visible structures.

- **93/93** scene translation files are present and verified.
- **1,040/1,040** labelled source dialogue records are linked.
- `schema.json` now describes the actual scene-sharded record architecture instead of the earlier unit-only shape, while accepting the richer provenance fields retained by the pilot/early records and the compact source fields used later.
- Scene 31's former placeholder song link was replaced by exact occurrence `tirumbippaar-song-006`.
- Scene 57 was repaired so all **50** labelled dialogue records are individually represented; its previously collapsed final confrontation is now fully source-linked.
- Star-only separators were removed from the derivative wherever they had been represented as synthetic `(Scene ends.)` units.
- Scene 90 retains the explicit source direction `[மரணமூச்சுவிடும் பரந்தாமன்]` as the transition into Paranthaman's dying exchange.
- Scene 91 preserves `பத்திரிகை News` / `(அக்காள் தம்பியைக் கொன்றாள்)` as written newspaper content rather than dialogue.
- Scene 93 preserves the final source-visible `வணக்கம்.` as `Vanakkam.`; the following `★` remains structural.

No canonical Tamil transcription, scene derivative, dialogue record, character record or song inventory was modified by the English translation reconciliation.

## Next activity

No required English translation activity remains. Optional future work may build publication-facing reader/export derivatives from this verified layer without changing the canonical Tamil or structured source layers.
