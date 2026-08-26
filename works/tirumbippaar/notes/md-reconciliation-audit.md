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
| PDF 19–24 / printed pp.11–16 through scene 15 | canonical Part 02 already corrected | scene 11 retained from scan-supported structure; scenes 12–15 reconciled | scene 11 remains zero-dialogue; scenes 12–15 reconciled with stable record IDs | complete through scene 15 |
| PDF 24–35 / printed pp.16–27, scenes 16–29 | canonical Part 02 corrected from Markdown baseline | scenes 16–29 reconciled | scenes 16–29 reconciled with stable record IDs and unchanged counts | **complete through Part 02** |
| PDF 36–112 / printed pp.28–104 | not yet reconciled in this pass | not yet reconciled | not yet reconciled | pending |

### Part 02 canonical merge

`transcription/parts/part-02-pdf-14-35.md` has been rewritten in source order from the corrected Markdown baseline for **PDF 14–35 / printed pp.6–27**. This establishes the user's corrected text as the main correction witness before all remaining derivatives are propagated.

The scan is still used where the Markdown omits or conflicts with visible structure. For example, PDF 19 visibly carries the scene-11 location label `[ஆறு`; the existing scene derivative retains it even though that label is absent from the Markdown extraction. Likewise, the corrected Markdown's accidental non-Tamil extraction token `అది` is not imported; the source-language form is `அது`.

### Derivative reconciliation through scene 29 / end of Part 02

Scenes 16–29 and their dialogue shards are now reconciled against the corrected Part-02 text. Stable dialogue IDs and the existing per-scene record counts were retained. Scene 25 and scene 26 remain legitimate zero-dialogue scenes.

Important exact-label corrections now propagated in this range include:

- `பூமால்` → `பூமாலை`;
- `புண்ணகோடி` → `புண்யகோடி`;
- `குணமணி` → `குண்டுமணி`;
- scene 21 `சமையல்காரி` → source-supported `சமையல்காரன்`.

Important text restorations include the corrected scene-17 elopement/deception passage, scene-20 railway conversation, scene-25 `நளன்` narration, scene-26 `மாலுமிகளுக்கு வழி காட்டும் தீபஸ்தம்பம்`, scene-28 examination-number exchange, and scene-29 labour-slogan / `பாட்டாளியின் குரல்` setup.

The PDF was used to adjudicate obvious remaining extraction doubts in the corrected Markdown rather than importing them blindly. In particular, PDF 25 supports `சூனியக்கார ... / சூனியக்காரன்` in scene 17, PDF 29 supports `காதிருந்தும் செவிடனாய்`, and PDF 30 preserves the structural scene-22 heading `[ஹோட்டலறை` and scene-23 `[மிருக காட்சிசாலை` layout.

Scene 29 crosses the transcription-part boundary. Its **PDF 34–35 / printed pp.26–27** portion is reconciled from the corrected Part-02 witness; its already stored **PDF 36 / printed p.28** continuation has intentionally been left textually unchanged until Part 03 is opened against the corrected Markdown.

Because exact speaker labels have changed during this pass, the existing character-label inventory and downstream entity mappings are now known to be stale and will be regenerated after the dialogue reconciliation pass reaches a stable full-work boundary. English / reader / EPUB derivatives likewise remain intentionally unsynchronized while the 104-page correction pass is open.

## Execution order from here

- Open **Part 03 / PDF 36–63 / printed pp.28–55** against the corrected Markdown, beginning with the PDF-36 continuation of scene 29 and then scene 30 onward.
- Propagate each confirmed Part-03 correction to its scene/dialogue derivatives while preserving stable dialogue IDs.
- Recheck character mappings after the dialogue label set stabilizes.
- Continue the corrected-Markdown-first canonical reconciliation into Parts 04–05.
- Reconcile English / reader / EPUB derivatives for semantic source changes instead of leaving them silently stale.
- Restore final archive status only after all affected layers agree.

The previous full-volume `104 verified / 0 review` claim is **superseded for textual correctness by this reconciliation pass until the pass closes**.
