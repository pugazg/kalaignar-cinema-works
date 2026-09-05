#!/usr/bin/env python3
"""Apply the locked Ammayappan historical-glyph synchronization manifest.

The script is deliberately page-scoped and idempotent. It never performs a
work-wide Tamil replacement. Every manifest entry is resolved only inside the
specified `<!-- source: pdf=N ... -->` block. Source line-wrap newlines are
ignored for matching but are reinserted after replacement using an alignment
map, so line-broken canonical/provenance text can still be synchronized without
rewriting unrelated text.

Exit non-zero before writing anything if any expected old/new occurrence count,
page anchor, provenance target, or preserve-control assertion is not satisfied.
"""

from __future__ import annotations

import difflib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[3]
WORK_ROOT = REPO_ROOT / "works" / "ammaiyappan"
MANIFEST_PATH = WORK_ROOT / "notes" / "historical-glyph-sync-manifest.json"
REPORT_PATH = WORK_ROOT / "notes" / "historical-glyph-sync-report.json"
FULL_TEXT_PATH = WORK_ROOT / "transcription" / "full-text.md"

ANCHOR_RE = re.compile(r"<!--\s*source:\s*pdf=(\d+)\b[^>]*-->")


@dataclass(frozen=True)
class Match:
    logical_start: int
    logical_end: int
    raw_start: int
    raw_end: int


def logical_text(raw: str) -> str:
    """Return text with source-layout newlines removed, preserving all else."""
    return raw.replace("\n", "")


def logical_index_map(raw: str) -> list[int]:
    """Map each logical character index to its raw-string index."""
    return [i for i, ch in enumerate(raw) if ch != "\n"]


def find_logical_matches(raw: str, needle: str) -> list[Match]:
    logical = logical_text(raw)
    mapping = logical_index_map(raw)
    out: list[Match] = []
    start = 0
    while True:
        pos = logical.find(needle, start)
        if pos < 0:
            break
        end = pos + len(needle)
        raw_start = mapping[pos]
        raw_end = mapping[end - 1] + 1
        out.append(Match(pos, end, raw_start, raw_end))
        start = end
    return out


def boundary_mapper(old: str, new: str):
    """Return a function mapping old logical boundaries to new boundaries."""
    opcodes = difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes()

    def map_pos(pos: int) -> int:
        if pos <= 0:
            return 0
        if pos >= len(old):
            return len(new)
        for tag, i1, i2, j1, j2 in opcodes:
            if pos < i1:
                return j1
            if i1 <= pos <= i2:
                if tag == "equal":
                    return j1 + (pos - i1)
                if pos == i1:
                    return j1
                if pos == i2:
                    return j2
                old_span = i2 - i1
                new_span = j2 - j1
                if old_span == 0:
                    return j2
                # Interior boundary in a changed span: preserve its relative
                # position as closely as possible.
                return j1 + round((pos - i1) * new_span / old_span)
        return len(new)

    return map_pos


def replace_preserving_newlines(raw_match: str, old: str, new: str) -> str:
    if logical_text(raw_match) != old:
        raise AssertionError("raw match does not normalize to manifest source text")

    # Record newline boundaries as logical character counts before each newline.
    boundaries: list[int] = []
    count = 0
    for ch in raw_match:
        if ch == "\n":
            boundaries.append(count)
        else:
            count += 1

    map_pos = boundary_mapper(old, new)
    mapped = [map_pos(p) for p in boundaries]

    pieces: list[str] = []
    last = 0
    for boundary in mapped:
        boundary = max(last, min(boundary, len(new)))
        pieces.append(new[last:boundary])
        pieces.append("\n")
        last = boundary
    pieces.append(new[last:])
    return "".join(pieces)


def page_span(text: str, pdf: int) -> tuple[int, int]:
    anchors = list(ANCHOR_RE.finditer(text))
    for idx, match in enumerate(anchors):
        if int(match.group(1)) == pdf:
            start = match.start()
            end = anchors[idx + 1].start() if idx + 1 < len(anchors) else len(text)
            return start, end
    raise ValueError(f"missing source anchor for PDF {pdf}")


def page_block(text: str, pdf: int) -> str:
    start, end = page_span(text, pdf)
    return text[start:end]


