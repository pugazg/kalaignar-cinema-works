# பராசக்தி — Tamil fidelity audit

Source: `TVA_BOK_0062968_பராசக்தி.pdf`  
SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`

This ledger records the second-pass visual comparison of the canonical Tamil draft against the scan. The scan alone controls corrections. Film subtitles, web quotations, later transcriptions, and memory are not used to repair the text.

## Audit procedure

For each PDF page:

1. compare the entire transcribed page against the scan, including headings, speaker labels, stage directions, dialogue, verse lineation, punctuation, and page continuity;
2. record every clear mismatch or omission;
3. keep genuinely damaged/unclear source text unresolved rather than guessing;
4. apply accumulated corrections to the canonical part in a consolidated rewrite after that part's audit;
5. only then change the canonical page anchor from `draft` to `review` or `verified`.

## Part 01 — PDF 4–35 / printed pp. 3–34

Four visual-audit batches covered PDF 4–35. The consolidated Part 01 application restored the omitted PDF 7 `காட்சி—3` block and PDF 12 lyric stanza, applied all recorded source-form corrections, and resolved ten uncertainty markers directly from the scan.

Part 01 result:

- **30 verified pages**
- **2 review pages: PDF 5 and PDF 16**
- PDF 5 retains the damaged short span in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?`
- PDF 16 retains the unclear word before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

Those two readings are not repaired from external versions.

## Batch 5 — PDF 36–43 / printed pp. 35–42

Visual comparison completed for all eight pages. Four first-pass uncertainty markers were resolved directly from the scan:

- PDF 36: `சேர்மையா`
- PDF 37: `ஒரு அரையணா`
- PDF 40: `பாலைவனத்தை பூஞ்சோலையாக்க`
- PDF 41: `சுட்டுக் கொல்லப்பட்டிருப்போம்`

PDF 42's Gnanasekaran refugee/beggar-conference speech was identified as materially corrupted in the first pass and marked for direct source-led retranscription.

## Batch 6 — PDF 44–51 / printed pp. 43–50

Visual comparison completed for all eight pages. Two additional uncertainty markers were resolved on PDF 50:

- `சூறையாட`
- `அணைப்பிலே`

Direct block retranscription was required for PDF 44, 45, 46, 48 and 49 because the first-pass prose was materially corrupted despite a readable scan. `காட்சி—48` on PDF 49 was confirmed in its anomalous printed position and retained.

## Batch 7 — PDF 52–57 / printed pp. 51–56

Visual comparison completed for all six final canonical pages. PDF 52–54, containing the continuation of Gunasekaran's courtroom defence, were added to the direct-retranscription set because the first-pass wording was materially corrupted. PDF 55–57 required smaller source-form corrections. Final `காட்சி—43` on PDF 57 was visually confirmed and retained after scenes 46 and 47.

No new genuinely unreadable Part 02 source span was found in Batches 5–7.

## Consolidated Part 02 application

The completed Batch 5–7 ledger was applied in one controlled rewrite of `transcription/parts/part-02-pdf-36-57.md`.

Applied:

- all recorded Part 02 source-form corrections;
- direct scan-led retranscription of the materially corrupted blocks on **PDF 42, 44, 45, 46, 48, 49, 52, 53 and 54**;
- replacement of all six Part 02 uncertainty markers resolved from the scan;
- preservation of the printed scene-order anomalies, including `காட்சி—48` on PDF 49 and final `காட்சி—43` on PDF 57;
- promotion of all **22 Part 02 page anchors to `verified`**;
- retention of PDF 58 as `paratext`, outside the canonical dialogue/song pagination.

A post-rewrite repository check confirmed the Part 02 anchor sequence PDF 36–57, zero remaining Part 02 uncertainty markers, and the required scene-order boundaries.

## Current cumulative state

- Canonical Tamil coverage: **PDF 4–57 / printed pp. 3–56**
- Full canonical visual audit: **complete**
- Part 01: **30 verified / 2 review**
- Part 02: **22 verified / 0 review**
- Total canonical pages: **52 verified / 2 review**
- Remaining explicit source uncertainties: **2**, both in Part 01 (PDF 5 and PDF 16)
- Part 02 resolved markers pending apply: **0**
- Part 02 corrections applied: **yes**
- English translation remains blocked for the two `review` pages; verified pages are eligible under the repository's translation gate.

No further fidelity-audit page remains in this scan. The two Part 01 uncertainties should remain explicit unless stronger source evidence becomes available.
