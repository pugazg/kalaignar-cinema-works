# வண்டிக்காரன் மகன் — Scene-heading audit

**Controlling source:** `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`  
**Audit status:** **COMPLETE-VERIFIED — 72/72 source-visible scene-heading occurrences mapped**

## Audit rule

This inventory records each source-visible identifying scene label and its start page. It does **not** normalize the complete printed heading typography. Canonical transcription and scene derivatives preserve each occurrence's exact `காட்சி` wording, dash/spacing form, punctuation and adjacent location caption.

For screenplay PDF 6–87, **printed page = PDF page − 1**.

## Corrective findings

- First-pass review of PDF 83 exposed source-visible `காட்சி -- 53 டி`, increasing the earlier inventory to 71.
- Scene-derivative boundary QA then exposed one further stale inventory omission already present in the closed canonical source layer: PDF 10 contains source-visible `காட்சி — 4 எ.`. It is a genuine scene boundary and is retained as source scene ID `4-எ`.
- Therefore the authoritative inventory is **72 observed headings**, not 71. No canonical Tamil was changed by this correction; only structural inventory/derivative mirrors were reconciled.

| Occurrence | Source scene label | PDF start | Printed start |
|---:|---|---:|---:|
| 1 | `1` | 6 | 5 |
| 2 | `2` | 8 | 7 |
| 3 | `3` | 9 | 8 |
| 4 | `4` | 9 | 8 |
| 5 | `4-எ` | 10 | 9 |
| 6 | `5` | 12 | 11 |
| 7 | `6` | 13 | 12 |
| 8 | `7` | 13 | 12 |
| 9 | `8` | 16 | 15 |
| 10 | `9` | 17 | 16 |
| 11 | `10` | 18 | 17 |
| 12 | `10-எ` | 19 | 18 |
| 13 | `11` | 20 | 19 |
| 14 | `12` | 22 | 21 |
| 15 | `13` | 24 | 23 |
| 16 | `14` | 25 | 24 |
| 17 | `14-எ` | 27 | 26 |
| 18 | `15` | 28 | 27 |
| 19 | `16` | 29 | 28 |
| 20 | `16-எ` | 29 | 28 |
| 21 | `17` | 30 | 29 |
| 22 | `18` | 31 | 30 |
| 23 | `19` | 33 | 32 |
| 24 | `20` | 35 | 34 |
| 25 | `20-எ` | 37 | 36 |
| 26 | `21` | 39 | 38 |
| 27 | `22` | 40 | 39 |
| 28 | `22-எ` | 40 | 39 |
| 29 | `23` | 42 | 41 |
| 30 | `24` | 42 | 41 |
| 31 | `24-எ` | 44 | 43 |
| 32 | `24-பி` | 44 | 43 |
| 33 | `24-சி` | 46 | 45 |
| 34 | `24-டி` | 47 | 46 |
| 35 | `25` | 48 | 47 |
| 36 | `26` | 50 | 49 |
| 37 | `27` | 51 | 50 |
| 38 | `28` | 52 | 51 |
| 39 | `29` | 53 | 52 |
| 40 | `29-எ` | 55 | 54 |
| 41 | `30` | 55 | 54 |
| 42 | `31` | 55 | 54 |
| 43 | `32` | 56 | 55 |
| 44 | `33` | 58 | 57 |
| 45 | `33-எ` | 59 | 58 |
| 46 | `34` | 59 | 58 |
| 47 | `35` | 60 | 59 |
| 48 | `36` | 60 | 59 |
| 49 | `37` | 61 | 60 |
| 50 | `38` | 62 | 61 |
| 51 | `39` | 64 | 63 |
| 52 | `40` | 65 | 64 |
| 53 | `41` | 66 | 65 |
| 54 | `42` | 67 | 66 |
| 55 | `42-எ` | 68 | 67 |
| 56 | `43` | 70 | 69 |
| 57 | `44` | 71 | 70 |
| 58 | `45-46` | 71 | 70 |
| 59 | `47` | 72 | 71 |
| 60 | `48` | 72 | 71 |
| 61 | `49` | 75 | 74 |
| 62 | `50` | 76 | 75 |
| 63 | `51` | 76 | 75 |
| 64 | `52` | 78 | 77 |
| 65 | `53` | 81 | 80 |
| 66 | `53-எ` | 81 | 80 |
| 67 | `53-பி` | 81 | 80 |
| 68 | `53-சி` | 81 | 80 |
| 69 | `53-டி` | 83 | 82 |
| 70 | `54` | 85 | 84 |
| 71 | `55` | 86 | 85 |
| 72 | `56` | 87 | 86 |

## Sequence findings

- observed heading occurrences: **72**;
- unsuffixed/combined headings: **55**;
- suffix insertions: **17**;
- numerical range represented: **1–56**;
- combined source heading: **`45-46`**;
- suffix insertions: `4-எ`, `10-எ`, `14-எ`, `16-எ`, `20-எ`, `22-எ`, `24-எ`, `24-பி`, `24-சி`, `24-டி`, `29-எ`, `33-எ`, `42-எ`, `53-எ`, `53-பி`, `53-சி`, `53-டி`;
- repeated PDF start pages are source-supported: multiple numbered scenes begin on the same printed page;
- no synthetic scene 45 or scene 46 is created: the printed combined `45-46` remains one source disposition.

## Typography safeguards

Exact printed heading typography remains in canonical pages and scene derivatives. The structural ID list is navigation metadata only and is not permission to normalize dash form, spacing or punctuation.

An internal location caption does not automatically create a scene. PDF 22, for example, begins scene 12 and later contains `கோகிலா அறை` without a new `காட்சி` heading.

## Gate disposition

**PASS — 72/72 source-visible headings are mapped.** `scenes/index.json` and `notes/scene-boundary-ownership-qa.md` independently close the scene derivative gate with 72/72 derivatives, exact ordered-span reconstruction, and 0 gaps / 0 overlaps.
