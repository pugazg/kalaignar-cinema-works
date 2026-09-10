#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / "works" / "vandikkaran-magan"
PAGES = W / "transcription" / "pages"
SCENES = W / "scenes"
NOTES = W / "notes"

SOURCE_META_RE = re.compile(r"\A<!-- source: pdf=(\d+).*?status=visual-verified -->\n?")
SCENE_HEADING_RE = re.compile(r"^##\s+(காட்சி.*)$", re.M)
DIALOGUE_RE = re.compile(
    r"^(?P<label>[^:#\[\]{}<>\n]{1,60}?)(?P<delimiter>:\s*(?:—|–|-)?)\s*(?P<text>\S.*)$"
)
ALT_RE = re.compile(
    r"^(?P<label>[\u0B80-\u0BFF A-Za-z.]{1,28}?)\s*(?P<delimiter>[;—–-])\s*(?P<text>\S.*)$"
)
SEPARATORS = {"★", "★★★", "* * *", "---", "***", "___"}


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_page(pdf: int) -> str:
    path = PAGES / f"{pdf:03d}.md"
    raw = path.read_text(encoding="utf-8")
    m = SOURCE_META_RE.match(raw)
    if not m or int(m.group(1)) != pdf:
        raise SystemExit(f"invalid canonical wrapper: {path}")
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
    if s.startswith("(") or s.endswith(")"):
        return "stage_direction_parenthetical"
    if s.startswith("[") or s.endswith("]"):
        return "stage_direction_square"
    if s.startswith("{") or s.endswith("}"):
        return "stage_direction_curly"
    return None


