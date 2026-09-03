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

## Reconciled before this checkpoint

### Canonical-to-scene / dialogue propagation fully closed for these scenes

- scenes 001–006 / dialogue shards 001–006 — reconciled through PDF 19.
- scene 016 / dialogue shard 016.
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
- scene 052 / dialogue shard 052 — corrected Socrates material across PDFs 70–73.
- scenes 057–058 / dialogue shards 057–058 — final manual corrections across PDFs 77–79.

### Scene-layer reconciliation completed, dialogue layer still pending where applicable

- scene 009 — corrected across PDFs 21–25; dialogue shard 009 still pending.
- scene 015 — corrected across PDFs 28–30; dialogue shard 015 still pending.
- scene 017 — corrected across PDFs 31–33; dialogue shard 017 still pending.
- scene 018 — corrected across PDFs 33–35; dialogue shard 018 still pending.
- scene 021 — corrected across PDFs 35–38; dialogue shard 021 still pending.
- scene 023 — corrected across PDFs 38–40; dialogue shard 023 still pending.

### Checked / no derivative text change required

- scenes 008, 010, 014, 027, 029–031, 035–038, 043 and 047.
- scene 032 had the single stage-only PDF 46 correction `கலகம் ஏற்பட`; it has no dialogue record to reconcile.
- scene 042 had the stage-only PDF 61 correction `சிபார்சு`; it has no dialogue record to reconcile.

### Existing English records already reconciled

- English scene 001: verified wording remains valid; source-fidelity note synchronized to corrected Tamil.
- English scene 006: affected source correction reconciled without adding new translation work.

## Explicit pending items at this checkpoint

1. **scene 007** — canonical pages 20–21 differ from the existing derivative, but the connected repository write action rejected the whole-file update. Do not mark scene 007 reconciled until the actual scene file is updated and rechecked.
2. **dialogue scene 007** — pending after scene 007.
3. **dialogue scenes 009, 015, 017, 018, 021 and 023** — corrected scene files exist, but these immutable shards still need source-exact whole-file reconciliation with all IDs and provenance retained.
4. **blocked scenes 011–013, 033, 039 and 053–055** remain blocked because they intersect PDF 27, 48, 57 or 74; do not reconstruct them.
5. Continue source-order canonical-to-scene/dialogue reconciliation after scene 047, skipping blocked scene 053–055 when reached. Recheck later eligible scenes for Correction 005 drift even where earlier correction campaigns had already generated them.
6. **existing English scenes 002–005, 007–010 and 14–18** must be reconciled where corrected Tamil changes their verified source units. Do not silently retain stale source-dependent English.
7. Later gate work still includes affected character mappings where exact speaker ownership changed, song/performance links only where corrected spans touch them, translation QA, dialogue/index/count consistency, work README/index/status files, root status metadata and final handover synchronization.

## Current checkpoint

Live `main` immediately before this note refresh:

`a23a778f0a69bb5805b60265887bcec701d6b7a5` — `raja-rani: reconcile scene 46 dialogue records`

This SHA is only a checkpoint. Live `main` remains authoritative if it advances.
