#!/usr/bin/env python3
"""Build the immutable source-preserving dialogue layer for வண்டிக்காரன் மகன்.

Authority is the closed 72-scene derivative layer backed by verified canonical
Tamil PDF 6–87. Only explicit source speaker labels create dialogue records.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / "works" / "vandikkaran-magan"
PAGES = W / "transcription" / "pages"
SCENES = W / "scenes"
DIALOGUES = W / "dialogues"
RECORDS = DIALOGUES / "records"
NOTES = W / "notes"

SOURCE_META_RE = re.compile(r"\A<!-- source: pdf=(\d+).*?status=visual-verified -->\n?")
SCENE_HEADING_RE = re.compile(r"^##\s+(காட்சி.*)$", re.M)
DIALOGUE_RE = re.compile(
    r"^(?P<label>[^:#\[\]{}<>\n]{1,60}?)(?P<delimiter>:\s*(?:—|–|-)?)\s*(?P<text>\S.*)$"
)
ALT_RE = re.compile(
    r"^(?P<label>[\u0B80-\u0BFF A-Za-z.]{1,28}?)\s*(?P<delimiter>[;—–-])\s*(?P<text>\S.*)$"
)
NON_SPEAKER_LABELS = {"இடம்", "நேரம்", "காலம்", "பாட்டு", "வசனம்", "டைரக்ஷன்", "கடிதத்தில்"}
SEPARATORS = {"★", "★★★", "* * *", "---", "***", "___"}
EXPECTED_ANOMALOUS = {
    "உருட்டல்; மிரட்டல்;",
    "பழுக்கப் பழுக்க-ரசம்",
    "பிழியப் பிழியப்-பழம்",
    "கங்குலில் எங்கும் பனிமூட்டம் — உடல்",
    "படுத்தாள்; புரண்டாள்;",
    "வந்தான்; சேர்ந்தேன்",
    "மின்னும் — பொன்",
    "மெத்தை — தத்தும்",
    "தத்தை; தன்",
    "சந்தம் — தன்",
    "என்று—தன்",
    "காட்டுவேன்; பாருங்களே!",
    "மேய்ப்பவன் என்று — எண்ணியிருக்கும்",
    "ஊரைத் திருத்த - ஒரு",
    "பேரை நிறுத்த - இரு",
    "கிளிப்புள்ளே; கிரிப்புள்ளே;",
}
NEXT = (
    "Begin character/entity indexing from the complete-verified immutable dialogue layer. "
    "Preserve all exact source speaker labels as immutable provenance; map label variants to "
    "character/entity IDs only in a separate interpretive alias layer; keep generic roles, voices, "
    "collectives and source abbreviations explicit; and run whole-work label/entity coverage QA "
    "before opening the song/performance authorship gate. Do not rewrite canonical Tamil, scenes, "
    "or dialogue records."
)


def load_page(pdf: int) -> str:
    raw = (PAGES / f"{pdf:03d}.md").read_text(encoding="utf-8")
    m = SOURCE_META_RE.match(raw)
    if not m or int(m.group(1)) != pdf:
        raise SystemExit(f"invalid canonical source wrapper on PDF {pdf}")
    body = raw[m.end():]
    if body.startswith("\n"):
        body = body[1:]
    return body.rstrip("\n")


def structural_kind(s: str) -> str | None:
    if not s:
        return "blank"
    if s.startswith("<!--") and s.endswith("-->"):
        return "comment"
    if s.startswith("#"):
        return "heading"
    if s in SEPARATORS:
        return "separator"
    if s.startswith("**") and s.endswith("**"):
        return "source_caption_or_emphasis"
    if s.startswith("(") or s.endswith(")"):
        return "stage_direction_parenthetical"
    if s.startswith("[") or s.endswith("]"):
        return "stage_direction_square"
    if s.startswith("{") or s.endswith("}"):
        return "stage_direction_curly"
    return None


def append_piece(obj: dict[str, Any], pdf: int, text: str) -> None:
    segs = obj.setdefault("_segments", [])
    if not segs or segs[-1]["pdf_page"] != pdf:
        segs.append({"pdf_page": pdf, "printed_page": pdf - 1, "lines": [text]})
    else:
        segs[-1]["lines"].append(text)


def finalize_record(obj: dict[str, Any]) -> None:
    segs = obj.pop("_segments")
    page_segments = []
    for seg in segs:
        text = "\n".join(seg["lines"]).strip("\n")
        assert text
        page_segments.append({
            "pdf_page": seg["pdf_page"],
            "printed_page": seg["printed_page"],
            "text": text,
        })
    obj["page_provenance"] = [
        {"pdf_page": s["pdf_page"], "printed_page": s["printed_page"]}
        for s in page_segments
    ]
    obj["text"] = "\n".join(s["text"] for s in page_segments)
    if len(page_segments) > 1:
        obj["page_segments"] = page_segments


def schema() -> dict[str, Any]:
    provenance = {
        "type": "object",
        "required": ["pdf_page", "printed_page"],
        "properties": {
            "pdf_page": {"type": "integer", "minimum": 6, "maximum": 87},
            "printed_page": {"type": "integer", "minimum": 5, "maximum": 86},
        },
        "additionalProperties": False,
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "vandikkaran-magan-dialogue-record.schema.json",
        "title": "Vandikkaran Magan immutable dialogue record",
        "type": "object",
        "required": [
            "id", "scene_id", "scene_ordinal", "source_scene_id", "source_heading",
            "speaker_label", "source_delimiter", "text", "page_provenance", "source_scene_file"
        ],
        "properties": {
            "id": {"type": "string", "pattern": "^vandikkaran-magan-s[0-9]{3}-d[0-9]{3}$"},
            "scene_id": {"type": "string", "pattern": "^vandikkaran-magan-s[0-9]{3}$"},
            "scene_ordinal": {"type": "integer", "minimum": 1, "maximum": 72},
            "source_scene_id": {"type": "string", "minLength": 1},
            "source_heading": {"type": "string", "minLength": 1},
            "speaker_label": {"type": "string", "minLength": 1},
            "source_delimiter": {"type": "string", "minLength": 1},
            "text": {"type": "string", "minLength": 1},
            "page_provenance": {"type": "array", "minItems": 1, "uniqueItems": True, "items": provenance},
            "page_segments": {
                "type": "array", "minItems": 2,
                "items": {
                    "type": "object",
                    "required": ["pdf_page", "printed_page", "text"],
                    "properties": {
                        "pdf_page": {"type": "integer", "minimum": 6, "maximum": 87},
                        "printed_page": {"type": "integer", "minimum": 5, "maximum": 86},
                        "text": {"type": "string", "minLength": 1},
                    },
                    "additionalProperties": False,
                },
            },
            "source_scene_file": {"type": "string", "pattern": "^scene-[0-9]{3}\\.md$"},
        },
        "additionalProperties": False,
    }


def main() -> None:
    scene_index = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    preflight = json.loads((NOTES / "dialogue-index-preflight.json").read_text(encoding="utf-8"))
    assert scene_index["status"] == "complete-verified" and scene_index["total_scenes"] == 72
    assert preflight["status"] == "review-ready" and preflight["scene_count"] == 72
    scenes = scene_index["scenes"]
    assert len(scenes) == 72
    assert preflight["explicit_dialogue_candidates"] == 744
    assert preflight["distinct_exact_speaker_labels"] == 38
    assert preflight["delimiter_distribution"] == {":": 8, ":—": 736}
    assert len(preflight["anomalous_delimiter_candidates"]) == 16
    assert {x["raw"] for x in preflight["anomalous_delimiter_candidates"]} == EXPECTED_ANOMALOUS
    assert len(preflight["cross_page_continuation_candidates"]) == 3

    # Rebuild the canonical screenplay stream and retain page ranges.
    stream = ""
    page_ranges: dict[int, tuple[int, int]] = {}
    for pdf in range(6, 88):
        body = load_page(pdf)
        if stream:
            stream += "\n\n"
        start = len(stream)
        stream += body
        page_ranges[pdf] = (start, len(stream))
    headings = list(SCENE_HEADING_RE.finditer(stream))
    assert len(headings) == 72

    if DIALOGUES.exists():
        shutil.rmtree(DIALOGUES)
    RECORDS.mkdir(parents=True)

    all_records: list[dict[str, Any]] = []
    all_unlabelled: list[dict[str, Any]] = []
    per_scene_counts: dict[str, int] = {}
    source_scene_counts: dict[str, int] = {}
    label_counts: Counter[str] = Counter()
    delimiter_counts: Counter[str] = Counter()
    classification_counts: Counter[str] = Counter()

    for ordinal, (scene, heading) in enumerate(zip(scenes, headings), 1):
        assert scene["ordinal"] == ordinal
        assert scene["source_heading"] == heading.group(1).strip()
        source_sid = scene["scene_id"]
        archive_sid = f"vandikkaran-magan-s{ordinal:03d}"
        scene_file = f"scene-{ordinal:03d}.md"
        scene_start = heading.start()
        scene_end = headings[ordinal].start() if ordinal < len(headings) else len(stream)
        records: list[dict[str, Any]] = []
        active: dict[str, Any] | None = None
        unlabelled: dict[str, Any] | None = None

        def flush_dialogue() -> None:
            nonlocal active
            if active is not None:
                finalize_record(active)
                records.append(active)
                active = None

        def flush_unlabelled() -> None:
            nonlocal unlabelled
            if unlabelled is not None:
                segs = unlabelled.pop("_segments")
                unlabelled["page_provenance"] = [
                    {"pdf_page": s["pdf_page"], "printed_page": s["printed_page"]} for s in segs
                ]
                unlabelled["text"] = "\n".join("\n".join(s["lines"]) for s in segs)
                unlabelled["block_id"] = f"{archive_sid}-u{sum(1 for x in all_unlabelled if x['scene_id']==archive_sid)+1:03d}"
                all_unlabelled.append(unlabelled)
                unlabelled = None

        for pdf in scene["pdf_pages"]:
            p0, p1 = page_ranges[pdf]
            a, b = max(scene_start, p0), min(scene_end, p1)
            if a >= b:
                continue
            for raw in stream[a:b].splitlines():
                s = raw.strip()
                kind = structural_kind(s)
                if kind == "blank":
                    flush_dialogue(); flush_unlabelled(); classification_counts["blank"] += 1
                    continue
                if kind is not None:
                    flush_dialogue(); flush_unlabelled(); classification_counts[kind] += 1
                    continue

                m = DIALOGUE_RE.match(s)
                if m:
                    label = m.group("label").strip()
                    if label in NON_SPEAKER_LABELS:
                        flush_dialogue(); flush_unlabelled()
                        classification_counts["non_speaker_colon_cue"] += 1
                        unlabelled = {
                            "scene_id": archive_sid, "scene_ordinal": ordinal,
                            "source_scene_id": source_sid, "reason": "known non-speaker colon cue",
                            "_segments": [],
                        }
                        append_piece(unlabelled, pdf, s)
                        continue
                    flush_dialogue(); flush_unlabelled()
                    active = {
                        "id": f"{archive_sid}-d{len(records)+1:03d}",
                        "scene_id": archive_sid,
                        "scene_ordinal": ordinal,
                        "source_scene_id": source_sid,
                        "source_heading": scene["source_heading"],
                        "speaker_label": label,
                        "source_delimiter": m.group("delimiter"),
                        "source_scene_file": scene_file,
                        "_segments": [],
                    }
                    append_piece(active, pdf, m.group("text"))
                    classification_counts["explicit_dialogue_start"] += 1
                    continue

                # Reviewed non-colon candidates are punctuation/verse fragments, never speakers.
                am = ALT_RE.match(s)
                if am and s in EXPECTED_ANOMALOUS:
                    flush_dialogue(); flush_unlabelled()
                    classification_counts["reviewed_non_dialogue_anomalous_delimiter"] += 1
                    unlabelled = {
                        "scene_id": archive_sid, "scene_ordinal": ordinal,
                        "source_scene_id": source_sid,
                        "reason": "reviewed non-dialogue non-colon punctuation/verse fragment",
                        "_segments": [],
                    }
                    append_piece(unlabelled, pdf, s)
                    continue

                if active is not None:
                    append_piece(active, pdf, s)
                    classification_counts["owned_unlabelled_continuation"] += 1
                else:
                    if unlabelled is None:
                        unlabelled = {
                            "scene_id": archive_sid, "scene_ordinal": ordinal,
                            "source_scene_id": source_sid,
                            "reason": "ordinary source text without an active explicit speaker label",
                            "_segments": [],
                        }
                    append_piece(unlabelled, pdf, s)
                    classification_counts["unlabelled_ordinary_text"] += 1
            # Deliberately do not flush active at page boundary: one utterance can cross pages.
            flush_unlabelled()

        flush_dialogue(); flush_unlabelled()
        assert all(r["id"] == f"{archive_sid}-d{i:03d}" for i, r in enumerate(records, 1))
        (RECORDS / f"scene-{ordinal:03d}.json").write_text(
            json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        per_scene_counts[archive_sid] = len(records)
        source_scene_counts[source_sid] = len(records)
        all_records.extend(records)
        label_counts.update(r["speaker_label"] for r in records)
        delimiter_counts.update(r["source_delimiter"] for r in records)

    # Lock generated output to the reviewed preflight.
    assert len(all_records) == 744, len(all_records)
    assert source_scene_counts == preflight["scene_dialogue_candidate_counts"]
    expected_labels = {x["speaker_label"]: x["count"] for x in preflight["exact_speaker_labels"]}
    assert dict(label_counts) == expected_labels
    assert dict(sorted(delimiter_counts.items())) == preflight["delimiter_distribution"]
    ids = [r["id"] for r in all_records]
    assert len(ids) == len(set(ids))
    multi = [r for r in all_records if len(r["page_provenance"]) > 1]
    assert len(multi) == 3, [(r["id"], r["page_provenance"]) for r in multi]
    expected_multi = [
        (35, "சடையன்", [48, 49]),
        (55, "சடையன்", [68, 69]),
        (70, "விங்கன்", [85, 86]),
    ]
    observed_multi = [
        (r["scene_ordinal"], r["speaker_label"], [p["pdf_page"] for p in r["page_provenance"]])
        for r in multi
    ]
    assert observed_multi == expected_multi, observed_multi
    colon_only = [r for r in all_records if r["source_delimiter"] == ":"]
    assert len(colon_only) == 8 and all(r["text"] == "—" for r in colon_only)
    zero_archive = [sid for sid, n in per_scene_counts.items() if n == 0]
    zero_source = [scene["scene_id"] for scene in scenes if source_scene_counts[scene["scene_id"]] == 0]
    assert zero_source == preflight["zero_explicit_dialogue_scenes"]
    assert len(zero_archive) == 15

    # Preserve the conservative preflight blocks as a durable exclusion audit.
    unlabelled_audit = {
        "work_id": "vandikkaran-magan",
        "status": "complete-reviewed",
        "authority": "closed canonical screenplay / dialogue preflight",
        "policy": "No source text without an explicit speaker label is promoted to immutable dialogue.",
        "preflight_unlabelled_blocks": len(preflight["unlabelled_blocks"]),
        "generated_unlabelled_blocks": len(all_unlabelled),
        "reviewed_anomalous_non_colon_candidates": len(preflight["anomalous_delimiter_candidates"]),
        "anomalous_disposition": "all 16 excluded as non-speaker punctuation/verse fragments",
        "preflight_blocks": preflight["unlabelled_blocks"],
        "generated_excluded_blocks": all_unlabelled,
    }
    (NOTES / "unlabelled-block-audit.json").write_text(
        json.dumps(unlabelled_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    qa = {
        "work_id": "vandikkaran-magan",
        "phase": "immutable-dialogue-index",
        "status": "PASS",
        "scene_derivatives": "72/72 complete-verified",
        "dialogue_records": len(all_records),
        "distinct_exact_speaker_labels": len(label_counts),
        "delimiter_distribution": dict(sorted(delimiter_counts.items())),
        "zero_dialogue_scenes": zero_archive,
        "zero_dialogue_source_scene_ids": zero_source,
        "multi_page_dialogue_records": len(multi),
        "multi_page_record_ids": [r["id"] for r in multi],
        "reviewed_anomalous_non_colon_candidates": 16,
        "anomalous_candidates_promoted_to_dialogue": 0,
        "unlabelled_source_blocks_assigned_a_speaker": 0,
        "duplicate_dialogue_ids": 0,
        "speaker_label_normalizations": 0,
        "canonical_or_scene_files_modified_by_builder": 0,
        "assertions": {
            "record_count_matches_preflight": True,
            "per_scene_counts_match_preflight": True,
            "exact_label_inventory_matches_preflight": True,
            "delimiter_inventory_matches_preflight": True,
            "three_cross_page_utterances_remain_single_records": True,
            "eight_colon_only_records_preserve_text_as_em_dash": True,
            "zero_dialogue_scenes_preserved": True,
        },
    }
    (NOTES / "dialogue-index-qa.json").write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    qa_md = f"""# வண்டிக்காரன் மகன் — immutable dialogue index QA

