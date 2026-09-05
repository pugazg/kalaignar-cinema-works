#!/usr/bin/env python3
"""Build a source-preserving dialogue extraction preflight for Ammayappan.

This script does not create dialogue records. It inventories explicit speaker-label
syntax in the already verified scene derivatives so that the immutable dialogue
builder can be locked against the actual source formatting first.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "scenes"
NOTES = ROOT / "notes"

SOURCE_RE = re.compile(
    r"^<!-- source: pdf=(?P<pdf>\d+)"
    r"(?: printed=(?P<printed>\d+)| logical_printed=(?P<logical>\d+))?"
)
DIALOGUE_RE = re.compile(r"^(?P<label>[^:#\[\]<>\n]{1,60}?)\s*:\s*(?P<text>\S.*)$")
# Audit-only detector for likely label-like prefixes using a non-colon delimiter.
ANOMALOUS_RE = re.compile(
    r"^(?P<label>[\u0B80-\u0BFF A-Za-z.]{1,24}?)\s*(?P<delimiter>[—–-])\s*(?P<text>\S.*)$"
)


def source_anchor(line: str):
    m = SOURCE_RE.match(line)
    if not m:
        return None
    printed = m.group("printed") or m.group("logical")
    return {
        "pdf_page": int(m.group("pdf")),
        "printed_page": int(printed) if printed else None,
    }


def is_metadata_comment(line: str) -> bool:
    return line.startswith("<!--") and line.endswith("-->")


def classify_non_dialogue(line: str) -> str:
    s = line.strip()
    if not s:
        return "blank"
    if is_metadata_comment(s):
        return "comment"
    if s.startswith("### "):
        return "heading"
    if s.startswith("[") and s.endswith("]"):
        return "stage_direction_square"
    if s.startswith("(") and s.endswith(")"):
        return "stage_direction_paren"
    if s in {"★", "★★★", "* * *"}:
        return "separator"
    return "other"


def main() -> None:
    index = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    assert index["status"] == "complete-verified"
    assert index["archive_scene_count"] == 63
    records = index["scene_records"]
    assert len(records) == 63

    label_counts: Counter[str] = Counter()
    scene_label_counts: dict[str, int] = {}
    scene_distinct_labels: dict[str, list[str]] = {}
    zero_dialogue_scenes: list[str] = []
    colon_rejects: list[dict] = []
    anomalous_candidates: list[dict] = []
    page_transition_candidates: list[dict] = []
    classification_counts: Counter[str] = Counter()
    per_scene_candidates: dict[str, list[dict]] = defaultdict(list)

    for scene in records:
        scene_id = scene["scene_id"]
        path = SCENES / scene["file"]
        assert path.exists(), path
        lines = path.read_text(encoding="utf-8").splitlines()

        current_page = None
        scene_labels: Counter[str] = Counter()
        dialogue_count = 0

        # Capture context around every page anchor to find possible utterances that
        # continue across a canonical page boundary without repeating the label.
        for i, raw in enumerate(lines):
            anchor = source_anchor(raw.strip())
            if not anchor:
                continue
            prev_nonblank = None
            prev_idx = None
            for j in range(i - 1, -1, -1):
                if lines[j].strip():
                    prev_nonblank = lines[j].strip()
                    prev_idx = j
                    break
            next_nonblank = None
            next_idx = None
            for j in range(i + 1, len(lines)):
                if lines[j].strip():
                    next_nonblank = lines[j].strip()
                    next_idx = j
                    break
            if prev_nonblank and next_nonblank:
                pm = DIALOGUE_RE.match(prev_nonblank)
                nm = DIALOGUE_RE.match(next_nonblank)
                next_class = classify_non_dialogue(next_nonblank)
                if pm and not nm and next_class == "other":
                    page_transition_candidates.append(
                        {
                            "scene_id": scene_id,
                            "scene_file": scene["file"],
                            "anchor_line": i + 1,
                            "from_pdf": current_page["pdf_page"] if current_page else None,
                            "to_pdf": anchor["pdf_page"],
                            "speaker_label": pm.group("label").strip(),
                            "before": pm.group("text"),
                            "after": next_nonblank,
                            "before_line": (prev_idx + 1) if prev_idx is not None else None,
                            "after_line": (next_idx + 1) if next_idx is not None else None,
                        }
                    )
            current_page = anchor

        current_page = None
        for line_no, raw in enumerate(lines, 1):
            s = raw.strip()
            anchor = source_anchor(s)
            if anchor:
                current_page = anchor
                classification_counts["source_anchor"] += 1
                continue

            m = DIALOGUE_RE.match(s)
            if m:
                label = m.group("label").strip()
                text = m.group("text")
                # Reject obvious narrative/heading leakage; retain it in the audit.
                if label.startswith("###") or label.startswith("<!--"):
                    colon_rejects.append(
                        {
                            "scene_id": scene_id,
                            "scene_file": scene["file"],
                            "line": line_no,
                            "raw": s,
                        }
                    )
                    classification_counts["colon_reject"] += 1
                    continue
                assert current_page is not None, (scene_id, line_no, s)
                dialogue_count += 1
                label_counts[label] += 1
                scene_labels[label] += 1
                classification_counts["explicit_colon_dialogue"] += 1
                per_scene_candidates[scene_id].append(
                    {
                        "line": line_no,
                        "speaker_label": label,
                        "text": text,
                        "pdf_page": current_page["pdf_page"],
                        "printed_page": current_page["printed_page"],
                    }
                )
                continue

            cls = classify_non_dialogue(s)
            classification_counts[cls] += 1
            if cls == "other":
                am = ANOMALOUS_RE.match(s)
                if am:
                    anomalous_candidates.append(
                        {
                            "scene_id": scene_id,
                            "scene_file": scene["file"],
                            "line": line_no,
                            "pdf_page": current_page["pdf_page"] if current_page else None,
                            "printed_page": current_page["printed_page"] if current_page else None,
                            "label_candidate": am.group("label").strip(),
                            "delimiter": am.group("delimiter"),
                            "text": am.group("text"),
                            "raw": s,
                        }
                    )

        scene_label_counts[scene_id] = dialogue_count
        scene_distinct_labels[scene_id] = sorted(scene_labels)
        if dialogue_count == 0:
            zero_dialogue_scenes.append(scene_id)

    # Structural assertions: all candidate dialogue records must have page provenance.
    all_candidates = [r for rows in per_scene_candidates.values() for r in rows]
    assert all(r["pdf_page"] is not None for r in all_candidates)
    assert all(5 <= r["pdf_page"] <= 109 for r in all_candidates)
    assert len(scene_label_counts) == 63

    payload = {
        "work_id": "ammaiyappan",
        "phase": "dialogue-index-preflight",
        "status": "review-ready",
        "scene_count": 63,
        "source_numbered_scenes": False,
        "explicit_colon_dialogue_candidates": len(all_candidates),
        "distinct_exact_speaker_labels": len(label_counts),
        "exact_speaker_labels": [
            {"speaker_label": label, "count": count}
            for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0]))
        ],
        "zero_explicit_dialogue_scenes": zero_dialogue_scenes,
        "scene_dialogue_candidate_counts": scene_label_counts,
        "scene_distinct_labels": scene_distinct_labels,
        "colon_rejects": colon_rejects,
        "anomalous_delimiter_candidates": anomalous_candidates,
        "cross_page_continuation_candidates": page_transition_candidates,
        "classification_counts": dict(sorted(classification_counts.items())),
        "policy": {
            "authority": "63 complete-verified scene derivatives",
            "speaker_label": "exact text before source colon; no normalization",
            "unlabelled_speech": "excluded from immutable dialogue records",
            "cross_page_rule": "one labelled utterance remains one record across page boundaries",
            "character_alias_resolution": "deferred to character/entity index",
        },
    }
    (NOTES / "dialogue-index-preflight.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = []
    md.append("# அம்மையப்பன் — dialogue-index preflight")
    md.append("")
    md.append("Status: **REVIEW READY**")
    md.append("")
    md.append("This is a source-format inventory only. It does not normalize speaker labels and does not yet create immutable dialogue records.")
    md.append("")
    md.append("## Coverage")
    md.append("")
    md.append(f"- verified scene derivatives scanned: **63/63**")
    md.append(f"- explicit colon-labelled dialogue candidates: **{len(all_candidates)}**")
    md.append(f"- distinct exact speaker labels: **{len(label_counts)}**")
    md.append(f"- zero-explicit-dialogue scenes: **{len(zero_dialogue_scenes)}**")
    md.append(f"- rejected colon-like metadata/heading lines: **{len(colon_rejects)}**")
    md.append(f"- anomalous non-colon delimiter candidates requiring review: **{len(anomalous_candidates)}**")
    md.append(f"- possible cross-page continuation candidates requiring review: **{len(page_transition_candidates)}**")
    md.append("")
    md.append("## Exact speaker-label inventory")
    md.append("")
    md.append("| Exact label | Candidate turns |")
    md.append("|---|---:|")
    for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0])):
        md.append(f"| `{label}` | {count} |")
    md.append("")
    md.append("## Zero-explicit-dialogue scenes")
    md.append("")
    md.append(", ".join(f"`{x}`" for x in zero_dialogue_scenes) if zero_dialogue_scenes else "None.")
    md.append("")
    md.append("## Anomalous delimiter candidates")
    md.append("")
    if anomalous_candidates:
        for r in anomalous_candidates:
            md.append(f"- `{r['scene_id']}` PDF {r['pdf_page']} line {r['line']}: `{r['raw']}`")
    else:
        md.append("None detected by the conservative short-label audit.")
    md.append("")
    md.append("## Cross-page continuation candidates")
    md.append("")
    if page_transition_candidates:
        for r in page_transition_candidates:
            md.append(
                f"- `{r['scene_id']}` {r['from_pdf']}→{r['to_pdf']} — label `{r['speaker_label']}`; "
                f"review lines {r['before_line']} / {r['after_line']} in `{r['scene_file']}`."
            )
    else:
        md.append("None detected by the immediate-before/immediate-after page-anchor heuristic.")
    md.append("")
    md.append("## Gate")
    md.append("")
    md.append("Before immutable dialogue generation: review every anomalous-delimiter and cross-page candidate against the verified scene text; then lock the extraction schema. Character alias/entity normalization remains out of scope.")
    md.append("")
    (NOTES / "dialogue-index-preflight.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps({
        "explicit_colon_dialogue_candidates": len(all_candidates),
        "distinct_exact_speaker_labels": len(label_counts),
        "zero_explicit_dialogue_scenes": len(zero_dialogue_scenes),
        "anomalous_delimiter_candidates": len(anomalous_candidates),
        "cross_page_continuation_candidates": len(page_transition_candidates),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
