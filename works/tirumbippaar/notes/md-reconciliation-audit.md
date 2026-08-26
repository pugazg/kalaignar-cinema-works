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
| PDF 19–35 / printed pp.11–27 | canonical Part 02 now replaced from the corrected Markdown baseline | pending reconciliation | pending reconciliation | **next derivative work** |
| PDF 36–112 / printed pp.28–104 | not yet reconciled in this pass | not yet reconciled | not yet reconciled | pending |

### Part 02 canonical merge

`transcription/parts/part-02-pdf-14-35.md` has now been rewritten from the corrected Markdown source order for **PDF 14–35 / printed pp.6–27**. This intentionally establishes the corrected Markdown as the canonical correction baseline for the whole part before the remaining scene/dialogue derivatives are propagated.

The merge also removes one obvious extraction-script artifact from the Markdown (`అది`) in favour of the Tamil source form `அது`. Earlier scan-adjudicated corrections already established source-visible `குரல் : பக்தா!` at PDF 14 rather than the repository's former `குரு: பக்தா!`.

The scene/dialogue layers are currently synchronized only through **PDF 18 / scene 10**. Therefore the archive must still be treated as **reconciliation-in-progress** until scenes beginning on PDF 19 onward, character-label inventories, translations and publication derivatives are updated from the corrected canonical text.

## Execution order from here

- Reconcile scene-text derivatives from PDF 19 onward against the corrected canonical Part 02.
- Reconcile immutable dialogue text / exact source labels only where the corrected source requires it; preserve stable record IDs where the source utterance itself remains the same record.
- Recheck character mappings when an exact source label changes.
- Continue the same corrected-Markdown-first pass into Parts 03–05.
- Reconcile English / reader / EPUB derivatives for semantic source changes instead of leaving them silently stale.
- Restore final archive status only after all affected layers agree.

The previous full-volume `104 verified / 0 review` claim is **superseded for textual correctness by this reconciliation pass until the pass closes**.
