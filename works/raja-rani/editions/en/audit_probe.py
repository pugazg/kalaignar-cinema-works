#!/usr/bin/env python3
"""Whole-work preflight for the Raja Rani bilingual reader/export layer."""

from pathlib import Path

import build

OUT = Path(__file__).resolve().parent


def main() -> int:
    model, stats, inputs = build.validate_model()
    input_hash = build.aggregate_sha256(inputs)
    report = f"""# Raja Rani bilingual reader/export — preflight QA

Status: **PASS**

This preflight validates the complete-verified Raja Rani bilingual input corpus before generated reader files are built.

## Screenplay input

- archival navigation scenes: **{stats['screenplay_scenes']}/58**
- source-numbered screenplay scenes: **none**
- verified English units: **{stats['screenplay_units']:,}/1,236**
- immutable dialogue links: **{stats['immutable_dialogue_links']:,}/1,071**
- source-unlabelled spoken units: **{stats['source_unlabelled_spoken_units']}/19**
- cross-page English units: **{stats['cross_page_screenplay_units']}/15**
- source-visible performance occurrence links: **{stats['screenplay_performance_occurrence_links']}/4**
- unit kinds: `{stats['screenplay_kind_counts']}`

## Numbered-song input

- actual source-numbered front-matter songs: **{stats['numbered_songs']}/11**
- translation sections: **{stats['numbered_song_sections']}/67**
- Tamil/English line-cue mappings: **{stats['numbered_song_line_cues']}/181**
- cross-page song records: **{stats['cross_page_numbered_songs']}/4**
- authorship: **{stats['song_authorship_anthology_attributed']} later-anthology Kalaignar-attributed / {stats['song_authorship_unresolved']} unresolved**
- performance-link disposition: **3 verified / 1 review**

## Integrity gates

- all 58 verified Tamil scene derivatives present: **PASS**
- all 58 verified English scene records present and ordered: **PASS**
- all 1,071 immutable dialogue IDs linked exactly once: **PASS**
- deleted T055 duplicate IDs absent from source and English linkage: **PASS**
- source-unlabelled speech retains null speaker metadata: **PASS**
- page provenance/order checks: **PASS**
- all 11 verified Tamil/English numbered-song records present: **PASS**
- every mapped Tamil song line/cue exists in its verified Tamil derivative: **PASS**
- song authorship tiers unchanged: **PASS**
- scene-58/song-11 relationship remains review-level: **PASS**
- songs are not assigned synthetic screenplay scene IDs: **PASS**
- placeholders / synthetic scene-end prose: **0**

## Reproducibility checkpoint

- authoritative input files: **{len(set(inputs))}**
- authoritative-input aggregate SHA-256: `{input_hash}`
- source scan SHA-256: `{build.SOURCE_SHA256}`

The reader builder may proceed from this checkpoint. Reader generation is downstream only and must not rewrite canonical Tamil, dialogue records, character mappings, song authorship or verified translations.
"""
    (OUT / "PREFLIGHT_QA_REPORT.md").write_text(report, encoding="utf-8")
    print("RAJA RANI BILINGUAL READER PREFLIGHT: PASS")
    print(stats)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
