# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-14

This document is the continuation entry point. Read it before doing translation work.

## Current English state

- scenes started/reviewed: **1–22, 24–30**
- scenes verified: **1–22, 24–25**
- scenes in review: **26–30**
- canonical scene **23 is absent**
- translation units: **500**
- verified units: **407**
- review units: **93**
- kinds: **410 dialogue / 80 stage-direction / 9 song / 1 quoted-verse**
- status: **`in-progress-review`**

The exact next activity is a deliberate second-pass review of all **93 units** in scenes **26–30**. Do not begin scenes 31–35 until this review is complete.

## Completed review gates

- scenes 6–10: **66/66** verified;
- scenes 11–15: **88/88** verified;
- scenes 16–20: **87/87** verified;
- observed scenes 21, 22, 24 and 25: **96/96** verified.

No completed English review has modified canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory or Tamil song derivatives.

## Scenes 26–30 review batch

The new source-linked batch is at `review` status:

- scene 26 — **4** units: 3 stage directions + 1 song;
- scene 27 — **4** units: 3 dialogue + 1 stage direction;
- scene 28 — **55** units: 48 dialogue + 6 stage directions + 1 quoted verse;
- scene 29 — **2** units: 1 stage direction + 1 song;
- scene 30 — **28** units: 26 dialogue + 2 stage directions.

Batch total: **93 units** — **77 dialogue + 13 stage directions + 2 songs + 1 quoted verse**.

Verified occurrence boundaries must remain unchanged:

- scene 26: `parasakthi-song-008`, PDF **31→32**;
- scene 28: quoted verse `parasakthi-song-009`, PDF **33**;
- scene 29: `parasakthi-song-010`, PDF **35**.

Scene 28 dialogue `parasakthi-s028-d023` remains one cross-page English unit across PDF **33→34**.

### Review pressure points

- **scene 26:** preserve the nested source parenthetical and review the pressure-sensitive verified forms `பட்டி சாதி` and `பட்சமாயிருங்க` without repairing Tamil.
- **scene 27:** preserve the family statements and photograph references without adding chronology.
- **scene 28:** review `குழுச்சியான`, `நானக்குப் போறேன்`, `தண்ணுடையைக்`, `மண்ணுங்கட்டி`, `உடம்பைப் பற்றித்தான்`, `பொம்மைகள்`, and `முண்டி`; preserve standalone `பாரா-3.` without inventing a function; keep the quoted verse distinct from soundtrack material.
- **scene 29:** review contextual `பொருள்` while retaining repeated questions, poverty imagery and refrain structure.
- **scene 30:** review `தேங்காய் முடி`, `ஏழை...ஏழவு`, the fragmentary chairman exchange, `ஒட்டப்பசங்க`, and the sound-chain `ஓடப்பர் / உதையப்பர் / உயரப்பர் / ஒப்பப்பர்`.

## Canonical/source state — immutable

- source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- canonical Tamil: **54 verified / 0 review / 0 unresolved markers**
- observed scene headings: **46**; headings **23 and 34 are absent**
- dialogue index: **642 complete-verified records**
- song authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate quoted-verse derivative

English translation must never repair, normalize or overwrite the Tamil source. Do not use film audio, subtitles, web copies, later editions or memory to change canonical Tamil.

## Translation rules

Tamil remains authoritative. Keep every English unit source-linked, preserve exact Tamil speaker labels and page provenance, add no action to stage directions, preserve rhetoric and source uncertainty, keep songs semantic-poetic rather than singable, keep quoted verse distinct, and keep cross-page source units whole. Put interpretive uncertainty in `translation.notes`.

## Exact next activity

Second-pass all **93 review units** in `records/scene-26.json` through `scene-30.json` against verified scene files, immutable dialogue records and the verified song/quoted-verse derivatives. Change **English only** where a genuine translation problem is found.

If the pass succeeds, mark all 93 units and scenes 26–30 `verified`, synchronize status surfaces and compare against the pre-batch checkpoint. **Only then begin scenes 31–35.**
