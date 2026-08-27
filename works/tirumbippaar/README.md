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

## Active corrected-transcription reconciliation

The earlier full-volume **104 verified / 0 review** state is now historical only. On 2026-08-26 the user supplied a corrected `thirumbipaar.md` covering all 104 screenplay pages and identified systematic OCR / old-Tamil-glyph loss in the earlier transcription, including forms such as `பூமால்` instead of `பூமாலை` and `இல்ல` instead of `இல்லை`.

For the active pass:

- `thirumbipaar.md` is the **primary correction baseline**;
- the rendered PDF remains the **final visual authority** for doubtful readings, extraction artefacts, punctuation, headings and page structure;
- source spelling, punctuation, labels, old forms and physical page boundaries are not silently modernized;
- earlier `verified` status is not accepted as proof that a Tamil reading is correct.

Current correction boundaries:

- canonical Tamil corrected/reconciled: **PDF 9–91 / printed pp.1–83 — Parts 01–04**;
- scene/dialogue corrected/reconciled: **through scene 48**, including scene 48's genuine PDF-64 / printed-p.56 continuation;
- next derivative range: **scenes 49–75** against corrected canonical Part 04;
- scene 76 begins on printed p.83 and crosses into Part 05;
- Part 05 canonical range **PDF 92–112 / printed pp.84–104** remains pending.

`notes/md-reconciliation-audit.md` is the authoritative progress ledger for this correction pass. `notes/post-fidelity-corrections.md` records concrete source corrections discovered after the earlier fidelity audit.

## Current archival status

- source intake: **complete**
- structural mapping / scene-number pass: **complete — 93 scenes, 1–93**
- scene-heading / structural-label audit: **93/93 dispositioned**
- first-pass canonical Tamil transcription: **historically complete**
- corrected canonical reconciliation: **in progress — Parts 01–04 complete**
- corrected scene/dialogue propagation: **in progress — through scene 48**
- immutable labelled-dialogue records: **1,042** after recovery of two omitted scene-41 utterances
- scene 41 dialogue count: **38**
- scene 43: **legitimate zero-dialogue scene**; its `கலப்படம்` non-dialogue/performance material remains in scene 43
- character/entity layer: **known stale during correction pass**
- English translation / reader / EPUB layers: **historically complete, but not currently claimed source-synchronized**
- song authorship mapping: **historically complete — 8 occurrences dispositioned; 3 verified / 5 unresolved**

Canonical Tamil transcription is indexed at `transcription/full-text.md` and stored in five source-order files under `transcription/parts/`. Scene derivatives are under `scenes/`; labelled dialogue records are under `dialogues/records/` with the work-level index at `dialogues/index.json`.

## Important reconciliation findings

Scene 41 originally contained 36 dialogue records. Fresh comparison against the corrected source proved that two explicitly labelled utterances had been omitted. They were added without renumbering any existing IDs:

- `tirumbippaar-s041-d037` — `பூமாலை`
- `tirumbippaar-s041-d038` — `பரந்தாமன்`

Existing `tirumbippaar-s041-d034` retains its stable ID and preserves its genuine PDF 56→57 cross-page split around `அன்பைக் கேட்-` / `காமல் ஐஸ்வரியத்தைக் கேட்கும்...`.

The Part-03 derivative pass also corrected the accidental structural drift that had placed scene-43 material inside scene 42. Scenes 42 and 43 are separate source-supported segments; scene 43 is zero-dialogue but contains the source's `கலப்படம்` performance material.

Part 04 has now been rebuilt canonically from the corrected witness for PDF 64–91 / printed pp.56–83. The scan was used to adjudicate clear extraction artefacts, including the truncated page-57 `குயில்` passage and genuine cross-page word boundaries such as scene 63's `கொஞ்சங்-` / `கொஞ்சமா` split.

## Source discipline

Do not modernize spelling or punctuation, normalize speaker labels, repair scene headings from film knowledge, fill unreadable text from subtitles/audio/web copies, or infer speakers for unlabelled source speech.

Only explicitly speaker-labelled utterances become immutable dialogue records. Standalone narrative/stage directions, written text and unlabelled speech remain outside that layer. Scenes **10, 11, 25, 26, 43 and 54** therefore remain zero-dialogue scenes.

The current dialogue index contains **1,042** labelled records. Existing IDs remain stable. New IDs are created only when the source proves that an explicitly labelled utterance was genuinely omitted, as happened in scene 41.

Exact speaker labels are preserved as printed. Character/entity resolution is a separate layer and is intentionally not regenerated until the corrected dialogue label set reaches a stable full-work boundary.

## Historical derivative status

Before this correction pass, the English layer had been recorded as complete across 93 scenes / 1,321 units, and reader/export plus deterministic EPUB packaging had passed their earlier QA gates. Those historical outputs remain in the repository, but **their previous verification status is not a current claim that they agree with the newly corrected Tamil source text**.

The same caution applies to the existing character/entity mappings. They will be regenerated only after the Tamil dialogue correction pass stabilizes.

## Exact next activity

Propagate corrected canonical **Part 04 / PDF 64–91 / printed pp.56–83** through scene and dialogue derivatives for **scenes 49–75**, preserving stable dialogue IDs, exact source labels and genuine page provenance. After that, reconcile canonical **Part 05 / PDF 92–112 / printed pp.84–104** and continue its derivative propagation.
