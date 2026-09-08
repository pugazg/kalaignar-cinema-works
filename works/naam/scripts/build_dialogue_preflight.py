#!/usr/bin/env python3
"""Inventory exact speaker-label syntax in the verified Naam scene derivatives."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "scenes"
NOTES = ROOT / "notes"

SOURCE_RE = re.compile(r"^<!--\s*source:\s*pdf=(?P<pdf>\d+)(?:\s+printed=(?P<printed>[^\s>]+))?[^>]*-->")
DIALOGUE_RE = re.compile(r"^(?P<label>[^:#\[\]{}<>\n]{1,60}?)\s*(?P<delimiter>:-|:)\s*(?P<text>\S.*)$")
ANOMALOUS_RE = re.compile(r"^(?P<label>[\u0B80-\u0BFF A-Za-z.]{1,24}?)\s*(?P<delimiter>[—–-])\s*(?P<text>\S.*)$")
NON_SPEAKER_LABELS = {"இடம்", "நேரம்", "காலம்", "பாட்டு", "வசனம்", "டைரக்ஷன்", "கடிதத்தில்"}
REVIEWED_ALT_DIALOGUE = {
    ("naam-s041", "ஜீவானந்தர் — குமரன்! குமரன்!"): ("ஜீவானந்தர்", "—", "குமரன்! குமரன்!"),
}


def source_anchor(line: str):
    m = SOURCE_RE.match(line)
    if not m:
        return None
    token = m.group("printed")
    return {"pdf_page": int(m.group("pdf")), "printed_page": int(token) if token and token.isdigit() else None}


def is_metadata_comment(s: str) -> bool:
    return s.startswith("<!--") and s.endswith("-->")


def classify_non_dialogue(s: str) -> str:
    if not s:
        return "blank"
    if is_metadata_comment(s):
        return "comment"
    if s.startswith("#"):
        return "heading"
    if s.startswith("[") or s.endswith("]"):
        return "stage_direction_square"
    if s.startswith("{") or s.endswith("}"):
        return "stage_direction_curly"
    if s.startswith("(") or s.endswith(")"):
        return "stage_direction_paren"
    if s in {"★", "★★★", "* * *", "---", "***", "___"}:
        return "separator"
    return "other"


def dialogue_parse(scene_id: str, s: str):
    alt = REVIEWED_ALT_DIALOGUE.get((scene_id, s))
    if alt:
        return {"label": alt[0], "delimiter": alt[1], "text": alt[2], "kind": "reviewed-alternate-delimiter"}
    if s.startswith(("(", "[", "{")):
        return None
    m = DIALOGUE_RE.match(s)
    if not m:
        return None
    label = m.group("label").strip()
    if label in NON_SPEAKER_LABELS or label.startswith("#") or label.startswith("<!--"):
        return None
    return {"label": label, "delimiter": m.group("delimiter"), "text": m.group("text"), "kind": "standard-colon"}


def non_speaker_colon_reason(s: str):
    if s.startswith(("(", "[", "{")) and DIALOGUE_RE.match(s):
        return "stage/location line beginning with structural punctuation"
    m = DIALOGUE_RE.match(s)
    if m and m.group("label").strip() in NON_SPEAKER_LABELS:
        return "known non-speaker colon label"
    return None


def main() -> None:
    idx = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    assert idx["status"] == "complete-verified"
    assert idx["source_numbered_scenes"] is True
    assert idx["source_scene_count"] == 45
    scenes = idx["scene_records"]
    assert len(scenes) == 45

    label_counts: Counter[str] = Counter(); delimiter_counts: Counter[str] = Counter()
    scene_counts = {}; scene_labels = {}; zero_scenes = []
    rejects = []; anomalous = []; reviewed_alt = []; candidates = defaultdict(list); classes = Counter()

    for scene in scenes:
        sid = scene["scene_id"]; lines = (SCENES / scene["file"]).read_text(encoding="utf-8").splitlines()
        current_page = None; local_labels = Counter(); count = 0
        for line_no, raw in enumerate(lines, 1):
            s = raw.strip(); anchor = source_anchor(s)
            if anchor:
                current_page = anchor; classes["source_anchor"] += 1; continue
            parsed = dialogue_parse(sid, s)
            if parsed:
                assert current_page is not None, (sid, line_no, s)
                count += 1; label_counts[parsed["label"]] += 1; delimiter_counts[parsed["delimiter"]] += 1; local_labels[parsed["label"]] += 1
                classes["explicit_dialogue"] += 1
                row = {"line": line_no, "speaker_label": parsed["label"], "delimiter": parsed["delimiter"], "text": parsed["text"], "pdf_page": current_page["pdf_page"], "printed_page": current_page["printed_page"], "parse_kind": parsed["kind"]}
                candidates[sid].append(row)
                if parsed["kind"] == "reviewed-alternate-delimiter":
                    reviewed_alt.append({"scene_id": sid, "scene_file": scene["file"], **row, "raw": s, "decision": "explicit-speaker-label-occurrence"})
                continue
            reason = non_speaker_colon_reason(s)
            if reason:
                rejects.append({"scene_id": sid, "scene_file": scene["file"], "line": line_no, "pdf_page": current_page["pdf_page"] if current_page else None, "raw": s, "reason": reason})
                classes["colon_reject"] += 1; continue
            cls = classify_non_dialogue(s); classes[cls] += 1
            if cls == "other":
                am = ANOMALOUS_RE.match(s)
                if am:
                    anomalous.append({"scene_id": sid, "scene_file": scene["file"], "line": line_no, "pdf_page": current_page["pdf_page"] if current_page else None, "printed_page": current_page["printed_page"] if current_page else None, "label_candidate": am.group("label").strip(), "delimiter": am.group("delimiter"), "text": am.group("text"), "raw": s})
        scene_counts[sid] = count; scene_labels[sid] = sorted(local_labels)
        if count == 0: zero_scenes.append(sid)

    all_candidates = [r for rows in candidates.values() for r in rows]
    assert len(scene_counts) == 45 and all(5 <= r["pdf_page"] <= 71 for r in all_candidates)
    assert len(reviewed_alt) == 1 and reviewed_alt[0]["speaker_label"] == "ஜீவானந்தர்"
    assert all(r["raw"] != "ஜீவானந்தர் — குமரன்! குமரன்!" for r in anomalous)

    payload = {
        "work_id": "naam", "phase": "dialogue-index-preflight", "status": "review-complete-ready-to-build",
        "scene_count": 45, "source_numbered_scenes": True,
        "explicit_dialogue_candidates": len(all_candidates), "distinct_exact_speaker_labels": len(label_counts),
        "delimiter_distribution": dict(sorted(delimiter_counts.items())),
        "exact_speaker_labels": [{"speaker_label": label, "count": count} for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0]))],
        "zero_explicit_dialogue_scenes": zero_scenes, "scene_dialogue_candidate_counts": scene_counts, "scene_distinct_labels": scene_labels,
        "colon_rejects": rejects, "reviewed_alternate_delimiter_dialogues": reviewed_alt,
        "anomalous_delimiter_candidates": [{**r, "decision": "not-a-speaker-label"} for r in anomalous],
        "classification_counts": dict(sorted(classes.items())),
        "policy": {
            "authority": "45/45 complete-verified source-numbered scene derivatives",
            "speaker_label": "exact source label; no normalization",
            "standard_delimiters": [":", ":-"],
            "reviewed_alternate_delimiter": "one occurrence only: scene 41 `ஜீவானந்தர் — குமரன்! குமரன்!`",
            "non_speaker_colon_cues": "location/stage cues and `கடிதத்தில்` remain non-dialogue source structures",
            "unlabelled_speech": "left unlabelled; never assigned by inference",
            "page_break": "provenance boundary, not utterance boundary",
            "character_alias_resolution": "deferred to character/entity index",
        },
    }
    NOTES.mkdir(exist_ok=True)
    (NOTES / "dialogue-index-preflight.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = ["# நாம் — dialogue-index preflight", "", "Status: **REVIEW COMPLETE — READY TO BUILD**", "", "Authority: 45/45 complete-verified scene derivatives. No speaker-label normalization or source-unlabelled speaker inference is permitted.", "", "## Coverage", "", f"- scene derivatives scanned: **45/45**", f"- explicit dialogue candidates: **{len(all_candidates)}**", f"- distinct exact speaker labels: **{len(label_counts)}**", f"- delimiter distribution: **{dict(sorted(delimiter_counts.items()))}**", f"- zero-explicit-dialogue scenes: **{len(zero_scenes)}**", f"- non-speaker colon/location/written-text cues rejected: **{len(rejects)}**", f"- reviewed alternate-delimiter dialogue occurrences: **{len(reviewed_alt)}**", f"- remaining dash candidates reviewed as non-speaker: **{len(anomalous)}**", "", "## Exact speaker-label inventory", "", "| Exact label | Turns |", "|---|---:|"]
    for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0])): md.append(f"| `{label}` | {count} |")
    md += ["", "## Occurrence-specific delimiter verdict", "", "- `naam-s041`, PDF 66: `ஜீவானந்தர் — குமரன்! குமரன்!` is an explicit speaker-labelled utterance. The em dash is accepted **only for this reviewed occurrence**; no global dash-to-dialogue rule is introduced.", "", "## Non-speaker safeguards", "", "- `(இடம் ...` / `இடம் ...` location cues are structural, not speakers.", "- `கடிதத்தில் :- ...` is written-text provenance, not a speaker label.", "- `உன்மீனு :- ...` remains an exact source speaker label because it is explicitly printed/transcribed as such; no silent normalization is applied.", "", "## Gate", "", "Preflight review is closed. Immutable dialogue generation may proceed using these exact counts and occurrence-specific verdicts.", ""]
    (NOTES / "dialogue-index-preflight.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({"explicit_dialogue_candidates": len(all_candidates), "distinct_exact_speaker_labels": len(label_counts), "colon_rejects": len(rejects), "reviewed_alternate": len(reviewed_alt), "remaining_dash_non_speakers": len(anomalous), "zero_explicit_dialogue_scenes": len(zero_scenes)}, ensure_ascii=False))

if __name__ == "__main__": main()
