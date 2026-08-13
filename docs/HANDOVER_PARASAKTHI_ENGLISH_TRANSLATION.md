# Parasakthi — English Translation Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover date: 2026-08-13  
State captured from pre-handover HEAD: `57c97ad5290347dfd64cd215aa765342dce59ac2`

This document is the continuation entry point for a **new chat**. Read it before doing any translation work.

## 1. Current stage

The Tamil/source archive and all non-English structured derivatives are complete. The active work is the **English translation layer**.

Current English state:

- scenes started: **1–10**
- scenes verified: **1–5**
- scenes in review: **6–10**
- translation units: **136**
- verified units: **70**
- review units: **66**
- unit kinds: **109 dialogue / 24 stage-direction / 3 song / 0 quoted-verse**
- current translation status: **`in-progress-review`**

The exact next activity is **second-pass fidelity/editorial review of all 66 units in scenes 6–10**. If they pass, mark scenes 6–10 verified and immediately begin the next translation batch with **scenes 11–15**.

## 2. Files to read first in the new chat

Fetch the current `main` versions of these files before making changes:

1. `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` — this document.
2. `docs/HANDOVER_PARASAKTHI_FIDELITY_AUDIT.md` — broader project state and historical constraints.
3. `docs/ARCHIVAL_WORKFLOW.md` — repository workflow rules.
4. `works/parasakthi/translations/README.md` — translation principles.
5. `works/parasakthi/translations/schema.json` — translation-unit schema.
6. `works/parasakthi/translations/index.json` — current translation checkpoint.
7. `works/parasakthi/translations/records/scene-06.json` through `scene-10.json` — current review batch.
8. `works/parasakthi/scenes/scene-06.md` through `scene-10.md` — verified canonical scene derivatives.
9. `works/parasakthi/dialogues/records/scene-06.json` through `scene-10.json` — immutable exact dialogue records.
10. `works/parasakthi/songs/tracks/06-o-rasikkum-seemane.md` — scene-8 song authority.
11. `works/parasakthi/metadata.yaml`
12. `data/works.json`

Do not begin by re-transcribing the PDF or reconstructing prior work from chat memory. The repository files above are the controlling project state.

## 3. Canonical/source state — immutable

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

## 4. Translation architecture

Translation files live under:

`works/parasakthi/translations/`

Current files:

- `README.md`
- `schema.json`
- `index.json`
- `records/scene-01.json` through `records/scene-10.json`

Every English translation unit is source-linked. Preserve:

- canonical scene number;
- exact Tamil `speaker_label` as immutable metadata;
- source dialogue record ID or song occurrence ID where available;
- PDF/printed-page provenance;
- source scene path;
- cross-page segmentation when a source record spans pages.

Unit kinds currently used:

- `dialogue`
- `stage-direction`
- `song`
- `quoted-verse`

Translation statuses are independent of Tamil verification:

- `draft`
- `review`
- `verified`

## 5. Translation rules that must continue

1. Tamil remains authoritative.
2. Translate stage directions without inventing action.
3. Preserve rhetorical force, repetition, questions, exclamations, metaphors, code-switching and social/political vocabulary where meaningful.
4. Do not normalize exact Tamil speaker labels in translation metadata.
5. Songs are **semantic-poetic translations**, not singable rewrites.
6. Do not introduce rhyme, meter, imagery or completed refrain lines absent from the source.
7. If a song is one canonical occurrence, keep it one translation unit rather than duplicating it into dialogue units simply because the source has speaker labels.
8. Cross-page source records remain one translation unit.
9. If English requires an interpretive choice, document it in `translation.notes` rather than hiding it.
10. English fluency is never evidence that the Tamil should be corrected.

## 6. Verified English coverage — scenes 1–5

Scenes **1–5 are verified**, totaling **70 verified units**.

Important reviewed decisions already settled:

### Scene 1

- `இரங்கூன்` → `Rangoon`
- `மலேயா` → `Malaya`
- `இலங்கை தீவு` → `the island of Ceylon` as a period-readable English rendering only
- `வாழ்க வாழ்கவே` is semantic-poetic, not singable
- source fragment `பண்ணிகர்` remains untouched in Tamil; English `melodious` is explicitly documented as contextual
- refrain fragments remain fragments
- Thangappan's dialogue remains one unit across PDF 4→5

### Scene 2

- `அண்ணியிடம் போதல்`: English was corrected so it does **not** add an unsupported possessive
- `தங்கையின் வாழ்விலே பொன் விழா?`: preserve its question-shaped form; do not turn it into a more specific ceremony label
- colloquial/code-switched Tamil is translated for meaning while exact source labels remain unchanged

### Scene 3

The source sentence:

`உலகில் ஒரு அண்ணன் இருந்து பெண்ணைப் பிறந்தால் பெரும் துயர் என்பார்கள்`

is semantically unusual. The verified English remains conservative and carries an explicit note. **Do not silently repair the Tamil or invent a more idiomatic source meaning.**

