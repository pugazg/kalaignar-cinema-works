# வண்டிக்காரன் மகன் — dialogue-index preflight

Status: **REVIEW COMPLETE / DIALOGUE GATE CLOSED**

This preflight inventories source-explicit dialogue syntax from the closed canonical screenplay/72-scene layer. Its review is now closed; the resulting immutable dialogue layer contains 744 complete-verified records. Exact source labels were not normalized.

## Coverage

- verified scenes scanned: **72/72**
- explicit labelled dialogue candidates: **744**
- distinct exact speaker labels: **38**
- zero-explicit-dialogue scenes: **15**
- anomalous non-colon delimiter candidates: **16**
- candidate cross-page utterances: **3**
- unlabelled ordinary blocks retained for review: **148**

## Delimiter distribution

- `:` — **8**
- `:—` — **736**

## Exact speaker-label inventory

| Exact label | Candidates |
|---|---:|
| `விங்கன்` | 159 |
| `ஜமீன்தார்` | 127 |
| `உமா` | 96 |
| `கோகிலா` | 64 |
| `மரகதம்` | 62 |
| `காளிங்` | 45 |
| `சடையன்` | 42 |
| `லிங்கன்` | 23 |
| `காளிங்க` | 18 |
| `புலவர்` | 15 |
| `கண்ணாயிரம்` | 11 |
| `டேவிட்` | 10 |
| `சொக்க` | 9 |
| `சொர்ணம்` | 9 |
| `சொக்` | 6 |
| `மக்கள்` | 6 |
| `லீனா` | 6 |
| `ஒருவன்` | 5 |
| `ஜம்பு` | 5 |
| `கடைக்` | 3 |
| `ஆட்கள்` | 2 |
| `காவலன்` | 2 |
| `சிறுமி` | 2 |
| `தரகர்` | 2 |
| `விங்கன் குரல்` | 2 |
| `இன்னொருவன்` | 1 |
| `ஊர்ப்பெரியவர்` | 1 |
| `எல்லோரும்` | 1 |
| `ஒரு சிறுமி` | 1 |
| `ஒருத்தி` | 1 |
| `ஒருவர்` | 1 |
| `கண்ணாயிரத்தின் குரல்` | 1 |
| `சடையன் குரல்` | 1 |
| `ஜமீன்` | 1 |
| `புரோகிதர்` | 1 |
| `பெண்` | 1 |
| `மற்றொரு சிறுவன்` | 1 |
| `முனியன்` | 1 |

## Zero-dialogue scenes

`2`, `3`, `10`, `14-எ`, `16`, `22`, `24-சி`, `31`, `33-எ`, `36`, `53`, `53-எ`, `53-பி`, `53-சி`, `56`

## Anomalous delimiter candidates

- scene `10` PDF 18: `உருட்டல்; மிரட்டல்;`
- scene `20` PDF 36: `பழுக்கப் பழுக்க-ரசம்`
- scene `20` PDF 36: `பிழியப் பிழியப்-பழம்`
- scene `24-சி` PDF 46: `கங்குலில் எங்கும் பனிமூட்டம் — உடல்`
- scene `24-சி` PDF 46: `படுத்தாள்; புரண்டாள்;`
- scene `24-சி` PDF 46: `வந்தான்; சேர்ந்தேன்`
- scene `24-சி` PDF 46: `மின்னும் — பொன்`
- scene `24-சி` PDF 47: `மெத்தை — தத்தும்`
- scene `24-சி` PDF 47: `தத்தை; தன்`
- scene `24-சி` PDF 47: `சந்தம் — தன்`
- scene `24-சி` PDF 47: `என்று—தன்`
- scene `36` PDF 60: `காட்டுவேன்; பாருங்களே!`
- scene `36` PDF 60: `மேய்ப்பவன் என்று — எண்ணியிருக்கும்`
- scene `48` PDF 73: `ஊரைத் திருத்த - ஒரு`
- scene `48` PDF 73: `பேரை நிறுத்த - இரு`
- scene `48` PDF 73: `கிளிப்புள்ளே; கிரிப்புள்ளே;`

## Cross-page continuation candidates

- scene `25` `சடையன்` — PDF 48→49 / delimiter `:—`
- scene `42-எ` `சடையன்` — PDF 68→69 / delimiter `:—`
- scene `54` `விங்கன்` — PDF 85→86 / delimiter `:—`

## Review disposition

- explicit labelled candidates accepted: **744/744**;
- exact source speaker labels retained without normalization: **38/38**;
- anomalous non-colon candidates reviewed: **16/16** — all are source-visible punctuation/verse fragments and **0** were promoted to dialogue;
- direct-scan anomaly review pages: **PDF 18, 36, 46–47, 60, 73**;
- cross-page candidates reviewed: **3/3** — source scenes `25` (PDF 48→49), `42-எ` (PDF 68→69), and `54` (PDF 85→86) each remain one immutable record with page segments;
- preflight unlabelled ordinary blocks: **148** — all remain governed by the no-inference rule; source-unlabelled blocks assigned a speaker: **0**;
- duplicate dialogue IDs / speaker-label normalizations: **0 / 0**.

**PASS — preflight review is closed. `dialogues/` is COMPLETE-VERIFIED / QA PASS; character/entity indexing is READY-NEXT.**
