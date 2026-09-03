# ராஜா ராணி — English translation layer

**Canonical authority:** verified Tamil scene derivatives, immutable dialogue records, and the separately verified song/performance layer  
**Target language:** English (`en`)  
**Status:** **screenplay complete-verified — 58 / 58 scenes; 1,236 verified units**

This directory contains the source-linked English derivative of `ராஜா ராணி`. Nothing here repairs, modernizes, expands or overwrites the Tamil source layers.

The booklet prints **no numbered screenplay scenes**. Translation IDs such as `raja-rani-en-s001-u001` use the archive's derivative navigation segmentation only and must never be presented as source scene numbering.

All **58 archival screenplay scenes** are source-verified and translated. There are **0 source-blocked scenes**. Final screenplay QA: `FINAL_SCREENPLAY_TRANSLATION_QA.md`.

## Files

- `schema.json` — scene-sharded source-linked translation schema.
- `index.json` — authoritative translation coverage and integrity checkpoint.
- `PILOT_REVIEW.md` — scene-1 fidelity/voice review and scaling rules.
- `BATCH_002_005_REVIEW.md` — scenes 2–5.
- `BATCH_006_010_REVIEW.md` — scenes 6–10.
- `BATCH_014_018_REVIEW.md` — scenes 14–18.
- `BATCH_019_023_REVIEW.md` — scenes 19–23.
- `BATCH_024_034_REVIEW.md` — historical 10-scene batch: scenes 24–32 and 34; s033 was still blocked at that time.
- `BATCH_011_040_REVIEW.md` — later 10-scene iteration: s011–s013, s033, s035–s040 after final source unblocking.
- `BATCH_041_058_REVIEW.md` — final all-remaining-scenes pass.
- `FINAL_SCREENPLAY_TRANSLATION_QA.md` — final screenplay linkage/count/boundary QA.
- `records/scene-001.json`–`records/scene-058.json` — verified English scene records.

The 11 numbered front-matter song bodies remain source structures outside the screenplay scene segmentation. They are the **only remaining English translation phase** and must be translated through a dedicated song-linked layer rather than invented scene IDs.

## Translation principles

1. **Verified Tamil remains authoritative.** English fluency is never evidence for changing a Tamil reading.
2. **Exact source speaker labels remain metadata.** Variants such as `ராஜா` / `ராசா`, `தாயம்` / source-exact `தர்யம்`, voice labels and personified roles are not normalized in translation metadata.
3. **Source-unlabelled speech remains unlabelled.** Null `speaker_label` and null `source_record_id` are deliberate when the source prints no label.
4. **Stage directions stay source-bounded.** Do not add action, motivation, identity or scene closure not printed in the verified derivative.
5. **Rhetoric and colloquial force survive.** Repetition, hesitation, insults, rhetorical questions, comic timing and code-switching remain visible where possible.
6. **Cross-page source units remain one English unit.** Provenance and `english_page_segments` preserve physical source crossings.
7. **Songs are distinct translation units.** Complete lyric bodies use semantic-poetic translation; cue-only occurrences never receive absent lyrics.
8. **Authorship status is not translation content.** The five later-anthology Kalaignar attributions remain evidence metadata only; six numbered-song lyricists remain unresolved.
9. **Decorative separators remain structural.** They do not become invented prose.
10. **Written material remains written text.** Letters and terminal printed matter are not converted to dialogue.
11. **Embedded dramas remain structurally distinct.** `சேரன் செங்குட்டுவன்`, `அகல்யா`, and `சாக்ரடீஸ்` identities are not collapsed into outer-film characters.
12. **Source uncertainty is never reconstructed through English.** The former review pages are resolved, but this remains a permanent rule.

## Final source-review resolution

The user's direct PDF review resolved every bounded source limitation:

- PDF 27: **`இரவெல்லாம்`**;
- PDF 48: **`வந்தனா`**, **`திடீர்னு`**;
- PDF 57: **`முன்னுக்கு பின் முரணாயிகிட்டே போவது?`**;
- PDF 74: `K. N. சங்கரன் ...` is a non-canonical ownership/library stamp; screenplay runs directly `ஞான: நீ விதவை.` → `ராஜா: விதவை.` → `சாந்: வித்தாரக்கள்ளி! விநாசகாரி`.

Current source derivative census after final QA is **58/58 verified scenes, 1,071 unique immutable dialogue records, 80/80 exact source labels, and 44 verified entities/roles/collectives**.

## T055 / T056 derivative-boundary correction

Final translation QA found that the earlier scene-55 derivative had duplicated the entire `(முன்)` flashback owned by scene 56. That duplicate was removed before final completion:

- scene 55 dialogue records: **25**;
- scene 56 dialogue records: **5**;
- corrected unique dialogue corpus: **1,071**;
- canonical page transcription: **unchanged**.

This is a derivative ownership correction, not a Tamil-text correction.

## Final screenplay English state

- verified scenes translated: **58/58**;
- verified English units: **1,236**;
- immutable dialogue links: **1,071/1,071**;
- unit mix: **1,090 dialogue / 137 stage direction / 4 performance cue / 5 written text**;
- source-unlabelled spoken units: **19**;
- genuine cross-page English units: **15**;
- screenplay singing/performance occurrences represented: **4/4**;
- draft units: **0**;
- review units: **0**.

The 1,090 dialogue-kind units consist of 1,071 immutable source-labelled records plus 19 deliberately unlabelled source-spoken units.

## Numbered-song English phase — next activity

Front-matter numbered song translations remain **0/11**.

Translate songs **1–11 in source order** through a dedicated source-linked song translation layer. For every song:

- use the verified Tamil song derivative as text authority;
- preserve its source page provenance;
- preserve existing screenplay performance links only where the song inventory already supports them;
- use semantic-poetic English while keeping source meaning and imagery;
- do not silently normalize the Tamil lyric body;
- do not infer a lyricist from style, context or translation;
- preserve authorship disposition exactly: songs **3, 5, 6, 7, 8** later-anthology Kalaignar-attributed; songs **1, 2, 4, 9, 10, 11** unresolved.

The screenplay translation is closed. Numbered-song translation is a separate phase.
