# Raja Rani — Correction 005 downstream reconciliation

Status: **in progress**

This note tracks downstream reconciliation after the late manual source-correction campaign recorded as Correction 005. Canonical Tamil page files remain authoritative. Translation expansion stays paused until this gate is closed.

## Invariants

- Controlling screenplay span: PDF 10–79; PDF 80 is the blank back cover.
- Review/source-limited pages remain PDF 27, 48, 57 and 74.
- Blocked scenes are not reconstructed from review-limited pages.
- Existing dialogue IDs, scene IDs and page provenance remain stable.
- Corrected exact speaker labels propagate without normalization.
- Existing English records are reconciled only where their Tamil source changed; no new translation scenes are added during this gate.

## Canonical-to-scene / dialogue propagation closed

The source-order Correction 005 propagation pass is complete for every eligible scene through the end of the screenplay. Existing scene and dialogue IDs/provenance were retained.

- scenes 001–007 / dialogue shards 001–007 — reconciled through PDF 21.
- scene 009 / dialogue shard 009 — reconciled across PDFs 21–25.
- scene 015 / dialogue shard 015 — reconciled across PDFs 28–30.
- scene 016 / dialogue shard 016.
- scene 017 / dialogue shard 017 — reconciled across PDFs 31–33, including the exact source speaker-label occurrence `தர்யம்` without normalization.
- scene 018 / dialogue shard 018 — reconciled across PDFs 33–35.
- scene 021 / dialogue shard 021 — reconciled across PDFs 35–38, including its PDF 37→38 cross-page record/page segments.
- scene 023 / dialogue shard 023 — reconciled across PDFs 38–40.
- scene 024 / dialogue shard 024 — corrected `அகல்யா நாடக ஒத்திகை` material across PDFs 40–42.
- scene 025 / dialogue shard 025 — PDFs 42–43.
- scene 026 / dialogue shard 026 — PDF 43 `முத்திப்போச்சா`.
- scene 028 / dialogue shard 028 — PDFs 44–46.
- scene 034 / dialogue shard 034 — PDF 52 speaker-label correction; stable `raja-rani-s034-d060` retained.
- scene 040 / dialogue shard 040 — PDFs 58–59, including the cross-page record and page-segment correction.
- scene 041 / dialogue shard 041 — PDFs 59–61.
- scene 044 / dialogue shard 044 — PDFs 61–63, including the cross-page final record and page segments.
- scene 045 / dialogue shard 045 — PDFs 63–64.
- scene 046 / dialogue shard 046 — PDFs 64–65, including its cross-page record and page segments.
- scenes 048–050 / dialogue shards 048–050 — reconciled across the PDF 65–67 frontier.
- scene 051 / dialogue shard 051 — reconciled across PDFs 67–70, including its PDF 69→70 cross-page record/page segments.
- scene 052 / dialogue shard 052 — corrected Socrates material across PDFs 70–73.
- scene 056 — checked against corrected PDF 77 and requires no derivative text change.
- scenes 057–058 / dialogue shards 057–058 — final manual corrections across PDFs 77–79.

## Checked / no derivative text change required

- scenes 008, 010, 014, 027, 029–031, 035–038, 043, 047 and 056.
- scene 032 had the single stage-only PDF 46 correction `கலகம் ஏற்பட`; it has no dialogue record to reconcile.
- scene 042 had the stage-only PDF 61 correction `சிபார்சு`; it has no dialogue record to reconcile.

## Intentionally blocked scenes

The following remain blocked because they intersect the bounded review/source-limited pages PDF 27, 48, 57 or 74. Do not reconstruct them during Correction 005 reconciliation:

- scenes 011–013 — PDF 27.
- scene 033 — PDF 48.
- scene 039 — PDF 57.
- scenes 053–055 — PDF 74.

## Existing English records reconciled

- English scene 001: verified wording remains valid; source-fidelity note synchronized to corrected Tamil.
- English scenes 002–005: Correction 005 English reconciliation completed without changing scene IDs, unit IDs, dialogue links or counts. The historical batch remains **98 units / 93 immutable dialogue links**. Source-visible anomalies and opaque forms are documented rather than silently normalized.
- English scene 006: affected PDF-19 source correction reconciled without adding new translation work.

## Remaining reconciliation gates

1. **Existing English scenes 007–010 and 014–018** must be checked against the corrected Tamil source units and reconciled only where the Tamil changed. Do not expand translation coverage during this gate.
2. Reconcile affected character mappings where source-exact speaker ownership/labels changed. In particular, audit the source-exact `தர்யம்` occurrence from scene 017 rather than normalizing it silently.
3. Recheck song/performance links only where Correction 005 touched a linked cue or performance span; leave unrelated song authorship unchanged.
4. Re-run translation QA plus dialogue/index/count consistency checks against the reconciled corpus.
5. Synchronize the work README, relevant indexes/audits/status files, `data/works.json`, root status metadata, handover and next-chat prompt only after the reconciliation gates pass.
6. Translation expansion remains paused until this note can be changed from **in progress** to **closed**.

## Current checkpoint

Live `main` immediately before this note update:

`16f26334f0b2389ab330c6cf552fa188fb4bb805` — `raja-rani: record English batch 002-005 reconciliation`

This SHA is only a checkpoint. Live `main` remains authoritative if it advances.
