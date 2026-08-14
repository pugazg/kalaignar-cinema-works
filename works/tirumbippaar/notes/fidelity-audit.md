# திரும்பிப்பார்! — canonical Tamil fidelity audit

Status: **in-progress**.

Source: `TVA_BOK_0014652_திரும்பிப்பார்.pdf`  
SHA-256: `973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682`

The full main-text first pass is **draft-complete** for PDF **9–112 / printed pp.1–104**. Verification is proceeding page by page against rendered scan images.

## Audit rules

- Rendered scan pages are controlling evidence; OCR is navigation-only.
- Preserve source spelling, punctuation, speaker labels, scene-marker irregularities, English code-switching, stage directions and performance/printed-text structures.
- Do not repair from film audio, subtitles, web copies, memory or later editions.
- A page becomes `verified` only after its complete visible text has been compared against the scan and all source-supported corrections are applied.
- If the scan cannot support a confident reading, retain the uncertainty explicitly rather than guessing.
- Structured scene/dialogue/character/song/translation derivatives remain blocked until their controlling Tamil source material is verified.

## Progress

| Range | Draft pages | Verified pages | Review / unresolved pages | Status |
|---|---:|---:|---:|---|
| PDF 9–13 / printed pp.1–5 | 0 | 5 | 0 | verified |
| PDF 14–18 / printed pp.6–10 | 0 | 5 | 0 | verified |
| PDF 19–112 / printed pp.11–104 | 94 | 0 | 0 | pending |
| **Total** | **94** | **10** | **0** | **in-progress** |

## PDF 9–13 / printed pp.1–5 — completed audit

All five pages were visually compared against the rendered source scan. The batch is `verified`; no unresolved reading remains in this range.

Source-supported first-pass corrections applied:

- **PDF 9 / printed p.1:** restored source `இல்ல.` in place of normalized `இல்லை.`.
- **PDF 9 / printed p.1:** restored repeated source form `இல்ல இல்ல.` in place of `இல்லை இல்லை,`.
- **PDF 10 / printed p.2:** corrected the place-name reading to source-visible `கோயமுத்தார்!`.
- **PDF 10 / printed p.2:** removed an unsupported editorial hyphen from `அதன் பெயர் கருடன் பதிப்பகம்.`.
- **PDF 12 / printed p.4:** restored the printed speaker label `குணரத்தனம்` throughout the page instead of normalizing it to `குணரத்தினம்`.
- **PDF 12 / printed p.4:** restored source spelling `லக்ஷ்மி` instead of modernized `லட்சுமி`.
- **PDF 13 / printed p.5:** restored the same printed speaker label `குணரத்தனம்`.
- **PDF 13 / printed p.5:** restored source colloquial spelling `இதைப்போயி!` instead of `இதைப்போய்!`.

Source-visible irregular forms such as `காட்சி 5[`, `[Bath Room`, `Nightdress`, `Silence`, `So many entertainments`, `செய்ய வில்லை`, `இருக்கிற தால்தான்`, and `எழுதிய தென்று` were retained rather than normalized.

## PDF 14–18 / printed pp.6–10 — completed audit

These five pages required a substantially heavier correction pass than the opening batch. All visible text on PDF 14–18 was checked against the rendered scan and the corrected page text is now stored in `transcription/parts/part-02-pdf-14-35.md` with `status=verified` anchors.

Representative source-supported corrections include:

- **PDF 14 / printed p.6:** restored the anomalous printed speaker label `குரு:` rather than silently expanding it to `கருடன்:`.
- **PDF 14:** restored the historical-name sequence `தலையாலங்கானத்து செருவென்ற பாண்டியனு? ஆரியப்படை கடந்த நெடுஞ்செழியனு?` instead of the corrupted first-pass paraphrase.
- **PDF 14:** restored `எழுத்துத் திருடன் சந்திக்கவந்த`, `ஆசிரியனு?`, `அயோக்கியத்தனம்`, `மரியாதையாகப் போகமாட்டாய்`, `சீ...பேசாதே!`, and the source stage action in which the மேஜை is opened and the ரிவால்வர் is taken.
- **PDF 15 / printed p.7:** restored `சும்மா இரு`, `அனாவசியமா`, the `பஞ்சண` / `பஞ்சணையைப்பத்தி` forms, `வரகவியா, சுய கவியா?`, the pen/ink imagery, and `வியாபாரமாகாவிட்டாலும்`.
- **PDF 15:** corrected scene-6 staging to `மரத்தின் மேலே இருந்து பரந்தாமன் குடத்தின் கழுத்தில் சுருக்குப் போட்டு இழுக்கிறான்`.
- **PDF 16 / printed p.8:** restored `கயிற்றால்`, `மரகதமணிக் கழுத்திலே`, `மாங்கல்யக் கயிற்றால்`, `புயலை அடக்கும்`, `அணைக்கின்ற`, `வர்ணனையாக`, `நாளை ஓடிவிடுவேனு`, `கொஞ்ச மொழியாலே!`, and `இல்ல...யில்ல...`.
- **PDF 17 / printed p.9:** restored `ஈடு பட்டிருக்கின்றனர்`, `வச்சு விட்டோம்னு நெனச்சேன்`, and the full colour-wordplay ending `எழுமிச்சம்பழ நிறமா, நாகற்பழ நிறமா, அல்லது இரண்டுங் கலந்ததா?`.
- **PDF 18 / printed p.10:** restored the printed `கவிதைகளால்ல` forms and corrected scene-9 staging to `மாடியில் தேடி அலுத்து பிரமைபிடித்தவள்போலிருக்கும் பூமாலிடம் குமுதா ஓடிவருகிறாள்`.

No unresolved reading remains in PDF 14–18 after this audit. Source irregularities were preserved rather than normalized.

**Next audit page:** PDF **19 / printed p.11**.
