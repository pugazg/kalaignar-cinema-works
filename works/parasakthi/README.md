# பராசக்தி

Archival record for the scanned booklet **`பராசக்தி — முழு வசனம் + பாடல்கள்`**.

## Source-supported identification

The title page shows `பராசக்தி`, `முழு வசனம் + பாடல்கள்`, `திரைக்கதை, வசனம்`, `கலைஞர் மு. கருணாநிதி`, and `விலை ரூபாய் 1-00.` The credits page also prints `கதை-வசனம் — கலைஞர் மு. கருணாநிதி`.

The PDF 3 `பாடல்கள்` credit lists six booklet-wide contributors: **பாரதியார், பாரதிதாசன், உடுமலை நாராயணகவி, மு. கருணாநிதி, கே. பி. காமாட்சி சுந்தரம், கு. ம. அண்ணல்தங்கோ**. That page itself does not pair contributors with individual songs; item-level resolution is therefore kept in the separate song derivative layer.

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
- Song/verse inventory: **complete — 14 occurrence records**
- Song authorship: **complete-verified — 14 verified / 0 review / 0 unresolved**
- Soundtrack compositions represented: **11**
- English translation: **not-started**

The final reviewer-assisted Part 01 readings are `கல்யாணிக்குக் கல்யாணம் உங்களுக்குத் தெரியுமா?` on PDF 5 and `குதிரைக்கு பதிலாக நரம்பு தெறிக்கத்தெறிக்க ரிக்ஷா இழுத்துக்...` on PDF 16.

## Canonical transcription

- [`transcription/parts/part-01-pdf-4-35.md`](transcription/parts/part-01-pdf-4-35.md) — PDF 4–35; fully verified.
- [`transcription/parts/part-02-pdf-36-57.md`](transcription/parts/part-02-pdf-36-57.md) — PDF 36–57; fully verified after consolidated correction and post-rewrite checking.

The scan controls the Tamil. Film audio, subtitles, later editions, web quotations and memory are not used to repair the canonical text.

## Scene, dialogue and character derivatives

[`scenes/`](scenes/) is complete for all 46 observed scenes. [`dialogues/`](dialogues/) contains **642 verified speaker-labelled records**. [`characters/`](characters/) gives explicit disposition to all **69 exact source speaker labels** across **48 entities**, with uncertainty retained rather than guessed away.

None of those derivative layers rewrites the canonical Tamil.

## Song / verse authorship layer

Files:

- [`songs/schema.json`](songs/schema.json)
- [`songs/credits.json`](songs/credits.json)
- [`songs/tracklist-evidence.json`](songs/tracklist-evidence.json)
- [`songs/inventory.json`](songs/inventory.json)
- [`songs/index.json`](songs/index.json)
- [`songs/README.md`](songs/README.md)

A user-supplied soundtrack screenshot was matched exactly to the Tamil Wikipedia soundtrack table for the 1952 film: the same **11 tracks**, singers, lyricists, durations and total length **35:46**. This item-level evidence resolves the soundtrack compositions without changing any canonical lyric wording.

Final soundtrack lyricists represented:

- `தேசம் ஞானம் கல்வி` — **உடுமலை நாராயண கவி**
- `கா கா கா` — **உடுமலை நாராயண கவி**
- `நெஞ்சு பொறுக்கு தில்லையே` — **சுப்பிரமணிய பாரதி**
- `இல் வாழ்வினிலே` — **பாரதிதாசன்**
- `புது பெண்ணின் மனதை` — **கே. பி. காமாட்சிசுந்தரம்**
- `ஓ ரசிக்கும் சீமானே` — **கே. பி. காமாட்சிசுந்தரம்**
- `எல்லோரும் வாழ வேண்டும்` — **அண்ணல் தங்கோ**
- `கொஞ்சு மொழி சொல்லும்` — **கே. பி. காமாட்சிசுந்தரம்**
- `பூமாலை` — **மு. கருணாநிதி**
- `பொருளே இல்லார்க்கு` — **கே. பி. காமாட்சிசுந்தரம்**
- `வாழ்க வாழ்கவே` — **பாரதிதாசன்**

The canonical inventory remains **14 occurrence records**, because soundtrack identity and source-text occurrence are not one-to-one: scene 15's `குதம்பாய்` and `தாண்டவக்கோனே` sections are two textual occurrences within one soundtrack track; scene 47 reprises the scene-33 composition; and scene 28 contains a separate Bharathidasan literary quotation rather than a soundtrack song.

## Next structured activity

Create source-faithful Tamil derivative files for the **11 soundtrack compositions**, copying text only from the verified canonical transcription/scene derivatives. Each derivative should retain authorship evidence, PDF/printed-page provenance, and all occurrence/reprise links. Keep the scene-28 Bharathidasan quotation as a separate quoted-verse derivative rather than folding it into the soundtrack set.
