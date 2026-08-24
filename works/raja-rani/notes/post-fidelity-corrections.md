# ராஜா ராணி — Post-Fidelity Source Corrections

## Purpose

Record source-backed corrections discovered after the full rendered-scan fidelity phase had already been closed-with-source-limitations.

The controlling source remains `TVA_BOK_0017188_ராஜா_ராணி.pdf`. Corrections in this file are made only from direct reinspection of the rendered scan. They do not use OCR as authority, film audio, subtitles, web text, another edition or contextual reconstruction.

## Correction 001 — PDF 49–50 / printed pp.48–49

During preparation of scene-text Batch 005, PDF 49 and PDF 50 were reopened against fresh high-resolution renders because their local page headers still carried stale `status=draft` bookkeeping despite the completed fidelity audit.

The recheck found a source-label normalization error that had survived the earlier first pass:

- **PDF 49:** the scan prints dialogue label **`ராசா:`** throughout the page where the canonical page file had `ராஜா:`. All affected dialogue labels were restored to the source-visible `ராசா:` form.
- **PDF 50:** the scan likewise prints **`ராசா:`** for Raja's dialogue labels on this page. Those labels were restored.
- PDF 50 separately prints the stage-direction name as **`(ராஜா: ராணியின் படத்தைப் பார்த்துவிடுகிறான்.)`**. That source-visible `ராஜா` form is preserved and was **not** changed to `ராசா`.

The local page headers for PDF 49 and 50 were also reconciled to `status=verified`, consistent with the already completed full fidelity disposition. No other wording was changed in this correction.

## Downstream effect

`scene-034.md` is generated only after these source-label corrections, so its speaker labels follow the corrected canonical page layer.

No review page was promoted and the global fidelity counts remain unchanged:

- verified source pages: **75/79**;
- review source pages: **4/79 — PDF 27, 48, 57, 74**;
- verified screenplay pages: **66/70**;
- review screenplay pages: **4/70**.
