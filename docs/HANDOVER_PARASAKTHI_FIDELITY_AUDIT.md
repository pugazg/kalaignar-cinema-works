# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — source, scene, dialogue, character, song-authorship and Tamil song-derivative layers complete; English translation pilot next**.

## Canonical source state

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- 58 PDF pages; PDF 4–57 / printed pp.3–56 are canonical dialogue/song pages; PDF 58 is back matter.
- Tamil canonical text: **54 verified / 0 review / 0 unresolved markers**.
- Never repair Tamil from film audio, subtitles, web copies, later editions or memory.

Final reviewer-assisted Part 01 readings remain:

- PDF 5: `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?`
- PDF 16: `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...`

## Scene structure — complete

- **46 observed canonical scenes**.
- Scene **23 absent**.
- Scene **34 absent**.
- PDF 49 source heading **48** → canonical scene **43**.
- PDF 57 source heading **43** → canonical final scene **48**.
- Scene 30 crosses PDF 35→36 across the Part 01 / Part 02 transcription-file boundary.
- Scene 33 spans PDF 38→42 because scene 34 is absent.
- All **46/46 observed scene derivatives are complete**.

## Dialogue index — complete-verified

- Records: **642** across all 46 observed scenes.
- Zero-record observed scenes: **26, 29, 48**.
- Cross-page records verified: **11**.
- Existing dialogue records are immutable derivatives and must not be rewritten by later indexes.
- Source-label punctuation anomalies remain preserved in `parasakthi-s021-d040`, `parasakthi-s025-d011`, and `parasakthi-s025-d017`.

## Character index — complete-verified

- Distinct exact source labels: **69**.
- Explicit label dispositions: **69 / 69**.
- Entities: **48**.
- Verified entities: **46**.
- Review entities: **1**.
- Unresolved entities: **1**.
- Verified labels: **66**.
- Review label: `ராக`.
- Unresolved labels: `நொண்டி`, `நொ`.
- Dialogue records modified by character indexing: **0**.

Do not force `நொண்டி` / `நொ` into ஞானசேகரன் without explicit source evidence.

## Song / verse layer — complete-verified

Files:

- `works/parasakthi/songs/README.md`
- `works/parasakthi/songs/schema.json`
- `works/parasakthi/songs/credits.json`
- `works/parasakthi/songs/tracklist-evidence.json`
- `works/parasakthi/songs/inventory.json`
- `works/parasakthi/songs/index.json`
- `works/parasakthi/songs/tracks/`
- `works/parasakthi/songs/quoted-verses/`

### Booklet-wide credits

PDF 3 prints `பாடல்கள்` and lists six contributors:

- `பாரதியார்`
- `பாரதிதாசன்`
- `உடுமலை நாராயணகவி`
- `மு. கருணாநிதி`
- `கே. பி. காமாட்சி சுந்தரம்`
- `கு. ம. அண்ணல்தங்கோ`

That credits page is booklet-wide and does **not** pair contributors with individual songs.

### Item-level soundtrack evidence

The user-supplied soundtrack screenshot was matched exactly to the Tamil Wikipedia `பராசக்தி (1952 திரைப்படம்)` soundtrack table: same 11 rows, titles, singers, lyricists, durations and total `35:46`.

`tracklist-evidence.json` preserves that secondary evidence and the limitation that the referenced 1952 National Pictures song booklet could not be directly retrieved in the session.

### Final authorship state

- Canonical song/verse occurrence records: **14**
- Verified authorship: **14**
- Review: **0**
- Unresolved: **0**
- Soundtrack compositions: **11**
- Soundtrack-linked occurrence records: **13**
- Separate quoted literary-verse records: **1**

Final soundtrack lyricists:

