# நாம் — visual-fidelity + final historical-glyph verification audit — PDF 10–14

Source: `TVA_BOK_0064201_நாம்.pdf`  
Range: **PDF 10–14**  
Audit mode: **dual gate — rendered-pixel lexical fidelity + occurrence-specific historical-glyph verification**  
Result: **PDF 11–14 PASS / VERIFIED; PDF 10 HOLD; 4/5 dual-gate verified**.  
**Final amendment:** the held page was subsequently resolved by the user's manual controlling-scan verdict; final batch status is **5/5 VERIFIED**.

The rendered scan is controlling. No OCR, film audio, subtitles, later edition, web text or semantic reconstruction is used as textual authority.

## PDF 10 — HOLD — INITIAL HOLD, SUPERSEDED

The page was reviewed at enlarged/native resolution. Most of the page is directly readable, but the physical right edge of the Malaiyappan speech is missing. The source positively preserves only the beginning of the damaged word through:

`நீ இங்கே வேலை பார்க்கிற வரைக்…`

The missing ending is **not** reconstructed as `வரைக்கும்` or any other expected form. This physical loss is now an explicit source uncertainty, so PDF 10 remains `needs-review` despite the remainder of the page being reconciled.

Scan-backed corrections include:

- `மகனுடை குலாவுறே?` → **`மகனோடே குலாவுறே?`**;
- source speaker abbreviation **`மல்`** is preserved rather than expanding it to `மல்ல`;
- `வேலைக்காரன்—வேலைக்காரன் தான்!` → **`வேலைக்காரன்—வேலைக்காரன்தான்!`**;
- `மறு புறம்` → **`மறுபுறம்`**.

Historical-glyph final review: **PASS** for all surviving/visible clusters. The hold is physical lexical loss at the page edge, not an unresolved historical-glyph identity.

## PDF 11 — PASS / VERIFIED

Complete visual comparison exposed several source-fidelity corrections:

- `வேலையப்பாரு!` → **`வேலையைப்பாரு!`**;
- expanded speaker label `மல்ல` → source **`மல்`**;
- `பாசம் கூடாது என்று` → source-colloquial **`பாசம் கூடாதுன்னு`**.

The source punctuation inside `(கண்ணாடிச் சாமான்கள் உடைந்திருப்பதைக் கண்டு . கடுஞ்சினம் கொண்டு)` is retained rather than normalized away.

Historical-glyph final review: **PASS**, including the positive `ணா`-family occurrence in `கண்ணாடிச்`.

Dual gate: **VERIFIED**.

## PDF 12 — PASS / VERIFIED

Scan-backed corrections:

- `அய்யா இல்லே...` → **`அப்பா இல்லே...`**;
- `எங்கள் புலியா மாத்துறுங்க` → **`எங்களை புலியா மாத்துறுங்க`**;
- `இதோ கூப்பிட்றேன் ஏ அய்யோ...` → **`இதோ கூப்பிட்றேன் ஏ அப்பா...`**;
- `இல்லை.` → **`இல்லே.`**;
- `இப்போ இல்லை.` → **`இப்போ இல்லே.`**;
- `அப்பறம் வாய்யா!` → **`அப்புறம் வாய்யா!`**.

The unusual source-visible `தளிர்ச்சிருக்கே` is preserved exactly; it is not modernized.

Historical-glyph final review: **PASS** after complete page-level family inspection.

Dual gate: **VERIFIED**.

## PDF 13 — PASS / VERIFIED

The first pass contained multiple normalization/substitution errors and one omitted stage direction. Direct scan comparison establishes:

- `என்ன பிரேமா` → **`ஏன் பிரேமா`**;
- `அந்தத் கீல்வலிக்கார` → **`அந்தக் கீல்வலிக்கார`**;
- `அது இல்லைய்யா!` → **`அது இல்லேப்பா!`**;
- omitted **`(மாத்திரை போகிறான்)`** restored;
- `நல்ல வேள` → **`நல்ல வேளை`**;
- `இல்லேன்னா` → **`இல்லேன்னு`**;
- `எனக்காக வரவில்லை!` → **`எனக்காக வரவில்லே!`**;
- `என்னை அடிச்ச ஜமீன்தார் கை...` → **`என்னை அடிச்சதிலே ஜமீன்தார் கை...`**;
- `உங்கள் கிட்டிட்டு போக வந்தேன்` → **`உங்களை கூட்டிட்டு போக வந்தேன்`**;
- `வரேன்` → **`வர்றேன்`**;
- source speaker abbreviation **`மல்`** is retained in `காட்சி 5`.

Historical-glyph final review: **PASS**. Source colloquial vocabulary is preserved without modernization.

Dual gate: **VERIFIED**.

## PDF 14 — PASS / VERIFIED

Direct source comparison confirms the unusual repeated **`வாலாம்`** reading and corrects three substantive first-pass substitutions:

- `ஹூ...ஹூம்...` → **`ஹா...ஹூம்...`**;
- `அந்த உயிரிலே மட்டும்` → **`அந்த உயிரை மட்டும்`**;
- `சங்கீதம் பாடாதீர்கள்!` → source **`சங்கேதப் படாதீர்கள்!`**.

The last correction is especially important: the source says `சங்கேதப் படாதீர்கள்`; it must not be silently normalized into a musically meaningful phrase.

Historical-glyph final review: **PASS** after page-level inspection of the mandatory families.

Dual gate: **VERIFIED**.

## Batch result

| PDF | Visual fidelity | Historical glyph final | Dual-gate status | Open uncertainty |
|---:|---|---|---|---:|
| 10 | HOLD — physical right-edge loss | PASS | needs-review | 1 |
| 11 | PASS after correction | PASS | VERIFIED | 0 |
| 12 | PASS after correction | PASS | VERIFIED | 0 |
| 13 | PASS after correction | PASS | VERIFIED | 0 |
| 14 | PASS after correction | PASS | VERIFIED | 0 |
| **Total** | **4 PASS + 1 HOLD** | **5 PASS** | **4 VERIFIED** | **1** |

Repository-wide checkpoint after synchronization should therefore be:

- canonical first pass: **67/67 COMPLETE**;
- visual-fidelity passed: **8/67**;
- historical-glyph final verified: **10/67**;
- dual-gate canonical verified: **8/67**;
- needs review: **59/67**;
- open source uncertainties: **2** — PDF 5 damaged introductory beginning and PDF 10 damaged right-edge word ending.

## Next activity

Proceed with the separate visual-fidelity and final historical-glyph verification audit for **PDF 15–19**. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen PDF 6–9 or PDF 11–14 absent genuinely new direct-source evidence. PDF 5 and PDF 10 remain explicit physical-source-damage holds. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete.


## Final user-manual source closure amendment

On 2026-09-08, the user manually inspected the controlling scan and supplied the exact reviewed reading for PDF 10: **`நீ இங்கே வேலை பார்க்கிற வரைக்கும்`**. Under the binding cinema-work processing guide, this manual source verdict supersedes the earlier assistant-side inability to recover the obscured characters. PDF 10 is now **VERIFIED**, this batch is **5/5 dual-gate VERIFIED**, and the current whole-work status is recorded in `canonical-closure-user-manual.md`.
