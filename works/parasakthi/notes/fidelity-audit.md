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

## Batch 2 — PDF 12–19 / printed pp. 11–18

Visual comparison completed for all eight pages directly against the scan.

| PDF | Printed | Audit result | Findings |
|---:|---:|---|---|
| 12 | 11 | substantive correction-needed | The draft omits an entire lyric stanza at the top of the page, beginning `கற்றிலும் சித்திரமும் கண்டு—அதன்` and ending `அளிக்கும் கலைகள் அறிவோம்`, before the existing `வானுலக மோட்சமதை நாடி—இன்ப` stanza. Additional clear corrections include source `ஆணவத்தினிலே` vs draft `ஆணவத்திலே`, source `இனிக்கும் விதத்தில் சுகம்` vs draft `வித்தத்தில்`, and the stage direction's `தன் பணத்தை பூராவும் பறிகொடுக்கிறான்` vs draft `சூறாவும்`. |
| 13 | 12 | correction-needed; two uncertainties resolved | The two marked readings are legible in the enlarged scan as `பஞ்சையாய்...பராரியாய்`. The source continues `என் தங்கைக்கு`, not draft `ஏன் தங்கைக்கு`. Other clear source forms include `வீதிகளிலே`, `இதுதானு`, and `ஊமையாய்`, which differ from the current draft. |
| 14 | 13 | correction-needed | The auction notice prints `என்னவென்றால்` as one word; the draft has `என்ன வென்றால்`. In the following conversation the scan reads the colloquial `ஆனுங்களோ?`, not draft `ஆனாங்களோ?`. Scene headings and song placement match. |
| 15 | 14 | correction-needed | The scan reads `நான் சொல்வதைக் கேளு`; the draft has `சொல்லுவதைக்`. It also prints `நடக்க வேண்டியதுதானே நடக்கும்` as a continuous form rather than the draft's separated `வேண்டியது தானே`. The remainder of the page follows the draft's sequence. |
| 16 | 15 | review / one source uncertainty remains | The marked `⟦சேப்பு?⟧` is clearly `சோப்பு` in the scan. The source also has `இல்லே எம்ப்டி பாக்கெட்`, not draft `இல்ல எம்ப்டி பாக்கெட்`. The later marked word before `தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்` remains too ambiguous in this scan to replace confidently, so that uncertainty is retained. |
| 17 | 16 | correction-needed; one uncertainty resolved | The marked phrase is legible as `நல்லவன், நாதியற்றவனை`. The scan also reads `உடுத்த மாற்றுத் துணியில்லை` where the draft has `உடுக்க`, and `வாடிக்கைக்காரங்க` where the draft has `வாடிக்கைகாரங்க`. |
| 18 | 17 | correction-needed; one uncertainty resolved | The stage-direction marker `⟦கேளாமலேயே?⟧` resolves to `கேளாமலேயே`. Other clear source forms include `பரவாயில்ல`, `நாலு அணாவுக்கு`, `தானப்பா`, `காசில்லையா?`, and `பாழாப் போனவனே`, all differing from the current draft in small but source-significant ways. |
| 19 | 18 | correction-needed; one uncertainty resolved | The marked phrase is clearly `வித்தாத்தானே வீணுப்போனவனே?`. The remainder of the page follows the first-pass sequence closely; one small source-form difference is `(மைனர்கள் கொடுத்துவிடுகின்றனர்)` rather than the draft's separated `கொடுத்து விடுகின்றனர்`. |

### Substantive omission on PDF 12

PDF 12 contains a full lyric stanza before the stanza currently beginning the draft page. This is the second substantive first-pass omission found during the fidelity audit. It is not a page-order issue: the omitted stanza is visibly part of the same song begun on PDF 11 and must be restored at the start of the PDF 12 source anchor during the consolidated part-01 correction.

### Uncertainty resolution in Batch 2

Six existing uncertainty markers can now be resolved directly from the scan when the canonical part is rewritten:

- PDF 13: `பஞ்சையாய்`
- PDF 13: `பராரியாய்`
- PDF 16: `சோப்பு`
- PDF 17: `நல்லவன், நாதியற்றவனை`
- PDF 18: `கேளாமலேயே`
- PDF 19: `வித்தாத்தானே வீணுப்போனவனே?`

One marked reading on PDF 16 remains unresolved after enlarged inspection. Together with the earlier source-damaged span on PDF 5, there are currently **two known unresolved readings within the already-audited pages**. This does not yet change the canonical draft's stored count of 19 markers because no consolidated rewrite has been applied.

## Batch 3 — PDF 20–27 / printed pp. 19–26

Visual comparison completed for all eight pages directly against the rendered scan.