def replace_page_occurrences(
    text: str,
    *,
    pdf: int,
    old: str,
    new: str,
    expected: int,
    surface: str,
) -> tuple[str, dict]:
    start, end = page_span(text, pdf)
    block = text[start:end]
    old_matches = find_logical_matches(block, old)
    new_matches = find_logical_matches(block, new)

    if len(old_matches) == 0 and len(new_matches) == expected:
        return text, {
            "surface": surface,
            "status": "already-synchronized",
            "from_count_before": 0,
            "to_count_before": expected,
            "applied": 0,
        }

    if len(old_matches) != expected:
        raise ValueError(
            f"PDF {pdf} {surface}: expected {expected} logical occurrence(s) of {old!r}; "
            f"found {len(old_matches)} (new-form count={len(new_matches)})"
        )

    # Replace from the end so raw indices remain valid.
    mutable = block
    for match in reversed(old_matches):
        raw_match = mutable[match.raw_start:match.raw_end]
        replacement = replace_preserving_newlines(raw_match, old, new)
        mutable = mutable[:match.raw_start] + replacement + mutable[match.raw_end:]

    # Postcondition: the old logical reading is gone and at least the expected
    # number of target readings are present on this page.
    if find_logical_matches(mutable, old):
        raise ValueError(f"PDF {pdf} {surface}: old reading remains after replacement: {old!r}")
    if len(find_logical_matches(mutable, new)) < expected:
        raise ValueError(f"PDF {pdf} {surface}: target reading missing after replacement: {new!r}")

    return text[:start] + mutable + text[end:], {
        "surface": surface,
        "status": "synchronized",
        "from_count_before": expected,
        "to_count_before": len(new_matches),
        "applied": expected,
    }


def resolve_part_path(manifest_part: str) -> Path:
    # Manifest paths are recorded relative to the notes directory.
    path = (WORK_ROOT / "notes" / manifest_part).resolve()
    if REPO_ROOT not in path.parents:
        raise ValueError(f"provenance path escapes repository: {manifest_part}")
    return path


def load_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> None:
    manifest = json.loads(load_utf8(MANIFEST_PATH))
    if manifest.get("policy") != "occurrence-specific-historical-glyph-sync":
        raise ValueError("unexpected manifest policy")
    if manifest.get("correction_bearing_pages") != len(manifest.get("pages", [])):
        raise ValueError("manifest page count mismatch")

    original: dict[Path, str] = {FULL_TEXT_PATH: load_utf8(FULL_TEXT_PATH)}
    working: dict[Path, str] = dict(original)
    report_pages: list[dict] = []
    total_applied = 0

    for page in manifest["pages"]:
        pdf = int(page["pdf"])
        expected_targets: list[tuple[Path, str]] = [(FULL_TEXT_PATH, "canonical")]
        if page.get("part"):
            part_path = resolve_part_path(page["part"])
            if part_path not in working:
                original[part_path] = load_utf8(part_path)
                working[part_path] = original[part_path]
            expected_targets.append((part_path, "provenance"))

        page_report = {
            "pdf": pdf,
            "printed": page["printed"],
            "replacement_count": len(page["replacements"]),
            "replacements": [],
        }

        for replacement in page["replacements"]:
            old = replacement["from"]
            new = replacement["to"]
            expected = int(replacement.get("occurrences", 1))
            replacement_report = {
                "from": old,
                "to": new,
                "family": replacement["family"],
                "expected_occurrences": expected,
                "targets": [],
            }
            for target_path, surface in expected_targets:
                updated, target_report = replace_page_occurrences(
                    working[target_path],
                    pdf=pdf,
                    old=old,
                    new=new,
                    expected=expected,
                    surface=surface,
                )
                working[target_path] = updated
                replacement_report["targets"].append(target_report)
                total_applied += target_report["applied"]
            page_report["replacements"].append(replacement_report)
        report_pages.append(page_report)

    # Preserve-controls are required in the canonical page blocks after sync.
    controls_report: list[dict] = []
    canonical = working[FULL_TEXT_PATH]
    for control in manifest.get("preserve_controls", []):
        pdf = int(control["pdf"])
        text = control["text"]
        count = len(find_logical_matches(page_block(canonical, pdf), text))
        if count != 1:
            raise ValueError(
                f"PDF {pdf} preserve-control mismatch: expected exactly 1 occurrence of {text!r}; found {count}"
            )
        controls_report.append({"pdf": pdf, "text": text, "status": "preserved"})

    changed_files = [path for path in working if working[path] != original[path]]
    if not changed_files:
        status = "already-synchronized"
    else:
        status = "synchronized"

    # Write only after *all* validation has passed.
    for path in changed_files:
        path.write_text(working[path], encoding="utf-8")

    report = {
        "work_id": manifest["work_id"],
        "source": manifest["source"],
        "status": status,
        "source_review_range": manifest["source_review_range"],
        "correction_bearing_pages": manifest["correction_bearing_pages"],
        "page_scoped": True,
        "global_replacement_used": False,
        "linewrap_tolerant_matching": True,
        "canonical_and_provenance_required": True,
        "logical_occurrences_applied_across_surfaces": total_applied,
        "changed_files": [str(path.relative_to(REPO_ROOT)) for path in changed_files],
        "preserve_controls": controls_report,
        "pages": report_pages,
        "post_sync_rule": "Each changed reading is the already source-established reading from the historical-glyph audit; the script verifies the exact target reading is present on its specified page and that preserve-controls remain unchanged.",
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": status,
        "changed_files": report["changed_files"],
        "logical_occurrences_applied_across_surfaces": total_applied,
        "pages": len(report_pages),
        "controls": len(controls_report),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
