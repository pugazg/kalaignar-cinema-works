# Raja Rani — Next Phase Readiness Checkpoint

## Current phase

Source intake, structural mapping, canonical Tamil first pass and the full rendered-scan fidelity audit are complete for the supplied scan.

The Tamil fidelity gate is **closed-with-source-limitations**. Four screenplay pages remain `review`: PDF **27, 48, 57 and 74**.

The source-supported scene segmentation/index phase is complete, and verified scene-text extraction is in progress using the established **five source pages per iteration** batching rule.

Controlling files:

- `notes/tamil-fidelity-gate-disposition.md`
- `notes/post-fidelity-corrections.md`
- `notes/scene-segmentation-audit.md`
- `scenes/index.json`
- `scenes/README.md`

## Completed

- Source identity, checksum, pagination and content boundaries verified.
- Canonical source-order page layer complete: `pages/001.md`–`079.md`.
- Screenplay range complete: PDF **10–79 / printed pp.9–78 — 70/70 pages**.
- Full rendered-scan visual audit complete through PDF 79.
- High-resolution review completed for the former uncertainty queue.
- Verified source pages: **75/79**.
- Review source pages: **4/79 — PDF 27, 48, 57, 74**.
- Verified screenplay pages: **66/70**.
- Review screenplay pages: **4/70**.
- Embedded dramatic boundaries retained:
  - `சேரன் செங்குட்டுவன்`: PDF 13–19;
  - `அகல்யா நாடக ஒத்திகை`: PDF 40–first part of 41;
  - `சாக்ரடீஸ் (நாடகம்)`: PDF 66–first part of 73.
- Source-supported archival scene segmentation complete: **58 segments**.
- Verified scene-text eligibility: **50 segments**.
- Source-review-blocked scene segments: **8**.
- Scene-text Batch 001 complete: `scene-001.md`–`scene-010.md`.
- Scene-text Batch 002 complete: `scene-014.md`–`scene-023.md`.
- Scene-text Batch 003 complete for source-page window **PDF 40–44**: `scene-024.md`–`scene-027.md`.
- Scene-text Batch 004 complete for source-page window **PDF 45–49**: carried-forward `scene-028.md` plus `scene-029.md`–`scene-032.md`.
- Scene-text Batch 005 complete for source-page window **PDF 50–54**: carried-forward `scene-034.md` plus `scene-035.md`.
- Scene-text Batch 006 complete for source-page window **PDF 55–59**: carried-forward `scene-036.md` plus `scene-037.md` and `scene-038.md`; blocked `s039` remains absent.
- Scene-text Batch 007 complete for source-page window **PDF 60–64**: resumed after blocked `s039`, completed carried-forward `scene-040.md` and `scene-041.md`, then `scene-042.md`–`scene-045.md`.
- Scene-text Batch 008 complete for source-page window **PDF 65–69**: completed carried-forward `scene-046.md` and then `scene-047.md`–`scene-050.md`; `s051` was carried forward.
- Scene-text Batch 009 complete for source-page window **PDF 70–74**: completed carried-forward `scene-051.md` and `scene-052.md`; stopped before blocked `s053` because it intersects review-source PDF 74.
- Verified scene-text files completed: **47/50 eligible**.

## Canonical-status / source recheck history

Before Batch 002, PDF 31–33 and 35–40 still carried stale local `draft` / audit-pending labels even though rendered-scan Fidelity Batch 004 had already verified them. Their local status metadata was reconciled to `verified`; PDF 34 had already been verified through targeted high-resolution review.

Before Batch 003, PDF 43 and PDF 44 likewise still carried stale local `status=draft` labels even though Fidelity Batch 005 had already completed their rendered-scan review. Their local metadata was reconciled to `verified`.

Before Batch 004, PDF 45 and PDF 46 still carried the same stale local `status=draft` labels even though Fidelity Batch 005 had visually reviewed them. Their local metadata was reconciled to `verified`.

During Batch 005, fresh rendered-scan reinspection of PDF 49–50 found source-visible `ராசா:` dialogue labels that had been normalized to `ராஜா:` in the first-pass page files. The affected labels were restored while PDF 50's distinct source stage-direction form `ராஜா` was preserved.

