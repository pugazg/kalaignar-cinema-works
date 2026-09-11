# Maruthanattu Ilavarasi Reading Room payload — QA report

Status: **PASS**

## Input authority

- reader manifest status: **PASS**
- authoritative inputs: **12** — reader JSON + reader manifest + 10 verified Tamil scene derivatives
- input aggregate SHA-256: `d8ddd19c06550006db5f88b8f82432f254bac95bef9a14c13ca4315618cfec9f`
- upstream source scan SHA-256: `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f`

## Payload checkpoint

- source-structure units: **10/10**
- unnumbered opening: **1/1**
- source-numbered scenes: **2–10 / 9 scenes**
- English units: **228/228**
- immutable dialogue links: **208/208 exactly once**
- non-dialogue source-linked units: **20/20**
- cross-page units: **5/5**
- retained performance records: **0/0**

## Semantic safeguards

- unnumbered opening remains unnumbered: **PASS**
- scene numbers 2–10 remain actual source scene numbers: **PASS**
- synthetic Scene 1: **0**
- Tamil/English/parallel switching is presentation-only metadata: **PASS**
- exact Tamil speaker labels and delimiters retained: **PASS**
- Tamil scene text loaded from verified scene derivatives: **10/10**
- page/source provenance retained: **PASS**
- Phase 8 zero-item performance state unchanged: **PASS**
- placeholder leakage: **0**
- site application status: **not-applied**

## Output integrity

- `reading-room.json` bytes: **236,481**
- `reading-room.json` SHA-256: `25715b161b9df7e47d158871aab56f479be226d7bde624e45e5c3f50724acbb2`

The payload is ready for the separate Reading Room implementation repository when that repository is explicitly authorized for modification. This step does not deploy or modify the public site.
