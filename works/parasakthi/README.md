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
- Dialogue index: **complete-verified — 642 records / 46 observed scenes**
- Character index: **complete-verified — 69/69 exact labels have an explicit disposition**
- Character entities: **48 total — 46 verified, 1 review, 1 unresolved**
- Character label dispositions: **66 verified, 1 review, 2 unresolved, 0 unmapped**
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

Dialogue extraction is **complete for all 46 observed scenes**, totaling **642 records**. Scenes 23 and 34 remain absent. Scenes 26, 29 and 48 are valid zero-record dialogue scenes. Scene 48 contains the unlabelled closing song plus `—சுபம்—` / printer line.

The complete dialogue index contains **11 verified cross-page utterances**. Exact speaker labels and source punctuation anomalies remain unnormalized.

## Character index

The character layer is a separate derivative and does **not** modify any dialogue record.

- [`characters/labels-inventory.json`](characters/labels-inventory.json) — all **69** distinct exact source speaker labels.
- [`characters/schema.json`](characters/schema.json) — entity/mapping schema.
- [`characters/entities-pilot.json`](characters/entities-pilot.json) — preserved 8-entity pilot.
- [`characters/entities.json`](characters/entities.json) — complete disposition for all 69 labels.
- [`characters/index.json`](characters/index.json) — final character-index checkpoint.

Final character coverage:

- **48 entities** total;
- **46 verified entities**;
- **1 review entity** — `ராக` → display form `இராகவன்`, retained at review because converting the printed vocative `இராகவா` to a nominative name is a grammatical normalization;
- **1 unresolved entity** — `நொண்டி` / `நொ`;
- **66 verified labels + 1 review label + 2 unresolved labels = 69/69**;
- **0 unmapped labels**.

Important conservative decisions are documented in [`characters/README.md`](characters/README.md). In particular, `நொண்டி` / `நொ` are **not** merged into ஞானசேகரன் because scene 37 proves the speaker is Kalyani's brother but does not explicitly identify which brother. Conversely, scene 43's `குரல்` is mapped to குணசேகரன் because the verified stage direction places the voice behind the goddess image and immediately has Gunasekaran emerge from that exact position.

## Next structured activity

Proceed to the **per-song authorship gate**. The booklet credits multiple song/lyric contributors, so first identify every song/verse block and map its authorship from the printed credits where possible. If the booklet does not disambiguate a particular song, keep authorship `unresolved` unless separately cited reliable evidence resolves it. Do not use outside sources to alter the canonical Tamil text.
