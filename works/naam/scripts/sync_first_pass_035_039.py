#!/usr/bin/env python3
"""Synchronize Naam canonical first-pass checkpoint through PDF 39."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 40–44, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. Keep all first-pass pages "
    "draft/needs-review until the later separate visual-fidelity and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-035-039.md",
    ROOT / "works/naam/notes/textual-notes-pdf-035-039.md",
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
    "first_pass_pages_completed": 35,
    "current_through_pdf": 39,
    "historical_glyph_checked_pages": 35,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [40, 44]:
    raise SystemExit("Naam next batch must be PDF 40-44")

batch = (ROOT / "works/naam/transcription/parts/pdf-035-039.md").read_text(encoding="utf-8")
for needle in [
    "## காட்சி 21",
    "## காட்சி 22",
    "## காட்சி 23",
    "## காட்சி-24.",
    "மணமில்லா மலர் நானம்மா!",
    "உன்னை",
    "எமனோடு",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 35-39 source decision missing: {needle}")

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
    ("first_pass_pages_completed: 30", "first_pass_pages_completed: 35", "metadata pages"),
    ('first_pass_pdf_range_completed: "5-34"', 'first_pass_pdf_range_completed: "5-39"', "metadata range"),
    ("first_pass_current_through_pdf: 34", "first_pass_current_through_pdf: 39", "metadata through pdf"),
    ("first_pass_current_through_printed_page: 34", "first_pass_current_through_printed_page: 39", "metadata through printed"),
    ("draft_pages: 30", "draft_pages: 35", "metadata drafts"),
    ("review_pages: 30", "review_pages: 35", "metadata review"),
    ("pages_checked: 30", "pages_checked: 35", "metadata glyph"),
    ("partial-first-pass-through-pdf-034", "partial-first-pass-through-pdf-039", "metadata status"),
    ('current_batch_path: "transcription/parts/pdf-030-034.md"', 'current_batch_path: "transcription/parts/pdf-035-039.md"', "metadata current batch"),
    ('current_textual_notes_path: "notes/textual-notes-pdf-030-034.md"', 'current_textual_notes_path: "notes/textual-notes-pdf-035-039.md"', "metadata notes"),
    ("pdf_30_34_new_performance_structures: 0", "pdf_35_39_new_performance_structures: 1", "metadata performance count"),
]:
    text = replace_once(text, old, new, label)
needle = '    - "transcription/parts/pdf-030-034.md"\n'
if '    - "transcription/parts/pdf-035-039.md"' not in text:
    text = replace_once(text, needle, needle + '    - "transcription/parts/pdf-035-039.md"\n', "metadata batch list")
if "batch_035_039_consequential_decodings" not in text:
    marker = "mapped_source_visible_performance_structures:\n"
    extra = '''  batch_035_039_consequential_decodings:\n    - pdf_page: 35\n      source_supported_unicode: "நானம்மா"\n      family: "னா"\n    - pdf_page: 37\n      source_supported_unicode: "உன்னை"\n      family: "னை"\n    - pdf_page: 39\n      source_supported_unicode: "எமனோடு"\n      family: "னோ"\n\n'''
    text = replace_once(text, marker, extra + marker, "metadata decoding block")
text = re.sub(r'next_action: ".*?"\n', f'next_action: "{NEXT}"\n', text, count=1)
write_if_changed(path, text)

# Work README.
path = ROOT / "works/naam/README.md"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("PDF 5–34 / 30 of 67 pages", "PDF 5–39 / 35 of 67 pages", "work README checkpoint"),
    ("30 pages checked / 0 final-verified", "35 pages checked / 0 final-verified", "work README glyph"),
    ("Current textual notes: `notes/textual-notes-pdf-030-034.md`", "Current textual notes: `notes/textual-notes-pdf-035-039.md`", "work README notes"),
    ("PDF **5–34** has now been transcribed as source-order draft material in six five-page batches.", "PDF **5–39** has now been transcribed as source-order draft material in seven five-page batches.", "work README batch count"),
    ("PDF 10–34 adds **0** new uncertainty markers", "PDF 10–39 adds **0** new uncertainty markers", "work README uncertainties"),
    ("**0** of the thirty first-pass pages are called verified yet.", "**0** of the thirty-five first-pass pages are called verified yet.", "work README verified count"),
]:
    text = replace_once(text, old, new, label)
if "`transcription/parts/pdf-035-039.md`" not in text:
    text = replace_once(text, "`transcription/parts/pdf-030-034.md`", "`transcription/parts/pdf-030-034.md`, `transcription/parts/pdf-035-039.md`", "work README batch list")
if "PDF 39 `எமனோடு`" not in text:
    marker = "- PDF 34 `அவளை` is checked historical `ளை`; PDF 34 `பஞ்சணை` is checked historical `ணை`;\n"
    addition = (
        "- PDF 35 `நானம்மா` is checked historical `னா`; PDF 37 `உன்னை` is checked historical `னை`; "
        "PDF 39 `எமனோடு` is checked historical `னோ`;\n"
        "- PDF 35–36 / `காட்சி 21` preserves the booklet's complete lineated lyrical witness beginning `மணமில்லா மலர் நானம்மா!`; authorship remains not adjudicated;\n"
    )
    text = replace_once(text, marker, marker + addition, "work README new decisions")
text = text.replace("PDF 20–34 introduces no newly distinct standalone lyric/song block.", "PDF 20–34 introduces no newly distinct standalone lyric/song block; PDF 35–36 contains the already mapped scene-21 lyrical block.")
text = re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\n\Z', f'## Exact next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Transcription README.
path = ROOT / "works/naam/transcription/README.md"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("PDF 5–34 / 30 pages", "PDF 5–39 / 35 pages", "trans README checkpoint"),
    ("30/67", "35/67", "trans README glyph"),
    ("current batch: `parts/pdf-030-034.md`", "current batch: `parts/pdf-035-039.md`", "trans README current batch"),
    ("PDF 6–34: visible printed numerals 6–34", "PDF 6–39: visible printed numerals 6–39", "trans README anchors"),
    ("PDF 10–34 introduced **0 new explicit uncertainty markers**.", "PDF 10–39 introduced **0 new explicit uncertainty markers**.", "trans README uncertainty"),
]:
    text = replace_once(text, old, new, label)
if "`parts/pdf-035-039.md`" not in text:
    text = replace_once(text, "`parts/pdf-030-034.md`;", "`parts/pdf-030-034.md`, `parts/pdf-035-039.md`;", "trans README batch list")
if "## PDF 35–39 source decisions" not in text:
    insertion = '''\n## PDF 35–39 source decisions\n\nThe seventh batch completes `காட்சி 20`, contains the full `காட்சி 21` lyrical witness across PDF 35–36, contains `காட்சி 22–23`, and opens/continues source heading `காட்சி-24.`.\n\n- PDF 35–36 preserves only the booklet witness beginning `மணமில்லா மலர் நானம்மா!`; no title or authorship is inferred.\n- PDF 35 `நானம்மா` is a checked historical-`னா` case.\n- PDF 37 `உன்னை` is a checked historical-`னை` case.\n- PDF 39 `எமனோடு` is a checked historical-`னோ` case.\n- Source-period wording such as `படாடோப பனிக்காற்றும்`, `சூழ்ச்சி வெயிலும்`, `மமதை மழையும்` remains unmodernized.\n- PDF 35–39 introduced **0 new explicit uncertainty markers**.\n\nSee `../notes/textual-notes-pdf-035-039.md` for the batch decision log.\n'''
    text = replace_once(text, "\n## Performance / lyric evidence encountered so far\n", insertion + "\n## Performance / lyric evidence encountered so far\n", "trans README insertion")
text = re.sub(r'## Next activity\n\n\*\*.*?\*\*.*?\n\Z', f'## Next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Historical glyph audit.
path = ROOT / "works/naam/notes/historical-glyph-audit.md"
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "| PDF 30–34 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 35–71 | 37 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **30** | **0** | **30** | **partial-first-pass** |",
    "| PDF 30–34 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 35–39 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 40–71 | 32 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **35** | **0** | **35** | **partial-first-pass** |",
    "glyph coverage",
)
if "| 39 | 39 | historical `னோ` cluster" not in text:
    marker = "| 34 | 34 | historical `ணை` cluster | `பஞ்சணை` | `ணை` | enlarged source pixels | draft-supported |\n"
    rows = (
        "| 35 | 35 | historical `னா` cluster | `நானம்மா` | `னா` | enlarged source pixels | draft-supported |\n"
        "| 37 | 37 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels | draft-supported |\n"
        "| 39 | 39 | historical `னோ` cluster | `எமனோடு` | `னோ` | enlarged source pixels + same-edition family comparison | draft-supported |\n"
    )
    text = replace_once(text, marker, marker + rows, "glyph findings rows")
if "## PDF 35–39 glyph/text findings" not in text:
    section = '''\n## PDF 35–39 glyph/text findings\n\n- PDF 35 `நானம்மா` is checked historical `னா`;\n- PDF 37 `உன்னை` is checked historical `னை`;\n- PDF 39 `எமனோடு` is checked historical `னோ`;\n- the PDF 35–36 scene-21 lyric is preserved as printed with lineation and without outside reconstruction or authorship inference;\n- PDF 35–39 introduced **0 new explicit uncertainty markers**.\n'''
    text = replace_once(text, "\n## Source-irregular forms retained\n", section + "\n## Source-irregular forms retained\n", "glyph section")
text = text.replace("PDF 20–34 introduces no newly distinct standalone lyric/song structure.", "PDF 20–34 introduces no newly distinct standalone lyric/song structure; PDF 35–36 contains the mapped scene-21 lyrical witness.")
text = text.replace("PDF 10–34 introduced **0 new explicit uncertainty markers**.", "PDF 10–39 introduced **0 new explicit uncertainty markers**.")
text = re.sub(r'## Next activity\n\n.*?\n\Z', f'## Next activity\n\n{NEXT}\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Project handover.
path = ROOT / "works/naam/PROJECT_HANDOVER.md"
text = path.read_text(encoding="utf-8")
for old, new, label in [
    ("PDF 5–34 / 30 of 67 pages", "PDF 5–39 / 35 of 67 pages", "handover checkpoint"),
    ("historical-glyph first-pass checked: **30/67**", "historical-glyph first-pass checked: **35/67**", "handover glyph"),
    ("all 30 first-pass pages remain", "all 35 first-pass pages remain", "handover draft count"),
]:
    if old in text:
        text = text.replace(old, new)
if "`transcription/parts/pdf-035-039.md`;" not in text:
    text = replace_once(text, "- `transcription/parts/pdf-030-034.md`;\n", "- `transcription/parts/pdf-030-034.md`;\n- `transcription/parts/pdf-035-039.md`;\n", "handover batch file")
if "`notes/textual-notes-pdf-035-039.md`;" not in text:
    text = replace_once(text, "- `notes/textual-notes-pdf-030-034.md`;\n", "- `notes/textual-notes-pdf-030-034.md`;\n- `notes/textual-notes-pdf-035-039.md`;\n", "handover notes file")
if "### PDF 35–39" not in text:
    section = '''\n### PDF 35–39\n\n- completes scene 20; contains scene 21 lyrical witness across PDF 35–36; contains scenes 22–23; opens/continues source heading `காட்சி-24.`;\n- PDF 35 `நானம்மா` is checked historical `னா`; PDF 37 `உன்னை` is checked historical `னை`; PDF 39 `எமனோடு` is checked historical `னோ`;\n- only the source booklet's scene-21 lyric witness is preserved; title/authorship are not inferred;\n- PDF 35–39 introduces **0** new uncertainty markers;\n- all 35 first-pass pages remain **draft / needs-review**, not verified.\n'''
    text = replace_once(text, "\n## Historical Tamil glyph rule\n", section + "\n## Historical Tamil glyph rule\n", "handover section")
text = re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\n\Z', f'## Exact next activity\n\n> **{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Next-chat prompt: replace with a compact authoritative handoff.
path = ROOT / "works/naam/NEXT_CHAT_PROMPT.md"
prompt = f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint when this prompt was prepared:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **PDF 5–39 / 35 of 67 pages**;\n- verified pages: **0**;\n- historical-glyph first-pass checked: **35/67**;\n- historical-glyph final verified: **0/67**;\n- open uncertainty markers: **2**;\n- next batch: **PDF 40–44**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; screenplay PDF **5–71**.\n\n## Frozen first-pass batches PDF 5–39\n\nDo not redo or silently rewrite completed pages absent new direct-scan evidence. The cumulative source uncertainties remain exactly **2** (PDF 5 damaged introductory text; PDF 9 unclear montage word). PDF 10–39 adds none.\n\nRecent glyph precedents: PDF 35 `நானம்மா` (`னா`), PDF 37 `உன்னை` (`னை`), PDF 39 `எமனோடு` (`னோ`). Occurrence-specific only; never global-replace.\n\nPDF 35–36 / scene 21 preserves the source lyrical witness beginning `மணமில்லா மலர் நானம்மா!`; authorship remains not adjudicated.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
write_if_changed(path, prompt)

# data/works.json mirror.
path = ROOT / "data/works.json"
data = json.loads(path.read_text(encoding="utf-8"))
naam = next((w for w in data if w.get("id") == "naam"), None)
if naam is None:
    raise SystemExit("Naam record missing from data/works.json")
naam.update({
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-039",
    "historical_glyph_audit": "partial-first-pass-through-pdf-039",
    "next_action": NEXT,
    "canonical_tamil_first_pass_pages_completed": 35,
    "canonical_tamil_first_pass_pdf_range_completed": "5-39",
    "canonical_tamil_first_pass_current_through_pdf": 39,
    "canonical_tamil_draft_pages": 35,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 35,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-035-039.md",
    "historical_glyph_pages_checked": 35,
    "historical_glyph_pages_verified": 0,
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-035-039.md",
    "pdf_35_39_new_performance_structures": 1,
    "pdf_35_historical_naa_decoding": "நானம்மா",
    "pdf_37_historical_nai_decoding": "உன்னை",
    "pdf_39_historical_noo_decoding": "எமனோடு",
})
write_if_changed(path, json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")

# Root README targeted Naam section.
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
text = text.replace("canonical Tamil first pass: **PDF 5–34 / 30 of 67 pages**;", "canonical Tamil first pass: **PDF 5–39 / 35 of 67 pages**;")
text = text.replace("historical-glyph first-pass checked: **30/67**; final glyph-verified: **0/67**;", "historical-glyph first-pass checked: **35/67**; final glyph-verified: **0/67**;")
text = text.replace("PDF 10–34 adds none", "PDF 10–39 adds none")
text = text.replace("newest batch: `works/naam/transcription/parts/pdf-030-034.md`;", "newest batch: `works/naam/transcription/parts/pdf-035-039.md`;")
text = text.replace("PDF 30–34 introduces no newly distinct standalone song/lyric block;", "PDF 35–36 preserves the mapped scene-21 lyrical witness; PDF 35–39 adds no new uncertainty marker;")
text = text.replace("PDF 35–36 / காட்சி 21 is the next mapped lyrical-block safeguard;", "PDF 39 `எமனோடு` is a checked historical `னோ` case;")
text = re.sub(r'\*\*Next:\*\* Continue canonical Tamil first-pass transcription with PDF 35–39.*?pass\.', f'**Next:** {NEXT}', text, count=1)
write_if_changed(path, text)

# Master handover targeted active checkpoint lines.
path = ROOT / "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
text = path.read_text(encoding="utf-8")
text = text.replace("canonical Tamil first pass **PDF 5–34 / 30 of 67**; glyph first-pass **30/67**", "canonical Tamil first pass **PDF 5–39 / 35 of 67**; glyph first-pass **35/67**")
text = text.replace("next PDF 35–39", "next PDF 40–44")
text = text.replace("canonical Tamil first pass: **PDF 5–34 / 30 of 67 pages**;", "canonical Tamil first pass: **PDF 5–39 / 35 of 67 pages**;")
text = text.replace("historical-glyph first-pass checked / final verified: **30/67 / 0/67**;", "historical-glyph first-pass checked / final verified: **35/67 / 0/67**;")
text = text.replace("current batch: `works/naam/transcription/parts/pdf-030-034.md`;", "current batch: `works/naam/transcription/parts/pdf-035-039.md`;")
text = text.replace("current source notes: `works/naam/notes/textual-notes-pdf-030-034.md`;", "current source notes: `works/naam/notes/textual-notes-pdf-035-039.md`;")
text = text.replace("PDF 30–34 adds no new uncertainty marker and no newly distinct standalone lyric/song block;", "PDF 35–39 adds no new uncertainty marker; PDF 35–36 preserves the mapped scene-21 lyrical witness; PDF 39 `எமனோடு` is checked historical `னோ`;")
text = re.sub(r'\*\*Exact next activity:\*\* Continue canonical Tamil first-pass transcription with PDF 35–39.*?pass\.', f'**Exact next activity:** {NEXT}', text, count=1)
write_if_changed(path, text)

# Status audit targeted current Naam checkpoint (leave historical audit date/result prose otherwise intact).
path = ROOT / "docs/STATUS_CONSISTENCY_AUDIT.md"
text = path.read_text(encoding="utf-8")
text = text.replace("first pass **PDF 5–34 / 30 of 67**, 0 verified", "first pass **PDF 5–39 / 35 of 67**, 0 verified")
text = text.replace("canonical Tamil first pass: **PDF 5–34 / 30 of 67 pages**;", "canonical Tamil first pass: **PDF 5–39 / 35 of 67 pages**;")
text = text.replace("historical-glyph first-pass checked / final verified: **30 / 0**;", "historical-glyph first-pass checked / final verified: **35 / 0**;")
text = text.replace("current draft: `works/naam/transcription/parts/pdf-030-034.md`;", "current draft: `works/naam/transcription/parts/pdf-035-039.md`;")
text = text.replace("current source notes: `works/naam/notes/textual-notes-pdf-030-034.md`;", "current source notes: `works/naam/notes/textual-notes-pdf-035-039.md`;")
text = re.sub(r'\*\*Next production phase:\*\* Continue canonical Tamil first-pass transcription with PDF 35–39.*?pass\.', f'**Next production phase:** {NEXT}', text, count=1)
write_if_changed(path, text)

print("Naam PDF 35-39 synchronization PASS")
for item in changed:
    print(item)
