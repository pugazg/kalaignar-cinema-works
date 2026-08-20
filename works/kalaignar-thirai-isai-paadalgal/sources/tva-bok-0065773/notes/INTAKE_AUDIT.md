# Intake audit — TVA_BOK_0065773

## Scope

This audit covers the complete **62-page** supplied scan only. It establishes identity, physical-source facts, page structure, song numbering and visible scan anomalies. It does **not** certify any canonical lyric transcription.

## Source identity gate

PASS for intake:

- exact visible title: `கலைஞர் திரை இசைப் பாடல்கள்`;
- cover credit: `தொகுப்பாசிரியர் சிலோன் விஜயேந்திரன்`;
- title-page credit: `தொகுப்பு சிலோன் விஜயேந்திரன்`;
- imprint: `காந்தளகம்`;
- explicit edition/date line: `முதற்பதிப்பு:` / `வைகாசி 21, திருவள்ளுவர் 2020 (03.06.89)`;
- archive identifier used by this repository: `TVA_BOK_0065773`, taken from the supplied archive filename rather than reconstructed from scan text;
- PDF pages: 62;
- bytes: 10,419,528;
- SHA-256: `56d414a65a61a73b990632eadc17a3b1efdc764d47f64b851060c161a3f98e3b`;
- source is image-only; no usable embedded text layer was observed.

PDF creation metadata was inspected only as a technical property and is **not** used as publication/edition evidence.

## Whole-scan structural gate

PASS:

| PDF | Structure |
|---:|---|
| 1 | cover |
| 2 | title / compiler / publisher-imprint page; library stamp and handwriting overlay |
| 3 | rights / first-edition date / price / printer line; handwritten library marks |
| 4 | `தொகுப்பாசிரியர் உரை` |
| 5–7 | `தும்பிப்புரை` — `(டாக்டர் சிலம்பொலி சு.செல்லப்பன்)` |
| 8–9 | `உள்ளடக்கம்` |
| 10–62 | numbered film-song body, printed pp.1–53 |

There is no separate back-matter range after the numbered corpus: PDF 62 is printed p.53 and continues song 40.

Printed pagination is continuous across the body. For PDF 10–62, `printed page = PDF page - 9`.

## Numbering and thematic divisions

The body prints **40** numbered song sections, consecutively 1–40, with no missing/repeated/out-of-order body number.

Body divisions:

1. `எழுச்சித் தமிழ்` — songs 1–15 — PDF 10–34 / printed pp.1–25;
2. `நேசத் தமிழ்` — songs 16–31 — PDF 35–50 / printed pp.26–41;
3. `பாசத் தமிழ்` — songs 32–36 — PDF 51–55 / printed pp.42–46;
4. `நகைச்சுவைத் தமிழ்` — songs 37–40 — PDF 56–62 / printed pp.47–53.

The contents typography joins the first two headings (`எழுச்சித்தமிழ்`, `நேசத்தமிழ்`); the body prints them with the visible spacing shown above. Both witnesses are retained rather than normalized.

## Preserved source anomaly

The contents on PDF 9 print:

- 30. `ஒண்ணு கொடுத்தா...` — `மறக்க முடியுமா` — p.40;
- 31. `வான் மலர்ச் சோலையில்` — `ரங்கோன் ராதா` — p.41.

The body instead prints:

- song 30, printed p.40 / PDF 49: `வான் மலர்ச் சோலையில்...` — `ரங்கோன் ராதா`;
- song 31, printed p.41 / PDF 50: `ஒண்ணு கொடுத்தா...` — `மறக்க முடியுமா?`.

This is recorded as a source-level contents/body ordering error. It is **not repaired** by rewriting either witness.

A second discrepancy occurs at song 33: contents PDF 9 assigns `பூமாலை...` to `மறக்க முடியுமா` on p.43, while body PDF 52 / printed p.43 states `ஆண்டு: 1952; படம்: 'பராசக்தி'; இசை: ஆர். சுதர்சனம்;`. This film-attribution mismatch is likewise preserved.

## Scan-condition findings

No missing or duplicated physical PDF page was observed. No content-critical crop was found in the mapped body.

Non-source overlays/scan artifacts include:

- library stamp and handwriting on PDF 2;
- handwritten shelf/call-number marks on PDF 3;
- library stamps on some body pages;
- scattered speckling, smudges and page-edge darkening, including a dark right edge on PDF 9;
- occasional edge marks in the body, without observed loss of the mapped text.

These are not canonical text.

## Gate result

- source intake: **complete**;
- structural mapping: **verified for this witness**;
- canonical Tamil first pass: **not-started**;
- downstream derivatives: **blocked**.

Next: canonical Tamil first-pass transcription from rendered scan images, source order, stable page anchors; then a separate line-by-line visual fidelity audit.
