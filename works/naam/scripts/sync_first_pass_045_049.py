#!/usr/bin/env python3
"""Synchronize Naam canonical first-pass checkpoint through PDF 49."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 50–54, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. PDF 50 continues the mapped "
    "scene-31 lyrical block; preserve only the booklet witness and do not infer missing lyrics or "
    "authorship. Keep all first-pass pages draft/needs-review until the later separate visual-fidelity "
    "and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-045-049.md",
    ROOT / "works/naam/notes/textual-notes-pdf-045-049.md",
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
    "first_pass_pages_completed": 45,
    "current_through_pdf": 49,
    "historical_glyph_checked_pages": 45,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [50, 54]:
    raise SystemExit("Naam next batch must be PDF 50-54")

batch = (ROOT / "works/naam/transcription/parts/pdf-045-049.md").read_text(encoding="utf-8")
for needle in [
    "## காட்சி 28.",
    "## காட்சி 29.",
    "## காட்சி 30,",
    "## காட்சி-31",
    "பொய் சொல்லுறியே!",
    "கண்ணங்கரேனு வந்திச்சாம்!",
    "கேளேனோ இனிமேல் இதுபோல் கீதம்",
    "தளா தீச்சுழலில்",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 45-49 source decision missing: {needle}")

changed: list[str] = []

def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing expected checkpoint text ({label}): {old}")
    return text.replace(old, new, 1)

# Work metadata.
path = ROOT / "works/naam/metadata.yaml"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("first_pass_pages_completed: 40", "first_pass_pages_completed: 45", "metadata pages"),
    ('first_pass_pdf_range_completed: "5-44"', 'first_pass_pdf_range_completed: "5-49"', "metadata range"),
    ("first_pass_current_through_pdf: 44", "first_pass_current_through_pdf: 49", "metadata through pdf"),
    ("first_pass_current_through_printed_page: 44", "first_pass_current_through_printed_page: 49", "metadata through printed"),
    ("draft_pages: 40", "draft_pages: 45", "metadata drafts"),
    ("review_pages: 40", "review_pages: 45", "metadata review"),
    ('current_batch_path: "transcription/parts/pdf-040-044.md"', 'current_batch_path: "transcription/parts/pdf-045-049.md"', "metadata batch"),
    ('current_textual_notes_path: "notes/textual-notes-pdf-040-044.md"', 'current_textual_notes_path: "notes/textual-notes-pdf-045-049.md"', "metadata notes"),
    ("pages_checked: 40", "pages_checked: 45", "metadata glyph pages"),
    ("canonical_tamil_transcription: partial-first-pass-through-pdf-044", "canonical_tamil_transcription: partial-first-pass-through-pdf-049", "metadata transcription status"),
    ("historical_glyph_audit: partial-first-pass-through-pdf-044", "historical_glyph_audit: partial-first-pass-through-pdf-049", "metadata glyph status"),
]:
    text = replace_once(text, old, new, label)
needle = '    - "transcription/parts/pdf-040-044.md"\n'
if '    - "transcription/parts/pdf-045-049.md"' not in text:
    text = replace_once(text, needle, needle + '    - "transcription/parts/pdf-045-049.md"\n', "metadata batch list")
if "batch_045_049_consequential_decodings" not in text:
    marker = "mapped_source_visible_performance_structures:\n"
    extra = '''  batch_045_049_consequential_decodings:\n    - pdf_page: 45\n      source_supported_unicode: "கொன்றாய்"\n      family: "றா"\n    - pdf_page: 48\n      source_supported_unicode: "என்னை"\n      family: "னை"\n    - pdf_page: 49\n      source_supported_unicode: "மணாளன்"\n      family: "ணா"\n    - pdf_page: 49\n      source_supported_unicode: "கேளேனோ"\n      family: "னோ"\n\n'''
    text = replace_once(text, marker, extra + marker, "metadata decoding block")
if "pdf_45_49_new_performance_structures" not in text:
    text = replace_once(
        text,
        "  pdf_40_44_new_performance_structures: 0\n",
        "  pdf_40_44_new_performance_structures: 0\n  pdf_45_49_new_performance_structures: 1\n",
        "metadata performance count",
    )
text = re.sub(r'next_action: ".*?"\s*$', f'next_action: "{NEXT}"', text, count=1, flags=re.S)
write_if_changed(path, text)

# Work README.
path = ROOT / "works/naam/README.md"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("PDF 5–44 / 40 of 67 pages", "PDF 5–49 / 45 of 67 pages", "work README checkpoint"),
    ("40 pages checked / 0 final-verified", "45 pages checked / 0 final-verified", "work README glyph"),
    ("Current textual notes: `notes/textual-notes-pdf-040-044.md`", "Current textual notes: `notes/textual-notes-pdf-045-049.md`", "work README notes"),
    ("PDF **5–44** has now been transcribed as source-order draft material in eight five-page batches.", "PDF **5–49** has now been transcribed as source-order draft material in nine five-page batches.", "work README batch count"),
    ("PDF 10–44 adds **0** new uncertainty markers", "PDF 10–49 adds **0** new uncertainty markers", "work README uncertainties"),
    ("**0** of the forty first-pass pages are called verified yet.", "**0** of the forty-five first-pass pages are called verified yet.", "work README verified count"),
]:
    text = replace_once(text, old, new, label)
if "`transcription/parts/pdf-045-049.md`" not in text:
    text = text.replace("`transcription/parts/pdf-040-044.md`", "`transcription/parts/pdf-040-044.md`, `transcription/parts/pdf-045-049.md`", 1)
if "PDF 49 `கேளேனோ`" not in text:
    marker = "- PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`; PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`;\n"
    addition = (
        "- PDF 45 `கொன்றாய்` is checked historical `றா`; PDF 48–49 `என்னை` is checked historical `னை`; PDF 49 `மணாளன்` is checked historical `ணா`; PDF 49 `கேளேனோ` is checked historical `னோ`;\n"
        "- PDF 49 / `காட்சி-31` opens the mapped lyrical witness beginning `பேசும் யாழே பெண் மானே`; only the booklet text is preserved and PDF 50 continues the same source block;\n"
    )
    text = replace_once(text, marker, marker + addition, "work README new decisions")
text = text.replace("PDF 40–44 adds no new standalone lyric/song block.", "PDF 40–44 adds no new standalone lyric/song block; PDF 49 opens the mapped scene-31 lyrical block.")
text = re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$', f'## Exact next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Transcription README.
path = ROOT / "works/naam/transcription/README.md"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("PDF 5–44 / 40 pages", "PDF 5–49 / 45 pages", "trans README checkpoint"),
    ("historical-glyph pages checked during first pass: **40/67**", "historical-glyph pages checked during first pass: **45/67**", "trans README glyph"),
    ("current batch: `parts/pdf-040-044.md`", "current batch: `parts/pdf-045-049.md`", "trans README current batch"),
    ("PDF 6–44: visible printed numerals 6–44", "PDF 6–49: visible printed numerals 6–49", "trans README anchors"),
    ("PDF 10–44 introduced **0 new explicit uncertainty markers**.", "PDF 10–49 introduced **0 new explicit uncertainty markers**.", "trans README uncertainty"),
]:
    text = replace_once(text, old, new, label)
if "`parts/pdf-045-049.md`" not in text:
    text = text.replace("`parts/pdf-040-044.md`;", "`parts/pdf-040-044.md`, `parts/pdf-045-049.md`;", 1)
if "## PDF 45–49 source decisions" not in text:
    section = '''\n## PDF 45–49 source decisions\n\nThe ninth batch opens `காட்சி 28.`, `காட்சி 29.`, and source `காட்சி 30,`, then opens `காட்சி-31` and the mapped lyrical block on PDF 49.\n\n- PDF 45 preserves the burned-hut scene, Meenu finding the will, and Sanjeevi's `பொய் சொல்லுறியே!`; `கொன்றாய்` is checked historical `றா`.\n- PDF 46 preserves `எம்ப்பா!`, the ghost-plan monologue, and `குமரனும்—மீனுவும் திடீரென்று சந்தித்து விட்டால்...?`.\n- PDF 47 preserves `பொய்பிரச்சாரம்`, the riverside rumor `கண்ணங்கரேனு வந்திச்சாம்!`, and opens `காட்சி 30,`.\n- PDF 48 preserves `எப்படி இரணமாச்சி...?`, the bandage-removal sequence and Kumaran's burned-face outburst; `என்னை` is checked historical `னை`.\n- PDF 49 preserves the continuation and Prema confrontation; `மணாளன்` is checked historical `ணா`. `கேளேனோ` is a same-edition historical-`னோ` decoding, compared with PDF 39 `எமனோடு`.\n- PDF 49 opens the scene-31 lyrical witness beginning `பேசும் யாழே பெண் மானே`; `தளா தீச்சுழலில்` is retained exactly as source-visible. PDF 50 continues the same source block.\n- PDF 45–49 introduced **0 new explicit uncertainty markers**.\n\nSee `../notes/textual-notes-pdf-045-049.md` for the batch decision log.\n'''
    text = text.replace("\n## Performance / lyric evidence encountered so far\n", section + "\n## Performance / lyric evidence encountered so far\n", 1)
text = text.replace("- PDF 35–36 preserves the mapped scene-21 lyrical witness; PDF 40–44 adds no new standalone lyric/song block.", "- PDF 35–36 preserves the mapped scene-21 lyrical witness; PDF 40–44 adds no new standalone lyric/song block.\n- PDF 49 opens the mapped scene-31 lyrical witness; PDF 50 continues it. No outside lyric text or authorship is inferred.")
text = re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$', f'## Next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Historical-glyph audit.
path = ROOT / "works/naam/notes/historical-glyph-audit.md"
text = path.read_text(encoding="utf-8")
old_coverage = "| PDF 40–44 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 45–71 | 27 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **40** | **0** | **40** | **partial-first-pass** |"
new_coverage = "| PDF 40–44 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 45–49 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 50–71 | 22 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **45** | **0** | **45** | **partial-first-pass** |"
text = replace_once(text, old_coverage, new_coverage, "glyph coverage")
if "| 49 | 49 | historical `னோ` cluster" not in text:
    marker = "| 43 | 43 | historical `னை` cluster | `குமரனை` | `னை` | enlarged source pixels | draft-supported |\n"
    rows = (
        "| 45 | 45 | historical `றா` cluster | `கொன்றாய்` | `றா` | enlarged source pixels | draft-supported |\n"
        "| 48 | 48 | historical `னை` cluster | `என்னை` | `னை` | enlarged source pixels | draft-supported |\n"
        "| 49 | 49 | historical `ணா` cluster | `மணாளன்` | `ணா` | enlarged source pixels | draft-supported |\n"
        "| 49 | 49 | historical `னோ` cluster | `கேளேனோ` | `னோ` | enlarged source pixels + same-edition PDF 39 comparison | draft-supported |\n"
    )
    text = replace_once(text, marker, marker + rows, "glyph findings rows")
if "## PDF 45–49 glyph/text findings" not in text:
    section = '''\n## PDF 45–49 glyph/text findings\n\n- PDF 45 `கொன்றாய்` is checked historical `றா`;\n- PDF 48–49 `என்னை` is checked historical `னை`;\n- PDF 49 `மணாளன்` is checked historical `ணா`;\n- PDF 49 `கேளேனோ` is checked historical `னோ`, using the same-edition PDF 39 `எமனோடு` precedent rather than modern visual resemblance;\n- PDF 49 opens the mapped scene-31 lyrical witness; `தளா தீச்சுழலில்` remains source-visible and unexpanded;\n- PDF 45–49 introduced **0 new explicit uncertainty markers**.\n'''
    text = text.replace("\n## Source-irregular forms retained\n", section + "\n## Source-irregular forms retained\n", 1)
text = text.replace("PDF 40–44 adds no new standalone lyric/song structure.", "PDF 40–44 adds no new standalone lyric/song structure; PDF 49 opens the mapped scene-31 lyrical witness and PDF 50 continues it.")
text = text.replace("PDF 10–44 introduced **0 new explicit uncertainty markers**.", "PDF 10–49 introduced **0 new explicit uncertainty markers**.")
text = re.sub(r'## Next activity\n\n.*?$', f'## Next activity\n\n{NEXT}\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Work-local project handover.
path = ROOT / "works/naam/PROJECT_HANDOVER.md"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("PDF 5–44 / 40 of 67 pages", "PDF 5–49 / 45 of 67 pages", "handover checkpoint"),
    ("historical-glyph first-pass checked: **40/67**", "historical-glyph first-pass checked: **45/67**", "handover glyph"),
    ("- `transcription/parts/pdf-040-044.md`;", "- `transcription/parts/pdf-040-044.md`;\n- `transcription/parts/pdf-045-049.md`;", "handover batch list"),
    ("- `notes/textual-notes-pdf-040-044.md`;", "- `notes/textual-notes-pdf-040-044.md`;\n- `notes/textual-notes-pdf-045-049.md`;", "handover notes list"),
]:
    text = replace_once(text, old, new, label)
if "### PDF 45–49" not in text:
    marker = "\n## Historical Tamil glyph rule\n"
    section = '''\n### PDF 45–49\n\n- opens scenes 28–30 and opens scene 31 on PDF 49;\n- PDF 45 `கொன்றாய்` is checked historical `றா`; PDF 48–49 `என்னை` is checked historical `னை`; PDF 49 `மணாளன்` is checked historical `ணா`; PDF 49 `கேளேனோ` is checked historical `னோ`;\n- source colloquial/period forms including `பொய் சொல்லுறியே!`, `பொய்பிரச்சாரம்`, `கண்ணங்கரேனு`, `இரணமாச்சி`, and `சண்டாளா` remain source-controlled;\n- PDF 49 opens the mapped scene-31 lyrical witness; only the booklet text is preserved and PDF 50 continues the same source block;\n- PDF 45–49 introduces **0** new uncertainty markers;\n- all 45 first-pass pages remain **draft / needs-review**, not verified.\n'''
    text = text.replace(marker, section + marker, 1)
text = re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\s*$', f'## Exact next activity\n\n> **{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Next-chat prompt: rewrite compact live handoff.
path = ROOT / "works/naam/NEXT_CHAT_PROMPT.md"
prompt = f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint when this prompt was prepared:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **PDF 5–49 / 45 of 67 pages**;\n- verified pages: **0**;\n- historical-glyph first-pass checked: **45/67**;\n- historical-glyph final verified: **0/67**;\n- open uncertainty markers: **2**;\n- next batch: **PDF 50–54**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; screenplay PDF **5–71**.\n\n## Frozen first-pass batches PDF 5–49\n\nDo not redo or silently rewrite completed pages absent new direct-scan evidence. The cumulative source uncertainties remain exactly **2** (PDF 5 damaged introductory text; PDF 9 unclear montage word). PDF 10–49 adds none.\n\nRecent glyph precedents: PDF 45 `கொன்றாய்` (`றா`), PDF 48–49 `என்னை` (`னை`), PDF 49 `மணாளன்` (`ணா`), PDF 49 `கேளேனோ` (`னோ`). Occurrence-specific only; never global-replace.\n\nPDF 49 opens the mapped scene-31 lyrical witness beginning `பேசும் யாழே பெண் மானே`; only the booklet witness is preserved. PDF 50 continues the same printed lyrical block. Do not infer missing lyric text, title, or authorship.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
write_if_changed(path, prompt)

# Repository data registry.
path = ROOT / "data/works.json"
data = json.loads(path.read_text(encoding="utf-8"))
items = data if isinstance(data, list) else data.get("works", [])
naam = next((item for item in items if item.get("id") == "naam"), None)
if naam is None:
    raise SystemExit("Naam entry not found in data/works.json")
naam.update({
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-049",
    "historical_glyph_audit": "partial-first-pass-through-pdf-049",
    "next_action": NEXT,
    "canonical_tamil_first_pass_pages_completed": 45,
    "canonical_tamil_first_pass_pdf_range_completed": "5-49",
    "canonical_tamil_first_pass_current_through_pdf": 49,
    "canonical_tamil_draft_pages": 45,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 45,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-045-049.md",
    "historical_glyph_pages_checked": 45,
    "historical_glyph_pages_verified": 0,
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-045-049.md",
    "pdf_45_49_new_performance_structures": 1,
    "pdf_49_historical_no_decoding": "கேளேனோ",
})
write_if_changed(path, json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")

# Root README: replace complete Naam status block.
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
naam_block = f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake and the 45-scene structural map are complete; canonical Tamil first-pass transcription is in progress.\n\n- source: **72 PDF pages**, image-only; SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`;\n- front matter / screenplay / back matter: **PDF 1–4 / 5–71 / 72**;\n- source-numbered scenes: **45 — காட்சி 1–45**, sequential;\n- canonical Tamil first pass: **PDF 5–49 / 45 of 67 pages**;\n- verified pages: **0**; separate visual-fidelity audit: **not-started**;\n- historical-glyph first-pass checked: **45/67**; final glyph-verified: **0/67**;\n- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–49 adds none;\n- newest batch: `works/naam/transcription/parts/pdf-045-049.md`;\n- PDF 45 `கொன்றாய்`, PDF 48–49 `என்னை`, PDF 49 `மணாளன்`, and PDF 49 `கேளேனோ` were checked against historical `றா` / `னை` / `ணா` / `னோ`;\n- PDF 49 opens the mapped scene-31 lyrical witness; PDF 50 continues it, with no outside lyric or authorship inference;\n- downstream derivatives remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''
text, n = re.subn(r'## நாம் status\n.*?(?=## ராஜா ராணி status)', naam_block + "\n", text, count=1, flags=re.S)
if n != 1:
    raise SystemExit("Could not replace root README Naam block")
write_if_changed(path, text)

# Master project handover: reconcile active Naam checkpoint.
path = ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–44 / 40 of 67", "PDF 5–49 / 45 of 67"),
    ("PDF 5–44 / 40 of 67 pages", "PDF 5–49 / 45 of 67 pages"),
    ("glyph first-pass **40/67**", "glyph first-pass **45/67**"),
    ("historical-glyph first-pass checked / final verified: **40/67 / 0/67**", "historical-glyph first-pass checked / final verified: **45/67 / 0/67**"),
    ("current batch: `works/naam/transcription/parts/pdf-040-044.md`", "current batch: `works/naam/transcription/parts/pdf-045-049.md`"),
    ("current source notes: `works/naam/notes/textual-notes-pdf-040-044.md`", "current source notes: `works/naam/notes/textual-notes-pdf-045-049.md`"),
]:
    text = text.replace(old, new)
if "PDF 49 `கேளேனோ`" not in text:
    marker = "- PDF 42 `மண்ணைவாரிப்` is checked historical `ணை`; PDF 40/41/43/44 `உன்னை` / `குமரனை` are checked historical `னை`;"
    addition = "\n- PDF 45 `கொன்றாய்` is checked historical `றா`; PDF 48–49 `என்னை` is checked historical `னை`; PDF 49 `மணாளன்` is checked historical `ணா`; PDF 49 `கேளேனோ` is checked historical `னோ`;\n- PDF 49 opens the mapped scene-31 lyrical witness; PDF 50 continues the same source block and no outside lyric/authorship inference is allowed;"
    if marker in text:
        text = text.replace(marker, marker + addition, 1)
text = re.sub(r'\*\*Exact next activity:\*\* Continue canonical Tamil first-pass transcription with PDF 45–49.*?pass\.', f'**Exact next activity:** {NEXT}', text, count=1, flags=re.S)
write_if_changed(path, text)

# Repository-wide status audit.
path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–44 / 40 of 67 pages", "PDF 5–49 / 45 of 67 pages"),
    ("PDF 5–44 / 40 of 67", "PDF 5–49 / 45 of 67"),
    ("historical-glyph first-pass **40/67**", "historical-glyph first-pass **45/67**"),
    ("historical-glyph first-pass checked / final verified: **40 / 0**", "historical-glyph first-pass checked / final verified: **45 / 0**"),
    ("current draft: `works/naam/transcription/parts/pdf-040-044.md`", "current draft: `works/naam/transcription/parts/pdf-045-049.md`"),
    ("current source notes: `works/naam/notes/textual-notes-pdf-040-044.md`", "current source notes: `works/naam/notes/textual-notes-pdf-045-049.md`"),
    ("The next batch is PDF 45–49.", "The next batch is PDF 50–54."),
]:
    text = text.replace(old, new)
text = re.sub(r'\*\*Next production phase:\*\* Continue canonical Tamil first-pass transcription with PDF 45–49.*?pass\.', f'**Next production phase:** {NEXT}', text, count=1, flags=re.S)
write_if_changed(path, text)

# Final self-checks.
expectations = {
    ROOT / "works/naam/metadata.yaml": ["first_pass_pages_completed: 45", "partial-first-pass-through-pdf-049", "pdf-045-049.md", "கேளேனோ"],
    ROOT / "works/naam/README.md": ["PDF 5–49 / 45 of 67 pages", "PDF 49 `கேளேனோ`", "PDF 50–54"],
    ROOT / "works/naam/transcription/README.md": ["PDF 5–49 / 45 pages", "## PDF 45–49 source decisions", "PDF 50–54"],
    ROOT / "works/naam/notes/historical-glyph-audit.md": ["| PDF 45–49 | 5 | 5 | 0 | 5 |", "`கேளேனோ`", "PDF 50–54"],
    ROOT / "works/naam/PROJECT_HANDOVER.md": ["PDF 5–49 / 45 of 67 pages", "### PDF 45–49", "PDF 50–54"],
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md": ["PDF 5–49 / 45 of 67 pages", "PDF 50–54", "PDF 50 continues"],
    ROOT / "README.md": ["canonical Tamil first pass: **PDF 5–49 / 45 of 67 pages**", "newest batch: `works/naam/transcription/parts/pdf-045-049.md`", "PDF 50–54"],
}
for path, needles in expectations.items():
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"Post-sync expectation missing in {path.relative_to(ROOT)}: {needle}")

print("Naam PDF 45-49 synchronization PASS")
for item in changed:
    print(item)
