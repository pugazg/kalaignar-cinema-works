# கலைஞர் திரை இசைப் பாடல்கள் — English Reader/Export Preflight QA

Status: **PASS**

This report records the whole-corpus integrity gate run after completion of the source-linked English song translation and before generation of publication-facing reader/export derivatives.

## Authority and scope

The preflight reads the repository's verified derivative layers directly:

- `translations/records/song-001.json` through `song-054.json`;
- `translations/index.json`;
- `songs/page-map.json`;
- immutable verified Tamil song files `songs/song-001.md` through `song-054.md`.

The audit does **not** alter the complete-verified Tamil song corpus or the complete-verified English source-linked translation records.

## Automated run

GitHub Actions workflow: `.github/workflows/kalaignar-song-anthology-english-preflight.yml`  
Preflight implementation: `works/kalaignar-thirai-isai-paadalgal/editions/en/audit_probe.py`

Passing run:

- head commit: `e4ba3bda354863321bedf224b32675d9a9d29f7a`;
- workflow run: `33307109342`;
- run URL: `https://github.com/pugazg/kalaignar-cinema-works/actions/runs/33307109342`;
- Python: 3.12.

## PASS results

| Check | Result |
|---|---:|
| Translation record files | **54 / 54** |
| Source-linked Tamil song files | **54 / 54** |
| Anthology order | **001–054, no gaps** |
| Pilot-verified records | **3** (`001–003`) |
| Verified records | **51** (`004–054`) |
| Draft records | **0** |
| Review records | **0** |
| Not-started records | **0** |
| `anthology-attributed` records | **54 / 54** |
| Mapped Tamil lyric lines/cues | **1105** |
| Mapped English lines/cues | **1105** |
| Tamil/English line-count mismatches | **0** |
| Duplicate anthology song numbers | **0** |
| Duplicate translation IDs | **0** |
| Duplicate song IDs | **0** |
| Duplicate record paths | **0** |
| Source-page mismatches vs `songs/page-map.json` | **0** |
| Tamil-title mismatches vs verified song files | **0** |
| Film-title mismatches vs verified song files | **0** |
| Attribution drift | **0** |
| Translation-mode drift | **0** |
| Audit warnings | **0** |
| Audit errors | **0** |

## Cross-page provenance integrity

Exactly **8** translation records span more than one song-bearing source page, matching the verified Tamil page map:

- `009` — PDF **38–39**
- `019` — PDF **53–54**
- `023` — PDF **58–59**
- `024` — PDF **62–63**
- `036` — PDF **86–87**
- `037` — PDF **90–91**
- `051` — PDF **121–122**
- `052` — PDF **123–124**

Each remains one translation record with its complete source-page array in source order.

## Status distinction safeguard

The preflight preserves the repository's deliberate status distinction:

- `001–003` remain **`pilot-verified`** because they established the translation voice baseline;
- `004–054` remain **`verified`**;
- both groups are included in the corpus-level **`complete-verified`** status without rewriting item-level status history.

## Attribution safeguard

All 54 records remain **`anthology-attributed`**. Reader/export readiness does not promote the 2024 anthology's attribution into original-film `primary-source-verified` authorship.

## Kalaignar-language safeguard

The preflight treats the completed `semantic-poetic-source-faithful` records as immutable reader input. It does not smooth, paraphrase, modernize or replace difficult source-shaped English merely for publication fluency. The translation-layer decisions documented in `PILOT_REVIEW.md` and the seven scaled batch reviews remain controlling.

## Gate disposition

**Reader/export preflight: PASS.**

The 54-song English translation layer is cleared for deterministic reader/export generation. The next activity may create publication-facing Markdown, standalone HTML and machine-readable JSON from the verified records, then run generated-output QA and an integrity manifest before any downstream Reading Room integration.
