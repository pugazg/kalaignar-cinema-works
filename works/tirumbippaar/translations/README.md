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

The ordinary source-order pass is now complete through **scene 91**. Scenes **1–91** are contiguous `corrected-source-reconciled` coverage.

### Scenes 82–91 — latest 10-scene iteration

- **Scene 82:** corrects the source phrase to `பண்பு கெட்ட வீணனே` in the note and restores `(பையன் எழுத)` as **the boy writes**, replacing the historical invented action that he gets up.
- **Scene 83:** preserves the source's **சென்னை / Chennai** rather than substituting Madras, corrects the boy's `ஏங்க...` from “Where...” to a contextual “Why, sir...”, and renders `மறுமலர்ச்சி` as revival. The genuine PDF 100→101 written appeal remains one cross-page unit.
- **Scene 84:** restores **Chennai**, separates Pandiyan's `ம்...` from the following printed `(வாங்கிக்கொண்டு போகிறான்)`, and adds that source-proven final action as new `tirumbippaar-en-s084-u008` without renumbering historical IDs.
- **Scene 85:** restores **Chennai** in the visible address and fixes the order and repetition of Pandiyan's discovery: `என் குமுதா அகப்பட்டுவிட்டாள் !` precedes the four printed `குமுதா!` cries.
- **Scene 86:** restores exact `புண்யகோடி` metadata and **Punyakodi** naming throughout the scene while preserving the collective `சாம்ப சதாசிவம்` begging chant as a chant rather than inventing an individual speaker.
- **Scene 87:** restores exact `பூமாலை` / **Poomaalai** and removes the invented “All right...” response: the corrected source prints only `...` for Gundumani.
- **Scene 88:** fixes the telegram pronoun: `தந்தி கொடுத்திருக்கிறாள்` is **“She's sent a telegram”**, not “He's sent a telegram.”
- **Scene 89:** restores exact `பூமாலை` and corrects the source-context telegram reference to **“the telegram she sent.”**
- **Scene 90:** restores exact `பூமாலை` / **Poomaalai**; restores Bama's `குமுதாவுக்கு வலைவீச` metaphor as **casting a net for Kumudha**; corrects Paranthaman's speech so **Poomaalai had already killed the old Paranthaman** rather than an invented third-person “they”; restores `அவசரப்பட்டு அறிவிழந்தேன்`; and adds the source-visible final `(பரந்தாமன் சாதல்)` as new `tirumbippaar-en-s090-u039`.
- **Scene 91:** restores exact `உஷா`, **Poomaalai**, and the correct PDF 110 provenance for `ஆங்!`; the newspaper heading historically attached to this scene is removed because the corrected Tamil places it at the opening of scene 92.

A necessary boundary spillover was made into **scene 92**: the source-visible `பத்திரிகை News / (அக்காள் தம்பியைக் கொன்றாள்)` block is now represented there as new `tirumbippaar-en-s092-u003`. Scene 92 is **not yet marked source-reconciled**; it remains part of the final 92–93 pass.

No historical surviving translation-unit IDs were renumbered. Scene 84 and scene 90 each gain one source-proven stage-direction unit; the scene-91 newspaper unit is removed from the wrong scene and recreated under scene 92, so that boundary repair is unit-count neutral.

The live English layer now contains **1,328 units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **260 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are linked**. Link coverage is not the same as textual reconciliation: scenes **1–91** are source-reconciled; scenes **92–93** still require their final corrected-source comparison.

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

Complete the corrected-source English pass with **scenes 92–93 as the final two-scene iteration**. Reconcile both against the corrected Tamil scene/dialogue layer, preserve surviving historical unit IDs, retain the scene-92 newspaper boundary repaired in this batch, add only source-proven omitted material, and then run a whole-English-layer integrity audit before any reader/export/EPUB regeneration.
