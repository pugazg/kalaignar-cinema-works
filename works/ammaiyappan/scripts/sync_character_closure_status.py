#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def main():
    char_idx_path = ROOT / "characters/index.json"
    char_idx = json.loads(char_idx_path.read_text(encoding="utf-8"))
    assert char_idx["status"] == "complete-verified-reconciled"
    assert char_idx["dialogue_records_source"] == 1024
    assert char_idx["distinct_source_labels"] == 62
    assert char_idx["entity_count"] == 26
    assert char_idx["unresolved_entities"] == 0
    assert char_idx["remaining_unmapped_records"] == 0

    # Work README.
    p = ROOT / "README.md"
    text = p.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "This closes only the **canonical Tamil first pass and assembly**. It does not close the remaining PDF 95–109 dual verification.",
        "Canonical Tamil, scene segmentation, dialogue indexing, and character/entity indexing are now closed. The next derivative phase is English translation/reconciliation.",
        "README historical gate sentence",
    )
    text = replace_once(text, "| Dialogue index | **READY — next phase** |", "| Dialogue index | **complete-source-role-resolved — 1,024/1,024 downstream units** |", "README dialogue row")
    text = replace_once(text, "| Character index | blocked pending dialogue-index closure |", "| Character/entity index | **complete-verified-reconciled — 26 entities / 62 labels / 1,024 units** |", "README character row")
    text = replace_once(text, "| English translation / reader | blocked by derivative gate order |", "| English translation / reader | **READY — next phase** |", "README English row")
    text = replace_once(
        text,
        "**Begin dialogue indexing from `scenes/index.json` and the 63 verified scene files.** Preserve each source speaker label exactly as printed, record archive scene ID + PDF provenance for each speech turn, and keep character-name normalization/alias resolution for the later character-index phase.",
        "**Begin English translation/reconciliation from the frozen 105/105 Tamil source plus the completed scene, dialogue, and character/entity derivatives.** Preserve source structure and exact Tamil linkage; do not modify canonical Tamil or dialogue evidence unless a new source-backed correction is independently established.",
        "README next activity",
    )
    p.write_text(text, encoding="utf-8")

    # Work handover.
    p = ROOT / "PROJECT_HANDOVER.md"
    text = p.read_text(encoding="utf-8")
    old_gates = """- dialogue index: **READY — next phase**;
- character index: blocked pending dialogue-index closure;
- song/performance authorship gate: not-started;
- English / reader: blocked by derivative gate order."""
    new_gates = """- dialogue index: **complete-source-role-resolved — 1,024/1,024 downstream units**;
- character/entity index: **complete-verified-reconciled — 26 entities / 62 exact labels / 1,024 units**;
- song/performance authorship gate: not-started;
- English / reader: **READY — next phase**."""
    text = replace_once(text, old_gates, new_gates, "handover phase gates")
    text = replace_once(
        text,
        "> **Build the dialogue index from the 63 verified scene-text derivatives. Preserve the exact printed speaker label for every dialogue turn, attach archive scene ID and source PDF provenance, do not normalize aliases/character identities in this phase, and run dialogue coverage/ownership QA before opening character indexing.**",
        "> **Begin English translation/reconciliation from the closed Tamil/scene/dialogue/character evidence layers. Keep exact Tamil provenance and source structure; do not reopen canonical Tamil or dialogue evidence without new scan-backed authority.**",
        "handover first next activity",
    )
    text = replace_once(
        text,
        "> **Build the character/entity index from `dialogues/final-index.json`, the 1009 explicit dialogue records, the 15 source-role-resolved dialogue supplements, and the 63 verified scene derivatives. Preserve every exact speaker label as provenance; perform alias/entity reconciliation only in the new character/entity layer, never by rewriting the dialogue records.**",
        "> **Begin English translation/reconciliation from the closed Tamil/scene/dialogue/character evidence layers. Use `characters/index.json` only as a derivative identity aid; exact Tamil/dialogue labels remain the provenance authority.**",
        "handover second next activity",
    )
    closure = """

## Character/entity closure — FINAL QA PASS

- downstream dialogue units dispositioned: **1,024/1,024**;
- exact source speaker labels dispositioned: **62/62**;
- stable entities / role categories: **26**;
- verified entities: **26**;
- review entities: **0**;
- unresolved entities: **0**;
- record-aware exact labels: **2** — `முத்`, `தன`;
- record-aware units: **187**;
- `முத்`: **80 → முத்தன் / 97 → முத்தாயி**;
- `தன`: **1 → தனபதி / 9 → தனவணிகர்**;
- dialogue records modified by character reconciliation: **no**;
- character index: `characters/index.json`;
- complete entities: `characters/entities.json`;
- exact-label disposition: `characters/labels-inventory.json`;
- record-aware assignments: `characters/record-aware-dispositions.json`;
- character/entity build commit: `e670816876c4f02c0bebe283c2c9bfc0de93fcc9`.

### Exact next activity

> **Begin English translation/reconciliation. Translate only from the frozen verified Tamil evidence, preserve scene/dialogue provenance, and use the character/entity layer to resolve identity without normalizing the Tamil source.**
"""
    if "## Character/entity closure — FINAL QA PASS" not in text:
        text = text.rstrip() + closure + "\n"
    p.write_text(text, encoding="utf-8")

    # Metadata — replace the already-existing stale structured-derivative/status block.
    p = ROOT / "metadata.yaml"
    text = p.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '  next_action: "Begin dialogue indexing from the 63/63 verified scene-text derivatives; preserve exact speaker labels and scene/page provenance."',
        '  next_action: "Begin English translation/reconciliation from the frozen verified Tamil plus completed scene/dialogue/character derivatives."',
        "metadata transcription next action",
    )
    old_structured = """structured_derivatives:
  scene_index: complete-verified-63-of-63
  scene_text_derivatives: complete-verified-63-of-63
  scene_index_path: "scenes/index.json"
  scene_boundary_ownership_qa_path: "notes/scene-boundary-ownership-qa.md"
  scene_derivative_commit: "6a764137616879d08f5a1ff14431caafa87b11eb"
  dialogue_index: ready
  character_index: blocked-pending-dialogue-index
  song_authorship_mapping: not-started
  english_translation: blocked
  reader_export: blocked
  reading_room_integration: blocked
"""
    new_structured = """structured_derivatives:
  scene_index: complete-verified-63-of-63
  scene_text_derivatives: complete-verified-63-of-63
  scene_index_path: "scenes/index.json"
  scene_boundary_ownership_qa_path: "notes/scene-boundary-ownership-qa.md"
  scene_derivative_commit: "6a764137616879d08f5a1ff14431caafa87b11eb"
  dialogue_index: complete-source-role-resolved-1024-of-1024
  dialogue_index_path: "dialogues/final-index.json"
  explicit_colon_records: 1009
  source_role_supplements: 15
  exact_source_speaker_labels: 62
  character_entity_index: complete-verified-reconciled
  character_entity_index_path: "characters/index.json"
  entity_count: 26
  verified_entities: 26
  record_aware_labels: 2
  record_aware_records: 187
  unresolved_entities: 0
  unresolved_records: 0
  dialogue_records_modified_by_character_layer: false
  song_authorship_mapping: not-started
  english_translation: ready-next-phase
  reader_export: blocked-pending-english
  reading_room_integration: blocked-pending-english
"""
    text = replace_once(text, old_structured, new_structured, "metadata structured derivatives")
    old_status = """status:
  duplicate_work_check: complete
  source_intake: complete
  whole_scan_inspection: complete
  structural_mapping: verified
  canonical_tamil_first_pass: draft-complete-105-of-105
  full_text_assembly: complete-pass
  boundary_qa: pass
  visual_fidelity_audit: complete-verified-105-of-105
  historical_glyph_audit: complete-verified-105-of-105
  final_tamil_verification: complete-verified-105-of-105-dual-gate
  scene_derivatives: complete-verified-63-of-63
  dialogue_index: blocked-pending-scene-text-derivatives
  character_index: blocked-pending-dialogue-index
  song_authorship_gate: not-started
  english_translation: blocked
  reader_export: blocked
  reading_room_integration: blocked

next_action: "Begin dialogue indexing from the 63/63 verified scene-text derivatives; preserve exact source speaker labels, archive scene IDs and page provenance. Do not normalize character names yet."
"""
    new_status = """status:
  duplicate_work_check: complete
  source_intake: complete
  whole_scan_inspection: complete
  structural_mapping: verified
  canonical_tamil_first_pass: draft-complete-105-of-105
  full_text_assembly: complete-pass
  boundary_qa: pass
  visual_fidelity_audit: complete-verified-105-of-105
  historical_glyph_audit: complete-verified-105-of-105
  final_tamil_verification: complete-verified-105-of-105-dual-gate
  scene_derivatives: complete-verified-63-of-63
  dialogue_index: complete-source-role-resolved-1024-of-1024
  character_entity_index: complete-verified-reconciled-26-entities-62-labels-1024-units
  song_authorship_gate: not-started
  english_translation: ready-next-phase
  reader_export: blocked-pending-english
  reading_room_integration: blocked-pending-english

next_action: "Begin English translation/reconciliation from the frozen verified Tamil plus completed scene/dialogue/character evidence layers; preserve exact source provenance."
"""
    text = replace_once(text, old_status, new_status, "metadata status and next action")
    p.write_text(text, encoding="utf-8")

    # Dialogue final index: close character gate, no dialogue records touched.
    p = ROOT / "dialogues/final-index.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    assert doc["total_dialogue_units_for_downstream_indexing"] == 1024
    assert doc["character_entity_gate"] in {"unlocked", "complete-verified-reconciled"}
    doc["character_entity_gate"] = "complete-verified-reconciled"
    doc["character_entity_index"] = "../characters/index.json"
    doc["next_activity"] = "Begin English translation/reconciliation from frozen verified Tamil and completed structured derivatives."
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Character compact index: synchronization precondition is now satisfied.
    p = ROOT / "characters/index.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    doc["status_synchronized"] = True
    doc["next_activity"] = "Begin English translation/reconciliation from the frozen verified Tamil, scene, dialogue, and character/entity layers."
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("AMMAYAPPAN CHARACTER CLOSURE STATUS SYNCHRONIZED")


if __name__ == "__main__":
    main()
