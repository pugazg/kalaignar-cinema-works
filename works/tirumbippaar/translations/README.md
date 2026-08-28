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

The ordinary 10-scene pass is now complete through **scene 51**. Scenes **1–51** are therefore contiguous `corrected-source-reconciled` coverage.

### Scenes 42–51 — latest 10-scene iteration

Representative repairs include:

- **Scenes 42–43:** the written-song performance and printed `“கலப்படம் கலப்படம்”` refrain are restored to scene 43, where the corrected source places them. Scene 42 now contains only its own source-visible material. No absent lyrics are reconstructed.
- **Scene 44:** `மந்தி` is restored as **monkey**, not the historical “minister”; `புகழ் தேடும் பூனைகள்` is restored as **cats seeking fame**, not cats in invented tiger skins. The source-unlabelled continuation remains unlabelled.
- **Scene 45:** exact `உஷா` metadata is restored; `சமதர்மம். சமத்துவம்.` is retained as **“Egalitarianism. Equality.”**; the `மஞ்சம் / பஞ்சம் / லஞ்சம்` rhetoric preserves the owner-on-bed / toiler-in-famine contrast and **swimming in bribes**; `கைகால் அசையாது` restores both hands and legs.
- **Scenes 46–47:** the revolver action is removed from the end of scene 46 and restored at the beginning of scene 47 as new unit `tirumbippaar-en-s047-u023`. Exact `பூமாலை` metadata is restored, and the flower-grove image no longer invents a cuckoo.
- **Scene 48:** exact `புண்யகோடி` metadata is restored, `மேஸ்திரி` is translated as **foreman**, and `நான் சங்கத்துப் பக்கம் போய்ட்டு வர்றேன்` retains the movement/future-return sense.
- **Scene 49:** exact `புண்யகோடி` metadata is restored; the direction indicates Radha; the source asks for **tea or coffee**; `பாடுமா?` is **“Can she sing?”**; and the cuckoo comparison is translated without inventing Kumudha.
- **Scene 50:** corrected-source comparison found no material English wording change; its status has been advanced without gratuitous rewriting.
- **Scene 51:** the complete labelled `tirumbippaar-s051-d001` utterance is consolidated into historical `u001`, including its internal directions and spoken continuation. Historical false split units `u002` and `u003` are removed. The difficult `சராசரங்கள்...` phrase is translated conservatively rather than completed from guesswork.

No historical dialogue-linked unit IDs were renumbered in this batch. The scene-42→43 song boundary and scene-46→47 revolver boundary are source-location corrections; scene 51 removes a false split rather than deleting source speech.

The live English layer now contains **1,324 units**:

- **1,049 dialogue-kind units** = 1,042 labelled source dialogue links + 7 deliberately unlabelled source-spoken units;
- **256 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are linked**. Link coverage is not the same as textual reconciliation: scenes **1–51** are source-reconciled; scenes 52–93 still require corrected-source comparison.

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

Continue the ordinary corrected-source English pass with **scenes 52–61 as one 10-scene iteration**. Compare each existing English unit against the corrected scene/dialogue source, update exact speaker metadata and materially affected English wording, preserve historical unit IDs, add only source-proven omitted units, remove unsupported historical units only when the corrected source proves they do not belong, and keep reader/EPUB regeneration blocked until the English layer reaches a stable full-work boundary.
