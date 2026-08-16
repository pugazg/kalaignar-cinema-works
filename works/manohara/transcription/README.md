# மனோகரா — canonical Tamil transcription

Status: **`draft-complete`; full first pass complete, fidelity audit in progress**.

`../mapping.md` is `verified`. This edition does not print numbered scenes; the source-visible transition system is documented in `../notes/scene-heading-audit.md` without inventing scene numbers.

The canonical screenplay/dialogue range is PDF **7–88** / logical printed pp. **6–87**. The rendered scan, not the OCR layer, controls every reading.

## Current checkpoint

- canonical range: PDF **7–88** / logical printed pp. **6–87** — **82 pages**;
- first-pass coverage: **82/82 pages — complete**;
- completed first-pass range: PDF **7–88** / logical printed pp. **6–87**;
- draft pages: **82**;
- verified pages: **0**;
- review pages: **0**;
- first-pass pages remaining: **0**;
- visual fidelity audit: **in-progress**;
- visually audited: **PDF 7–30 / logical printed pp.6–29 — 24 pages**;
- Part 01 visual-audit coverage: **complete**;
- correction groups recorded for Part 01: **89**, with **0 unresolved source readings**;
- accumulated Part 01 corrections applied: **no — consolidated application is now the required next gate**;
- next source page after Part 01: PDF **31** / printed p. **30**, but no further audit batch should begin until the PDF 7–30 corrections have been applied and rechecked;
- structured derivatives: **blocked until the Tamil source layer is fidelity-verified**.

The aggregate transcription index is [`full-text.md`](full-text.md). Source-order batch files are listed in [`parts/README.md`](parts/README.md). The fidelity ledger is [`../notes/fidelity-audit.md`](../notes/fidelity-audit.md).

Each page has a stable source anchor. Because the main text opens on PDF 7 with its printed folio suppressed, its anchor records the mapped logical page explicitly:

```md
<!-- source: pdf=7 printed-logical=6 folio=suppressed status=draft -->
```

From PDF 8 onward the visible/continuous interior pagination is recorded normally, for example:

```md
<!-- source: pdf=8 printed=7 status=draft -->
```

The anchors remain `draft` even though PDF 7–30 has now been visually audited, because the scan-supported corrections have not yet been written back to the canonical Part 01 file. Only after the consolidated rewrite and a post-application recheck may the 24 affected anchors be promoted to `verified` or `review`.

Batch 4 (PDF 25–30) records important source restorations including the omitted `என்னை அவன் வெறுக்கலாம்—ஆனால் அவன்`, `ரத்தின சிம்மாசனம்`, `வீரவாள் வரும் என் செய்தி கூறும்!`, repeated `மறைந்து மறைந்து`, `மீன் கொடி`, `புலிக் கொடியைப் ராஜப்ரியன்`, `நீர் வீரனெனில்`, `லக்ஷணத்தைப்பற்றி`, the omitted `கைதி - பாதுகாப்புக் கைதி!`, and the source forms `(உள்ளேவந்து)` and `பரவாயில்ல.`.

OCR, film audio, subtitles, web quotations, memory and later editions are not canonical repair sources.

**Next:** apply all **89** recorded PDF **7–30** corrections to `parts/part-01-pdf-7-30.md` in one controlled source-led rewrite. Recheck that rewritten range against the audit ledger; if it passes with no unresolved reading, promote all **24 Part 01 anchors** to `verified` before continuing at PDF **31 / printed p.30**.
