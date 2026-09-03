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

## Correction 004 — PDF 66 / printed p.65

During preparation of scene-text Batch 008, the T047→T050 source span was reopened against a fresh high-resolution render before the scene derivatives were emitted.

The first dialogue label at the top of PDF 66 is visibly printed **`ராசா:`** in the continuation of the Raja/Gnanakkan exchange from PDF 65. The canonical page had normalized that label to `ராஜா:`.

The opening label has therefore been restored to **`ராசா:`**. The running-text forms `ராஜா` elsewhere on the same page—including the bracketed Babu plot summary and Rani's instruction to Current—remain unchanged because the scan prints those forms distinctly.

PDF 66 remains `verified`; no review page was promoted and no other wording was changed.

## Correction 005 — user-led old-glyph comparison campaign

A later comparison campaign reopened canonical wording after the derivative layers had already been built. The user compared repository pages against `r1.md`, `r2.md` and `r3.md`, then manually inspected disputed words in the scan because the old Tamil typeface caused repeated OCR and assistant visual-reading errors.

The durable lesson is that Repository text and comparison/OCR text are only candidate readings. For disputed old-typeface words, the rendered scan controls, and the user's explicit manual scan verdict for a reviewed token must not be overridden by OCR or modern-spelling expectations.

Current correction state:

- pages **1–25** and **26–50** received the earlier selectively approved comparison replacements;
- pages **51–55** have user-supplied manual scan verdicts, but they are **not yet declared reconciled against live main** and must be checked in the final reconciliation;
- pages **56–70** have had the user-approved manual verdicts applied directly to the canonical page files;
- pages **71–75** have had the user-approved manual verdicts applied directly;
- PDF 72 was subsequently corrected again from `சாக்ரடீசன்` to the user-verified **`சாக்ரடீசின்`**;
- the user will complete a final **075–080** comparison/correction batch in the next chat.

Occurrence-specific variation must remain occurrence-specific. The campaign has already demonstrated legitimate differing forms such as `சேர்ந்தாப்பிலே` / `சேந்தாப்பிலே` and `ஒன்ஸ்மோர்` / `ஒன்சுமோர்`; these are not global-normalization targets.

Two explicitly resolved `Neither` cases in the applied range are:

- PDF 59: **`நினைக்கிறேன்`**;
- PDF 69: **`வீசும்`**.

PDF 71 also received the separately resolved source form **`மாறினான்`**.

### Reconciliation status after Correction 005

The canonical corrections in this campaign post-date existing scene, dialogue, character and translation derivatives. Those downstream layers therefore cannot be assumed synchronized merely because they were previously marked complete/verified.

**Reconciliation is intentionally deferred until the user's final 075–080 correction batch is applied.** After that batch, the archive must:

1. reconcile all user-approved correction decisions against live canonical pages, especially pages 51–55 and the overlapping page 75;
2. identify affected scene derivatives and update them from canonical text;
3. reconcile affected dialogue records while preserving stable IDs/provenance and exact corrected speaker labels;
4. re-evaluate character exact-label metadata only where speaker-label corrections affect it;
5. recheck any affected song/performance links;
6. verify any translation records touching changed source text;
7. rerun relevant counts/consistency checks and synchronize work/project metadata.

Until that reconciliation passes, English translation expansion is paused.

## Downstream effect of Corrections 001–004

- `scene-034.md` was generated after Correction 001 and therefore already follows the corrected PDF 49–50 labels.
- `scene-035.md` has been reconciled so its PDF 53 portion now carries the restored `ராசா:` labels.
- `scene-036.md` was generated only after Correction 002 and begins with the restored T036 stage-direction form.
- `scene-040.md` was generated only after Correction 003 and therefore preserves the exact alternating `ராஜா:` / `ராசா:` labels across PDF 58–59.
- `scene-047.md` is generated only after Correction 004 and therefore carries the source-visible `ராசா:` continuation on PDF 66.

The earlier derivative synchronization statements above do **not** automatically cover Correction 005. Correction 005 requires the dedicated reconciliation described above.

No review page is promoted merely by these spelling/glyph corrections. The bounded source limitations remain:

- verified source pages: **75/79**;
- review source pages: **4/79 — PDF 27, 48, 57, 74**;
- verified screenplay pages: **66/70**;
- review screenplay pages: **4/70**.
