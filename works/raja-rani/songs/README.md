# Raja Rani — song / performance inventory and authorship gate

Status: **complete with unresolved authorship; Tamil 11/11 and English 11/11 complete-verified**.

This layer inventories the source-visible song/singing structures in `ராஜா ராணி` without changing canonical Tamil, immutable dialogue records, or source wording.

## Source song layer

The booklet prints **11 numbered `பாட்டு` blocks** in PDF **4–9**. All 11 are complete or clearly bounded lyric bodies in the verified canonical page layer and have **11/11 standalone verified Tamil derivatives** under `tamil/`.

The PDF-9 film-wide `பாடல்கள்:` roster prints:

- `மு. கருணாநிதி`
- `ஏ. மருதகாசி`
- `கே. பி. காமாக்ஷி`
- `எம். கே. ஆத்மநாதன்`
- `வில்லிபுத்தன்`
- `விவேகன்`

That roster establishes film-wide participation only. It does **not** assign any numbered block to one lyricist.

## Later Kalaignar anthology cross-witness

The verified repository work `works/kalaignar-thirai-isai-paadalgal/` establishes item correspondence at `anthology-attributed` tier for:

- song **3** ↔ `kalaignar-song-019`;
- song **5** ↔ `kalaignar-song-020`;
- song **6** ↔ `kalaignar-song-021`;
- song **7** ↔ `kalaignar-song-022`;
- song **8** ↔ `kalaignar-song-023`.

These five remain **later-anthology Kalaignar-attributed**, not original-film primary-source item credits. Songs **1, 2, 4, 9, 10 and 11** remain unresolved.

The later witness is never textual authority for this booklet. Edition differences remain visible; for example, Raja Rani song 8 retains `லீலா!...லாலீ!...அது போலீ!...` rather than importing the later anthology's different opening.

## Screenplay singing references

Four source-visible screenplay references remain dispositioned:

1. scene 4 / PDF 13 → song 3 — **verified**;
2. scene 16 / PDF 30 → song 5 — **verified**;
3. scene 40 / PDF 58 → song 8 — **verified**;
4. scene 58 / PDF 79 → song 11 — **review**, because the cue prints only `(இருவரும் பாடுகிறார்கள்)` and no song number/lyric.

No absent lyric is supplied for a screenplay cue.

## Tamil derivatives

- numbered song blocks: **11**;
- verified Tamil song derivatives: **11/11**;
- screenplay singing references: **4**;
- total song/singing occurrences inventoried: **15**;
- later-anthology Kalaignar-attributed numbered songs: **5**;
- unresolved numbered-song lyricists: **6**;
- original-booklet item-level lyricist credits: **0**.

## English numbered-song translation

The dedicated source-linked English layer under `../translations/songs/` is now **complete-verified**:

- English numbered-song records: **11/11**;
- translation sections / source-turn groups: **67**;
- Tamil source line/cue entries represented: **181**;
- English line/cue entries represented: **181**;
- multi-page song records: **4** — songs 2, 3, 8 and 10;
- draft/review/not-started song translations: **0/0/0**.

Translation changed **no** authorship tier and **no** screenplay performance-link status. Song 11's scene-58 relation remains review-level.

English index: `../translations/songs/index.json`.  
English QA: `../translations/songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`.

## Scene-16 derivative correction found during the song gate

Canonical PDF 30 contains the source divider and verified singing stage direction before `ஞானக்கண்: ராணி! ராணி...!`. The earlier `scenes/scene-016.md` derivative had omitted that non-dialogue source material; it was restored from canonical Tamil without altering dialogue records or fidelity totals.

## Files

- `schema.json`
- `credits.json`
- `cross-witness-evidence.json`
- `inventory.json`
- `index.json`
- `tamil/README.md`
- `tamil/song-001.md` through `tamil/song-011.md`
- English derivative: `../translations/songs/`

## Final downstream state

The source song/performance gate remains **complete with unresolved authorship** and its evidence tiers are unchanged:

- Tamil numbered-song derivatives: **11/11 complete-verified**;
- English numbered-song derivatives: **11/11 complete-verified**;
- reader/export: **complete-verified — QA PASS**;
- Reading Room payload: **complete-verified — QA PASS**;
- site application: **not-applied**;
- authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**;
- screenplay performance relations: **3 verified / 1 review**.

No later translation, reader or integration phase upgrades authorship or the scene-58/song-11 review relation.

## Next gate

No repository-internal song/performance work remains. Preserve this evidence state; apply the verified Reading Room payload externally only when that separate repository is explicitly authorized.
