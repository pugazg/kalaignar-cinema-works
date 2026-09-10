#!/usr/bin/env python3
"""Synchronize current status mirrors after Vandikkaran Magan dialogue closure.

This script changes status/control documents only. It must not rewrite canonical
Tamil, verified scene derivatives, or immutable dialogue records.
"""
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_section(text: str, start: str, end: str | None, replacement: str) -> str:
    a = text.find(start)
    if a < 0:
        raise SystemExit(f"missing section start: {start}")
    if end is None:
        b = len(text)
    else:
        b = text.find(end, a + len(start))
        if b < 0:
            raise SystemExit(f"missing section end: {end}")
    return text[:a] + replacement.rstrip() + "\n\n" + (text[b:] if end is not None else "")


def main() -> None:
    idx = json.loads(read(W / "dialogues" / "index.json"))
    qa = json.loads(read(W / "notes" / "dialogue-index-qa.json"))
    assert idx["status"] == "complete-verified"
    assert idx["dialogue_record_count"] == 744
    assert idx["distinct_exact_speaker_labels"] == 38
    assert idx["delimiter_distribution"] == {":": 8, ":—": 736}
    assert idx["multi_page_dialogue_records"] == 3
    assert len(idx["zero_dialogue_scenes"]) == 15
    assert qa["status"] == "PASS"
    assert qa["dialogue_records"] == 744
    assert qa["reviewed_anomalous_non_colon_candidates"] == 16
    assert qa["anomalous_candidates_promoted_to_dialogue"] == 0
    assert qa["unlabelled_source_blocks_assigned_a_speaker"] == 0
    assert qa["duplicate_dialogue_ids"] == 0
    assert qa["speaker_label_normalizations"] == 0

    # Work-local metadata.
    p = W / "metadata.yaml"
    text = read(p)
    text = re.sub(r"(?m)^  historical_glyph_first_pass_checked_pages: \d+$",
                  "  historical_glyph_first_pass_checked_pages: 87", text)
    old = "  dialogue_index: ready-next\n  character_entity_index: blocked\n"
    new = (
        "  dialogue_index: complete-verified\n"
        "  dialogue_index_path: works/vandikkaran-magan/dialogues/index.json\n"
        "  dialogue_records: 744\n"
        "  dialogue_distinct_exact_speaker_labels: 38\n"
        "  dialogue_zero_record_scenes: 15\n"
        "  dialogue_cross_page_records: 3\n"
        "  dialogue_reviewed_anomalous_non_colon_candidates: 16\n"
        "  dialogue_anomalous_candidates_promoted: 0\n"
        "  dialogue_unlabelled_speaker_assignments: 0\n"
        "  dialogue_qa: PASS\n"
        "  dialogue_qa_path: works/vandikkaran-magan/notes/dialogue-index-qa.json\n"
        "  character_entity_index: ready-next\n"
    )
    if old not in text:
        raise SystemExit("metadata dialogue/character checkpoint drift")
    text = text.replace(old, new, 1)
    text = re.sub(r'(?m)^next_action: ".*"$', 'next_action: "' + NEXT + '"', text)
    write(p, text)

    # Work README: replace current downstream checkpoint and next action only.
    p = W / "README.md"
    text = read(p)
    replacement = f"""## Downstream gates

- dialogue index: **COMPLETE-VERIFIED — 744 immutable records / QA PASS**;
- exact source speaker labels: **38**;
- delimiter distribution: **`:—` 736 / `:` 8**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3**, each retained as one immutable record;
- unlabelled source blocks assigned a speaker: **0**;
- reviewed anomalous non-colon candidates promoted to dialogue: **0/16**;
- character/entity index: **READY-NEXT**;
- song/performance authorship: **BLOCKED pending character/entity closure**;
- English translation: **BLOCKED**;
- reader/export / Reading Room: **BLOCKED**.

See `dialogues/index.json`, `dialogues/README.md`, `notes/unlabelled-block-audit.json`, and `notes/dialogue-index-qa.json`.

## Exact next activity

> **{NEXT}**"""
    text = replace_section(text, "## Downstream gates", None, replacement)
    write(p, text)

    # Scene-layer README now points to the closed downstream dialogue authority.
    p = W / "scenes" / "README.md"
    text = read(p)
    old = (
        "Scene-text derivatives are **COMPLETE-VERIFIED**. Dialogue indexing may now open. "
        "Character/entity indexing remains blocked until dialogue indexing closes."
    )
    new = (
        "Scene-text derivatives remain **COMPLETE-VERIFIED**. The downstream immutable dialogue "
        "index is now **COMPLETE-VERIFIED — 744 records / QA PASS**. Character/entity indexing is **READY-NEXT**."
    )
    if old not in text:
        raise SystemExit("scene README downstream checkpoint drift")
    write(p, text.replace(old, new, 1))

    # Work handover: preserve the closed source/scene sections and replace downstream state.
    p = W / "PROJECT_HANDOVER.md"
    text = read(p)
    replacement = f"""## Derivative gate state

- scene-text derivatives: **COMPLETE-VERIFIED — 72/72 / QA PASS**;
- immutable dialogue index: **COMPLETE-VERIFIED — 744 records / 38 exact labels / QA PASS**;
- delimiter distribution: **`:—` 736 / `:` 8**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3** — each remains one logical record with multi-page provenance;
- reviewed anomalous non-colon candidates: **16/16 excluded from dialogue starts**;
- unlabelled source blocks assigned a speaker: **0**;
- duplicate dialogue IDs / speaker-label normalizations: **0 / 0**;
- dialogue build checkpoint: `a7b80ccac2473b998b40bb05577a439fd970136b`;
- character/entity index: **READY-NEXT**;
- song/performance authorship gate: **BLOCKED pending character/entity closure**;
- English translation: **BLOCKED**;
- reader/export / Reading Room: **BLOCKED**.

The three verified cross-page records are `vandikkaran-magan-s035-d006` (source scene `25`, PDF 48→49), `vandikkaran-magan-s055-d004` (source scene `42-எ`, PDF 68→69), and `vandikkaran-magan-s070-d005` (source scene `54`, PDF 85→86). The 16 non-colon preflight candidates are source-visible punctuation/verse fragments and were not promoted to dialogue. No canonical Tamil or scene file was changed by dialogue construction.

## Exact next activity

> **{NEXT}**"""
    text = replace_section(text, "## Derivative gate state", None, replacement)
    write(p, text)

    # Next-chat prompt: character/entity indexing is the next open gate.
    p = W / "NEXT_CHAT_PROMPT.md"
    prompt = f"""# Next Chat Prompt — வண்டிக்காரன் மகன் / character-entity index

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only. The attached/rendered scan remains canonical authority.

## Durable closed state

- canonical source layer: **87/87 COMPLETE-VERIFIED — PDF 4–90**;
- open source/glyph uncertainty: **0**;
- source-visible scene-heading inventory: **72/72 COMPLETE-VERIFIED**;
- scene derivatives: **72/72 COMPLETE-VERIFIED**;
- scene boundary ownership: **PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps / 0 duplicate ownership**;
- canonical/joined scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- immutable dialogue index: **744 records / 38 exact source speaker labels / COMPLETE-VERIFIED / QA PASS**;
- delimiter distribution: **`:—` 736 / `:` 8**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3**, preserved as single records with page segments;
- reviewed anomalous non-colon candidates promoted: **0/16**;
- unlabelled source blocks assigned a speaker: **0**;
- duplicate dialogue IDs / speaker-label normalizations: **0 / 0**.

Do not reopen the closed Tamil, scene, or dialogue layers without new direct contradictory evidence from the controlling scan.

## Character/entity-index rules

Follow `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` Phase 11. Inventory every exact immutable `speaker_label` first. Character/entity mapping is interpretive metadata only: never rewrite dialogue records, never normalize their source labels, preserve spelling variants and abbreviations, and leave generic roles/voices/collectives explicit when identity is not source-supported. Reused labels such as generic `குரல்`-type labels must not be collapsed automatically.

## Exact next activity

> **{NEXT}**
"""
    write(p, prompt)

    # Machine-readable repository catalogue.
    p = ROOT / "data" / "works.json"
    works = json.loads(read(p))
    item = next((x for x in works if x.get("id") == "vandikkaran-magan"), None)
    if item is None:
        raise SystemExit("vandikkaran-magan missing from data/works.json")
    item.update({
        "structural_mapping": "verified",
        "scene_heading_occurrences_observed": 72,
        "scene_headings_observed": 72,
        "canonical_tamil_first_pass": "complete-87-of-87",
        "canonical_tamil_first_pass_current_through_pdf": 90,
        "canonical_tamil_first_pass_current_through_printed": 86,
        "canonical_tamil_draft_pages": 0,
        "canonical_tamil_verified_pages": 87,
        "canonical_tamil_review_pages": 0,
        "canonical_tamil_open_uncertainty_markers": 0,
        "historical_glyph_first_pass_checked_pages": 87,
        "historical_glyph_final_verified_pages": 87,
        "tamil_transcription": "complete-verified",
        "tamil_first_pass_complete": True,
        "tamil_transcription_through_pdf_page": 90,
        "next_action": NEXT,
    })
    sd = item.setdefault("structured_derivatives", {})
    sd.update({
        "scene_index": "complete-verified",
        "scene_index_path": "works/vandikkaran-magan/scenes/index.json",
        "scene_records": 72,
        "scene_text_derivatives": "complete-verified",
        "scene_text_files_completed": 72,
        "scene_boundary_ownership_qa": "PASS",
        "scene_boundary_gaps": 0,
        "scene_boundary_overlaps": 0,
        "dialogue_index": "complete-verified",
        "dialogue_index_path": "works/vandikkaran-magan/dialogues/index.json",
        "dialogue_records": 744,
        "dialogue_distinct_exact_speaker_labels": 38,
        "dialogue_zero_record_scenes": 15,
        "dialogue_cross_page_records": 3,
        "dialogue_reviewed_anomalous_non_colon_candidates": 16,
        "dialogue_anomalous_candidates_promoted": 0,
        "dialogue_unlabelled_speaker_assignments": 0,
        "dialogue_qa": "PASS",
        "dialogue_qa_path": "works/vandikkaran-magan/notes/dialogue-index-qa.json",
        "character_index": "ready-next",
        "next_structured_derivative": "character-index",
    })
    write(p, json.dumps(works, ensure_ascii=False, indent=2) + "\n")

    # Root README: replace only the active Vandikkaran section.
    p = ROOT / "README.md"
    text = read(p)
    replacement = f"""## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the current active cinema-work source.

- source: **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978**;
- source credits: **`மூலக்கதை அண்ணா` / `திரைக்கதை-வசனம் கலைஞர்`**;
- canonical Tamil source layer: **87/87 COMPLETE-VERIFIED — PDF 4–90 / 0 open uncertainties**;
- scene-heading inventory: **72/72 COMPLETE-VERIFIED**, including source scene `4-எ` at PDF 10; base 1–56, 17 suffix insertions, combined `45-46`;
- scene derivatives: **72/72 COMPLETE-VERIFIED**;
- boundary ownership: **PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps / 0 duplicate ownership**;
- immutable dialogue index: **744 records / 38 exact labels / COMPLETE-VERIFIED / QA PASS**;
- dialogue safeguards: **15 zero-dialogue scenes / 3 cross-page records / 0 unlabelled speaker assignments / 0 of 16 reviewed non-colon candidates promoted**;
- character/entity index: **READY-NEXT**;
- song/performance, English and reader layers: **gated downstream**.

**Next:** {NEXT}"""
    text = replace_section(text, "## வண்டிக்காரன் மகன் status", "## நாம் status", replacement)
    write(p, text)

    # Master handover: update only Vandikkaran's current bullet and active-work sentence.
    p = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = read(p)
    text, n1 = re.subn(
        r"(?m)^- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*?$",
        "- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; source-visible scene headings **72/72**; scene derivatives **72/72 COMPLETE-VERIFIED**; boundary ownership **PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps**; immutable dialogue index **744 records / 38 exact labels / COMPLETE-VERIFIED / QA PASS**; **3** cross-page records; **15** zero-dialogue scenes; **0** unlabelled speaker assignments; character/entity index **READY-NEXT**.",
        text,
        count=1,
    )
    if n1 != 1:
        raise SystemExit("master handover Vandikkaran bullet drift")
    text, n2 = re.subn(
        r"(?m)^Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*$",
        "Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: canonical Tamil and the 72-scene derivative layer remain closed; its immutable dialogue index is now COMPLETE-VERIFIED at 744 records with whole-work QA PASS, and character/entity indexing is READY-NEXT.**",
        text,
        count=1,
    )
    if n2 != 1:
        raise SystemExit("master handover active-work sentence drift")
    write(p, text)

    # Repository status audit: update only Vandikkaran-specific current state.
    p = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = read(p)
    text, n = re.subn(
        r"(?m)^\*\*PASS for the current repository-wide checkpoint\.\*\* Vandikkaran Magan .*?$",
        "**PASS for the current repository-wide checkpoint.** Vandikkaran Magan is now closed through immutable dialogue indexing: **744 records / 38 exact source labels / QA PASS**, with 15 legitimate zero-dialogue scenes, 3 cross-page records preserved whole, 0 unlabelled speaker assignments, and 0/16 reviewed non-colon candidates promoted. Character/entity indexing is READY-NEXT. Ammayappan and the other recorded work checkpoints remain preserved.",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit("status result paragraph drift")
    text, n = re.subn(
        r"(?m)^\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*?$",
        "| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 744 dialogue records / 38 exact labels; QA PASS** | not-started | not-started |",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit("status matrix row drift")
    checkpoint = f"""## Vandikkaran Magan current checkpoint

- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- source-visible scene-heading inventory: **72/72**, including PDF 10 `காட்சி — 4 எ.` / source scene `4-எ`;
- scene derivatives: **72/72 COMPLETE-VERIFIED**;
- boundary ownership: **PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps / 0 duplicate ownership**;
- canonical/joined scene-body SHA-256: `84227c9855f3de942c8f1c240f9e6ddeee2d13f348fdda14b7712a81c4cfc19a`;
- immutable dialogue index: **744 records / 38 exact source labels / COMPLETE-VERIFIED / QA PASS**;
- delimiters: **`:—` 736 / `:` 8**;
- zero-dialogue scenes: **15**;
- cross-page dialogue records: **3** — source scenes `25`, `42-எ`, `54`;
- reviewed anomalous non-colon candidates promoted: **0/16**;
- unlabelled source blocks assigned a speaker: **0**;
- duplicate dialogue IDs / speaker-label normalizations: **0 / 0**;
- canonical Tamil or scene files modified by dialogue build: **0**;
- character/entity index: **READY-NEXT**.

**Next production phase:** {NEXT}"""
    text = replace_section(text, "## Vandikkaran Magan current checkpoint", "## Naam current checkpoint", checkpoint)
    text, n = re.subn(
        r"(?m)^Vandikkaran Magan is the active production work\. .*?$",
        "Vandikkaran Magan is the active production work. Its canonical Tamil/source gates and **72/72 scene derivatives remain COMPLETE-VERIFIED**; the immutable dialogue index is now **COMPLETE-VERIFIED — 744 records / 38 exact labels / QA PASS**. **Next: character/entity indexing from the immutable exact-label inventory.**",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit("status conclusion drift")
    write(p, text)

    # Fail closed if any active Vandikkaran mirror still advertises dialogue indexing as next.
    current_files = [
        W / "metadata.yaml", W / "README.md", W / "PROJECT_HANDOVER.md",
        W / "NEXT_CHAT_PROMPT.md", ROOT / "README.md",
        ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
        ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md",
    ]
    bad_phrases = [
        "dialogue index: **READY-NEXT**",
        "dialogue_index: ready-next",
        '"next_structured_derivative": "dialogue-index"',
        "**Next:** Build the immutable dialogue index",
        "**Next: immutable dialogue indexing",
    ]
    for path in current_files:
        body = read(path)
        for phrase in bad_phrases:
            if phrase in body:
                raise SystemExit(f"stale Vandikkaran checkpoint in {path}: {phrase}")

    print(json.dumps({
        "status": "PASS",
        "dialogue_records": 744,
        "exact_labels": 38,
        "cross_page_records": 3,
        "zero_dialogue_scenes": 15,
        "next": "character-entity-index",
        "canonical_or_scene_files_modified": 0,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
