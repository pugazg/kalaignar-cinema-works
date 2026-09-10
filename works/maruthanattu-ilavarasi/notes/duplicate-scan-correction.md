# மருதநாட்டு இளவரசி — final-range duplicate scan correction

Direct source rendering during the final Tamil first-pass range established a non-obvious scan geometry that supersedes the initial one-PDF-page/one-printed-page assumption after PDF 16.

- PDF 17 and PDF 18 are identical two-page spreads containing printed pages **16–17**.
- PDF 19 and PDF 20 are identical two-page spreads containing printed pages **18–19**.
- PDF 21 and PDF 22 are identical two-page spreads containing printed pages **20–21**.

Canonical text therefore uses representative spreads PDF **17, 19, 21** only, split into left/right logical-page records. Duplicate physical scans **18, 20, 22** are retained in provenance but contribute no second copy of text.

This correction also relocates source-heading provenance without changing the printed sequence: `காட்சி 9.` is on printed page 17 / PDF 17 right, and `காட்சி 10.` + `பலி பீடம்.` is on printed page 18 / PDF 19 left.

No source text was inferred from the duplicate relationship; the rendered pixels remain controlling.
