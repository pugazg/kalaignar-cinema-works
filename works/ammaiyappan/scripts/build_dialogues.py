#!/usr/bin/env python3
"""Build immutable source-preserving dialogue records for Ammayappan.

Authority is the 63 complete-verified scene derivative layer.  The builder keeps
speaker labels exactly as printed/transcribed, never performs alias expansion,
and treats a page break as provenance rather than an utterance boundary.

One explicit ``speaker : text`` source line starts one immutable dialogue record.
Subsequent ordinary unlabelled text remains with that record until a hard
structural boundary (new speaker label, scene heading, stage direction,
separator, or non-source metadata).  Ordinary text that has no active speaker is
not guessed: it is written to the unlabelled-block audit.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "scenes"
DIALOGUES = ROOT / "dialogues"
RECORDS = DIALOGUES / "records"
NOTES = ROOT / "notes"

SOURCE_RE = re.compile(
    r"^<!-- source: pdf=(?P<pdf>\d+)"
    r"(?: printed=(?P<printed>\d+)| logical_printed=(?P<logical>\d+))?"
)
DIALOGUE_RE = re.compile(r"^(?P<label>[^:#\[\]<>\n]{1,60}?)\s+:\s+(?P<text>\S.*)$")
HEADING_RE = re.compile(r"^#{1,6}\s+")
SEPARATORS = {"★", "★★★", "* * *", "---", "***", "___"}


def anchor_from(line: str) -> dict[str, int | None] | None:
    m = SOURCE_RE.match(line)
    if not m:
        return None
    printed = m.group("printed") or m.group("logical")
    return {
        "pdf_page": int(m.group("pdf")),
        "printed_page": int(printed) if printed else None,
    }


def is_comment(line: str) -> bool:
    return line.startswith("<!--") and line.endswith("-->")


def append_text_piece(obj: dict[str, Any], page: dict[str, Any], text: str, blank_before: bool) -> None:
    """Append exact lexical text to a page segment, preserving logical blank separation."""
    assert text
    assert page is not None
    pdf = page["pdf_page"]
    printed = page["printed_page"]
    segments = obj.setdefault("_segments", [])
    if not segments or segments[-1]["pdf_page"] != pdf:
        segments.append({"pdf_page": pdf, "printed_page": printed, "lines": [text]})
        return
    if blank_before and segments[-1]["lines"] and segments[-1]["lines"][-1] != "":
        segments[-1]["lines"].append("")
    segments[-1]["lines"].append(text)


def finalize_segments(obj: dict[str, Any]) -> None:
    segs = obj.pop("_segments")
    page_segments = []
    for seg in segs:
        # Strip only derivative blank padding; lexical source lines are unchanged.
        lines = list(seg["lines"])
        while lines and lines[0] == "":
            lines.pop(0)
        while lines and lines[-1] == "":
            lines.pop()
        text = "\n".join(lines)
        assert text
        page_segments.append(
            {
                "pdf_page": seg["pdf_page"],
                "printed_page": seg["printed_page"],
                "text": text,
            }
        )
    obj["page_provenance"] = [
        {"pdf_page": s["pdf_page"], "printed_page": s["printed_page"]}
        for s in page_segments
    ]
    obj["text"] = "\n".join(s["text"] for s in page_segments)
    if len(page_segments) > 1:
        obj["page_segments"] = page_segments


def hard_structure_kind(s: str, in_square_direction: bool) -> tuple[str | None, bool]:
    """Return (kind, new_in_square_direction) for hard structural source lines."""
    if in_square_direction:
        return "stage_direction_square_continuation", not s.endswith("]")
    if s.startswith("["):
        return "stage_direction_square", not s.endswith("]")
    if HEADING_RE.match(s):
        return "heading", False
    if s in SEPARATORS:
        return "separator", False
    if len(s) >= 2 and s.startswith("(") and s.endswith(")"):
        return "stage_direction_parenthetical", False
    return None, False


def build_scene(scene: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    scene_id = scene["scene_id"]
    scene_file = scene["file"]
    lines = (SCENES / scene_file).read_text(encoding="utf-8").splitlines()
    records: list[dict[str, Any]] = []
    unowned: list[dict[str, Any]] = []
    active: dict[str, Any] | None = None
    active_unowned: dict[str, Any] | None = None
    current_page: dict[str, Any] | None = None
    pending_blank = False
    unowned_pending_blank = False
    in_square_direction = False
    stats = Counter()
    explicit_source_lines: list[int] = []
    continuation_source_lines: list[int] = []
    unowned_source_lines: list[int] = []
    structural_source_lines: list[int] = []

    def flush_dialogue() -> None:
        nonlocal active, pending_blank
        if active is None:
            pending_blank = False
            return
        finalize_segments(active)
        active.pop("_start_line", None)
        active.pop("_last_line", None)
        records.append(active)
        active = None
        pending_blank = False

    def flush_unowned() -> None:
        nonlocal active_unowned, unowned_pending_blank
        if active_unowned is None:
            unowned_pending_blank = False
            return
        finalize_segments(active_unowned)
        active_unowned.pop("_start_line", None)
        active_unowned.pop("_last_line", None)
        active_unowned["block_id"] = f"{scene_id}-u{len(unowned)+1:03d}"
        unowned.append(active_unowned)
        active_unowned = None
        unowned_pending_blank = False

    for line_no, raw in enumerate(lines, 1):
        s = raw.strip()

        anchor = anchor_from(s)
        if anchor:
            assert 5 <= anchor["pdf_page"] <= 109
            assert anchor["printed_page"] is not None
            current_page = anchor
            # Blank padding around derivative page anchors is not source dialogue.
            pending_blank = False
            unowned_pending_blank = False
            stats["source_anchor"] += 1
            continue

        if not s:
            if active is not None:
                pending_blank = True
            if active_unowned is not None:
                unowned_pending_blank = True
            stats["blank"] += 1
            continue

        if is_comment(s):
            # Non-source comments are derivative metadata and therefore hard boundaries.
            flush_dialogue()
            flush_unowned()
            stats["metadata_comment"] += 1
            continue

        kind, next_square = hard_structure_kind(s, in_square_direction)
        if kind:
            flush_dialogue()
            flush_unowned()
            in_square_direction = next_square
            structural_source_lines.append(line_no)
            stats[kind] += 1
            continue
        in_square_direction = False

        dm = DIALOGUE_RE.match(s)
        if dm:
            assert current_page is not None, (scene_id, line_no, s)
            flush_dialogue()
            flush_unowned()
            label = dm.group("label").strip()
            text = dm.group("text")
            active = {
                "id": f"{scene_id}-d{len(records)+1:03d}",
                "archive_scene_id": scene_id,
                "archive_scene_ordinal": scene["ordinal"],
                "source_scene_number": None,
                "source_heading": scene["heading"],
                "speaker_label": label,
                "source_scene_file": scene_file,
                "_segments": [],
                "_start_line": line_no,
                "_last_line": line_no,
            }
            append_text_piece(active, current_page, text, False)
            explicit_source_lines.append(line_no)
            stats["explicit_dialogue_start"] += 1
            continue

        # Ordinary source text.  It is a continuation only when a speaker-labelled
        # utterance is currently active; otherwise preserve it in an explicit audit.
        assert current_page is not None, (scene_id, line_no, s)
        if active is not None:
            append_text_piece(active, current_page, s, pending_blank)
            active["_last_line"] = line_no
            pending_blank = False
            continuation_source_lines.append(line_no)
            stats["owned_unlabelled_continuation"] += 1
        else:
            if active_unowned is None:
                active_unowned = {
                    "archive_scene_id": scene_id,
                    "archive_scene_ordinal": scene["ordinal"],
                    "source_heading": scene["heading"],
                    "source_scene_file": scene_file,
                    "reason": "ordinary source text without an active explicit speaker label",
                    "_segments": [],
                    "_start_line": line_no,
                    "_last_line": line_no,
                }
            append_text_piece(active_unowned, current_page, s, unowned_pending_blank)
            active_unowned["_last_line"] = line_no
            unowned_pending_blank = False
            unowned_source_lines.append(line_no)
            stats["unowned_ordinary_text"] += 1

    flush_dialogue()
    flush_unowned()
    assert not in_square_direction, f"Unclosed square stage direction in {scene_file}"

    # Stable per-scene IDs after all flushes.
    for i, rec in enumerate(records, 1):
        assert rec["id"] == f"{scene_id}-d{i:03d}"
    for i, block in enumerate(unowned, 1):
        assert block["block_id"] == f"{scene_id}-u{i:03d}"

    scene_qa = {
        "scene_id": scene_id,
        "scene_file": scene_file,
        "dialogue_records": len(records),
        "unowned_blocks": len(unowned),
        "unowned_source_lines": len(unowned_source_lines),
        "owned_unlabelled_continuation_lines": len(continuation_source_lines),
        "explicit_dialogue_source_lines": len(explicit_source_lines),
        "structural_source_lines": len(structural_source_lines),
        "classification_counts": dict(sorted(stats.items())),
    }
    return records, unowned, scene_qa


def schema() -> dict[str, Any]:
    provenance = {
        "type": "object",
        "required": ["pdf_page", "printed_page"],
        "properties": {
            "pdf_page": {"type": "integer", "minimum": 5, "maximum": 109},
            "printed_page": {"type": "integer", "minimum": 3, "maximum": 107},
        },
        "additionalProperties": False,
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "ammaiyappan-dialogue-record.schema.json",
        "title": "Ammayappan dialogue record",
        "type": "object",
        "required": [
            "id", "archive_scene_id", "archive_scene_ordinal", "source_scene_number",
            "source_heading", "speaker_label", "text", "page_provenance", "source_scene_file"
        ],
        "properties": {
            "id": {"type": "string", "pattern": "^ammaiyappan-s[0-9]{3}-d[0-9]{3}$"},
            "archive_scene_id": {"type": "string", "pattern": "^ammaiyappan-s[0-9]{3}$"},
            "archive_scene_ordinal": {"type": "integer", "minimum": 1, "maximum": 63},
            "source_scene_number": {"type": "null", "description": "The booklet does not provide a complete printed scene-number system."},
            "source_heading": {"type": "string", "minLength": 1},
            "speaker_label": {"type": "string", "minLength": 1, "description": "Exact source label before the colon; never expanded or normalized."},
            "text": {"type": "string", "minLength": 1, "description": "Verified utterance text after the source label, including unlabelled continuation text until a hard structural boundary. Cross-page segment texts are joined with one newline."},
            "page_provenance": {"type": "array", "minItems": 1, "uniqueItems": True, "items": provenance},
            "page_segments": {
                "type": "array", "minItems": 2,
                "description": "Present when one immutable utterance contains source text on more than one PDF page.",
                "items": {
                    "type": "object",
                    "required": ["pdf_page", "printed_page", "text"],
                    "properties": {
                        "pdf_page": {"type": "integer", "minimum": 5, "maximum": 109},
                        "printed_page": {"type": "integer", "minimum": 3, "maximum": 107},
                        "text": {"type": "string", "minLength": 1},
                    },
                    "additionalProperties": False,
                },
            },
            "source_scene_file": {"type": "string", "pattern": "^scene-[0-9]{3}\\.md$"},
        },
        "allOf": [
            {
                "if": {"properties": {"page_provenance": {"minItems": 2}}},
                "then": {"required": ["page_segments"]},
            }
        ],
        "additionalProperties": False,
    }


def main() -> None:
    scene_index = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    preflight = json.loads((NOTES / "dialogue-index-preflight.json").read_text(encoding="utf-8"))
    assert scene_index["status"] == "complete-verified"
    assert scene_index["canonical_tamil_gate"] == "105/105-dual-gate-complete-verified"
    assert scene_index["archive_scene_count"] == 63
    scenes = scene_index["scene_records"]
    assert len(scenes) == 63
    assert preflight["scene_count"] == 63
    assert preflight["explicit_colon_dialogue_candidates"] == 910

    DIALOGUES.mkdir(exist_ok=True)
    RECORDS.mkdir(exist_ok=True)
    NOTES.mkdir(exist_ok=True)

    all_records: list[dict[str, Any]] = []
    all_unowned: list[dict[str, Any]] = []
    scene_qas: list[dict[str, Any]] = []
    scene_record_counts: dict[str, int] = {}

    for scene in scenes:
        records, unowned, qa = build_scene(scene)
        all_records.extend(records)
        all_unowned.extend(unowned)
        scene_qas.append(qa)
        scene_record_counts[scene["scene_id"]] = len(records)
        (RECORDS / f"scene-{scene['ordinal']:03d}.json").write_text(
            json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    # Primary invariant: one immutable record per explicit source label.
    assert len(all_records) == preflight["explicit_colon_dialogue_candidates"] == 910
    assert scene_record_counts == preflight["scene_dialogue_candidate_counts"]

    label_counts = Counter(r["speaker_label"] for r in all_records)
    expected_label_counts = {
        r["speaker_label"]: r["count"] for r in preflight["exact_speaker_labels"]
    }
    assert dict(label_counts) == expected_label_counts
    assert len(label_counts) == preflight["distinct_exact_speaker_labels"] == 35

    ids = [r["id"] for r in all_records]
    assert len(ids) == len(set(ids))
    assert all(r["source_scene_number"] is None for r in all_records)
    assert all(5 <= p["pdf_page"] <= 109 for r in all_records for p in r["page_provenance"])
    assert all(3 <= p["printed_page"] <= 107 for r in all_records for p in r["page_provenance"])

    multi_page = [r for r in all_records if len(r["page_provenance"]) > 1]
    for r in multi_page:
        assert "page_segments" in r
        assert len(r["page_segments"]) == len(r["page_provenance"])
        assert r["text"] == "\n".join(s["text"] for s in r["page_segments"])

    # The 19 heuristic candidates were reviewed against the verified scene text.
    # Require every one to land inside a single generated multi-page record with
    # both lexical sides present.  This prevents a future builder regression from
    # truncating the continuation at the page anchor.
    cross_page_review = []
    for c in preflight["cross_page_continuation_candidates"]:
        matches = [
            r for r in all_records
            if r["archive_scene_id"] == c["scene_id"]
            and r["speaker_label"] == c["speaker_label"]
            and c["before"] in r["text"]
            and c["after"] in r["text"]
            and c["from_pdf"] in [p["pdf_page"] for p in r["page_provenance"]]
            and c["to_pdf"] in [p["pdf_page"] for p in r["page_provenance"]]
        ]
        assert len(matches) == 1, (c, [m["id"] for m in matches])
        cross_page_review.append({
            "scene_id": c["scene_id"],
            "from_pdf": c["from_pdf"],
            "to_pdf": c["to_pdf"],
            "speaker_label": c["speaker_label"],
            "dialogue_id": matches[0]["id"],
            "decision": "same-utterance-continuation-confirmed",
        })
    assert len(cross_page_review) == 19

    # All 14 conservative dash candidates were source-reviewed: they are lexical
    # text containing a dash, not an alternate speaker delimiter.  They must never
    # become explicit speaker labels.
    dash_review = []
    for c in preflight["anomalous_delimiter_candidates"]:
        assert not DIALOGUE_RE.match(c["raw"])
        dash_review.append({
            "scene_id": c["scene_id"],
            "pdf_page": c["pdf_page"],
            "line": c["line"],
            "raw": c["raw"],
            "decision": "not-a-speaker-label",
        })
    assert len(dash_review) == 14

    total_continuation_lines = sum(q["owned_unlabelled_continuation_lines"] for q in scene_qas)
    total_unowned_lines = sum(q["unowned_source_lines"] for q in scene_qas)
    total_unowned_blocks = sum(q["unowned_blocks"] for q in scene_qas)

    dialogue_index = {
        "work_id": "ammaiyappan",
        "status": "review-ready",
        "authority": "63 complete-verified archive-only scene derivatives",
        "canonical_tamil_gate": "105/105-dual-gate-complete-verified",
        "source_numbered_scenes": False,
        "archive_scene_count": 63,
        "dialogue_record_count": len(all_records),
        "distinct_exact_speaker_labels": len(label_counts),
        "multi_page_dialogue_records": len(multi_page),
        "scene_record_counts": scene_record_counts,
        "zero_dialogue_scenes": [sid for sid, n in scene_record_counts.items() if n == 0],
        "schema": "schema.json",
        "records_directory": "records/",
        "unlabelled_block_audit": "../notes/unlabelled-block-audit.json",
        "qa": "../notes/dialogue-index-qa.json",
        "policy": {
            "immutable_unit": "one explicit speaker-labelled utterance",
            "speaker_label": "exact source label before colon; no normalization",
            "page_break": "provenance boundary, not utterance boundary",
            "hard_utterance_boundaries": ["new explicit speaker label", "scene heading", "stage direction", "separator", "non-source metadata"],
            "unlabelled_text_without_active_speaker": "excluded and inventoried; never guessed",
            "character_alias_resolution": "deferred",
        },
    }
    (DIALOGUES / "index.json").write_text(
        json.dumps(dialogue_index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (DIALOGUES / "schema.json").write_text(
        json.dumps(schema(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    readme = f"""# அம்மையப்பன் — immutable dialogue layer

