#!/usr/bin/env python3
"""Apply locked Ammayappan PDF 85-94 visual-fidelity + historical-glyph corrections.

The operation is page-scoped and fail-fast. It changes only source-established
readings from the locked manifest, preserves existing layout whitespace, marks
PDF 85-94 verified only after all replacements validate, requires canonical and
retained provenance to agree page-by-page, and closes markers 98-107 only after
both surfaces pass.
"""

from __future__ import annotations

import difflib
import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
MANIFEST = WORK / "notes" / "dual-gate-sync-pdf-085-094.json"
REPORT = WORK / "notes" / "dual-gate-sync-report-pdf-085-094.json"
LEDGER = WORK / "notes" / "textual-notes-pdf-085-094.md"
CANONICAL = WORK / "transcription" / "full-text.md"
PROVENANCE = WORK / "transcription" / "parts" / "pdf-085-094.md"
ANCHOR_RE = re.compile(r"<!--\s*source:\s*pdf=(\d+)\b[^>]*-->")


@dataclass(frozen=True)
class Match:
    logical_start: int
    logical_end: int
    raw_start: int
    raw_end: int


def logical_text(raw: str) -> str:
    return "".join(ch for ch in raw if not ch.isspace())


def logical_index_map(raw: str) -> list[int]:
    return [idx for idx, ch in enumerate(raw) if not ch.isspace()]


def find_logical_matches(raw: str, needle: str) -> list[Match]:
    logical = logical_text(raw)
    target = logical_text(needle)
    if not target:
        raise ValueError("empty logical replacement source")
    mapping = logical_index_map(raw)
    matches: list[Match] = []
    start = 0
    while True:
        pos = logical.find(target, start)
        if pos < 0:
            break
        end = pos + len(target)
        matches.append(Match(pos, end, mapping[pos], mapping[end - 1] + 1))
        start = end
    return matches


def standalone_old_matches(old_matches: list[Match], new_matches: list[Match]) -> list[Match]:
    return [
        old for old in old_matches
        if not any(new.logical_start <= old.logical_start and old.logical_end <= new.logical_end for new in new_matches)
    ]


def boundary_mapper(old: str, new: str):
    ops = difflib.SequenceMatcher(a=old, b=new, autojunk=False).get_opcodes()

    def map_pos(pos: int) -> int:
        if pos <= 0:
            return 0
        if pos >= len(old):
            return len(new)
        for tag, i1, i2, j1, j2 in ops:
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
                return j2 if old_span == 0 else j1 + round((pos - i1) * new_span / old_span)
        return len(new)

    return map_pos


def whitespace_runs(raw: str) -> list[tuple[int, str]]:
    runs: list[tuple[int, str]] = []
    logical_count = 0
    i = 0
    while i < len(raw):
        if raw[i].isspace():
            start = i
            while i < len(raw) and raw[i].isspace():
                i += 1
            runs.append((logical_count, raw[start:i]))
        else:
            logical_count += 1
            i += 1
    return runs


def replace_preserving_whitespace(raw_match: str, old: str, new: str) -> str:
    old_logical = logical_text(old)
    new_logical = logical_text(new)
    if logical_text(raw_match) != old_logical:
        raise AssertionError("matched text did not normalize to manifest source")
    map_pos = boundary_mapper(old_logical, new_logical)
    pieces: list[str] = []
    last = 0
    for pos, ws in whitespace_runs(raw_match):
        boundary = max(last, min(map_pos(pos), len(new_logical)))
        pieces.append(new_logical[last:boundary])
        pieces.append(ws)
        last = boundary
    pieces.append(new_logical[last:])
    return "".join(pieces)


def page_span(text: str, pdf: int) -> tuple[int, int]:
    anchors = list(ANCHOR_RE.finditer(text))
    for idx, anchor in enumerate(anchors):
        if int(anchor.group(1)) == pdf:
            end = anchors[idx + 1].start() if idx + 1 < len(anchors) else len(text)
            return anchor.start(), end
    raise ValueError(f"missing source anchor for PDF {pdf}")


def page_block(text: str, pdf: int) -> str:
    start, end = page_span(text, pdf)
    return text[start:end]


def replace_page(text: str, *, pdf: int, old: str, new: str, surface: str) -> tuple[str, dict]:
    start, end = page_span(text, pdf)
    block = text[start:end]
    old_all = find_logical_matches(block, old)
    new_matches = find_logical_matches(block, new)
    old_matches = standalone_old_matches(old_all, new_matches)

    if not old_matches and len(new_matches) == 1:
        return text, {"surface": surface, "status": "already-synchronized", "applied": 0}
    if len(old_matches) != 1:
        raise ValueError(
            f"PDF {pdf} {surface}: expected one standalone occurrence of {old!r}; "
            f"old={len(old_matches)}, all_old={len(old_all)}, new={len(new_matches)}"
        )

    match = old_matches[0]
    raw_match = block[match.raw_start:match.raw_end]
    replacement = replace_preserving_whitespace(raw_match, old, new)
    updated_block = block[:match.raw_start] + replacement + block[match.raw_end:]

    post_new = find_logical_matches(updated_block, new)
    post_old = standalone_old_matches(find_logical_matches(updated_block, old), post_new)
    if post_old or len(post_new) != 1:
        raise ValueError(
            f"PDF {pdf} {surface}: replacement postcondition failed for {old!r} -> {new!r}; "
            f"old_remaining={len(post_old)}, new_count={len(post_new)}"
        )
    return text[:start] + updated_block + text[end:], {"surface": surface, "status": "synchronized", "applied": 1}


