# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover date: 2026-08-13  
Previous review-gate checkpoint: `250f4ae975722c5d1a6dedb9a5dc81a783c3fedd`  
Scenes 11–15 review/status-sync checkpoint before this handover update: `f2764fa1cb10fac57cc5385eeeced8b382794e1c`

This document is the continuation entry point for a **new chat**. Read it before doing any translation work.

## 1. Current stage

The Tamil/source archive and all non-English structured derivatives are complete. The active work is the **English translation layer**.

Current English state:

- scenes started: **1–15**
- scenes verified: **1–15**
- scenes in review: **none**
- translation units: **224**
- verified units: **224**
- review units: **0**
- unit kinds: **176 dialogue / 42 stage-direction / 6 song / 0 quoted-verse**
- current translation status: **`in-progress-verified`**

The exact next activity is to create the source-linked English translation batch for canonical **scenes 16–20** at `review` status. Do not mark that future batch verified until it has received its own deliberate second-pass review.

## 2. Review gates completed

### Scenes 6–10

The first review gate was completed before scenes 11–15 were created.

At checkpoint `250f4ae975722c5d1a6dedb9a5dc81a783c3fedd`:

- scenes **1–10** were verified;
- all **136** units through scene 10 were verified;
- review units were **0**.

English-only corrections included removing unsupported additions in scenes 6–7, restoring source action `விழுந்து` in scene 8, changing scene 9 `காலையிலே` from `all morning` to `this morning`, and tightening scene 10 without altering Tamil.

### Scenes 11–15

The second review gate is now complete.

All **88 units** in scenes 11–15 were reviewed against:

- `scenes/scene-11.md` through `scene-15.md`;
- immutable `dialogues/records/scene-11.json` through `scene-15.json`;
- PDF/printed-page provenance;
- `songs/tracks/09-poomalai.md`;
- `songs/tracks/01-desam-gnanam-kalvi.md`;
- the verified song occurrence inventory.

The batch now stands at **88/88 verified**.

English-only refinements made during the pass:

- **scene 13:** `திண்ணை` is rendered consistently as `raised veranda`; `மாடு செய்த புண்ணியம்` is expressed as the cow's `good fortune` rather than the awkward literal `merit`, while the metaphor remains intact;
- **scene 14:** an added English endearment was removed from `அதெல்லாம் முடியாதம்மா`; `நாணயம்` is rendered through trustworthiness/creditworthiness rather than `coin`;
- **scene 15:** `மண்ணைப் போச்சே` is rendered idiomatically as `gone to waste`; standalone stage directions avoid the misleading modern English age-sense of `minors` for `மைனர்கள்`, while exact Tamil source labels remain unchanged.

No canonical Tamil, scene derivative, dialogue record, character mapping, song inventory or Tamil song derivative was modified.

## 3. Source pressure points deliberately retained

The second-pass review did **not** smooth away the following verified-source difficulties:

### Scene 11

- `வில்லுக்கொத்து போல` remains the unusual source simile, conservatively translated as `together like a bundle of bows`.
- Kalyani's cash/jewellery line is translated so English does not literally suggest selling cash, but the source event order remains intact.

### Scene 12

`பூமாலை` remains one semantic-poetic translation unit linked to `parasakthi-song-004`.

Retained review notes include:

- `வந்தேன் தவழ்ந்தாய்?` — first-/second-person instability remains visible;
- `பாரான எந்தன் வயிற்றில்` — contextual `burdened womb` remains documented as interpretive;
- `தாலி அறுத்தவர்கள்` — period tali image retained;
- `தாசில் உத்தியோகம்` — culturally specific `Tahsildar's post` comparison retained rather than generalized.

### Scene 13

- Marwari-shop dialect/code-switching remains source-linked without a caricatured English accent.
- `நீப்பன்—` remains unresolved/nonstandard rather than normalized into a guessed word or place.
- `தம்பி முறையில்லா கொண்டாட` remains kinship-claim wordplay.
- `parasakthi-s013-d023` remains one PDF **16→17** translation unit with explicit notes on first-/third-person rhetorical instability.
- d024 remains fragmentary; no missing transformation verb is supplied.

### Scene 14

- `மாப்கரோஜ் மகராஜ்` remains transliterated as `Maaf karo ji, Maharaj` so Venu's sound-play survives.
- `ரோஜ்` remains part of the sound-play rather than being over-explained.

### Scene 15

