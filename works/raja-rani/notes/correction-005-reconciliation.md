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

### Canonical-to-scene / dialogue propagation

- scene 034 / dialogue scene 034 — PDF 52 speaker-label correction; `raja-rani-s034-d060` remains the same ID and provenance, with source-verified speaker `ராணி`.
- scene 052 / dialogue scene 052 — corrected Socrates material across PDFs 70–73.
- scenes 057–058 / dialogue scenes 057–058 — final manual corrections across PDFs 77–79.
- PDF 76 remains inside blocked scene 055 because PDF 74 is source-limited; no derivative reconstruction was made.

### Source-order reconciliation completed in the current pass

- scenes 001–005 and dialogue shards 001–005 reconciled through PDF 19.
- scene 006 and dialogue shard 006 reconciled on PDF 19.
- scene 008: checked; no derivative text change required.
- scene 009: canonical scene file reconciled across PDFs 21–25.
- scene 010: checked; no derivative text change required.

### Existing English records already reconciled

- English scene 001: verified wording remains valid; the source-fidelity note now records corrected Tamil `அப்படின்னா... அவன்கண்...?`.
- English scene 006: corrected `வீசினாய்` reading propagated; the `அணைத்தும்` source form is documented without changing canonical Tamil.

## Explicit pending items at this checkpoint

1. **scene 007** — canonical pages 20–21 differ from the existing derivative, but the connected repository write action rejected the whole-file update. Do not mark scene 007 reconciled until the actual scene file is updated and rechecked.
2. **dialogue scene 007** — pending after scene 007.
3. **dialogue scene 009** — scene file is corrected, but the 58-record minified shard still needs safe whole-file reconciliation. Do not alter record IDs or provenance.
4. **existing English scenes 002–005** — source changes touch verified translation units and require a translation-reconciliation pass. In particular, scene 002 includes corrected source readings `மனச்சாந்தியோட ... மந்திகளும்` and source-exact `நான் பேய் பார்த்துட்டு வரட்டுமாப்பா?`; stale English must not be silently retained.
5. **existing English scenes 007–010** — reconcile after corresponding Tamil scene/dialogue layers close.
6. Continue source-order reconciliation from the next eligible screenplay span after scene 010, skipping blocked scenes 011–013 and preserving the four review-page limitations.
7. Later gate work still includes affected song/front-matter derivatives, character mappings where exact speaker ownership changed, all existing translated scenes 14–18 touched by corrections, QA/count consistency, and final README/index/handover synchronization.

## Checkpoint

Live `main` immediately before this note was created:

`006b8a011e0209a4fdcfd8ea4f4c1d0ae0944c1b` — `raja-rani: reconcile scene 9 with corrected pages 21-25`

This SHA is only a checkpoint. Live `main` remains authoritative if it advances.
