# அம்மையப்பன் — scene boundary ownership QA

Status: **PASS**

## Inputs

- canonical Tamil: `transcription/full-text.md` — **105/105 dual-gate verified**;
- segmentation preflight: `notes/scene-segmentation-preflight.json` — **PASS**;
- planned/generated archive segments: **63**.

## Assertions

- canonical source-visible headings used as boundaries: **63**;
- generated scene files: **63/63**;
- source-numbered scenes invented: **0**;
- pre-boundary screenplay body lines omitted: **0**;
- gaps between consecutive derivative spans: **0**;
- overlaps between consecutive derivative spans: **0**;
- joined derivative spans equal canonical body from first scene heading through PDF 109 EOF: **PASS**;
- canonical derivative-body SHA-256: `602a5a4d584b10570bae66b31c91c3db5ec69859b0c5f41b03209358e9d05ad2`;
- joined scene-span SHA-256: `602a5a4d584b10570bae66b31c91c3db5ec69859b0c5f41b03209358e9d05ad2`;
- scene-file canonical-span roundtrip errors: **0**;
- canonical PDF pages represented across scene derivatives: **105/105 — PDF 5–109**;
- missing canonical PDF pages: **0**.

## Boundary policy

Page breaks alone are not scene boundaries. Every boundary is a source-visible heading preserved in the verified canonical transcription. `ammaiyappan-sNNN` identifiers are derivative navigation only.

## Disposition

**PASS — scene-text derivatives are complete-verified. Dialogue indexing is unblocked.**
