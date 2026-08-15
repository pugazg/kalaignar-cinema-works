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
- dialogue index: **complete — 93/93 scenes, 1,040 records**
- character index: **complete-verified — 45/45 exact labels, 39 entities/role categories**
- song authorship mapping: **complete — 8 occurrences dispositioned; 3 verified / 5 unresolved**
- source-named songs with verified item-level authorship: **2**
- Tamil song derivative files: **0 — no full lyric body for either source-named song is printed in this booklet**
- English translation: **complete-verified — scenes 1–93, 1,330 units**

`mapping.md` records the verified structural gate. `notes/scene-heading-audit.md` contains the 93-scene structural-label audit, source-visible irregular forms and mapped performance/printed-text candidates. `notes/fidelity-audit.md` records the complete page-by-page source corrections and verification history. Later source corrections discovered during derivative work are recorded separately in `notes/post-fidelity-corrections.md`.

Canonical Tamil transcription is indexed at `transcription/full-text.md` and stored in five verified source-order files under `transcription/parts/`. The complete scene layer is under `scenes/`. The completed dialogue derivative is under `dialogues/`, using a fixed schema and 93 scene-sharded record files. The completed character/entity layer is under `characters/`; it inventories all 45 exact dialogue speaker labels and gives each one a verified named-character, role, or collective disposition without modifying any dialogue record. The song/performance authorship gate is under `songs/`. The completed source-linked English derivative is under `translations/`.

Earlier audit work found two first-pass integrity defects: PDF **61–63 / printed pp.53–55** had been omitted from the stored part 03, and the PDF **80 / printed p.72** text lacked an explicit page anchor. Both were repaired from the scan and have since passed normal fidelity verification.

The final PDF 84–112 audit also corrected a prior structural reading for scene 72: the source heading at PDF **87 / printed p.79** is `[தாசி வீடு`, not `[காசி வீடு`.

During dialogue-index batch 5, direct comparison with the verified Part 03 canonical transcription exposed a prior drift in `scenes/scene-41.md`. The scene derivative was repaired to restore the canonical opening Pandiyan/Paranthaman exchange and the missing PDF 54 page anchor. No canonical transcription was changed.

During the later song-authorship gate, direct rendered-scan reinspection of **PDF 38 / printed p.30** found another source-level correction: scene 31 prints the song title **`பாண்டியன் என் சொல்லை`**, not the earlier transcription `பாண்டியன் என் செல்வம்`. Both the canonical Part 03 transcription and scene-31 derivative were corrected from the scan; `notes/post-fidelity-corrections.md` records the change. Page counts/status remain **104 verified / 0 draft / 0 review**.

## Source discipline

The supplied scan is the controlling source. Do not modernize spelling or punctuation, normalize speaker labels, repair scene headings from film knowledge, fill unreadable text from subtitles/audio/web copies, or infer lyric authorship from proximity.

The dialogue index follows the same discipline: only explicitly speaker-labelled utterances become dialogue records. Speaker labels remain exact; standalone narrative/stage directions and unlabelled material are not silently assigned to a character. Scenes **10, 11, 25, 26, 43 and 54** therefore correctly have zero dialogue records.

The completed dialogue layer contains **eight** verified cross-page utterances: `tirumbippaar-s001-d006`, `tirumbippaar-s041-d034`, `tirumbippaar-s045-d015`, `tirumbippaar-s063-d003`, `tirumbippaar-s072-d001`, `tirumbippaar-s076-d012`, `tirumbippaar-s080-d022`, and `tirumbippaar-s080-d028`.

Unlabelled structures remain in the canonical/scene layer rather than being silently converted to dialogue. Examples include the scene-29 `கோஷம்`, scene-31 song-performance material, scene-43 `கலப்படம்` performance description, scene-44 platform-speech continuation after the Garudan reaction direction, scene-54 newspaper report, scene-83 letter, scene-84 unlabelled advertisement reading, scene-85 address card, scene-91 `பத்திரிகை News`, and the final `வணக்கம்.` in scene 93.

The character layer likewise does not rewrite source labels. `குணமணி` and `குண்டுமணி` are source-supported variants mapped to one household-helper character; scene-79 `அவன் குரல்` maps to Pandiyan from the scene context. By contrast, the reused exact label `குரல்` remains a role category because it represents different contextual voices in scenes 38, 67 and 72. Generic `பையன்`, worker labels, police labels and `Echo` are also retained as role/collective categories rather than being falsely turned into named individuals.

The song layer follows an equally strict gate. Visual inspection of PDF **1–8** found no `பாடல்கள்` heading, lyricist list or item-level song credit; the cover's `கதை - வசனம்` credit is not treated as lyric authorship. Of eight source-visible song/performance occurrences, five remain unresolved because the booklet supplies no safe title/lyric evidence. Separately documented item-level soundtrack metadata is used only where the booklet itself names the song: **`பாண்டியன் என் சொல்லை` → பாரதிதாசன்** and **`கலப்படம்` → கண்ணதாசன்**. External metadata never supplies or repairs canonical lyrics.

No Tamil song-lyric derivative is created from absent text. Scene 31 prints only a named performance reference; scenes 42–43 print/name only `கலப்படம்` material rather than a complete lyric body. The canonical scene files therefore remain the complete source-supported Tamil record for these occurrences.

## English translation — final checkpoint

All **93 scenes** now contain **1,330 verified source-linked units**: **1,047 dialogue / 263 stage direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song units**. There are **0 review / 0 draft** units.

All **1,040 immutable labelled dialogue records** are linked exactly once. The remaining seven dialogue-kind units are source-visible spoken passages without a printed speaker label and therefore retain null speaker/dialogue-record metadata: scenes 5, 15, 44, 51, 84, 88 and 91.

There are **12 genuine cross-page English units**: scene 1 PDF 9→10; scene 26 PDF 31→32; scene 41 PDF 52→53 and PDF 56→57; scene 45 PDF 59→60; scene 61 PDF 78→79; scene 63 PDF 79→80; scene 72 PDF 87→88; scene 76 PDF 91→92; scene 80 PDF 96→97 and PDF 97→98; and scene 83 PDF 100→101.

The completion reconciliation replaced scene 31's temporary song-reference placeholder with exact occurrence `tirumbippaar-song-006`. Scene 57 was repaired so all **50** labelled source dialogue records are represented individually rather than collapsing its final confrontation into a summary. Translation-only `(Scene ends.)` units that had been created from structural `★` separators were removed.

The final dramatic structures remain source-specific: scene 80 preserves Poomaal's title-bearing `திரும்பிப்பார்` confrontation; scene 81 retains the printed `Reaction-Echo`; scene 90 retains `[மரணமூச்சுவிடும் பரந்தாமன்]`; scene 91 preserves `பத்திரிகை News` as written newspaper content; and scene 93 preserves final `வணக்கம்.` while leaving the following `★` structural.

No canonical Tamil, scene, dialogue, character or song-inventory layer was changed by the English translation or its final reconciliation.

## Exact next activity

No required English translation activity remains. Optional future work may build publication-facing reader/export derivatives from the verified English layer without changing the canonical Tamil or structured source layers.
