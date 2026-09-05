# அம்மையப்பன் — canonical Tamil transcription

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

The rendered scan controls. OCR, parsed text, film audio, subtitles, web quotations and later editions are non-canonical.

Because this 1954 source contains frequent historical Tamil typeforms, a page is final Tamil verified only after both:

1. rendered-scan visual source-fidelity verification; and
2. historical-Tamil-glyph verification under `../../docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` and `../notes/historical-glyph-audit.md`.

## Current dual-gate checkpoint

- canonical screenplay range: **PDF 5–109 / logical printed pp.3–107**;
- canonical pages expected: **105**;
- first-pass pages completed: **105 / 105**;
- first-pass status: **draft-complete**;
- visual-fidelity-passed pages: **70/105 — PDF 5–74**;
- historical-glyph-passed pages: **70/105 — PDF 5–74**;
- final dual-gate verified pages: **70/105 — PDF 5–74**;
- current dual-gate review pages: **0** in the closed PDF 5–74 range;
- remaining canonical pages: **35 — PDF 75–109**;
- open first-pass uncertain readings: **29**;
- continuous assembled transcription: `full-text.md` through **PDF 109**;
- assembly QA: `ASSEMBLY_QA.md` — **PASS**;
- next source page: **PDF 75 / logical printed p.73**.

PDF 5 has no visible printed folio. Its anchor records `logical_printed=3` with `printed_folio=suppressed`; PDF 6 onward uses the visible printed page where present.

## Retrospective historical-glyph synchronization — CLOSED

PDF 5–74 had already passed visual fidelity before the explicit historical-glyph gate was introduced. The full range was re-inspected from the scan and then synchronized occurrence-by-occurrence.

- retrospective source review: **70/70 pages complete**;
- correction-bearing pages: **38**;
- correction-free pages: **32**;
- synchronization manifest: `../notes/historical-glyph-sync-manifest.json`;
- synchronization report: `../notes/historical-glyph-sync-report.json`;
- synchronization commit: `880978627191a122f55b50522d112d163faa7e10`;
- synchronized logical occurrences across canonical/provenance surfaces: **97**;
- global replacement used: **no**;
- source whitespace/layout preserved: **yes**;
- genuine same-edition controls on PDF **48, 62, 64 and 69**: **preserved / PASS**.

Retained first-pass part files were updated only where the matching audited occurrence existed; placeholder-era omissions were not synthesized from `full-text.md`.

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

## Batch history

- PDF 5–14: initial continuous draft; now dual-gate verified.
- PDF 15–24: first-pass draft retained as provenance; matching historical-glyph occurrences synchronized; canonical pages dual-gate verified.
- PDF 25–34: same status.
- PDF 35–44: same status; `தனபதி` remains restored where initially misread as `தளபதி`.
- PDF 45–54: same status.
- PDF 55–64: same status; preserves locked `பழுதார் வீதி` and PDF 64→65 quoted-poetry boundary.
- PDF 65–74: canonical range now dual-gate verified after retrospective backfill; retained first-pass part remains a provenance artifact with its original uncertainty history.
- PDF 75–84: draft complete, 10 batch markers; dual-gate verification pending.
- PDF 85–94: draft complete, 10 batch markers; dual-gate verification pending.
- PDF 95–104: draft complete, 7 batch markers numbered 108–114; dual-gate verification pending.
- PDF 105–109: final draft batch complete, 2 batch markers numbered **115–116**; dual-gate verification pending; preserves the PDF 104→105 continuation and locked `தூக்குமேடை` heading.

## Exact next activity

Resume at **PDF 75 / logical printed p.73** and perform **visual source-fidelity + historical-Tamil-glyph verification together**. Adjudicate markers **88–116** occurrence-by-occurrence. PDF 5–74 are closed and should not be reopened unless new direct source evidence requires a specific local correction. Structured derivatives stay blocked until both verification gates reach **105/105**.
