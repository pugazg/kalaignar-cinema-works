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

The earlier full-volume **104 verified / 0 review** state is historical only. On 2026-08-26 the user supplied a corrected `thirumbipaar.md` covering all 104 screenplay pages and identified systematic OCR / old-Tamil-glyph loss in the earlier transcription, including forms such as `பூமால்` instead of `பூமாலை` and `இல்ல` instead of `இல்லை`.

For this pass:

- `thirumbipaar.md` is the **primary correction baseline**;
- the rendered PDF is the **final visual authority** for doubtful readings, extraction artefacts, punctuation, headings, page structure and material visibly omitted from the Markdown;
- source spelling, punctuation, labels, old forms and physical page boundaries are not silently modernized;
- earlier `verified` status is not accepted as proof that a Tamil reading is correct.

Current correction boundaries:

- corrected canonical coverage: **PDF 9–112 / printed pp.1–104 — Parts 01–05**;
- corrected scene/dialogue propagation: **through scene 93 / end of work**;
- immutable labelled-dialogue total: **1,042**;
- scene 41 dialogue count: **38** after recovery of two omitted labelled source utterances;
- all existing dialogue IDs remain stable; only the two source-proven scene-41 omissions were added;
- one final scan-visible **non-dialogue** departure parenthetical on PDF 112 is retained in `scenes/scene-93.md` but still needs propagation into canonical `transcription/parts/part-05-pdf-92-112.md` before the canonical source layer is declared scan-closed.

`notes/md-reconciliation-audit.md` is the authoritative progress ledger for this correction pass. `notes/post-fidelity-corrections.md` records concrete source corrections discovered after the earlier fidelity audit.

## Current archival status

- source intake: **complete**
- structural mapping / scene-number pass: **complete — 93 scenes, 1–93**
- scene-heading / structural-label audit: **93/93 dispositioned**
- corrected canonical text coverage: **complete across Parts 01–05, with one final PDF-112 non-dialogue line still pending canonical insertion**
- corrected scene/dialogue propagation: **complete through scene 93 / end of work**
- immutable labelled-dialogue records: **1,042**
- scene 41 dialogue count: **38**
- scene 43: **legitimate zero-dialogue scene**; its `கலப்படம்` non-dialogue/performance material remains in scene 43
- character/entity layer: **known stale; eligible for regeneration only after canonical source closure**
- English translation / reader / EPUB layers: **historically complete, but not currently claimed source-synchronized**
- song authorship mapping: **historically complete — 8 occurrences dispositioned; 3 verified / 5 unresolved**

Canonical Tamil transcription is indexed at `transcription/full-text.md` and stored in five source-order files under `transcription/parts/`. Scene derivatives are under `scenes/`; labelled dialogue records are under `dialogues/records/` with the work-level index at `dialogues/index.json`.

## Important reconciliation findings

Scene 41 originally contained 36 dialogue records. Fresh comparison against the corrected source proved that two explicitly labelled utterances had been omitted. They were added without renumbering any existing IDs:

- `tirumbippaar-s041-d037` — `பூமாலை`
- `tirumbippaar-s041-d038` — `பரந்தாமன்`

Existing `tirumbippaar-s041-d034` retains its stable ID and preserves its genuine PDF 56→57 cross-page split around `அன்பைக் கேட்-` / `காமல் ஐஸ்வரியத்தைக் கேட்கும்...`.

The Part-03 derivative pass corrected the accidental structural drift that had placed scene-43 material inside scene 42. Scenes 42 and 43 are separate source-supported segments; scene 43 is zero-dialogue but contains the source's `கலப்படம்` performance material.

Part 04 / PDF 64–91 is closed at canonical and scene/dialogue layers. Scan adjudications include the full scene-49 `குயில் பாடுதுங்கிறான்` reading, scene 69's `12½` clock, and scene 72's printed Paranthaman / `(திரையில் குரல்)` / `குரல்:` performance order.

Part 05 / PDF 92–112 has been reconciled through scene 93. Representative repairs include exact `பூமாலை`, `புண்யகோடி` and `உஷா` forms; scene 87's explicitly labelled `குண்டுமணி : ...`; scene 88's `தந்தி கொடுத்திருக்கிறாள்`; scene 90's corrected Bama/Paranthaman/Poomalai ending sequence; scene 91's source order around `பாண்டியன்!` and `(பாண்டியன் பிரவேசம்)`; scene 92's newspaper lead-in; and scene 93's corrected closing speech through `வணக்கம்.`.

Direct inspection of PDF 112 also shows a final non-dialogue departure parenthetical omitted from the corrected Markdown. The scene derivative preserves it; canonical Part 05 still needs that one source-scan insertion.

## Source discipline

Do not modernize spelling or punctuation, normalize speaker labels, repair scene headings from film knowledge, fill unreadable text from subtitles/audio/web copies, or infer speakers for unlabelled source speech.

Only explicitly speaker-labelled utterances become immutable dialogue records. Standalone narrative/stage directions, written text and unlabelled speech remain outside that layer. Scenes **10, 11, 25, 26, 43 and 54** remain zero-dialogue scenes.

The current dialogue index contains **1,042** labelled records and **93/93 completed scenes**. Existing IDs remain stable. New IDs are created only when the source proves that an explicitly labelled utterance was genuinely omitted, as happened in scene 41.

Exact speaker labels are preserved at the dialogue layer. Character/entity resolution is separate and remains known-stale until the source layer is closed.

## Historical derivative status

Before this correction pass, the English layer had been recorded as complete across 93 scenes / 1,321 units, and reader/export plus deterministic EPUB packaging had passed their earlier QA gates. Those outputs remain in the repository, but **their previous verification status is not a current claim that they agree with the newly corrected Tamil source text**.

The same caution applies to existing character/entity mappings.

## Exact next activity

1. Propagate the scan-visible final PDF-112 departure parenthetical into canonical `part-05-pdf-92-112.md` and close the canonical source layer.
2. Reconcile README/metadata/checkpoints to that closed source state.
3. Regenerate/reconcile the character/entity layer from the stable 1,042-record dialogue corpus.
4. Revalidate English / reader / EPUB derivatives where the corrected Tamil changes wording, meaning or source linkage.
