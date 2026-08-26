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
| PDF 24–35 / printed pp.16–27, scenes 16–29 | canonical Part 02 reconciled and final cleanup complete | scenes 16–29 reconciled through PDF 35 | scenes 16–29 reconciled with stable record IDs and unchanged counts; scene-29 PDF-36 continuation deferred | **complete through Part 02** |
| PDF 36–63 / printed pp.28–55 | **canonical Part 03 reconciled from corrected Markdown** | pending | pending | **next derivative work: scene-29 continuation + scenes 30–48** |
| PDF 64–112 / printed pp.56–104 | not yet reconciled in this pass | not yet reconciled | not yet reconciled | pending |

### Part 02 closure

`transcription/parts/part-02-pdf-14-35.md` is now closed for this corrected-Markdown pass. After the primary merge, a final consistency cleanup resolved remaining Markdown extraction artifacts and structural-order drift already adjudicated from the scan/scene evidence, including the scene-17 `சூனியக்கார` reading, `கலங்குதய்யோ`, `காதிருந்தும் செவிடனாய்`, page-35 `டே...`, and the correct structural placement of scenes 22–27 material.

### Part 03 canonical reconciliation

`transcription/parts/part-03-pdf-36-63.md` has now been rebuilt from the corrected Markdown baseline for **Play Pages 28–55 / PDF 36–63**. Iteration commentary embedded in the supplied Markdown was excluded rather than imported as source text. The page anchors remain explicit so the scene/dialogue pass can now reconcile against a stable canonical source layer.

This Part-03 canonical merge includes the corrected forms and labels supplied by the user witness, including `பூமாலை`, `புண்யகோடி`, the corrected labour-movement passages, the scene-31 `பாண்டியன் என் சொல்லை` performance reference, and the corrected scene-42/43 `கலப்படம்` material. The existing special scan-supported scene-31 song-title correction remains consistent with this witness.

### Derivative boundary

Scenes 1–29 are reconciled through **PDF 35 / printed p.27**. Scene 29 crosses the transcription-part boundary: its **PDF 36 / printed p.28 continuation** is now corrected canonically but still needs to be propagated to `scene-29.md` and its immutable dialogue records. After that, scenes 30–48 require the same corrected-canonical reconciliation.

Exact speaker labels have already changed during this pass (`பூமாலை`, `புண்யகோடி`, `குரல்`, `குண்டுமணி`, `சமையல்காரன்`). The existing character-label inventory and entity mappings therefore remain known-stale and will be regenerated only after the full dialogue reconciliation reaches a stable boundary.

## Execution order from here

- Reconcile scene 29's **PDF-36 continuation**, then scenes **30–48**, against corrected canonical Part 03.
- Preserve stable dialogue IDs and existing record boundaries unless the corrected source proves the old segmentation itself wrong.
- Continue the corrected-Markdown-first canonical reconciliation into Parts 04–05.
- Rebuild character mappings after the dialogue label set stabilizes.
- Reconcile English / reader / EPUB derivatives for semantic source changes instead of leaving them silently stale.
- Restore final archive status only after all affected layers agree.

The previous full-volume `104 verified / 0 review` claim is **superseded for textual correctness by this reconciliation pass until the pass closes**.
