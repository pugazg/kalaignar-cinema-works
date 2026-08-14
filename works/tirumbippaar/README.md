# திரும்பிப்பார்!

Archival intake for the scanned first-edition screenplay/dialogue booklet **`திரும்பிப்பார்!`** credited on the cover as `கதை - வசனம் — கலைஞர் மு. கருணாநிதி`.

## Source checkpoint

- Source file: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`
- Source identifier: `TVA_BOK_0014652`
- PDF pages: **112**
- File size: **173,960,052 bytes**
- SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`
- Explicit edition statement: **`முதல் பதிப்பு: 1953`**
- Main screenplay range: PDF **9–112** / printed pp. **1–104**
- Source scan: image-based; embedded OCR is not canonical evidence

The cover also shows `திராவிடப் பண்ணை` and `தெப்பக்குளம் :: திருச்சி`. PDF 2 prints `உரிமையுடையது.` and `விலை ரூ. 0-10-0`; this archive records those source statements without turning them into a present-day rights determination.

The lower PDF-2 imprint line remains physically cropped. High-resolution reinspection supports only `சிட்டி பிரஸ், மதுரை ரோ…`; the missing continuation is not reconstructed.

## Current archival status

- source intake: **complete**
- full-scan scene-number/start-page pass: **complete**
- structural mapping: **verified**
- scene-heading / structural-label audit: **93/93 dispositioned**
- observed scene numbers: **93**, consecutively **1–93**
- scene numbering gaps/repeats/out-of-order findings: **none observed**
- main-text missing/duplicate/crop findings: **none observed**
- canonical Tamil first-pass transcription: **complete — PDF 9–112 / printed pp.1–104**
- canonical Tamil page status: **104 verified / 0 draft / 0 review**
- fidelity audit: **complete**
- unresolved audited main-text pages: **0**
- scene index: **complete — 93/93**
- scene-text derivatives: **complete — 93/93**
- dialogue index: **in progress — scenes 1–50 complete, 593 records**
- character index: **not-started**
- song authorship mapping / Tamil song derivatives: **not-started**
- English translation: **not-started**

`mapping.md` records the verified structural gate. `notes/scene-heading-audit.md` contains the 93-scene structural-label audit, source-visible irregular forms and mapped performance/printed-text candidates. `notes/fidelity-audit.md` records the complete page-by-page source corrections and verification history.

Canonical Tamil transcription is indexed at `transcription/full-text.md` and stored in five verified source-order files under `transcription/parts/`. The complete scene layer is under `scenes/`. The dialogue derivative is under `dialogues/`, using a fixed schema and scene-sharded record files.

Earlier audit work found two first-pass integrity defects: PDF **61–63 / printed pp.53–55** had been omitted from the stored part 03, and the PDF **80 / printed p.72** text lacked an explicit page anchor. Both were repaired from the scan and have since passed normal fidelity verification.

The final PDF 84–112 audit also corrected a prior structural reading for scene 72: the source heading at PDF **87 / printed p.79** is `[தாசி வீடு`, not `[காசி வீடு`.

During dialogue-index batch 5, direct comparison with the verified Part 03 canonical transcription exposed a prior drift in `scenes/scene-41.md`. The scene derivative was repaired to restore the canonical opening Pandiyan/Paranthaman exchange and the missing PDF 54 page anchor. No canonical transcription was changed.

## Source discipline

The supplied scan is the controlling source. Do not modernize spelling or punctuation, normalize speaker labels, repair scene headings from film knowledge, fill unreadable text from subtitles/audio/web copies, or infer lyric authorship from proximity.

The dialogue index follows the same discipline: only explicitly speaker-labelled utterances become dialogue records. Speaker labels remain exact; standalone narrative/stage directions and unlabelled material are not silently assigned to a character. Scenes 10, 11, 25, 26 and 43 therefore correctly have zero dialogue records. The scene-29 standalone `கோஷம்`, scene-31 unlabelled song-performance material, scene-33 unlabelled speech after a standalone direction, and scene-44 unlabelled continuation after `(கருடன் ஆத்திரம்)` remain in the canonical/scene layer rather than being silently assigned.

Three cross-page dialogue records are currently verified: `tirumbippaar-s001-d006`, `tirumbippaar-s041-d034`, and `tirumbippaar-s045-d015`.

## Exact next activity

Continue the **dialogue index with scenes 51–60** from the completed scene derivatives and verified canonical Tamil. Keep the fixed dialogue schema, preserve exact source labels and text, record PDF/printed-page provenance, and use `page_segments` only when one labelled utterance crosses a page boundary.
