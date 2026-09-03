# Raja Rani Reading Room payload — QA report

Status: **PASS**

## Input authority

- reader manifest status: **PASS**
- reader input files: **2** (`reader-edition.json`, `manifest.json`)
- reader-input aggregate SHA-256: `40bb6c42dfda5049a4e030ca5ace5536e1ea54e14ac91c4ff41cbb455ab18078`
- upstream source scan SHA-256: `26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4`

## Payload checkpoint

- numbered source songs: **11/11**
- numbered-song sections: **67/67**
- Tamil/English song line-cues: **181/181**
- archival screenplay scenes: **58/58**
- screenplay English units: **1,236/1,236**
- immutable dialogue links: **1,071/1,071**
- source-unlabelled spoken units: **19/19**
- cross-page screenplay units: **15/15**
- screenplay performance occurrence links: **4/4**
- song authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**
- song-performance relations: **3 verified / 1 review**

## Semantic safeguards

- source-numbered songs remain songs 1–11: **PASS**
- screenplay scene ordinals are explicitly archival/editorial navigation only: **PASS**
- Tamil/English switching is presentation-only metadata: **PASS**
- page/source provenance retained: **PASS**
- deleted T055 duplicate dialogue IDs absent: **PASS**
- scene-58/song-11 relation remains review-level: **PASS**
- authorship tiers are not upgraded: **PASS**
- placeholder leakage: **0**
- site application status: **not-applied**

## Output integrity

- `reading-room.json` bytes: **974,510**
- `reading-room.json` SHA-256: `ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b`

The payload is ready for use by the separate Reading Room implementation repository when that repository is explicitly authorized for modification. This repository-only step does not deploy or change the public site.
