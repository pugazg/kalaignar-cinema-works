# அம்மையப்பன் — English Reader/Export Preflight QA

Status: **PASS**

This report records the executable whole-work integrity gate run after completion of the source-linked English translation and before generation of publication-facing reader/export derivatives.

## Authority and scope

The preflight reads the repository's frozen verified derivative layers directly:

- `translations/records/scene-001.json` through `scene-063.json`;
- immutable `dialogues/records/scene-001.json` through `scene-063.json`;
- `dialogues/source-role-resolved-records.json`;
- `songs/inventory.json`;
- `translations/index.json`.

It is read-only. Canonical Tamil, scene derivatives, immutable dialogue records, character mappings and song/performance evidence are not altered.

The booklet prints no scene numbers. All `ammaiyappan-sNNN` identifiers remain archival navigation derivatives only.

## Automated run

GitHub Actions workflow: `.github/workflows/ammaiyappan-english-reader-preflight.yml`  
Preflight implementation: `works/ammaiyappan/editions/en/audit_probe.py`

Passing run checkpoint:

- workflow run: **34025680568**;
- head commit: `ae554f92faf7a9b0f4005c42cc28c8b3e8e95d36`;
- Python: **3.12**;
- probe result: **PASS**.

## PASS results

| Check | Result |
|---|---:|
| Translation scene files | **63 / 63** |
| Verified translation units | **1,210 / 1,210** |
| Draft / review units | **0 / 0** |
| Dialogue-kind units | **1,025** |
| Stage-direction units | **181** |
| Song-reference units | **3** |
| Japa units | **1** |
| Literary-verse / written-text units | **0 / 0** |
| Immutable explicit dialogue records | **1,009** |
| Closed source-role supplements | **16** |
| Total dialogue authority | **1,025** |
| Dialogue/source-role links | **1,025 / 1,025 exactly once** |
| Missing / extra / duplicate dialogue links | **0 / 0 / 0** |
| Genuine cross-page translation units | **28** |
| Cross-page provenance/segment errors | **0** |
| Retained occurrence identities | **5 / 5** |
| Occurrence-linked source spans | **7** |
| Synthetic `(Scene ends.)` units | **0** |
| Units derived directly from decorative/structural stars | **0** |
| Page-order regressions | **0** |
| Unit-ID errors | **0** |
| Page-provenance errors | **0** |
| Scene/unit metadata errors | **0** |
| Audit warnings | **0** |
| Audit errors | **0** |

## Exact speaker-label / source-role provenance

The probe independently compared every dialogue-linked English unit against the closed source authority.

- all **1,009** immutable explicit records retain the exact Tamil `speaker_label`, `source-explicit-colon` origin and exact page provenance;
- all **16** source-role supplements retain their exact Tamil label, recorded origin and exact page provenance;
- scene 3 `பூங் ; ...` and scene 5 `திரு; ...` remain `source-explicit-noncolon-delimiter` records rather than being normalized to printed-colon dialogue;
- context-attributed supplements remain `source-context-attributed` and are never promoted into printed labels.

Missing, extra or duplicate source-record links: **0**.

## Cross-page integrity

The probe independently derived **28** genuine cross-page units from the scene records and confirmed that this ordered list exactly matches `translations/index.json`. Every cross-page unit retains multi-page provenance and matching `english_page_segments`; provenance errors and page-order regressions are **0**.

## Song / verse / performance integrity

The five closed source-visible occurrence identities are all represented with their intended source-span multiplicity:

- `ammaiyappan-song-001` — **1** link (`song-reference`);
- `ammaiyappan-song-002` — **1** link (`dialogue`);
- `ammaiyappan-song-003` — **1** link (`song-reference`);
- `ammaiyappan-song-004` — **2** links (`japa` + the separately printed labelled dialogue token);
- `ammaiyappan-song-005` — **2** links (the dialogue request + the separate performance cue).

Thus **5 occurrence identities / 7 intentionally distinct source-span links** are preserved. No absent lyric, title or authorship is introduced.

## Structural and navigation safeguards

PASS:

- source scene numbering remains `null` for all 63 archival scene records;
- archive ordinals remain navigation only;
- synthetic `(Scene ends.)` units: **0**;
- units whose source locator is a decorative/structural star: **0**;
- frozen source layers reported modified by the translation index: **0**.

## Validation scope

This is an **executable Python preflight run in GitHub Actions**, not merely a manual count reconciliation. The probe validates the repository's reader-critical invariants directly. It is not a JSON-Schema-library validation unless such a separate schema validator is later added and recorded.

## Gate disposition

**Reader/export preflight: PASS.**

The complete-verified 63-scene translation is cleared for deterministic publication-facing reader/export generation. The next activity is to generate **Markdown, standalone HTML and machine-readable JSON from the verified structured translation**, then run generated-output QA and produce an integrity manifest before Reading Room integration.
