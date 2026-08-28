# திரும்பிப்பார்! — English translation layer

**Canonical authority:** corrected/scan-closed Tamil transcription, reconciled 93-scene derivatives, immutable **1,042-record** dialogue corpus, and regenerated character/entity layer  
**Target language:** English (`en`)  
**Status:** **corrected-source reconciliation in progress**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the authoritative Tamil source.

The historical English pass had been recorded as **93 scenes / 1,321 verified units / 1,040 labelled dialogue links**. That state is historical: the corrected Tamil pass recovered two omitted scene-41 dialogue records and corrected many exact source readings, labels and scene boundaries. English verification is therefore being reopened against the stable corrected Tamil corpus rather than silently carrying the old `verified` claim forward.

## Files

- `schema.json` — schema for the 93 scene-sharded source-linked translation records.
- `index.json` — current English reconciliation/integrity checkpoint.
- `records/scene-XX.json` — 93 scene-sharded English translation records.
- `../editions/en/` — publication-facing reader/export layer; currently treated as downstream-stale until this English reconciliation stabilizes.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every source-labelled utterance must be linked exactly once.** The immutable source corpus contains **1,042** labelled dialogue records.
3. **Exact Tamil speaker labels stay exact metadata.** Character/entity mapping does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the corrected scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from audio, web pages, streaming metadata or another booklet.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material do not receive invented speakers or dialogue-record IDs.
9. **The printed `★` is structural.** It is not translated into an invented `(Scene ends.)` unit.
10. **Historical translation-unit IDs are preserved.** New unit IDs are added only where the corrected source proves that a unit was omitted; unsupported historical units may be removed only when the corrected source proves that they do not belong.

## Current corrected-source reconciliation

The ordinary 10-scene pass is now complete through **scene 61**. Scenes **1–61** are therefore contiguous `corrected-source-reconciled` coverage.

### Scenes 52–61 — latest 10-scene iteration

Representative repairs include:

- **Scene 52:** exact `புண்யகோடி` metadata is restored. `நாணயமான` is corrected from the false “motherly man” reading to an upright/honest leader; Pandiyan is restored as `பெரிய பகுத்தறிவுவாதி / இலட்சிய வீரன் / உண்மைத் தொண்டன்`; the social-reform list is translated from the actual source; and the rain joke now correctly says even rain making the town prosper would be rejected if cinema were to disappear.
- **Scene 53:** `புஸ் வாணங்கள்` is corrected from the invented “trailing tiger's tail” metaphor to **dud fireworks**; the diamond/necklace wording is also brought back to the printed source.
- **Scene 54:** corrected-source comparison found no material wording change; the newspaper block is retained and its reconciliation status is advanced.
- **Scene 55:** exact `பூமாலை` metadata is restored; `கூடாதென்றா சொல்கிறேன்` is correctly a question rather than a prohibition; `உற்றார் உறவினர்` is restored as kith and kin; Paranthaman's `என்னை ஒருபோதும் காட்டிக் கொடுக்க மாட்டாயே` is restored as a direct appeal to Poomaalai; and the source-visible final `(பூமாலை போகிறாள்)` action is added as `tirumbippaar-en-s055-u016`.
- **Scene 56:** exact `உஷா` metadata is restored; Paranthaman's first address to Usha is repaired; `அராஜகத்திற்கு ஆரம்பவிழா` is restored as an inaugural ceremony for lawlessness; and the false historical claim that friends had informed him where the necklace was is removed. The source instead has him infer that the stolen necklace must be in Pandiyan's house and urge an immediate police search.
- **Scene 57:** exact `பூமாலை` metadata is restored; Poomaalai's `உண்மையைச் சொன்னா கோபமா?` is corrected; `எய்ட் செவன் சிக்ஸ்` is retained without inventing a different code; and the jeep-stage direction now correctly shows Poomaalai catching and embracing Kumudha as she runs after Pandiyan crying.
- **Scene 58:** corrected-source comparison found no material wording change.
- **Scenes 59–60:** the now-clear `எனக்கும் விடுதலையில்லாமலா போய்விடப் போகிறது` is translated rather than marked corrupt. The unsupported historical `(Kumudha leaves.)` unit is removed from scene 59 and restored at the source-proven beginning of scene 60 as new `tirumbippaar-en-s060-u016`. Scene 60 also restores exact `பூமாலை`, the sibling-affection comparison in `சகோதர வாஞ்சை`, and the direction of `முன்பே சொன்னாயே; காட்டிக் கொடு என்று`.
- **Scene 61:** the unsupported historical `(Kumudha sobs.)` unit is removed. The corrected scene ends with the manager's order; the next scene separately begins with `(குமுதா நகருதல்)` and will be handled in the following batch.

No historical dialogue-linked unit IDs were renumbered in this batch. Source-proven new stage units use new IDs, while unsupported historical stage units are removed only where the corrected source proves they do not belong or places the action in a neighboring scene.

The live English layer remains at **1,324 units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **256 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are linked**. Link coverage is not the same as textual reconciliation: scenes **1–61** are source-reconciled; scenes 62–93 still require corrected-source comparison.

## Cross-page English units

The cross-page list remains structurally valid:

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
- `tirumbippaar-en-s034-u012`
- `tirumbippaar-en-s044-u004`
- `tirumbippaar-en-s084-u002`
- `tirumbippaar-en-s088-u004`
- `tirumbippaar-en-s091-u014`

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — remain represented from source-visible narrative/performance/written material.

## Song/performance constraint

Seven translated song references remain linked to source occurrences `tirumbippaar-song-001`, `002`, `003`, `004`, `006`, `007` and `008`. The booklet prints no complete lyric body for either source-named soundtrack song, so this layer continues to contain **zero reconstructed full-song translations**. The scene-29 labour slogan and scene-86 begging chant remain chants, not fabricated soundtrack lyrics.

## Reader/export status

`../editions/en/` still contains the previously generated Markdown, standalone HTML and machine-readable JSON reader editions together with their historical QA/manifest outputs. Those files are **known-stale downstream derivatives** until corrected-source English reconciliation completes and the reader/export layer is regenerated and revalidated.

## Next activity

Continue the ordinary corrected-source English pass with **scenes 62–71 as one 10-scene iteration**. Compare each existing English unit against the corrected scene/dialogue source, update exact speaker metadata and materially affected English wording, preserve historical unit IDs, add only source-proven omitted units, remove unsupported historical units only when the corrected source proves they do not belong, and keep reader/EPUB regeneration blocked until the English layer reaches a stable full-work boundary.
