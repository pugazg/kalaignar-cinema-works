#!/usr/bin/env python3
"""Synchronize Naam canonical first-pass checkpoint through PDF 54."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 55–59, preserving source order, "
    "stable page anchors and page-level historical-glyph checks. PDF 59 reaches the first of the "
    "already mapped poetic/song-like blocks between scenes 36 and 37; preserve only the booklet "
    "witness and do not infer missing lyrics or authorship. Keep all first-pass pages draft/needs-review "
    "until the later separate visual-fidelity and final historical-glyph gates pass."
)

required = [
    ROOT / "works/naam/transcription/index.json",
    ROOT / "works/naam/transcription/parts/pdf-050-054.md",
    ROOT / "works/naam/notes/textual-notes-pdf-050-054.md",
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
    "first_pass_pages_completed": 50,
    "current_through_pdf": 54,
    "historical_glyph_checked_pages": 50,
    "verified_pages": 0,
    "open_uncertainty_markers": 2,
}
for key, expected in checks.items():
    if index.get(key) != expected:
        raise SystemExit(f"Transcription index mismatch {key}: {index.get(key)!r} != {expected!r}")
if index.get("next_batch_pdf_range") != [55, 59]:
    raise SystemExit("Naam next batch must be PDF 55-59")

batch = (ROOT / "works/naam/transcription/parts/pdf-050-054.md").read_text(encoding="utf-8")
for needle in [
    "தனியாய் விழித்தீரோ",
    "## காட்சி-32",
    "## காட்சி 33",
    "மலையங்களா",
    "அண்ணுமலை",
    "இந்த மூட்டாள் பயல் சிநேகிதன்—சங்கரமூர்த்தி!",
    "சிசுஹத்தி",
]:
    if needle not in batch:
        raise SystemExit(f"Naam PDF 50-54 source decision missing: {needle}")

changed: list[str] = []

def write_if_changed(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if old != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def rep(text: str, old: str, new: str) -> str:
    return text.replace(old, new)

# Work metadata.
path = ROOT / "works/naam/metadata.yaml"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("first_pass_pages_completed: 45", "first_pass_pages_completed: 50"),
    ('first_pass_pdf_range_completed: "5-49"', 'first_pass_pdf_range_completed: "5-54"'),
    ("first_pass_current_through_pdf: 49", "first_pass_current_through_pdf: 54"),
    ("first_pass_current_through_printed_page: 49", "first_pass_current_through_printed_page: 54"),
    ("draft_pages: 45", "draft_pages: 50"),
    ("review_pages: 45", "review_pages: 50"),
    ('current_batch_path: "transcription/parts/pdf-045-049.md"', 'current_batch_path: "transcription/parts/pdf-050-054.md"'),
    ('current_textual_notes_path: "notes/textual-notes-pdf-045-049.md"', 'current_textual_notes_path: "notes/textual-notes-pdf-050-054.md"'),
    ("pages_checked: 45", "pages_checked: 50"),
    ("canonical_tamil_transcription: partial-first-pass-through-pdf-049", "canonical_tamil_transcription: partial-first-pass-through-pdf-054"),
    ("historical_glyph_audit: partial-first-pass-through-pdf-049", "historical_glyph_audit: partial-first-pass-through-pdf-054"),
]:
    text = rep(text, old, new)
needle = '    - "transcription/parts/pdf-045-049.md"\n'
if '    - "transcription/parts/pdf-050-054.md"' not in text:
    text = text.replace(needle, needle + '    - "transcription/parts/pdf-050-054.md"\n', 1)
if "batch_050_054_consequential_decodings" not in text:
    marker = "mapped_source_visible_performance_structures:\n"
    extra = '''  batch_050_054_consequential_decodings:\n    - pdf_page: 51\n      source_supported_unicode: "என்னை"\n      family: "னை"\n    - pdf_page: 52\n      source_supported_unicode: "மலையங்களா"\n      family: "லை"\n    - pdf_page: 52\n      source_supported_unicode: "அண்ணுமலை"\n      family: "லை"\n    - pdf_page: 53\n      source_supported_unicode: "அண்ணுமலை"\n      family: "லை"\n    - pdf_page: 54\n      source_supported_unicode: "மலையங்களா"\n      family: "லை"\n\n'''
    text = text.replace(marker, extra + marker, 1)
if "pdf_50_54_new_performance_structures" not in text:
    text = text.replace(
        "  pdf_45_49_new_performance_structures: 1\n",
        "  pdf_45_49_new_performance_structures: 1\n  pdf_50_54_new_performance_structures: 0\n",
        1,
    )
text = re.sub(r'next_action: ".*?"\s*$', f'next_action: "{NEXT}"', text, count=1, flags=re.S)
write_if_changed(path, text)

# Work README.
path = ROOT / "works/naam/README.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–49 / 45 of 67 pages", "PDF 5–54 / 50 of 67 pages"),
    ("45 pages checked / 0 final-verified", "50 pages checked / 0 final-verified"),
    ("Current textual notes: `notes/textual-notes-pdf-045-049.md`", "Current textual notes: `notes/textual-notes-pdf-050-054.md`"),
    ("PDF **5–49** has now been transcribed as source-order draft material in nine five-page batches.", "PDF **5–54** has now been transcribed as source-order draft material in ten five-page batches."),
    ("PDF 10–49 adds **0** new uncertainty markers", "PDF 10–54 adds **0** new uncertainty markers"),
    ("**0** of the forty-five first-pass pages are called verified yet.", "**0** of the fifty first-pass pages are called verified yet."),
]:
    text = rep(text, old, new)
if "`transcription/parts/pdf-050-054.md`" not in text:
    text = text.replace("`transcription/parts/pdf-045-049.md`", "`transcription/parts/pdf-045-049.md`, `transcription/parts/pdf-050-054.md`", 1)
marker = "- PDF 45 `கொன்றாய்` is checked historical `றா`; PDF 48–49 `என்னை` is checked historical `னை`; PDF 49 `மணாளன்` is checked historical `ணா`; PDF 49 `கேளேனோ` is checked historical `னோ`;\n"
if "PDF 52/54 `மலையங்களா`" not in text:
    add = (
        "- PDF 51 `என்னை` is checked historical `னை`; PDF 52/54 `மலையங்களா` and PDF 52–53 `அண்ணுமலை` are checked historical `லை`;\n"
        "- PDF 50 completes the mapped scene-31 lyrical witness from the booklet only; PDF 52 opens `காட்சி-32`, and PDF 54 opens `காட்சி 33`;\n"
    )
    if marker in text:
        text = text.replace(marker, marker + add, 1)
text = text.replace("PDF 49 opens the mapped scene-31 lyrical block.", "PDF 49 opens the mapped scene-31 lyrical block; PDF 50 completes it without outside reconstruction.")
text = re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$', f'## Exact next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Transcription README.
path = ROOT / "works/naam/transcription/README.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–49 / 45 pages", "PDF 5–54 / 50 pages"),
    ("historical-glyph pages checked during first pass: **45/67**", "historical-glyph pages checked during first pass: **50/67**"),
    ("current batch: `parts/pdf-045-049.md`", "current batch: `parts/pdf-050-054.md`"),
    ("PDF 6–49: visible printed numerals 6–49", "PDF 6–54: visible printed numerals 6–54"),
    ("PDF 10–49 introduced **0 new explicit uncertainty markers**.", "PDF 10–54 introduced **0 new explicit uncertainty markers**."),
]:
    text = rep(text, old, new)
if "`parts/pdf-050-054.md`" not in text:
    text = text.replace("`parts/pdf-045-049.md`;", "`parts/pdf-045-049.md`, `parts/pdf-050-054.md`;", 1)
if "## PDF 50–54 source decisions" not in text:
    section = '''\n## PDF 50–54 source decisions\n\nThe tenth batch completes the scene-31 lyrical witness, continues the Meenu / Malaiyappan / Sanjeevi sequence, opens `காட்சி-32`, and opens `காட்சி 33`.\n\n- PDF 50 preserves the continuation of the scene-31 lyrical witness with printed `(பேதம்)` cues and no outside reconstruction or authorship inference.\n- PDF 51 continues the Meenu / Malaiyappan confrontation; `என்னை` is checked historical `னை`.\n- PDF 52 opens `காட்சி-32`; `மலையங்களா` and `அண்ணுமலை` are checked historical `லை`.\n- PDF 53 preserves Maathirai's colloquial ghost-rumour account and `இந்த மூட்டாள் பயல் சிநேகிதன்—சங்கரமூர்த்தி!`; `அண்ணுமலை` is a further historical-`லை` occurrence.\n- PDF 54 opens `காட்சி 33` at `மலையங்களா`; the place-name is again checked historical `லை`; `சிசுஹத்தி` and source-colloquial will dialogue remain unmodernized.\n- PDF 50–54 introduced **0 new explicit uncertainty markers** and no newly distinct performance structure beyond completion of the already mapped scene-31 block.\n\nSee `../notes/textual-notes-pdf-050-054.md` for the batch decision log.\n'''
    text = text.replace("\n## Performance / lyric evidence encountered so far\n", section + "\n## Performance / lyric evidence encountered so far\n", 1)
text = text.replace("- PDF 49 opens the mapped scene-31 lyrical witness; PDF 50 continues it. No outside lyric text or authorship is inferred.", "- PDF 49 opens and PDF 50 completes the mapped scene-31 lyrical witness. No outside lyric text or authorship is inferred.")
text = re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$', f'## Next activity\n\n**{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Historical glyph audit.
path = ROOT / "works/naam/notes/historical-glyph-audit.md"
text = path.read_text(encoding="utf-8")
text = text.replace(
    "| PDF 45–49 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 50–71 | 22 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **45** | **0** | **45** | **partial-first-pass** |",
    "| PDF 45–49 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 50–54 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 55–71 | 17 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **50** | **0** | **50** | **partial-first-pass** |",
)
row_marker = "| 49 | 49 | historical `னோ` cluster | `கேளேனோ` | `னோ` | enlarged source pixels + same-edition PDF 39 comparison | draft-supported |\n"
if "| 54 | 54 | historical `லை` place-name" not in text:
    rows = (
        "| 51 | 51 | historical `னை` cluster | `என்னை` | `னை` | enlarged source pixels | draft-supported |\n"
        "| 52 | 52 | historical `லை` place-name | `மலையங்களா` | `லை` | enlarged source pixels | draft-supported |\n"
        "| 52 | 52 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |\n"
        "| 53 | 53 | historical `லை` name ending | `அண்ணுமலை` | `லை` | enlarged source pixels | draft-supported |\n"
        "| 54 | 54 | historical `லை` place-name | `மலையங்களா` | `லை` | enlarged source pixels | draft-supported |\n"
    )
    if row_marker in text:
        text = text.replace(row_marker, row_marker + rows, 1)
if "## PDF 50–54 glyph/text findings" not in text:
    section = '''\n## PDF 50–54 glyph/text findings\n\n- PDF 51 `என்னை` is checked historical `னை`;\n- PDF 52/54 `மலையங்களா` and PDF 52–53 `அண்ணுமலை` are checked historical `லை`;\n- PDF 50 completes the mapped scene-31 booklet lyric; printed `(பேதம்)` cues and lineation are preserved without outside reconstruction or authorship inference;\n- PDF 53 source `இந்த மூட்டாள் பயல் சிநேகிதன்—சங்கரமூர்த்தி!` and PDF 54 source `சிசுஹத்தி` remain unmodernized;\n- PDF 50–54 introduced **0 new explicit uncertainty markers**.\n'''
    text += section
text = re.sub(r'## Next activity\n\n.*?$', f'## Next activity\n\n{NEXT}\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Project handover.
path = ROOT / "works/naam/PROJECT_HANDOVER.md"
text = path.read_text(encoding="utf-8")
for old, new in [
    ("PDF 5–49 / 45 of 67 pages", "PDF 5–54 / 50 of 67 pages"),
    ("historical-glyph first-pass checked: **45/67**", "historical-glyph first-pass checked: **50/67**"),
    ("- `transcription/parts/pdf-045-049.md`;", "- `transcription/parts/pdf-045-049.md`;\n- `transcription/parts/pdf-050-054.md`;"),
    ("- `notes/textual-notes-pdf-045-049.md`;", "- `notes/textual-notes-pdf-045-049.md`;\n- `notes/textual-notes-pdf-050-054.md`;"),
]:
    text = rep(text, old, new)
if "### PDF 50–54" not in text:
    marker = "\n## Historical Tamil glyph rule\n"
    section = '''\n### PDF 50–54\n\n- completes the mapped scene-31 lyrical witness, then continues the Meenu / Malaiyappan / Sanjeevi sequence;\n- opens `காட்சி-32` and `காட்சி 33`;\n- PDF 51 `என்னை` is checked historical `னை`; PDF 52/54 `மலையங்களா` and PDF 52–53 `அண்ணுமலை` are checked historical `லை`;\n- PDF 50–54 introduces **0** new uncertainty markers;\n- all 50 first-pass pages remain **draft / needs-review**, not verified.\n'''
    text = text.replace(marker, section + marker, 1)
text = re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\s*$', f'## Exact next activity\n\n> **{NEXT}**\n', text, count=1, flags=re.S)
write_if_changed(path, text)

# Next-chat prompt: compact authoritative handoff.
path = ROOT / "works/naam/NEXT_CHAT_PROMPT.md"
prompt = f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint when this prompt was prepared:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **PDF 5–54 / 50 of 67 pages**;\n- verified pages: **0**;\n- historical-glyph first-pass checked: **50/67**;\n- historical-glyph final verified: **0/67**;\n- open uncertainty markers: **2**;\n- next batch: **PDF 55–59**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; screenplay PDF **5–71**.\n\n## Frozen first-pass batches PDF 5–54\n\nDo not redo or silently rewrite completed pages absent new direct-scan evidence. The cumulative source uncertainties remain exactly **2** (PDF 5 damaged introductory text; PDF 9 unclear montage word). PDF 10–54 adds none.\n\nRecent glyph precedents: PDF 49 `கேளேனோ` (`னோ`), PDF 51 `என்னை` (`னை`), PDF 52/54 `மலையங்களா` (`லை`), PDF 52–53 `அண்ணுமலை` (`லை`). Occurrence-specific only; never global-replace.\n\nPDF 49–50 / scene 31 is a source-visible lyrical witness with printed `(பேதம்)` cues; preserve booklet text only and do not infer title/authorship. PDF 59 reaches the first already mapped poetic/song-like block between scenes 36 and 37; apply the same safeguard.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
write_if_changed(path, prompt)

# data/works.json: mutate only Naam entry and preserve other records.
path = ROOT / "data/works.json"
data = json.loads(path.read_text(encoding="utf-8"))
items = data if isinstance(data, list) else data.get("works", [])
naam = next((item for item in items if item.get("id") == "naam"), None)
if naam is None:
    raise SystemExit("Naam entry not found in data/works.json")
naam.update({
    "canonical_tamil_transcription": "partial-first-pass-through-pdf-054",
    "historical_glyph_audit": "partial-first-pass-through-pdf-054",
    "next_action": NEXT,
    "canonical_tamil_first_pass_pages_completed": 50,
    "canonical_tamil_first_pass_pdf_range_completed": "5-54",
    "canonical_tamil_first_pass_current_through_pdf": 54,
    "canonical_tamil_draft_pages": 50,
    "canonical_tamil_verified_pages": 0,
    "canonical_tamil_review_pages": 50,
    "canonical_tamil_open_uncertainty_markers": 2,
    "canonical_tamil_current_batch_path": "works/naam/transcription/parts/pdf-050-054.md",
    "historical_glyph_pages_checked": 50,
    "historical_glyph_pages_verified": 0,
    "canonical_tamil_current_textual_notes_path": "works/naam/notes/textual-notes-pdf-050-054.md",
    "pdf_50_54_new_performance_structures": 0,
    "pdf_52_54_historical_lai_decoding": "மலையங்களா / அண்ணுமலை",
})
write_if_changed(path, json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")

# Root README — update Naam status section generically.
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
text = rep(text, "PDF 5–49 / 45 of 67 pages", "PDF 5–54 / 50 of 67 pages")
text = rep(text, "historical-glyph first-pass checked: **45/67**", "historical-glyph first-pass checked: **50/67**")
text = rep(text, "newest batch: `works/naam/transcription/parts/pdf-045-049.md`", "newest batch: `works/naam/transcription/parts/pdf-050-054.md`")
text = rep(text, "PDF 10–49 adds none", "PDF 10–54 adds none")
text = re.sub(r'\*\*Next:\*\* Continue canonical Tamil first-pass transcription with PDF 50–54.*?pass\.', f'**Next:** {NEXT}', text, count=1, flags=re.S)
write_if_changed(path, text)

# Master handover and status audit — checkpoint substitutions without touching other works.
for rel in ["docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md", "docs/STATUS_CONSISTENCY_AUDIT.md"]:
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    text = rep(text, "PDF 5–49 / 45 of 67", "PDF 5–54 / 50 of 67")
    text = rep(text, "PDF 5–49 / 45 of 67 pages", "PDF 5–54 / 50 of 67 pages")
    text = rep(text, "historical-glyph first-pass **45/67**", "historical-glyph first-pass **50/67**")
    text = rep(text, "historical-glyph first-pass checked / final verified: **45/67 / 0/67**", "historical-glyph first-pass checked / final verified: **50/67 / 0/67**")
    text = rep(text, "historical-glyph first-pass checked / final verified: **45 / 0**", "historical-glyph first-pass checked / final verified: **50 / 0**")
    text = rep(text, "current batch: `works/naam/transcription/parts/pdf-045-049.md`", "current batch: `works/naam/transcription/parts/pdf-050-054.md`")
    text = rep(text, "current draft: `works/naam/transcription/parts/pdf-045-049.md`", "current draft: `works/naam/transcription/parts/pdf-050-054.md`")
    text = rep(text, "current source notes: `works/naam/notes/textual-notes-pdf-045-049.md`", "current source notes: `works/naam/notes/textual-notes-pdf-050-054.md`")
    text = rep(text, "The next batch is PDF 50–54.", "The next batch is PDF 55–59.")
    text = re.sub(r'(?:\*\*Exact next activity:\*\*|\*\*Next production phase:\*\*) Continue canonical Tamil first-pass transcription with PDF 50–54.*?pass\.', lambda m: m.group(0).split(':')[0] + ':** ' + NEXT, text, count=1, flags=re.S)
    write_if_changed(path, text)

# Final checks.
expected = {
    ROOT / "works/naam/metadata.yaml": ["first_pass_pages_completed: 50", "partial-first-pass-through-pdf-054", "pdf-050-054.md"],
    ROOT / "works/naam/README.md": ["PDF 5–54 / 50 of 67 pages", "PDF 52/54 `மலையங்களா`", "PDF 55–59"],
    ROOT / "works/naam/transcription/README.md": ["PDF 5–54 / 50 pages", "## PDF 50–54 source decisions", "PDF 55–59"],
    ROOT / "works/naam/notes/historical-glyph-audit.md": ["| PDF 50–54 | 5 | 5 | 0 | 5 |", "`மலையங்களா`", "PDF 55–59"],
    ROOT / "works/naam/PROJECT_HANDOVER.md": ["PDF 5–54 / 50 of 67 pages", "### PDF 50–54", "PDF 55–59"],
    ROOT / "works/naam/NEXT_CHAT_PROMPT.md": ["PDF 5–54 / 50 of 67 pages", "PDF 55–59", "PDF 59 reaches"],
}
for p, needles in expected.items():
    content = p.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in content:
            raise SystemExit(f"Post-sync validation failed for {p.relative_to(ROOT)}: {needle}")

print("Naam PDF 50-54 checkpoint synchronized.")
for rel in changed:
    print(rel)
