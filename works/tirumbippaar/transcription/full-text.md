# திரும்பிப்பார்! — canonical Tamil transcription

**Status:** `reconciliation-in-progress` — corrected Tamil and scene/dialogue reconciliation now covers the full screenplay; one scan-visible final non-dialogue line on PDF 112 still needs propagation into canonical Part 05 before the source layer is declared scan-closed.

Source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`  
SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

Correction witness: user-supplied `thirumbipaar.md`. It is the primary correction baseline for this pass; the rendered scan remains final authority where a reading is doubtful, conflicts with the printed page, or visibly omits printed material.

The canonical page-order transcription is split into five archival batches:

1. [`parts/part-01-pdf-9-13.md`](parts/part-01-pdf-9-13.md) — PDF 9–13 / printed pp.1–5 — **corrected-Markdown reconciled**.
2. [`parts/part-02-pdf-14-35.md`](parts/part-02-pdf-14-35.md) — PDF 14–35 / printed pp.6–27 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized**.
3. [`parts/part-03-pdf-36-63.md`](parts/part-03-pdf-36-63.md) — PDF 36–63 / printed pp.28–55 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized**.
4. [`parts/part-04-pdf-64-91.md`](parts/part-04-pdf-64-91.md) — PDF 64–91 / printed pp.56–83 — **corrected-Markdown reconciled; scan micro-cleanup complete; scene/dialogue derivatives synchronized through scene 75**.
5. [`parts/part-05-pdf-92-112.md`](parts/part-05-pdf-92-112.md) — PDF 92–112 / printed pp.84–104 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized through scene 93; one final PDF-112 non-dialogue parenthetical still pending canonical insertion**.

## Current state

- Main-text range: PDF **9–112 / printed pp.1–104**.
- Corrected Markdown coverage: **104/104 Play Pages**.
- Corrected canonical text coverage: **Parts 01–05 / full main-text range**.
- Scene/dialogue derivative reconciliation: **complete through scene 93 / end of work**.
- Scene 41 contains **38** immutable labelled-dialogue records after recovering two explicitly labelled source utterances.
- Whole-work immutable labelled-dialogue count: **1,042**.
- Existing dialogue IDs were preserved; only `tirumbippaar-s041-d037` and `tirumbippaar-s041-d038` were added because the source proved those labelled utterances had been omitted.
- Scene 43 remains a source-supported **zero-dialogue** scene and retains its `கலப்படம்` non-dialogue/performance material.
- Part 04 scan adjudications include the full `குயில் பாடுதுங்கிறான்` reading, the `12½` clock, and scene 72's printed `குரல்` performance order.
- Part 05 scene/dialogue propagation includes scenes 76–93, including scene 76's genuine PDF 91→92 continuation.
- PDF 112 visibly contains a final non-dialogue departure parenthetical before `வணக்கம்.` which is retained in `scenes/scene-93.md` but is still absent from canonical `part-05-pdf-92-112.md`.

## Active boundaries

- **Corrected canonical coverage:** PDF **9–112** / printed pp. **1–104**.
- **Canonical scan-closed boundary:** all source text and dialogue are reconciled; one final PDF-112 non-dialogue parenthetical remains to be copied into canonical Part 05.
- **Scene/dialogue corrected reconciliation:** **scene 93 / end of work**.
- **Next source-layer activity:** propagate that final PDF-112 parenthetical into Part 05, then close the canonical source layer.
- **Next downstream activity after source closure:** rebuild/reconcile character/entity mappings from the stable corrected dialogue corpus.

Character/entity mappings, English translations, reader/export derivatives and EPUB outputs remain **known-stale** until explicitly regenerated or revalidated. Their previous complete/verified state is historical and is not a current synchronization claim.

The exact correction history is recorded in [`../notes/md-reconciliation-audit.md`](../notes/md-reconciliation-audit.md) and [`../notes/post-fidelity-corrections.md`](../notes/post-fidelity-corrections.md).

The former `104 verified / 0 review` statement remains historical audit status only and is **superseded for textual correctness until this reconciliation pass and downstream synchronization close**.
