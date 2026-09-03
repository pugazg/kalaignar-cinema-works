# Raja Rani — Final English Screenplay Translation QA

Status: **PASS — screenplay English translation complete and source-linked**

This checkpoint closes the English translation of all archival screenplay segments for `ராஜா ராணி` after the final source-review resolutions and the T055/T056 derivative-boundary correction.

## Final corpus census

- archival screenplay scenes: **58 / 58 translated and verified**
- source-blocked scenes: **0**
- verified English units: **1,236**
- unique immutable dialogue records in the corrected corpus: **1,071**
- immutable dialogue links from English: **1,071 / 1,071**
- dialogue-kind English units: **1,090**
- stage-direction units: **137**
- performance-cue units: **4**
- written-text units: **5**
- source-unlabelled spoken units: **19**
- genuine cross-page English units: **15**
- numbered front-matter song translations: **0 / 11**

The 1,090 dialogue-kind units consist of the 1,071 immutable source-labelled dialogue records plus 19 source-unlabelled spoken units that deliberately remain null-speaker/null-record.

## T055 / T056 boundary correction

Final QA discovered that the earlier `scene-055.md` derivative had continued past its declared `end_before=T056` boundary and duplicated the complete `(முன்)` flashback already represented by `scene-056.md`. The corresponding dialogue shard duplicated the five scene-56 labelled utterances as `s055-d026`–`s055-d030`.

The correction is now durable:

- `scene-055.md` ends before `(முன்)`;
- `dialogues/records/scene-055.json` contains **25** records, `d001`–`d025`;
- `scene-056.md` is the sole owner of the flashback;
- `dialogues/records/scene-056.json` retains its **5** records;
- the corpus dialogue census is therefore **1,071**, not the historical provisional count 1,076;
- canonical page transcription was **not changed** by this derivative-boundary correction.

## Linkage and structure QA

PASS:

- all 58 English scene records exist;
- all source-labelled utterances in the corrected dialogue corpus are linked exactly once;
- no deleted T055 duplicate IDs are used as English source links;
- all 19 source-unlabelled spoken spans remain null-speaker/null-record rather than receiving inferred ownership;
- all 15 genuine physical-page crossings remain single English units with source provenance;
- exact source speaker labels remain metadata and are not normalized in English;
- embedded `சேரன் செங்குட்டுவன்`, `அகல்யா`, and `சாக்ரடீஸ்` dramatic identities remain distinct from outer-film characters;
- letters and terminal printed matter remain written text rather than dialogue;
- source-visible singing references remain performance cues and do not import absent lyrics.

## Song/performance QA

All four screenplay singing occurrences are represented:

1. `raja-rani-song-perf-001` — scene 4
2. `raja-rani-song-perf-002` — scene 16
3. `raja-rani-song-perf-003` — scene 40
4. `raja-rani-song-perf-004` — scene 58

The scene-58 association with numbered song 11 remains **review-level**, exactly as in the song inventory. Translation has not upgraded that linkage or any lyricist attribution.

The numbered-song authorship gate remains unchanged:

- later-anthology Kalaignar-attributed: **songs 3, 5, 6, 7, 8**;
- unresolved lyricist: **songs 1, 2, 4, 9, 10, 11**;
- original-booklet item-level lyricist credits: **0**.

## Source-review fidelity retained

The final English layer preserves the user's direct-scan source verdicts, including:

- PDF 27: `இரவெல்லாம்`;
- PDF 48: `வந்தனா`, `திடீர்னு`;
- PDF 57: `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`;
- PDF 74: the `K. N. சங்கரன் ...` impression is a non-canonical ownership/library stamp and is not screenplay text.

No English translation decision modifies canonical Tamil or supersedes those source verdicts.

## Disposition

**PASS — screenplay English translation is complete.**

The next separate production phase is the English translation of the **11 numbered front-matter song bodies** through a dedicated source-linked song translation layer. Translate the verified Tamil lyric bodies only; preserve page provenance, performance relationships and existing authorship tiers, and do not infer unresolved lyricists.