Status: **REVIEW READY**

Authority: the **63/63 complete-verified archive-only scene derivatives**, themselves derived only after the **105/105 dual-gate Tamil source verification** closed.

## Current build

- archive scenes represented: **63/63**
- immutable dialogue records: **{len(all_records)}**
- distinct exact speaker-label strings: **{len(label_counts)}**
- multi-page immutable utterances: **{len(multi_page)}**
- zero-dialogue scene files retained as empty arrays: **{len(dialogue_index['zero_dialogue_scenes'])}**
- source scene numbers invented: **0**
- alias/name normalization: **0**

Each explicit source `speaker : text` line starts one record.  Ordinary unlabelled text that follows remains part of that utterance until a hard structural boundary.  A physical PDF-page transition does not end an utterance; multi-page records carry `page_segments` and page provenance.

Text that occurs with no active explicit speaker is **not assigned by inference**.  It is preserved separately in `../notes/unlabelled-block-audit.json` for source-role review.

The character/entity index remains blocked until the unlabelled-block audit and final dialogue QA are closed.
"""
    (DIALOGUES / "README.md").write_text(readme, encoding="utf-8")

    unowned_payload = {
        "work_id": "ammaiyappan",
        "phase": "unlabelled-block-audit",
        "status": "review-required" if all_unowned else "pass-no-unowned-blocks",
        "authority": "63 complete-verified scene derivatives",
        "block_count": len(all_unowned),
        "source_line_count": total_unowned_lines,
        "policy": "No ordinary source text without an active explicit speaker label is assigned to a dialogue record by inference.",
        "blocks": all_unowned,
    }
    (NOTES / "unlabelled-block-audit.json").write_text(
        json.dumps(unowned_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    unowned_md = [
        "# அம்மையப்பன் — unlabelled source-block audit",
        "",
        f"Status: **{'REVIEW REQUIRED' if all_unowned else 'PASS'}**",
        "",
        f"- unlabelled ordinary blocks: **{len(all_unowned)}**",
        f"- source lines in those blocks: **{total_unowned_lines}**",
        "- policy: never infer a speaker for these blocks during immutable dialogue extraction.",
        "",
    ]
    if all_unowned:
        unowned_md.extend(["## Inventory", ""])
        for b in all_unowned:
            pages = ", ".join(str(p["pdf_page"]) for p in b["page_provenance"])
            preview = b["text"].replace("\n", " / ")
            if len(preview) > 180:
                preview = preview[:177] + "..."
            unowned_md.append(f"- `{b['block_id']}` — `{b['archive_scene_id']}` — PDF {pages}: {preview}")
    else:
        unowned_md.append("No unowned ordinary source text was found.")
    (NOTES / "unlabelled-block-audit.md").write_text("\n".join(unowned_md) + "\n", encoding="utf-8")

    qa_status = "review-required" if all_unowned else "pass"
    qa = {
        "work_id": "ammaiyappan",
        "phase": "dialogue-index-qa",
        "status": qa_status,
        "scene_coverage": "63/63",
        "explicit_source_labels_expected": 910,
        "immutable_dialogue_records": len(all_records),
        "explicit_label_ownership": "910/910 exactly once",
        "distinct_exact_speaker_labels": len(label_counts),
        "label_distribution_matches_preflight": True,
        "source_scene_numbers_invented": 0,
        "speaker_alias_normalizations": 0,
        "owned_unlabelled_continuation_lines": total_continuation_lines,
        "unowned_ordinary_source_blocks": total_unowned_blocks,
        "unowned_ordinary_source_lines": total_unowned_lines,
        "multi_page_dialogue_records": len(multi_page),
        "reviewed_cross_page_candidates": cross_page_review,
        "reviewed_dash_candidates": dash_review,
        "zero_dialogue_scenes": dialogue_index["zero_dialogue_scenes"],
        "per_scene": scene_qas,
        "next_gate": "character/entity index remains BLOCKED until unlabelled-block audit is source-role reviewed and dialogue QA status becomes pass",
    }
    (NOTES / "dialogue-index-qa.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    qa_md = f"""# அம்மையப்பன் — dialogue-index QA

