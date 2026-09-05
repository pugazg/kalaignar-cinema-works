# அம்மையப்பன் — canonical Tamil transcription

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

The rendered scan controls. OCR, parsed text, film audio, subtitles, web quotations and later editions are non-canonical.

Because this 1954 source contains frequent historical Tamil typeforms, a page is final Tamil verified only after both:

1. rendered-scan visual source-fidelity verification; and
2. historical-Tamil-glyph verification under `../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` and `../notes/historical-glyph-audit.md`.

## First-pass closure checkpoint

- canonical screenplay range: **PDF 5–109 / logical printed pp.3–107**;
- canonical pages expected: **105**;
- first-pass pages completed: **105 / 105**;
- completed range: **PDF 5–109 / logical pp.3–107**;
- first-pass status: **draft-complete**;
- visual-fidelity-passed pages: **70/105**;
- historical-glyph-cleared pages under the explicit new gate: **0/105 at gate introduction**;
- final dual-gate verified pages: **0/105 at gate introduction**;
- review pages: **0**;
- open first-pass uncertain readings: **29**;
- continuous assembled transcription: `full-text.md` through **PDF 109**;
- assembly QA: `ASSEMBLY_QA.md` — **PASS**;
- full rendered-scan visual fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 passed (70/105)**;
- historical Tamil glyph audit: **required across PDF 5–109 / all 105 pages**.

PDF 5 has no visible printed folio. Its anchor records `logical_printed=3` with `printed_folio=suppressed`; PDF 6 onward uses the visible printed page where present.

The existing PDF 5–74 visual-fidelity result is retained as visual evidence, but those pages require a retrospective historical-glyph pass. For PDF 75–109, both audits must be performed together.

## Assembly result

The first pass was created in bounded source-order batches and then assembled into one continuous `full-text.md`.

- original continuous base: **PDF 5–14**;
- bounded parts: **PDF 15–24, 25–34, 35–44, 45–54, 55–64, 65–74, 75–84, 85–94, 95–104, 105–109**;
- assembly preserved each `<!-- source: pdf=... -->` page anchor;
- batch wrapper metadata was excluded from the continuous text;
- anchor count: **105**;
- anchor sequence: **exactly PDF 5 through PDF 109**;
- missing anchors: **0**;
- duplicate anchors: **0**;
- bounded-part boundary QA: **PASS**;
- locked PDF 107 heading `தூக்குமேடை`: **PASS**;
- rejected `தாக்குமேடை`: **absent**.

The bounded part files remain useful source-order provenance and audit artifacts even though `full-text.md` is now the complete continuous first-pass draft.

## First-pass policy retained

- source order only;
- exact visible headings/speaker labels/stage directions where secure;
- no modernization or silent repair;
- uncertain old-typeface tokens remain visibly marked with `⟦...⟧`;
- user-reviewed scan verdicts remain locked occurrence-by-occurrence;
- no scene/dialogue/character derivative work until the whole canonical range passes the dual verification gate.

## Historical Tamil glyph verification policy

Minimum known families to inspect occurrence-by-occurrence on every canonical page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This minimum set does not exhaust all historical typeform risks. Inspect other old ligatures, faint vowel marks, broken or worn type, and edition-specific forms as encountered.

Character identity must be established from enlarged/native source pixels. Use same-edition/same-font comparison for doubtful forms. OCR, semantic expectation and modern spelling are not proof. Do not global-replace suspected forms. A historical-glyph correction changes character identity only; it does not license spelling modernization.

If a historical-glyph correction changes a page that already passed visual fidelity, recheck the corrected occurrence visually and record the correction in the work-level audit.

## Batch history

- PDF 5–14: initial continuous draft.
- PDF 15–24: draft complete.
- PDF 25–34: draft complete.
- PDF 35–44: draft complete after direct scan reconciliation; `தனபதி` restored where initially misread as `தளபதி`.
- PDF 45–54: draft complete.
- PDF 55–64: draft complete; preserves locked `பழுதார் வீதி` and the PDF 64→65 quoted-poetry boundary.
- PDF 65–74: coverage complete, **high uncertainty**, with 39 batch markers.
- PDF 75–84: draft complete, 10 batch markers.
- PDF 85–94: draft complete, 10 batch markers; preserves source-visible local transitions beyond the narrower intake inventory.
- PDF 95–104: draft complete, 7 batch markers numbered 108–114.
- PDF 105–109: final draft batch complete, 2 batch markers numbered **115–116**; preserves the PDF 104→105 continuation and locked `தூக்குமேடை` heading.

## Exact next activity

Continue at **PDF 75 / logical printed p.73** and perform **visual source-fidelity + historical-Tamil-glyph verification together**. Markers **88–116** remain unresolved on PDF 75–109. Before final Tamil closure, complete the retrospective historical-glyph audit for **PDF 5–74**. Structured derivatives stay blocked until both verification gates reach **105/105**.
