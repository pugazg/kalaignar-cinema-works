# திரும்பிப்பார்! — canonical Tamil transcription

**Status:** `verified-reconciled` — corrected canonical Tamil and scene/dialogue reconciliation are complete across the full screenplay, including final scan adjudication on PDF 112. Downstream English reader and EPUB publication derivatives have also been regenerated and independently QA-verified against the reconciled source-linked English layer.

Source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`  
SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

Correction witness: user-supplied `thirumbipaar.md`. It is the primary correction baseline for this pass; the rendered scan remains final authority where a reading is doubtful, conflicts with the printed page, or visibly omits printed material.

The canonical page-order transcription is split into five archival batches:

1. [`parts/part-01-pdf-9-13.md`](parts/part-01-pdf-9-13.md) — PDF 9–13 / printed pp.1–5 — **corrected-Markdown reconciled**.
2. [`parts/part-02-pdf-14-35.md`](parts/part-02-pdf-14-35.md) — PDF 14–35 / printed pp.6–27 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized**.
3. [`parts/part-03-pdf-36-63.md`](parts/part-03-pdf-36-63.md) — PDF 36–63 / printed pp.28–55 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized**.
4. [`parts/part-04-pdf-64-91.md`](parts/part-04-pdf-64-91.md) — PDF 64–91 / printed pp.56–83 — **corrected-Markdown reconciled; scan micro-cleanup and final three-string canonical synchronization complete**.
5. [`parts/part-05-pdf-92-112.md`](parts/part-05-pdf-92-112.md) — PDF 92–112 / printed pp.84–104 — **corrected-Markdown reconciled; scene/dialogue derivatives synchronized through scene 93; final PDF-112 non-dialogue departure direction restored from the scan**.

## Current state

- Main-text range: PDF **9–112 / printed pp.1–104**.
- Corrected Markdown coverage: **104/104 Play Pages**.
- Corrected canonical reconciliation: **Parts 01–05 / full main-text range — scan-closed**.
- Scene/dialogue derivative reconciliation: **complete through scene 93 / end of work**.
- Scene 41 contains **38** immutable labelled-dialogue records after recovering two explicitly labelled source utterances.
- Whole-work immutable labelled-dialogue count: **1,042**.
- Existing dialogue IDs were preserved; only `tirumbippaar-s041-d037` and `tirumbippaar-s041-d038` were added because the source proved those labelled utterances had been omitted.
- Scene 43 remains a source-supported **zero-dialogue** scene and retains its `கலப்படம்` non-dialogue/performance material.
- Part 04 scan adjudications include the full `குயில் பாடுதுங்கிறான்` reading, the `12½` clock, and scene 72's printed `குரல்` performance order.
- The final Part04 closure also removes the stray `ஈ.` after `இதெல்லாம் சினிமா.`, corrects `ஏல்லாம்` to `எல்லாம்`, and restores `[புண்யகோடி கதவைத் தட்டல்]` in agreement with the reconciled derivatives.
- Part 05 scene/dialogue propagation includes scenes 76–93, including scene 76's genuine PDF 91→92 continuation.
- PDF 112's scan-visible final non-dialogue departure direction is present in both `scenes/scene-93.md` and canonical `parts/part-05-pdf-92-112.md` immediately before `வணக்கம்.`.
- Character/entity regeneration is complete against the corrected dialogue corpus: **45 exact source labels / 39 verified entities**, with no review or unresolved mappings.

## Closed downstream checkpoint

The source-linked English layer is complete at **93/93 scenes / 1,330 verified units / 1,042 of 1,042 labelled dialogue links**. Its composition is **1,049 dialogue-kind / 262 stage-direction / 7 song-reference / 2 chant / 10 written-text / 0 full-song**.

The deterministic publication workflow subsequently passed both release gates:

- reader Markdown/HTML/JSON QA: **PASS — 93 scenes / 1,330 units / 1,042 links**;
- EPUB 3 QA: **PASS — 93 scenes / 1,330 units / 99 ZIP members / 370,218 bytes**;
- EPUB SHA-256: `88bf02ac345926d02a3b6e25ea262c3f6aafe59383a620b2bb160cdd3fabbb31`.

Generated publication commit: **`55bb983eb2959190f025250099793ab5efce2b9f`**.

## Active boundaries

- **Corrected canonical coverage:** PDF **9–112** / printed pp. **1–104**.
- **Canonical source layer:** **scan-closed**.
- **Scene/dialogue corrected reconciliation:** **scene 93 / end of work**.
- **Immutable dialogue total:** **1,042**.
- **Character/entity layer:** **complete-verified-reconciled — 45 labels / 39 entities**.
- **English translation:** **complete-verified — 1,330 units / 1,042 linked labelled records**.
- **Reader/export/EPUB derivatives:** **complete-verified — QA PASS**.

The exact correction and publication history is recorded in [`../notes/md-reconciliation-audit.md`](../notes/md-reconciliation-audit.md). Generated publication QA is recorded in [`../editions/en/QA_REPORT.md`](../editions/en/QA_REPORT.md) and [`../editions/en/EPUB_QA_REPORT.md`](../editions/en/EPUB_QA_REPORT.md).

The former `104 verified / 0 review` first-pass state and the historical `1,321 units / 1,040 dialogue links` English build are retained only as history. The corrected source and current deterministic publication package supersede them.
