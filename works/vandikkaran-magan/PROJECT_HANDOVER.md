# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**. Source pixels control canonical Tamil; do not substitute web text, film audio, OCR, later editions or memory.

## Closed source authority

- PDF 4–5 — `கலைஞரின் முன்னுரை`;
- PDF 6–87 — screenplay/dialogue, printed pp.5–86;
- PDF 88–89 — film credits;
- PDF 90 — back cover;
- canonical source pages: **87/87 — PDF 4–90**;
- visual verification: **87/87 COMPLETE**;
- historical-glyph verification: **87/87 COMPLETE / 0 holds**;
- final full visual verification: **87/87 PASS / 0 final corrections**;
- open uncertainty markers: **0**.

## Structural / scene authority

The corrected source-visible scene inventory is **72/72**, after derivative QA exposed the previously omitted but already canonical PDF 10 heading `காட்சி — 4 எ.` (`4-எ`). The sequence spans base numbers 1–56, **17 suffix insertions**, and the source-combined `45-46` heading. `notes/scene-heading-audit.md` is the current mapping record.

Scene-text derivatives are **72/72 COMPLETE-VERIFIED** in `scenes/`. Boundary ownership QA is **PASS**:

- screenplay coverage: **82/82 pages — PDF 6–87**;
- gaps: **0**;
- overlaps: **0**;
- duplicate source ownership: **0**;
- joined scene-span SHA-256 equals canonical scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`.

PDF 4–5 and PDF 88–90 are deliberately outside the scene layer. No canonical Tamil was rewritten by scene construction.

## Derivative gate state

- scene-text derivatives: **COMPLETE-VERIFIED — 72/72 / QA PASS**;
- dialogue index: **READY-NEXT**;
- character/entity index: **BLOCKED pending dialogue closure**;
- song/performance authorship gate: **BLOCKED**;
- English translation: **BLOCKED**;
- reader/export / Reading Room: **BLOCKED**.

## Exact next activity

> **Build the immutable dialogue index from the 72 complete-verified scene derivatives. Only explicitly speaker-labelled source utterances become dialogue records. Preserve exact Tamil `speaker_label`, exact dialogue text, source scene ID, PDF/printed-page provenance, and cross-page ownership; keep one labelled utterance crossing a page as one record; leave unlabelled speech unassigned; allow legitimate zero-dialogue scenes; validate that each extracted dialogue span is owned exactly once with no invented speakers or normalized labels; commit/push the dialogue layer; then synchronize all active status mirrors before opening character/entity indexing.**
