# Parasakthi — controlling handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Handover refreshed: 2026-08-13

Current stage: **Structured Derivatives — scene, dialogue and character indexes complete; song/verse inventory complete; item-level authorship resolution next**.

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

Files:

- `works/parasakthi/dialogues/schema.json`
- `works/parasakthi/dialogues/index.json`
- `works/parasakthi/dialogues/records/scene-XX.json`

Final state:

- Observed scenes represented: **46 / 46**
- Dialogue records: **642**
- Zero-record observed scenes: **26, 29, 48**
- Missing headings: **23, 34**
- Existing dialogue records are immutable derivatives and must not be rewritten by later indexes.
- Cross-page records verified: **11**.

Source-label punctuation anomalies remain preserved in dialogue records:

- `parasakthi-s021-d040`
- `parasakthi-s025-d011`
- `parasakthi-s025-d017`

## Character index — complete-verified

Files:

- `works/parasakthi/characters/README.md`
- `works/parasakthi/characters/schema.json`
- `works/parasakthi/characters/labels-inventory.json`
- `works/parasakthi/characters/entities-pilot.json`
- `works/parasakthi/characters/entities.json`
- `works/parasakthi/characters/index.json`

Final coverage:

- Distinct exact source labels: **69**
- Explicit label dispositions: **69 / 69**
- Unmapped labels: **0**
- Entities: **48**
- Verified entities: **46**
- Review entities: **1**
- Unresolved entities: **1**
- Labels attached to verified entities: **66**
- Review label: `ராக`
- Unresolved labels: `நொண்டி`, `நொ`
- Dialogue records modified by character indexing: **0**

Important conservative decisions remain documented in `characters/README.md`. Do not force `நொண்டி` / `நொ` into ஞானசேகரன் without explicit source evidence.

## Song / verse authorship gate — inventory complete

Files:

- `works/parasakthi/songs/README.md`
- `works/parasakthi/songs/schema.json`
- `works/parasakthi/songs/credits.json`
- `works/parasakthi/songs/inventory.json`
- `works/parasakthi/songs/index.json`

### Exact booklet-wide song credits

PDF 3 prints the heading `பாடல்கள்` followed by:

- `பாரதியார்`
- `பாரதிதாசன்`
- `உடுமலை நாராயணகவி`
- `மு. கருணாநிதி`
- `கே. பி. காமாட்சி சுந்தரம்`
- `கு. ம. அண்ணல்தங்கோ`

This is a **booklet-wide contributor list**. The credits page does **not** pair contributors with specific songs. `songs/credits.json` records `item_level_assignment_present: false`.

### Candidate inventory

The source-led inventory contains **14 candidate song/verse occurrences**:

1. `parasakthi-song-001` — scene 1 — `வாழ்க வாழ்கவே வாழ்க வாழ்கவே` — PDF 4.
2. `parasakthi-song-002` — scene 4 — `இவ்வாழ்வினிலே ஒளி ஏற்றும் தீபம்` — PDF 8 — speaker-labelled verse / dialogue overlap.
3. `parasakthi-song-003` — scene 8 — `ஓ ரசிகரும் சீமானே வா` — PDF 11→12.
4. `parasakthi-song-004` — scene 12 — `பூமாலே நீயே புழுதி மண்மேலே வீணே` — PDF 14.
5. `parasakthi-song-005` — scene 15 — `தேசம், ஞானம், கல்வி, ஈசன் பூசையெல்லாம்` — PDF 19→20 — `குதம்பாய்` section.
6. `parasakthi-song-006` — scene 15 — `ஆரியக் கூத்தாடினாலும்` — PDF 20 — `தாண்டவக்கோனே` section.
7. `parasakthi-song-007` — scene 17 — `கொஞ்சும் மொழி சொல்லும் கிளியே` — PDF 21→22.
8. `parasakthi-song-008` — scene 26 — `கா—கா—கா—கா—` — PDF 31→32.
9. `parasakthi-song-009` — scene 28 — `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு` — PDF 33 — quoted verse.
10. `parasakthi-song-010` — scene 29 — `பொருளே இல்லார்க்கு தொல்லையா` — PDF 35.
11. `parasakthi-song-011` — scene 33 — `புதுப்பெண்ணின் மனதைத் தொட்டுப் போறவரே` — PDF 40.
12. `parasakthi-song-012` — scene 39 — `நெஞ்சு பொறுக்குதில்லையே—இந்த` — PDF 44→45.
13. `parasakthi-song-013` — scene 47 — short reprise of song 011 — PDF 56.
14. `parasakthi-song-014` — scene 48 — `எல்லோரும் வாழ வேண்டும்—உயிர்கள்` — PDF 57.

The earlier structural map was only a verse-location aid. This inventory improves it by splitting the two structurally separable scene-15 sections and adding the scene-28 literary quotation on PDF 33.

### Current authorship state

- Candidate occurrences: **14**
- Authorship verified: **1**
- Authorship review: **0**
- Authorship unresolved: **13**

`parasakthi-song-009` is the only internally verified item at this checkpoint. In scene 28, Narayana Pillai says `யாரோ பாரதிதாசனும் விதவையைப் பற்றி சொல்லியிருக்கான் பாரு` immediately before the verse, so its lyric/verse authorship is recorded as **பாரதிதாசன்** with `canonical-context-explicit` evidence.

All other 13 records remain unresolved even when a literary or soundtrack attribution may be familiar. Familiarity is not archival evidence.

Special cases:

- Scene 4 performers/speaker labels do not imply lyric authorship.
- Scene 15's `குதம்பாய்` and `தாண்டவக்கோனே` sections are separate inventory records so mixed authorship can be represented if evidence requires it.
- Scene 33 has a partial reprise in scene 47; the reprise points back to the original block.
- Scene 39 explicitly says `நெஞ்சு பொறுக்குதில்லையே` is another person's song but does not name the author in the scene text.
- Scene 48 is an unlabelled collective closing song; scene 47 immediately precedes it with `(பேதமின்றி பாடுகின்றனர்)`.

## Exact next work — resolve 13 unresolved authorship records

Proceed item by item from `songs/inventory.json`.

For each unresolved item:

1. preserve the canonical opening line and page/scene provenance exactly;
2. search first for primary/official or otherwise reliable attribution sources;
3. prefer sources that identify the exact song/title/opening line, not merely a generic film-credit list;
4. record the attribution source separately from canonical text;
5. if multiple reliable sources disagree, mark the record `review` and preserve the disagreement;
6. if no reliable item-level source is found, leave the item `unresolved`;
7. outside evidence may change only attribution metadata — never canonical Tamil wording;
8. do not create song-specific English translations until the corresponding authorship record has an explicit disposition.

A practical first resolution batch should cover the most recognizable exact openings: `வாழ்க வாழ்கவே`, `நெஞ்சு பொறுக்குதில்லையே`, the two scene-15 sections, and the scene-33/47 `புதுப்பெண்ணின்...` composition. Then continue through the remaining items.

## Other stages

- Structural mapping: verified
- Canonical Tamil transcription: verified
- Tamil fidelity audit: complete
- Scene index: complete
- Scene text derivatives: complete
- Dialogue index: complete-verified
- Character index: complete-verified
- Song/verse inventory: complete
- Song authorship mapping: **in progress — 1 verified / 13 unresolved**
- English translation: not started
