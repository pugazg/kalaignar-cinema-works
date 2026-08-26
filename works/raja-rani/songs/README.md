# Raja Rani — song / performance inventory and authorship gate

Status: **complete with unresolved authorship**.

This layer inventories the source-visible song/singing structures in `ராஜா ராணி` without changing canonical Tamil, immutable dialogue records, or source wording.

## Source song layer

The booklet prints **11 numbered `பாட்டு` blocks** in PDF **4–9** (first part of PDF 9). All 11 are complete or clearly bounded lyric bodies in the verified canonical page layer, so this gate creates **11/11 standalone verified Tamil derivatives** under `tamil/`.

The PDF-9 film-wide `பாடல்கள்:` roster prints:

- `மு. கருணாநிதி`
- `ஏ. மருதகாசி`
- `கே. பி. காமாக்ஷி`
- `எம். கே. ஆத்மநாதன்`
- `வில்லிபுத்தன்`
- `விவேகன்`

That roster establishes film-wide participation only. It does **not** assign any numbered block to one lyricist.

## Later Kalaignar anthology cross-witness

The verified repository work `works/kalaignar-thirai-isai-paadalgal/` contains five Raja Rani items at `anthology-attributed` tier. Item correspondence is established for:

- numbered song **3** ↔ `kalaignar-song-019` — `வாங்க... வாங்க... வாங்க...`
- numbered song **5** ↔ `kalaignar-song-020` — `வேலை யில்லாத தொல்லை`
- numbered song **6** ↔ `kalaignar-song-021` — `ஆழிசூழ் உலகம் விடிந்த தென்று என்`
- numbered song **7** ↔ `kalaignar-song-022` — `மணிப் புறா!... புது மணிப் புறா!...`
- numbered song **8** ↔ `kalaignar-song-023` — `கண்ணற்ற தகப்பனுக்கு பெண்ணாகப் பிறந்தவளே!`

These five are therefore dispositioned as **verified item correspondences / anthology-attributed to மு. கருணாநிதி**. This is deliberately not described as original-film primary-source item credit.

The later witness is not a textual authority for this booklet. Edition differences remain visible. In particular, Raja Rani song 8 prints `சீலா!...லாலீ!...அது போலீ!...`, while the later anthology opens its corresponding item `வீணா!... வாலி!... அது போலி!...`; the Raja Rani reading remains unchanged.

The other six numbered blocks—1, 2, 4, 9, 10 and 11—remain **authorship unresolved** at this gate. No singer, character, soundtrack memory or film-wide roster order is used to guess a lyricist.

## Screenplay singing references

A navigation sweep of the verified screenplay/canonical text found four actual source-visible singing references relevant to this gate:

1. scene 4 / PDF 13: `[ராணி பாடிக் கொண்டே டிக்கட் விற்கிறாள்...]` — securely linked to numbered song 3.
2. scene 16 / PDF 30: `[ராணி “வேலையில்லாத் தொல்லையில்லை” என்று பாடிக் கொண்டிருக்கிறாள்.]` — securely linked to numbered song 5.
3. scene 40 / PDF 58: `[ராஜா பாடிக்கொண்டு வருகிறான்.]`; Rani's immediate `பூலோகம் ... இருண்டு போகலே` response securely links the performance to numbered song 8.
4. scene 58 / PDF 79: `(இருவரும் பாடுகிறார்கள்)` after Raja's statement that love cannot be hidden. This strongly echoes numbered song 11 but the source does not print the song number or lyric at the cue, so the link remains **review** rather than being forced.

No absent lyric is supplied for any screenplay cue.

## Scene-16 derivative correction found during this gate

Canonical PDF 30 contains the source divider and verified singing stage direction before `ஞானக்கண்: ராணி! ராணி...!`. The earlier `scenes/scene-016.md` derivative had omitted that non-dialogue source material.

This gate restores the source divider and stage direction to the scene derivative. This is a **derivative completeness correction only**:

- canonical page text: unchanged;
- fidelity totals: unchanged;
- dialogue records: unchanged;
- character mapping: unchanged.

## Final counts

- numbered song blocks: **11**
- full verified Tamil song derivatives: **11/11**
- screenplay singing references: **4**
- total song/singing occurrences inventoried: **15**
- numbered songs anthology-attributed to Kalaignar: **5**
- numbered songs with unresolved lyricist: **6**
- original-booklet item-level lyricist credits: **0**

## Files

- `schema.json`
- `credits.json`
- `cross-witness-evidence.json`
- `inventory.json`
- `index.json`
- `tamil/README.md`
- `tamil/song-001.md` through `tamil/song-011.md`

## Next gate

The next structured phase is **source-linked English translation from verified Tamil only**. The translation layer must retain song units distinctly, translate screenplay singing references only to the extent printed, preserve exact source linkage, and never invent absent lyrics or upgrade unresolved authorship.