During Batch 006, reinspection of PDF 53 found the same surviving normalization in that page's dialogue labels and the T036 stage direction. PDF 53 was restored to source-visible `ராசா:` labels and `(ராசா, ராணியைக் கொண்டு வந்து விடுகிறான்...)`; the affected PDF-53 portion of `scene-035.md` was reconciled before `scene-036.md` was emitted.

During Batch 007, the carried-forward T040 source span on PDF 58–59 was reopened against fresh high-resolution renders. The source deliberately alternates `ராஜா:` and `ராசா:`. PDF 58's relevant sequence is `ராசா:` / `ராஜா:` / `ராசா:`; PDF 59's five pre-T041 labels are `ராஜா:` / `ராசா:` / `ராஜா:` / `ராசா:` / `ராஜா:`. The previously normalized `ராசா:` occurrences were restored before `scene-040.md` was generated. The source-visible `[ராஜா பாடிக்கொண்டு வருகிறான்.]` stage direction remains unchanged.

During Batch 008, the T047→T050 span was reopened against fresh high-resolution renders. The opening continuation label on PDF 66 is source-visible `ராசா:` rather than the normalized `ராஜா:` in the canonical page. That label was restored before `scene-047.md` was generated; running-text `ராஜா` forms elsewhere on PDF 66 remain unchanged as printed. See `notes/post-fidelity-corrections.md`.

During Batch 009, PDF 70–74 were reopened against fresh high-resolution renders, including the T052 prison boundary, the PDF 73 return from the staged `சாக்ரடீஸ்` performance, and the PDF 74 obstruction. No new canonical correction was required in verified PDF 70–73. PDF 74 remains review because the later `K. N. சங்கரன்` ownership/address overprint physically obscures original printing.

No review page was promoted and the global fidelity totals remain unchanged.

## Bounded source limitations

- PDF 27: one faint/washed internal-monologue word remains unresolved.
- PDF 48: two short spans before `சமரசம் வீடு` remain unresolved.
- PDF 57: one compact colloquial phrase remains unresolved after repeated high-resolution review.
- PDF 74: later `K. N. சங்கரன்` ownership/address overprint physically obscures original printing; hidden text is not reconstructed.

These four pages remain `review` even though the audit phase itself is closed.

## Downstream eligibility rule

Later layers must use **verified Tamil only**.

- The structural scene index covers the entire screenplay.
- A verified scene-text derivative may be created only when its complete source span is verified.
- Any scene intersecting PDF 27, 48, 57 or 74 remains blocked for verified scene-text output.
- Dialogue records may be created only from explicitly speaker-labelled verified source utterances.
- English translation may begin only for corresponding verified Tamil units.
- No uncertain or physically obscured text may be filled from context, film audio, subtitles, websites, OCR or another edition.
- A five-page iteration never creates a partial scene file; a scene crossing the window boundary is carried into the next iteration.
- A blocked scene is not skipped within the same iteration.

## Current scene-text progress

- archival segments: **58**
- eligible scene-text segments: **50**
- completed verified scene-text files: **47**
- remaining eligible scene-text files: **3**
- blocked scene segments: **8**

Blocked IDs:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

`raja-rani-s051` and `raja-rani-s052` are now complete. The next three archival segments `s053`–`s055` remain blocked because each intersects review-source PDF 74. The remaining eligible scene-text files are therefore `s056`, `s057` and `s058`.

## Readiness

- scene segmentation/index: **COMPLETE**
- verified scene-text derivative generation: **IN PROGRESS — 47/50 eligible complete**
- dialogue extraction: **not yet started; follow verified-source-unit gate**
- character/entity index: **not yet started**
- song/performance authorship gate: **not yet started**
- English translation: **not yet started; verified Tamil units only**

## Next activity

Process the next **five-source-page** window: **PDF 75–79 / printed pp.74–78**. The opening portion still belongs to blocked `s055`, which intersects review-source PDF 74 and continues through PDF 77. Resume only after blocked `s053`–`s055` at T056 on PDF 77, then complete the remaining eligible `s056`, `s057` and `s058` through PDF 79. Do not import any text from blocked PDF-74 scenes into verified derivatives.
