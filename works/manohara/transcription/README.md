# மனோகரா — canonical Tamil transcription

Status: **draft; first pass in progress**.

`../mapping.md` is `verified`. This edition does not print numbered scenes; the source-visible transition system is documented in `../notes/scene-heading-audit.md` without inventing scene numbers.

The canonical screenplay/dialogue range is PDF **7–88** / logical printed pp. **6–87**. The rendered scan, not the OCR layer, controls every reading.

## Current checkpoint

- canonical range: PDF **7–88** / logical printed pp. **6–87** — **82 pages**;
- first-pass coverage: **48/82 pages**;
- completed first-pass range: PDF **7–54** / logical printed pp. **6–53**;
- draft pages: **48**;
- verified pages: **0**;
- review pages: **0**;
- next first-pass page: PDF **55** / logical printed p. **54**;
- visual fidelity audit: **not-started**;
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

First-pass `draft` does **not** mean visually verified. A separate complete fidelity audit against the rendered scan must follow after first-pass coverage is complete. OCR, film audio, subtitles, web quotations, memory and later editions are not canonical repair sources.

**Next:** continue canonical Tamil first-pass transcription from **PDF 55 / logical printed p.54**, in source order, using a meaningful multi-page batch and stable page anchors.
