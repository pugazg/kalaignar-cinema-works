# Raja Rani — Next Phase Readiness Checkpoint

## Current phase

Source intake, structural mapping, canonical Tamil first pass and the full rendered-scan fidelity audit are complete for the supplied scan.

The Tamil fidelity gate is **closed-with-source-limitations**. Four screenplay pages remain `review`: PDF **27, 48, 57 and 74**.

The source-supported scene segmentation/index phase is complete, and verified scene-text extraction is in progress using the user-requested **five source pages per iteration** batching rule.

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
- Verified scene-text files completed: **34/50 eligible**.

## Canonical-status / source recheck history

Before Batch 002, PDF 31–33 and 35–40 still carried stale local `draft` / audit-pending labels even though rendered-scan Fidelity Batch 004 had already verified them. Their local status metadata was reconciled to `verified`; PDF 34 had already been verified through targeted high-resolution review.

Before Batch 003, PDF 43 and PDF 44 likewise still carried stale local `status=draft` labels even though Fidelity Batch 005 had already completed their rendered-scan review. Their local metadata was reconciled to `verified`.

Before Batch 004, PDF 45 and PDF 46 still carried the same stale local `status=draft` labels even though Fidelity Batch 005 had visually reviewed them. Their local metadata was reconciled to `verified`.

During Batch 005, fresh rendered-scan reinspection of PDF 49–50 found that the dialogue label printed there is `ராசா:` rather than the normalized `ராஜா:` retained in the first-pass page files. The affected dialogue labels were corrected directly from the scan, while PDF 50's distinct source stage-direction form `ராஜா` was preserved. The page headers were reconciled to `verified`.

During Batch 006, reinspection of PDF 53 found the same surviving normalization in that page's dialogue labels and the T036 stage direction. PDF 53 was restored to source-visible `ராசா:` labels and `(ராசா, ராணியைக் கொண்டு வந்து விடுகிறான்...)`; the affected PDF-53 portion of previously completed `scene-035.md` was reconciled before `scene-036.md` was emitted. See `notes/post-fidelity-corrections.md`.

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
- completed verified scene-text files: **34**
- remaining eligible scene-text files: **16**
- blocked scene segments: **8**

Blocked IDs:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

`raja-rani-s039` begins on PDF 56 and intersects review-source PDF 57. Batch 006 therefore stopped before it and did not skip across it to emit `s040` in the same iteration.

## Readiness

- scene segmentation/index: **COMPLETE**
- verified scene-text derivative generation: **IN PROGRESS — 34/50 eligible complete**
- dialogue extraction: **not yet started; follow verified-source-unit gate**
- character/entity index: **not yet started**
- song/performance authorship gate: **not yet started**
- English translation: **not yet started; verified Tamil units only**

## Next activity

Process the next **five-source-page** window: **PDF 60–64 / printed pp.59–63**. Resume after blocked `s039` by completing carried-forward `s040` from its verified PDF 58 start and `s041` from its verified PDF 59 start, then complete eligible `s042`, `s043`, `s044` and `s045` through PDF 64. Do not include any text from blocked `s039`.
