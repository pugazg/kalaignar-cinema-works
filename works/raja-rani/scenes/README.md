# ராஜா ராணி — scene derivatives

**Stage:** structured derivatives  
**Scene segmentation/index:** complete — **58 archival segments**  
**Verified scene-text files:** **20 / 50 eligible**  
**Blocked source-review segments:** **8**

This directory is a derivative layer built from the canonical Tamil page files under `../pages/`. It does **not** replace, normalize or repair the canonical source layer.

## Canonical authority

- Source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- Canonical screenplay: PDF **10–79** / printed pp. **9–78**
- Tamil fidelity gate: **closed-with-source-limitations**
- Verified screenplay pages: **66/70**
- Review screenplay pages: **4/70 — PDF 27, 48, 57, 74**
- Gate disposition: `../notes/tamil-fidelity-gate-disposition.md`
- Segmentation audit: `../notes/scene-segmentation-audit.md`

## Scene-number policy

The booklet does **not** print numbered screenplay scenes.

Therefore:

- `raja-rani-s001` through `raja-rani-s058` are archive-only navigation identifiers;
- their ordinals are not represented as source scene numbers;
- `reader_label_ta` values in `index.json` are archival navigation labels, not invented source headings;
- page breaks alone are never scene boundaries.

## Eligibility

`index.json` records **58** source-supported archival scene segments.

- **50** segments are eligible for verified scene-text extraction.
- **8** segments are blocked because their span intersects a review-source page.

Blocked scene IDs:

- `raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013` — intersect PDF 27
- `raja-rani-s033` — intersects PDF 48
- `raja-rani-s039` — intersects PDF 57
- `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055` — intersect PDF 74

No verified scene-text file is created for a blocked scene until a stronger source resolves the affected page.

## Scene-text extraction progress

Completed batches:

- Batch 001: `scene-001.md` through `scene-010.md`
- Batch 002: `scene-014.md` through `scene-023.md`

Blocked `scene-011.md`–`scene-013.md` are intentionally absent because those archive segments intersect PDF 27.

Batch reports:

- `../notes/scene-text-batch-001.md`
- `../notes/scene-text-batch-002.md`

Current totals:

- archival scene segments: **58**
- eligible scene-text segments: **50**
- completed verified scene-text files: **20**
- remaining eligible scene-text files: **30**
- blocked scene-text segments: **8**

## Derivative rules

Each verified scene file:

1. copies Tamil only from verified canonical page files;
2. retains source spelling, punctuation, exact speaker labels, stage directions, written text and source-visible ornaments represented in the canonical layer;
3. retains every canonical PDF/printed-page anchor occurring inside the scene;
4. stops immediately before the next accepted transition in the segmentation audit;
5. does not invent a speaker for source-unlabelled speech;
6. does not repair or normalize the canonical page layer;
7. is not produced when any part of the scene intersects PDF 27, 48, 57 or 74.

## Next activity

Continue source-order verified scene-text extraction with **`s024`–`s032`**, then stop before blocked `s033`. Preserve the accepted segmentation boundaries exactly.
