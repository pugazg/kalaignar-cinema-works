#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
W = ROOT / "works" / "vandikkaran-magan"
D = json.loads((W / "dialogues/index.json").read_text(encoding="utf-8"))
assert D["status"] == "complete-verified"
assert D["dialogue_record_count"] == 744
assert D["distinct_exact_speaker_labels"] == 38
assert D["multi_page_dialogue_records"] == 3
assert len(D["zero_dialogue_scenes"]) == 15
assert D["delimiter_distribution"] == {":": 8, ":—": 736}

NEXT = (
    "Begin character/entity indexing from the complete-verified 744-record dialogue layer. "
    "Inventory all 38 exact source speaker labels first; preserve every label in immutable dialogue provenance; "
    "map spelling/abbreviation variants only in a separate interpretive alias layer when source/context supports the relationship; "
    "keep generic roles, voices and collectives explicit; run 38/38 label and 744/744 dialogue-record coverage QA; "
    "then synchronize checkpoints before opening the song/performance authorship gate. Do not rewrite canonical Tamil, scenes or dialogue records."
)


def must_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing expected text for {label}: {old!r}")
    return text.replace(old, new)

# Close/reconcile the dialogue preflight review.
p = W / "notes/dialogue-index-preflight.json"
pre = json.loads(p.read_text(encoding="utf-8"))
assert pre["explicit_dialogue_candidates"] == 744
assert len(pre["anomalous_delimiter_candidates"]) == 16
assert len(pre["cross_page_continuation_candidates"]) == 3
pre["status"] = "review-complete"
pre["review_summary"] = {
    "explicit_candidates_accepted": 744,
    "anomalous_non_colon_candidates_reviewed": 16,
    "anomalous_non_colon_candidates_promoted": 0,
    "cross_page_candidates_reviewed": 3,
    "cross_page_candidates_retained_as_single_records": 3,
    "colon_only_records_reviewed": 8,
    "colon_only_disposition": "explicit speaker label with delimiter : and complete source text —",
    "unlabelled_source_blocks_assigned_speakers": 0,
}
p.write_text(json.dumps(pre, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

p = W / "notes/dialogue-index-preflight.md"
t = p.read_text(encoding="utf-8")
t = t.replace("Status: **REVIEW READY**", "Status: **REVIEW COMPLETE**")
t = re.sub(
    r"## Gate\n\n.*?\n?$",
    "## Review disposition\n\n"
    "- all **744** explicit labelled candidates accepted as immutable-dialogue starts;\n"
    "- all **16** non-colon anomaly candidates reviewed as punctuation/verse fragments and excluded from dialogue starts;\n"
    "- all **3** cross-page candidates retained as one dialogue record each;\n"
    "- all **8** colon-only cases are source-explicit dialogue records whose complete text is `—`;\n"
    "- source-unlabelled blocks assigned a speaker: **0**.\n\n"
    "**PASS — preflight review is closed and `dialogues/` is COMPLETE-VERIFIED.**\n",
    t,
    flags=re.S,
)
p.write_text(t, encoding="utf-8")

# Make the builder reproducible after preflight closure.
p = W / "scripts/build_dialogues.py"
t = p.read_text(encoding="utf-8")
t = must_replace(t, 'assert preflight["status"] == "review-ready" and preflight["scene_count"] == 72', 'assert preflight["status"] in {"review-ready", "review-complete"} and preflight["scene_count"] == 72', "builder preflight status")
p.write_text(t, encoding="utf-8")

# Work README.
p = W / "README.md"; t = p.read_text(encoding="utf-8")
t = must_replace(t,
    "- dialogue index: **READY-NEXT**;\n- character/entity index: **BLOCKED pending dialogue closure**;",
    "- dialogue index: **744 immutable records / COMPLETE-VERIFIED / QA PASS**;\n- exact source speaker labels: **38**; cross-page records: **3**; zero-dialogue scenes: **15**;\n- character/entity index: **READY-NEXT**;",
    "work README gates")
t = re.sub(r"## Exact next activity\n\n.*?\n?$", "## Exact next activity\n\n" + NEXT + "\n", t, flags=re.S)
p.write_text(t, encoding="utf-8")

# Project handover.
p = W / "PROJECT_HANDOVER.md"; t = p.read_text(encoding="utf-8")
t = must_replace(t,
    "- dialogue index: **READY-NEXT**;\n- character/entity index: **BLOCKED pending dialogue closure**;",
    "- dialogue index: **744 immutable records / COMPLETE-VERIFIED / QA PASS**;\n- exact speaker labels: **38**; delimiter distribution: **`:—` 736 / `:` 8**;\n- cross-page dialogue records: **3**; zero-dialogue scenes: **15**;\n- anomalous non-colon candidates promoted: **0/16**; inferred-speaker assignments: **0**;\n- character/entity index: **READY-NEXT**;",
    "handover gates")
t = re.sub(r"## Exact next activity\n\n> \*\*.*?\*\*\n?$", "## Exact next activity\n\n> **" + NEXT + "**\n", t, flags=re.S)
p.write_text(t, encoding="utf-8")

# Next-chat prompt becomes character/entity indexing.
(W / "NEXT_CHAT_PROMPT.md").write_text(f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / character-entity index

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Closed authority

- controlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages / first edition 1978 / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`;
- canonical Tamil: **87/87 COMPLETE-VERIFIED**;
- scene headings / scene derivatives: **72/72 / 72/72 COMPLETE-VERIFIED**;
- scene boundary QA: **PASS — 0 gaps / 0 overlaps / 82/82 screenplay pages**;
- immutable dialogue index: **744 records / COMPLETE-VERIFIED / QA PASS**;
- exact source speaker labels: **38**;
- delimiter distribution: **`:—` 736 / `:` 8**;
- cross-page dialogue records: **3**;
- zero-dialogue scenes: **15**;
- anomalous non-colon candidates promoted to dialogue: **0/16**;
- source-unlabelled blocks assigned a speaker: **0**.

The 8 `:` records are genuine source-labelled turns whose complete dialogue text is `—`. The three cross-page records remain single turns across PDF 48→49 (`சடையன்`), PDF 68→69 (`சடையன்`) and PDF 85→86 (`விங்கன்`).

Do not rewrite the closed Tamil, scene or dialogue layers.

## Exact next activity

> **{NEXT}**
''', encoding="utf-8")

# Metadata.
p = W / "metadata.yaml"; t = p.read_text(encoding="utf-8")
t = must_replace(t, "  dialogue_index: ready-next\n  character_entity_index: blocked", "  dialogue_index: complete-verified-744-records\n  dialogue_record_count: 744\n  dialogue_distinct_exact_speaker_labels: 38\n  dialogue_cross_page_records: 3\n  dialogue_zero_record_scenes: 15\n  dialogue_qa_path: works/vandikkaran-magan/notes/dialogue-index-qa.json\n  character_entity_index: ready-next", "metadata dialogue state")
t = re.sub(r'^next_action: .*$', 'next_action: "' + NEXT.replace('"','\\"') + '"', t, flags=re.M)
p.write_text(t, encoding="utf-8")

# Mapping status only; retain structural detail.
p = W / "mapping.md"; t = p.read_text(encoding="utf-8")
t = must_replace(t, "- dialogue index: **READY-NEXT**;", "- dialogue index: **744 immutable records / COMPLETE-VERIFIED / QA PASS**;\n- exact speaker labels / cross-page dialogue / zero-dialogue scenes: **38 / 3 / 15**;\n- character/entity index: **READY-NEXT**;", "mapping dialogue state")
t = re.sub(r"## Exact next activity\n\n.*?\n?$", "## Exact next activity\n\n**" + NEXT + "**\n", t, flags=re.S)
p.write_text(t, encoding="utf-8")

# Scene README downstream gate.
p = W / "scenes/README.md"; t = p.read_text(encoding="utf-8")
t = must_replace(t,
    "Scene-text derivatives are **COMPLETE-VERIFIED**. Dialogue indexing may now open. Character/entity indexing remains blocked until dialogue indexing closes.",
    "Scene-text derivatives remain **COMPLETE-VERIFIED**. The downstream immutable dialogue layer is now **744 records / COMPLETE-VERIFIED / QA PASS**. Character/entity indexing is READY-NEXT.",
    "scene README downstream")
p.write_text(t, encoding="utf-8")

# Canonical transcription README downstream note.
p = W / "transcription/README.md"; t = p.read_text(encoding="utf-8")
t = re.sub(r"## Next\n\n.*?\n?$", "## Downstream state\n\nThe 72/72 scene layer remains COMPLETE-VERIFIED. The immutable dialogue index is now **744 records / COMPLETE-VERIFIED / QA PASS**, with 38 exact source labels and 3 cross-page records. Character/entity indexing is READY-NEXT; canonical Tamil remains closed.\n", t, flags=re.S)
p.write_text(t, encoding="utf-8")

# Repository registry JSON.
p = ROOT / "data/works.json"
works = json.loads(p.read_text(encoding="utf-8"))
entry = next((x for x in works if x.get("id") == "vandikkaran-magan"), None)
assert entry is not None
entry["scene_headings_observed"] = 72
entry["tamil_transcription"] = "complete-verified"
entry["tamil_first_pass_complete"] = True
entry["tamil_transcription_verified_pages"] = 87
entry["tamil_transcription_draft_pages"] = 0
entry["tamil_fidelity_audit"] = "complete"
sd = entry.setdefault("structured_derivatives", {})
sd.update({
    "scene_index": "complete-verified",
    "scene_index_path": "works/vandikkaran-magan/scenes/index.json",
    "scene_records": 72,
    "scene_text_derivatives": "complete-verified",
    "scene_text_files_completed": 72,
    "dialogue_index": "complete-verified",
    "dialogue_index_path": "works/vandikkaran-magan/dialogues/index.json",
    "dialogue_records": 744,
    "dialogue_distinct_source_labels": 38,
    "dialogue_cross_page_records": 3,
    "dialogue_zero_record_scenes": D["zero_dialogue_source_scene_ids"],
    "character_index": "ready-next",
    "next_structured_derivative": "character-entity-index",
})
entry["next_action"] = NEXT
p.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Root README active section.
p = ROOT / "README.md"; t = p.read_text(encoding="utf-8")n
