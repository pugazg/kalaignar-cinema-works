#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    song = json.loads((ROOT / "songs/index.json").read_text(encoding="utf-8"))
    assert song["status"] == "complete-verified-source-only"
    assert song["candidate_hits_reviewed"] == 64
    assert song["source_visible_occurrences"] == 5
    assert song["unresolved_authorship_occurrences"] == 3
    assert song["source_attributed_literary_quotation_occurrences"] == 1
    assert song["authorship_not_applicable_occurrences"] == 1
    assert song["full_named_song_lyric_blocks_printed"] == 0
    assert song["standalone_tamil_lyric_files_authorized"] == 0
    assert song["standalone_tamil_lyric_files_created"] == 0
    assert song["external_item_level_evidence_used"] is False
    assert song["canonical_tamil_changed"] is False
    assert song["english_translation_gate"] == "ready"

    # Work README.
    p = ROOT / "README.md"
    text = p.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "| Song/performance authorship gate | not-started |",
        "| Song/performance authorship gate | **complete-verified-source-only — 5 source-visible occurrences / 0 standalone lyric files** |",
        "README song row",
    )
    text = replace_once(
        text,
        "**Begin English translation/reconciliation from the frozen 105/105 Tamil source plus the completed scene, dialogue, and character/entity derivatives.** Preserve source structure and exact Tamil linkage; do not modify canonical Tamil or dialogue evidence unless a new source-backed correction is independently established.",
        "**Begin source-linked English translation/reconciliation from the frozen 105/105 Tamil source plus the completed scene, dialogue, character/entity, and song/performance evidence layers.** Preserve source structure and exact Tamil linkage; translate only source-visible song/performance material and do not reconstruct absent lyrics.",
        "README next action",
    )
    p.write_text(text, encoding="utf-8")

    # Work handover.
    p = ROOT / "PROJECT_HANDOVER.md"
    text = p.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- song/performance authorship gate: not-started;",
        "- song/performance authorship gate: **complete-verified-source-only — 64/64 candidates reviewed; 5 retained occurrences; 0 standalone lyric files**;",
        "handover song gate",
    )
    closure = """

## Song / verse / performance authorship closure — FINAL SOURCE GATE

- preflight candidate hits reviewed: **64/64**;
- retained source-visible occurrences: **5**;
- unresolved authorship occurrences: **3**;
- source-attributed literary quotation occurrences: **1**;
- authorship-not-applicable japa occurrences: **1**;
- complete named song lyric bodies printed by the booklet: **0**;
- standalone Tamil lyric files authorized / created: **0 / 0**;
- external item-level evidence used: **no**;
- canonical Tamil changed by this gate: **no**;
- source inventory: `songs/index.json`, `songs/inventory.json`, `songs/candidate-disposition.json`, `songs/credits.json`;
- gate commit: `d51e3151a3fff218d8e942fc91e6eb837c1d487c`.

The booklet's printed `கதை வசனம் / மு. கருணாநிதி` credit is not promoted into lyric authorship. English may translate only the source-visible performance references, literary fragment, japa token and cues; absent song lyrics must not be reconstructed from film audio, websites, subtitles, later editions or memory.

### Exact next activity

> **Begin source-linked English translation/reconciliation from the frozen Tamil and completed derivative evidence layers. Preserve scene/dialogue/character provenance and translate only source-visible song/performance material.**
"""
    if "## Song / verse / performance authorship closure — FINAL SOURCE GATE" not in text:
        text = text.rstrip() + closure + "\n"
    p.write_text(text, encoding="utf-8")

    # Metadata.
    p = ROOT / "metadata.yaml"
    text = p.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "  song_authorship_mapping: not-started\n  english_translation: ready-next-phase",
        "  song_authorship_mapping: complete-verified-source-only\n  song_index_path: \"songs/index.json\"\n  song_candidate_hits_reviewed: 64\n  song_source_visible_occurrences: 5\n  song_unresolved_authorship_occurrences: 3\n  song_full_named_lyric_blocks_printed: 0\n  song_standalone_tamil_lyric_files: 0\n  english_translation: ready-next-phase",
        "metadata structured song block",
    )
    text = replace_once(
        text,
        "  song_authorship_gate: not-started\n  english_translation: ready-next-phase",
        "  song_authorship_gate: complete-verified-source-only-64-reviewed-5-occurrences-0-lyric-files\n  english_translation: ready-next-phase",
        "metadata status song gate",
    )
    text = replace_once(
        text,
        'next_action: "Begin English translation/reconciliation from the frozen verified Tamil plus completed scene/dialogue/character evidence layers; preserve exact source provenance."',
        'next_action: "Begin source-linked English translation/reconciliation from the frozen verified Tamil plus completed scene/dialogue/character/song-performance evidence layers; do not reconstruct absent lyrics."',
        "metadata next action",
    )
    p.write_text(text, encoding="utf-8")

    # Shared work registry.
    p = REPO / "data/works.json"
    works = json.loads(p.read_text(encoding="utf-8"))
    matches = [w for w in works if w.get("id") == "ammaiyappan"]
    assert len(matches) == 1, f"data/works.json: expected one ammaiyappan record, found {len(matches)}"
    w = matches[0]
    sd = w.setdefault("structured_derivatives", {})
    sd.update({
        "song_authorship_mapping": "complete-verified-source-only",
        "song_index_path": "works/ammaiyappan/songs/index.json",
        "song_candidate_hits_reviewed": 64,
        "song_source_visible_occurrences": 5,
        "song_unresolved_authorship_occurrences": 3,
        "song_source_attributed_literary_quotation_occurrences": 1,
        "song_authorship_not_applicable_occurrences": 1,
        "song_full_named_lyric_blocks_printed": 0,
        "song_tamil_derivatives": "complete-source-only-no-standalone-lyrics",
        "song_tamil_derivative_files": 0,
        "english_translation": "ready-next-phase",
        "next_structured_derivative": "english-translation",
    })
    w["next_action"] = "Begin source-linked English translation/reconciliation; preserve verified Tamil provenance and do not reconstruct absent song lyrics."
    p.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("AMMAYAPPAN SONG/PERFORMANCE CLOSURE STATUS SYNCHRONIZED")


if __name__ == "__main__":
    main()
