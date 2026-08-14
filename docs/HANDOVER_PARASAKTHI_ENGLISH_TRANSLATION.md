# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-14

This document is the continuation entry point for a new chat. Read it before doing any translation work.

## 1. Current English state

The Tamil/source archive and non-English structured derivatives remain complete and immutable. The active derivative is English translation.

- scenes started/reviewed/verified: **1–22, 24–25**
- scenes in review: **none**
- canonical scene **23 is absent and has no translation record**
- translation units: **407**
- verified units: **407**
- review units: **0**
- kinds: **333 dialogue / 67 stage-direction / 7 song / 0 quoted-verse**
- status: **`in-progress-verified`**

The exact next activity is to create the source-linked English review batch for canonical **scenes 26–30**, then perform a deliberate second-pass review before verification.

## 2. Completed review gates

- scenes 6–10: **66/66** second-pass verified;
- scenes 11–15: **88/88** second-pass verified;
- scenes 16–20: **87/87** second-pass verified;
- observed scenes 21, 22, 24 and 25: **96/96** second-pass verified.

### Scenes 21–25 review refinements

The latest pass changed English only:

- **scene 21:** clarified the `மூச்சிக்கு முப்பத்திரண்டு` repeated-address hyperbole; repeated `-ம்மா` is retained as `amma` rather than literal `mother`;
- **scene 22:** preserved `களங்கம்` as the source's stain/disgrace image and kept the force of `கள்ளப்புருஷன்` without normalizing the Tamil;
- **scene 24:** preserved the source's unresolved come/leave sequence rather than repairing the travel logic;
- **scene 25:** kept singular `அதை` singular in the sack joke, removed a misleading literal `mother` for feminine `ஏம்மா`, rendered departure-context `வணக்கம்` as `Goodbye`, and removed an added child reference from a stage-direction locator.

No canonical Tamil, scene derivative, dialogue record, character mapping, song inventory or Tamil song derivative was modified.

## 3. Canonical/source state — immutable

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

## 4. Translation rules

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

## 5. Exact next activity — scenes 26–30

Before creating the next batch, fetch current `main` versions of:

- this handover and `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`;
- `docs/ARCHIVAL_WORKFLOW.md`;
- `works/parasakthi/translations/README.md`, `schema.json`, and `index.json`;
- canonical scene files **26–30**;
- immutable dialogue-record files for **26–30**;
- the verified song inventory and the relevant Tamil derivatives.

The verified occurrence boundaries that must be preserved are:

- scene 26 — soundtrack occurrence `parasakthi-song-008`;
- scene 28 — quoted verse `parasakthi-song-009`;
- scene 29 — soundtrack occurrence `parasakthi-song-010`.

Create scenes 26–30 at **`review`** status, derive the unit count from the verified source, synchronize status surfaces, and only then perform a separate second-pass before verification.

## 6. Repository discipline

Keep state synchronized in the translation index/README, work/root READMEs, metadata, `data/works.json`, and both handovers. After each durable checkpoint, compare against the previous checkpoint and confirm that canonical/source derivatives were not modified.

## 7. Continuation prompt

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Create the English review batch for scenes 26–30, preserving verified song and quoted-verse occurrence boundaries; do not mark the batch verified until its own second-pass review is complete.
