# திரும்பிப்பார்! — canonical Tamil transcription

**Status:** `reconciliation-in-progress` — the previous full-volume `verified` state has been reopened after systematic OCR / old-Tamil-glyph errors were identified and a corrected full-volume Markdown transcription was supplied by the user.

Source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`  
SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

Correction witness: user-supplied `thirumbipaar.md`. It is the primary correction baseline for this pass; the rendered scan remains final authority where a reading is doubtful or conflicts with the printed page.

The canonical page-order transcription is split into five archival batches:

1. [`parts/part-01-pdf-9-13.md`](parts/part-01-pdf-9-13.md) — PDF 9–13 / printed pp.1–5 — **corrected-Markdown reconciled**.
2. [`parts/part-02-pdf-14-35.md`](parts/part-02-pdf-14-35.md) — PDF 14–35 / printed pp.6–27 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized**.
3. [`parts/part-03-pdf-36-63.md`](parts/part-03-pdf-36-63.md) — PDF 36–63 / printed pp.28–55 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized through scene 48**.
4. [`parts/part-04-pdf-64-91.md`](parts/part-04-pdf-64-91.md) — PDF 64–91 / printed pp.56–83 — **pending corrected-Markdown canonical reconciliation**.
5. [`parts/part-05-pdf-92-112.md`](parts/part-05-pdf-92-112.md) — PDF 92–112 / printed pp.84–104 — **pending this reconciliation pass**.

## Current state

- Main-text range: PDF **9–112 / printed pp.1–104**.
- Corrected Markdown coverage: **104/104 Play Pages**.
- Canonical parts reconciled from corrected Markdown: **Parts 01–03 / PDF 9–63 / printed pp.1–55**.
- Scene/dialogue derivative reconciliation completed through: **scene 48**, including its genuine cross-part continuation on **PDF 64 / printed p.56**.
- Scene 41 now contains **38** immutable labelled-dialogue records after recovering two explicitly labelled source utterances; whole-work dialogue count is **1,042**.
- Scene 43 remains a source-supported **zero-dialogue** scene and retains its `கலப்படம்` non-dialogue/performance material in `scene-43.md`.
- Part 04 remains pending at the canonical layer. Scene 48's PDF-64 continuation was reconciled only because it completes a scene that begins in Part 03; it does not advance the canonical Part-04 boundary.
- Parts 04–05 remain pending at the canonical layer.
- Character/entity, English translation, reader/export and EPUB layers must be revalidated after the source-layer pass; their previous complete status is not treated as proof of textual synchronization during this correction cycle.

## Active boundaries

- **Canonical corrected reconciliation:** PDF **9–63** / printed pp. **1–55**.
- **Scene/dialogue corrected reconciliation:** through **scene 48**, including PDF **64** / printed p. **56** continuation.
- **Next canonical range:** Part 04 — PDF **64–91** / printed pp. **56–83**.

The exact correction history and current synchronization boundary are recorded in [`../notes/md-reconciliation-audit.md`](../notes/md-reconciliation-audit.md) and [`../notes/post-fidelity-corrections.md`](../notes/post-fidelity-corrections.md).

The former `104 verified / 0 review` statement remains historical audit status only and is **superseded for textual correctness until this reconciliation pass closes**.
