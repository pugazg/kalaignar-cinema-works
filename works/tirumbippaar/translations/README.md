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

The ordinary 10-scene pass is now complete through **scene 71**. Scenes **1–71** are contiguous `corrected-source-reconciled` coverage.

### Scenes 62–71 — latest 10-scene iteration

- **Scene 62:** restores the source-visible opening `(குமுதா நகருதல்)` as new `tirumbippaar-en-s062-u005`, exact `அம்மாமி` metadata, the omitted `கர்ப்ப ஸ்திரியை` pregnancy clause, and the explicit reference to nine daughters.
- **Scene 63:** restores exact `புண்யகோடி`, preserves the unfinished `என்ன, உங்களைத்தானே...` without guessed completion, and repairs Garudan's final single printed utterance while retaining the deliberate stable `d020`/`d021` split. The old invented telephone-call reading is removed.
- **Scenes 64–65:** corrected-source comparison found no material English wording change; both are advanced to `corrected-source-reconciled` without gratuitous rewriting.
- **Scene 66:** restores exact `புண்யகோடி` and removes the invented **Socrates** reference. `சாக்ஷாத் புரட்சி அவதாரம்` is rendered as the **very embodiment of revolution**.
- **Scene 67:** restores exact `புண்யகோடி`; Radha's source-printed dots remain dots rather than an invented vocalization; `சாப்ட்டு படுக்கணும்` restores the eat-and-go-to-bed meaning; and the gramophone/window directions follow the corrected source.
- **Scene 68:** corrected-source comparison found no material wording change.
- **Scene 69:** restores exact `புண்யகோடி`, corrects the stage action from Paranthaman covering Radha's cheek to covering her **eyes**, and retains the source's Indra–Gautama satire and arrest sequence without modernization.
- **Scene 70:** restores Punyakodi naming in the English text and the source `அய்யோ` exclamation.
- **Scene 71:** corrected-source comparison found no material wording change.

No historical dialogue-linked unit IDs were renumbered. The only net unit-count change in this batch is scene 62's source-proven opening stage direction.

The live English layer now contains **1,325 units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **257 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are linked**. Link coverage is not the same as textual reconciliation: scenes **1–71** are source-reconciled; scenes **72–93** still require corrected-source comparison.

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

Continue the ordinary corrected-source English pass with **scenes 72–81 as one 10-scene iteration**. Compare each existing English unit against the corrected scene/dialogue source, update exact speaker metadata and materially affected English wording, preserve historical unit IDs, add only source-proven omitted units, remove unsupported historical units only when the corrected source proves they do not belong, and keep reader/EPUB regeneration blocked until the English layer reaches a stable full-work boundary.
