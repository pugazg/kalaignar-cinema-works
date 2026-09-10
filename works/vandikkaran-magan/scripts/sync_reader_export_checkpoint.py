#!/usr/bin/env python3
"""Synchronize the completed Vandikkaran Magan English reader/export checkpoint."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "vandikkaran-magan"
EDITION = WORK / "editions" / "en"
MANIFEST = EDITION / "manifest.json"

NEXT = (
    "Build and verify the deterministic source-linked Reading Room payload for `வண்டிக்காரன் மகன்` from the closed "
    "72-scene Tamil/source structure and the complete-verified 1,181-unit English reader/export. Preserve source scene IDs and "
    "PDF/printed provenance; retain all 773 immutable dialogue links, 27 source-unlabelled spoken units, 58 cross-page units "
    "and all 9 verified song/performance occurrence identities; preserve unresolved item-level lyric authorship; do not modify "
    "closed Tamil, scene, dialogue, character, song/performance or translation authorities; and do not modify the separate "
    "Reading Room implementation repository unless explicitly authorized."
)


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_section(text: str, heading: str, body: str) -> str:
    pattern = re.compile(rf"^{re.escape(heading)}\n.*?(?=^## |\Z)", re.M | re.S)
    replacement = heading + "\n\n" + body.rstrip() + "\n\n"
    if not pattern.search(text):
        raise RuntimeError(f"Missing section {heading!r}")
    return pattern.sub(replacement, text, count=1)


def update_metadata() -> None:
    path = WORK / "metadata.yaml"
    text = path.read_text(encoding="utf-8")
    marker = "  english_translation:"
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError("metadata.yaml missing english_translation marker")
    prefix = text[:idx]
    tail = f'''  english_translation: complete-verified
  english_translation_index_path: works/vandikkaran-magan/translations/index.json
  english_translation_verified_scenes: 72
  english_translation_batch_size_scenes: 20
  english_translation_units: 1181
  english_translation_unit_kind_counts: dialogue=800,performance-cue=10,song=53,stage-direction=316,written-text=2
  english_translation_immutable_dialogue_links: 773
  english_translation_source_unlabelled_spoken_units: 27
  english_translation_performance_occurrence_links: 9
  english_translation_cross_page_units: 58
  english_translation_latest_batch_qa_path: works/vandikkaran-magan/translations/batch-061-072-qa.json
  english_translation_latest_batch_review_path: works/vandikkaran-magan/translations/BATCH_061_072_REVIEW.md
  english_translation_final_qa_path: works/vandikkaran-magan/translations/FINAL_TRANSLATION_QA.md
  reader_export: complete-verified
  english_reader_preflight: complete-pass
  english_reader_preflight_report_path: works/vandikkaran-magan/editions/en/PREFLIGHT_QA_REPORT.md
  english_reader_edition_directory: works/vandikkaran-magan/editions/en
  english_reader_qa: PASS
  english_reader_qa_path: works/vandikkaran-magan/editions/en/QA_REPORT.md
  english_reader_qa_units: 1181
  english_reader_qa_dialogue_links: 773
  english_reader_qa_source_unlabelled_spoken_units: 27
  english_reader_qa_cross_page_units: 58
  english_reader_qa_song_occurrence_links: 9
  english_reader_manifest_path: works/vandikkaran-magan/editions/en/manifest.json
  reading_room_integration: ready-next
next_action: "{NEXT}"
'''
    write(path, prefix + tail)


def update_work_docs(manifest: dict) -> None:
    md_sha = manifest["outputs"]["reader-edition.md"]["sha256"]
    html_sha = manifest["outputs"]["reader-edition.html"]["sha256"]
    json_sha = manifest["outputs"]["reader-edition.json"]["sha256"]
    input_sha = manifest["authoritative_input_aggregate_sha256"]

    readme = f'''# வண்டிக்காரன் மகன்

Source-led archival workspace for the 1978 first-edition dialogue/screenplay booklet **`வண்டிக்காரன் மகன்`**.

## Source authority

Controlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**. The image-only scan is canonical authority.

## Current verified state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 unresolved**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue authority: **773 records / 38 exact labels / QA PASS** — **744/744 legacy IDs preserved + 29 append-only repairs**;
- character/entity index: **32 entities — 15 characters / 14 roles / 3 collectives / 38/38 labels / 773/773 records / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS** — 6 bounded Tamil bodies + 3 cue-only;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance occurrences / 0 inferred speakers**;
- English reader/export: **COMPLETE-VERIFIED / QA PASS** — deterministic Markdown, HTML and JSON under `editions/en/`;
- reader authoritative-input aggregate SHA-256: `{input_sha}`;
- reader output SHA-256: Markdown `{md_sha}`, HTML `{html_sha}`, JSON `{json_sha}`;
- Reading Room integration payload: **READY-NEXT / not yet built**.

## Exact next activity

> **{NEXT}**
'''
    write(WORK / "README.md", readme)

    handover = f'''# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**.

## Durable closed state

- canonical source: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps**;
- dialogue authority: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**; legacy IDs **744/744 preserved**, append-only repairs **29**, action-only exclusions **2**;
- character/entity: **32 entities / 38/38 labels / 773/773 dialogue records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**; 6 bounded bodies / 3 cue-only / 0 source-attributed + 6 unresolved item-level lyric authorships;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 immutable links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance identities / 0 inferred speakers**;
- reader/export: **COMPLETE-VERIFIED / QA PASS** — `editions/en/reader-edition.md`, `.html`, `.json`, `QA_REPORT.md`, `manifest.json`;
- reader input aggregate SHA-256: `{input_sha}`;
- reader output SHA-256: Markdown `{md_sha}`, HTML `{html_sha}`, JSON `{json_sha}`;
- Reading Room integration: **READY-NEXT / payload not yet built / separate site not modified**.

Do not reopen or rewrite closed Tamil, scene, immutable dialogue-record, character-mapping, song/performance, translation or reader authority without new direct contradictory source evidence. Historical 744 counts refer only to the preserved pre-reconciliation ID set.

## Exact next activity

> **{NEXT}**
'''
    write(WORK / "PROJECT_HANDOVER.md", handover)

    prompt = f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / Reading Room payload

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only.

## Durable state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / QA PASS** — 744 legacy IDs preserved + 29 append-only repairs;
- characters/entities: **32 / 38/38 labels / 773/773 records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- English translation: **72/72 COMPLETE-VERIFIED / 1,181 units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 verified performance occurrence identities / 0 inferred speakers**;
- final English QA: `translations/FINAL_TRANSLATION_QA.md` — **PASS**;
- reader/export: **COMPLETE-VERIFIED / QA PASS** under `editions/en/`;
- reader manifest: `editions/en/manifest.json`, authoritative-input aggregate `{input_sha}`;
- reader SHA-256: Markdown `{md_sha}`, HTML `{html_sha}`, JSON `{json_sha}`;
- Reading Room payload: **not built**; separate Reading Room implementation repository: **not authorized by this checkpoint**.

Do not reopen or rewrite closed canonical Tamil, scene derivatives, reconciled immutable dialogue records, character/entity mappings, song/performance records, English translation records or verified reader outputs without new direct contradictory source evidence.

## Exact next activity

> **{NEXT}**
'''
    write(WORK / "NEXT_CHAT_PROMPT.md", prompt)

    mapping_path = WORK / "mapping.md"
    mapping = mapping_path.read_text(encoding="utf-8")
    mapping = replace_section(mapping, "## Exact next activity", f'''English translation is now **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS** at **1,181 units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 verified performance occurrence identities**. The deterministic English reader/export is **COMPLETE-VERIFIED / QA PASS** under `editions/en/`.

**{NEXT}**''')
    write(mapping_path, mapping)

    trans_readme = f'''# வண்டிக்காரன் மகன் — canonical Tamil transcription

The rendered scan is the controlling source. The canonical source layer is closed.

## Closed checkpoint

- transcription scope: **PDF 4–90 / 87 pages**;
- first pass / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- final-pass corrections: **0**;
- unresolved glyph holds / open uncertainty markers: **0 / 0**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**.

## Downstream state

The reconciled immutable dialogue authority is **773 records / 38 exact source labels / QA PASS**, preserving all **744/744** legacy IDs and adding **29** append-only repaired IDs. Character/entity coverage is **773/773**; song/performance is **9/9** source-only QA PASS; English translation is **72/72 COMPLETE-VERIFIED / 1,181 units**; deterministic English reader/export is **COMPLETE-VERIFIED / QA PASS**. Canonical Tamil remains unchanged.

**Next:** {NEXT}
'''
    write(WORK / "transcription" / "README.md", trans_readme)

    dialogue_readme = f'''# வண்டிக்காரன் மகன் — immutable dialogue layer

**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**

Built from the closed 72/72 source-led scene derivatives without rewriting canonical Tamil or scene files. A late structural-collision audit corrected a parser defect that had treated some explicit speaker-labelled lines ending in parenthetical action as stage directions.

## Coverage

- immutable dialogue records: **773**;
- legacy IDs preserved: **744/744**; append-only repair records: **29**;
- exact source speaker labels: **38**;
- zero-dialogue scenes: **15**; cross-page records: **3**;
- delimiters: **`:—` 765 / `:` 8**;
- 31 structural collisions reviewed: **29 spoken records restored / 2 action-only labels excluded**;
- unlabelled text assigned to speakers: **0**; label normalizations: **0**.

See `../notes/dialogue-structural-collision-audit.json` and `../notes/dialogue-index-qa.json`.

## Downstream

Character/entity and song/performance layers remain closed against this 773-record authority. English translation links **773/773 exactly once** and is **72/72 COMPLETE-VERIFIED**; deterministic English reader/export is **COMPLETE-VERIFIED / QA PASS** without modifying this immutable layer.

**Next:** {NEXT}
'''
    write(WORK / "dialogues" / "README.md", dialogue_readme)

    character_readme = f'''# வண்டிக்காரன் மகன் — character/entity index

**Status:** **COMPLETE-VERIFIED / RECONCILED / QA PASS**

This interpretive layer maps the reconciled immutable dialogue authority without rewriting source speaker labels or dialogue text.

## Coverage

- immutable dialogue records: **773/773 mapped exactly once**;
- exact source speaker labels: **38/38 mapped**;
- entities: **32** — **15 named characters / 14 generic roles / 3 collectives**;
- verified / review / unresolved entities: **32 / 0 / 0**;
- unmapped labels / records: **0 / 0**;
- upstream dialogue records modified: **0**.

Variant and voice mappings exist only here as interpretive metadata. `லிங்கன்` is not collapsed into `விங்கன்`; `ஜம்பு` is not collapsed into `ஜம்புலிங்க பூபதி`; generic labels remain categorical.

## Downstream

Song/performance is closed at 9/9 source-visible occurrences; English translation is **72/72 COMPLETE-VERIFIED**, and deterministic English reader/export is **COMPLETE-VERIFIED / QA PASS**. This character/entity layer was not rewritten by either downstream phase.

**Next:** {NEXT}
'''
    write(WORK / "characters" / "README.md", character_readme)

    songs_readme = f'''# வண்டிக்காரன் மகன் — song / performance layer

**Status:** **COMPLETE-VERIFIED-SOURCE-ONLY / AUTHORSHIP GATE CLOSED / QA PASS**

- source-visible performance occurrences: **9/9**;
- full or clearly bounded Tamil song/lyric bodies: **6**;
- cue-only / non-lyric performance occurrences: **3**;
- item-level source-attributed lyric authorship: **0**;
- unresolved item-level lyric authorship: **6**;
- non-lyric records where lyric authorship is not applicable: **3**.

PDF 88 prints `பாடல்கள்: கவிஞர் வாலி`; it remains film-level metadata and is not promoted item-by-item. No missing lyric or chant text is reconstructed. English translation represents **9/9** occurrence identities across **66** source-linked units without changing item-level authorship. The deterministic reader/export is **COMPLETE-VERIFIED / QA PASS** and preserves those dispositions.

**Next:** {NEXT}
'''
    write(WORK / "songs" / "README.md", songs_readme)

    translation_readme = f'''# வண்டிக்காரன் மகன் — English translation

**Status:** **COMPLETE-VERIFIED / 72 OF 72 / WHOLE-WORK QA PASS**

- verified scenes: **72/72**;
- cumulative translation units: **1,181**;
- unit kinds: **dialogue=800, performance-cue=10, song=53, stage-direction=316, written-text=2**;
- immutable dialogue links: **773/773 exactly once**;
- source-unlabelled spoken units: **27**, with **0 inferred speakers**;
- unique song/performance occurrence links: **9/9** — `perf-001` through `perf-009`;
- cross-page units: **58**;
- final batch: **archive scenes 61–72 / PASS / 105 of 105 immutable dialogue records linked exactly once**;
- upstream source-layer mutations caused by translation: **0**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS**, `../editions/en/`.

See `batch-061-072-qa.json`, `BATCH_061_072_REVIEW.md`, `FINAL_TRANSLATION_QA.md`, `records/scene-061.json` through `records/scene-072.json`, and `index.json`.

## Next

{NEXT}
'''
    write(WORK / "translations" / "README.md", translation_readme)


def update_data_works() -> None:
    path = ROOT / "data" / "works.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    row = next((r for r in data if r.get("id") == "vandikkaran-magan"), None)
    if row is None:
        raise RuntimeError("data/works.json missing vandikkaran-magan")
    sd = row.setdefault("structured_derivatives", {})
    sd.update({
        "english_translation": "complete-verified",
        "translation_index_path": "works/vandikkaran-magan/translations/index.json",
        "translation_scenes_verified": 72,
        "translation_units": 1181,
        "translation_verified_units": 1181,
        "translation_review_units": 0,
        "translation_draft_units": 0,
        "translation_unit_kind_counts": {"dialogue":800,"performance_cue":10,"song":53,"stage_direction":316,"written_text":2},
        "translation_dialogue_source_records_linked": 773,
        "translation_source_unlabelled_spoken_units": 27,
        "translation_cross_page_units": 58,
        "translation_song_occurrence_links": 9,
        "english_reader_preflight": "complete-pass",
        "english_reader_preflight_report_path": "works/vandikkaran-magan/editions/en/PREFLIGHT_QA_REPORT.md",
        "reader_export": "complete-verified",
        "english_reader_edition": "complete-verified",
        "english_reader_edition_directory": "works/vandikkaran-magan/editions/en",
        "english_reader_qa": "PASS",
        "english_reader_qa_units": 1181,
        "english_reader_qa_dialogue_links": 773,
        "english_reader_qa_source_unlabelled_spoken_units": 27,
        "english_reader_qa_cross_page_units": 58,
        "english_reader_qa_song_occurrence_links": 9,
        "reading_room_integration": "ready-next",
        "next_structured_derivative": "reading-room-integration",
    })
    row["next_action"] = NEXT
    write(path, json.dumps(data, ensure_ascii=False, indent=2))


def update_root_readme(manifest: dict) -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    body = f'''`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` now has a **complete-verified Tamil + structured + English reader checkpoint**.

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance occurrences**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS** — Markdown / HTML / JSON / manifest under `works/vandikkaran-magan/editions/en/`;
- reader input aggregate SHA-256: `{manifest['authoritative_input_aggregate_sha256']}`;
- Reading Room payload: **READY-NEXT / site not modified**.

**Next:** {NEXT}'''
    text = replace_section(text, "## வண்டிக்காரன் மகன் status", body)
    write(path, text)


def update_master_handover() -> None:
    path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"^- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* —.*$",
        "- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72**; dialogues **773 / 38 labels / reconciled QA PASS**; characters **32 / 38/38 / 773/773**; song/performance **9/9 source-only QA PASS**; English **72/72 COMPLETE-VERIFIED / 1,181 units / 773 dialogue links / 27 source-unlabelled / 58 cross-page / 9/9 performance identities**; deterministic English reader/export **QA PASS**; Reading Room payload ready-next.",
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(
        r"Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*",
        "Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: source/Tamil, scene, reconciled dialogue, character, song/performance and English translation are closed; deterministic English reader/export is complete-verified with QA PASS. The next repository-internal phase is the source-linked Reading Room payload; the separate site remains unmodified.**",
        text,
        count=1,
        flags=re.S,
    )
    write(path, text)


def update_status_audit(manifest: dict) -> None:
    path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = path.read_text(encoding="utf-8")
    result = f'''**PASS for the current repository-wide checkpoint.** Vandikkaran Magan English translation is **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS** at **1,181 units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 verified performance occurrence identities**. Its deterministic English reader/export is also **COMPLETE-VERIFIED / QA PASS** with every verified translation unit rendered exactly once in Markdown and HTML and round-tripped exactly once in JSON. Reader authoritative-input aggregate SHA-256 is `{manifest['authoritative_input_aggregate_sha256']}`. All closed Tamil/scene/dialogue/character/song authorities remain unchanged.

The scene-3 post-closure source form `பூங் ; என்ன அண்ணா...என்ன விசேஷம்.......` remains a distinct பூங்காவனம் dialogue unit with its semicolon preserved exactly. Scene 5 `திரு; ...` remains the other source-explicit non-colon speaker delimiter. Neither form is normalized to a colon.'''
    text = replace_section(text, "## Result", result)

    text = re.sub(
        r"^\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*$",
        "| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 773 dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **72/72 COMPLETE-VERIFIED / 1,181 units / 773 dialogue links / 27 unlabelled / 58 cross-page / 9/9 performance IDs** | **English reader/export QA PASS; Reading Room ready-next** |",
        text,
        count=1,
        flags=re.M,
    )

    checkpoint = f'''- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue index: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level source-attributed lyricists: **0**; unresolved item-level lyric authorships: **6**;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 unique performance occurrence identities**;
- final English batch: **61–72 / PASS — 172 units / 105 immutable dialogue links / 6 source-unlabelled spoken units / perf-009 linked / 0 provenance fallbacks**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS** — all 1,181 units exactly once in Markdown/HTML and exact JSON round-trip;
- reader output SHA-256: Markdown `{manifest['outputs']['reader-edition.md']['sha256']}`, HTML `{manifest['outputs']['reader-edition.html']['sha256']}`, JSON `{manifest['outputs']['reader-edition.json']['sha256']}`;
- upstream canonical Tamil / scene / dialogue-record / character-mapping / song-record mutation from English/reader phases: **0**.

**Next production phase:** {NEXT}'''
    text = replace_section(text, "## Vandikkaran Magan current checkpoint", checkpoint)

    conclusion = f'''Vandikkaran Magan is the active production work. Its source/Tamil, 72-scene, reconciled 773-dialogue, 32-entity, 9-occurrence song/performance, 72-scene English translation and deterministic reader/export authorities are closed with QA PASS. **Next: build and verify the source-linked Reading Room payload inside this repository; do not apply it to the separate site without explicit authorization.**'''
    text = replace_section(text, "## Conclusion", conclusion)
    write(path, text)


def active_stale_gate() -> None:
    paths = [
        WORK / "README.md", WORK / "PROJECT_HANDOVER.md", WORK / "NEXT_CHAT_PROMPT.md", WORK / "mapping.md", WORK / "metadata.yaml",
        WORK / "transcription" / "README.md", WORK / "dialogues" / "README.md", WORK / "characters" / "README.md", WORK / "songs" / "README.md", WORK / "translations" / "README.md",
        ROOT / "README.md", ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md", ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md",
    ]
    stale = ["60/72", "1009 units", "1,009 units", "668 immutable", "668 dialogue", "verified-through-scene-060", "remaining archive scene ordinals 61–72", "pending final English closure", "gated until final English closure"]
    bad = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for token in stale:
            if token in text:
                bad.append(f"{path.relative_to(ROOT)} :: {token}")
    if bad:
        raise RuntimeError("Stale active checkpoint markers remain:\n" + "\n".join(bad))


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("status") != "complete-verified" or manifest.get("qa_status") != "PASS":
        raise RuntimeError("Reader manifest is not complete-verified/PASS")
    if manifest.get("translation_units") != 1181 or manifest.get("immutable_dialogue_records_linked") != 773:
        raise RuntimeError("Reader manifest counts drifted")
    update_metadata()
    update_work_docs(manifest)
    update_data_works()
    update_root_readme(manifest)
    update_master_handover()
    update_status_audit(manifest)
    active_stale_gate()
    print("Vandikkaran Magan reader/export checkpoint synchronization: PASS")


if __name__ == "__main__":
    main()
