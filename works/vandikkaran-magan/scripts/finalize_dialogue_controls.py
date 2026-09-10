#!/usr/bin/env python3
"""Close the dialogue preflight controls after verified immutable index generation."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / "works" / "vandikkaran-magan"
NEXT = (
    "Begin character/entity indexing from the complete-verified immutable dialogue layer. "
    "Preserve all exact source speaker labels as immutable provenance; map label variants to "
    "character/entity IDs only in a separate interpretive alias layer; keep generic roles, voices, "
    "collectives and source abbreviations explicit; and run whole-work label/entity coverage QA "
    "before opening the song/performance authorship gate. Do not rewrite canonical Tamil, scenes, "
    "or dialogue records."
)


def main() -> None:
    idx = json.loads((W / "dialogues/index.json").read_text(encoding="utf-8"))
    qa = json.loads((W / "notes/dialogue-index-qa.json").read_text(encoding="utf-8"))
    assert idx["status"] == "complete-verified" and idx["dialogue_record_count"] == 744
    assert idx["distinct_exact_speaker_labels"] == 38
    assert idx["multi_page_dialogue_records"] == 3
    assert len(idx["zero_dialogue_scenes"]) == 15
    assert qa["status"] == "PASS"
    assert qa["reviewed_anomalous_non_colon_candidates"] == 16
    assert qa["anomalous_candidates_promoted_to_dialogue"] == 0
    assert qa["unlabelled_source_blocks_assigned_a_speaker"] == 0

    # Close the machine preflight while retaining its original candidate inventory.
    p = W / "notes/dialogue-index-preflight.json"
    pre = json.loads(p.read_text(encoding="utf-8"))
    assert pre["explicit_dialogue_candidates"] == 744
    assert pre["distinct_exact_speaker_labels"] == 38
    assert len(pre["anomalous_delimiter_candidates"]) == 16
    assert len(pre["cross_page_continuation_candidates"]) == 3
    pre["status"] = "review-complete"
    pre["review_summary"] = {
        "explicit_labelled_candidates_accepted": 744,
        "anomalous_non_colon_candidates_reviewed": 16,
        "anomalous_non_colon_candidates_promoted": 0,
        "cross_page_candidates_reviewed": 3,
        "cross_page_candidates_retained_as_single_records": 3,
        "preflight_unlabelled_blocks_reviewed_under_no-inference-rule": 148,
        "source_unlabelled_blocks_assigned_a_speaker": 0,
        "duplicate_dialogue_ids": 0,
        "speaker_label_normalizations": 0,
        "direct_scan_review_pages_for_anomalous_non_colon_candidates": [18, 36, 46, 47, 60, 73],
        "direct_scan_review_page_pairs_for_cross_page_records": [[48, 49], [68, 69], [85, 86]],
        "result": "PASS",
    }
    p.write_text(json.dumps(pre, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Human-readable preflight becomes a closed historical/control record, not an open gate.
    p = W / "notes/dialogue-index-preflight.md"
    t = p.read_text(encoding="utf-8")
    t = t.replace("Status: **REVIEW READY**", "Status: **REVIEW COMPLETE / DIALOGUE GATE CLOSED**", 1)
    t = t.replace(
        "This preflight inventories source-explicit dialogue syntax from the closed canonical screenplay/72-scene layer. It does not normalize speaker labels and does not yet create immutable dialogue records.",
        "This preflight inventories source-explicit dialogue syntax from the closed canonical screenplay/72-scene layer. Its review is now closed; the resulting immutable dialogue layer contains 744 complete-verified records. Exact source labels were not normalized.",
        1,
    )
    t, n = re.subn(
        r"## Gate\n\n.*?\n?$",
        """## Review disposition

- explicit labelled candidates accepted: **744/744**;
- exact source speaker labels retained without normalization: **38/38**;
- anomalous non-colon candidates reviewed: **16/16** — all are source-visible punctuation/verse fragments and **0** were promoted to dialogue;
- direct-scan anomaly review pages: **PDF 18, 36, 46–47, 60, 73**;
- cross-page candidates reviewed: **3/3** — source scenes `25` (PDF 48→49), `42-எ` (PDF 68→69), and `54` (PDF 85→86) each remain one immutable record with page segments;
- preflight unlabelled ordinary blocks: **148** — all remain governed by the no-inference rule; source-unlabelled blocks assigned a speaker: **0**;
- duplicate dialogue IDs / speaker-label normalizations: **0 / 0**.