Status: **PASS**

- verified scene inputs: **72/72**
- immutable dialogue records: **{len(all_records)}**
- distinct exact source speaker labels: **{len(label_counts)}**
- delimiter distribution: **`:—` {delimiter_counts[':—']} / `:` {delimiter_counts[':']}**
- zero-dialogue scenes: **{len(zero_archive)}**
- cross-page dialogue records: **{len(multi)}**
- reviewed anomalous non-colon candidates promoted to dialogue: **0/16**
- source-unlabelled blocks assigned a speaker: **0**
- duplicate dialogue IDs: **0**
- source speaker-label normalizations: **0**

The three cross-page records preserve one immutable utterance across PDF 48→49 (`சடையன்`), PDF 68→69 (`சடையன்`) and PDF 85→86 (`விங்கன்`). The eight colon-delimited records whose complete source text is `—` remain explicit dialogue records with delimiter `:` and text `—`.

**PASS — the immutable dialogue layer is complete-verified. Character/entity indexing is unblocked.**
"""
    (NOTES / "dialogue-index-qa.md").write_text(qa_md, encoding="utf-8")

    index = {
        "work_id": "vandikkaran-magan",
        "status": "complete-verified",
        "authority": "72/72 complete-verified source-led scene derivatives",
        "canonical_tamil_gate": "87/87-complete-verified-final-visual-pass",
        "source_numbered_scenes": True,
        "source_scene_count": 72,
        "dialogue_record_count": len(all_records),
        "distinct_exact_speaker_labels": len(label_counts),
        "delimiter_distribution": dict(sorted(delimiter_counts.items())),
        "multi_page_dialogue_records": len(multi),
        "scene_record_counts": per_scene_counts,
        "source_scene_record_counts": source_scene_counts,
        "zero_dialogue_scenes": zero_archive,
        "zero_dialogue_source_scene_ids": zero_source,
        "schema": "schema.json",
        "records_directory": "records/",
        "preflight": "../notes/dialogue-index-preflight.json",
        "unlabelled_block_audit": "../notes/unlabelled-block-audit.json",
        "qa": "../notes/dialogue-index-qa.json",
        "policy": {
            "immutable_unit": "one explicit source speaker-labelled utterance",
            "speaker_label": "exact source label; never normalized",
            "source_delimiter": "preserved exactly; :— for 736 records and : for 8 records whose source text is —",
            "page_break": "provenance boundary, not utterance boundary",
            "unlabelled_text_without_active_speaker": "excluded and audited; never guessed",
            "non_colon_punctuation_or_verse_fragments": "16 reviewed candidates excluded from dialogue starts",
            "character_alias_resolution": "deferred",
        },
        "next_action": NEXT,
    }
    (DIALOGUES / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DIALOGUES / "schema.json").write_text(json.dumps(schema(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    readme = f"""# வண்டிக்காரன் மகன் — immutable dialogue layer

