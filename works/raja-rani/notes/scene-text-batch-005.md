# ராஜா ராணி — Scene-Text Derivative Batch 005

## Scope

Verified scene-text derivative iteration using the established **five-source-page batching policy**.

Source-page window for this iteration:

- PDF **50–54**
- printed pp. **49–53**

The iteration first completes carried-forward `raja-rani-s034`, whose accepted source span begins on verified PDF 49, then completes `raja-rani-s035`. `raja-rani-s036` begins on PDF 53 but continues through PDF 56, so no partial `scene-036.md` is emitted at the PDF 54 batch boundary.

## Post-fidelity source recheck

Before extraction, PDF **49–50** were reopened against fresh high-resolution renders because their local headers still carried stale `status=draft` bookkeeping.

That source recheck found a surviving speaker-label normalization error:

- PDF 49 prints **`ராசா:`** for Raja's dialogue labels; the canonical page had `ராஜா:` and has now been corrected.
- PDF 50 likewise prints **`ராசா:`** for the dialogue labels corrected in this pass.
- PDF 50 separately prints the stage-direction form **`(ராஜா: ராணியின் படத்தைப் பார்த்துவிடுகிறான்.)`**; that distinct source form remains `ராஜா`.

The page headers for PDF 49 and 50 are now reconciled to `verified`. The source-backed label correction is documented separately in `notes/post-fidelity-corrections.md`.

No review page was promoted and the fidelity totals remain **75 verified / 4 review source pages** and **66 verified / 4 review screenplay pages**.

## Completed scene-text derivatives

Two eligible scene files are complete in this iteration:

- `raja-rani-s034` → `scenes/scene-034.md`
- `raja-rani-s035` → `scenes/scene-035.md`

Both are fully supported by verified Tamil source pages.

## Boundary checks

- `s034` begins at T034 with the standalone source `★` on PDF 49 and `(பாபு ராணியின் வீட்டில் ஏற முயற்சிக்கிறான்)`. It continues through PDF 50 and PDF 51, then through the opening portion of PDF 52. It stops immediately before T035 `—★—` on PDF 52.
- `s035` begins at T035 on PDF 52 with the electric-store aftermath, retains Raja's utterance across the physical PDF 52→53 page boundary as one source continuation, and ends on PDF 53 immediately before T036 `—★—`.
- `s036` begins at T036 on PDF 53 with `(ராஜா, ராணியைக் கொண்டுவந்து விடுகிறான்...)` and continues through PDF 56. Because the present five-page window ends at PDF 54, it is carried forward intact rather than emitted partially.

## Extraction rules applied

- Tamil copied only from verified canonical page files.
- The derivative uses the corrected source-visible `ராசா:` labels on PDF 49–50 and does not normalize them to `ராஜா:`.
- Exact source spelling, punctuation, stage directions, source-labelled/unlabelled structure and ornaments are preserved from the canonical layer.
- Page provenance comments are retained at every represented PDF boundary.
- Cross-page utterances remain continuous across page anchors.
- Archive scene IDs are derivative navigation only; the booklet prints no screenplay scene numbers.
- No review-source Tamil from PDF 27, 48, 57 or 74 is promoted.
- No partial scene file is emitted merely to satisfy a five-page batch boundary.

## Result

- archival scene segments: **58**
- eligible scene-text segments: **50**
- blocked scene-text segments: **8**
- verified scene-text files completed before this batch: **29**
- newly completed in this batch: **2**
- verified scene-text files completed: **31/50 eligible**
- remaining eligible scene-text files: **19**

## Next five-page iteration

Process source window **PDF 55–59 / printed pp.54–58**.

First complete carried-forward `s036` through PDF 56, then complete the short eligible `s037` and `s038` transitions on PDF 56. Stop before/block `s039` because it intersects review-source PDF 57. Do not skip across that blocked segment to emit `s040` within the same iteration.
