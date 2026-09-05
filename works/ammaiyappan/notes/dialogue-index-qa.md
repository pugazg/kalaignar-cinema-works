# அம்மையப்பன் — dialogue-index QA

Status: **REVIEW REQUIRED**

- scene coverage: **63/63**
- explicit source speaker labels: **910/910 owned exactly once**
- immutable dialogue records: **1009**
- distinct exact speaker-label strings: **62**
- speaker-label distribution vs preflight: **PASS**
- reviewed dash false positives: **14/14 excluded as labels**
- reviewed page-boundary candidates: **19/19 preserved as same-utterance continuations**
- total multi-page dialogue records found by full state machine: **26**
- unlabelled continuation source lines owned by an active utterance: **374**
- ordinary source blocks with no active explicit speaker: **20 blocks / 35 lines**
- source scene numbers invented: **0**
- alias/name normalization: **0**

The immutable record build is structurally complete.  The character/entity gate stays **BLOCKED** until every unlabelled ordinary block is source-role reviewed; those blocks are deliberately not guessed into dialogue ownership.
