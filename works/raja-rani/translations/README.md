# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and verified Tamil numbered-song derivatives  
**Target language:** English (`en`)  
**Status:** **complete-verified — screenplay 58/58 + numbered songs 11/11**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering. The 11 numbered front-matter songs retain their actual source numbering and are translated separately under `songs/`.

## Final English coverage

### Screenplay

- verified scenes: **58/58**;
- verified screenplay units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- unit mix: **1,090 dialogue / 137 stage direction / 4 performance cue / 5 written text**;
- source-unlabelled spoken units: **19**;
- genuine cross-page English units: **15**;
- draft/review screenplay units: **0/0**.

Final screenplay QA: `FINAL_SCREENPLAY_TRANSLATION_QA.md`.

### Numbered front-matter songs

- numbered song bodies: **11/11 complete-verified**;
- translation sections / turn groups: **67**;
- Tamil source line/cue entries represented: **181**;
- English line/cue entries represented: **181**;
- multi-page song records: **4** — songs 2, 3, 8 and 10;
- draft/review/not-started song records: **0/0/0**.

Song translation index: `songs/index.json`.  
Final song QA: `songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md`.

## Files

- `schema.json` — scene-sharded screenplay translation schema.
- `index.json` — authoritative work-level English coverage/integrity checkpoint.
- `PILOT_REVIEW.md` and `BATCH_*_REVIEW.md` — historical screenplay translation checkpoints.
- `FINAL_SCREENPLAY_TRANSLATION_QA.md` — final screenplay linkage/count/boundary QA.
- `records/scene-001.json`–`records/scene-058.json` — verified English scene records.
- `songs/schema.json` — numbered-song English schema.
- `songs/records/song-001.json`–`song-011.json` — verified numbered-song translations.
- `songs/index.json` — numbered-song coverage/authorship/performance-link integrity state.
- `songs/FINAL_NUMBERED_SONG_TRANSLATION_QA.md` — final numbered-song QA PASS.

Historical batch reviews retain the state that was true when each batch ran; they are not current status mirrors.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker/turn labels remain metadata.** Variants such as `ராஜா` / `ராசா`, source-exact `தர்யம்`, voice labels, personified roles and song turn labels are not normalized upstream.
3. **Source-unlabelled speech remains unlabelled.** Null speaker/source-record fields are deliberate when the source prints no label.
4. **Stage directions stay source-bounded.** No invented action, motivation, identity or scene closure.
5. **Rhetoric and colloquial force survive.** Repetition, hesitation, insults, satire, comic timing, imagery and code-switching remain visible where possible.
6. **Cross-page source units remain one English unit/record.** Physical provenance is retained.
7. **Complete lyric bodies and cue-only performances remain distinct.** Missing lyrics are never imported into screenplay cues.
8. **Authorship status is independent of translation status.** Translation does not promote evidence tiers.
9. **Decorative separators remain structural.** They do not become invented prose.
10. **Written material remains written text.** Letters and terminal printed matter are not converted to dialogue.
11. **Embedded dramas remain structurally distinct.** `சேரன் செங்குட்டுவன்`, `அகல்யா`, and `சாக்ரடீஸ்` identities are not collapsed into outer-film characters.
12. **Opaque verified Tamil is not silently repaired through English.** Conservative transliteration/notes are preferred where a clean English rendering would imply an unrecorded Tamil emendation.

## Final source/derivative census

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- scene derivatives: **58/58 verified / 0 blocked**;
- unique immutable dialogue records: **1,071**;
- exact source speaker labels: **80/80**;
- verified entities / roles / collectives: **44**;
- numbered Tamil song derivatives: **11/11**;
- screenplay singing references: **4**.

### T055 / T056 derivative-boundary correction

Final screenplay QA found that an earlier scene-55 derivative had duplicated the `(முன்)` flashback owned by scene 56. The duplicate derivative ownership was removed:

- scene 55 dialogue records: **25**;
- scene 56 dialogue records: **5**;
- corrected unique dialogue corpus: **1,071**;
- canonical page transcription: **unchanged**.

Deleted duplicate `s055-d026`–`s055-d030` IDs must not be restored.

## Song authorship/performance integrity

Later-anthology Kalaignar-attributed numbered songs remain exactly **3, 5, 6, 7, 8**. Songs **1, 2, 4, 9, 10, 11** remain unresolved. Original-booklet item-level lyricist credits remain **0**.

Verified screenplay links remain song 3/scene 4, song 5/scene 16, song 8/scene 40. The song 11/scene 58 relation remains **review-level** only.

## Next activity

The English textual translation phase is complete. Build and QA a deterministic whole-work bilingual reader/export from the verified screenplay and numbered-song records, then prepare source-linked Reading Room integration data for `https://nenjukkuneethi.org/read`. Do not create another standalone PDF/EPUB by default.