**PASS — preflight review is closed. `dialogues/` is COMPLETE-VERIFIED / QA PASS; character/entity indexing is READY-NEXT.**
""",
        t,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit("preflight markdown gate section drift")
    p.write_text(t, encoding="utf-8")

    # Keep the dialogue builder reproducible after the preflight's status advances.
    p = W / "scripts/build_dialogues.py"
    t = p.read_text(encoding="utf-8")
    old = 'assert preflight["status"] == "review-ready" and preflight["scene_count"] == 72'
    new = 'assert preflight["status"] in {"review-ready", "review-complete"} and preflight["scene_count"] == 72'
    if old not in t and new not in t:
        raise SystemExit("dialogue builder preflight assertion drift")
    if old in t:
        t = t.replace(old, new, 1)
    p.write_text(t, encoding="utf-8")

    # Mapping is structural authority but must not advertise a completed phase as still next.
    p = W / "mapping.md"
    t = p.read_text(encoding="utf-8")
    marker = "## Exact next activity"
    if marker not in t:
        raise SystemExit("mapping next section missing")
    replacement = f"""## Dialogue derivative gate

- immutable dialogue records: **744 / COMPLETE-VERIFIED / QA PASS**;
- exact source speaker labels: **38**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3**;
- anomalous non-colon candidates promoted: **0/16**;
- source-unlabelled blocks assigned a speaker: **0**;
- canonical Tamil / scene files changed by dialogue construction: **0**.

## Exact next activity

**{NEXT}**
"""
    t = t[: t.index(marker)] + replacement
    p.write_text(t, encoding="utf-8")

    # Canonical transcription README remains closed while reflecting downstream progress.
    p = W / "transcription/README.md"
    t = p.read_text(encoding="utf-8")
    t, n = re.subn(
        r"## Next\n\n.*?\n?$",
        f"""## Downstream state

The immutable dialogue index is now **COMPLETE-VERIFIED — 744 records / 38 exact source labels / QA PASS**. Three labelled utterances crossing page boundaries remain single dialogue records; 15 scenes legitimately contain zero labelled dialogue; no source-unlabelled block was assigned a speaker. Canonical Tamil remains closed.

**Next:** {NEXT}
""",
        t,
        flags=re.S,
    )
    if n != 1:
        raise SystemExit("transcription README next section drift")
    p.write_text(t, encoding="utf-8")

    # Durable visual-review note for the source-sensitive preflight decisions.
    p = W / "notes/dialogue-source-review.md"
    p.write_text("""# வண்டிக்காரன் மகன் — dialogue source review

Status: **PASS / CLOSED**

This note records the source-sensitive adjudications that were required between dialogue preflight and immutable record generation. The controlling authority remains the rendered image-only scan `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`; no PDF binary is committed.

## Non-colon anomaly review

All **16/16** preflight non-colon candidates were checked against the controlling scan and retained as non-dialogue source text. They occur on PDF **18, 36, 46–47, 60 and 73** and are punctuation/verse/performance fragments, not explicit speaker labels. **Promoted to dialogue: 0.**

## Cross-page review

All **3/3** candidate cross-page labelled utterances were checked as continuous source turns and remain one immutable dialogue record each:

- `vandikkaran-magan-s035-d006` — source scene `25`, `சடையன்`, PDF **48→49**;
- `vandikkaran-magan-s055-d004` — source scene `42-எ`, `சடையன்`, PDF **68→69**;
- `vandikkaran-magan-s070-d005` — source scene `54`, `விங்கன்`, PDF **85→86**.

Each record preserves both PDF/printed-page provenance entries and `page_segments`; no repeated speaker label was invented at the page break.

## Unlabelled-source rule

The preflight inventoried **148** unlabelled ordinary blocks. They were reviewed under the source rule rather than assigned inferred identities: **source-unlabelled blocks assigned a speaker = 0**. Stage directions, source captions, songs/performance matter, written/narrative matter and unlabelled speech remain outside immutable dialogue starts unless an explicit source speaker label exists.

## Closure

The final immutable dialogue layer contains **744 records / 38 exact labels**, with **15** legitimate zero-dialogue scenes, **3** multi-page records, **0** duplicate dialogue IDs and **0** speaker-label normalizations. See `dialogue-index-qa.json` and `../dialogues/index.json`.
""", encoding="utf-8")

    print(json.dumps({
        "status": "PASS",
        "preflight": "review-complete",
        "dialogues": 744,
        "exact_labels": 38,
        "anomalies_excluded": 16,
        "cross_page_records": 3,
        "unlabelled_speaker_assignments": 0,
        "next": "character-entity-index",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
