# திரும்பிப்பார்! — scene derivatives

This directory contains scene-level derivatives constructed only from the verified canonical Tamil transcription of `TVA_BOK_0014652_திரும்பிப்பார்.pdf`.

## Scene index

[`index.json`](index.json) records all **93** source-observed scene headings, consecutively numbered **1–93**, with each scene's starting PDF page, printed page, canonical transcription part, and scene-text filename.

The index is derived from the completed canonical transcription and the verified structural audit in [`../notes/scene-heading-audit.md`](../notes/scene-heading-audit.md). No film audio, subtitles, web text, later edition, or Parasakthi wording is used as a text source.

## Source policy

- The verified canonical Tamil under [`../transcription/`](../transcription/) is the controlling text for scene extraction.
- Scene text is copied without modernization, correction, normalization, paraphrase, or reconstruction.
- Source page anchors are retained inside scene files so page-level provenance remains inspectable.
- A scene begins at its printed scene heading and ends immediately before the next numbered scene heading.
- Material between numbered scenes stays with the preceding scene unless the canonical structure establishes it as a separate non-scene block.
- Cross-part scenes are assembled in source order without duplicating or dropping text at the part boundary.
- Source-visible scene-marker irregularities remain in scene text; `index.json` uses the numeric scene identity only for navigation.
- Parasakthi is a schema/workflow reference only and is never a text source for this work.

## Current status

- scene index: **complete — 93/93 records**
- numbering gaps/repeats: **none**
- scene-text files: **complete — 93/93 files**
- completed scene range: **1–93**
- next structured derivative: **dialogue index**

## Cross-part scenes

Four scenes cross canonical transcription-part boundaries and are assembled explicitly in source order with page anchors preserved:

- scene 5: `part-01` → `part-02` — PDF 13–15 / printed pp.5–7
- scene 29: `part-02` → `part-03` — PDF 34–36 / printed pp.26–28
- scene 48: `part-03` → `part-04` — PDF 63–64 / printed pp.55–56
- scene 76: `part-04` → `part-05` — PDF 91–92 / printed pp.83–84

## Derivative repair log

During dialogue-index batch 5 (scenes 41–50), direct comparison against the already-verified Part 03 canonical transcription exposed a prior drift in [`scene-41.md`](scene-41.md). The scene derivative had substituted the opening Pandiyan/Paranthaman exchange after PDF 53 and omitted the PDF 54 page anchor. It was repaired from the verified canonical transcription before dialogue extraction.

The repair restored the canonical `பாண்டியன்: கேளேன் தருகிறேன் ...` line, the PDF 54 exchange beginning `பரந்தாமன்: (கேலியாக சிரித்து விட்டு) சரியான திருடன்பா!...`, and the PDF 54 page anchor. No canonical Tamil transcription was altered.

The final derivative, [`scene-93.md`](scene-93.md), preserves the source ending on PDF 112 / printed p.104, including `வணக்கம்.` and the final star.
