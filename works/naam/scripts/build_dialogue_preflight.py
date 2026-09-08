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
NON_SPEAKER_LABELS = {"இடம்", "நேரம்", "காலம்", "பாட்டு", "வசனம்", "டைரக்ஷன்"}


def source_anchor(line: str):
    m = SOURCE_RE.match(line)
    if not m:
        return None
    token = m.group("printed")
    return {
        "pdf_page": int(m.group("pdf")),
        "printed_page": int(token) if token and token.isdigit() else None,
    }


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


def main() -> None:
    idx = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    assert idx["status"] == "complete-verified"
    assert idx["source_numbered_scenes"] is True
    assert idx["source_scene_count"] == 45
    scenes = idx["scene_records"]
    assert len(scenes) == 45

    label_counts: Counter[str] = Counter()
    delimiter_counts: Counter[str] = Counter()
    scene_counts: dict[str, int] = {}
    scene_labels: dict[str, list[str]] = {}
    zero_scenes: list[str] = []
    rejects: list[dict] = []
    anomalous: list[dict] = []
    candidates: dict[str, list[dict]] = defaultdict(list)
    classes: Counter[str] = Counter()

    for scene in scenes:
        sid = scene["scene_id"]
        path = SCENES / scene["file"]
        lines = path.read_text(encoding="utf-8").splitlines()
        current_page = None
        local_labels: Counter[str] = Counter()
        count = 0
        for line_no, raw in enumerate(lines, 1):
            s = raw.strip()
            anchor = source_anchor(s)
            if anchor:
                current_page = anchor
                classes["source_anchor"] += 1
                continue
            m = DIALOGUE_RE.match(s)
            if m:
                label = m.group("label").strip()
                text = m.group("text")
                if label in NON_SPEAKER_LABELS or label.startswith("#") or label.startswith("<!--"):
                    rejects.append({
                        "scene_id": sid, "scene_file": scene["file"], "line": line_no,
                        "pdf_page": current_page["pdf_page"] if current_page else None,
                        "raw": s, "reason": "known non-speaker colon label",
                    })
                    classes["colon_reject"] += 1
                    continue
                assert current_page is not None, (sid, line_no, s)
                count += 1
                label_counts[label] += 1
                delimiter_counts[m.group("delimiter")] += 1
                local_labels[label] += 1
                classes["explicit_dialogue"] += 1
                candidates[sid].append({
                    "line": line_no,
                    "speaker_label": label,
                    "delimiter": m.group("delimiter"),
                    "text": text,
                    "pdf_page": current_page["pdf_page"],
                    "printed_page": current_page["printed_page"],
                })
                continue
            cls = classify_non_dialogue(s)
            classes[cls] += 1
            if cls == "other":
                am = ANOMALOUS_RE.match(s)
                if am:
                    anomalous.append({
                        "scene_id": sid, "scene_file": scene["file"], "line": line_no,
                        "pdf_page": current_page["pdf_page"] if current_page else None,
                        "printed_page": current_page["printed_page"] if current_page else None,
                        "label_candidate": am.group("label").strip(),
                        "delimiter": am.group("delimiter"), "text": am.group("text"), "raw": s,
                    })
        scene_counts[sid] = count
        scene_labels[sid] = sorted(local_labels)
        if count == 0:
            zero_scenes.append(sid)

    all_candidates = [r for rows in candidates.values() for r in rows]
    assert len(scene_counts) == 45
    assert all(5 <= r["pdf_page"] <= 71 for r in all_candidates)

    payload = {
        "work_id": "naam",
        "phase": "dialogue-index-preflight",
        "status": "review-ready",
        "scene_count": 45,
        "source_numbered_scenes": True,
        "explicit_dialogue_candidates": len(all_candidates),
        "distinct_exact_speaker_labels": len(label_counts),
        "delimiter_distribution": dict(sorted(delimiter_counts.items())),
        "exact_speaker_labels": [
            {"speaker_label": label, "count": count}
            for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0]))
        ],
        "zero_explicit_dialogue_scenes": zero_scenes,
        "scene_dialogue_candidate_counts": scene_counts,
        "scene_distinct_labels": scene_labels,
        "colon_rejects": rejects,
        "anomalous_delimiter_candidates": anomalous,
        "classification_counts": dict(sorted(classes.items())),
        "policy": {
            "authority": "45/45 complete-verified source-numbered scene derivatives",
            "speaker_label": "exact source text before : or :-; no normalization",
            "delimiter": "source delimiter is structural and not copied into utterance text",
            "unlabelled_speech": "left unlabelled; never assigned by inference",
            "page_break": "provenance boundary, not utterance boundary",
            "character_alias_resolution": "deferred to character/entity index",
        },
    }
    NOTES.mkdir(exist_ok=True)
    (NOTES / "dialogue-index-preflight.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# நாம் — dialogue-index preflight", "", "Status: **REVIEW READY**", "",
        "This inventory is generated only from the 45/45 complete-verified scene derivatives. It does not normalize speaker labels and does not assign source-unlabelled speech.", "",
        "## Coverage", "",
        f"- scene derivatives scanned: **45/45**",
        f"- explicit `:` / `:-` dialogue candidates: **{len(all_candidates)}**",
        f"- distinct exact speaker labels: **{len(label_counts)}**",
        f"- zero-explicit-dialogue scenes: **{len(zero_scenes)}**",
        f"- known non-speaker colon lines rejected: **{len(rejects)}**",
        f"- anomalous non-colon delimiter candidates: **{len(anomalous)}**", "",
        "## Exact speaker-label inventory", "", "| Exact label | Turns |", "|---|---:|",
    ]
    for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0])):
        md.append(f"| `{label}` | {count} |")
    md += ["", "## Known non-speaker colon lines", ""]
    if rejects:
        for r in rejects:
            md.append(f"- `{r['scene_id']}` PDF {r['pdf_page']} line {r['line']}: `{r['raw']}`")
    else:
        md.append("None.")
    md += ["", "## Anomalous delimiter candidates", ""]
    if anomalous:
        for r in anomalous:
            md.append(f"- `{r['scene_id']}` PDF {r['pdf_page']} line {r['line']}: `{r['raw']}`")
    else:
        md.append("None detected by the conservative short-label audit.")
    md += ["", "## Gate", "", "Review every anomalous delimiter candidate before immutable dialogue generation. Character/entity alias resolution remains out of scope.", ""]
    (NOTES / "dialogue-index-preflight.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({
        "explicit_dialogue_candidates": len(all_candidates),
        "distinct_exact_speaker_labels": len(label_counts),
        "colon_rejects": len(rejects),
        "anomalous_delimiter_candidates": len(anomalous),
        "zero_explicit_dialogue_scenes": len(zero_scenes),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