**Status:** **COMPLETE-VERIFIED / QA PASS**

Built only from the closed 72/72 source-led scene derivatives. Canonical Tamil and scene files are upstream authority and are not rewritten here.

## Coverage

- scene inputs: **72/72**
- immutable dialogue records: **{len(all_records)}**
- exact source speaker labels: **{len(label_counts)}**
- zero-dialogue scenes: **{len(zero_archive)}**
- cross-page dialogue records: **{len(multi)}**
- delimiters: **`:—` {delimiter_counts[':—']} / `:` {delimiter_counts[':']}**
- unlabelled text assigned to speakers: **0**
- reviewed anomalous non-colon candidates promoted to dialogue: **0/16**

Each `records/scene-NNN.json` file follows derivative scene ordinal order while retaining the exact source scene ID separately. Speaker labels and dialogue text are source-preserving; alias resolution belongs only to the next character/entity layer.

See `../notes/dialogue-index-preflight.json`, `../notes/unlabelled-block-audit.json`, and `../notes/dialogue-index-qa.json`.

## Next

{NEXT}
"""
    (DIALOGUES / "README.md").write_text(readme, encoding="utf-8")

    print(json.dumps({
        "dialogue_records": len(all_records),
        "distinct_exact_speaker_labels": len(label_counts),
        "zero_dialogue_scenes": len(zero_archive),
        "cross_page_dialogue_records": len(multi),
        "delimiter_distribution": dict(sorted(delimiter_counts.items())),
        "anomalous_promoted": 0,
        "unlabelled_speaker_assignments": 0,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
