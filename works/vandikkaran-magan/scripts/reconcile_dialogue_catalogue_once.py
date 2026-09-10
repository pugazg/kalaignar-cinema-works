#!/usr/bin/env python3
"""One-time reconciliation of the Vandikkaran Magan registry after dialogue closure."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
p = ROOT / "data" / "works.json"
works = json.loads(p.read_text(encoding="utf-8"))
item = next(x for x in works if x.get("id") == "vandikkaran-magan")
sd = item["structured_derivatives"]
assert sd["dialogue_index"] == "complete-verified"
assert sd["dialogue_records"] == 744
assert sd["dialogue_distinct_exact_speaker_labels"] == 38
assert sd["dialogue_qa"] == "PASS"

item.update({
    "canonical_tamil_first_pass": "complete-87-of-87",
    "canonical_tamil_scope_pdf_pages": "4-90",
    "canonical_tamil_total_pages": 87,
    "canonical_tamil_first_pass_pages_completed": 87,
    "canonical_tamil_first_pass_pdf_range_completed": "4-90",
    "canonical_tamil_first_pass_current_through_pdf": 90,
    "canonical_tamil_first_pass_current_through_printed": 86,
    "canonical_tamil_draft_pages": 0,
    "canonical_tamil_verified_pages": 87,
    "canonical_tamil_review_pages": 0,
    "canonical_tamil_open_uncertainty_markers": 0,
    "visual_fidelity_audit": "complete-87-of-87-through-pdf-90",
    "historical_glyph_audit": "complete-87-of-87-through-pdf-90",
    "historical_glyph_first_pass_checked_pages": 87,
    "historical_glyph_final_verified_pages": 87,
    "tamil_transcription": "complete-verified",
    "tamil_first_pass_complete": True,
    "tamil_transcription_through_pdf_page": 90,
    "tamil_transcription_through_printed_page": 86,
    "tamil_transcription_draft_pages": 0,
    "tamil_transcription_verified_pages": 87,
    "tamil_transcription_review_pages": 0,
    "tamil_fidelity_audit": "complete",
    "canonical_range_fidelity_audit_complete": True,
    "total_canonical_pages": 87,
    "total_verified_pages": 87,
    "total_review_pages": 0,
})

p.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status":"PASS","work":"vandikkaran-magan","canonical_pages":87,"dialogues":744,"next":"character-index"}))
