# வண்டிக்காரன் மகன் — immutable dialogue layer

**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**

Built from the closed 72/72 source-led scene derivatives without rewriting canonical Tamil or scene files. A late structural-collision audit corrected a parser defect that had treated some explicit speaker-labelled lines ending in parenthetical action as stage directions.

## Coverage

- immutable dialogue records: **773**;
- legacy IDs preserved: **744/744**; append-only repair records: **29**;
- exact source speaker labels: **38**;
- zero-dialogue scenes: **15**; cross-page records: **3**;
- delimiters: **`:—` 765 / `:` 8**;
- 31 structural collisions reviewed: **29 spoken records restored / 2 action-only labels excluded**;
- unlabelled text assigned to speakers: **0**; label normalizations: **0**.

See `../notes/dialogue-structural-collision-audit.json` and `../notes/dialogue-index-qa.json`.

## Downstream

Character/entity and song/performance layers are reconciled and closed against this 773-record authority. English translation is **72/72 COMPLETE-VERIFIED**; reader/export and Reading Room payload are **QA PASS**.

**Next:** No required repository-internal `வண்டிக்காரன் மகன்` production work remains. Keep canonical Tamil, scene, reconciled immutable dialogue, character/entity, song/performance, English translation, reader/export and Reading Room payload layers closed. Apply `works/vandikkaran-magan/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; fetch its live state first and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here.
