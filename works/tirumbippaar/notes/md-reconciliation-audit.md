# திரும்பிப்பார்! — corrected Markdown reconciliation audit

Status: **in progress — full-volume source text reopened for correction**

Date opened: 2026-08-26

## Correction witness and authority

The user supplied `thirumbipaar.md` as a corrected transcription specifically to repair OCR / old-Tamil-glyph errors remaining in the repository transcription.

For this reconciliation pass:

1. **Use the user-supplied `thirumbipaar.md` as the primary correction baseline when comparing against the existing repository text.**
2. The supplied scan `TVA_BOK_0014652_திரும்பிப்பார்.pdf` remains the final visual authority if the corrected Markdown and the printed page appear to disagree, or if a reading is doubtful.
3. Do **not** trust the earlier `verified` label as proof that a reading is correct. This pass was opened because systematic old-print glyph loss survived the earlier audit.
4. Do not silently modernize beyond the corrected Markdown. If a wording or glyph remains doubtful, inspect the scan rather than infer from context.
5. Every confirmed source-text correction must ultimately be propagated to affected scene, dialogue, character-label, translation and publication derivatives so the archive does not retain contradictory layers.

## First confirmed systematic error

The earlier repository transcription dropped the terminal old-print glyph in forms such as:

- repository `பூமால்` → corrected `பூமாலை`
- repository `இல்ல` → corrected `இல்லை`

These are not treated as intentional source spellings in this pass. They demonstrate that the previous visual audit can contain systematic glyph-reading errors and justify reopening all PDF 9–112 / printed pp.1–104.

## Input coverage check

The supplied corrected Markdown contains **104 `Play Page` sections, numbered 1 through 104 without gaps**, matching the booklet main-text range PDF 9–112 / printed pp.1–104.

Iteration commentary / extraction-review prose embedded between Markdown batches is not source text and must not be imported into the canonical transcription.

## Progress

| Reconciliation unit | Canonical Tamil | Scene derivatives | Dialogue derivatives | Status |
|---|---|---|---|---|
| PDF 9–13 / printed pp.1–5 | reconciled from corrected Markdown | scenes 1–4 reconciled | affected records in scenes 1, 2 and 4 reconciled; scene 3 dialogue unchanged | complete for this range |
| PDF 14–18 / printed pp.6–10 | reconciled as the opening portion of Part 02 | scenes 5–10 reconciled | affected records in scenes 5–9 reconciled; scene 10 remains zero-dialogue | complete for this range |
| PDF 19–24 / printed pp.11–16 through scene 15 | canonical Part 02 reconciled | scene 11 retained from scan-supported structure; scenes 12–15 reconciled | scene 11 remains zero-dialogue; scenes 12–15 reconciled with stable record IDs | complete for this range |
| PDF 24–35 / printed pp.16–27, scenes 16–29 | canonical Part 02 reconciled and final cleanup complete | scenes 16–29 reconciled through PDF 35 | scenes 16–29 reconciled with stable record IDs | **complete through Part 02** |
| PDF 36–63 / printed pp.28–55 | **canonical Part 03 reconciled from corrected Markdown** | scene 29 PDF-36 continuation + scenes 30–48 reconciled; scene 48 retains its PDF-64 continuation | corresponding dialogue shards reconciled; scene 41 recovered two omitted labelled utterances | **Part 03 derivative reconciliation complete** |
| PDF 64–91 / printed pp.56–83 | **not yet canonically reconciled in this pass** | scene 48 PDF-64 continuation already reconciled as a cross-part derivative | scene 48 PDF-64 records already reconciled; later scenes pending | **next canonical range: Part 04** |
| PDF 92–112 / printed pp.84–104 | not yet reconciled in this pass | not yet reconciled | not yet reconciled | pending |

### Part 02 closure

`transcription/parts/part-02-pdf-14-35.md` is closed for this corrected-Markdown pass. After the primary merge, a final consistency cleanup resolved remaining Markdown extraction artifacts and structural-order drift already adjudicated from the scan/scene evidence, including the scene-17 `சூனியக்கார` reading, `கலங்குதய்யோ`, `காதிருந்தும் செவிடனாய்`, page-35 `டே...`, and the correct structural placement of scenes 22–27 material.

