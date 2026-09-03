# ராஜா ராணி — scene derivatives

**Stage:** **complete-verified**  
**Scene segmentation/index:** complete — **58 archival segments**  
**Verified scene-text files:** **58/58**  
**Blocked source-review segments:** **0**

This directory is a derivative layer built from canonical Tamil page files under `../pages/`. It does **not** replace, normalize or repair the canonical source layer.

## Canonical authority

- Source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- Canonical screenplay: PDF **10–79** / printed pp. **9–78**
- Tamil fidelity gate: **closed-verified**
- verified source pages: **79/79**
- verified screenplay pages: **70/70**
- review source pages: **0**
- final source-review record: `../notes/final-source-review-resolution.md`
- gate disposition: `../notes/tamil-fidelity-gate-disposition.md`
- post-fidelity corrections: `../notes/post-fidelity-corrections.md`
- segmentation audit: `../notes/scene-segmentation-audit.md`

## Scene-number policy

The booklet does **not** print numbered screenplay scenes.

Therefore:

- `raja-rani-s001`–`raja-rani-s058` are archive-only navigation identifiers;
- their ordinals are not source scene numbers;
- `reader_label_ta` in `index.json` is archival navigation, not an invented source heading;
- page breaks alone are never scene boundaries.

## Final source eligibility

`index.json` records **58 source-supported archival scene segments** and all **58/58 are verified**.

The former source-review blocks were resolved by direct scan review:

- PDF 27 → `இரவெல்லாம்` — unblocked s011–s013;
- PDF 48 → `வந்தனா`, `திடீர்னு` — unblocked s033;
- PDF 57 → `முன்னுக்கு பின் முரணாயிகிட்டே போவது?` — unblocked s039;
- PDF 74 → `K. N. சங்கரன் ...` identified as a non-canonical ownership/library stamp; canonical dialogue runs directly `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி` — unblocked s053–s055.

There are no blocked scene IDs remaining.

## Historical extraction batches

The original ten five-source-page extraction batches were produced while some source pages were still review-limited. Their reports remain valuable historical checkpoints, but their then-current blocked-scene statements are not current production state.

Reports:

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

Later direct source review supplied the final seven previously blocked scene derivatives: s011–s013, s033, s039, s053–s055.

## T055 / T056 derivative-boundary correction

Final English QA found a scene-derivative ownership error independent of source fidelity: the older `scene-055.md` had continued beyond its declared `end_before=T056` boundary and duplicated the complete `(முன்)` flashback owned by `scene-056.md`.

The scene layer is now corrected:

- `scene-055.md` ends before `(முன்)`;
- `scene-056.md` exclusively owns the flashback;
- canonical page transcription is unchanged;
- downstream dialogue census is **1,071** unique records rather than the provisional 1,076.

See `../translations/FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Final scene-text totals

- archival scene segments: **58**
- source-eligible segments: **58**
- completed verified scene-text files: **58**
- blocked segments: **0**
- remaining scene-text files: **0**

## Derivative rules

Each verified scene file:

1. copies Tamil only from verified canonical page files;
2. retains source spelling, punctuation, exact speaker labels, stage directions, written text and source-visible ornaments represented in the canonical layer;
3. retains every canonical PDF/printed-page anchor occurring inside the scene;
4. stops immediately before the next accepted transition in the segmentation audit;
5. does not invent a speaker for source-unlabelled speech;
6. does not repair or normalize canonical pages;
7. is never emitted partially merely because a processing iteration ends inside the scene.

## Downstream state

- dialogue layer: **complete-verified — 1,071 unique immutable records / 58 scenes**;
- character layer: **complete-verified — 80/80 exact labels / 44 entities**;
- English screenplay layer: **complete-verified — 58/58 scenes / 1,236 units / 1,071/1,071 links**.

The current production frontier is the separate English translation of the **11 verified numbered front-matter song bodies**. Scene derivatives must remain unchanged during that phase unless direct source evidence explicitly reopens a source issue.
