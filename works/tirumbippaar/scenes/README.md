# திரும்பிப்பார்! — scene derivatives

This directory contains scene-level derivatives constructed only from the verified canonical Tamil transcription of `TVA_BOK_0014652_திரும்பிப்பார்.pdf`.

## Scene index

[`index.json`](index.json) records all **93** source-observed scene headings, consecutively numbered **1–93**, with each scene's starting PDF page, printed page, canonical transcription part, and intended scene-text filename.

The index is derived from the completed canonical transcription and the verified structural audit in [`../notes/scene-heading-audit.md`](../notes/scene-heading-audit.md). No film audio, subtitles, web text, later edition, or Parasakthi wording is used as a text source.

## Source policy

- The verified canonical Tamil under [`../transcription/`](../transcription/) is the controlling text for scene extraction.
- Scene text must be copied without modernization, correction, normalization, paraphrase, or reconstruction.
- Source page anchors are retained inside scene files so page-level provenance remains inspectable.
- A scene begins at its printed scene heading and ends immediately before the next numbered scene heading.
- Material between numbered scenes stays with the preceding scene unless the canonical structure establishes it as a separate non-scene block.
- Cross-part scenes must be assembled in source order without duplicating or dropping text at the part boundary.
- Source-visible scene-marker irregularities remain in scene text; `index.json` uses the numeric scene identity only for navigation.
- Parasakthi is a schema/workflow reference only and is never a text source for this work.

## Current status

- scene index: **complete — 93/93 records**
- numbering gaps/repeats: **none**
- scene-text files: **not started**
- next extraction batch: **scenes 1–10**

Scene 5 crosses the `part-01` → `part-02` transcription boundary: it starts on PDF 13 / printed p.5 and continues on PDF 14 / printed p.6 before scene 6 begins on PDF 15 / printed p.7. That boundary must be handled explicitly during the first scene-text batch.
