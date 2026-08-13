# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — scene, dialogue, character and song-authorship layers complete; source-faithful song derivative extraction next**.

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

## Song / verse authorship layer — complete-verified

Files:

- `works/parasakthi/songs/README.md`
- `works/parasakthi/songs/schema.json`
- `works/parasakthi/songs/credits.json`
- `works/parasakthi/songs/tracklist-evidence.json`
- `works/parasakthi/songs/inventory.json`
- `works/parasakthi/songs/index.json`

### Booklet-wide credits

PDF 3 prints `பாடல்கள்` and lists six contributors:

- `பாரதியார்`
- `பாரதிதாசன்`
- `உடுமலை நாராயணகவி`
- `மு. கருணாநிதி`
- `கே. பி. காமாட்சி சுந்தரம்`
- `கு. ம. அண்ணல்தங்கோ`

That credits page itself is booklet-wide and does **not** pair contributors with specific songs.

### Item-level evidence received and reconciled

A user-supplied screenshot was matched exactly to the Tamil Wikipedia `பராசக்தி (1952 திரைப்படம்)` soundtrack table: same 11 rows, row order, titles, singers, lyricists, durations, and total length `35:46`.

`tracklist-evidence.json` records the screenshot provenance, identified public page, all 11 rows, and the mapping from soundtrack tracks to our canonical occurrence records. The public page is secondary evidence; it cites a 1952 National Pictures song booklet among its references, but that archived PDF could not be directly retrieved in the session. This limitation remains explicit.

### Final soundtrack authorship

1. `தேசம் ஞானம் கல்வி` — **உடுமலை நாராயண கவி**
2. `கா கா கா` — **உடுமலை நாராயண கவி**
3. `நெஞ்சு பொறுக்கு தில்லையே` — **சுப்பிரமணிய பாரதி**
4. `இல் வாழ்வினிலே` — **பாரதிதாசன்**
5. `புது பெண்ணின் மனதை` — **கே. பி. காமாட்சிசுந்தரம்**
6. `ஓ ரசிக்கும் சீமானே` — **கே. பி. காமாட்சிசுந்தரம்**
7. `எல்லோரும் வாழ வேண்டும்` — **அண்ணல் தங்கோ**
8. `கொஞ்சு மொழி சொல்லும்` — **கே. பி. காமாட்சிசுந்தரம்**
9. `பூமாலை` — **மு. கருணாநிதி**
10. `பொருளே இல்லார்க்கு` — **கே. பி. காமாட்சிசுந்தரம்**
11. `வாழ்க வாழ்கவே` — **பாரதிதாசன்**

### Canonical occurrence reconciliation

The canonical inventory remains **14 occurrence records**, all now `verified` for authorship:

- **13 records** map to the 11 soundtrack tracks.
- `parasakthi-song-005` (`குதம்பாய்` section) and `parasakthi-song-006` (`தாண்டவக்கோனே` section) are separate canonical text occurrences within the same soundtrack track `தேசம் ஞானம் கல்வி`, both by **உடுமலை நாராயண கவி**.
- `parasakthi-song-013` is a partial reprise of `parasakthi-song-011` (`புது பெண்ணின் மனதை`) and therefore shares **கே. பி. காமாட்சிசுந்தரம்**.
- `parasakthi-song-009`, beginning `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு`, is a **separate literary quotation**, not one of the 11 soundtrack tracks. Scene 28 explicitly attributes it to **பாரதிதாசன்**.

Final song-authorship state:

- Candidate occurrence records: **14**
- Verified authorship: **14**
- Review: **0**
- Unresolved: **0**
- Soundtrack compositions: **11**
- Quoted literary-verse records: **1**

No canonical Tamil, scene file, dialogue record, or character mapping was modified during authorship resolution.

## Exact next work — create source-faithful song derivatives

Create **11 soundtrack-composition Tamil derivative files** under `works/parasakthi/songs/` (prefer a dedicated `tracks/` or similarly explicit subdirectory if introducing one).

For each composition:

1. copy Tamil only from the verified canonical transcription / verified scene derivative;
2. record the soundtrack title and verified lyricist from `tracklist-evidence.json`;
3. record all canonical scene occurrence IDs and PDF/printed-page provenance;
4. preserve source line breaks and wording exactly;
5. if a composition spans more than one canonical occurrence, assemble it without losing the occurrence boundary metadata;
6. for `தேசம் ஞானம் கல்வி`, combine the source-faithful text of `parasakthi-song-005` and `parasakthi-song-006` while retaining both occurrence IDs;
7. for `புது பெண்ணின் மனதை`, use scene 33 as the primary composition text and record scene 47 as a reprise occurrence rather than duplicating it as a second song file;
8. do **not** fold the scene-28 Bharathidasan quotation into the soundtrack set; create a separate quoted-verse derivative if desired;
9. do not use web lyrics or audio to repair/normalize any Tamil;
10. after all 11 files are verified, update song README/index, metadata, `data/works.json`, work/root READMEs and this handover.

Only after the source-faithful Tamil song derivative set is complete should song-specific English translation begin.

## Overall stage status

- Structural mapping: verified
- Canonical Tamil transcription: verified
- Tamil fidelity audit: complete
- Scene index: complete
- Scene text derivatives: complete
- Dialogue index: complete-verified
- Character index: complete-verified
- Song/verse inventory: complete
- Song authorship mapping: **complete-verified**
- Song-specific Tamil derivatives: **not-started — next**
- English translation: not-started
