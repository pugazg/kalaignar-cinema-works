# பராசக்தி

Archival record for the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**.

## Source-supported identification

The title page shows `பராசக்தி`, `முழு வசனம் + பாடல்கள்`, `திரைக்கதை, வசனம்`, `கலைஞர் மு. கருணாநிதி`, and `விலை ரூபாய் 1-00.` The credits page also prints `கதை-வசனம் — கலைஞர் மு. கருணாநிதி` and lists multiple song/lyric contributors, so individual songs are not attributed automatically to Kalaignar.

## Scan

- Source: `TVA_BOK_0062968_பராசக்தி.pdf`
- PDF pages: **58**
- SHA-256: `b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c`
- Image-only scan
- Canonical dialogue/song range: PDF **4–57** / printed pp. **3–56**
- PDF 58: rear advertisement / back matter

See [`mapping.md`](mapping.md) for the structural page map.

## Scene numbering

The verified source contains **46 observed scene headings**. Headings 23 and 34 are not observed.

The booklet transposes two late scene numbers:

- PDF 49 / printed p.48: source `காட்சி-48` → canonical **scene 43**;
- PDF 57 / printed p.56: source `காட்சி-43` → canonical final **scene 48**.

The canonical layer corrects those two numbers explicitly while retaining the printed readings as provenance.

## Current state

- Canonical Tamil transcription: **54 verified / 0 review**
- Remaining source uncertainties: **0**
- Scene index: **complete — 46 records**
- Individual scene derivatives: **complete — 46/46 observed scenes**
- Dialogue index: **complete and verified — 642 records / 46 observed scenes**
- Character index: **pilot verified — 69 exact labels inventoried; 8 entities / 18 labels mapped**
- Character labels remaining for review: **51**
- Per-song authorship mapping: **not-started**
- English translation: **not-started**

The final reviewer-assisted Part 01 readings are `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?` on PDF 5 and `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...` on PDF 16.

## Canonical transcription

- [`transcription/parts/part-01-pdf-4-35.md`](transcription/parts/part-01-pdf-4-35.md) — PDF 4–35; fully verified.
- [`transcription/parts/part-02-pdf-36-57.md`](transcription/parts/part-02-pdf-36-57.md) — PDF 36–57; fully verified after consolidated correction and post-rewrite checking.

The scan controls the Tamil. Film audio, subtitles, later editions, web quotations and memory are not used to repair the canonical text.

## Scene derivatives

[`scenes/index.json`](scenes/index.json) and [`scenes/README.md`](scenes/README.md) define the complete scene layer. Important cases include scene 30 crossing the Part 01/Part 02 file boundary, scene 33 continuing because scene 34 is absent, and the documented source/canonical numbering distinction for scenes 43 and 48.

## Dialogue index

[`dialogues/schema.json`](dialogues/schema.json) is the fixed record schema. [`dialogues/index.json`](dialogues/index.json) is the final manifest; records are stored by canonical scene under [`dialogues/records/`](dialogues/records/).

Dialogue extraction is **complete for all 46 observed scenes**, totaling **642 records**. Scenes 23 and 34 remain absent. Scene 48 is a valid zero-record dialogue scene because its content is the unlabelled closing song plus `—சுபம்—` / printer line.

The complete dialogue index contains **11 verified cross-page utterances**. Exact speaker labels and source punctuation anomalies remain unnormalized.

## Character index

[`characters/labels-inventory.json`](characters/labels-inventory.json) inventories every exact speaker label in the completed dialogue layer. It records **69 distinct exact labels** across the 642 records.

[`characters/schema.json`](characters/schema.json) defines a separate entity layer; [`characters/entities-pilot.json`](characters/entities-pilot.json) contains the first **8 verified character entities**, mapping **18 exact labels**:

- குணசேகரன்
- கல்யாணி
- சந்திரசேகரன்
- ஞானசேகரன்
- சரஸ்வதி
- தங்கப்பன்
- மாணிக்கம் பிள்ளை
- விமலா

The character derivative does not modify dialogue records. Exact labels remain intact in `dialogues/records/`; only the separate character layer links supported variants to stable entity IDs.

The pilot deliberately leaves **51 labels** unmapped. Ambiguous or generic labels are not merged merely because their spelling or narrative context suggests a likely identity. For example, `நொண்டி` / `நொ` remain outside the ஞானசேகரன் entity until the systematic evidence pass.

## Next structured activity

Expand the character/entity index across the remaining **51 exact source labels**. Resolve evidence-backed named characters and roles, create role/collective entities where appropriate, and retain genuinely ambiguous labels as explicitly unresolved. Do not modify any of the 642 dialogue records.
