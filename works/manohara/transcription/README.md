# மனோகரா — canonical Tamil transcription

Status: **`draft-complete`; full first pass complete, fidelity audit not-started**.

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
- visual fidelity audit: **not-started**;
- next fidelity-audit page: PDF **7** / logical printed p. **6**;
- structured derivatives: **blocked until the Tamil source layer is fidelity-verified**.

The aggregate transcription index is [`full-text.md`](full-text.md). Source-order batch files are listed in [`parts/README.md`](parts/README.md).

Each page has a stable source anchor. Because the main text opens on PDF 7 with its printed folio suppressed, its anchor records the mapped logical page explicitly:

```md
<!-- source: pdf=7 printed-logical=6 folio=suppressed status=draft -->
```

From PDF 8 onward the visible/continuous interior pagination is recorded normally, for example:

```md
<!-- source: pdf=8 printed=7 status=draft -->
```

`draft-complete` means only that every canonical page now has a first-pass transcription. It does **not** mean visually verified. A separate complete fidelity audit against the rendered scan must now begin from PDF 7. OCR, film audio, subtitles, web quotations, memory and later editions are not canonical repair sources.

**Next:** begin the visual fidelity audit from **PDF 7 / logical printed p.6**, applying corrections only when supported by the rendered scan and recording unresolved readings explicitly.
