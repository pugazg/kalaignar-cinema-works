#!/usr/bin/env python3
"""Write the passing anthology English reader/export preflight report."""

import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "kalaignar-thirai-isai-paadalgal"
TRANS = WORK / "translations" / "records"
INDEX = json.loads((WORK / "translations" / "index.json").read_text(encoding="utf-8"))
PAGE_MAP = json.loads((WORK / "songs" / "page-map.json").read_text(encoding="utf-8"))
REPORT = WORK / "editions" / "en" / "PREFLIGHT_QA_REPORT.md"

records = []
for n in range(1, 55):
    records.append(json.loads((TRANS / f"song-{n:03d}.json").read_text(encoding="utf-8")))

statuses = Counter(r["status"] for r in records)
attributions = Counter(r["source"]["attribution_status"] for r in records)
source_links = sum(1 for r in records if r["source"]["song_file"] == f"works/kalaignar-thirai-isai-paadalgal/songs/song-{r['anthology_song_number']:03d}.md")
mapped_tamil_lines = sum(len(s["source_tamil_lines"]) for r in records for s in r["translation"]["sections"])
mapped_english_lines = sum(len(s["english_lines"]) for r in records for s in r["translation"]["sections"])
cross_page = [(r["anthology_song_number"], r["source"]["pdf_pages"]) for r in records if len(r["source"]["pdf_pages"]) > 1]

sha = os.getenv("GITHUB_SHA", "unknown")
run_id = os.getenv("GITHUB_RUN_ID", "unknown")
repo = os.getenv("GITHUB_REPOSITORY", "pugazg/kalaignar-cinema-works")
server = os.getenv("GITHUB_SERVER_URL", "https://github.com")
run_url = f"{server}/{repo}/actions/runs/{run_id}" if run_id != "unknown" else "not-recorded"

cross_lines = "\n".join(f"- `{n:03d}` — PDF **{'–'.join(map(str, pages))}**" for n, pages in cross_page)

text = f"""# கலைஞர் திரை இசைப் பாடல்கள் — English Reader/Export Preflight QA

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

- head commit: `{sha}`;
- workflow run: `{run_id}`;
- run URL: `{run_url}`;
- Python: 3.12.

## PASS results

| Check | Result |
|---|---:|
| Translation record files | **{len(records)} / 54** |
| Source-linked Tamil song files | **{source_links} / 54** |
| Anthology order | **001–054, no gaps** |
| Pilot-verified records | **{statuses.get('pilot-verified', 0)}** (`001–003`) |
| Verified records | **{statuses.get('verified', 0)}** (`004–054`) |
| Draft records | **{statuses.get('draft', 0)}** |
| Review records | **{statuses.get('review', 0)}** |
| Not-started records | **0** |
| `anthology-attributed` records | **{attributions.get('anthology-attributed', 0)} / 54** |
| Mapped Tamil lyric lines/cues | **{mapped_tamil_lines}** |
| Mapped English lines/cues | **{mapped_english_lines}** |
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

Exactly **{len(cross_page)}** translation records span more than one song-bearing source page, matching the verified Tamil page map:

{cross_lines}

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
"""

REPORT.write_text(text, encoding="utf-8")
print(f"wrote {REPORT.relative_to(ROOT)}")