1. `தேசம் ஞானம் கல்வி` — உடுமலை நாராயண கவி
2. `கா கா கா` — உடுமலை நாராயண கவி
3. `நெஞ்சு பொறுக்கு தில்லையே` — சுப்பிரமணிய பாரதி
4. `இல் வாழ்வினிலே` — பாரதிதாசன்
5. `புது பெண்ணின் மனதை` — கே. பி. காமாட்சிசுந்தரம்
6. `ஓ ரசிக்கும் சீமானே` — கே. பி. காமாட்சிசுந்தரம்
7. `எல்லோரும் வாழ வேண்டும்` — அண்ணல் தங்கோ
8. `கொஞ்சு மொழி சொல்லும்` — கே. பி. காமாட்சிசுந்தரம்
9. `பூமாலை` — மு. கருணாநிதி
10. `பொருளே இல்லார்க்கு` — கே. பி. காமாட்சிசுந்தரம்
11. `வாழ்க வாழ்கவே` — பாரதிதாசன்

### Tamil soundtrack derivatives — complete-verified

Exactly **11 source-faithful composition files** now exist under `works/parasakthi/songs/tracks/`:

1. `01-desam-gnanam-kalvi.md`
2. `02-kaa-kaa-kaa.md`
3. `03-nenju-porukkuthillaiye.md`
4. `04-il-vaazhvinile.md`
5. `05-pudhu-pennin-manathai.md`
6. `06-o-rasikkum-seemane.md`
7. `07-ellorum-vaazha-vendum.md`
8. `08-konju-mozhi-sollum.md`
9. `09-poomalai.md`
10. `10-porule-illaarkku.md`
11. `11-vaazhga-vaazhgave.md`

Source-faithfulness rules applied:

- Tamil bodies were copied only from verified scene/canonical text.
- Track metadata comes from `tracklist-evidence.json` and never alters Tamil wording.
- Cross-page source anchors are retained where they occur.
- Scene 4 speaker labels remain because they are canonical source representation.
- `தேசம் ஞானம் கல்வி` combines two canonical occurrence records (`005`, `006`) inside one composition file while retaining both occurrence boundaries.
- `புது பெண்ணின் மனதை` uses scene 33 as primary text and preserves scene 47 as a reprise section inside the same composition file.
- Scene 48's song file contains only song text; `—சுபம்—` and printer line are excluded.

### Separate quoted verse

`works/parasakthi/songs/quoted-verses/001-vidhavayin-kaadhal.md` preserves the scene-28 Bharathidasan quotation beginning `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு`.

It is **not** counted among the 11 soundtrack compositions.

No canonical Tamil, scene file, dialogue record or character mapping was modified by song derivative extraction.

## Exact next work — English translation pilot

Create a separate translation layer under `works/parasakthi/translations/`.

First checkpoint should be schema-first and small:

1. create `translations/README.md` defining translation principles;
2. create `translations/schema.json` for source-linked translation records;
3. create `translations/index.json` with pilot status;
4. use immutable source references rather than copying/rewriting Tamil identifiers;
5. distinguish at minimum `dialogue`, `stage-direction`, `song`, and `quoted-verse` translation units;
6. preserve exact canonical scene number, source record/occurrence ID, PDF/printed-page provenance and source path;
7. never alter `speaker_label`; normalized character identity may be referenced separately from the character index;
8. mark translation status independently (`draft`, `review`, `verified`);
9. do not treat fluent English as permission to simplify or correct the Tamil source;
10. start with a **small pilot**, preferably canonical scene 1 because it exercises a stage direction, a verified song composition (`வாழ்க வாழ்கவே`) and the cross-page Thangappan dialogue in one bounded scene.

For scene-1 pilot translation:

- source scene: `works/parasakthi/scenes/scene-01.md`;
- song source: `works/parasakthi/songs/tracks/11-vaazhga-vaazhgave.md`;
- dialogue source record: `parasakthi-s001-d001`;
- preserve PDF 4→5 / printed pp.3→4 provenance for the Thangappan utterance;
- translation must remain a derivative and must not change any Tamil file.

After the pilot is reviewed, choose the batching strategy for full-scene translation and song-specific English derivatives.

## Overall stage status

- Structural mapping: verified
- Canonical Tamil transcription: verified
- Tamil fidelity audit: complete
- Scene index: complete
- Scene text derivatives: complete
- Dialogue index: complete-verified
- Character index: complete-verified
- Song/verse inventory: complete
- Song authorship mapping: complete-verified
- Song-specific Tamil derivatives: **complete-verified — 11/11**
- Separate quoted-verse derivatives: **complete-verified — 1**
- English translation: **not-started — next**