- unexplained canonical token `பாரா-2` remains exposed as `[para-2]`;
- the Mariamman earth-flinging ritual/cursing image remains source-specific;
- Gunasekaran's `பைத்தியக்கார உலகம்` rhetoric remains blunt and sequential;
- `parasakthi-song-005` (`குதம்பாய்`, PDF 19→20) and `parasakthi-song-006` (`தாண்டவக்கோனே`, PDF 20) remain two translation units because the verified Tamil derivative identifies two distinct source occurrences, even though both belong to soundtrack track 1;
- `ஆரியக் கூத்து` remains literally `Aryan dance` inside the lyric without added ideological exposition.

## 4. Canonical/source state — immutable

Source PDF:

- file: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- total PDF pages: **58**
- canonical dialogue/song pages: PDF **4–57** / printed pp. **3–56**
- PDF 58: rear advertisement/back matter

Tamil source state:

- canonical Tamil: **54 verified / 0 review / 0 unresolved markers**
- observed canonical scenes: **46**
- scene headings **23 and 34 are absent** and must never be invented
- PDF 49 source heading `48` is canonical scene **43**
- PDF 57 source heading `43` is canonical final scene **48**
- dialogue index: **642 complete-verified records**
- song authorship: **14/14 verified**
- Tamil soundtrack derivatives: **11/11 complete-verified**, plus one separate Bharathidasan quoted-verse derivative

Critical rule: **English translation must never be used to repair, normalize, or overwrite Tamil.** Do not use film audio, subtitles, web copies, later editions, memory, or familiar quotations to change canonical Tamil.

## 5. Translation architecture and rules

Translation files live under `works/parasakthi/translations/`.

Current records exist for canonical scenes **1–15**.

Every unit must preserve:

- canonical scene number;
- exact Tamil `speaker_label` as immutable metadata;
- source dialogue record ID or song occurrence ID where available;
- PDF/printed-page provenance;
- source scene path;
- cross-page unity/segmentation when the source record spans pages.

Rules that must continue:

1. Tamil remains authoritative.
2. Translate stage directions without inventing action.
3. Preserve rhetorical force, repetition, questions, exclamations, metaphors, code-switching and social/political vocabulary where meaningful.
4. Never normalize source `speaker_label` values.
5. Songs are **semantic-poetic translations**, not singable rewrites.
6. Do not introduce rhyme, metre, imagery or completed refrain lines absent from the source.
7. Keep canonical song occurrences exactly as the song inventory defines them.
8. Cross-page source records remain one translation unit.
9. Record interpretive choices in `translation.notes`.
10. English fluency is never evidence that Tamil should be corrected.

## 6. Exact next activity — scenes 16–20

Before creating anything, fetch the current `main` versions of:

1. this handover;
2. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md`;
3. `docs/ARCHIVAL_WORKFLOW.md`;
4. `works/parasakthi/translations/README.md`;
5. `works/parasakthi/translations/schema.json`;
6. `works/parasakthi/translations/index.json`;
7. `works/parasakthi/scenes/scene-16.md` through `scene-20.md`;
8. `works/parasakthi/dialogues/records/scene-16.json` through `scene-20.json`;
9. the song inventory and any verified Tamil song derivative whose occurrence lies in scenes 16–20.

Then:

1. create source-linked translation records for canonical scenes **16–20**;
2. preserve source ordering, exact labels and page provenance;
3. keep any cross-page dialogue as one translation unit;
4. translate stage directions without invented action;
5. keep song/verse occurrence boundaries exactly as verified;
6. record interpretive pressure points explicitly in notes;
7. set the new batch to **`review`**, not `verified`;
8. synchronize translation/status manifests after creation;
9. perform a separate second-pass review before any verification of scenes 16–20.

## 7. Expected next-batch state

Before scenes 16–20 are created:

- scenes verified: **1–15**
- verified units: **224**
- review units: **0**

After the new batch is created, totals will depend on the source-linked unit count in scenes 16–20. Do not estimate or invent that count before deriving it from the verified source files.

## 8. Repository update discipline

- Fetch the current blob SHA before replacing any existing file.
- Never edit canonical Tamil files as part of translation work.
- Never edit `dialogues/records/` to make English easier.
- Never normalize `speaker_label` values inside translation source metadata.
- Keep review/verification state synchronized in:
  - `works/parasakthi/translations/index.json`
  - `works/parasakthi/translations/README.md`
  - `works/parasakthi/metadata.yaml`
  - `data/works.json`
  - `works/parasakthi/README.md`
  - root `README.md`
  - the controlling handover document(s)
- After each durable checkpoint, compare against the previous checkpoint and confirm that source/Tamil derivative files were not modified.

## 9. One-line continuation prompt for a new chat

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Create the English review batch for scenes 16–20; do not mark it verified until its own second-pass review is complete.
