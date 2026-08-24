# Raja Rani — Next Phase Readiness Checkpoint

## Current phase

Source intake, structural mapping, canonical Tamil first pass and the full rendered-scan fidelity audit are complete for the supplied scan.

The Tamil fidelity gate is **closed-with-source-limitations**. Four screenplay pages remain `review`: PDF **27, 48, 57 and 74**.

The source-supported scene segmentation/index phase is complete, and verified scene-text extraction is in progress.

Controlling files:

- `notes/tamil-fidelity-gate-disposition.md`
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
- Verified scene-text files completed: **20/50 eligible**.

## Canonical-status reconciliation

Before Batch 002, PDF 31–33 and 35–40 still carried stale local `draft` / audit-pending labels even though rendered-scan Fidelity Batch 004 had already verified them. Their local status metadata has now been reconciled to `verified`; PDF 34 had already been verified through targeted high-resolution review.

This was bookkeeping reconciliation only. No canonical Tamil wording was changed.

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

## Current scene-text progress

- archival segments: **58**
- eligible scene-text segments: **50**
- completed verified scene-text files: **20**
- remaining eligible scene-text files: **30**
- blocked scene segments: **8**

Blocked IDs:

`raja-rani-s011`, `raja-rani-s012`, `raja-rani-s013`, `raja-rani-s033`, `raja-rani-s039`, `raja-rani-s053`, `raja-rani-s054`, `raja-rani-s055`.

## Readiness

- scene segmentation/index: **COMPLETE**
- verified scene-text derivative generation: **IN PROGRESS — 20/50 eligible complete**
- dialogue extraction: **not yet started; follow verified-source-unit gate**
- character/entity index: **not yet started**
- song/performance authorship gate: **not yet started**
- English translation: **not yet started; verified Tamil units only**

## Next activity

Continue verified scene-text extraction with **`raja-rani-s024` through `raja-rani-s032`**, then stop before blocked `raja-rani-s033`. Preserve the accepted source-supported boundaries exactly.
