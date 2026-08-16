# மனோகரா — Tamil fidelity audit

Source: `TVA_BOK_0010102_மனோகரா.pdf`  
SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`

This ledger records the second-pass visual comparison of the canonical Tamil first-pass transcription against the rendered scan. The scan is the textual authority. OCR, film audio, subtitles, web quotations, memory and later editions are navigation or comparison aids only and are not used to silently repair the canonical text.

## Audit procedure

For each PDF page:

1. compare the complete stored page against the rendered scan, including headings, speaker labels, stage directions, dialogue, performance labels, punctuation and page continuity;
2. record every clear mismatch, omission or source-form normalization;
3. leave genuinely unclear source readings unresolved rather than guessing;
4. accumulate corrections for the active transcription part and apply them in a consolidated source-led rewrite after that part has been fully audited;
5. only after the corrections are applied may the affected page anchors move from `draft` to `review` or `verified`.

## Batch 1 — PDF 7–12 / logical printed pp.6–11

Visual comparison completed for all six pages. The first-pass text is substantially usable, but the scan exposes several source-form corrections and one omitted spoken phrase. No genuinely unreadable source span was found in this batch.

The following corrections are **recorded but not yet applied** to `transcription/parts/part-01-pdf-7-30.md`:

| PDF | Printed | First-pass reading | Scan-supported reading / disposition |
|---:|---:|---|---|
| 7 | logical 6 | `நடத்திக்கொண்டே இருக்கின்றன.` | `நடத்திக்கொண்டே யிருக்கின்றன.` |
| 7 | logical 6 | `கண்டுபிடித்த மருந்து` | `கண்டு பிடித்த மருந்து` |
| 8 | 7 | laughter normalized as `ஹா ஹா ஹா` | retain source form `ஹ ஹ ஹ` with source punctuation |
| 8 | 7 | `ஏன் செதுக்கலேன் இவளை!` | `ஏன் செதுக்குகிறேன் இவளை!` |
| 9 | 8 | `சந்தேகமில்லை` in the Vasanthan/Vikatan exchange | source repeatedly prints `சந்தேகமில்லே` |
| 9 | 8 | `(வசந்தன் ; விகடன் சந்தேகமில்லை பாட்டு)` | `(வசந்தன் ; விகடன் சந்தேகமில்லே பாட்டு)` |
| 9 | 8 | `எழில் திரு நம் செல்வத்தை` | `எழில் பூத்த நம் செல்வத்தை` |
| 10 | 9 | `அவசரமாகப் புறப்படுகிறாய்?` | `அவசரமாகப் புறப்பட்டு இருப்பாய்?` |
| 10 | 9 | stage direction uses `முத்தாரத்திலுள்ள` | source separates the phrase as `முத்தாரத்தில் உள்ள` |
| 11 | 10 | `[வந்துகொண்டே வசந்தனைத் தொடுகிறான்]` | `[வந்துகொண்டே வசந்தாவைத் தொடுகிறான்]` |
| 11 | 10 | `சுட்டுவிடும் தேகா!` | `சுட்டுவிடும் தேகம்!` |
| 11 | 10 | `சந்தேகமில்லை...சந்தேகமில்லை` | `சந்தேகமில்லே...சந்தேகமில்லே` |
| 11 | 10 | `பிள்ளையாரு மாத்திரம் கேட்ட அம்மா பார்வதியைப் போல பெண்ணு! என்னாப்பா...` | restore the source-visible wording: `பிள்ளையாரு மாத்திரம் கேட்டாரா, அவுங்க அம்மா பார்வதியைப் போல பெண்ணு! நான் கேட்டா என்னப்பா...` |
| 12 | 11 | — | no clear textual mismatch requiring correction was found in this page during this batch |

### Batch 1 disposition

- pages visually audited: **6**;
- audited range: PDF **7–12** / logical printed pp. **6–11**;
- clear correction groups recorded: **13**;
- unresolved source readings: **0**;
- corrections applied to canonical Part 01: **no — intentionally deferred until the active part is fully audited**;
- verified page anchors: **0**;
- review page anchors: **0**;
- next visual-audit page: **PDF 13 / printed p.12**.

## Current cumulative state

- canonical Tamil range: **PDF 7–88 / logical printed pp.6–87 — 82 pages**;
- first pass: **82/82 complete (`draft-complete`)**;
- visual audit completed through: **PDF 12 / logical printed p.11**;
- visually audited pages: **6/82**;
- canonical corrections pending consolidated application: **yes**;
- verified canonical pages: **0**;
- review canonical pages: **0**;
- structured derivatives: **blocked**.

**Next:** continue the visual fidelity audit with **PDF 13–18 / printed pp.12–17**, remaining within Part 01. Do not promote any Part 01 page anchor until the accumulated Part 01 corrections have been applied to the canonical transcription.
