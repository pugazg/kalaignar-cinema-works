# ராஜா ராணி — scene derivatives

**Stage:** verified scene-text derivatives complete with review-source exclusions  
**Scene segmentation/index:** complete — **58 archival segments**  
**Verified scene-text files:** **50 / 50 eligible**  
**Blocked source-review segments:** **8**

This directory is a derivative layer built from the canonical Tamil page files under `../pages/`. It does **not** replace, normalize or repair the canonical source layer.

## Canonical authority

- Source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- Canonical screenplay: PDF **10–79** / printed pp. **9–78**
- Tamil fidelity gate: **closed-with-source-limitations**
- Verified screenplay pages: **66/70**
- Review screenplay pages: **4/70 — PDF 27, 48, 57, 74**
- Gate disposition: `../notes/tamil-fidelity-gate-disposition.md`
- Post-fidelity corrections: `../notes/post-fidelity-corrections.md`
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

- **50** segments are eligible for verified scene-text extraction and all **50/50 are now complete**.
- **8** segments remain blocked because their span intersects a review-source page.

Blocked scene IDs:

- `raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013` — intersect PDF 27
- `raja-rani-s033` — intersects PDF 48
- `raja-rani-s039` — intersects PDF 57
- `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055` — intersect PDF 74

No verified scene-text file is created for a blocked scene until a stronger source resolves the affected page.

## Scene-text extraction history

Completed batches:

- Batch 001: `scene-001.md` through `scene-010.md`
- Batch 002: `scene-014.md` through `scene-023.md`
- Batch 003: PDF **40–44**; completed `scene-024.md` through `scene-027.md`
- Batch 004: PDF **45–49**; completed carried-forward `scene-028.md` and `scene-029.md` through `scene-032.md`; blocked `s033` remained absent
- Batch 005: PDF **50–54**; completed carried-forward `scene-034.md` and `scene-035.md`; `s036` carried forward
- Batch 006: PDF **55–59**; completed carried-forward `scene-036.md`, `scene-037.md` and `scene-038.md`; blocked `s039` remained absent
- Batch 007: PDF **60–64**; resumed after blocked `s039`, completed `scene-040.md` through `scene-045.md`; `s046` carried forward
- Batch 008: PDF **65–69**; completed carried-forward `scene-046.md`, then `scene-047.md` through `scene-050.md`; `s051` carried forward
- Batch 009: PDF **70–74**; completed carried-forward `scene-051.md` and `scene-052.md`; stopped before blocked `s053`
- Batch 010: PDF **75–79**; resumed only at T056 after the blocked PDF-74 scene group and completed final eligible `scene-056.md`, `scene-057.md` and `scene-058.md`

Blocked `scene-011.md`–`scene-013.md`, `scene-033.md`, `scene-039.md` and `scene-053.md`–`scene-055.md` are intentionally absent because their archive segments intersect review-source pages.

The five-source-page batching policy never emits a partial scene merely because an iteration boundary is reached, and it never fills or imports review-source text to force continuity.

Post-fidelity rendered-scan rechecks restored source-visible Raja-label variation on PDF 49–50, PDF 53, PDF 58–59 and PDF 66. Batch 009 found no further canonical correction in PDF 70–73, and Batch 010 found no new canonical correction in the verified T056–T058 span on PDF 77–79.

Batch reports:

- `../notes/scene-text-batch-001.md`
- `../notes/scene-text-batch-002.md`
- `../notes/scene-text-batch-003.md`
- `../notes/scene-text-batch-004.md`
- `../notes/scene-text-batch-005.md`
- `../notes/scene-text-batch-006.md`
- `../notes/scene-text-batch-007.md`
- `../notes/scene-text-batch-008.md`
- `../notes/scene-text-batch-009.md`
- `../notes/scene-text-batch-010.md`

Final scene-text totals:

- archival scene segments: **58**
- eligible scene-text segments: **50**
- completed verified scene-text files: **50**
- remaining eligible scene-text files: **0**
- blocked scene-text segments: **8**

## Derivative rules

Each verified scene file:

1. copies Tamil only from verified canonical page files;
2. retains source spelling, punctuation, exact speaker labels, stage directions, written text and source-visible ornaments represented in the canonical layer;
3. retains every canonical PDF/printed-page anchor occurring inside the scene;
4. stops immediately before the next accepted transition in the segmentation audit;
5. does not invent a speaker for source-unlabelled speech;
6. does not repair or normalize the canonical page layer;
7. is not produced when any part of the scene intersects PDF 27, 48, 57 or 74;
8. is never emitted partially merely because a five-page iteration ends inside the scene.

## Next activity

Run a compact **scene-layer completion / repository-bookkeeping checkpoint**. Reconcile the pre-existing Raja Rani registry gap in `data/works.json` and the repository root README, verify that all 50 eligible scene files and 8 blocked IDs agree across work metadata/indexes, and then open the **dialogue index** phase.

Dialogue extraction must use only explicitly speaker-labelled utterances from verified Tamil units. Source-unlabelled speech must remain unassigned.
