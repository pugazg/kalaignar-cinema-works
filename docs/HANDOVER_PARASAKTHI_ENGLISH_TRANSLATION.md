# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover date: 2026-08-13  
Previous review-gate checkpoint: `250f4ae975722c5d1a6dedb9a5dc81a783c3fedd`

This document is the continuation entry point for a **new chat**. Read it before doing any translation work.

## 1. Current stage

The Tamil/source archive and all non-English structured derivatives are complete. The active work is the **English translation layer**.

Current English state:

- scenes started: **1–15**
- scenes verified: **1–10**
- scenes in review: **11–15**
- translation units: **224**
- verified units: **136**
- review units: **88**
- unit kinds: **176 dialogue / 42 stage-direction / 6 song / 0 quoted-verse**
- current translation status: **`in-progress-review`**

The exact next activity is **second-pass fidelity/editorial review of all 88 units in scenes 11–15**. Do **not** begin scenes 16–20 until that review is complete.

## 2. Review gate already completed — scenes 6–10

The prior handover required scenes 6–10 to be reviewed before scenes 11–15 could begin. That gate was completed first.

At review-gate checkpoint `250f4ae975722c5d1a6dedb9a5dc81a783c3fedd`:

- scenes **1–10** were verified;
- all **136** units through scene 10 were verified;
- review units were **0**;
- a compare against the pre-review handover HEAD showed changes only inside `works/parasakthi/translations/`.

English-only corrections made during the 66-unit scenes 6–10 review:

- **scene 6:** removed an added first-person plural from `புறப்படு சீக்கிரம்`; removed the unstated object `she` from the elliptical `நீ சொன்ன படியெல்லாம் கேட்டிரு` translation;
- **scene 7:** removed an unstated kinship address from `சரிதாம்போ`; removed added `to feed` from `பிள்ளைக் குட்டிக்காரன்`;
- **scene 8:** restored source action `விழுந்து` (`falls`) in the closing stage direction; retained the compressed `ஓ ரசிக்கும் சீமானே` stanza without invented syntax;
- **scene 9:** changed `all morning` to `this morning` for `காலையிலே`; retained documented uncertainty around `வங்கத்திலே` and `தகுதி? போக்கியதை?`;
- **scene 10:** tightened the bombing/hospital English while retaining `பெட்டிலே` contextually as hospital `bed` in English only.

No Tamil scene, dialogue, character or song derivative was changed.

## 3. Files to read first in the next chat

Fetch the current `main` versions of these files before making changes:

1. `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` — this document.
2. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md` — broader project state and historical constraints.
3. `docs/ARCHIVAL_WORKFLOW.md` — repository workflow rules.
4. `works/parasakthi/translations/README.md` — translation principles and current pressure points.
5. `works/parasakthi/translations/schema.json` — translation-unit schema.
6. `works/parasakthi/translations/index.json` — current translation checkpoint.
7. `works/parasakthi/translations/records/scene-11.json` through `scene-15.json` — current review batch.
8. `works/parasakthi/scenes/scene-11.md` through `scene-15.md` — verified canonical scene derivatives.
9. `works/parasakthi/dialogues/records/scene-11.json` through `scene-15.json` — immutable exact dialogue records.
10. `works/parasakthi/songs/tracks/09-poomalai.md` — scene-12 song authority.
11. `works/parasakthi/songs/tracks/01-desam-gnanam-kalvi.md` — scene-15 song authority.
12. `works/parasakthi/songs/inventory.json` — occurrence boundaries for scenes 12 and 15.
13. `works/parasakthi/metadata.yaml`
14. `data/works.json`

Do not begin by re-transcribing the PDF or reconstructing prior work from chat memory. Repository canonical derivatives control the translation layer.

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
- character index: **69/69 labels explicitly disposed across 48 entities**
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
7. Keep canonical song occurrences as the song inventory defines them.
8. Cross-page source records remain one translation unit.
9. Record interpretive choices in `translation.notes`.
10. English fluency is never evidence that Tamil should be corrected.

## 6. Current review batch — scenes 11–15

Exactly **88 review units** exist:

- scene 11 — **3**: 2 dialogue + 1 stage direction
- scene 12 — **10**: 7 dialogue + 2 stage directions + 1 song
- scene 13 — **32**: 26 dialogue + 6 stage directions
- scene 14 — **19**: 16 dialogue + 3 stage directions
- scene 15 — **24**: 16 dialogue + 6 stage directions + 2 songs

New cross-page English units in this batch:

- `parasakthi-en-s013-u028` — scene-13 dialogue `parasakthi-s013-d023`, PDF **16→17**
- `parasakthi-en-s015-u023` — scene-15 song occurrence `parasakthi-song-005`, PDF **19→20**

### Scene 11

Review carefully:

- `வில்லுக்கொத்து போல` is currently `together like a bundle of bows`; the source simile is unusual and must not be replaced casually.
- The line about Kalyani's money/jewellery is rendered so English does not imply literally selling cash; verify that no source event was lost.

### Scene 12

`பூமாலை` is `parasakthi-song-004`, one semantic-poetic unit on PDF 14.

Review-sensitive forms:

- `வந்தேன் தவழ்ந்தாய்?` — verified source has a first-/second-person shift; current English preserves it rather than correcting it.
- `பாரான எந்தன் வயிற்றில்` — semantically difficult; current `burdened womb` reading is explicitly provisional/review-sensitive.
- `தாலி அறுத்தவர்கள்` — current English preserves the period tali image.
- `தாசில் உத்தியோகம்` — current English preserves the culturally specific `Tahsildar's post` comparison rather than substituting a generic `usual job`.

