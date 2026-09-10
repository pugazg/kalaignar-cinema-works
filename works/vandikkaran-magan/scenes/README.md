# வண்டிக்காரன் மகன் — scene-text derivatives

**Stage:** **COMPLETE-VERIFIED**  
**Source-visible scene-heading occurrences:** **72**  
**Generated scene-text derivatives:** **72/72**  
**Boundary ownership:** **PASS — 0 gaps / 0 overlaps / 0 duplicate text ownership**

This directory is built only from the closed canonical Tamil screenplay in `../transcription/pages/006.md` through `087.md`. It does not replace or normalize the canonical source layer.

## Source-scene policy

The booklet prints its own scene labels. `scene-001.md` through `scene-072.md` are derivative filenames only. The authoritative labels are the 72-item sequence in `index.json`, including source-visible `4-எ` at PDF 10, later suffix inserts, and combined `45-46`.

## Boundary policy

Each derivative begins at a source-visible `காட்சி` heading and ends immediately before the next such heading, or at screenplay EOF for scene `56`. Cross-page continuations, decorative stars, songs, location captions, spelling, punctuation, speaker labels and stage directions remain inside their exact canonical span.

PDF 4–5 foreword and PDF 88–90 credit/back-cover matter are excluded. The work-title line before scene 1 on PDF 6 is work-level metadata, not scene body.

## QA

- source-heading count: **72/72**;
- screenplay page coverage: **82/82 — PDF 6–87**;
- ordered spans reconstruct canonical scene body: **PASS**;
- gaps / overlaps: **0 / 0**;
- derivative roundtrip errors: **0**;
- canonical scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- joined derivative-span SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`.

See `../notes/scene-boundary-ownership-qa.md`.

## Downstream gate

Scene-text derivatives remain **COMPLETE-VERIFIED**. Downstream dialogue indexing is **744 records / COMPLETE-VERIFIED / QA PASS** and character/entity indexing is **32 entities / 38/38 labels / 744/744 dialogue records / COMPLETE-VERIFIED / QA PASS**. Song/performance authorship is **READY-NEXT**.
