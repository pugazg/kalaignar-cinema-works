# ராஜா ராணி — Scene-Text Derivative Batch 002

## Scope

Second verified scene-text derivative batch after the Tamil fidelity gate was closed with documented source limitations.

Blocked `raja-rani-s011`–`raja-rani-s013` were skipped because they intersect review-source PDF 27. Extraction resumed at the next eligible source-order segment.

Completed archive scene segments:

- `raja-rani-s014` → `scenes/scene-014.md`
- `raja-rani-s015` → `scenes/scene-015.md`
- `raja-rani-s016` → `scenes/scene-016.md`
- `raja-rani-s017` → `scenes/scene-017.md`
- `raja-rani-s018` → `scenes/scene-018.md`
- `raja-rani-s019` → `scenes/scene-019.md`
- `raja-rani-s020` → `scenes/scene-020.md`
- `raja-rani-s021` → `scenes/scene-021.md`
- `raja-rani-s022` → `scenes/scene-022.md`
- `raja-rani-s023` → `scenes/scene-023.md`

All ten scenes are outside review-source PDFs 27, 48, 57 and 74 and are therefore eligible for verified scene-text derivation under `tamil-fidelity-gate-disposition.md`.

## Pre-extraction canonical-status reconciliation

Before producing scenes whose spans reach PDF 31–40, the canonical page metadata was reconciled with the already completed rendered-scan fidelity audit:

- PDF 31–33 and 35–40 had stale `status=draft` / `Visual fidelity audit: pending` bookkeeping even though `visual-fidelity-audit-batch-004.md` had already verified those pages against the rendered scan;
- those page files were updated to `status=verified` and their local status sections now point to completed Batch 004 review;
- PDF 34 was already verified after targeted high-resolution review and required no status change.

No canonical Tamil wording was changed by that bookkeeping reconciliation.

## Extraction rules applied

- Tamil is copied only from verified canonical page files.
- Source spelling, punctuation, speaker labels, stage directions, written-text structures and ornaments are retained.
- Page-anchor comments are retained at every PDF-page boundary represented inside a scene.
- Archive scene IDs and ordinals are navigation metadata only; the booklet prints no screenplay scene numbers.
- A page break alone never creates a scene boundary.
- Each derivative stops immediately before the next accepted transition in `scene-segmentation-audit.md`.
- No text from PDF 27, 48, 57 or 74 is included in this batch.

## Boundary checks

- `s014` is the source-supported home-confrontation transition on PDF 28 and stops before T015.
- `s015` begins with the transition into `ராஜாவின் எலக்ட்ரிக் ஸ்டோரில்` and runs through PDF 30, stopping before the home transition T016.
- `s016` begins with T016 on PDF 30, continues into PDF 31, and stops before the Geetha-house transition T017.
- `s017` begins at T017 on PDF 31, continues through the Raja/Geetha/Babu exchange across PDFs 31–33, and stops before circular separator T018.
- `s018` begins at the source `○` on PDF 33 and continues through Current's explanation, the bulb-colour exchange and salary discussion into PDF 35, stopping before T019.
- `s019` and `s020` preserve the first and second of the source-visible three `——★——` transitions on PDF 35 as separate short event scenes.
- `s021` begins at the third PDF 35 separator and preserves the cross-page pigeon/Samarasam/Shantham sequence through the opening of PDF 38. The internal PDF 36 separator remains source text inside this accepted archival segment because the segmentation audit does not treat it as a separate accepted boundary.
- `s022` is the short source-supported Gnanakkan salary-request block on PDF 38.
- `s023` begins at the standalone `★` on PDF 38, continues through the heroine/money discussion across PDFs 38–40, and stops before the `அகல்யா நாடக ஒத்திகை` transition T024.

## Result

- archival scene segments: **58**
- source-review-blocked segments: **8**
- eligible scene-text segments: **50**
- verified scene-text files completed: **20/50 eligible**
- remaining eligible scene-text files: **30**
- blocked scene-text segments remain: **8**

Blocked scene IDs remain:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

## Next activity

Continue verified scene-text extraction with the next eligible source-order run, **`s024`–`s032`**, then stop before blocked `s033`. Preserve the accepted segmentation boundaries exactly and do not pull review-source text into a verified derivative.
