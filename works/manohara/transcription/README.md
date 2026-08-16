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
- visually audited: **PDF 7–12 / logical printed pp.6–11 — 6 pages**;
- Batch 1 correction groups recorded: **13**, with **0 unresolved source readings**;
- Batch 1 corrections applied: **no — intentionally deferred until Part 01 has been fully audited**;
- next fidelity-audit page: PDF **13** / printed p. **12**;
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

The anchors remain `draft` during the Part 01 visual audit even when a page has already been inspected, because the scan-supported corrections are being accumulated for a consolidated Part 01 rewrite. Only after those corrections are applied will the affected anchors be promoted to `verified` or `review`.

OCR, film audio, subtitles, web quotations, memory and later editions are not canonical repair sources.

**Next:** continue the visual fidelity audit with **PDF 13–18 / printed pp.12–17**. Do not begin structured derivatives and do not promote Part 01 anchors before the accumulated corrections are applied.