Status: **{'REVIEW REQUIRED' if all_unowned else 'PASS'}**

- scene coverage: **63/63**
- explicit source speaker labels: **910/910 owned exactly once**
- immutable dialogue records: **{len(all_records)}**
- distinct exact speaker-label strings: **{len(label_counts)}**
- speaker-label distribution vs preflight: **PASS**
- reviewed dash false positives: **14/14 excluded as labels**
- reviewed page-boundary candidates: **19/19 preserved as same-utterance continuations**
- total multi-page dialogue records found by full state machine: **{len(multi_page)}**
- unlabelled continuation source lines owned by an active utterance: **{total_continuation_lines}**
- ordinary source blocks with no active explicit speaker: **{total_unowned_blocks} blocks / {total_unowned_lines} lines**
- source scene numbers invented: **0**
- alias/name normalization: **0**

The immutable record build is structurally complete.  The character/entity gate stays **BLOCKED** until every unlabelled ordinary block is source-role reviewed; those blocks are deliberately not guessed into dialogue ownership.
"""
    (NOTES / "dialogue-index-qa.md").write_text(qa_md, encoding="utf-8")

    print(json.dumps({
        "dialogue_records": len(all_records),
        "distinct_exact_speaker_labels": len(label_counts),
        "multi_page_dialogue_records": len(multi_page),
        "owned_unlabelled_continuation_lines": total_continuation_lines,
        "unowned_blocks": total_unowned_blocks,
        "unowned_lines": total_unowned_lines,
        "qa_status": qa_status,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