| PDF | Printed | Audit result | Findings |
|---:|---:|---|---|
| 20 | 19 | correction-needed; one uncertainty resolved | The marked line is legible as `ஈசனும் ஈசனார் பூசையும் தேசத்தில்`. Other clear corrections include source `சாட்சி கோர்ட்டு ஏறாதடி` vs draft `ஏறுதடி`, source `இல்லா தவனை` vs draft `இல்லாதவன்`, source `முட்டாபயலையெல்லாம்` vs draft `முட்டாப்பயலெல்லாம்`, and source `நான் பிச்சைக்காரனில்லை` vs draft `பிச்சைக்காரனில்லே`. |
| 21 | 20 | correction-needed | Clear source forms include `அவுங்க அப்பாதானே?`, `அவளையும் வாழ விடலே`, `அவளை சிசுவும் கையுமா விதவையாக்கிருச்சி`, `துயரப்படுறியே`, and `கல்யாணியைத் தேட`. The `காட்சி 17` direction has `இதப் பார்த்துக்கொண்டே` and `நெஞ்சைத் துளைக்கும்`, and the lullaby line reads `யானையும் வாகனமாய்—சின்ன`, not draft `பாண்டமும்`. |
| 22 | 21 | correction-needed; two uncertainties resolved | The source reads `வெள்ளியினால் செய்த ஏட்டில்` and `பாடம் எழுத உனை`, not draft `வெள்ளியினில்` / `உன்`. In `காட்சி-18`, the marked readings resolve as `லாண்டறியே` and `டேபின்`. Other clear corrections include source `தான் ஆட்டத்துக்கு வர்லே`, `ஏது ஆள் அவுட்டா`, and `ஒன்கிட்டே`. |
| 23 | 22 | correction-needed; one uncertainty resolved | Source corrections include `அங்கே வர்றியா`, `கற்பித்தானா?`, `மந்திரி பிரதானீகளே`, `இசைக்குயில் போல்`, `கடக்கட்டு`, and `பரதேசிப் பசங்களா`. The longer marked span resolves as `சஞ்சீவி நாம பர்வதம்`. The end verse block otherwise follows the draft sequence. |
| 24 | 23 | correction-needed | The source has `(இவ்வாறாக...)`, `இங்கே வாயேன்`, `பெத்து தர்றேன்`, `கட்டிக்கிறாயா?`, `முதல்லே`, `தர்றேன்`, and `சத்தியமா`, where the draft has smaller source-form errors. The scene direction prints `(இடம்ரோடு)`, and the road dialogue includes `கொடப்பா` and `நடக்கும்லே?`. |
| 25 | 24 | correction-needed | Clear source forms include `காசு எடப்பா`, `ஏனப்பா`, `திமிறுபடைச்சவன்`, `எடுன்னா`, `விளையாடுறே`, `பாக்றயா`, `யாருனு`, `அப்படின்னா`, `ரெண்டணாவுக்குக் கொடு`, `ஏங்க உங்களுக்கு`, and `பிட்டுக் கொடுக்கிறான்`, all differing from the draft. |
| 26 | 25 | correction-needed | The source reads `நழுவ விடுவாயோ—ஏதுங்காணும் இந்தக் காசு?`, `ஏதுங் காணும்`, `எய்ட் நாட்திரீ`, `கொட்டாபுளியை`, `தூக்கவிட மறுத்தல்`, and `தலையின்மீது`. In `காட்சி 21`, the scan has `ஏண்ணா இவ்வளவு நாழி?`, `இருக்குல்லே?`, `இருங்கண்ணா! கொண்டு வர்றேன்`, `போடாமல்`, `இரண்டாக`, `கலந்துகிட்டால் லாபமும்`, repeated `அண்ணா`, and `பாவியானேன்`. |
| 27 | 26 | correction-needed | The page continues the `அண்ணா` source form. Other clear corrections include `பலாமரமாக`, source spelling `மாழி`, `தானும் அப்படித்தான்`, `கந்தல்பாயிலே`, and `வஞ்சக வலைவீசினால் விழுவார்கள்`. The rescue dialogue has `மைத்துனு`, `நீ வரலின்னா`, repeated `கிறுக்கண்ணா`, `இட்லி தர்றேன்`, `கேட்பியே`, and `சொன்னா`, not the draft's corresponding forms. |

### Uncertainty resolution in Batch 3

Four additional existing uncertainty markers can now be resolved directly from the scan when `part-01-pdf-4-35.md` is rewritten:

- PDF 20: `ஈசனார்`
- PDF 22: `லாண்டறியே`
- PDF 22: `டேபின்`
- PDF 23: `சஞ்சீவி நாம பர்வதம்`

No new unresolved source reading was identified in PDF 20–27 during this pass.

## Cumulative audit state

- Pages visually compared: **PDF 4–27 / printed pp. 3–26**
- Total audited pages: **24**
- Clean pages so far: **PDF 8, 10**
- Substantive first-pass omissions found: **PDF 7 (`காட்சி—3` opening block), PDF 12 (lyric stanza)**
- Uncertainty markers resolved from the scan but pending canonical rewrite: **10**
- Known unresolved readings within audited pages: **PDF 5 and PDF 16**
- Canonical part has **not yet been rewritten**; all source anchors in part 01 remain `draft` until the accumulated corrections are applied together.
- Next audit page: **PDF 28 / printed p. 27**
