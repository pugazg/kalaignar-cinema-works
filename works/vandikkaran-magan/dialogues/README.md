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

Each `records/scene-NNN.json` file follows derivative scene ordinal order while retaining the exact source scene ID separately. Speaker labels and dialogue text are source-preserving; alias resolution belongs only to the next character/entity layer.

See `../notes/dialogue-index-preflight.json`, `../notes/unlabelled-block-audit.json`, and `../notes/dialogue-index-qa.json`.

## Next

Begin character/entity indexing from the complete-verified immutable dialogue layer. Preserve all exact source speaker labels as immutable provenance; map label variants to character/entity IDs only in a separate interpretive alias layer; keep generic roles, voices, collectives and source abbreviations explicit; and run whole-work label/entity coverage QA before opening the song/performance authorship gate. Do not rewrite canonical Tamil, scenes, or dialogue records.
