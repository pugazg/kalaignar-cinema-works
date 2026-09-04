# மந்திரி குமாரி — source-linked bilingual reader/export

Status: **complete-verified — QA PASS**.

This directory is the deterministic bilingual reader composition for the verified Manthiri Kumari archive.

The booklet is not a screenplay. Navigation remains:

- **1** continuous `கதைச்சுருக்கம்` / story-summary record;
- **15** separately headed song/performance records.

The reader does not duplicate or normalize upstream translation records. `reader-edition.json` names the verified source-linked inputs; `reader-edition.html` renders those records directly.

## Files

- `build.py` — deterministic validator/composition builder;
- `PREFLIGHT_QA_REPORT.md` — input preflight;
- `reader-edition.json` — machine composition/index;
- `reader-edition.md` — human-readable source-order index;
- `reader-edition.html` — bilingual HTML renderer;
- `QA_REPORT.md` — whole-reader QA;
- `manifest.json` — integrity metadata.

## Checkpoint

- top-level source structures: **16/16**;
- story-summary logical units: **13**;
- performance records: **15/15**;
- performance sections: **52**;
- Tamil / English performance line-cues: **234 / 234**;
- mapping mismatches: **0**;
- synthetic scenes: **0**;
- item-level lyric authorship: **0 verified / 15 unresolved**;
- QA: **PASS**.

## Downstream Reading Room payload

The source-linked composition payload under `../../integrations/reading-room/` is now **payload-complete-verified — QA PASS**.

- payload: `../../integrations/reading-room/reading-room.json`;
- payload mode: `source-linked-composition`;
- source-link targets: **32**;
- payload bytes: **15,704**;
- SHA-256: `20a0db293b936757e7d01def336252f28543337f319dfae6ad7bf5ae886bab43`;
- site application: **not-applied**.

## Next activity / disposition

No required repository-internal reader/export or payload work remains. Site application may proceed only in the separate Reading Room implementation repository when explicitly authorized.
