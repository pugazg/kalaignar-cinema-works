# நாம் — Historical Tamil Glyph Audit

Status: **not-started**  
Canonical source range: **PDF 5–71 — 67 pages**  
Binding guide: `../../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## Purpose

The `நாம்` source uses older Tamil print and an image-only scan. Historical character identity must therefore be decoded from the rendered source pixels rather than from modern visual resemblance, OCR, semantic expectation or a later spelling.

This audit begins with canonical transcription and remains a separate gate from ordinary visual-fidelity review.

## Mandatory families

Every canonical page must explicitly consider at least:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

The set is a minimum. Other worn, faint, broken or edition-specific ligatures remain in scope.

## Page-level method

For each PDF page 5–71:

1. inspect the complete page at enlarged/native resolution;
2. decode the full glyph cluster, not an isolated loop or vowel mark;
3. compare clearer same-edition examples when needed;
4. use grammar/lexical expectation only to locate a doubtful form, never as proof;
5. encode the positively supported historical character identity in normal Unicode;
6. preserve every other source feature — spelling, grammar, vocabulary, spacing and punctuation;
7. record consequential corrections explicitly;
8. never global-replace a glyph family;
9. leave unresolved forms `needs-review` rather than guessing.

OCR is a discovery/navigation aid only and has no authority for historical glyph identity.

## Verification model

A page can complete its historical-glyph inspection without becoming globally verified. Final canonical verification requires both:

- complete visual-fidelity comparison against the rendered page; and
- historical-glyph audit PASS for that page.

Until both gates are complete, no structured scene/dialogue/character/song derivative may treat the page as verified authority.

## Coverage

| Range | Pages expected | Glyph pass complete | Dual-gate verified | Needs review | Status |
|---|---:|---:|---:|---:|---|
| PDF 5–71 | 67 | 0 | 0 | 0 | not-started |

## Correction log

No corrections recorded yet. During transcription use entries of the form:

| PDF | Printed page | Earlier/apparent reading | Source-supported Unicode reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| — | — | — | — | — | — | not-started |

## Source-specific cautions

- front matter is physically damaged, but this canonical audit currently covers the screenplay range PDF 5–71;
- many pages contain later handwritten pencil numbers/marks near the upper-right margin; these are not printed Tamil and must not enter the canonical layer;
- fading, bleed-through and broken ink require same-edition comparison rather than silent normalization;
- PDF 5 has no securely visible printed page numeral; glyph decisions and pagination decisions must remain separate.

## Next activity

Begin this audit concurrently with the **canonical Tamil first-pass transcription**, page by page from PDF 5 onward. Do not mark pages verified merely because the first-pass text appears plausible.
