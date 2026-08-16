# மனோகரா — English Reader/Export Preflight QA

Status: **PASS**

This report records the whole-work integrity gate run after completion of the source-linked English translation and before generation of publication-facing reader/export derivatives.

## Authority and scope

The preflight reads the repository's verified derivative layers directly:

- `translations/records/scene-001.json` through `scene-057.json`;
- all immutable `dialogues/records/scene-001.json` through `scene-057.json`;
- `songs/inventory.json`;
- `translations/index.json`.

The audit does not alter canonical Tamil, scene derivatives, immutable dialogue records, character mappings or song evidence.

The booklet prints no scene numbers. The 57 `manohara-sNNN` segments remain archival navigation derivatives only.

## Automated run

GitHub Actions workflow: `.github/workflows/manohara-english-preflight.yml`

Preflight implementation: `works/manohara/editions/en/audit_probe.py`

Passing run:

- head commit: `b2cd2a597a9f2eeb0e8016b78102ec67fe05ae7e`;
- workflow run: `31956654990`;
- conclusion: **success**;
- Python: 3.12.

An initial diagnostic run correctly exposed two overly broad assertions in the new audit probe itself: it treated the source-labelled scene-11 war proclamation as ordinary dialogue-only linkage even though the verified translation intentionally classifies it as `chant`, and it mistook contextual descriptions mentioning a preceding structural star for translations of that star. The probe was narrowed to the repository's actual schema/policy and rerun. **No translation record or source derivative was changed to make the audit pass.**

## PASS results

| Check | Result |
|---|---:|
| Translation scene files | **57 / 57** |
| Verified translation units | **1,190 / 1,190** |
| Draft units | **0** |
| Review units | **0** |
| Dialogue-kind units | **1,009** |
| Stage-direction units | **173** |
| Song-reference units | **6** |
| Chant units | **1** |
| Written-text units | **1** |
| Immutable dialogue records | **983** |
| Immutable dialogue links | **983 / 983 exactly once** |
| Missing dialogue links | **0** |
| Extra dialogue links | **0** |
| Duplicate dialogue links | **0** |
| Direct source-unlabelled spoken units | **27** |
| Genuine cross-page translation units | **17** |
| Song/performance occurrence links | **6 / 6 exactly once** |
| Missing song occurrence links | **0** |
| Extra song occurrence links | **0** |
| Synthetic `(Scene ends.)` units | **0** |
| Units derived directly from decorative/structural stars | **0** |
| Page-order regressions | **0** |
| Unit-ID errors | **0** |
| Page-provenance errors | **0** |
| Scene/unit metadata errors | **0** |
| Audit warnings | **0** |
| Audit errors | **0** |

## Cross-page integrity

The following **17** English units retain multi-page source provenance in source order:

`manohara-en-s001-u006`, `manohara-en-s008-u008`, `manohara-en-s008-u077`, `manohara-en-s011-u007`, `manohara-en-s013-u017`, `manohara-en-s015-u006`, `manohara-en-s021-u023`, `manohara-en-s036-u035`, `manohara-en-s036-u044`, `manohara-en-s036-u080`, `manohara-en-s048-u009`, `manohara-en-s048-u044`, `manohara-en-s052-u018`, `manohara-en-s055-u010`, `manohara-en-s055-u016`, `manohara-en-s055-u023`, `manohara-en-s055-u029`.

## Source-unlabelled speech integrity

The preflight independently found the same **27** dialogue-kind units that have no immutable labelled-dialogue record and verified that each retains `speaker_label: null`. No speaker was inferred merely from dramatic context.

This includes the final four colon-only continuations in scene 56. The scene-57 `பத்மா! என் இதயராணி...` continuation is not in this set because the source sequence is intentionally preserved inside the preceding explicit king's immutable dialogue record.

## Song/performance integrity

The translation links exactly once to each source-visible song/performance occurrence:

- `manohara-song-001`;
- `manohara-song-002`;
- `manohara-song-003`;
- `manohara-song-004`;
- `manohara-song-005`;
- `manohara-song-006`.

No absent lyric was reconstructed or imported.

## Structural-star safeguard

No decorative `★` separator is represented as reader prose. In particular, there are **0** synthetic `(Scene ends.)` units and **0** translation units whose source locator is a decorative/structural star.

The probe deliberately distinguishes a real stage direction whose provenance note says it occurs *after* a structural star from a unit actually derived from the star itself.

## Gate disposition

**Reader/export preflight: PASS.**

The verified translation layer is now cleared for generation of deterministic publication-facing derivatives. The next activity may create the English reader/export package (Markdown, standalone HTML and machine-readable JSON), then run whole-work generated-output QA and produce an integrity manifest before any Reading Room integration.
