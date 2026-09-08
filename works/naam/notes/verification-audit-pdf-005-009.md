# நாம் — visual-fidelity + final historical-glyph verification audit — PDF 5–9

Source: `TVA_BOK_0064201_நாம்.pdf`  
Range: **PDF 5–9**  
Audit mode: **dual gate — rendered-pixel lexical fidelity + occurrence-specific historical-glyph verification**  
Result: **PDF 6–9 PASS / VERIFIED; PDF 5 HOLD; 4/5 dual-gate verified**.

The rendered scan is controlling. No OCR, film audio, subtitles, later edition, web text or semantic reconstruction is used as textual authority.

## PDF 5 — HOLD

The page was compared throughout against enlarged/native source pixels. The ordinary dialogue and narration are readable enough for source-level correction, but the first scene-introduction line remains physically damaged at the left edge. The surviving pixels support the visible tail:

`…னைத் கொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`

The missing initial characters are **not** reconstructed. The prior broad uncertainty marker is narrowed to this exact surviving evidence, but PDF 5 remains `needs-review` and cannot be called verified while the damaged beginning is unresolved.

Scan-backed corrections:

- `கொண்டாட்டம் ஒன்றுமில்லையப்பா...` → **`கொண்டாட்டம் ஒண்ணுமில்லையப்பா...`**;
- `அதனால் மாரியாத்தாளுக்கு பூஜை நடத்துகிறோம்.` → **`அதனால் மாரியாத்தாளுக்கு பூசை நடத்துகிறோம்.`**.

The earlier narrative sentence `ஒரு கிராமத்தில் மாரிக்கு பூஜை நடந்து கொண்டிருக்கிறது.` remains **`பூஜை`**; the `பூசை` correction applies only to the later Jeevanandar dialogue occurrence.

Historical-glyph final review: **PASS** for the page. The unresolved item is physical lexical loss, not an unresolved historical-character identity.

## PDF 6 — PASS / VERIFIED

Full-page visual comparison: **PASS**. No new lexical correction required.

Historical-glyph final review: **PASS**. In particular:

- `அவளை` is confirmed as historical `ளை` identity;
- `சூரியனால்` is confirmed against the historical `னா` family.

Dual gate: **VERIFIED**.

## PDF 7 — PASS / VERIFIED

Full-page visual comparison: **PASS**. The song continuation, `காட்சி 2`, speaker labels and dialogue agree with the source-visible wording; no lexical correction required.

Historical-glyph final review: **PASS** after page-level review of the mandatory families.

Dual gate: **VERIFIED**.

## PDF 8 — PASS / VERIFIED

Full-page visual comparison exposed one substantive first-pass lexical error:

- `அந்த உலகத்திலே அவற்றை எல்லாம் மறந்து விடுவான்!` → **`அந்த உல்லாசத்திலே அவற்றை எல்லாம் மறந்து விடுவான்!`**.

The remainder of the page, including the move to `காட்சி 3`, is source-supported.

Historical-glyph final review: **PASS**, including page-visible `உன்னை` / `அண்ணாமலை`-family shapes where applicable.

Dual gate: **VERIFIED** after correction.

## PDF 9 — PASS / VERIFIED

Native/enlarged source comparison resolves the previously carried montage uncertainty and corrects four additional first-pass readings.

Scan-backed corrections / adjudications:

- `வந்திருக்காங்களே.` → **`வந்திருக்காங்க.`**;
- uncertainty marker `குறுக்கொடிய போலத் தோன்றும்...` → **`குறுக்கொடிய`**; the unusual source form is preserved without modernization;
- `ஆட்டுப்பழம் வருகிறது` → **`ஆரஞ்சுப்பழம் வருகிறது`**;
- `பட்டாளி குமரனுக்கு` → **`பாட்டாளி குமரனுக்கு`**;
- `தனது காதில் சுவையுள்ள பொருள்கள்` → **`தனது காதல் சுவையுள்ள பொருள்கள்`**.

The resolved montage sequence therefore preserves the source wording rather than semantic normalization. This closes the former PDF 9 uncertainty.

Historical-glyph final review: **PASS**, including the `லை` identity in page-visible lexical material such as `வேலைக்காரி` / `காதல்` context where relevant.

Dual gate: **VERIFIED**.

## Batch result

| PDF | Visual fidelity | Historical glyph final | Dual-gate status | Open uncertainty |
|---:|---|---|---|---:|
| 5 | HOLD — damaged intro beginning | PASS | needs-review | 1 |
| 6 | PASS | PASS | VERIFIED | 0 |
| 7 | PASS | PASS | VERIFIED | 0 |
| 8 | PASS after correction | PASS | VERIFIED | 0 |
| 9 | PASS after correction/adjudication | PASS | VERIFIED | 0 |
| **Total** | **4 PASS + 1 HOLD** | **5 PASS** | **4 VERIFIED** | **1** |

Repository-wide checkpoint after synchronization should therefore be:

- canonical first pass: **67/67 COMPLETE**;
- visual-fidelity passed: **4/67**;
- historical-glyph final verified: **5/67**;
- dual-gate canonical verified: **4/67**;
- needs review: **63/67**;
- open source uncertainties: **1**, only the physically damaged beginning of the PDF 5 introductory line.

## Next activity

Proceed with the separate visual-fidelity and final historical-glyph verification audit for **PDF 10–14**. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen PDF 6–9 absent genuinely new direct-source evidence; PDF 5 remains an explicit source-damage hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete.
