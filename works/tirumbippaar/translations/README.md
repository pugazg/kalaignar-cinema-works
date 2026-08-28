# திரும்பிப்பார்! — English translation layer

**Canonical authority:** corrected/scan-closed Tamil transcription, reconciled 93-scene derivatives, immutable **1,042-record** dialogue corpus, and regenerated character/entity layer  
**Target language:** English (`en`)  
**Status:** **corrected-source reconciliation in progress**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the authoritative Tamil source.

The historical English pass had been recorded as **93 scenes / 1,321 verified units / 1,040 labelled dialogue links**. That state is historical: the corrected Tamil pass recovered two omitted scene-41 dialogue records and corrected many exact source readings, labels and scene boundaries. English verification is therefore being reopened against the stable corrected Tamil corpus.

## Files

- `schema.json` — schema for the 93 scene-sharded source-linked translation records.
- `index.json` — current English reconciliation/integrity checkpoint.
- `records/scene-XX.json` — 93 scene-sharded English translation records.
- `../editions/en/` — publication-facing reader/export layer; currently downstream-stale until this English reconciliation stabilizes.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every source-labelled utterance must be linked exactly once.** The immutable source corpus contains **1,042** labelled dialogue records.
3. **Exact Tamil speaker labels stay exact metadata.** Character/entity mapping does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the corrected scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from external sources.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material do not receive invented speakers or dialogue-record IDs.
9. **The printed `★` is structural.** It is not translated into an invented `(Scene ends.)` unit.
10. **Historical translation-unit IDs are preserved.** New unit IDs are added only where the corrected source proves that a unit was omitted; unsupported historical units may be removed only when the corrected source proves that they do not belong.

## Current corrected-source reconciliation

The ordinary 10-scene pass is now complete through **scene 81**. Scenes **1–81** are contiguous `corrected-source-reconciled` coverage.

### Scenes 72–81 — latest 10-scene iteration

- **Scene 72:** removes the false historical distinction between `அழித்தெழுதாச்` and `அழுத்தெழுதாச்`. The corrected source prints `அழித்தெழுதாச் சித்திரமே` in both linked utterances. The unclear colloquial opening before the one-rupee action is translated conservatively rather than expanded into an unsupported instruction about taking money.
- **Scene 73:** corrected-source comparison found no material English wording change.
- **Scene 74:** the court plea preserves the request for a warning and forgiveness without making the repeated `மன்னிப்புக் கேட்டுக்கொள்கிறேன்` sound like three separate forgiveness requests.
- **Scene 75:** removes the unsupported addition of “confession” from `பாவ மன்னிப்புப் படலம்`; the source says a chapter/episode of pardon for sins.
- **Scene 76:** restores exact `புண்யகோடி` and `பூமாலை`; gives the duplicated `என்னய்யா ஒதற்றே` one consistent rendering; restores the livelihood sense of the source dirt/food imagery; and leaves the unusual `நிழல் மாடு` conservative rather than guessing a normalization. The genuine PDF 91→92 dialogue remains one English unit.
- **Scene 77:** restores exact `பூமாலை` and `உஷா`; preserves the unfinished `அவர்களை மறுபடியும்...` without supplying a missing action; renders `பிராயச்சித்தம்` as **atonement**; and restores the past-tense sense that the workers had worked for the mill owner.
- **Scene 78:** corrected-source comparison found no material English wording change.
- **Scene 79:** retains exact source speaker metadata `அவன் குரல்` rather than normalizing it to Pandiyan and corrects Poomaalai's English name.
- **Scene 80:** restores exact `பூமாலை` and `உஷா`; corrects the stage action so Poomaalai **jumps up** rather than snores; restores `சூதும், சூழ்ச்சியும் சுகபோக வெறியும்` as deceit, intrigue and a frenzy for sensual pleasure; restores `பயங்கர மிருகமே` as **terrifying beast**; and keeps the difficult `அந்தியின் மொத்த வியாபாரியே` phrase explicitly unresolved rather than inventing a reading. The PDF 96→97 and 97→98 cross-page units remain intact.
- **Scene 81:** restores the source-visible final `(ஓடுகிறான்)` as new `tirumbippaar-en-s081-u006` — `(He runs.)` — without renumbering any historical unit IDs.

No historical dialogue-linked unit IDs were renumbered in this batch. The only net unit-count change is the source-proven final scene-81 stage direction.

The live English layer now contains **1,326 units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **258 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are linked**. Link coverage is not the same as textual reconciliation: scenes **1–81** are source-reconciled; scenes **82–93** still require corrected-source comparison.

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

`../editions/en/` still contains the previously generated Markdown, standalone HTML and machine-readable JSON reader editions together with their historical QA/manifest outputs. Those files remain **known-stale downstream derivatives** until corrected-source English reconciliation completes and the reader/export layer is regenerated and revalidated.

## Next activity

Continue the ordinary corrected-source English pass with **scenes 82–91 as one 10-scene iteration**. Compare each existing English unit against the corrected scene/dialogue source, update exact speaker metadata and materially affected English wording, preserve historical unit IDs, add only source-proven omitted units, remove unsupported historical units only when the corrected source proves they do not belong, and keep reader/EPUB regeneration blocked until the English layer reaches a stable full-work boundary.
