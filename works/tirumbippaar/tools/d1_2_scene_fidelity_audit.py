#!/usr/bin/env python3
"""D1.2 canonical/scene strict-fidelity probe for Tirumbippaar.

This is an audit helper only. It never treats either text layer as source
truth; the controlling scan must adjudicate every reported difference.
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
    # Alignment key only: discard whitespace and punctuation/glyphs, preserve
    # letters/digits from every script. This is NOT a textual equality rule.
    return "".join(ch for ch in s if ch.isalnum())


def ws_fold(s: str) -> str:
    return re.sub(r"\s+", "", s)


def punct_fold(s: str) -> str:
    return "".join(ch for ch in s if ch.isalnum())


def classify(a: str, b: str) -> str:
    if a == b:
        return "exact"
    if ws_fold(a) == ws_fold(b):
        return "whitespace-only"
    glyph_map = str.maketrans({"—":"-", "–":"-", "’":"'", "‘":"'", "“":"\"", "”":"\""})
    if ws_fold(a.translate(glyph_map)) == ws_fold(b.translate(glyph_map)):
        return "quote-dash-glyph"
    # Bracket/parenthesis separately because these are structurally meaningful.
    bracket_chars = set("[](){}")
    if norm_word(a) == norm_word(b) and any(ch in bracket_chars for ch in a+b):
        return "bracket-parenthesis"
    if norm_word(a) == norm_word(b):
        # Rough split of ellipsis/count from other punctuation.
        dots_a = re.sub(r"[^.]", "", a)
        dots_b = re.sub(r"[^.]", "", b)
        if dots_a != dots_b or "..." in a or "..." in b:
            return "ellipsis-punct-count"
        return "other-punctuation"
    return "word-level"


def parse_file(path: Path, scene_hint: int | None, *, include_stars: bool, include_title: bool) -> list[Line]:
    out: list[Line] = []
    pdf = printed = None
    started = scene_hint is not None
    current_scene = scene_hint
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
        # Strip markdown heading syntax but retain the printed heading text.
        display = re.sub(r"^#{1,6}\s+", "", s)
        if not include_title and display == "திரும்பிப்பார்!":
            continue
        if not include_stars and display == "★":
            continue
        sm = SCENE_RE.search(display)
        if sm:
            current_scene = int(sm.group(1))
        # Exclude non-source explanatory markdown accidentally present after
        # the first anchor. Source files use only source text after anchors;
        # this catches section headings if any appear.
        if display.startswith("Status:") or display.startswith("Source:") or display.startswith("SHA-256:"):
            continue
        out.append(Line(display, str(path.relative_to(ROOT)), i, pdf, printed, current_scene))
    return out


def build(include_stars: bool, include_title: bool):
    canonical: list[Line] = []
    for p in PARTS:
        canonical += parse_file(p, None, include_stars=include_stars, include_title=include_title)
    scenes: list[Line] = []
    for n, p in enumerate(SCENES, 1):
        scenes += parse_file(p, n, include_stars=include_stars, include_title=include_title)

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
    exact = 0
    for idx, (a,b) in enumerate(pairs, 1):
        if a.text == b.text and a.pdf == b.pdf:
            exact += 1
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
        "include_stars": include_stars,
        "include_title": include_title,
        "canonical_lines": len(canonical),
        "scene_lines": len(scenes),
        "aligned_pairs": len(pairs),
        "unaligned_blocks": len(unaligned),
        "exact_text_and_page": exact,
        "mismatch_count_including_page": len(mismatches),
        "class_counts": counts,
        "unaligned": unaligned,
        "mismatches": mismatches,
    }


def main():
    profiles = [
        build(False, False),
        build(True, False),
        build(False, True),
        build(True, True),
    ]
    # Prefer the profile matching the documented D1.1 gate of 1,342 aligned
    # textual lines; otherwise preserve every profile for diagnosis.
    chosen = next((p for p in profiles if p["aligned_pairs"] == 1342 and not p["unaligned"]), profiles[0])
    result = {
        "work_id":"tirumbippaar",
        "audit":"D1.2 strict canonical/scene source-order fidelity",
        "authority":"controlling scan; neither canonical nor scene derivative is presumptively correct",
        "profiles_summary":[{k:v for k,v in p.items() if k not in {"unaligned","mismatches"}} for p in profiles],
        "chosen_profile": chosen,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result["profiles_summary"], ensure_ascii=False, indent=2))
    print("chosen aligned", chosen["aligned_pairs"], "mismatches", len(chosen["mismatches"]), chosen["class_counts"])

if __name__ == "__main__":
    main()
