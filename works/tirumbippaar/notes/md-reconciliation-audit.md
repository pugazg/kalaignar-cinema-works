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

## Execution order

- Compare repository canonical Tamil against corrected Markdown page by page.
- Use the PDF only to adjudicate doubt or apparent conflict.
- Record confirmed corrections by PDF / printed page.
- Update canonical transcription parts.
- Reconcile scene-text derivatives.
- Reconcile immutable dialogue text / exact source labels only where the corrected source requires it; preserve stable record IDs where the source utterance itself remains the same record.
- Recheck character mappings if an exact source label changes.
- Reconcile English / reader / EPUB derivatives for semantic source changes instead of leaving them silently stale.
- Restore final archive status only after all affected layers agree.

The previous full-volume `104 verified / 0 review` claim should therefore be read as **superseded for textual correctness by this reconciliation pass until the pass closes**.
