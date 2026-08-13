# பராசக்தி — Tamil fidelity audit

Source: `TVA_BOK_0062968_பராசக்தி.pdf`  
SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`

This ledger records the second-pass visual comparison of the canonical Tamil draft against the scan. The scan controls textual corrections. Film subtitles, web quotations, later transcriptions, and memory are not used to repair the text.

## Audit procedure

For each PDF page:

1. compare the entire transcribed page against the scan, including headings, speaker labels, stage directions, dialogue, verse lineation, punctuation, and page continuity;
2. record every clear mismatch or omission;
3. keep genuinely damaged/unclear source text unresolved rather than guessing;
4. apply accumulated corrections to the canonical part in a consolidated rewrite after that part's audit;
5. only then change the canonical page anchor from `draft` to `review` or `verified`.

## Part 01 — PDF 4–35 / printed pp. 3–34

Four visual-audit batches covered PDF 4–35. The consolidated Part 01 application restored the omitted PDF 7 `காட்சி—3` block and PDF 12 lyric stanza, applied all recorded source-form corrections, and resolved ten uncertainty markers directly from the scan.

Two short readings initially remained under review on PDF 5 and PDF 16. They were subsequently resolved by direct reviewer-assisted inspection of the same source scan:

| PDF | Printed | Previously unresolved | Resolved reading | Canonical context |
|---:|---:|---|---|---|
| 5 | 4 | `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?` | **`உங்களுக்குத்`** | `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?` |
| 16 | 15 | `குதிரைக்கு பதிலாக ⟦நாப்பு?⟧ தெறிக்கத்தெறிக்க...` | **`நரம்பு`** | `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...` |

Those readings were applied in commit `13b29064d01d606f64f2ae817b25008d21394f75`, and both page anchors were promoted from `review` to `verified`.

Final Part 01 result:

- **32 verified pages**
- **0 review pages**
- **0 remaining uncertainty markers**

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

Direct block retranscription was required for PDF 44, 45, 46, 48 and 49 because the first-pass prose was materially corrupted despite a readable scan.

The scan visibly prints `காட்சி—48` on PDF 49 / printed p.48. This was initially retained as a source anomaly during the fidelity pass. A later editorial numbering review established that this is the misplaced/misprinted scene 43; the canonical correction is documented below.

## Batch 7 — PDF 52–57 / printed pp. 51–56

Visual comparison completed for all six final canonical pages. PDF 52–54, containing the continuation of Gunasekaran's courtroom defence, were added to the direct-retranscription set because the first-pass wording was materially corrupted. PDF 55–57 required smaller source-form corrections.

The scan visibly prints `காட்சி—43` on PDF 57 / printed p.56 after scenes 46 and 47. This was initially retained as printed during the fidelity pass. A later editorial numbering review established that this is the final scene 48; the canonical correction is documented below.

No genuinely unreadable Part 02 source span remained after Batches 5–7.

## Consolidated Part 02 application

The completed Batch 5–7 ledger was applied in one controlled rewrite of `transcription/parts/part-02-pdf-36-57.md`.

Applied:

- all recorded Part 02 source-form corrections;
- direct scan-led retranscription of the materially corrupted blocks on **PDF 42, 44, 45, 46, 48, 49, 52, 53 and 54**;
- replacement of all six Part 02 uncertainty markers resolved from the scan;
- promotion of all **22 Part 02 page anchors to `verified`**;
- retention of PDF 58 as `paratext`, outside the canonical dialogue/song pagination.

## Post-rewrite corrective verification

The first consolidated Part 02 rewrite was followed by another enlarged visual check of the direct-retranscription pages and scene/page boundaries. That check found that several phrases in the first consolidated version—especially on **PDF 44–46 and PDF 52–54**—still did not reproduce the scan closely enough.

Those blocks were re-read directly from enlarged source renders and corrected in the canonical file. The final corrective Part 02 commit is:

`ac4828c60f9a69590f1fc6b2da17114f62c16d22`

The post-correction state has:

- **22 verified Part 02 page anchors**;
- **0 Part 02 uncertainty markers**;
- the nine source-led retranscription pages retained as PDF **42, 44, 45, 46, 48, 49, 52, 53, 54**;
- all page boundaries and the closing sequence rechecked.

## Editorial scene-number correction

The source itself remains fully documented, but the visible canonical copy corrects two scene-number misprints/transpositions:

| Location | Printed booklet | Canonical copy | Reason |
|---|---|---|---|
| PDF 49 / printed p.48 | `காட்சி—48` | **`காட்சி—43`** | It follows scene 42 and precedes scene 44. |
| PDF 57 / printed p.56 | `காட்சி—43` | **`காட்சி—48`** | It is the final scene after scenes 46 and 47. |

These are **not silent corrections**. Hidden HTML comments immediately before the two canonical headings retain the printed source readings, and `mapping.md` records both the source and canonical numbering.

## Final cumulative state

- Canonical Tamil coverage: **PDF 4–57 / printed pp. 3–56**
- Full canonical visual audit: **complete**
- Part 01: **32 verified / 0 review**
- Part 02: **22 verified / 0 review**
- Total canonical pages: **54 verified / 0 review**
- Remaining explicit source uncertainties: **0**
- Remaining canonical uncertainty markers: **0**
- Part 02 corrections applied: **yes**
- Part 02 post-rewrite corrective verification: **complete**
- Canonical scene-number corrections: **PDF 49 source 48 → canonical 43; PDF 57 source 43 → canonical 48**
- Tamil fidelity audit: **complete**
- English translation: **eligible to begin as a separate derivative activity**

No further Tamil fidelity-audit work remains for this scan.
