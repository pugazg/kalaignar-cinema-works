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
| PDF 10–14 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 15–19 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 20–24 | 5 | 5 | 0 | 5 | partial-first-pass |
| PDF 25–71 | 47 | 0 | 0 | 0 | not-started |
| **Total** | **67** | **20** | **0** | **20** | **partial-first-pass** |

## First-pass findings / correction log

| PDF | Printed page | Earlier/apparent reading | Source-supported Unicode reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|
| 6 | 6 | apparent bare-`ள்` surface in `அவள்...` cluster | `அவளை` | `ளை` | enlarged source cluster + same-word syntax; old `ளை` identity | draft-supported |
| 6 | 6 | old `னா` form in `சூரியனால்` | `சூரியனால்` | `னா` | enlarged source pixels; family explicitly checked before Unicode encoding | draft-supported |
| 11 | 11 | old-form cluster in `கண்ணாடிச்` | `கண்ணாடிச்` | `ணா` | enlarged source pixels; positive family occurrence | draft-supported |
| 21 | 21 | modern-lookalike `நீதானு...?` | `நீதானா...?` | `னா` | enlarged source pixels + binding guide's same-family precedent (`மட்டுந்தானு?` → `மட்டுந்தானா?`) | draft-supported |

These findings decode character identity only. They do not authorize spelling modernization elsewhere.

## PDF 15–19 scan-backed textual reconciliation

Direct enlarged-pixel comparison corrected five local first-pass readings:

- PDF 15 `எல்லோருக்கும்` — not `எல்லோருக்குமே`;
- PDF 15 `உருண்டோடிடுமே` — the printed `மே` is retained;
- PDF 17 `அவன் கை வலி` — not `அவனே கை வலி`;
- PDF 19 `என்னே` — not `என்ன`;
- PDF 19 `என் மருமகளும்` — not `என் மருமகனும்`.

These are local source-fidelity corrections, not historical-family substitution rules. PDF 15–19 was nevertheless checked page-by-page for the full mandatory family set.

## PDF 20–24 glyph/text findings

- PDF 21 `நீதானா...?` is the batch's consequential historical-family decision: the old `னா` glyph can resemble `னு`, but source-supported character identity is `னா`;
- PDF 20 `போறு ஞானம்!` and `பாய்சன்!` remain source-visible forms;
- PDF 21 `மாடெல்லே` and related colloquial forms remain source-controlled;
- PDF 22 `பாலிலா` remains as printed;
- PDF 23 `தூர பந்து` / `மட்டாக` and `காலராவா? ஜன்னியா?` remain unmodernized;
- PDF 24 `கெளரவம்` remains in the printed orthographic form;
- PDF 20–24 introduced **0 new explicit uncertainty markers**.

The non-glyph items above are textual-fidelity decisions and do not create replacement rules.

## Source-irregular forms retained

- PDF 12 `தளிர்ச்சிருக்கே` is retained as source-visible wording at first pass;
- PDF 13 `கீல்வலிக்கார தங்கையன்` is preserved source-faithfully;
- PDF 14 visibly prints `வாலாம்` twice;
- PDF 15 `பிரேமா வாகவர்` remains as printed;
- PDF 17's extended labour/tax rhetoric remains source-controlled;
- PDF 19 `சோபிதத்தை`, `கானல் மாடுமே`, and `காதியின்` remain unmodernized first-pass readings;
- PDF 20–24 source-irregular/period wording remains as documented in `textual-notes-pdf-020-024.md`.

## Performance evidence affecting later gates

- PDF 16 / `காட்சி 7` contains an explicit `[பாட்டு]` witness with three numbered sections. The booklet's PDF 4 item-level credit identifies **`ஆயிரம் தெய்வங்கள்` — பாரதியார்**. No outside lyric witness was used.
- PDF 18 / `காட்சி 8` contains a source-visible lineated lyrical duet labelled `குமரன்`, `மீனு`, and `இருவர்`, beginning `பேசும் யாழே பெண் மானே`. Its authorship remains unadjudicated.
- PDF 20–24 introduces no newly distinct standalone lyric/song structure.

These observations are structural/source evidence only and do not bypass the canonical dual gate.

## Open source questions affecting the cumulative draft

- PDF 5: one physically damaged introductory line remains unresolved;
- PDF 9: one word in the montage/action paragraph after `(நாட்கள் பல கடந்தன)` remains unresolved;
- PDF 10–24 introduced **0 new explicit uncertainty markers**.

Neither open issue is being guessed from context.

## Source-specific cautions

- front matter is physically damaged, but this canonical audit currently covers the screenplay range PDF 5–71;
- many pages contain later handwritten pencil numbers/marks near the upper-right margin; these are not printed Tamil and must not enter the canonical layer;
- fading, bleed-through and broken ink require same-edition comparison rather than silent normalization;
- PDF 5 has no securely visible printed page numeral; glyph decisions and pagination decisions remain separate;
- source-colloquial and source-irregular forms remain source-faithful and are not standardized during glyph decoding.

## Next activity

Continue the historical-glyph first-pass concurrently with **canonical Tamil PDF 25–29**. Do not mark PDF 5–24 verified merely because their first-pass text now exists; the separate visual-fidelity and final historical-glyph gates are still open.
