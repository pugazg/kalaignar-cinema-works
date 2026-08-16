# Manohara English Reader Edition — Whole-work QA

**Status:** PASS  
**English authority:** `works/manohara/translations/records/`  
**Source scan SHA-256:** `87518fd8c290d7880aa2ddd9f2b5999c9d421d48fe1f02d61cf8e254393236a9`

## Verified checks

- archival navigation scenes: **57/57** in source order; the booklet itself prints no scene numbers;
- English units: **1,190/1,190 unique, sequential and verified**;
- status counts: **1,190 verified / 0 review / 0 draft**;
- kind counts: **1,009 dialogue / 173 stage direction / 6 song-reference / 1 chant / 1 written-text**;
- immutable labelled dialogue records linked exactly once: **983/983**;
- source-visible unlabelled spoken units retained without invented speakers/dialogue IDs: **27**;
- song/performance occurrence links cross-checked exactly once: **6/6**;
- cross-page English units: **17**, exactly matching `translations/index.json`;
- all provenance lies inside PDF **7–88** / printed **6–87**, with `printed = PDF - 1`;
- source-only decorative stars do not survive as synthetic `(Scene ends.)` units;
- reader Markdown, standalone HTML and machine-readable JSON each contain every verified English unit exactly once;
- exact Tamil `speaker_label` values remain presentation labels only for source-labelled speech;
- no editorial placeholder token appears in reader text.

## Source-sensitive safeguards retained

Scene numbering is explicitly labelled archival rather than source numbering. Scene 11 retains its source-labelled war proclamation as a `chant` while preserving the immutable dialogue-source link. Scene 55 retains all four genuine page crossings. Scene 56 keeps four source-empty speaker lines unlabelled. Scene 57 keeps the unlabelled `Padma! Queen of my heart...` continuation inside the preceding king's source-linked unit. All six song/performance references remain limited to what the booklet prints; no absent lyric is reconstructed.

The generator writes only inside `works/manohara/editions/en/` and does not modify canonical Tamil or structured source layers.
