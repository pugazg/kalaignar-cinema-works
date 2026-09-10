# வண்டிக்காரன் மகன் — scene boundary ownership QA

Status: **PASS**

## Inputs

- closed canonical Tamil screenplay: `transcription/pages/006.md`–`087.md`;
- source-visible canonical scene headings: **72**;
- generated source-led scene derivatives: **72**.

## Corrective boundary finding

Derivative construction exposed one stale inventory omission: canonical PDF 10 contains source-visible `காட்சி — 4 எ.`. It is a real scene boundary and is retained as source scene ID `4-எ`. The earlier 71-heading inventory is superseded by the canonical **72-heading** sequence.

## Assertions

- source-visible scene headings used as boundaries: **72/72**;
- generated scene files: **72/72**;
- source scene labels normalized or renumbered in scene text: **0**;
- source-text corrections performed by derivative builder: **0**;
- gaps between consecutive scene spans: **0**;
- overlaps between consecutive scene spans: **0**;
- ordered scene spans reconstruct the canonical scene-bearing body exactly: **PASS**;
- canonical scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- joined scene-span SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- derivative file roundtrip errors: **0**;
- screenplay PDF pages represented: **82/82 — PDF 6–87**;
- missing screenplay PDF pages: **0**;
- excluded non-scene matter: PDF 4–5 foreword, PDF 88–90 credits/back cover, and the work-title line preceding scene 1 on PDF 6.

## Boundary ownership rule

A scene begins at its source-visible `காட்சி` heading and owns every canonical character until immediately before the next source-visible `காட்சி` heading. Page breaks are not boundaries. Multiple scene starts on one page are allowed without duplicate text ownership.

## Disposition

**PASS — 72/72 source-led scene-text derivatives are complete-verified. Dialogue indexing is unblocked.**