### Scene 13

Review-sensitive forms:

- Marwari-shop dialect/code-switching is translated for meaning without an invented caricatured accent.
- `நீப்பன்—` in d005 is compressed/nonstandard; current English deliberately does not turn it into an unsupported place name.
- `தம்பி முறையில்லா கொண்டாட` is treated as kinship-claim wordplay.
- `parasakthi-s013-d023` remains one cross-page unit. The Tamil repeatedly uses first-person verb forms and then shifts toward third-person reference; current English preserves that instability and documents it.
- the source page break occurs inside `போயிருக்கிறேனே`; English page segments align at a nearby clause boundary without splitting an English word.
- d024, `நீ மெட்ராசுக்கு மேயராக வர்ற காலத்திலே மிருகத்தையெல்லாம் மனுஷனுக்கு.`, is fragmentary in the verified source. Current English remains fragmentary and does not supply a missing verb.

### Scene 14

Review-sensitive forms:

- `மாப்கரோஜ் மகராஜ்` is transliterated as `Maaf karo ji, Maharaj` because Venu's reply depends on the sound.
- Venu's `மாப்கரோஜ்—மண்ணாங்கட்டி. ரோஜ்—...` is rendered as sound-play; verify without over-explaining it.
- `நாணயம்` in the credit offer is currently `reliability`/creditworthiness, not `coin`.

### Scene 15

Review-sensitive forms:

- d007 contains unexplained canonical token `பாரா-2`; current English exposes it as `[para-2]` rather than guessing.
- the Mariamman-temple `மண்ணுவாரி இறைப்பேன்` image remains explicit.
- Gunasekaran's `பைத்தியக்கார உலகம்` monologue retains the source sequence of hunger, theft, punishment, fear and deception.
- soundtrack track 1 has **two verified source occurrences** in scene 15:
  - `parasakthi-song-005` — `குதம்பாய்` section, PDF **19→20**
  - `parasakthi-song-006` — `தாண்டவக்கோனே` section, PDF **20**
- Keep them as two translation units even though they belong to the same soundtrack composition.
- `ஆரியக் கூத்து` is currently translated literally as `Aryan dance`; do not insert explanatory ideology into the lyric itself.

## 7. Exact next activity

First perform a deliberate second-pass review of **all 88 units in scenes 11–15**:

1. verify unit ordering against `scenes/scene-11.md` through `scene-15.md`;
2. verify every dialogue `source_record_id`, exact label and page provenance against `dialogues/records/scene-11.json` through `scene-15.json`;
3. verify all stage-direction locators and ensure no action was invented;
4. verify `parasakthi-song-004`, `parasakthi-song-005` and `parasakthi-song-006` against their verified Tamil track derivatives and `songs/inventory.json`;
5. review the pressure points above one by one;
6. change **English only** where a genuine problem is found;
7. if the review passes, set all 88 units/scenes 11–15 to `verified`;
8. synchronize `translations/index.json`, `translations/README.md`, `metadata.yaml`, `data/works.json`, work/root READMEs and the handover;
9. verify current `main` HEAD and compare against the checkpoint to confirm source/Tamil derivative immutability;
10. only then begin canonical **scenes 16–20**.

## 8. Expected post-review state

If scenes 11–15 pass unchanged or after English-only corrections:

- scenes verified: **1–15**
- verified units: **224**
- review units: **0** before creating scenes 16–20

## 9. Repository update discipline

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

## 10. One-line continuation prompt for a new chat

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Review scenes 11–15 first; do not begin scenes 16–20 until that review is complete.
