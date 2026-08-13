# பராசக்தி

Archival record for the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**.

## Source-supported identification

The title page shows `பராசக்தி`, `முழு வசனம் + பாடல்கள்`, `திரைக்கதை, வசனம்`, `கலைஞர் மு. கருணாநிதி`, and `விலை ரூபாய் 1-00.` The credits page also prints `கதை-வசனம் — கலைஞர் மு. கருணாநிதி`.

The PDF 3 `பாடல்கள்` credit lists six booklet-wide contributors: **பாரதியார், பாரதிதாசன், உடுமலை நாராயணகவி, மு. கருணாநிதி, கே. பி. காமாட்சி சுந்தரம், கு. ம. அண்ணல்தங்கோ**. The page does not pair those contributors with individual songs, so booklet presence alone is not item-level authorship evidence.

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
- Song/verse inventory: **complete — 14 candidate occurrences**
- Song authorship: **1 verified / 13 unresolved / 0 review**
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

Dialogue extraction is **complete for all 46 observed scenes**, totaling **642 records**. Scenes 23 and 34 remain absent. Scenes 26, 29 and 48 are valid zero-record dialogue scenes. The complete dialogue index contains **11 verified cross-page utterances** and preserves exact source labels/punctuation.

## Character index

The character layer is a separate derivative and does **not** modify any dialogue record.

- [`characters/labels-inventory.json`](characters/labels-inventory.json) — all **69** distinct exact source speaker labels.
- [`characters/entities.json`](characters/entities.json) — complete disposition for all 69 labels.
- [`characters/index.json`](characters/index.json) — final character-index checkpoint.

Final character coverage is **48 entities**, with **66 verified labels**, `ராக` at review, and `நொண்டி` / `நொ` explicitly unresolved. There are **0 unmapped labels**.

## Song / verse authorship gate

The song layer is now initialized and source-inventory complete:

- [`songs/schema.json`](songs/schema.json) — attribution/inventory schema.
- [`songs/credits.json`](songs/credits.json) — exact booklet-wide song contributor credit from PDF 3.
- [`songs/inventory.json`](songs/inventory.json) — **14 candidate song/verse occurrences** in canonical order.
- [`songs/index.json`](songs/index.json) — current checkpoint.
- [`songs/README.md`](songs/README.md) — controlling attribution rules.

The inventory distinguishes unlabelled songs, speaker-labelled verse, quoted verse, and a reprise. It also splits scene 15's `குதம்பாய்` and `தாண்டவக்கோனே` sections because later evidence may establish different authorship.

At this checkpoint, only **one item is internally verified**: `parasakthi-song-009`, the scene-28 quotation beginning `கோரிக்கையற்று கிடக்குதண்ணே—இங்கு`. Narayana Pillai explicitly introduces that quotation as Bharathidasan's verse immediately before it, so the inventory records **பாரதிதாசன்** with `canonical-context-explicit` evidence.

The remaining **13 items stay unresolved**. Even familiar literary/song attributions are not entered until item-level evidence is documented. Outside sources may resolve authorship metadata, but they must never alter canonical Tamil wording.

## Next structured activity

Resolve the **13 unresolved song/verse items** one by one using primary/official or otherwise reliable attribution sources. Record evidence separately, preserve the canonical text unchanged, and only then create song-specific derivative files or English song translations.
