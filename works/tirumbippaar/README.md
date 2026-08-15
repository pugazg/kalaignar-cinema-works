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
- English translation: **in-progress — scenes 1–10 verified, 124 units**

`mapping.md` records the verified structural gate. `notes/scene-heading-audit.md` contains the 93-scene structural-label audit, source-visible irregular forms and mapped performance/printed-text candidates. `notes/fidelity-audit.md` records the complete page-by-page source corrections and verification history. Later source corrections discovered during derivative work are recorded separately in `notes/post-fidelity-corrections.md`.

Canonical Tamil transcription is indexed at `transcription/full-text.md` and stored in five verified source-order files under `transcription/parts/`. The complete scene layer is under `scenes/`. The completed dialogue derivative is under `dialogues/`, using a fixed schema and 93 scene-sharded record files. The completed character/entity layer is under `characters/`; it inventories all 45 exact dialogue speaker labels and gives each one a verified named-character, role, or collective disposition without modifying any dialogue record. The song/performance authorship gate is under `songs/`. The source-linked English derivative is under `translations/`, with scenes 1–10 now verified.

Earlier audit work found two first-pass integrity defects: PDF **61–63 / printed pp.53–55** had been omitted from the stored part 03, and the PDF **80 / printed p.72** text lacked an explicit page anchor. Both were repaired from the scan and have since passed normal fidelity verification.

The final PDF 84–112 audit also corrected a prior structural reading for scene 72: the source heading at PDF **87 / printed p.79** is `[தாசி வீடு`, not `[காசி வீடு`.

During dialogue-index batch 5, direct comparison with the verified Part 03 canonical transcription exposed a prior drift in `scenes/scene-41.md`. The scene derivative was repaired to restore the canonical opening Pandiyan/Paranthaman exchange and the missing PDF 54 page anchor. No canonical transcription was changed.

During the later song-authorship gate, direct rendered-scan reinspection of **PDF 38 / printed p.30** found another source-level correction: scene 31 prints the song title **`பாண்டியன் என் சொல்லை`**, not the earlier transcription `பாண்டியன் என் செல்வம்`. Both the canonical Part 03 transcription and scene-31 derivative were corrected from the scan; `notes/post-fidelity-corrections.md` records the change. Page counts/status remain **104 verified / 0 draft / 0 review**.

## Source discipline

The supplied scan is the controlling source. Do not modernize spelling or punctuation, normalize speaker labels, repair scene headings from film knowledge, fill unreadable text from subtitles/audio/web copies, or infer lyric authorship from proximity.

The dialogue index follows the same discipline: only explicitly speaker-labelled utterances become dialogue records. Speaker labels remain exact; standalone narrative/stage directions and unlabelled material are not silently assigned to a character. Scenes **10, 11, 25, 26, 43 and 54** therefore correctly have zero dialogue records.

The completed dialogue layer contains **eight** verified cross-page utterances: `tirumbippaar-s001-d006`, `tirumbippaar-s041-d034`, `tirumbippaar-s045-d015`, `tirumbippaar-s063-d003`, `tirumbippaar-s072-d001`, `tirumbippaar-s076-d012`, `tirumbippaar-s080-d022`, and `tirumbippaar-s080-d028`.

Unlabelled structures remain in the canonical/scene layer rather than being silently converted to dialogue. Examples include the scene-29 `கோஷம்`, scene-31 song-performance material, scene-43 `கலப்படம்` performance description, scene-54 newspaper report, scene-83 letter, scene-84 unlabelled advertisement reading, scene-85 address card, scene-91 `பத்திரிகை News`, and the final `வணக்கம்.` in scene 93.

The character layer likewise does not rewrite source labels. `குணமணி` and `குண்டுமணி` are source-supported variants mapped to one household-helper character; scene-79 `அவன் குரல்` maps to Pandiyan from the scene context. By contrast, the reused exact label `குரல்` remains a role category because it represents different contextual voices in scenes 38, 67 and 72. Generic `பையன்`, worker labels, police labels and `Echo` are also retained as role/collective categories rather than being falsely turned into named individuals.

The song layer follows an equally strict gate. Visual inspection of PDF **1–8** found no `பாடல்கள்` heading, lyricist list or item-level song credit; the cover's `கதை - வசனம்` credit is not treated as lyric authorship. Of eight source-visible song/performance occurrences, five remain unresolved because the booklet supplies no safe title/lyric evidence. Separately documented item-level soundtrack metadata is used only where the booklet itself names the song: **`பாண்டியன் என் சொல்லை` → பாரதிதாசன்** and **`கலப்படம்` → கண்ணதாசன்**. External metadata never supplies or repairs canonical lyrics.

No Tamil song-lyric derivative is created from absent text. Scene 31 prints only a named performance reference; scenes 42–43 print/name only `கலப்படம்` material rather than a complete lyric body. The canonical scene files therefore remain the complete source-supported Tamil record for these occurrences.

The English layer follows the same immutability rule. Scenes **1–10** now contain **124 verified source-linked units**: **97 dialogue, 25 stage directions and 2 song-references**. Scene 6 translates only the fact that Bama's song has ended and supplies no absent title or lyrics. Scene 10 correctly has no dialogue record and is represented entirely by one scene-linked visual direction showing Bama's tears becoming a waterfall and river. Scene 5's unlabelled coffee request remains source-linked dialogue with a null speaker and no invented dialogue-record ID. The only cross-page English unit so far remains the scene-1 Poomaal utterance across PDF 9→10.

## Exact next activity

Translate and verify **scenes 11–15**. Preserve canonical order and exact Tamil speaker labels as metadata, link every labelled utterance to its immutable dialogue record, retain stage/performance and other unlabelled material without invented speakers, mirror genuine cross-page provenance, and keep absent song lyrics absent.