### Scene 4

- `மாங்குயில்` is rendered naturally as `cuckoo`; Tamil remains unchanged
- `இல் வாழ்வினிலே` is one song unit linked to `parasakthi-song-002`
- exact source labels `தங்`, `கல்`, `இரு` remain inline in the English song lines
- source refrain fragment `(இல்` remains incomplete in English rather than being reconstructed

### Scene 5

The wartime newspaper line around:

`இரங்கூன் கடலோரங்களில் எதிரிகள் கப்பல்கள் இந்தியா போய்ச் சேரவில்லை`

is compressed/awkward in the verified Tamil. English is intentionally conservative and does not invent a causal syntax not present in the source.

## 7. Scenes 6–10 — current review batch

Exactly **66 review units** exist across scenes 6–10.

Per-scene counts:

- scene 6 — **22**: 19 dialogue + 3 stage directions
- scene 7 — **24**: 22 dialogue + 2 stage directions
- scene 8 — **10**: 5 dialogue + 4 stage directions + 1 song
- scene 9 — **1**: one long cross-page dialogue
- scene 10 — **9**: 7 dialogue + 2 stage directions

Cross-page English units currently include:

- `parasakthi-en-s001-u004` — verified scene-1 dialogue
- `parasakthi-en-s008-u002` — scene-8 song across PDF 11→12
- `parasakthi-en-s009-u001` — scene-9 Gunasekaran monologue across PDF 12→13

### Review-sensitive decisions in scenes 6–10

#### Scene 6

`முழுகாதிருக்கிற பெண்ணு` is currently rendered as **`a woman in her condition`**, treating it as a contextual pregnancy euphemism. Review the tone carefully; do not modernize or repair the Tamil.

#### Scene 7

Preserve:

- explicit references to begging and prostitution;
- Gunasekaran's irony around Tamil Nadu's `first voice`;
- Jolly's social/moral vocabulary without rewriting it into a more modern moral framework;
- code-switched terms where their flavour matters.

#### Scene 8

`parasakthi-song-003` / `ஓ ரசிக்கும் சீமானே` is one semantic-poetic unit spanning PDF **11→12**.

Review carefully against:

`works/parasakthi/songs/tracks/06-o-rasikkum-seemane.md`

The compressed third stanza, especially around:

`பெண்களின் வாழ்க்கையை இழந்தவர்கள் கோடி`

must not be made smoother by inventing missing syntax.

#### Scene 9

`parasakthi-s009-d001` remains **one** translation unit across PDF **12→13** with `english_page_segments` aligned to the source break `நெஞ்சிலே / நஞ்சைக்`.

Review-sensitive source forms:

- `வங்கத்திலே` is anomalous in context; current English uses context-neutral **`in this land`** and documents that decision
- `தகுதி? போக்கியதை?` is also semantically difficult; preserve rhetorical force and uncertainty rather than over-resolving it
- the monologue's social/political rhetoric must remain forceful; do not flatten it into explanatory prose

#### Scene 10

Source `பெட்டிலே` is currently rendered contextually as hospital **`bed`** in English, with a note. Verify the hospital context but do not change the Tamil form.

## 8. Exact next activity in the new chat

Do **not** jump to scenes 11–15 first.

First perform a deliberate second-pass review of all **66 units in scenes 6–10**:

1. verify unit ordering against `scenes/scene-06.md` through `scene-10.md`;
2. verify every dialogue `source_record_id`, exact source label and page provenance against `dialogues/records/scene-06.json` through `scene-10.json`;
3. verify all stage-direction locators and ensure no action was invented;
4. review scene 6 euphemistic/colloquial language;
5. review scene 7 social vocabulary and Jolly dialogue;
6. review scene 8 song against the verified Tamil track derivative, especially the compressed third stanza;
7. review the complete scene-9 rhetorical monologue, its anomalies and PDF 12→13 segmentation;
8. review scene-10 hospital terminology and grief dialogue;
9. change **English only** where a genuine translation problem is found;
10. if the review passes, set all units/scenes 6–10 to `verified` and update `translations/index.json`, `translations/README.md`, `metadata.yaml`, `data/works.json`, work/root READMEs and the handover;
11. only after that, create the next translation batch for canonical **scenes 11–15** at `review` status.

## 9. Expected post-review state

If scenes 6–10 pass unchanged or after English-only corrections:

- scenes verified: **1–10**
- verified units: **136**
- review units: **0** before creating scenes 11–15

Then immediately begin scenes **11–15**, keeping the same schema and source-linking discipline.

## 10. Repository update discipline

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
- After each durable checkpoint, verify current `main` HEAD and compare against the previous checkpoint to confirm source/Tamil derivative immutability.

## 11. One-line continuation prompt for a new chat

Use this prompt:

> Read `docs/HANDOVER_PARASAKTHI_ENGLISH_TRANSLATION.md` and continue exactly from there. Review scenes 6–10 first; do not begin scenes 11–15 until that review is complete.
