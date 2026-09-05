# அம்மையப்பன் — scene-text derivatives

**Stage:** **complete-verified**  
**Archive-only scene/segment IDs:** **63**  
**Verified scene-text files:** **63/63**  
**Blocked source-review segments:** **0**

This directory is a derivative layer built only from the **105/105 dual-gate verified** canonical Tamil in `../transcription/full-text.md`. It does not replace or normalize the canonical source layer.

## Scene-number policy

The booklet does **not** print numbered screenplay scenes. Therefore `ammaiyappan-s001`–`ammaiyappan-s063` are archive-only navigation identifiers. Their ordinals are not source scene numbers.

## Boundary authority

- canonical source-visible headings: **63**;
- earlier intake-ledger transitions: **58**;
- all 58 reconciled against canonical headings;
- later canonical/source review contributed **5 additional source-visible headings**;
- final boundary inventory: `../notes/scene-segmentation-preflight.md`;
- whole-work ownership QA: `../notes/scene-boundary-ownership-qa.md` — **PASS**.

## Derivative rules

Each scene file:

1. copies an exact contiguous span from verified canonical Tamil;
2. begins at one source-visible canonical heading;
3. ends immediately before the next source-visible canonical heading, or at canonical EOF for the final segment;
4. preserves source spelling, punctuation, speaker labels, stage directions and page anchors;
5. adds only derivative provenance comments and an archive-only ID;
6. never invents a printed scene number;
7. never repairs or normalizes canonical Tamil.

## Downstream gate

Scene-text derivative construction and boundary-ownership QA are complete. The **dialogue-index phase may now open**. Character/entity indexing remains blocked until dialogue indexing closes.