def main() -> None:
    scene_index = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    assert scene_index["status"] == "complete-verified"
    assert scene_index["total_scenes"] == 72
    records = scene_index["scenes"]
    assert len(records) == 72

    # Reconstruct the same canonical screenplay stream used by the scene builder,
    # while retaining page ranges so dialogue candidates can be tied back to pages.
    stream = ""
    page_ranges: dict[int, tuple[int, int]] = {}
    page_bodies: dict[int, str] = {}
    for pdf in range(6, 88):
        body = load_page(pdf)
        page_bodies[pdf] = body
        if stream:
            stream += "\n\n"
        start = len(stream)
        stream += body
        page_ranges[pdf] = (start, len(stream))

    headings = list(SCENE_HEADING_RE.finditer(stream))
    assert len(headings) == 72
    canonical_body = stream[headings[0].start():]
    assert sha256(canonical_body) == scene_index["canonical_scene_body_sha256"]
    assert scene_index["canonical_scene_body_sha256"] == scene_index["joined_scene_spans_sha256"]

    label_counts: Counter[str] = Counter()
    delimiter_counts: Counter[str] = Counter()
    scene_counts: dict[str, int] = {}
    scene_distinct_labels: dict[str, list[str]] = {}
    zero_dialogue_scenes: list[str] = []
    anomalous_candidates: list[dict] = []
    cross_page_candidates: list[dict] = []
    unlabelled_blocks: list[dict] = []
    classification_counts: Counter[str] = Counter()
    candidates_by_scene: dict[str, list[dict]] = defaultdict(list)

    # Build exact scene absolute ranges and then intersect them with each canonical page.
    for ordinal, (scene, heading) in enumerate(zip(records, headings), 1):
        assert scene["ordinal"] == ordinal
        assert heading.group(1).strip() == scene["source_heading"]
        scene_start = heading.start()
        scene_end = headings[ordinal].start() if ordinal < len(headings) else len(stream)
        sid = scene["scene_id"]

        active: dict | None = None
        pending_unlabelled: dict | None = None
        candidate_count = 0
        scene_labels: Counter[str] = Counter()

        def flush_active() -> None:
            nonlocal active
            if active is not None:
                if len(active["pdf_pages"]) > 1:
                    cross_page_candidates.append({
                        "scene_id": sid,
                        "scene_ordinal": ordinal,
                        "speaker_label": active["speaker_label"],
                        "source_delimiter": active["source_delimiter"],
                        "pdf_pages": active["pdf_pages"],
                        "printed_pages": [p - 1 for p in active["pdf_pages"]],
                        "start_pdf": active["pdf_pages"][0],
                        "end_pdf": active["pdf_pages"][-1],
                        "start_line_text": active["start_line_text"],
                    })
                active = None

        def flush_unlabelled() -> None:
            nonlocal pending_unlabelled
            if pending_unlabelled is not None:
                unlabelled_blocks.append(pending_unlabelled)
                pending_unlabelled = None

        for pdf in scene["pdf_pages"]:
            p0, p1 = page_ranges[pdf]
            a, b = max(scene_start, p0), min(scene_end, p1)
            if a >= b:
                continue
            segment = stream[a:b]
            lines = segment.splitlines()
            for raw in lines:
                s = raw.strip()
                kind = structural_kind(s)
                if kind == "blank":
                    # Internal blank lines end ordinary paragraph ownership. A page
                    # transition itself is handled outside this loop and does not flush.
                    flush_active()
                    flush_unlabelled()
                    classification_counts["blank"] += 1
                    continue
                if kind is not None:
                    flush_active()
                    flush_unlabelled()
                    classification_counts[kind] += 1
                    continue

                m = DIALOGUE_RE.match(s)
                if m:
                    flush_active()
                    flush_unlabelled()
                    label = m.group("label").strip()
                    delimiter = m.group("delimiter")
                    text = m.group("text")
                    # Reject obvious non-speaker metadata labels conservatively.
                    if label in {"இடம்", "நேரம்", "காலம்", "பாட்டு", "வசனம்", "டைரக்ஷன்", "கடிதத்தில்"}:
                        classification_counts["non_speaker_colon_cue"] += 1
                        pending_unlabelled = {
                            "scene_id": sid,
                            "scene_ordinal": ordinal,
                            "pdf_page": pdf,
                            "printed_page": pdf - 1,
                            "reason": "known non-speaker colon cue",
                            "lines": [s],
                        }
                        continue
                    candidate_count += 1
                    label_counts[label] += 1
                    delimiter_counts[delimiter] += 1
                    scene_labels[label] += 1
                    rec = {
                        "scene_id": sid,
                        "scene_ordinal": ordinal,
                        "source_heading": scene["source_heading"],
                        "candidate_ordinal": candidate_count,
                        "speaker_label": label,
                        "source_delimiter": delimiter,
                        "text_start": text,
                        "pdf_page": pdf,
                        "printed_page": pdf - 1,
                    }
                    candidates_by_scene[sid].append(rec)
                    active = {
                        "speaker_label": label,
                        "source_delimiter": delimiter,
                        "pdf_pages": [pdf],
                        "start_line_text": s,
                    }
                    classification_counts["explicit_dialogue_start"] += 1
                    continue

                am = ALT_RE.match(s)
                if am:
                    anomalous_candidates.append({
                        "scene_id": sid,
                        "scene_ordinal": ordinal,
                        "pdf_page": pdf,
                        "printed_page": pdf - 1,
                        "label_candidate": am.group("label").strip(),
                        "delimiter": am.group("delimiter"),
                        "text": am.group("text"),
                        "raw": s,
                    })
                    classification_counts["anomalous_delimiter_candidate"] += 1
                    flush_active()
                    flush_unlabelled()
                    continue

                # Ordinary non-structural line: if it follows an explicit label within
                # the same source paragraph, it is a continuation. Otherwise it is kept
                # as an unlabelled block for review and never silently assigned.
                if active is not None:
                    if active["pdf_pages"][-1] != pdf:
                        active["pdf_pages"].append(pdf)
                    classification_counts["owned_unlabelled_continuation"] += 1
                else:
                    if pending_unlabelled is None:
                        pending_unlabelled = {
                            "scene_id": sid,
                            "scene_ordinal": ordinal,
                            "pdf_page": pdf,
                            "printed_page": pdf - 1,
                            "reason": "ordinary source text without active explicit speaker label",
                            "lines": [],
                        }
                    pending_unlabelled["lines"].append(s)
                    classification_counts["unlabelled_ordinary_text"] += 1

            # Do not flush active at a page boundary: a labelled utterance can legally
            # continue onto the next canonical page without repeating the source label.
            if pending_unlabelled is not None:
                flush_unlabelled()

        flush_active()
        flush_unlabelled()
        scene_counts[sid] = candidate_count
        scene_distinct_labels[sid] = sorted(scene_labels)
        if candidate_count == 0:
            zero_dialogue_scenes.append(sid)

    total_candidates = sum(scene_counts.values())
    assert total_candidates == sum(label_counts.values())
    assert len(scene_counts) == 72

    payload = {
        "work_id": "vandikkaran-magan",
        "phase": "dialogue-index-preflight",
        "status": "review-ready",
        "authority": "72/72 complete-verified source-led scene derivatives backed by canonical PDF 6-87",
        "scene_count": 72,
        "explicit_dialogue_candidates": total_candidates,
        "distinct_exact_speaker_labels": len(label_counts),
        "delimiter_distribution": dict(sorted(delimiter_counts.items())),
        "scene_dialogue_candidate_counts": scene_counts,
        "scene_distinct_labels": scene_distinct_labels,
        "zero_explicit_dialogue_scenes": zero_dialogue_scenes,
        "anomalous_delimiter_candidates": anomalous_candidates,
        "cross_page_continuation_candidates": cross_page_candidates,
        "unlabelled_blocks": unlabelled_blocks,
        "classification_counts": dict(sorted(classification_counts.items())),
        "exact_speaker_labels": [
            {"speaker_label": label, "count": count}
            for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0]))
        ],
        "candidates_by_scene": candidates_by_scene,
        "policy": {
            "immutable_unit": "one explicit source speaker-labelled utterance",
            "speaker_label": "exact source label; no normalization",
            "source_delimiter": "preserved exactly as canonical transcription",
            "page_break": "provenance boundary, not an utterance boundary",
            "unlabelled_text": "never assigned a speaker by inference",
            "stage_song_written_text": "not dialogue starts unless the source explicitly labels a speaker",
            "character_alias_resolution": "deferred to character/entity indexing",
        },
    }
    NOTES.mkdir(parents=True, exist_ok=True)
    (NOTES / "dialogue-index-preflight.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "# வண்டிக்காரன் மகன் — dialogue-index preflight",
        "",
        "Status: **REVIEW READY**",
        "",
        "This preflight inventories source-explicit dialogue syntax from the closed canonical screenplay/72-scene layer. It does not normalize speaker labels and does not yet create immutable dialogue records.",
        "",
        "## Coverage",
        "",
        f"- verified scenes scanned: **72/72**",
        f"- explicit labelled dialogue candidates: **{total_candidates}**",
        f"- distinct exact speaker labels: **{len(label_counts)}**",
        f"- zero-explicit-dialogue scenes: **{len(zero_dialogue_scenes)}**",
        f"- anomalous non-colon delimiter candidates: **{len(anomalous_candidates)}**",
        f"- candidate cross-page utterances: **{len(cross_page_candidates)}**",
        f"- unlabelled ordinary blocks retained for review: **{len(unlabelled_blocks)}**",
        "",
        "## Delimiter distribution",
        "",
    ]
    for delim, count in sorted(delimiter_counts.items()):
        md.append(f"- `{delim}` — **{count}**")
    md += ["", "## Exact speaker-label inventory", "", "| Exact label | Candidates |", "|---|---:|"]
    for label, count in sorted(label_counts.items(), key=lambda x: (-x[1], x[0])):
        md.append(f"| `{label}` | {count} |")
    md += ["", "## Zero-dialogue scenes", ""]
    md.append(", ".join(f"`{x}`" for x in zero_dialogue_scenes) if zero_dialogue_scenes else "None.")
    md += ["", "## Anomalous delimiter candidates", ""]
    if anomalous_candidates:
        for r in anomalous_candidates:
            md.append(f"- scene `{r['scene_id']}` PDF {r['pdf_page']}: `{r['raw']}`")
    else:
        md.append("None detected by the conservative short-label audit.")
    md += ["", "## Cross-page continuation candidates", ""]
    if cross_page_candidates:
        for r in cross_page_candidates:
            md.append(
                f"- scene `{r['scene_id']}` `{r['speaker_label']}` — PDF "
                f"{r['start_pdf']}→{r['end_pdf']} / delimiter `{r['source_delimiter']}`"
            )
    else:
        md.append("None detected.")
    md += ["", "## Gate", ""]
    md.append(
        "Review every anomalous delimiter, cross-page candidate and unlabelled block before immutable dialogue generation. Character/entity alias normalization remains out of scope."
    )
    (NOTES / "dialogue-index-preflight.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(json.dumps({
        "explicit_dialogue_candidates": total_candidates,
        "distinct_exact_speaker_labels": len(label_counts),
        "zero_dialogue_scenes": len(zero_dialogue_scenes),
        "anomalous_delimiter_candidates": len(anomalous_candidates),
        "cross_page_continuation_candidates": len(cross_page_candidates),
        "unlabelled_blocks": len(unlabelled_blocks),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
