#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "scenes"
SONGS = ROOT / "songs"

PATTERNS = {
    "song-or-singing": re.compile(r"பாட|பாட்டு|பாடல்|கீத|தாலாட்டு|பல்லவி|சரணம்"),
    "music-or-dance": re.compile(r"இசை|ராக|வீணை|நடன|ஆடுகிற|ஆடுகின்ற|ஆடின|கச்சேரி"),
    "chant-or-ritual": re.compile(r"ஜப|மந்திர|ஸ்லோக|பஜனை|பூஜை|குருபூஜை"),
}
SOURCE_RE = re.compile(r"<!-- source: pdf=(\d+)(?: (?:logical_)?printed(?:_page)?=(\d+))?.*?-->")


def main():
    scene_index = json.loads((SCENES / "index.json").read_text(encoding="utf-8"))
    assert scene_index["archive_scene_count"] == 63

    candidates = []
    scanned_lines = 0
    for rec in scene_index["scene_records"]:
        scene_no = rec["ordinal"]
        path = SCENES / rec["file"]
        lines = path.read_text(encoding="utf-8").splitlines()
        pdf_page = None
        printed_page = None
        for lineno, line in enumerate(lines, start=1):
            m = SOURCE_RE.search(line)
            if m:
                pdf_page = int(m.group(1))
                printed_page = int(m.group(2)) if m.group(2) else None
                continue
            if not line.strip() or line.lstrip().startswith("<!--"):
                continue
            scanned_lines += 1
            matches = [kind for kind, pat in PATTERNS.items() if pat.search(line)]
            if not matches:
                continue
            candidates.append({
                "candidate_id": f"ammaiyappan-perf-cand-{len(candidates)+1:03d}",
                "archive_scene_id": rec["scene_id"],
                "archive_scene_ordinal": scene_no,
                "source_heading": rec["heading"],
                "source_scene_file": rec["file"],
                "source_line": lineno,
                "pdf_page": pdf_page,
                "printed_page": printed_page,
                "matched_categories": matches,
                "source_text": line,
                "disposition": "review",
            })

    doc = {
        "work_id": "ammaiyappan",
        "phase": "song-performance-authorship-preflight",
        "status": "review-ready",
        "canonical_tamil_gate": "105/105-dual-gate-complete-verified",
        "scene_derivative_gate": "63/63-complete-verified",
        "scene_files_scanned": 63,
        "nonblank_source_lines_scanned": scanned_lines,
        "candidate_count": len(candidates),
        "search_categories": list(PATTERNS),
        "policy": {
            "candidate_match_is_not_song_authorship_evidence": True,
            "story_dialogue_credit_does_not_establish_lyric_authorship": True,
            "external_lyrics_may_not_fill_absent_source_text": True,
            "source_visible_bodies_must_be_classified_before_english_translation": True,
        },
        "candidates": candidates,
        "next_action": "Review every candidate against verified scene context; classify song/verse/performance occurrences and authorship evidence without importing absent lyrics.",
    }
    SONGS.mkdir(exist_ok=True)
    (SONGS / "performance-preflight.json").write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = [
        "# அம்மையப்பன் — song / verse / performance preflight",
        "",
        "Status: **REVIEW READY**",
        "",
        f"- verified scene files scanned: **63/63**",
        f"- keyword/context candidates: **{len(candidates)}**",
        "- candidate hits are navigation only; they are **not** authorship evidence.",
        "",
        "## Candidates",
        "",
    ]
    for x in candidates:
        page = f"PDF {x['pdf_page']}" if x['pdf_page'] else "page unknown"
        if x["printed_page"]:
            page += f" / printed {x['printed_page']}"
        md.append(f"- `{x['candidate_id']}` — scene {x['archive_scene_ordinal']} — {page} — {', '.join(x['matched_categories'])} — `{x['source_text']}`")
    md += [
        "",
        "## Review rule",
        "",
        "Each candidate must be dispositioned from source context as dialogue mentioning music/song, source-visible performance cue, bounded song/verse/chant text, or false positive. Do not infer lyric authorship from Kalaignar's story/dialogue credit.",
    ]
    (SONGS / "performance-preflight.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"scenes": 63, "candidates": len(candidates)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
