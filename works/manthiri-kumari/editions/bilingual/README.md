# மந்திரி குமாரி — source-linked bilingual reader/export

Status: **complete-verified — QA PASS**.

This directory is the deterministic bilingual reader composition for the verified Manthiri Kumari archive.

The booklet is not a screenplay. Navigation therefore remains:

- **1** continuous `கதைச்சுருக்கம்` / story-summary record;
- **15** separately headed song/performance records.

The reader does not duplicate or normalize the upstream translation records. `reader-edition.json` names the verified source-linked inputs; `reader-edition.html` renders those records directly. This keeps the generated layer small while preserving one textual authority chain.

## Files

- `build.py` — deterministic validator/composition builder;
- `PREFLIGHT_QA_REPORT.md` — input preflight;
- `reader-edition.json` — machine composition/index;
- `reader-edition.md` — human-readable reader index;
- `reader-edition.html` — bilingual HTML renderer backed by the composition index;
- `QA_REPORT.md` — whole-reader QA;
- `manifest.json` — input Git-blob identities and output SHA-256 hashes.

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

## Next activity

Prepare and QA the **Reading Room integration payload** from this complete-verified bilingual reader while preserving story-summary + performance navigation and the unresolved item-level lyric-authorship state.
