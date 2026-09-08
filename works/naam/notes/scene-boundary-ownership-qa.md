# நாம் — Scene boundary ownership QA

Result: **PASS**

The 45 source-numbered scene spans were generated only from the complete-verified canonical Tamil. Scene boundaries are the exact `## காட்சி...` headings already preserved in canonical transcription; no film audio, subtitle, OCR, web text or semantic reconstruction was used.

## Whole-work checks

- source scene numbers: **1–45 exactly; 0 gaps / 0 repeats / 0 out-of-order**;
- mapping start-PDF check: **45/45 PASS** against `mapping.md`;
- canonical page representation: **PDF 5–71 / 67 unique pages**;
- cross-page scenes: **34**;
- additional same-page scene starts: **11**;
- canonical scene-region SHA-256: `787695af1e3d5c3dae28085b76558df9efae73fe239c39e802989442fa593146`;
- joined scene-span SHA-256: `787695af1e3d5c3dae28085b76558df9efae73fe239c39e802989442fa593146`;
- joined-span equality: **PASS — exact byte-for-byte equality for the canonical region from `காட்சி 1` through the final screenplay text**;
- source text gaps / overlaps: **0 / 0**;
- canonical Tamil modified by this derivative phase: **0**.

## Scene ranges

| Scene | Start PDF | End PDF | File | Status |
|---:|---:|---:|---|---|
| 1 | 5 | 7 | `scene-001.md` | PASS |
| 2 | 7 | 8 | `scene-002.md` | PASS |
| 3 | 8 | 11 | `scene-003.md` | PASS |
| 4 | 11 | 13 | `scene-004.md` | PASS |
| 5 | 13 | 14 | `scene-005.md` | PASS |
| 6 | 14 | 16 | `scene-006.md` | PASS |
| 7 | 16 | 17 | `scene-007.md` | PASS |
| 8 | 17 | 19 | `scene-008.md` | PASS |
| 9 | 19 | 21 | `scene-009.md` | PASS |
| 10 | 21 | 24 | `scene-010.md` | PASS |
| 11 | 24 | 25 | `scene-011.md` | PASS |
| 12 | 25 | 25 | `scene-012.md` | PASS |
| 13 | 25 | 29 | `scene-013.md` | PASS |
| 14 | 29 | 31 | `scene-014.md` | PASS |
| 15 | 31 | 31 | `scene-015.md` | PASS |
| 16 | 31 | 32 | `scene-016.md` | PASS |
| 17 | 32 | 33 | `scene-017.md` | PASS |
| 18 | 33 | 34 | `scene-018.md` | PASS |
| 19 | 34 | 34 | `scene-019.md` | PASS |
| 20 | 34 | 35 | `scene-020.md` | PASS |
| 21 | 35 | 36 | `scene-021.md` | PASS |
| 22 | 36 | 38 | `scene-022.md` | PASS |
| 23 | 38 | 38 | `scene-023.md` | PASS |
| 24 | 38 | 42 | `scene-024.md` | PASS |
| 25 | 42 | 42 | `scene-025.md` | PASS |
| 26 | 42 | 43 | `scene-026.md` | PASS |
| 27 | 43 | 45 | `scene-027.md` | PASS |
| 28 | 45 | 45 | `scene-028.md` | PASS |
| 29 | 45 | 47 | `scene-029.md` | PASS |
| 30 | 47 | 49 | `scene-030.md` | PASS |
| 31 | 49 | 52 | `scene-031.md` | PASS |
| 32 | 52 | 54 | `scene-032.md` | PASS |
| 33 | 54 | 56 | `scene-033.md` | PASS |
| 34 | 56 | 58 | `scene-034.md` | PASS |
| 35 | 58 | 58 | `scene-035.md` | PASS |
| 36 | 58 | 60 | `scene-036.md` | PASS |
| 37 | 60 | 60 | `scene-037.md` | PASS |
| 38 | 60 | 62 | `scene-038.md` | PASS |
| 39 | 62 | 65 | `scene-039.md` | PASS |
| 40 | 65 | 65 | `scene-040.md` | PASS |
| 41 | 65 | 67 | `scene-041.md` | PASS |
| 42 | 67 | 67 | `scene-042.md` | PASS |
| 43 | 67 | 68 | `scene-043.md` | PASS |
| 44 | 68 | 68 | `scene-044.md` | PASS |
| 45 | 68 | 71 | `scene-045.md` | PASS |

## Gate result

**Scene-text derivative phase CLOSED / COMPLETE-VERIFIED.** Dialogue indexing may now begin from these derivatives while canonical Tamil remains the upstream authority.

## Next activity

Begin Phase 6 dialogue indexing from the 45/45 complete-verified scene derivatives. Inventory every explicit source speaker label exactly as printed, create immutable dialogue records in scene/source order with PDF provenance, keep cross-page labelled utterances as one logical record, leave source-unlabelled speech unlabelled, and run whole-work dialogue coverage QA before starting the character/entity index. Do not alter canonical Tamil or scene text except for later source-supported corrections.
