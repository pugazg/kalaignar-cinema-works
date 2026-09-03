# Next Chat Prompt — Raja Rani final manual fidelity corrections + reconciliation

Continue directly in:

`pugazg/kalaignar-cinema-works`

Branch: `main`

Active work: `works/raja-rani/` — **ராஜா ராணி**

Controlling full source: `TVA_BOK_0017188_ராஜா_ராணி.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve any newer durable state. Do not reset, repeat or overwrite later work because this prompt contains an older checkpoint.

The source identity recorded in the repository is:

- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- screenplay/dialogue: PDF **10–79**, printed pp. **9–78**
- PDF 80: unnumbered back cover

## Mandatory startup

Before any write, read completely:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. `docs/HANDOVER_RAJA_RANI.md`
7. this `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/notes/post-fidelity-corrections.md`

Then fetch the current live page files for the range being changed.

## Latest correction checkpoint

The manually reviewed correction campaign has already updated pages **56–75**. The later page-72 clarification has also been applied:

`சாக்ரடீசன்` → **`சாக்ரடீசின்`**

Do not revert it.

Pages **51–55** have user manual scan verdicts from the preceding chat, but they must still be explicitly checked during the final reconciliation rather than assumed synchronized.

## EXACT NEXT ACTIVITY

The user will supply or continue the **final 075–080 comparison/manual correction batch**.

Process that batch first.

Rules:

- the user's manual scan verdict is authoritative for each disputed word;
- `r*.md`, Repository text, OCR and PDF parsed text are candidate readings only;
- old Tamil glyphs must be read from the rendered scan at high enlargement;
- never choose a modern/familiar spelling merely because it seems more plausible;
- preserve occurrence-specific spelling variants;
- page 75 is intentionally overlapping with the prior batch, so re-check it if the new comparison contains it;
- change only the approved words/forms;
- do not import unrelated missing text, punctuation, formatting or OCR reconstruction;
- preserve existing bounded review spans and the PDF-74 overprint limitation.

Commit the final 075–080 corrections before starting anything else.

## THEN — MANDATORY RECONCILIATION

After the final batch is updated, reconcile the correction campaign end to end before resuming translation.

At minimum:

1. audit canonical pages against all user-approved comparison/manual verdicts, with special attention to **51–55** and the overlapping final page 75;
2. determine every canonical span changed after downstream derivatives were generated;
3. reconcile affected scene-text derivatives;
4. reconcile affected immutable dialogue records without changing IDs unnecessarily; exact corrected speaker labels/text must propagate;
5. update character exact-label/entity metadata only where affected;
6. recheck any affected song/performance links without changing unrelated authorship decisions;
7. verify any translation records that touch corrected source spans; do not expand translation until this gate closes;
8. update/revalidate indexes, counts and QA reports;
9. synchronize the work README, relevant audit/README/index files, `data/works.json`, and root README where needed;
10. write a durable reconciliation note and mark affected downstream layers synchronized only after checks pass.

The old next action — translating `raja-rani-s002`–`s005` — is **paused** until this reconciliation is complete.

## Old-glyph lesson that must survive the fresh chat

The earlier assistant scan review produced many errors because OCR/parsed text and modern-spelling expectations biased interpretation of the old Tamil typeface. Do not repeat that method.

When a token is disputed, zoom the scan and compare the actual glyphs. If still uncertain, mark uncertainty. Do not guess. Where the user has already manually reviewed a token and supplied its source form, preserve that explicit verdict exactly.
