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

Visual comparison completed for all eight pages. See repository history for the full per-page correction list. The consolidated Part 01 rewrite applied all recorded corrections; PDF 5 alone retains a source uncertainty in this batch.

## Batch 2 — PDF 12–19 / printed pp. 11–18

Visual comparison completed for all eight pages. The omitted PDF 12 lyric stanza was restored; six marked readings were resolved. PDF 16 retains one genuine source uncertainty.

## Batch 3 — PDF 20–27 / printed pp. 19–26

Visual comparison completed for all eight pages. Four additional uncertainty markers were resolved directly from the scan and the recorded source-form corrections were applied.

## Batch 4 — PDF 28–35 / printed pp. 27–34

Visual comparison completed for all eight pages. No new uncertainty marker was introduced.

## Consolidated Part 01 application

The accumulated corrections for **PDF 4–35 / printed pp. 3–34** have been applied to `transcription/parts/part-01-pdf-4-35.md` in one controlled rewrite.

Applied in that rewrite:

- all recorded Batch 1–4 source-form corrections;
- restoration of the omitted PDF 7 `காட்சி—3` opening block directly from the scan;
- restoration of the omitted PDF 12 lyric stanza directly from the scan, with opening `கற்சிலையும் சித்திரமும் கண்டு—அதன்`;
- replacement of all ten uncertainty markers resolved during the audit;
- retention of the two genuinely unresolved readings on PDF 5 and PDF 16;
- page-anchor promotion to `verified` for 30 pages and `review` for PDF 5 and PDF 16.

## Batch 5 — PDF 36–43 / printed pp. 35–42

Visual comparison completed for all eight pages directly against enlarged renders of the source scan. Part 02 remains unchanged in this checkpoint; these findings are recorded for its later consolidated rewrite.

| PDF | Printed | Audit result | Findings |
|---:|---:|---|---|
| 36 | 35 | correction-needed; uncertainty resolved | The existing marked reading `⟦சேர்மையா?⟧` is legible in context as `சேர்மையா`. Clear source-form corrections include `தர்மம் தலைகாக்கும்னு` (draft `தானம்...`) and the surrounding Narayanapillai / Gunasekaran exchange must be brought back to the printed wording without normalization. |
| 37 | 36 | correction-needed; uncertainty resolved | In `காட்சி—32`, the marked amount is clearly `ஒரு அரையணா`; the first-pass `⟦ஒரு அணையணு?⟧` is erroneous. The preceding Vimala/Gunasekaran dialogue also contains small source-form differences to apply. |
| 38 | 37 | correction-needed | `காட்சி 33` was compared in full. Several first-pass lexical forms differ from the scan in Gunasekaran's account and Vimala's reply; no genuinely unreadable source span was found on this page. |
| 39 | 38 | correction-needed | Clear corrections include source `திருமாலுக்கு திருவிழா` where the draft has `திருமணுக்கு திருவிழா`, and source `மோகன வாழ்வு` where the draft has `மோசன வாழ்வு`. The remainder of the argument contains additional source-form corrections but no unresolved scan reading. |
| 40 | 39 | correction-needed; uncertainty resolved | The marked phrase resolves clearly from the scan as `பாலைவனத்தை பூஞ்சோலையாக்க`; the draft's `⟦பாக்குவனத்தை?⟧ பூஞ்சோலையாக` is not source-faithful. The dream lyric and surrounding dialogue were visually checked; smaller spelling/spacing corrections remain for consolidated application. |
| 41 | 40 | correction-needed; uncertainty resolved | The marked long reading in Gnanasekaran's refugee-camp speech is legible as the printed `சுட்டுக் கொல்லப்பட்டிருப்போம்` in context. The page contains several colloquial/source-form differences that must be retained exactly in the consolidated rewrite. |
| 42 | 41 | substantive correction-needed | The first-pass transcription of Gnanasekaran's long speech is materially corrupted in places. The scan clearly includes `பிச்சைக்காரர்கள் நாம்மட்டு மல்ல இந்தநாடு பூராவுமே பரந்துகிடக்கின்றனர்` and a coherent sequence about uniting beggars, holding a conference, passing resolutions, and making the government hear their demands. This page requires direct source-led retranscription of the affected paragraph rather than piecemeal word replacement. `காட்சி—35` begins at the bottom of the page. |
| 43 | 42 | correction-needed | The continuation of `காட்சி—35`, `காட்சி—36`, and opening of `காட்சி—37` were visually checked. The scene sequence is correct; several small colloquial/source-form corrections are required, but no new unresolved source reading was identified. |

### Batch 5 uncertainty resolution

Three existing Part 02 uncertainty markers can be resolved directly from the scan during the consolidated Part 02 rewrite:

- PDF 36: `சேர்மையா`
- PDF 37: `ஒரு அரையணா`
- PDF 40: `பாலைவனத்தை பூஞ்சோலையாக்க`

The marked PDF 41 reading `சுட்டுக் கொல்லப்பட்டிருப்போம்` is also visually confirmed and can lose its uncertainty notation.

PDF 42 is the important fidelity finding in this batch: because a substantial paragraph is textually corrupted rather than merely misspelled, it must be retranscribed directly from the page image during application.

## Current cumulative state

- Pages visually compared: **PDF 4–43 / printed pp. 3–42**
- Part 01: **audit complete; corrections applied — 30 verified / 2 review**
- Part 02 audited so far: **PDF 36–43 / printed pp. 35–42**
- Part 02 canonical corrections: **not yet applied**
- Part 02 uncertainty markers visually resolved in Batch 5: **4**
- New unresolved source readings found in Batch 5: **0**
- Substantive Part 02 retranscription required: **PDF 42 / printed p.41 paragraph**
- Next fidelity-audit page: **PDF 44 / printed p.43**
- Continue auditing Part 02 before doing its consolidated rewrite.
