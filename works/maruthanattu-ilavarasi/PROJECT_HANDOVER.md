# மருதநாட்டு இளவரசி — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/maruthanattu-ilavarasi/`

**LIVE MAIN IS AUTHORITATIVE.**

Current live checkpoint when this handover was refreshed: `a99de46015a361feda8b7f05039cedf6bc28f7b2` — `Add Maruthanattu Ilavarasi verification batch 11-15`.

## Controlling source

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**.

The rendered source pixels are controlling authority. The user-supplied transcription may be used only as a candidate/navigation aid. Do not normalize wording, silently repair grammar, or prefer OCR/extraction over the scan.

## Durable source geometry

- PDF 2 is unique;
- duplicate spreads: **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22**;
- canonical representative PDFs: **2,3,5,7,9,11,13,15,17,19,21**;
- canonical logical printed pages: **1–21**;
- logical pages 1–3 are an unnumbered opening; do **not** invent `காட்சி 1.`;
- source-numbered headings observed: **2,3,4,5,6,7,8,9,10**.

## Current durable verification state

- source intake / mapping: **COMPLETE / COMPLETE-VERIFIED-CORRECTED**;
- Tamil T1: **21/21 COMPLETE-DRAFT**;
- independent visual-fidelity verification: **10/21 PASS**;
- final historical-glyph verification: **10/21 PASS**;
- remaining draft pages: **11**;
- open uncertainty markers: **0**;
- structured scene/dialogue/character/song/English/reader derivatives: **BLOCKED**.

### User/source corrections that must remain authoritative

- logical page 1 / PDF 2 right: **`தங்கையின் குழந்தை தரணி ஆளவேண்டுமே`** — not `தான் ஆளவேண்டுமே`;
- logical page 3 / PDF 3 right: **`இத்தியாகம் செய்யத்தான் வேண்டும்;`** — not `செய்துதான்`.

V1 historical notes/builders were patched so these corrected readings are not reintroduced.

## Prepared but not yet promoted

`works/maruthanattu-ilavarasi/scripts/verify_batch_011_015.py` has been added on live `main` for the next five-page verification batch. **Its presence does not mean logical pages 11–15 are verified yet.** Durable counters remain **10/21** until that batch is independently source-checked, executed, QA-passed, and committed.

The prepared V3 script expects these candidate source corrections during verification:

- logical page 11: `பழக்கொலை நீ!` → candidate source reading `பழக்கொடி நீ!`;
- logical page 13: `இவன் கைது செய்த` → candidate source reading `இவனை கைது செய்த`;
- logical page 15: `இவன் கைது செய்த` → candidate source reading `இவனை கைது செய்த`;
- logical page 15: `அந்த சுத்தவீரன் இவனே` → candidate source reading `அந்த சுத்தவீரனை இவனே`;
- logical page 15: `இந்நாட்டு மக்கள் காட்டு மிருகம்போல்` → candidate source reading `இந்நாட்டு மக்களை காட்டு மிருகம்போல்`.

These must still be confirmed against the controlling pixels before promotion to VERIFIED.

## Exact next activity

> **Independently re-read logical printed pages 11–15 against representative source pixels: PDF 11 right (printed 11), PDF 13 left/right (printed 12–13), and PDF 15 left/right (printed 14–15). Treat PDFs 12,14,16 as provenance-only duplicate spreads. Confirm or reject every prepared V3 correction against the source pixels; only then run the prepared V3 builder, require QA PASS / 0 unresolved, advance both verification counters from 10/21 to 15/21, and keep structured derivatives blocked.**

After a successful V3 closure, the following batch is logical printed pages **16–20** using PDF 17 left/right, PDF 19 left/right and PDF 21 left.
