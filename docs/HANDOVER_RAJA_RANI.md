# Raja Rani — Manual Tamil Fidelity Correction Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Active work: `works/raja-rani/` — **ராஜா ராணி**

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first in every fresh chat. Preserve any newer durable state. Do not reset, repeat or reopen later completed work merely because this handover records an older checkpoint.

The checkpoint at which this handover was created follows the direct correction of PDF page 72 from `சாக்ரடீசன்` to the user-verified source form **`சாக்ரடீசின்`**.

## Controlling source

Full source recorded by the repository:

- filename: `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- PDF pages: **80**
- SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`
- canonical screenplay/dialogue range: PDF **10–79**, printed pp. **9–78**
- PDF 80: unnumbered back cover

Comparison extracts such as `r1.md`, `r2.md`, `r3.md` and part PDFs are review aids. They are not independent canonical authorities. The rendered source scan controls.

## Mandatory startup in the next chat

Read completely before changing anything:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/ARCHIVAL_WORKFLOW.md`
3. `docs/SOURCE_POLICY.md`
4. `docs/TRANSCRIPTION_GUIDE.md`
5. `docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md`
6. this `docs/HANDOVER_RAJA_RANI.md`
7. `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
8. `works/raja-rani/README.md`
9. `works/raja-rani/notes/post-fidelity-corrections.md`

Then fetch the live target page files involved in the next correction batch before writing.

## Critical old-Tamil glyph lesson

The recent review exposed a systematic failure mode: OCR and modern-Tamil visual expectations can bias reading of older Tamil typeforms.

For this work:

- do **not** use OCR or parsed PDF text to decide disputed characters;
- do **not** prefer a familiar/modern spelling because it seems linguistically more natural;
- inspect the rendered scan at high enlargement and read the disputed token glyph by glyph;
- Repository text and `r*.md` text are only candidate readings;
- when the user has manually reviewed the scan and supplied the correct form, the user's explicit source verdict controls that reviewed occurrence;
- preserve different spellings when the source actually uses different forms in different occurrences;
- no global normalization;
- no silent reconstruction of obscured text.

Examples from the current correction campaign include occurrence-specific pairs such as `சேர்ந்தாப்பிலே` / `சேந்தாப்பிலே` and `ஒன்ஸ்மோர்` / `ஒன்சுமோர்`.

## Manual comparison/correction campaign

The user has been comparing repository text against extracted comparison files and then manually resolving old-glyph disputes from the scan.

Earlier comparison phases:

- pages 1–25: selective approved spelling replacements from `r1.md`;
- pages 26–50: selective approved spelling replacements from `r2.md`;
- pages 51 onward: `r3.md` comparison followed by direct user scan review because automated/assistant glyph reading proved unreliable.

### Pages 51–55

The user manually supplied authoritative scan verdicts for the disputed words in pages 51–55.

**Important:** do not assume those verdicts have all been reconciled against current live page files. They must be included in the final reconciliation after the final 075–080 batch.

### Pages 56–70

User-reviewed corrections were applied directly to `works/raja-rani/pages/056.md` through `070.md`.

The correction policy was:

- use the user's manually approved `r3.md` form where selected;
- retain the Repository form where selected;
- use the separately supplied source form for `Neither` cases;
- preserve occurrence-specific variants rather than globally replacing them.

Notable `Neither` corrections included:

- PDF 59: `நினைக்கிறேன்`;
- PDF 69: `வீசும்`.

### Pages 71–75

User-reviewed corrections were applied to `071.md` through `075.md`.

Notable points:

- PDF 71: `மாறினான்` was a `Neither` correction;
- PDF 72: the user subsequently clarified that the correct form is **`சாக்ரடீசின்`**. This supersedes the earlier `சாக்ரடீசன்` reading and has now been corrected in `pages/072.md`;
- other Repository-approved forms were retained exactly.

## Exact next activity

The user will continue the **final 075–080 correction batch in a fresh chat**.

1. Fetch live `main` first.
2. Read the mandatory startup documents above.
3. Use the user's next supplied 075–080 comparison/manual verdicts as the correction instructions.
4. Treat page 75 as an intentional overlap: it has already received one correction pass, but do not skip it if the new final batch supplies additional source-backed corrections.
5. Apply only approved source-word changes. Do not import unrelated missing words, punctuation, layout changes or OCR guesses.
6. Do not begin reconciliation until that final 075–080 update is complete.

## Mandatory reconciliation after 075–080 is updated

After the final correction batch is committed, perform a dedicated reconciliation **before resuming English translation or other downstream production**.

The reconciliation must:

1. compare the live canonical page files against all user-approved correction decisions from the comparison campaign, especially pages **51–55**, which must not be assumed complete merely because later ranges were committed;
2. verify the final overlapping 075 page state and the terminal 075–080 user batch;
3. identify every changed canonical source span since the previously generated derivatives;
4. reconcile affected `scenes/scene-*.md` files against corrected canonical pages;
5. reconcile affected immutable dialogue records while preserving IDs and source provenance; exact source `speaker_label` changes must propagate without normalization;
6. re-evaluate character exact-label inventory/entity mappings only where source speaker-label changes affect them;
7. recheck song/performance occurrence links only if an affected canonical span touches such a cue; do not alter unrelated song authorship;
8. verify whether any existing translation record touches a corrected span before leaving it verified; currently the English layer is only pilot-verified, but translation expansion is paused until reconciliation closes;
9. rerun/reperform relevant counts and consistency checks;
10. synchronize `works/raja-rani/README.md`, relevant layer READMEs/indexes/audit notes, `data/works.json`, and root `README.md` where the project checkpoint changes;
11. record the reconciliation in a durable note and only then declare downstream layers current again.

Do not regenerate or rewrite unaffected derivatives merely for style.

## Downstream status right now

The repository contains mature scene, dialogue, character, song and English-pilot derivatives created **before** this late manual spelling/glyph correction campaign.

Therefore their previous completion labels describe the pre-correction checkpoint. Until the post-075–080 reconciliation is completed, treat affected downstream layers as **reconciliation-pending**, not as automatically synchronized with the newly corrected canonical Tamil.

Do **not** continue the former next activity of translating `raja-rani-s002`–`s005` yet.

## Existing bounded source limitations remain

The late spelling/glyph correction campaign does not authorize reconstruction of the established review limitations:

- PDF 27 / printed p.26: faint/washed internal-monologue word;
- PDF 48 / printed p.47: two visually insecure short spans;
- PDF 57 / printed p.56: compact unresolved colloquial group after `என்னடா இது, முன்னுக்கு பின்...`;
- PDF 74 / printed p.73: `K. N. சங்கரன்` ownership/address overprint physically obscures original text.

Hidden or insecure wording stays unresolved unless the scan itself becomes readable enough to establish it.

## Current durable rule

**Canonical scan fidelity comes before derivative consistency.** If a later direct scan review corrects canonical Tamil, make the source correction first, then explicitly reconcile downstream derivatives. Never preserve an incorrect canonical word merely to avoid changing already-built derivatives.
