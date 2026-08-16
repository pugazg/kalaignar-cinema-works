# மனோகரா — Part 03 final fidelity record

Source: `TVA_BOK_0010102_மனோகரா.pdf`  
SHA-256: `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`

This note records the final, source-led disposition of Part 03, PDF **43–54** / printed pp. **42–53**. It supersedes the temporary preliminary/review notes created while PDF 49–54 was being checked.

## Why the PDF 49–54 review was repeated

The preliminary Batch 8 notes mixed genuine first-pass/source mismatches with several source forms that the first-pass transcription had already retained correctly. No canonical rewrite was allowed from that preliminary list. The six pages were therefore re-audited directly against the rendered scan before any write to `transcription/parts/part-03-pdf-43-54.md`.

The re-audit confirmed **18 actual correction groups** for PDF 49–54. Combined with the **30** already recorded for PDF 43–48, the final Part 03 source-led set contains **48 correction groups**.

Examples of preliminary observations rejected during re-audit include attempts to change source-supported `சத்திய :`, `மனோகரா!`, `ஹூம்`, `குள்ள நரி வேலை தான்`, the period in `சம்பந்தம் இல்லாதது.`, `என் உத்தரவை`, and `சத். சீல :`. Those forms were retained because the rendered scan supports them.

## Final PDF 49–54 corrections

The actual correction groups added by the direct re-audit were:

- PDF 49 / p.48: `இரும்புச் சங்கிலியால்` → `இரும்பு சங்கிலியால்`; `அழைத்து வாருங்கள்.` → `அழைத்து வாருங்கள்,`; `விலங்கா?` → `விலங்கா ?`; `அதற்கு எப்படி சென்றால் என்ன?` → `அதற்கு எப்படிச் சென்றால் என்ன?`; `திருத்திக் கொள்ளுங்கள் தயவு செய்து.` → `திருத்திக் கொள்ளுங்கள் தயவு செய்து,`.
- PDF 50 / p.49: `தந்தத்தால் ஆன கட்டிலே` → `தந்தத்தால் ஆன கட்டிலிலே`; `அவனை அந்த மனோகரன் சங்கிலியால்` → `அவனை அந்த மனோகரனை சங்கிலியால்`; `மாவீரர்கள்` → `மா வீரர்கள்`.
- PDF 51 / p.50: **no additional correction after direct re-audit**.
- PDF 52 / p.51: `தயார் தானா...? தயார்தானா?...` → `தயார் தானா...? தயார் தானா?...`; laughter `ஹா...ஹா...ஹா` → `ஹ...ஹ...ஹ`; `புலி—வாள்` → `புலி - வாள்`; `பாசறையை பார்வையிட்ட` → `பாசறையைப் பார்வையிட்ட`; `குட்டிச்சுவரின்` → `குட்டி சுவரின்`.
- PDF 53 / p.52: `மாற்றுக்குறையாத தங்கம்` → `மாற்றுக் குறையாத தங்கம்`; restore the omitted source line `என் அன்னையைத் தூஷித்த சின்னஞ்சிறு புழுவே...`; `ஏ, ராஜவிக்ரகமே!` → source punctuation `ஏ, ராஜவிக்ரகமே :`.
- PDF 54 / p.53: `(அரசரைப் பார்த்து)` → source's anomalous `(அரசரைப் பார்த்து]`; `பிச்சை கேட்பதும்` → `பிச்சைக் கேட்பதும்`.

## Controlled application

The exact pre-application Part 03 blob was:

`26904619942e2249c8c1b2a5af006af354d2d8c4`

The reviewed corrections were applied in one controlled rewrite. The resulting corrected-draft blob was independently calculated before the GitHub write and matched the blob returned by GitHub exactly:

`96e4510a09a445663444b7b37340a6405dabc6f6`

Application commit:

`f084ff91647ec1d76d2a113351e1a769fc8bad53`

The corrected file retained all **12** source anchors, PDF 43 through PDF 54, in order and at `draft` status during the recheck. Mechanical checks confirmed that the expected source-supported readings were present and the superseded first-pass readings were absent.

## Post-application recheck and promotion

PDF **43–54** was rechecked against the rendered scan after application. No unresolved source reading remained. The verified version was independently hashed before the promotion write, and GitHub returned the same expected blob:

`557dfb39e42d2fe777600ce0f73ad4ef00745ec0`

Verification-promotion commit:

`7f1413a451b7ac4ee769c0f20766f9c08939d753`

Part 03 final result:

- canonical range: **PDF 43–54 / printed pp.42–53**;
- pages: **12 verified / 0 review / 0 draft within Part 03**;
- final correction groups: **48 applied**;
- unresolved source readings: **0**;
- post-application visual recheck: **passed**.

Cumulative Manohara fidelity state after Part 03:

- verified: **48/82 pages** — PDF **7–54 / printed pp.6–53**;
- draft: **34 pages** — PDF **55–88**;
- review: **0**;
- next audit page: **PDF 55 / printed p.54**.

**Next:** begin the Part 04 visual fidelity audit at PDF 55 / printed p.54. Keep Part 04 anchors `draft` until its corrections are accumulated, applied and rechecked.
