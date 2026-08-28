#!/usr/bin/env python3
"""D1.2 canonical/scene strict-fidelity probe for Tirumbippaar.

The gate compares source-bearing scene content, excluding scene-heading/location
markup because the source and derivative legitimately encode those structural
headers differently. It never treats either text layer as source truth: the
controlling scan must adjudicate every reported difference.
"""
from __future__ import annotations

import difflib
import json
import re
import unicodedata
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "tirumbippaar"
PARTS = sorted((WORK / "transcription" / "parts").glob("part-*.md"))
SCENES = [WORK / "scenes" / f"scene-{n:02d}.md" for n in range(1, 94)]
OUT = WORK / "notes" / "d1-2-scene-fidelity-audit.generated.json"
SOURCE_RE = re.compile(r"<!--\s*source:\s*pdf=(\d+)(?:\s+printed=(\d+))?\s+status=([^\s>]+)")
SCENE_RE = re.compile(r"காட்சி\s*(\d+)")

@dataclass
class Line:
    text: str
    path: str
    file_line: int
    pdf: int | None
    printed: int | None
    scene: int | None


def norm_word(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    return "".join(ch for ch in s if ch.isalnum())


def ws_fold(s: str) -> str:
    return re.sub(r"\s+", "", s)


def classify(a: str, b: str) -> str:
    if a == b:
        return "exact"
    if ws_fold(a) == ws_fold(b):
        return "whitespace-only"
    glyph_map = str.maketrans({"—":"-", "–":"-", "’":"'", "‘":"'", "“":"\"", "”":"\""})
    if ws_fold(a.translate(glyph_map)) == ws_fold(b.translate(glyph_map)):
        return "quote-dash-glyph"
    bracket_chars = set("[](){}")
    if norm_word(a) == norm_word(b) and any(ch in bracket_chars for ch in a+b):
        return "bracket-parenthesis"
    if norm_word(a) == norm_word(b):
        dots_a = re.sub(r"[^.]", "", a)
        dots_b = re.sub(r"[^.]", "", b)
        if dots_a != dots_b or "..." in a or "..." in b:
            return "ellipsis-punct-count"
        return "other-punctuation"
    return "word-level"


def is_split_location_header(display: str) -> bool:
    """True for the structural location line sometimes stored after காட்சி N.

    In this source those lines are open-bracket/open-parenthesis structures,
    whereas a following stage direction is normally closed on the same line.
    """
    if not display or display[0] not in "[(":
        return False
    if ":" in display:
        return False
    if display[0] == "[":
        return not display.endswith("]")
    return not display.endswith(")")


def parse_file(path: Path, scene_hint: int | None) -> list[Line]:
    out: list[Line] = []
    pdf = printed = None
    started = scene_hint is not None
    current_scene = scene_hint
    after_scene_heading = False
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = SOURCE_RE.search(raw)
        if m:
            pdf = int(m.group(1)); printed = int(m.group(2)) if m.group(2) else None
            started = True
            continue
        if not started:
            continue
        s = raw.strip()
        if not s or s.startswith("<!--"):
            continue
        display = re.sub(r"^#{1,6}\s+", "", s)
        if display in {"திரும்பிப்பார்!", "★"}:
            continue
        sm = SCENE_RE.search(display)
        if sm:
            current_scene = int(sm.group(1))
            after_scene_heading = True
            # Scene heading/location structure is outside the 1,342-line text
            # equality gate used in D1.1/D1.2.
            continue
        if after_scene_heading:
            after_scene_heading = False
            if is_split_location_header(display):
                continue
        if display.startswith("Status:") or display.startswith("Source:") or display.startswith("SHA-256:"):
            continue
        out.append(Line(display, str(path.relative_to(ROOT)), i, pdf, printed, current_scene))
    return out


def build():
    canonical: list[Line] = []
    for p in PARTS:
        canonical += parse_file(p, None)
    scenes: list[Line] = []
    for n, p in enumerate(SCENES, 1):
        scenes += parse_file(p, n)

    ak = [norm_word(x.text) for x in canonical]
    bk = [norm_word(x.text) for x in scenes]
    sm = difflib.SequenceMatcher(a=ak, b=bk, autojunk=False)
    pairs = []
    unaligned = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for i, j in zip(range(i1,i2), range(j1,j2)):
                pairs.append((canonical[i], scenes[j]))
        else:
            unaligned.append({
                "tag": tag,
                "canonical": [asdict(x) | {"key":norm_word(x.text)} for x in canonical[i1:i2]],
                "scene": [asdict(x) | {"key":norm_word(x.text)} for x in scenes[j1:j2]],
            })
    mismatches = []
    exact_text = 0
    exact_text_and_page = 0
    for idx, (a,b) in enumerate(pairs, 1):
        if a.text == b.text:
            exact_text += 1
            if a.pdf == b.pdf:
                exact_text_and_page += 1
                continue
        cls = classify(a.text,b.text)
        if a.text == b.text and a.pdf != b.pdf:
            cls = "page-attribution"
        mismatches.append({
            "pair_index": idx,
            "class": cls,
            "canonical": asdict(a),
            "scene": asdict(b),
            "same_text": a.text == b.text,
            "same_pdf": a.pdf == b.pdf,
        })
    counts = {}
    for x in mismatches:
        counts[x["class"]] = counts.get(x["class"],0)+1
    return {
        "canonical_lines": len(canonical),
        "scene_lines": len(scenes),
        "aligned_pairs": len(pairs),
        "unaligned_blocks": len(unaligned),
        "exact_text": exact_text,
        "exact_text_and_page": exact_text_and_page,
        "mismatch_count_including_page": len(mismatches),
        "class_counts": counts,
        "unaligned": unaligned,
        "mismatches": mismatches,
    }


def main():
    gate = build()
    result = {
        "work_id":"tirumbippaar",
        "audit":"D1.2 strict canonical/scene source-order fidelity",
        "authority":"controlling scan; neither canonical nor scene derivative is presumptively correct",
        "gate_definition":"exact trimmed-line identity for 1,342 source-bearing non-heading scene lines; punctuation, ellipses, whitespace and quote/dash glyphs significant; page attribution audited separately",
        "gate": gate,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in gate.items() if k not in {"unaligned","mismatches"}}, ensure_ascii=False, indent=2))
    if gate["aligned_pairs"] != 1342 or gate["unaligned"]:
        raise SystemExit(f"D1.2 alignment gate drift: aligned={gate['aligned_pairs']} unaligned_blocks={gate['unaligned_blocks']}")

if __name__ == "__main__":
    main()
