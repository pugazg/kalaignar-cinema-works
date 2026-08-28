# திரும்பிப்பார்! — English translation layer

**Canonical authority:** corrected/scan-closed Tamil transcription, reconciled 93-scene derivatives, immutable **1,042-record** dialogue corpus, and regenerated character/entity layer  
**Target language:** English (`en`)  
**Status:** **corrected-source reconciliation in progress**

This directory contains interpretive English derivatives. Nothing here repairs, normalizes, expands or overwrites the authoritative Tamil source.

The historical English pass had been recorded as **93 scenes / 1,321 verified units / 1,040 labelled dialogue links**. That state is historical: the Tamil corrected-source pass recovered two omitted scene-41 dialogue records and corrected many exact source readings and labels. English verification is therefore being reopened against the stable corrected Tamil corpus rather than silently carrying the old `verified` claim forward.

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
11. **Historical translation-unit IDs are preserved.** New unit IDs are added only where the corrected source proves that a unit was omitted; existing IDs are not renumbered simply to restore source order. Unsupported historical units may be removed when the corrected source proves that they do not belong.

## Current corrected-source reconciliation

The ordinary 10-scene pass has now reached **scene 40**. Because scene **41** was reconciled earlier after two labelled Tamil utterances were recovered there, the English corrected-source coverage is now contiguous through **scene 41**.

### Scenes 31–40 — latest 10-scene iteration

Scenes **31–40** have been compared against the corrected scene/dialogue source and marked `corrected-source-reconciled`.

Representative corrections include:

- scene 31 required no material English wording change beyond advancing its corrected-source status;
- scene 32 restores exact `புண்யகோடி` metadata, removes invented `Run...run` wording from `தொழிலாளி. தொழிலாளியாம் தொழிலாளி`, and restores `தொழிலாளி சம்பளம் ஜாஸ்தியா கேட்டா, அதை சிந்திச்சு பார்க்க` as a call to consider a worker's request for higher wages rather than an agitation reference;
- scene 33 restores exact `புண்யகோடி`, corrects `நாமெல்லோரும்` from the unsupported “whole country” reading, removes invented red-paddy wording from Paranthaman's speech, and removes the cheers/Punyakodi-delight action that actually belongs at the beginning of scene 34;
- scene 34 restores those opening cheers in their proper scene, adds the source-visible `[பூமாலை பிள்ளைகளுடன்!]` direction, restores `முகுந்தா`, separates the source-unlabelled `பாண்டியன்` answer without inventing a speaker or dialogue-record ID, and corrects `உதடுகள் முணுமுணுக்கின்றன` from the stale “Garudan murmurs” reading;
- scene 35 restores exact `பூமாலை` metadata and repairs `கானத்தால்` as song/music rather than sight, preserves the difficult `தெரியவில்லை...` line conservatively, and restores `அதட்டாதே` as a rebuke against being snapped/scolded at rather than “don't interfere”;
- scene 36 restores exact `பூமாலை`, corrects Kumudha's `ஏன் சின்னம்மா என்னை அடிச்சே`, restores her question about whether uncle may treat Pandiyan that way, preserves the unfinished `அவனை எனக்கு நேராகவே` without supplying a missing action, and removes the unsupported historical departure unit;
- scene 37 restores exact `புண்யகோடி` throughout, improves the father/son wording around `பெத்து வளர்த்து பாதுகாத்து மனுஷனாக்கி`, and moves the source-visible `(போகிறாள்)` carry-over action from the end of scene 36 to the beginning of scene 37 as new unit `u051`;
- scene 38 restores exact `பூமாலை`, corrects `குமுதா உங்களை அழைக்கிறாள்`, removes unsupported “melting heart” wording, restores the imperative force of `கண்ணீரைத் துடையுங்கள்`, and removes the historical walking action that belongs to the next scene;
- scene 39 restores that `(பாண்டியன் நடக்கிறான் அவளுடன்)` action at the beginning of its proper scene as new unit `u026`, restores Punyakodi naming, renders `புண்யகோடியை மாற்றினால்தான்` as winning Punyakodi over, and removes the historical `(The two rise.)` action from the end of the scene;
- scene 40 restores `(இருவரும் எழுதல்)` at the beginning of its proper scene as new unit `u006` and restores exact `புண்யகோடி` metadata.

Earlier reconciled scenes **1–30** retain their corrected-source repairs. Scene **41** retains its recovered-source repair: `tirumbippaar-s041-d037` and `tirumbippaar-s041-d038` remain linked as `tirumbippaar-en-s041-u050` and `u051`, historical `u046` remains linked to corrected cross-page `d034`, and the source-visible Kumudha/Pandiyan departure direction remains `u052`.

No historical dialogue-linked unit IDs were renumbered in scenes 31–40. Source-proven omitted actions were added with new IDs, while unsupported historical units were removed only where the corrected source located the action in a neighboring scene or proved it absent.

The live English layer now contains **1,326 units**:

- **1,050 dialogue-kind units** = 1,042 labelled source dialogue links + 8 deliberately unlabelled source-spoken units;
- **257 stage-direction units**;
- **7 song-reference units**;
- **2 chant units**;
- **10 written-text units**;
- **0 reconstructed full-song units**.

All **1,042 dialogue record IDs are linked**. Link coverage is not the same as textual reconciliation: scenes **1–41** are source-reconciled; scenes 42–93 still require corrected-source comparison.

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

These eight source-visible spoken passages remain `dialogue` units without invented speaker metadata or dialogue-record IDs:

- `tirumbippaar-en-s005-u026`
- `tirumbippaar-en-s015-u018`
- `tirumbippaar-en-s034-u012`
- `tirumbippaar-en-s044-u004`
- `tirumbippaar-en-s051-u003`
- `tirumbippaar-en-s084-u002`
- `tirumbippaar-en-s088-u004`
- `tirumbippaar-en-s091-u014`

The six source scenes with no labelled dialogue records — **10, 11, 25, 26, 43 and 54** — remain represented from source-visible narrative/performance/written material.

## Song/performance constraint

Seven historical translated song references remain linked to source occurrences `tirumbippaar-song-001`, `002`, `003`, `004`, `006`, `007` and `008`. The booklet prints no complete lyric body for either source-named soundtrack song, so this layer continues to contain **zero reconstructed full-song translations**. The scene-29 labour slogan and scene-86 begging chant remain chants, not fabricated soundtrack lyrics.

## Reader/export status

`../editions/en/` still contains the previously generated Markdown, standalone HTML and machine-readable JSON reader editions, together with their historical QA/manifest outputs. Those files are **known-stale downstream derivatives** until corrected-source English reconciliation completes and the reader/export layer is regenerated/revalidated.

## Next activity

Continue the ordinary corrected-source English pass with **scenes 42–51 as one 10-scene iteration**. Compare each existing English unit against the corrected scene/dialogue source, update exact speaker metadata and materially affected English wording, preserve historical unit IDs, add only source-proven omitted units, remove unsupported historical units only when the corrected source proves they do not belong, and keep reader/EPUB regeneration blocked until the English layer reaches a stable full-work boundary.
