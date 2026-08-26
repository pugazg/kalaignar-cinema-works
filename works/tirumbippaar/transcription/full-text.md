# திரும்பிப்பார்! — canonical Tamil transcription

**Status:** `reconciliation-in-progress` — the previous full-volume `verified` state has been reopened after systematic OCR / old-Tamil-glyph errors were identified and a corrected full-volume Markdown transcription was supplied by the user.

Source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`  
SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

Correction witness: user-supplied `thirumbipaar.md`. It is the primary correction baseline for this pass; the rendered scan remains final authority where a reading is doubtful or conflicts with the printed page.

The canonical page-order transcription is split into five archival batches:

1. [`parts/part-01-pdf-9-13.md`](parts/part-01-pdf-9-13.md) — PDF 9–13 / printed pp.1–5 — **corrected-Markdown reconciled**.
2. [`parts/part-02-pdf-14-35.md`](parts/part-02-pdf-14-35.md) — PDF 14–35 / printed pp.6–27 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized through scene 29 / PDF 35**.
3. [`parts/part-03-pdf-36-63.md`](parts/part-03-pdf-36-63.md) — PDF 36–63 / printed pp.28–55 — **corrected-Markdown reconciled at canonical layer; derivative synchronization pending**.
4. [`parts/part-04-pdf-64-91.md`](parts/part-04-pdf-64-91.md) — PDF 64–91 / printed pp.56–83 — **pending this reconciliation pass**.
5. [`parts/part-05-pdf-92-112.md`](parts/part-05-pdf-92-112.md) — PDF 92–112 / printed pp.84–104 — **pending this reconciliation pass**.

## Current state

- Main-text range: PDF **9–112 / printed pp.1–104**.
- Corrected Markdown coverage: **104/104 Play Pages**.
- Canonical parts reconciled from corrected Markdown: **Parts 01–03 / PDF 9–63 / printed pp.1–55**.
- Scene/dialogue derivative reconciliation completed through: **scene 29's PDF 35 / printed p.27 portion**.
- Scene 29's PDF **36 / printed p.28** continuation and scenes 30–48 now have corrected canonical Part-03 text available and are the next derivative reconciliation range.
- Parts 04–05 remain pending at the canonical layer.
- Character/entity, English translation, reader/export and EPUB layers must be revalidated after the source-layer pass; their previous complete status is not treated as proof of textual synchronization during this correction cycle.

The exact correction history and current synchronization boundary are recorded in [`../notes/md-reconciliation-audit.md`](../notes/md-reconciliation-audit.md) and [`../notes/post-fidelity-corrections.md`](../notes/post-fidelity-corrections.md).

The former `104 verified / 0 review` statement remains historical audit status only and is **superseded for textual correctness until this reconciliation pass closes**.
