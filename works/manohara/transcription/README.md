# மனோகரா — canonical Tamil transcription

Status: **`draft-complete`; full first pass complete, fidelity audit in progress; Parts 01–04 verified**.

`../mapping.md` is `verified`. This edition does not print numbered scenes; the source-visible transition system is documented in `../notes/scene-heading-audit.md` without inventing scene numbers.

The canonical screenplay/dialogue range is PDF **7–88** / logical printed pp. **6–87**. The rendered scan, not the OCR layer, controls every reading.

## Current checkpoint

- canonical range: PDF **7–88** / logical printed pp. **6–87** — **82 pages**;
- first-pass coverage: **82/82 pages — complete**;
- verified pages: **60** — PDF **7–66 / logical printed pp.6–65**;
- draft pages: **22** — PDF **67–88**;
- review pages: **0**;
- visual fidelity audit: **in-progress**;
- visually audited: **PDF 7–78 / logical printed pp.6–77 — 72 pages**;
- Part 01: **complete-verified — 24 pages, 89 corrections applied, post-application recheck passed**;
- Part 02: **complete-verified — 12 pages, 43 corrections applied, post-application recheck passed**;
- Part 03: **complete-verified — 12 pages, 48 reviewed correction groups applied, post-application recheck passed**;
- Part 04: **complete-verified — 12 pages, 63 reviewed correction groups applied, post-application recheck passed**;
- Part 05 visual audit: **complete — PDF 67–78 / printed pp.66–77 — 12/12 pages audited**;
- Part 05 correction groups pending application: **69** — Batch 11: 33; Batch 12: 36;
- unresolved source readings: **0**;
- structured derivatives: **blocked until the remaining Tamil source layer is fidelity-verified**.

The aggregate transcription index is [`full-text.md`](full-text.md). Source-order batch files are listed in [`parts/README.md`](parts/README.md). The historical fidelity ledger is [`../notes/fidelity-audit.md`](../notes/fidelity-audit.md); Part 03's final disposition is recorded in [`../notes/fidelity-audit-part03-final.md`](../notes/fidelity-audit-part03-final.md), Part 04's final disposition is recorded in [`../notes/fidelity-audit-part04-final.md`](../notes/fidelity-audit-part04-final.md). Part 05 audit records are [`../notes/fidelity-audit-part05-batch11.md`](../notes/fidelity-audit-part05-batch11.md) and [`../notes/fidelity-audit-part05-batch12.md`](../notes/fidelity-audit-part05-batch12.md).

Parts 01–04 carry verified page anchors continuously from PDF 7 through PDF 66. Parts 05–06 remain `draft`. The **69** Part 05 corrections found across PDF 67–78 have deliberately **not** been written back yet. Part 05 must now receive one controlled source-led rewrite, followed by mechanical checks and a separate visual recheck before any anchor is promoted.

Part 04 was audited in two six-page passes. Batch 9 recorded 33 corrections for PDF 55–60 and Batch 10 recorded 30 corrections for PDF 61–66. All **63** reviewed corrections were applied in commit `fd9e993a21deae53a9b4310fd2022384e8ccb7c1` while all anchors remained `draft`. The corrected file's Git blob matched the independently calculated expected blob `d0936ed84f4809d637b8d88e80a9309f13072d61`. PDF 55–66 was then visually rechecked against the rendered scan with **0 unresolved readings** and no additional correction required. All twelve Part 04 anchors were promoted in `0795ea5d668cecda8a258563d7b93d0c27f7dc29`; the verified blob is `42253eb2489e875f7b729a8aab2f084394463e85`.

OCR, film audio, subtitles, web quotations, memory and later editions are not canonical repair sources.

**Next:** apply all **69** reviewed Part 05 corrections to `parts/part-05-pdf-67-78.md` in one controlled source-led rewrite while keeping all twelve anchors `draft`; mechanically verify the result, then visually recheck PDF **67–78** against the rendered scan. Promote Part 05 only if that recheck passes with no unresolved source reading.
