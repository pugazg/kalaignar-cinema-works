#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NEXT = (
    "Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 20–24. "
    "Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified "
    "PDF 6–9 or PDF 11–19 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain explicit "
    "physical-source-damage holds. Structured derivatives and English translation remain blocked until the verified "
    "Tamil gate is complete."
)
changed: list[str] = []


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    p = ROOT / rel
    old = p.read_text(encoding="utf-8") if p.exists() else ""
    if old != text:
        p.write_text(text, encoding="utf-8")
        changed.append(rel)


def replace_one(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing {label}: {old}")
    return text.replace(old, new, 1)


def replace_section(text: str, heading: str, next_heading: str, replacement: str) -> str:
    i = text.find(heading)
    if i < 0:
        raise SystemExit(f"missing section heading: {heading}")
    j = text.find(next_heading, i + len(heading))
    if j < 0:
        raise SystemExit(f"missing next section heading: {next_heading}")
    return text[:i] + replacement.rstrip() + "\n\n" + text[j:]


# Preconditions: live main must still be at the PDF 10–14 synchronized checkpoint.
idxp = "works/naam/transcription/index.json"
idx = json.loads(read(idxp))
for key, value in {
    "first_pass_pages_completed": 67,
    "verified_pages": 8,
    "visual_fidelity_passed_pages": 8,
    "historical_glyph_verified_pages": 10,
    "open_uncertainty_markers": 2,
}.items():
    if idx.get(key) != value:
        raise SystemExit(f"index precondition {key}: {idx.get(key)!r} != {value!r}")

batch = read("works/naam/transcription/parts/pdf-015-019.md")
for safeguard in [
    "pdf=15 printed=15 status=verified glyph=verified-final",
    "pdf=19 printed=19 status=verified glyph=verified-final",
    "பரவாயில்லே",
    "ஆடுமாடுகளா கவலைப்படும்?",
    "நீ யில்லா துலகினிலே",
    "அறிவிலிகாள்—பல",
    "பட்டினிப் பஞ்சம் தலை விரித்தாடுது",
    "மல் :- டேய்...அங்கே என்னடா சப்தம்?",
    "என்னே நடந்து போகச்சொல்றியா?",
    "பிடிச்சி இழுடா",
    "குமரன் மாடிக்கு ஓடுகிறான்",
]:
    if safeguard not in batch:
        raise SystemExit(f"batch safeguard missing: {safeguard}")

audit = read("works/naam/notes/verification-audit-pdf-015-019.md")
for safeguard in [
    "PDF 15–19 PASS / VERIFIED",
    "`தெய்வம`",
    "`தலை விரித்தாடுது`",
    "`மாடிக்கு`",
    "13/67",
]:
    if safeguard not in audit:
        raise SystemExit(f"audit safeguard missing: {safeguard}")

# Canonical index.
idx.update(
    status="verification-in-progress",
    draft_pages=54,
    verified_pages=13,
    visual_fidelity_passed_pages=13,
    historical_glyph_verified_pages=15,
    review_pages=54,
    open_uncertainty_markers=2,
    next_action=NEXT,
)
for part in idx.get("parts", []):
    if part.get("path") == "parts/pdf-015-019.md":
        part.update(status="verified", historical_glyph_status="verified-final", open_uncertainties=0)
write(idxp, json.dumps(idx, ensure_ascii=False, indent=2) + "\n")

# Work metadata.
rel = "works/naam/metadata.yaml"
t = read(rel)
for old, new, label in [
    ("  draft_pages: 59", "  draft_pages: 54", "metadata draft"),
    ("  verified_pages: 8", "  verified_pages: 13", "metadata verified"),
    ("  review_pages: 59", "  review_pages: 54", "metadata review"),
    ("  pages_verified: 10", "  pages_verified: 15", "metadata glyph verified"),
]:
    t = replace_one(t, old, new, label)

verification_block = '''verification_progress:
  current_audit_path: "notes/verification-audit-pdf-015-019.md"
  visual_fidelity_passed_pages: 13
  historical_glyph_final_verified_pages: 15
  dual_gate_verified_pages: 13
  held_pages:
    - pdf_page: 5
      reason: "physically damaged left beginning of introductory line"
    - pdf_page: 10
      reason: "physically damaged right-edge ending in Malaiyappan speech"
  resolved_uncertainties:
    - pdf_page: 9
      reading: "குறுக்கொடிய"
  next_pdf_range: "20-24"
'''
t = re.sub(
    r"verification_progress:\n.*?\nhistorical_glyph:\n",
    verification_block + "\nhistorical_glyph:\n",
    t,
    count=1,
    flags=re.S,
)
t = t.replace(
    "  visual_fidelity_audit: in-progress-through-pdf-014-8-of-67-pass",
    "  visual_fidelity_audit: in-progress-through-pdf-019-13-of-67-pass",
    1,
)
t = t.replace(
    "  historical_glyph_audit: final-verification-in-progress-10-of-67",
    "  historical_glyph_audit: final-verification-in-progress-15-of-67",
    1,
)
if "  batch_015_019_consequential_decodings:" not in t:
    anchor = "  batch_020_024_consequential_decoding:\n"
    block = '''  batch_015_019_consequential_decodings:
    - pdf_page: 15
      source_supported_unicode: "வாறேன்"
      family: "றா"
    - pdf_page: 16
      source_supported_unicode: "காடனை / வேடனை"
      family: "னை"
    - pdf_page: 18
      source_supported_unicode: "தன்னை"
      family: "னை"
'''
    if anchor not in t:
        raise SystemExit("metadata historical batch anchor missing")
    t = t.replace(anchor, block + anchor, 1)
t = re.sub(r'next_action: ".*?"\s*$', f'next_action: "{NEXT}"', t, count=1, flags=re.S)
write(rel, t)

# Historical-glyph audit.
rel = "works/naam/notes/historical-glyph-audit.md"
t = read(rel)
t = replace_one(
    t,
    "| PDF 15–19 | 5 | 5 | 0 | 5 | partial-first-pass |",
    "| PDF 15–19 | 5 | 5 | 5 | 0 | final-audit: 5 verified |",
    "glyph coverage 15-19",
)
t = replace_one(
    t,
    "| **Total** | **67** | **67** | **8** | **59** | **final-verification-in-progress** |",
    "| **Total** | **67** | **67** | **13** | **54** | **final-verification-in-progress** |",
    "glyph coverage total",
)
if "| 15 | 15 | historical `றா` cluster | `வாறேன்`" not in t:
    anchor = "| 21 | 21 | modern-lookalike"
    rows = '''| 15 | 15 | historical `றா` cluster | `வாறேன்` | `றா` | enlarged source pixels; occurrence-specific final review | **final-verified** |
| 16 | 16 | historical `னை` clusters | `காடனை` / `வேடனை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |
| 18 | 18 | historical `னை` cluster | `தன்னை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |
'''
    if anchor not in t:
        raise SystemExit("historical correction-log anchor missing")
    t = t.replace(anchor, rows + anchor, 1)
if "## PDF 15–19 final dual-gate audit" not in t:
    t += '''
## PDF 15–19 final dual-gate audit

- historical-glyph final PASS: **PDF 15–19 / 5 of 5**;
- visual-fidelity PASS: **PDF 15–19 / 5 of 5**;
- dual-gate canonical status: **5/5 VERIFIED**;
- scan-backed corrections include PDF 15 `பரவாயில்லே`, `ஆடுமாடுகளா கவலைப்படும்?`, `நீ யில்லா துலகினிலே`, `எண்ணெயை`; PDF 16 `அறிவிலிகாள்—பல` / line-final `தெய்வம`; PDF 17 `தலை விரித்தாடுது`; PDF 18 source speaker `மல்`; PDF 19 `என்னே`, `பிடிச்சி`, `மல்`, and `மாடிக்கு`;
- source scene-heading punctuation `காட்சி 8.` / `காட்சி 9.` is retained;
- no new source uncertainty is introduced; PDF 5 and PDF 10 remain the only physical-source-damage holds;
- full decision log: `verification-audit-pdf-015-019.md`.

Next final audit range: **PDF 20–24**.
'''
write(rel, t)

# Work README.
rel = "works/naam/README.md"
t = read(rel)
for old, new, label in [
    ("canonical Tamil verified pages: **8/67**", "canonical Tamil verified pages: **13/67**", "README verified"),
    ("visual fidelity audit: **in progress — 8/67 pages passed**", "visual fidelity audit: **in progress — 13/67 pages passed**", "README visual"),
    ("historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 10/67 final-verified**", "historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 15/67 final-verified**", "README glyph"),
    ("dual-gate verification pass is in progress: **8/67** pages are now verified", "dual-gate verification pass is in progress: **13/67** pages are now verified", "README checkpoint"),
    ("**8/67** canonical pages are dual-gate VERIFIED: PDF 6–9 and PDF 11–14.", "**13/67** canonical pages are dual-gate VERIFIED: PDF 6–9 and PDF 11–19.", "README verified range"),
]:
    t = replace_one(t, old, new, label)
verification_section = '''## Verification audit — through PDF 19

- PDF 6–9 and PDF 11–19: **dual-gate VERIFIED — 13/67 total**;
- PDF 5: **HOLD** for physically missing introductory-line beginning;
- PDF 10: **HOLD** for physically missing right-edge word ending after visible `வரைக்…`;
- visual-fidelity passed: **13/67**; historical-glyph final verified: **15/67**;
- open source uncertainties: **2** — PDF 5 and PDF 10;
- PDF 15–19 scan-backed corrections include `பரவாயில்லே`, `ஆடுமாடுகளா கவலைப்படும்?`, `நீ யில்லா துலகினிலே`, `எண்ணெயை`, `அறிவிலிகாள்—பல`, line-final `தெய்வம`, `தலை விரித்தாடுது`, source speaker `மல்`, `என்னே`, `பிடிச்சி`, and `மாடிக்கு`;
- PDF 16's explicit `[பாட்டு]` remains governed by the PDF 4 item-level Bharathiyar credit; PDF 18's lyrical duet remains authorship-not-adjudicated from that page alone;
- detailed logs: `notes/verification-audit-pdf-005-009.md`, `notes/verification-audit-pdf-010-014.md`, and `notes/verification-audit-pdf-015-019.md`.

**Next verification range:** PDF 20–24.
'''
t = replace_section(t, "## Verification audit — through PDF 14", "## Song / verse / performance structures mapped or confirmed so far", verification_section)
t = re.sub(r"## Exact next activity\n\n\*\*.*?\*\*\s*$", f"## Exact next activity\n\n**{NEXT}**\n", t, count=1, flags=re.S)
write(rel, t)

# Transcription README.
rel = "works/naam/transcription/README.md"
t = read(rel)
t = re.sub(r"- verified pages: \*\*\d+\*\*;", "- verified pages: **13**;", t, count=1)
t = re.sub(r"- separate visual-fidelity audit: \*\*.*?\*\*;", "- separate visual-fidelity audit: **in progress — 13/67 passed**;", t, count=1)
t = re.sub(r"- historical-glyph final verified pages: \*\*\d+/67\*\*;", "- historical-glyph final verified pages: **15/67**;", t, count=1)
t = re.sub(r"- open source uncertainty markers: \*\*\d+\*\*;", "- open source uncertainty markers: **2**;", t, count=1)
if "## Verification audit — PDF 15–19" not in t:
    marker = "## PDF 20–24 source decisions"
    block = '''## Verification audit — PDF 15–19

PDF 15–19 are **5/5 VERIFIED** after direct rendered-page comparison and final historical-glyph review. Current totals: visual **13/67**, glyph-final **15/67**, dual-gate verified **13/67**, open source uncertainties **2** (PDF 5 and PDF 10 only). Detailed log: `../notes/verification-audit-pdf-015-019.md`.

'''
    if marker not in t:
        raise SystemExit("transcription README PDF20 marker missing")
    t = t.replace(marker, block + marker, 1)
t = re.sub(r"## Next activity\n\n\*\*.*?\*\*\s*$", f"## Next activity\n\n**{NEXT}**\n", t, count=1, flags=re.S)
write(rel, t)

# Project handover.
rel = "works/naam/PROJECT_HANDOVER.md"
t = read(rel)
for old, new, label in [
    ("canonical Tamil verified: **8/67**", "canonical Tamil verified: **13/67**", "handover verified"),
    ("visual fidelity audit: **in progress — 8/67 passed**", "visual fidelity audit: **in progress — 13/67 passed**", "handover visual"),
    ("historical-glyph final verified: **10/67**", "historical-glyph final verified: **15/67**", "handover glyph"),
]:
    t = replace_one(t, old, new, label)
if "- `notes/verification-audit-pdf-015-019.md`." not in t:
    anchor = "- `notes/verification-audit-pdf-010-014.md`."
    if anchor not in t:
        raise SystemExit("handover audit-list anchor missing")
    t = t.replace(anchor, anchor + "\n- `notes/verification-audit-pdf-015-019.md`.", 1)
checkpoint = f'''## Verification checkpoint through PDF 19

- PDF 6–9 and PDF 11–19: **VERIFIED — 13/67 total**;
- PDF 5: physical left-edge introductory-line hold;
- PDF 10: physical right-edge word-ending hold after visible `வரைக்…`;
- visual-fidelity passed: **13/67**; glyph-final: **15/67**; dual-gate verified: **13/67**;
- open source uncertainties: **2**;
- PDF 15–19 adds no uncertainty and is fully verified;
- detailed audits: `notes/verification-audit-pdf-005-009.md`, `notes/verification-audit-pdf-010-014.md`, `notes/verification-audit-pdf-015-019.md`.

## Exact next activity

> **{NEXT}**
'''
if "## Verification checkpoint through PDF 14" in t:
    # Replace from old checkpoint to EOF because it contains the exact-next block.
    i = t.find("## Verification checkpoint through PDF 14")
    t = t[:i] + checkpoint
else:
    t = re.sub(r"## Exact next activity\n\n> \*\*.*?\*\*\s*$", checkpoint, t, count=1, flags=re.S)
write(rel, t)

# Next-chat prompt.
write(
    "works/naam/NEXT_CHAT_PROMPT.md",
    f'''# Next Chat Prompt — நாம்

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

Current durable checkpoint:

- source intake / mapping: **complete / verified**;
- canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages**;
- visual-fidelity passed: **13/67**;
- historical-glyph first-pass checked: **67/67**;
- historical-glyph final verified: **15/67**;
- dual-gate canonical verified: **13/67** — PDF 6–9 and PDF 11–19;
- open source uncertainties: **2** — PDF 5 damaged introductory beginning and PDF 10 damaged right-edge word ending;
- PDF 9's former uncertainty is resolved as source-visible `குறுக்கொடிய`;
- structured derivatives / English: **blocked pending verified Tamil**.

## Controlling source

Resolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; canonical screenplay PDF **5–71**.

## Verification checkpoint

PDF 6–9 and PDF 11–19 are frozen as VERIFIED absent genuinely new direct-source evidence. PDF 5 and PDF 10 remain physical-source-damage holds and must not be reconstructed.

PDF 15–19 scan-backed corrections include `பரவாயில்லே`, `ஆடுமாடுகளா கவலைப்படும்?`, `நீ யில்லா துலகினிலே`, `எண்ணெயை`, PDF 16 `அறிவிலிகாள்—பல` / line-final `தெய்வம`, PDF 17 `தலை விரித்தாடுது`, PDF 18 source label `மல்`, and PDF 19 `என்னே`, `பிடிச்சி`, `மல்`, `மாடிக்கு`. Source headings `காட்சி 8.` and `காட்சி 9.` retain their printed punctuation.

Detailed audit: `works/naam/notes/verification-audit-pdf-015-019.md`.

## Exact next activity

> **{NEXT}**
''',
)

# Structured root data.
rel = "data/works.json"
data = json.loads(read(rel))
naam = next(x for x in data if x.get("id") == "naam")
naam.update(
    canonical_tamil_transcription="verification-in-progress",
    visual_fidelity_audit="in-progress-through-pdf-019-13-of-67",
    historical_glyph_audit="final-verification-in-progress-15-of-67",
    canonical_tamil_draft_pages=54,
    canonical_tamil_verified_pages=13,
    canonical_tamil_review_pages=54,
    canonical_tamil_open_uncertainty_markers=2,
    historical_glyph_pages_verified=15,
    visual_fidelity_passed_pages=13,
    canonical_tamil_current_verification_path="works/naam/notes/verification-audit-pdf-015-019.md",
    next_action=NEXT,
)
write(rel, json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")

# Root/master mirrors: limit replacements to values established at the prior Naam checkpoint.
for rel in [
    "README.md",
    "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
    "docs/STATUS_CONSISTENCY_AUDIT.md",
]:
    t = read(rel)
    t = t.replace("verified **8/67**", "verified **13/67**")
    t = t.replace("verified pages: **8/67**", "verified pages: **13/67**")
    t = t.replace("visual-fidelity audit: **in progress — 8/67 passed**", "visual-fidelity audit: **in progress — 13/67 passed**")
    t = t.replace("visual-fidelity audit: **in progress — 8/67**", "visual-fidelity audit: **in progress — 13/67**")
    t = t.replace("historical-glyph first-pass checked / final verified: **67/67 / 10/67**", "historical-glyph first-pass checked / final verified: **67/67 / 15/67**")
    t = t.replace("final glyph-verified: **10/67**", "final glyph-verified: **15/67**")
    t = t.replace("PDF 15–19", "PDF 20–24") if "Next verification" in t else t
    t = t.replace(
        "Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 15–19. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen PDF 6–9 or PDF 11–14 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain explicit physical-source-damage holds. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete.",
        NEXT,
    )
    write(rel, t)

print("Synchronized Naam verification PDF 15–19:")
for rel in changed:
    print("-", rel)
