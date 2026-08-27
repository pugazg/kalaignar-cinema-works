# திரும்பிப்பார்! — English translation layer

**Canonical authority:** corrected/scan-closed Tamil transcription, reconciled 93-scene derivatives, immutable **1,042-record** dialogue corpus, and regenerated character/entity layer  
**Target language:** English (`en`)  
**Status:** **corrected-source reconciliation in progress**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the authoritative Tamil source.

The historical English pass had been recorded as **93 scenes / 1,321 verified units / 1,040 labelled dialogue links**. That state is now historical because the Tamil corrected-source pass recovered two omitted scene-41 dialogue records and corrected many exact source readings and labels. English verification is therefore being reopened against the stable corrected Tamil corpus rather than silently carrying the old `verified` claim forward.

## Files

- `schema.json` — schema for the 93 scene-sharded source-linked translation records.
- `index.json` — current English reconciliation/integrity checkpoint.
- `records/scene-XX.json` — 93 scene-sharded English translation records.
- `../editions/en/` — publication-facing reader/export layer; currently treated as downstream-stale until this English reconciliation stabilizes.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every source-labelled utterance must be linked exactly once.** The current immutable source corpus contains **1,042** labelled dialogue records.
3. **Exact Tamil speaker labels stay exact metadata.** Character/entity mapping does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the corrected scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material do not receive invented speakers or dialogue-record IDs.
9. **External authorship metadata is not translation text.** It may identify a song occurrence, but it cannot supply missing Tamil or English lyrics.
10. **The printed `★` is structural.** It is not translated into an invented `(Scene ends.)` unit.
11. **Historical translation-unit IDs are preserved.** New unit IDs are added only where the corrected source proves that a unit was omitted; existing IDs are not renumbered simply to restore source order.

## Current corrected-source reconciliation

Scene **41** is the first English scene fully reopened and reconciled because the Tamil pass proved two labelled utterances had been omitted there.

The scene-41 English layer now:

- links recovered `tirumbippaar-s041-d037` (`பூமாலை`) and `tirumbippaar-s041-d038` (`பரந்தாமன்`) as new English units `tirumbippaar-en-s041-u050` and `tirumbippaar-en-s041-u051`;
- preserves all historical translation-unit IDs instead of renumbering existing units;
- keeps historical `tirumbippaar-en-s041-u046` linked to cross-page dialogue `tirumbippaar-s041-d034` and replaces its old mistranscription with the corrected `அன்பைக் கேட்- / காமல் ஐஸ்வரியத்தைக் கேட்கும்...` meaning;
- adds the source-visible `(குமுதா போய்விடுகிறாள் பாண்டியனுடன்)` direction, missing from the historical English layer, as new unit `tirumbippaar-en-s041-u052`;
- updates exact `பூமாலை` speaker metadata and Poomalai naming in the English stage-direction text.

Accordingly, the live English layer currently contains **1,324 units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **255 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **11 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are now linked** in the English layer, but link coverage is not the same as textual reconciliation. The remaining historical scene files still need comparison against the corrected Tamil for exact source labels, wording, semantics and structure.

## Cross-page English units

The historical cross-page list remains structurally valid, including:

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

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — remain represented from source-visible narrative/performance/written material.

## Song/performance constraint

Seven historical translated song references remain linked to source occurrences `tirumbippaar-song-001`, `002`, `003`, `004`, `006`, `007` and `008`. The booklet prints no complete lyric body for either source-named soundtrack song, so this layer continues to contain **zero reconstructed full-song translations**. The scene-29 labour slogan and scene-86 begging chant remain chants, not fabricated soundtrack lyrics.

## Reader/export status

`../editions/en/` still contains the previously generated Markdown, standalone HTML and machine-readable JSON reader editions, together with their historical QA/manifest outputs. Those files are now **known-stale downstream derivatives** until corrected-source English reconciliation completes and the reader/export layer is regenerated/revalidated.

## Next activity

Continue scene-by-scene corrected-source English reconciliation beyond scene 41. For each scene, compare the existing English unit against the corrected scene/dialogue source, update exact speaker metadata and materially affected English wording, preserve historical unit IDs, add only source-proven omitted units, and keep reader/EPUB regeneration blocked until the English layer reaches a stable full-work boundary.
