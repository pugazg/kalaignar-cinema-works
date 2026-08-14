# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-14

This document is the continuation entry point. Read it before doing translation work.

## Current English state

- scenes started/reviewed/verified: **1–22, 24–30**
- scenes in review: **none**
- canonical scene **23 is absent**
- translation units: **500**
- verified units: **500**
- review units: **0**
- kinds: **410 dialogue / 80 stage-direction / 9 song / 1 quoted-verse**
- status: **`in-progress-verified`**

The exact next activity is to create the source-linked English **review** batch for observed canonical scenes **31, 32, 33 and 35**. Canonical **scene 34 is absent and must not be invented**. Inspect the verified song/quoted-verse inventory before deriving units, then second-pass the batch before verification.

## Completed review gates

- scenes 6–10: **66/66** verified;
- scenes 11–15: **88/88** verified;
- scenes 16–20: **87/87** verified;
- observed scenes 21, 22, 24 and 25: **96/96** verified;
- scenes 26–30: **93/93** verified.

No completed English review has modified canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory or Tamil song derivatives.

## Scenes 26–30 second-pass checkpoint

The batch comprised:

- scene 26 — **4** units: 3 stage directions + 1 song;
- scene 27 — **4** units: 3 dialogue + 1 stage direction;
- scene 28 — **55** units: 48 dialogue + 6 stage directions + 1 quoted verse;
- scene 29 — **2** units: 1 stage direction + 1 song;
- scene 30 — **28** units: 26 dialogue + 2 stage directions.

Batch total: **93 units** — **77 dialogue + 13 stage directions + 2 songs + 1 quoted verse**.

Verified occurrence boundaries remain unchanged:

- scene 26: `parasakthi-song-008`, PDF **31→32**;
- scene 28: quoted verse `parasakthi-song-009`, PDF **33**;
- scene 29: `parasakthi-song-010`, PDF **35**.

Scene 28 dialogue `parasakthi-s028-d023` remains one cross-page English unit across PDF **33→34**.

### English-only refinements made in the second pass

- **scene 26:** pressure-sensitive `பட்டி சாதி` and `பட்சமாயிருங்க` remain exposed through transliteration rather than source repair;
- **scene 27:** the Gnana Sekaran line now directly reflects `இறந்ததை நினைக்கும்போது` without added chronology;
- **scene 28:** `குழுச்சியான` is no longer assigned the guessed meaning “scheming”; `ஆபத்பாந்தவா` is tightened to “helper in distress”; `பலே, பலே` is rendered functionally as “Bravo, bravo!”; `உடம்பைப் பற்றித்தான்` is kept close to its bodily wording; `முண்டி` remains transliterated; standalone `பாரா-3.` remains uninterpreted;
- **scene 29:** contextual `பொருள்` remains “means” and the repeated poverty/darkness questions are preserved;
- **scene 30:** `தேங்காய் முடி` is rendered less specifically as a piece of coconut; pressure-sensitive `ஏழவு`, `சேர்மையா`, and `ஒட்டப்பசங்க` elements are transliterated rather than guessed; the fragmentary chairman exchange stays fragmentary; the `ஓடப்பர் / உதையப்பர் / உயரப்பர் / ஒப்பப்பர்` semantic chain is retained while documenting the sound loss.

## Canonical/source state — immutable

- source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; canonical dialogue/song range PDF **4–57** / printed pp. **3–56**
- canonical Tamil: **54 verified / 0 review / 0 unresolved markers**
- observed scene headings: **46**
- headings **23 and 34 are absent**
- PDF 49 source heading `48` is canonical scene **43**
- PDF 57 source heading `43` is canonical final scene **48**
- dialogue index: **642 complete-verified records**
- song authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate quoted-verse derivative

Critical rule: English translation must never repair, normalize or overwrite the Tamil source. Do not use film audio, subtitles, web copies, later editions or memory to change canonical Tamil.

## Translation rules

1. Tamil remains authoritative.
2. Every English unit remains source-linked with scene, record/occurrence where available, and PDF/printed-page provenance.
3. Exact Tamil speaker labels remain immutable metadata.
4. Stage directions gain no invented action.
5. Preserve repetition, questions, metaphors, code-switching, social vocabulary and rhetorical force where meaningful.
6. Songs are semantic-poetic translations, not singable rewrites.
7. Never invent song occurrence boundaries or authorship.
8. Cross-page source units remain one translation unit.
9. Unlabelled canonical material may be source-located directly; do not manufacture dialogue IDs merely to fit the index.
10. Interpretive choices and unresolved source forms belong in `translation.notes`.

## Exact next activity — observed scenes 31–35

Before creating the next batch, fetch current `main` versions of:

- this handover and `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`;
- `docs/ARCHIVAL_WORKFLOW.md`;
- `works/parasakthi/translations/README.md`, `schema.json`, and `index.json`;
- canonical scene files **31, 32, 33 and 35**;
- immutable dialogue-record files for **31, 32, 33 and 35**;
- `songs/inventory.json` and any verified Tamil song/quoted-verse derivatives whose occurrences fall inside those scenes.

Canonical **scene 34 is absent**. Do not create `scene-34.json`, invent a heading, or shift material into it.

Known dialogue-record counts are **13 / 4 / 56 / 10** for scenes **31 / 32 / 33 / 35** respectively, but the English unit total must be derived from the complete verified source, including standalone stage directions and any verified song/verse occurrences. Create the batch at `review` status and stop at that gate before its separate second pass.

## Repository discipline

Keep state synchronized in the translation index/README, work/root READMEs, metadata, `data/works.json`, and both handovers. After each durable checkpoint, compare against the previous checkpoint and confirm that canonical/source derivatives were not modified.

## Continuation prompt

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Create the English review batch for observed scenes 31, 32, 33 and 35; scene 34 is absent and must not be invented. Inspect verified song/quoted-verse occurrences before deriving units, and do not mark the new batch verified until its own second-pass review is complete.
