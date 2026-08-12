# பராசக்தி — Tamil fidelity audit

Source: `TVA_BOK_0062968_பராசக்தி.pdf`  
SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`

This ledger records the second-pass visual comparison of the canonical Tamil draft against the scan. The scan alone controls corrections. Film subtitles, web quotations, later transcriptions, and memory are not used to repair the text.

## Audit procedure

For each PDF page:

1. compare the entire transcribed page against the scan, including headings, speaker labels, stage directions, dialogue, verse lineation, punctuation, and page continuity;
2. record every clear mismatch or omission;
3. keep genuinely damaged/unclear source text unresolved rather than guessing;
4. apply accumulated corrections to the canonical part in a consolidated rewrite after that part's audit, avoiding repeated large-file rewrites;
5. only then change the canonical page anchor from `draft` to `review` or `verified`.

## Batch 1 — PDF 4–11 / printed pp. 3–10

Visual comparison completed for all eight pages.

| PDF | Printed | Audit result | Findings |
|---:|---:|---|---|
| 4 | 3 | correction-needed | In the opening speech, the scan reads `இந்த மண் மாதாவின் மடியிலே`; the draft has `மடியில்`. No additional unresolved scan reading identified on this page in this pass. |
| 5 | 4 | review / source uncertainty remains | Clear draft error: `விண்ணியாண்டுகிட்டு` must be `விளையாண்டுகிட்டு`. The existing short uncertainty in `கல்யாணிக்குக் கல்யாணம் ⟦?⟧ தெரியுமா?` remains unresolved: the intervening letters are damaged/blurred in this scan and are not safe to infer. |
| 6 | 5 | correction-needed | The scan prints `இல்ல...ஒங்க அப்பா படத்தைப் பார்த்தவுடன்`; the draft has `இல்லை...`. Other text on the page was visually compared without a new unresolved span. |
| 7 | 6 | substantive correction-needed | The parenthetical after the gift-packing instruction reads `(ஞான சேகரன் வருந்துகிறான்)`; the draft has `வந்துகிறான்`. More importantly, the draft omits the printed `காட்சி—3` heading and its complete opening block at the bottom of the page. This block must be restored from the scan before the page can be verified. |
| 8 | 7 | clean in this pass | Continuation of `காட்சி—3`, `காட்சி—4`, its duet, and the opening of `காட்சி—5` visually match the draft. |
| 9 | 8 | correction-needed | At the end of the page the scan line-breaks the form corresponding to `போயிட்டுத்தான் வரட்டுமே`; the draft currently separates it as `போயிட்டு தான் வரட்டுமே`. |
| 10 | 9 | clean in this pass | `காட்சி—7` opening and the page's dialogue/stage directions visually match the draft; no new unresolved span identified. |
| 11 | 10 | correction-needed | The first stage direction is feminine in the scan: `தவறியவள் நான் தான் (உடனே வெளியேறுபவள் போல் பாவனை செய்கிறாள்)`; the draft has masculine/neutral forms. The scan also has `உம்...வேண்டாம்...தேங்க்ஸ்` where the draft has `ம்...`, and the lyric reads `இனிக்கும் விதத்தில் சுகம்`, not `வித்தத்தில்`. |

### Substantive omission on PDF 7

The scan visibly contains a `காட்சி—3` heading after the end of the Rangoon conversation. It begins with the stage direction showing கல்யாணி in wedding dress, crying before a mirror, followed by her lament about her absent brothers and replies from பார்வதி and மாணிக்கம். The current first-pass draft jumps directly from PDF 7's preceding dialogue to the continuation on PDF 8, so this is a genuine first-pass omission rather than a scene-numbering anomaly.

The missing block will be transcribed directly from the scan during the consolidated correction of `part-01-pdf-4-35.md`; any word that cannot be read confidently will receive the repository's explicit uncertainty notation.

## Batch 1 state

- Pages visually compared: **PDF 4–11 / printed pp. 3–10**
- Pages in batch: **8**
- Clean in this pass: **PDF 8, 10**
- Corrections/omission recorded: **PDF 4, 5, 6, 7, 9, 11**
- Existing source-damaged uncertainty still unresolved in this batch: **PDF 5**
- Canonical part has **not yet been rewritten**; page anchors therefore remain `draft` until the accumulated corrections are applied.
- Next audit page: **PDF 12 / printed p. 11**
