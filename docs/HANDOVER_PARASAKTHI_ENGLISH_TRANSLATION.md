# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

This document is the continuation entry point for a new chat. Read it before doing any translation work.

## 1. Current English state

The Tamil/source archive and non-English structured derivatives remain complete and immutable. The active derivative is English translation.

- scenes started: **1–20**
- scenes reviewed: **1–20**
- scenes verified: **1–20**
- scenes in review: **none**
- translation units: **311**
- verified units: **311**
- review units: **0**
- kinds: **250 dialogue / 54 stage-direction / 7 song / 0 quoted-verse**
- status: **`in-progress-verified`**

The next source-linked batch is canonical **21–25**, but only observed scenes **21, 22, 24 and 25** exist. Canonical **scene 23 is absent and must never be invented**.

## 2. Completed review gates

- scenes 6–10: **66/66** second-pass verified;
- scenes 11–15: **88/88** second-pass verified;
- scenes 16–20: **87/87** second-pass verified.

### Scenes 16–20 review refinements

The latest review changed English only:

- **scene 16:** tightened `மறுவருஷம்` to `the following year` while retaining the carved-statue, `பாழும் தெய்வம்`, and infant-in-arms imagery;
- **scene 17:** refined the cross-page lullaby while preserving `மாமன்மார் மூவர் தம்பி`, `பாலாடை`, `சீதனம்`, the unlabelled conscience passage, and `சுமைதாங்கி / சோகம் தாங்கி` wordplay;
- **scene 18:** changed the over-specific `epileptic fits` to generic `fits` for period `காக்கா வலிப்பு`; unresolved `டேபின்`, `லாண்டறி`, and Hindi code-switching remain exposed in notes;
- **scene 19:** corrected the split-name handling of `நந்த / கோபாலன்` and `வேணு / கோபாலன்` so it does not imply the character Venu; four unlabelled performed blocks remain scene-located without invented dialogue IDs, soundtrack occurrence IDs or authorship;
- **scene 20:** corrected `பொறுக்கவா?` from the mistaken `pick what up?` reading to `Why—to scavenge?`; source-specific `போணி`, `எய்ட் நாட்திரீ`, `கொட்டாபுளி`, wordplay and the final arrest ambiguity remain documented.

No canonical Tamil, scene derivative, dialogue record, character mapping, song inventory or Tamil song derivative was modified.

## 3. Important representation decisions through scene 20

- Scene 17 `parasakthi-song-007` remains one semantic-poetic translation unit across PDF **21→22**.
- Scene 17's conscience paragraph is unlabelled in the canonical scene, so it is source-located directly rather than assigned an invented dialogue record ID.
- Scene 19 contains four unlabelled performed speech/verse blocks. The verified song inventory does not identify them as soundtrack occurrences, so they remain scene-located translation units without invented occurrence IDs or authorship.
- Exact Tamil `speaker_label` values are immutable metadata even where English stage directions avoid misleading modern meanings.
- Opaque verified-source forms stay visible in translation notes rather than being silently repaired.

## 4. Canonical/source state — immutable

- source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; canonical dialogue/song range PDF **4–57** / printed pp. **3–56**
- canonical Tamil: **54 verified / 0 review / 0 unresolved markers**
- observed scene headings: **46**
- headings **23 and 34 are absent**
- PDF 49 printed source heading `48` is canonical scene **43**
- PDF 57 printed source heading `43` is canonical final scene **48**
- dialogue index: **642 complete-verified records**
- song authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate quoted-verse derivative

Critical rule: English translation must never repair, normalize or overwrite the Tamil source. Do not use film audio, subtitles, web copies, later editions or memory to change canonical Tamil.

## 5. Translation rules

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

## 6. Exact next activity

Before creating the next batch, fetch current `main` versions of:

- this handover and `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`;
- `docs/ARCHIVAL_WORKFLOW.md`;
- `works/parasakthi/translations/README.md`, `schema.json`, and `index.json`;
- canonical scene files **21, 22, 24, 25**;
- immutable dialogue-record files for **21, 22, 24, 25**;
- the verified song inventory and any song/quoted-verse derivatives whose occurrences lie in those scenes.

Then create source-linked English records for observed scenes **21, 22, 24 and 25** at **`review`** status. Do not create scene 23. Derive the new unit count from the verified source; do not estimate it in advance. After batch creation, synchronize status surfaces and perform a separate second-pass review before verification.

## 7. Repository update discipline

Keep state synchronized in:

- `works/parasakthi/translations/index.json`
- `works/parasakthi/translations/README.md`
- `works/parasakthi/metadata.yaml`
- `data/works.json`
- `works/parasakthi/README.md`
- root `README.md`
- both Parasakthi handover documents

After each durable checkpoint, compare against the prior checkpoint and confirm that canonical/source derivatives were not modified.

## 8. Continuation prompt

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Create the next English review batch for observed scenes 21, 22, 24 and 25; scene 23 is absent and must not be invented.
