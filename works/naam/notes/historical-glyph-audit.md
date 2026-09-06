# நாம் — Historical Tamil Glyph Audit

Status: **partial-first-pass**  
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

A page can complete its historical-glyph first-pass inspection without becoming globally verified. Final canonical verification requires both:

- complete visual-fidelity comparison against the rendered page; and
- historical-glyph audit PASS for that page.

Until both gates are complete, no structured scene/dialogue/character/song derivative may treat the page as verified authority.

## Coverage

| Range | Pages expected | Glyph first-pass checked | Dual-gate verified | Needs review | Status |
|---|---:|---:|---:|---:|---|
| PDF 5–9 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 10–71 | 62 | 0 | 0 | 0 | not-started |
| **Total** | **67** | **5** | **0** | **5** | **partial-first-pass** |

## First-pass findings / correction log

| PDF | Printed page | Earlier/apparent reading | Source-supported Unicode reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| 6 | 6 | apparent bare-`ள்` surface in `அவள்...` cluster | `அவளை` | `ளை` | enlarged source cluster + same-word syntax; old `ளை` identity | draft-supported |
| 6 | 6 | old `னா` form in `சூரியனால்` | `சூரியனால்` | `னா` | enlarged source pixels; family explicitly checked before Unicode encoding | draft-supported |

These findings decode character identity only. They do not authorize spelling modernization elsewhere.

## Open source questions affecting this batch

- PDF 5: one physically damaged introductory line remains unresolved; secure surrounding text is retained and the damaged span is marked explicitly in the canonical draft.
- PDF 9: one word in the montage/action paragraph after `(நாட்கள் பல கடந்தன)` remains unresolved; the approximate visible cluster is retained only inside an uncertainty marker.

Neither issue is being guessed from context.

## Source-specific cautions

- front matter is physically damaged, but this canonical audit currently covers the screenplay range PDF 5–71;
- many pages contain later handwritten pencil numbers/marks near the upper-right margin; these are not printed Tamil and must not enter the canonical layer;
- fading, bleed-through and broken ink require same-edition comparison rather than silent normalization;
- PDF 5 has no securely visible printed page numeral; glyph decisions and pagination decisions remain separate;
- source-colloquial forms encountered in PDF 5–9 remain source-faithful and are not standardized during glyph decoding.

## Next activity

Continue the historical-glyph first-pass concurrently with **canonical Tamil PDF 10–14**. Do not mark PDF 5–9 verified merely because their first-pass text now exists; the separate visual-fidelity and final historical-glyph gates are still open.