### Part 03 canonical reconciliation

`transcription/parts/part-03-pdf-36-63.md` was rebuilt from the corrected Markdown baseline for **Play Pages 28–55 / PDF 36–63**. Iteration commentary embedded in the supplied Markdown was excluded rather than imported as source text. Page anchors remain explicit.

This canonical merge includes corrected forms and labels supplied by the user witness, including `பூமாலை`, `புண்யகோடி`, the corrected labour-movement passages, the scene-31 `பாண்டியன் என் சொல்லை` performance reference, and the corrected scene-42/43 `கலப்படம்` material.

### Part 03 derivative closure

The scene/dialogue reconciliation now reaches **scene 48**, including scene 48's genuine cross-part continuation on **PDF 64 / printed p.56**. This does **not** mean canonical Part 04 has been reconciled; it only preserves the complete source-supported scene-48 derivative before the Part-04 canonical pass begins.

Important derivative corrections in this closure include:

- scene 29's PDF-36 continuation propagated from corrected canonical Part 03;
- scenes 30–48 reconciled against the corrected Markdown and, where needed, the rendered scan;
- scene 34 retains the source's unlabelled `பாண்டியன்` line without inventing a dialogue speaker;
- scene 42 and scene 43 are restored as separate source-supported segments;
- scene 43 remains a legitimate **zero-dialogue** scene, with its `கலப்படம்` performance/non-dialogue material retained in `scene-43.md` rather than misplaced in scene 42;
- scene 44's unlabelled platform-speech continuation remains outside the immutable labelled-dialogue layer;
- source-exact label corrections such as `பூமாலை` and `புண்யகோடி` were propagated to the affected dialogue shards.

### Scene 41 recovered dialogue records

Fresh source reconciliation proved that the old dialogue extraction omitted two explicitly labelled utterances on PDF 56 / printed p.48. They were added without renumbering any existing stable ID:

- `tirumbippaar-s041-d037` — `பூமாலை` — beginning `நீ வீட்டிலா இருக்கிறாய்... 'வீடு' என்றாவது...`
- `tirumbippaar-s041-d038` — `பரந்தாமன்` — beginning `அக்கா ! உன்னை உணர்ந்துகொண்டேன்...`

Existing `tirumbippaar-s041-d034` remains the same stable record ID and now preserves the genuine PDF 56→57 / printed 48→49 page break around `அன்பைக் கேட்-` / `காமல் ஐஸ்வரியத்தைக் கேட்கும்...`.

Accordingly:

- scene 41 dialogue count: **38**
- whole-work immutable labelled-dialogue count: **1,042**
- existing dialogue IDs were not renumbered.

### Current synchronization boundary

- **Canonical corrected-Markdown boundary:** PDF **9–63** / printed pp. **1–55** (Parts 01–03).
- **Scene/dialogue derivative boundary:** through **scene 48**, including its PDF **64** / printed p. **56** continuation.
- **Next canonical work:** Part 04, PDF **64–91** / printed pp. **56–83**.

Exact speaker labels have changed during this pass (`பூமாலை`, `புண்யகோடி`, `குரல்`, `குண்டுமணி`, `சமையல்காரன்`). The existing character-label inventory and entity mappings therefore remain **known-stale** and must not be treated as synchronized yet.

English translations, reader/export derivatives and EPUB outputs may likewise be stale wherever corrected Tamil changes meaning or source linkage. Their historical verification status is not a current synchronization claim.

## Execution order from here

- Reconcile canonical **Part 04 / PDF 64–91 / printed pp.56–83** from the corrected Markdown baseline, using the rendered scan to adjudicate doubtful readings and physical structure.
- Propagate each corrected Part-04 source reading to its scene/dialogue derivatives while preserving stable IDs and genuine page provenance.
- Continue through Part 05.
- Rebuild character mappings only after the dialogue correction pass reaches a stable full-work boundary.
- Reconcile English / reader / EPUB derivatives for semantic source changes instead of leaving them silently stale.
- Restore final archive status only after all affected layers agree.

The previous full-volume `104 verified / 0 review` claim is **superseded for textual correctness by this reconciliation pass until the pass closes**.
