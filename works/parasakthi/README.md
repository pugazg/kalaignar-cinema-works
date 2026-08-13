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
- Dialogue index: **in-progress-verified — 527 records across 38 observed scenes**
- Character index: **not-started**
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

[`dialogues/schema.json`](dialogues/schema.json) is the fixed record schema. [`dialogues/index.json`](dialogues/index.json) is the compact checkpoint; records are stored by canonical scene under [`dialogues/records/`](dialogues/records/).

Dialogue extraction is verified for canonical scenes **1–22, 24–33 and 35–40**, totaling **527 records**. Scenes 23 and 34 remain absent.

The observed 31–40 batch added **114 records**:

- scene 31: 13
- scene 32: 4
- scene 33: 56
- scene 35: 10
- scene 36: 4
- scene 37: 8
- scene 38: 8
- scene 39: 9
- scene 40: 2

Scene 33 intentionally spans PDF **38–42** because scene 34 is absent. `parasakthi-s033-d053` crosses PDF **41→42** and remains one record with `page_segments`. The unlabelled dream song inside scene 33 is excluded. Scene 39's opening unlabelled song is also excluded; only the explicitly labelled dialogue that follows is indexed.

Current cross-page records are:

- `parasakthi-s001-d001` — PDF 4→5;
- `parasakthi-s009-d001` — PDF 12→13;
- `parasakthi-s013-d023` — PDF 16→17;
- `parasakthi-s028-d023` — PDF 33→34;
- `parasakthi-s033-d053` — PDF 41→42.

Scenes 26 and 29 remain valid zero-record dialogue files. Source-label punctuation anomalies documented in scenes 21 and 25 remain preserved without normalization.

## Next dialogue batch

Extract the **final observed scenes 41–48**. The canonical/source heading distinction must be retained for canonical scene **43** (`source_scene_heading: 48`) and canonical final scene **48** (`source_scene_heading: 43`).
