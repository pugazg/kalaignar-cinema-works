#!/usr/bin/env python3
"""Synchronize Naam canonical first-pass checkpoint through PDF 44."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 45–49, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. PDF 49 opens the already mapped "
    "scene-31 lyrical block; preserve only the booklet witness and do not infer missing lyrics or "
    "authorship. Keep all first-pass pages draft/needs-review until the later separate visual-fidelity "
    "and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-040-044.md",
    ROOT / "works/naam/notes/textual-notes-pdf-040-044.md",
    ROOT / "works/naam/metadata.yaml",
    ROOT / "works/naam/README.md",
    ROOT / "works/naam/transcription/README.md",
    ROOT / "works/naam/notes/historical-glyph-audit.md",
    ROOT / "works/naam/PROJECT_HANDOVER.md",
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md",
    ROOT / "README.md",
    ROOT / "data/works.json",
    ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
    ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")

idx_path = ROOT / "works/naam/transcription/index.json"
index = json.loads(idx_path.read_text(encoding="utf-8"))
checks = {
    "status": "partial-first-pass",
    "first_pass_pages_completed": 40,
    "current_through_pdf": 44,
    "historical_glyph_checked_pages": 40,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [45, 49]:
    raise SystemExit("Naam next batch must be PDF 45-49")

batch_path = ROOT / "works/naam/transcription/parts/pdf-040-044.md"
batch = batch_path.read_text(encoding="utf-8")
for needle in [
    "## காட்சி 25.",
    "## காட்சி 26",
    "## காட்சி 27",
    "கோவேரிக் கழுதைக்கு",
    "ஆவேஷ மூச்சால்",
    "மண்ணைவாரிப்",
    "மண்டேகங்கள்",
    "மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 40-44 source decision missing: {needle}")

changed: list[str] = []

def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new)

# Work metadata.
path = ROOT / "works/naam/metadata.yaml"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("first_pass_pages_completed: 35", "first_pass_pages_completed: 40"),
    ('first_pass_pdf_range_completed: "5-39"', 'first_pass_pdf_range_completed: "5-44"'),
    ("first_pass_current_through_pdf: 39", "first_pass_current_through_pdf: 44"),
    ("first_pass_current_through_printed_page: 39", "first_pass_current_through_printed_page: 44"),
    ("draft_pages: 35", "draft_pages: 40"),
    ("review_pages: 35", "review_pages: 40"),
    ('current_batch_path: "transcription/parts/pdf-035-039.md"', 'current_batch_path: "transcription/parts/pdf-040-044.md"'),
    ('current_textual_notes_path: "notes/textual-notes-pdf-035-039.md"', 'current_textual_notes_path: "notes/textual-notes-pdf-040-044.md"'),
    ("pages_checked: 35", "pages_checked: 40"),
    ("canonical_tamil_transcription: partial-first-pass-through-pdf-039", "canonical_tamil_transcription: partial-first-pass-through-pdf-044"),
    ("historical_glyph_audit: partial-first-pass-through-pdf-029", "historical_glyph_audit: partial-first-pass-through-pdf-044"),
]:
    text = replace(text, old, new)
needle = '    - "transcription/parts/pdf-035-039.md"\n'
if '    - "transcription/parts/pdf-040-044.md"' not in text:
    text = text.replace(needle, needle + '    - "transcription/parts/pdf-040-044.md"\n', 1)
if "batch_040_044_consequential_decodings" not in text:
    marker = "mapped_source_visible_performance_structures:\n"
    extra = '''  batch_040_044_consequential_decodings:\n    - pdf_page: 40\n      source_supported_unicode: "உன்னை"\n      family: "னை"\n    - pdf_page: 42\n      source_supported_unicode: "மண்ணைவாரிப்"\n      family: "ணை"\n    - pdf_page: 43\n      source_supported_unicode: "குமரனை"\n      family: "னை"\n\n'''
    text = text.replace(marker, extra + marker, 1)
if "pdf_40_44_new_performance_structures" not in text:
    text = text.replace("  pdf_35_39_new_performance_structures: 1\n", "  pdf_35_39_new_performance_structures: 1\n  pdf_40_44_new_performance_structures: 0\n", 1)
text = re.sub(r'next_action: ".*?"\s*$', f'next_action: "{NEXT}"', text, count=1, flags=re.S)
write_if_changed(path, text)

# Work README.
path = ROOT / "works/naam/README.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–39 / 35 of 67 pages", "PDF 5–44 / 40 of 67 pages"),
    ("35 pages checked / 0 final-verified", "40 pages checked / 0 final-verified"),
    ("`transcription/parts/pdf-035-039.md`  ", "`transcription/parts/pdf-035-039.md`, `transcription/parts/pdf-040-044.md`  "),
    ("Current textual notes: `notes/textual-notes-pdf-035-039.md`", "Current textual notes: `notes/textual-notes-pdf-040-044.md`"),
    ("PDF **5–39** has now been transcribed as source-order draft material in seven five-page batches. The newest batch continues `காட்சி 14`, contains `காட்சி 15–19`, and opens `காட்சி 20`.", "PDF **5–44** has now been transcribed as source-order draft material in eight five-page batches. The newest batch continues `காட்சி-24.`, contains `காட்சி 25–27`, and ends within `காட்சி 27`."),
    ("PDF 10–39 adds **0** new uncertainty markers", "PDF 10–44 adds **0** new uncertainty markers"),
    ("**0** of the thirty-five first-pass pages are called verified yet.", "**0** of the forty first-pass pages are called verified yet."),
]:
    text = replace(text, old, new)
marker = "- PDF 35 `நானம்மா` is checked historical `னா`; PDF 37 `உன்னை` is checked historical `னை`; PDF 39 `எமனோடு` is checked historical `னோ`;\n"
if "PDF 42 `மண்ணைவாரிப்`" not in text:
    addition = (
        "- PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`; PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`;\n"
        "- PDF 40–44 retains source-period/colloquial forms including `கோவேரிக் கழுதைக்கு`, `ஆவேஷ மூச்சால்`, `விட்டானுக்கும்?`, `மண்டேகங்கள்`, `நாய்க்குட்டி`, and `மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை`;\n"
    )
    text = text.replace(marker, marker + addition, 1)
text = replace(text, "PDF 20–34 introduces no newly distinct standalone lyric/song block; PDF 35–36 contains the already mapped scene-21 lyrical block.", "PDF 20–34 introduces no newly distinct standalone lyric/song block; PDF 35–36 contains the already mapped scene-21 lyrical block; PDF 40–44 adds no new standalone lyric/song block.")
text = re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$', f'## Exact next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Transcription README.
path = ROOT / "works/naam/transcription/README.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–39 / 35 pages", "PDF 5–44 / 40 pages"),
    ("historical-glyph pages checked during first pass: **35/67**", "historical-glyph pages checked during first pass: **40/67**"),
    ("completed batches: `parts/pdf-005-009.md`, `parts/pdf-010-014.md`, `parts/pdf-015-019.md`, `parts/pdf-020-024.md`, `parts/pdf-025-029.md`, `parts/pdf-030-034.md`;", "completed batches: `parts/pdf-005-009.md`, `parts/pdf-010-014.md`, `parts/pdf-015-019.md`, `parts/pdf-020-024.md`, `parts/pdf-025-029.md`, `parts/pdf-030-034.md`, `parts/pdf-035-039.md`;"),
    ("current batch: `parts/pdf-035-039.md`", "current batch: `parts/pdf-040-044.md`"),
    ("PDF 6–39: visible printed numerals 6–39", "PDF 6–44: visible printed numerals 6–44"),
    ("PDF 10–39 introduced **0 new explicit uncertainty markers**.", "PDF 10–44 introduced **0 new explicit uncertainty markers**."),
]:
    text = replace(text, old, new)
if "PDF 42 `மண்ணைவாரிப்`" not in text.split("## PDF 15–19", 1)[0]:
    anchor = "- PDF 29 `அணா`: positive historical `ணா` case.\n"
    # tolerate punctuation variation by inserting after the established PDF29 example line
    if anchor not in text:
        anchor = "- PDF 29 `அணா`: positive historical `ணா` case."
    if anchor in text:
        text = text.replace(anchor, anchor + "\n- PDF 40/41/43/44 `உன்னை` / `குமரனை`: checked historical `னை`; PDF 42 `மண்ணைவாரிப்`: checked historical `ணை`;", 1)
if "## PDF 40–44 source decisions" not in text:
    section = '''\n## PDF 40–44 source decisions\n\nThe eighth batch continues `காட்சி-24.`, contains `காட்சி 25`, `காட்சி 26`, and `காட்சி 27`, and ends within scene 27.\n\n- PDF 40 preserves `கோவேரிக் கழுதைக்கு` and the confrontation rhetoric; `உன்னை` is checked historical `னை`.\n- PDF 41 preserves `ஆவேஷ மூச்சால்`, the rights rhetoric, and the source hut-burning stage directions; `உன்னை` is checked historical `னை`.\n- PDF 42 opens scene 25; `மண்ணைவாரிப்` is checked historical `ணை`; source `விவாக சப முகூர்த்தத்துக்கு` and `விட்டானுக்கும்?` remain unmodernized; scene 26 opens later on the page.\n- PDF 43 opens scene 27 and preserves the extended `பாவம்` rhetoric including source `மண்டேகங்கள்`; `உன்னைப்` / `குமரனை` are checked historical `னை`.\n- PDF 44 preserves Maathirai's `நாய்க்குட்டி` / notice / medical wordplay and `மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை`; `உன்னை` is checked historical `னை`.\n- PDF 40–44 introduces **0 new explicit uncertainty markers** and no newly distinct standalone lyric/song block.\n\nSee `../notes/textual-notes-pdf-040-044.md` for the batch decision log.\n'''
    text = text.replace("\n## Performance / lyric evidence encountered so far\n", section + "\n## Performance / lyric evidence encountered so far\n", 1)
text = replace(text, "- PDF 20–34 introduces no newly distinct standalone song/lyric block.", "- PDF 20–34 introduces no newly distinct standalone song/lyric block.\n- PDF 35–36 preserves the mapped scene-21 lyrical witness; PDF 40–44 adds no new standalone lyric/song block.")
text = re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$', f'## Next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Historical glyph audit.
path = ROOT / "works/naam/notes/historical-glyph-audit.md"
text = path.read_text(encoding="utf-8")
text = replace(
    text,
    "| PDF 35–39 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 40–71 | 32 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **35** | **0** | **35** | **partial-first-pass** |",
    "| PDF 35–39 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 40–44 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 45–71 | 27 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **40** | **0** | **40** | **partial-first-pass** |",
)
marker = "| 39 | 39 | historical `னோ` cluster | `எமனோடு` | `னோ` | enlarged source pixels + same-edition family comparison | draft-supported |\n"
if "| 42 | 42 | historical `ணை` cluster" not in text:
    rows = (
        "| 40 | 40 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels | draft-supported |\n"
        "| 42 | 42 | historical `ணை` cluster | `மண்ணைவாரிப்` | `ணை` | enlarged source pixels | draft-supported |\n"
        "| 43 | 43 | historical `னை` cluster | `குமரனை` | `னை` | enlarged source pixels | draft-supported |\n"
    )
    text = text.replace(marker, marker + rows, 1)
if "## PDF 40–44 glyph/text findings" not in text:
    section = '''\n## PDF 40–44 glyph/text findings\n\n- PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`;\n- PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`;\n- source-period/colloquial readings `கோவேரிக் கழுதைக்கு`, `ஆவேஷ மூச்சால்`, `விட்டானுக்கும்?`, `மண்டேகங்கள்`, `நாய்க்குட்டி`, and `மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை` remain unmodernized;\n- PDF 40–44 introduced **0 new explicit uncertainty markers** and no new standalone lyric/song block.\n'''
    text = text.replace("\n## Source-irregular forms retained\n", section + "\n## Source-irregular forms retained\n", 1)
text = replace(text, "- PDF 25–29 source-irregular/period wording remains as documented in `textual-notes-pdf-025-029.md`.", "- PDF 25–29 source-irregular/period wording remains as documented in `textual-notes-pdf-025-029.md`;\n- PDF 40–44 source-irregular/period wording remains as documented in `textual-notes-pdf-040-044.md`.")
text = replace(text, "- PDF 20–34 introduces no newly distinct standalone lyric/song structure; PDF 35–36 contains the mapped scene-21 lyrical witness.", "- PDF 20–34 introduces no newly distinct standalone lyric/song structure; PDF 35–36 contains the mapped scene-21 lyrical witness; PDF 40–44 adds no new standalone lyric/song structure.")
text = replace(text, "- PDF 10–39 introduced **0 new explicit uncertainty markers**.", "- PDF 10–44 introduced **0 new explicit uncertainty markers**.")
text = re.sub(r'## Next activity\n\n.*?$', f'## Next activity\n\n{NEXT}\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Work-local project handover.
path = ROOT / "works/naam/PROJECT_HANDOVER.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–39 / 35 of 67 pages", "PDF 5–44 / 40 of 67 pages"),
    ("historical-glyph first-pass checked: **35/67**", "historical-glyph first-pass checked: **40/67**"),
    ("- `transcription/parts/pdf-035-039.md`;", "- `transcription/parts/pdf-035-039.md`;\n- `transcription/parts/pdf-040-044.md`;"),
    ("- `notes/textual-notes-pdf-035-039.md`;", "- `notes/textual-notes-pdf-035-039.md`;\n- `notes/textual-notes-pdf-040-044.md`;"),
]:
    text = replace(text, old, new)
if "### PDF 40–44" not in text:
    marker = "\n## Historical Tamil glyph rule\n"
    section = '''\n### PDF 40–44\n\n- continues scene 24; contains scenes 25–27; ends within scene 27;\n- PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`; PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`;\n- source-period/colloquial forms including `கோவேரிக் கழுதைக்கு`, `ஆவேஷ மூச்சால்`, `விட்டானுக்கும்?`, `மண்டேகங்கள்`, `நாய்க்குட்டி`, and `மாத்திரை முன்னேற்ற ஆஸ்பத்திரியை` remain source-controlled;\n- PDF 40–44 introduces **0** new uncertainty markers and no new standalone lyric/song block;\n- all 40 first-pass pages remain **draft / needs-review**, not verified.\n'''
    text = text.replace(marker, section + marker, 1)
text = replace(text, "all 35 first-pass pages remain **draft / needs-review**, not verified.", "all 35 pages through PDF 39 remain **draft / needs-review**, not verified.")
text = re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\s*$', f'## Exact next activity\n\n> **{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Next-chat prompt: rewrite the compact live handoff rather than stacking stale checkpoints.
path = ROOT / "works/naam/NEXT_CHAT_PROMPT.md"
prompt = f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint when this prompt was prepared:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **PDF 5–44 / 40 of 67 pages**;\n- verified pages: **0**;\n- historical-glyph first-pass checked: **40/67**;\n- historical-glyph final verified: **0/67**;\n- open uncertainty markers: **2**;\n- next batch: **PDF 45–49**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; screenplay PDF **5–71**.\n\n## Frozen first-pass batches PDF 5–44\n\nDo not redo or silently rewrite completed pages absent new direct-scan evidence. The cumulative source uncertainties remain exactly **2** (PDF 5 damaged introductory text; PDF 9 unclear montage word). PDF 10–44 adds none.\n\nRecent glyph precedents: PDF 39 `எமனோடு` (`னோ`), PDF 40/41/43/44 `உன்னை` / `குமரனை` (`னை`), PDF 42 `மண்ணைவாரிப்` (`ணை`). Occurrence-specific only; never global-replace.\n\nPDF 35–36 / scene 21 preserves the source lyrical witness beginning `மணமில்லா மலர் நானம்மா!`; authorship remains not adjudicated. PDF 40–44 contains no new standalone lyric/song block. PDF 49 opens the already mapped scene-31 lyrical block, so preserve only the booklet witness and do not infer missing lyrics or authorship.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
write_if_changed(path, prompt)

# Repository data registry.
path = ROOT / "data/works.json"
data = json.loads(path.read_text(encoding="utf-8"))
items = data if isinstance(data, list) else data.get("works", [])
naam = next((item for item in items if item.get("id") == "naam"), None)
if naam is None:
    raise SystemExit("Naam entry not found in data/works.json")
naam.update({
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-044",
    "historical_glyph_audit": "partial-first-pass-through-pdf-044",
    "next_action": NEXT,
    "canonical_tamil_first_pass_pages_completed": 40,
    "canonical_tamil_first_pass_pdf_range_completed": "5-44",
    "canonical_tamil_first_pass_current_through_pdf": 44,
    "canonical_tamil_draft_pages": 40,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 40,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-040-044.md",
    "historical_glyph_pages_checked": 40,
    "historical_glyph_pages_verified": 0,
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-040-044.md",
    "pdf_40_44_new_performance_structures": 0,
    "pdf_42_historical_nai_decoding": "மண்ணைவாரிப்",
})
write_if_changed(path, json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")

# Root README: replace the complete Naam status block for consistency.
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
naam_block = f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake and the 45-scene structural map are complete; canonical Tamil first-pass transcription is in progress.\n\n- source: **72 PDF pages**, image-only; SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`;\n- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;\n- source-numbered scenes: **45 — காட்சி 1–45**, sequential;\n- canonical Tamil first pass: **PDF 5–44 / 40 of 67 pages**;\n- verified pages: **0**; separate visual-fidelity audit: **not-started**;\n- historical-glyph first-pass checked: **40/67**; final glyph-verified: **0/67**;\n- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–44 adds none;\n- newest batch: `works/naam/transcription/parts/pdf-040-044.md`;\n- PDF 40/41/43/44 `உன்னை` / `குமரனை` and PDF 42 `மண்ணைவாரிப்` were checked against historical `னை` / `ணை`;\n- PDF 40–44 adds no new uncertainty marker and no new standalone lyric/song block;\n- PDF 49 opens the next mapped scene-31 lyrical-block safeguard;\n- downstream derivatives remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''
text, n = re.subn(r'## நாம் status\n.*?(?=## ராஜா ராணி status)', naam_block + "\n", text, count=1, flags=re.S)
if n != 1:
    raise SystemExit("Could not replace root README Naam block")
write_if_changed(path, text)

# Master project handover: reconcile the active Naam checkpoint without touching closed works.
path = ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–39 / 35 of 67", "PDF 5–44 / 40 of 67"),
    ("PDF 5–39 / 35 of 67 pages", "PDF 5–44 / 40 of 67 pages"),
    ("glyph first-pass **35/67**", "glyph first-pass **40/67**"),
    ("historical-glyph first-pass checked / final verified: **35/67 / 0/67**", "historical-glyph first-pass checked / final verified: **40/67 / 0/67**"),
    ("current batch: `works/naam/transcription/parts/pdf-035-039.md`", "current batch: `works/naam/transcription/parts/pdf-040-044.md`"),
    ("current source notes: `works/naam/notes/textual-notes-pdf-035-039.md`", "current source notes: `works/naam/notes/textual-notes-pdf-040-044.md`"),
    ("PDF 30–34 adds no new uncertainty marker and no newly distinct standalone lyric/song block;", "PDF 30–34 adds no new uncertainty marker and no newly distinct standalone lyric/song block;\n- PDF 35–36 preserves the mapped scene-21 lyrical witness; PDF 40–44 adds no new uncertainty marker or standalone lyric/song block;\n- PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`; PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`;"),
]:
    text = replace(text, old, new)
text = re.sub(r'\*\*Exact next activity:\*\* Continue canonical Tamil first-pass transcription with PDF 40–44.*?pass\.', f'**Exact next activity:** {NEXT}', text, count=1, flags=re.S)
write_if_changed(path, text)

# Repository-wide status audit: update current Naam block plus stale top/bottom summaries.
path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
text = path.read_text(encoding="utf-8")
text = replace(text, "PDF 5–24 / 20 of 67 pages", "PDF 5–44 / 40 of 67 pages")
text = replace(text, "historical-glyph first-pass **20/67**", "historical-glyph first-pass **40/67**")
text = replace(text, "PDF 5–39 / 35 of 67", "PDF 5–44 / 40 of 67")
text = replace(text, "historical-glyph first-pass checked / final verified: **35 / 0**", "historical-glyph first-pass checked / final verified: **40 / 0**")
text = replace(text, "current draft: `works/naam/transcription/parts/pdf-035-039.md`", "current draft: `works/naam/transcription/parts/pdf-040-044.md`")
text = replace(text, "current source notes: `works/naam/notes/textual-notes-pdf-035-039.md`", "current source notes: `works/naam/notes/textual-notes-pdf-040-044.md`")
text = replace(text, "PDF 25–29 introduces no new explicit uncertainty and no new standalone song/lyric block;", "PDF 25–29 introduces no new explicit uncertainty and no new standalone song/lyric block;\n- PDF 40–44 introduces no new explicit uncertainty and no new standalone song/lyric block;\n- PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`; PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`;" )
text = replace(text, "The next batch is PDF 25–29.", "The next batch is PDF 45–49.")
text = re.sub(r'\*\*Next production phase:\*\* Continue canonical Tamil first-pass transcription with PDF 40–44.*?pass\.', f'**Next production phase:** {NEXT}', text, count=1, flags=re.S)
write_if_changed(path, text)

# Final self-checks after synchronization.
expectations = {
    ROOT / "works/naam/metadata.yaml": ["first_pass_pages_completed: 40", "partial-first-pass-through-pdf-044", "pdf-040-044.md"],
    ROOT / "works/naam/README.md": ["PDF 5–44 / 40 of 67 pages", "PDF 42 `மண்ணைவாரிப்`", "PDF 45–49"],
    ROOT / "works/naam/transcription/README.md": ["PDF 5–44 / 40 pages", "## PDF 40–44 source decisions", "PDF 45–49"],
    ROOT / "works/naam/notes/historical-glyph-audit.md": ["| PDF 40–44 | 5 | 5 | 0 | 5 |", "`மண்ணைவாரிப்`", "PDF 45–49"],
    ROOT / "works/naam/PROJECT_HANDOVER.md": ["PDF 5–44 / 40 of 67 pages", "### PDF 40–44", "PDF 45–49"],
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md": ["PDF 5–44 / 40 of 67 pages", "PDF 45–49", "PDF 49 opens"],
    ROOT / "README.md": ["canonical Tamil first pass: **PDF 5–44 / 40 of 67 pages**", "newest batch: `works/naam/transcription/parts/pdf-040-044.md`", "PDF 45–49"],
    ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md": ["PDF 5–44 / 40 of 67", "40/67"],
    ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md": ["PDF 5–44 / 40 of 67", "PDF 45–49"],
}
for check_path, needles in expectations.items():
    body = check_path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in body:
            raise SystemExit(f"Post-sync assertion failed in {check_path.relative_to(ROOT)}: {needle}")

print("Naam PDF 40-44 synchronization complete")
for item in changed:
    print(item)