def mark_verified(text: str, pdf: int) -> str:
    start, end = page_span(text, pdf)
    block = text[start:end]
    anchor = ANCHOR_RE.search(block)
    if not anchor:
        raise ValueError(f"PDF {pdf}: source anchor missing inside page block")
    anchor_text = anchor.group(0)
    if "status=verified" in anchor_text:
        return text
    if "status=draft" not in anchor_text:
        raise ValueError(f"PDF {pdf}: unexpected anchor status: {anchor_text}")
    new_anchor = anchor_text.replace("status=draft", "status=verified", 1)
    new_block = block[:anchor.start()] + new_anchor + block[anchor.end():]
    return text[:start] + new_block + text[end:]


def comparable_page(text: str, pdf: int) -> str:
    block = page_block(text, pdf)
    anchor = ANCHOR_RE.search(block)
    if not anchor:
        raise ValueError(f"PDF {pdf}: cannot find anchor for comparison")
    return logical_text(block[anchor.end():])


def resolved_ledger(manifest: dict) -> str:
    lines = [
        "# அம்மையப்பன் — PDF 85–94 dual-gate marker resolution",
        "",
        "Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`",
        "",
        "Markers **98–107 are CLOSED** by rendered-scan visual-fidelity and historical-Tamil-glyph review. The readings below are occurrence-specific source verdicts; they are not semantic normalization or OCR repair.",
        "",
        "| Marker | Accepted source reading |",
        "|---:|---|",
    ]
    for marker in range(98, 108):
        reading = manifest["resolved_markers"][str(marker)]
        lines.append(f"| {marker} | `{reading}` |")
    lines += [
        "",
        "## Batch disposition",
        "",
        "- PDF range: **85–94 / printed pp.83–92**;",
        "- visual source fidelity: **PASS 10/10**;",
        "- historical-Tamil-glyph gate: **PASS 10/10**;",
        "- unresolved markers remaining in this range: **0**;",
        "- global replacement: **not used**;",
        "- canonical/provenance agreement: **PASS**;",
        "- next uncertainty sequence begins at marker **108** in PDF 95–104.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("policy") != "page-scoped-dual-gate-sync" or manifest.get("pdf_range") != [85, 94]:
        raise ValueError("unexpected PDF 85-94 manifest identity")

    originals = {
        CANONICAL: CANONICAL.read_text(encoding="utf-8"),
        PROVENANCE: PROVENANCE.read_text(encoding="utf-8"),
    }
    working = dict(originals)
    pages_report: list[dict] = []
    applied = 0

    for page in manifest["pages"]:
        pdf = int(page["pdf"])
        page_report = {"pdf": pdf, "printed": page["printed"], "replacements": []}
        for item in page["replacements"]:
            entry = {"from": item["from"], "to": item["to"], "basis": item["basis"], "targets": []}
            for path, surface in [(CANONICAL, "canonical"), (PROVENANCE, "provenance")]:
                working[path], result = replace_page(
                    working[path], pdf=pdf, old=item["from"], new=item["to"], surface=surface
                )
                entry["targets"].append(result)
                applied += result["applied"]
            page_report["replacements"].append(entry)
        pages_report.append(page_report)

    for pdf in range(85, 95):
        working[CANONICAL] = mark_verified(working[CANONICAL], pdf)
        working[PROVENANCE] = mark_verified(working[PROVENANCE], pdf)

    for pdf in range(85, 95):
        for path, surface in [(CANONICAL, "canonical"), (PROVENANCE, "provenance")]:
            block = page_block(working[path], pdf)
            if "⟦" in block or "⟧" in block:
                raise ValueError(f"PDF {pdf} {surface}: uncertainty marker remains after dual-gate audit")

    for pdf in range(85, 95):
        if comparable_page(working[CANONICAL], pdf) != comparable_page(working[PROVENANCE], pdf):
            raise ValueError(f"PDF {pdf}: canonical/provenance content mismatch after synchronization")

    controls = []
    for control in manifest.get("preserve_controls", []):
        pdf = int(control["pdf"])
        text = control["text"]
        count = len(find_logical_matches(page_block(working[CANONICAL], pdf), text))
        if count != 1:
            raise ValueError(f"PDF {pdf}: preserve control {text!r} expected once, found {count}")
        controls.append({"pdf": pdf, "text": text, "status": "preserved"})

    changed_files = []
    for path, content in working.items():
        if content != originals[path]:
            path.write_text(content, encoding="utf-8")
            changed_files.append(str(path.relative_to(ROOT)))

    ledger_content = resolved_ledger(manifest)
    if LEDGER.read_text(encoding="utf-8") != ledger_content:
        LEDGER.write_text(ledger_content, encoding="utf-8")
        changed_files.append(str(LEDGER.relative_to(ROOT)))

    report = {
        "work_id": manifest["work_id"],
        "source": manifest["source"],
        "status": "complete-pass",
        "pdf_range": manifest["pdf_range"],
        "printed_range": manifest["printed_range"],
        "pages_verified": 10,
        "page_scoped": True,
        "global_replacement_used": False,
        "source_whitespace_preserved_around_replacements": True,
        "uncertainty_markers_remaining_in_range": 0,
        "canonical_provenance_page_match": "PASS",
        "logical_replacements_applied_across_surfaces": applied,
        "changed_files": changed_files,
        "preserve_controls": controls,
        "resolved_markers": manifest["resolved_markers"],
        "pages": pages_report,
        "next_pdf_page": 95,
        "next_printed_page": 93,
        "next_action": "Continue at PDF 95 / printed p.93 with visual source-fidelity and historical-Tamil-glyph verification together; adjudicate markers 108-114."
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "pages_verified": report["pages_verified"],
        "replacements_applied_across_surfaces": applied,
        "changed_files": changed_files,
        "controls": controls,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
