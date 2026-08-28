# திரும்பிப்பார்! — English translation layer

**Canonical authority:** corrected/scan-closed Tamil transcription, reconciled 93-scene derivatives, immutable **1,042-record** dialogue corpus, and regenerated character/entity layer  
**Target language:** English (`en`)  
**English source-reconciliation status:** **complete — all 93 scenes**  
**Archive-wide status:** **canonical/scene/dialogue/character/English source layers synchronized; reader/export/EPUB rebuild pending**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the authoritative Tamil source.

The historical English pass had been recorded as **93 scenes / 1,321 verified units / 1,040 labelled dialogue links**. The corrected Tamil work recovered two omitted scene-41 dialogue records and exposed multiple source-reading, speaker-label, unit-boundary and scene-boundary errors. The complete corrected-source English reconciliation now supersedes that historical state.

## Translation principles

1. **Tamil remains authoritative.** English fluency is never evidence for changing the canonical Tamil.
2. **Every source-labelled utterance is linked exactly once.** The immutable source corpus contains **1,042** labelled dialogue records.
3. **Exact Tamil speaker labels stay exact metadata.** Character/entity mapping does not rewrite them.
4. **Stage directions do not gain action.** Translate only what the corrected scene supplies.
5. **Dialogue preserves rhetorical force.** Repetition, questions, code-switching, imagery and political/social rhetoric are not silently flattened.
6. **Cross-page source units remain one English unit.** Genuine source-spanning units retain all page provenance.
7. **Song/performance material is limited to what this booklet prints.** Do not import absent lyrics from external sources.
8. **Unlabelled source material stays unlabelled.** Direct speech, letters, newspaper blocks, advertisements, chants and other source-visible material do not receive invented speakers or dialogue-record IDs.
9. **The printed `★` is structural.** It is not translated into an invented `(Scene ends.)` unit.
10. **Historical surviving translation-unit IDs are preserved.** New IDs were added only where the corrected source proved omitted material; unsupported historical units were removed only where the source proved they did not belong.

## Complete corrected-source reconciliation

Scenes **1–93** are now contiguous `corrected-source-reconciled` coverage.

The final pass closed **scenes 92–93**:

- **Scene 92:** retains the source-boundary repair that moved `பத்திரிகை News / (அக்காள் தம்பியைக் கொன்றாள்)` out of scene 91 and into its actual scene-92 opening; restores the printed **Court** setting as new `tirumbippaar-en-s092-u004`; keeps both labelled dialogue links unchanged; and uses exact **Poomaalai** naming in the judgment.
- **Scene 93:** restores exact `பூமாலை` speaker metadata and **Poomaalai** naming throughout; restores the printed **Jail** setting as new `tirumbippaar-en-s093-u013`; preserves the female-student passage, the final children/warders action, `வணக்கம்.`, and the structural closing star without inventing a scene-end translation unit.

No surviving historical translation-unit IDs were renumbered in this final pass.

The reconciled English layer contains **1,330 verified units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **262 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs remain linked**. The seven direct source-unlabelled spoken units remain unlabelled, and all 12 genuine cross-page English units remain intact.

## Canonical Part04 synchronization — closed

The final whole-layer audit had identified three stale strings in `../transcription/parts/part-04-pdf-64-91.md` while the corresponding scene/dialogue derivatives were already correct. The canonical file has now been synchronized without changing scene structure or stable IDs:

- `இதெல்லாம் சினிமா. ஈ. எப்ப ஒழியுமோ` → `இதெல்லாம் சினிமா. எப்ப ஒழியுமோ`
- `ஏல்லாம் உன் தம்பியின்` → `எல்லாம் உன் தம்பியின்`
- `[புண்ணகோடி கதவைத் தட்டல்]` → `[புண்யகோடி கதவைத் தட்டல்]`

The canonical Part04 blocker is therefore **closed**. These corrections merely bring the upstream part file into agreement with the already-reconciled scene/dialogue source layer; they do not alter the immutable **1,042-record** dialogue total or any stable translation-unit IDs.

## Cross-page English units

The verified cross-page units remain:

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

These seven source-visible passages remain dialogue-kind units without invented speaker metadata or dialogue-record IDs:

- `tirumbippaar-en-s005-u026`
- `tirumbippaar-en-s015-u018`
- `tirumbippaar-en-s034-u012`
- `tirumbippaar-en-s044-u004`
- `tirumbippaar-en-s084-u002`
- `tirumbippaar-en-s088-u004`
- `tirumbippaar-en-s091-u014`

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — remain represented from source-visible narrative/performance/written material.

## Reader/export status

`../editions/en/` still contains the historical Markdown, standalone HTML and machine-readable JSON reader editions together with their earlier QA/manifest outputs. They remain **downstream-stale until the deterministic publication workflow rebuilds and revalidates them against the now-synchronized source and English layers**.

## Next activity

Run the deterministic Tirumbippaar English publication workflow to regenerate and revalidate the Markdown/HTML/JSON reader derivatives, EPUB package, QA reports, manifests and synchronized work metadata. Archive-wide publication closure can be declared only after that workflow passes.