# வண்டிக்காரன் மகன் — immutable dialogue layer

**Status:** **COMPLETE-VERIFIED / QA PASS**

Built only from the closed 72/72 source-led scene derivatives. Canonical Tamil and scene files are upstream authority and are not rewritten here.

## Coverage

- scene inputs: **72/72**
- immutable dialogue records: **744**
- exact source speaker labels: **38**
- zero-dialogue scenes: **15**
- cross-page dialogue records: **3**
- delimiters: **`:—` 736 / `:` 8**
- unlabelled text assigned to speakers: **0**
- reviewed anomalous non-colon candidates promoted to dialogue: **0/16**

Each `records/scene-NNN.json` file follows derivative scene ordinal order while retaining the exact source scene ID separately. Speaker labels and dialogue text remain source-preserving. The downstream character/entity layer is now complete-verified and keeps alias resolution separate from these immutable records.

See `../notes/dialogue-index-preflight.json`, `../notes/unlabelled-block-audit.json`, and `../notes/dialogue-index-qa.json`.

## Downstream

Character/entity indexing is **COMPLETE-VERIFIED — 32 entities / 38/38 labels / 744/744 dialogue records / QA PASS**. Song/performance authorship is **READY-NEXT**.

Begin the song/performance authorship gate from the closed source, scene, dialogue and character/entity layers. Inventory source-visible song, verse and performance occurrences first; preserve exact source wording, lineation, cues and provenance; do not infer item-level lyric authorship from the film-level `பாடல்கள்: கவிஞர் வாலி` credit alone; assign authorship only where item-level evidence supports it; run whole-work occurrence/authorship coverage QA before English translation. Do not rewrite canonical Tamil, scenes, immutable dialogue records or character/entity mappings.
