# அம்மையப்பன் — immutable dialogue layer

Status: **COMPLETE — FINAL QA PASS**

Authority: the **63/63 complete-verified archive-only scene derivatives**, themselves derived only after the **105/105 dual-gate Tamil source verification** closed.

## Current build

- archive scenes represented: **63/63**
- explicit immutable colon-labelled records: **1009**
- source-role-resolved dialogue supplements: **15**
- downstream dialogue units: **1024**
- distinct exact speaker-label strings: **62**
- multi-page immutable utterances: **26**
- zero-dialogue scene files retained as empty arrays: **3**
- source scene numbers invented: **0**
- alias/name normalization: **0**

Each explicit source `speaker : text` line starts one record.  Ordinary unlabelled text that follows remains part of that utterance until a hard structural boundary.  A physical PDF-page transition does not end an utterance; multi-page records carry `page_segments` and page provenance.

Text that occurs with no active explicit speaker was first preserved separately in `../notes/unlabelled-block-audit.json`. The complete 20/20 source-role review is recorded in `../notes/unlabelled-source-role-review.json`. Fifteen source-supported dialogue supplements are kept in `source-role-resolved-records.json`; six non-dialogue source units are documented in `../notes/non-dialogue-source-role-exclusions.json`. The exact source form `திரு; ...` is retained with `;` as its recorded delimiter.

Final dialogue QA is **PASS** in `../notes/dialogue-final-qa.json`. The character/entity index gate is **UNLOCKED**.
