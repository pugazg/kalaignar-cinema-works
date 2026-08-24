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

## Correction 002 — PDF 53 / printed p.52

During preparation of scene-text Batch 006, the T036 boundary and surrounding PDF 53 text were reopened against the rendered scan before the carried-forward scene was emitted.

The scan shows that the first-pass canonical page had again normalized source-visible Raja forms:

- the dialogue labels on PDF 53 print **`ராசா:`**, not `ராஜா:`;
- the T036 stage direction prints **`(ராசா, ராணியைக் கொண்டு வந்து விடுகிறான்...`**, not the normalized `(ராஜா, ராணியைக் கொண்டுவந்து விடுகிறான்...`.

The canonical PDF 53 page has been restored accordingly. This correction is source-visible and does not alter the page's verified status or the global fidelity counts.

## Correction 003 — PDF 58–59 / printed pp.57–58

During preparation of scene-text Batch 007, the verified T040 span was reopened against fresh high-resolution renders before `scene-040.md` was emitted.

The recheck found the same type of surviving speaker-label normalization while also confirming that the source deliberately alternates forms on these pages:

- **PDF 58:** the first Raja dialogue after `[ராஜா பாடிக்கொண்டு வருகிறான்.]` prints **`ராசா:`**; the following `அது சரி...ராணி...` line prints **`ராஜா:`**; the next `நீ இருந்தாலும்...` line again prints **`ராசா:`**. The canonical page had normalized both `ராசா:` labels to `ராஜா:`; they are now restored without changing the genuinely printed `ராஜா:` occurrence or stage-direction form.
- **PDF 59:** five Raja dialogue labels occur before T041. The source prints them in the sequence **`ராஜா:` / `ராசா:` / `ராஜா:` / `ராசா:` / `ராஜா:`**. The two `ராசா:` occurrences had been normalized and are now restored while the three source-visible `ராஜா:` labels remain unchanged.

No other wording was changed in this correction. Both pages remain `verified`, and no review page was promoted.

## Downstream effect

- `scene-034.md` was generated after Correction 001 and therefore already follows the corrected PDF 49–50 labels.
- `scene-035.md` has been reconciled so its PDF 53 portion now carries the restored `ராசா:` labels.
- `scene-036.md` was generated only after Correction 002 and begins with the restored T036 stage-direction form.
- `scene-040.md` is generated only after Correction 003 and therefore preserves the exact alternating `ராஜா:` / `ராசா:` labels across PDF 58–59.

No review page was promoted and the global fidelity counts remain unchanged:

- verified source pages: **75/79**;
- review source pages: **4/79 — PDF 27, 48, 57, 74**;
- verified screenplay pages: **66/70**;
- review screenplay pages: **4/70**.
