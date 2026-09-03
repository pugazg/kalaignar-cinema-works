# Raja Rani bilingual reader/export — preflight QA

Status: **PASS**

This preflight validates the complete-verified Raja Rani bilingual input corpus before generated reader files are built.

## Screenplay input

- archival navigation scenes: **58/58**
- source-numbered screenplay scenes: **none**
- verified English units: **1,236/1,236**
- immutable dialogue links: **1,071/1,071**
- source-unlabelled spoken units: **19/19**
- cross-page English units: **15/15**
- source-visible performance occurrence links: **4/4**
- unit kinds: `{'stage-direction': 137, 'dialogue': 1090, 'performance-cue': 4, 'written-text': 5}`

## Numbered-song input

- actual source-numbered front-matter songs: **11/11**
- translation sections: **67/67**
- Tamil/English line-cue mappings: **181/181**
- cross-page song records: **4/4**
- authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**
- performance-link disposition: **3 verified / 1 review**

## Integrity gates

- all 58 verified Tamil scene derivatives present: **PASS**
- all 58 verified English scene records present and ordered: **PASS**
- all 1,071 immutable dialogue IDs linked exactly once: **PASS**
- deleted T055 duplicate IDs absent from source and English linkage: **PASS**
- source-unlabelled speech retains null speaker metadata: **PASS**
- page provenance/order checks: **PASS**
- all 11 verified Tamil/English numbered-song records present: **PASS**
- every mapped Tamil song line/cue exists in its verified Tamil derivative: **PASS**
- song authorship tiers unchanged: **PASS**
- scene-58/song-11 relationship remains review-level: **PASS**
- songs are not assigned synthetic screenplay scene IDs: **PASS**
- placeholders / synthetic scene-end prose: **0**

## Reproducibility checkpoint

- authoritative input files: **200**
- authoritative-input aggregate SHA-256: `35cfc21e70eed9e0fb820c3df6a6a1c41fbddc21594f78b0cb5a799ab6a7efc2`
- source scan SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`

The reader builder may proceed from this checkpoint. Reader generation is downstream only and must not rewrite canonical Tamil, dialogue records, character mappings, song authorship or verified translations.
