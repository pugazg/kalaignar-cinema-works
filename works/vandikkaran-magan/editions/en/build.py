#!/usr/bin/env python3
"""Build and QA the deterministic Vandikkaran Magan English reader/export layer."""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "vandikkaran-magan"
TRANSLATIONS = WORK / "translations"
TRANS_INDEX = TRANSLATIONS / "index.json"
TRANS_RECORDS = TRANSLATIONS / "records"
SCENE_INDEX = WORK / "scenes" / "index.json"
SCENES = WORK / "scenes"
DIALOGUE_INDEX = WORK / "dialogues" / "index.json"
DIALOGUES = WORK / "dialogues" / "records"
SONG_INDEX = WORK / "songs" / "index.json"
SONG_INVENTORY = WORK / "songs" / "inventory.json"
OUT = WORK / "editions" / "en"

SOURCE_SHA256 = "03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253"
EXPECTED_SCENES = 72
EXPECTED_UNITS = 1181
EXPECTED_KINDS = {
    "dialogue": 800,
    "performance-cue": 10,
    "song": 53,
    "stage-direction": 316,
    "written-text": 2,
}
EXPECTED_DIALOGUE_RECORDS = 773
EXPECTED_UNLABELLED = 27
EXPECTED_CROSS_PAGE = 58
EXPECTED_PERFORMANCE_LINKED_UNITS = 66
EXPECTED_PERFORMANCE_IDS = [f"vandikkaran-magan-perf-{i:03d}" for i in range(1, 10)]
UNIT_RE = re.compile(r"^vandikkaran-magan-en-s(\d{3})-u\d{3}$")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
SYNTHETIC_END_RE = re.compile(r"^\s*[\[(]?\s*Scene\s+ends?\.?\s*[\])]?\s*$", re.I)


class QAError(RuntimeError):
    pass


def ensure(ok: bool, message: str) -> None:
    if not ok:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.as_posix()):
        ensure(path.exists(), f"Missing authoritative input {path.relative_to(ROOT)}")
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def collect_ids(node: Any, prefix: str) -> set[str]:
    result: set[str] = set()
    if isinstance(node, dict):
        value = node.get("id")
        if isinstance(value, str) and value.startswith(prefix):
            result.add(value)
        for child in node.values():
            result.update(collect_ids(child, prefix))
    elif isinstance(node, list):
        for child in node:
            result.update(collect_ids(child, prefix))
    return result


def translation_payload(unit: dict[str, Any]) -> tuple[str, list[str] | None]:
    tr = unit.get("translation")
    ensure(isinstance(tr, dict), f"{unit.get('id')} has malformed translation")
    text, lines = tr.get("english_text"), tr.get("english_lines")
    ensure(isinstance(text, str) ^ isinstance(lines, list), f"{unit.get('id')} must have exactly one English payload")
    if isinstance(text, str):
        ensure(text.strip(), f"{unit.get('id')} has empty English text")
        return text, None
    ensure(lines and all(isinstance(line, str) and line.strip() for line in lines), f"{unit.get('id')} has malformed English lines")
    return "\n".join(lines), lines


def page_label(provenance: list[dict[str, int]]) -> str:
    if len(provenance) == 1:
        p = provenance[0]
        return f"PDF {p['pdf_page']} / printed {p['printed_page']}"
    a, b = provenance[0], provenance[-1]
    return f"PDF {a['pdf_page']}→{b['pdf_page']} / printed {a['printed_page']}→{b['printed_page']}"


def dialogue_records(scene: int) -> list[dict[str, Any]]:
    path = DIALOGUES / f"scene-{scene:03d}.json"
    ensure(path.exists(), f"Missing dialogue shard {path.relative_to(ROOT)}")
    data = load_json(path)
    records = data if isinstance(data, list) else data.get("records") if isinstance(data, dict) else None
    ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
    return records


def authoritative_input_paths() -> list[Path]:
    paths = [TRANS_INDEX, SCENE_INDEX, DIALOGUE_INDEX, SONG_INDEX, SONG_INVENTORY]
    paths.extend(TRANS_RECORDS / f"scene-{n:03d}.json" for n in range(1, EXPECTED_SCENES + 1))
    paths.extend(DIALOGUES / f"scene-{n:03d}.json" for n in range(1, EXPECTED_SCENES + 1))
    paths.extend(SCENES / f"scene-{n:03d}.md" for n in range(1, EXPECTED_SCENES + 1))
    return paths


def render_markdown(records: list[dict[str, Any]]) -> str:
    out = [
        "# Vandikkaran Magan — English Reader Edition",
        "",
        "**Tamil title:** வண்டிக்காரன் மகன்  ",
        "**Status:** complete-verified source-linked English derivative  ",
        "**English authority:** `works/vandikkaran-magan/translations/records/`  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`",
        "",
        f"> Editorial note: This deterministic reader renders all {EXPECTED_UNITS:,} verified English translation units in source order without rewriting them. Exact Tamil speaker labels remain visible for source-labelled dialogue; source-unlabelled speech remains unassigned. Song/performance occurrence links retain their verified source-only evidence and unresolved item-level authorship where applicable. Structural `★` separators are not converted into prose.",
        "",
        "## Contents",
        "",
    ]
    for record in records:
        source_id = record["source_scene_id"]
        ordinal = record["scene_ordinal"]
        out.append(f"- [Source scene {source_id} — archive {ordinal}](#archive-scene-{ordinal})")
    out.extend(["", "---", ""])

    for record in records:
        ordinal = record["scene_ordinal"]
        source_id = record["source_scene_id"]
        heading = record["source_heading"]
        location = record.get("location")
        out.extend([f'<a id="archive-scene-{ordinal}"></a>', f"## {heading}", "", f"*Archive scene {ordinal} / source scene ID `{source_id}`*", ""])
        if location:
            out.extend([f"**Source location:** {location}", ""])
        for unit in record["units"]:
            uid, kind, source = unit["id"], unit["kind"], unit["source"]
            text, lines = translation_payload(unit)
            out.append(f"<!-- unit:{uid}; source:{page_label(source['page_provenance'])}; source-scene:{source_id} -->")
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                if speaker:
                    out.append(f"**{speaker}**  ")
                out.extend([text, ""])
            elif kind == "stage-direction":
                out.extend([f"*{text}*", ""])
            elif kind == "performance-cue":
                out.extend(["*Performance cue*  ", f"*{text}*", ""])
            elif kind == "song":
                out.append("*Song / lyrical performance*  ")
                out.extend([*(f"> {line}  " for line in lines), ""] if lines else [f"> {text}", ""])
            elif kind == "written-text":
                out.extend(["*Written text*  ", f"> {text}", ""])
            else:
                raise QAError(f"Unsupported render kind {kind!r}")
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(records: list[dict[str, Any]]) -> str:
    nav = " ".join(f'<a href="#archive-scene-{r["scene_ordinal"]}">{html.escape(str(r["source_scene_id"]))}</a>' for r in records)
    sections: list[str] = []
    for record in records:
        ordinal = record["scene_ordinal"]
        source_id = record["source_scene_id"]
        body = [f'<section class="scene" id="archive-scene-{ordinal}"><h2>{html.escape(record["source_heading"])}</h2>', f'<p class="meta">Archive scene {ordinal} / source scene ID {html.escape(str(source_id))}</p>']
        if record.get("location"):
            body.append(f'<p class="location">{html.escape(record["location"])}</p>')
        for unit in record["units"]:
            uid, kind, source = unit["id"], unit["kind"], unit["source"]
            text, _ = translation_payload(unit)
            content = html.escape(text).replace("\n", "<br>")
            attrs = f'data-unit-id="{html.escape(uid, quote=True)}" data-kind="{html.escape(kind, quote=True)}" data-source-scene="{html.escape(str(source_id), quote=True)}" data-source-page="{html.escape(page_label(source["page_provenance"]), quote=True)}"'
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                lead = f'<span class="speaker">{html.escape(speaker)}</span>' if isinstance(speaker, str) and speaker else ""
                body.append(f'<p class="unit dialogue" {attrs}>{lead}<span>{content}</span></p>')
            elif kind == "stage-direction":
                body.append(f'<p class="unit stage" {attrs}>{content}</p>')
            elif kind == "performance-cue":
                body.append(f'<div class="unit special" {attrs}><strong>Performance cue</strong><p><em>{content}</em></p></div>')
            elif kind == "song":
                body.append(f'<div class="unit special song" {attrs}><strong>Song / lyrical performance</strong><p>{content}</p></div>')
            elif kind == "written-text":
                body.append(f'<div class="unit special" {attrs}><strong>Written text</strong><p>{content}</p></div>')
        body.append('<p class="back"><a href="#contents">Back to contents</a></p></section>')
        sections.append("\n".join(body))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vandikkaran Magan — English Reader Edition</title>
<style>body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:58rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}nav{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0}}.scene{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}}.meta{{font-size:.9rem;opacity:.75}}.location{{font-weight:700}}.dialogue{{display:grid;grid-template-columns:minmax(5rem,9rem) 1fr;gap:.75rem}}.dialogue:not(:has(.speaker)){{display:block}}.speaker{{font-weight:700}}.stage{{font-style:italic}}.special{{margin:1rem 0 1rem 1rem;border-left:2px solid;padding-left:1rem}}@media(max-width:36rem){{.dialogue{{display:block}}.speaker{{display:block}}}}@media print{{nav,.back{{display:none}}.scene{{break-before:page}}}}</style>
</head><body><h1>Vandikkaran Magan — English Reader Edition</h1><p><strong>Tamil title:</strong> வண்டிக்காரன் மகன்</p><p><strong>Status:</strong> complete-verified source-linked English derivative</p><p>This deterministic reader renders all {EXPECTED_UNITS:,} verified English units in source order. Exact Tamil speaker labels remain visible for labelled dialogue; source-unlabelled speech remains unassigned.</p><h2 id="contents">Contents</h2><nav>{nav}</nav>{''.join(sections)}</body></html>\n'''


def main() -> int:
    index = load_json(TRANS_INDEX)
    scene_index = load_json(SCENE_INDEX)
    dialogue_index = load_json(DIALOGUE_INDEX)
    song_index = load_json(SONG_INDEX)
    song_inventory = load_json(SONG_INVENTORY)

    ensure(index.get("status") == "complete-verified", "Translation index is not complete-verified")
    ensure(index.get("verified_scenes") == EXPECTED_SCENES, "Translation scene coverage drifted")
    ensure(index.get("verified_scene_ordinals") == list(range(1, EXPECTED_SCENES + 1)), "Verified scene ordinals are incomplete/out of order")
    ensure(index.get("translation_units") == EXPECTED_UNITS, "Translation unit total drifted")
    ensure(index.get("unit_kind_counts") == EXPECTED_KINDS, "Translation kind totals drifted")
    ensure(index.get("immutable_dialogue_records_linked") == EXPECTED_DIALOGUE_RECORDS, "Translation dialogue-link total drifted")
    ensure(index.get("source_unlabelled_spoken_units") == EXPECTED_UNLABELLED, "Translation source-unlabelled total drifted")
    ensure(index.get("cross_page_units") == EXPECTED_CROSS_PAGE, "Translation cross-page total drifted")
    ensure(index.get("performance_linked_units") == EXPECTED_PERFORMANCE_LINKED_UNITS, "Translation performance-linked-unit total drifted")
    ensure(index.get("performance_occurrence_ids_linked") == EXPECTED_PERFORMANCE_IDS, "Translation performance occurrence set/order drifted")

    ensure(scene_index.get("status") == "complete-verified" and scene_index.get("total_scenes") == EXPECTED_SCENES, "Scene authority is not complete-verified 72/72")
    scene_rows = scene_index.get("scenes")
    ensure(isinstance(scene_rows, list) and len(scene_rows) == EXPECTED_SCENES, "Scene index must contain 72 rows")
    ensure([int(r.get("ordinal")) for r in scene_rows] == list(range(1, EXPECTED_SCENES + 1)), "Scene index is unordered")
    ensure(scene_index.get("source", {}).get("sha256") == SOURCE_SHA256, "Scene index source SHA drifted")

    ensure(dialogue_index.get("status") == "complete-verified-reconciled" and dialogue_index.get("dialogue_record_count") == EXPECTED_DIALOGUE_RECORDS, "Dialogue authority is not complete-verified-reconciled 773")
    ensure(song_index.get("status") == "complete-verified-source-only", "Song/performance authority is not complete-verified-source-only")

    performance_ids = collect_ids(song_inventory, "vandikkaran-magan-perf-")
    ensure(performance_ids == set(EXPECTED_PERFORMANCE_IDS), f"Song inventory performance IDs drifted: {sorted(performance_ids)}")

    dialogue_by_id: dict[str, dict[str, Any]] = {}
    dialogue_paths: list[Path] = [DIALOGUE_INDEX]
    for scene in range(1, EXPECTED_SCENES + 1):
        path = DIALOGUES / f"scene-{scene:03d}.json"
        dialogue_paths.append(path)
        for record in dialogue_records(scene):
            rid = record.get("id")
            ensure(isinstance(rid, str) and rid not in dialogue_by_id, f"Bad/duplicate dialogue ID {rid!r}")
            dialogue_by_id[rid] = record
    ensure(len(dialogue_by_id) == EXPECTED_DIALOGUE_RECORDS, f"Dialogue inventory {len(dialogue_by_id)} != {EXPECTED_DIALOGUE_RECORDS}")

    units_seen: set[str] = set()
    dialogue_links: list[str] = []
    unlabelled: list[str] = []
    cross_page: list[str] = []
    performance_links: list[str] = []
    kinds: Counter[str] = Counter()
    records: list[dict[str, Any]] = []
    translation_paths: list[Path] = [TRANS_INDEX]
    previous_scene_first_page = 0

    for scene, meta in enumerate(scene_rows, 1):
        path = TRANS_RECORDS / f"scene-{scene:03d}.json"
        translation_paths.append(path)
        record = load_json(path)
        ensure(record.get("work_id") == "vandikkaran-magan" and record.get("target_language") == "en", f"Scene {scene} work/language mismatch")
        ensure(record.get("scene_ordinal") == scene and record.get("source_scene_id") == meta.get("scene_id"), f"Scene {scene} metadata mismatch")
        ensure(record.get("scene_status", record.get("pilot_status")) == "verified", f"Scene {scene} is not verified")
        units = record.get("units")
        ensure(isinstance(units, list) and record.get("unit_count") == len(units), f"Scene {scene} unit_count mismatch")
        ensure(units, f"Scene {scene} has no translation units")

        first_page = min(p["pdf_page"] for unit in units for p in unit["source"]["page_provenance"])
        ensure(first_page >= previous_scene_first_page, f"Scene {scene} regresses in source-page order")
        previous_scene_first_page = first_page
        for unit in units:
            uid = unit.get("id")
            match = UNIT_RE.match(uid) if isinstance(uid, str) else None
            ensure(match is not None and int(match.group(1)) == scene, f"Malformed/cross-scene unit ID {uid!r}")
            ensure(uid not in units_seen and unit.get("status") == "verified" and unit.get("target_language") == "en", f"Duplicate/unverified unit {uid}")
            units_seen.add(uid)

            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported kind {kind!r} at {uid}")
            kinds[kind] += 1

            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"No page provenance at {uid}")
            # Some verified lyrical/performance units intentionally carry the full multi-page
            # occurrence span (for example PDF 36–37) even when interleaved with a labelled
            # turn anchored on the later page. Source order is authoritative from the verified
            # unit sequence; provenance is validated for bounds and exact dialogue equality,
            # not forced into a lossy monotonic first-page heuristic.
            for page in provenance:
                pdf = page.get("pdf_page")
                printed = page.get("printed_page")
                ensure(isinstance(pdf, int) and 6 <= pdf <= 87 and printed == pdf - 1, f"Invalid screenplay provenance at {uid}: {page}")
            if len(provenance) > 1:
                cross_page.append(uid)

            record_id = source.get("source_record_id")
            if record_id is not None:
                ensure(record_id in dialogue_by_id, f"Unknown immutable dialogue link {record_id} at {uid}")
                immutable = dialogue_by_id[record_id]
                ensure(immutable.get("scene_ordinal") == scene, f"Dialogue scene mismatch at {uid}")
                ensure(immutable.get("speaker_label") == source.get("speaker_label"), f"Speaker-label mismatch at {uid}")
                ensure(immutable.get("page_provenance") == provenance, f"Dialogue provenance mismatch at {uid}")
                dialogue_links.append(record_id)
            elif kind == "dialogue":
                ensure(source.get("speaker_label") in {None, ""} and source.get("speaker_label_origin") == "source-unlabelled", f"Unlabelled speech gained a speaker at {uid}")
                unlabelled.append(uid)

            occurrence = source.get("source_occurrence_id")
            if occurrence is not None:
                ensure(occurrence in performance_ids, f"Unknown song/performance occurrence {occurrence} at {uid}")
                performance_links.append(occurrence)

            text, _ = translation_payload(unit)
            ensure(not PLACEHOLDER_RE.search(text), f"Editorial placeholder at {uid}")
            ensure(not SYNTHETIC_END_RE.match(text), f"Synthetic scene-end prose at {uid}")

        records.append({
            "scene_ordinal": scene,
            "source_scene_id": meta["scene_id"],
            "source_heading": meta["source_heading"],
            "location": meta.get("location"),
            "source_pdf_pages": meta.get("pdf_pages", []),
            "translation_record_path": f"works/vandikkaran-magan/translations/records/scene-{scene:03d}.json",
            "unit_count": len(units),
            "units": units,
        })

    actual_kinds = {kind: kinds.get(kind, 0) for kind in EXPECTED_KINDS}
    ensure(len(units_seen) == EXPECTED_UNITS and actual_kinds == EXPECTED_KINDS, f"Translation totals differ: units={len(units_seen)}, kinds={actual_kinds}")
    ensure(len(dialogue_links) == len(set(dialogue_links)) == EXPECTED_DIALOGUE_RECORDS and set(dialogue_links) == set(dialogue_by_id), "Immutable dialogue links are not exact 1:1 coverage")
    ensure(len(unlabelled) == EXPECTED_UNLABELLED, f"Source-unlabelled speech {len(unlabelled)} != {EXPECTED_UNLABELLED}")
    ensure(len(cross_page) == EXPECTED_CROSS_PAGE, f"Cross-page units {len(cross_page)} != {EXPECTED_CROSS_PAGE}")
    ensure(len(performance_links) == EXPECTED_PERFORMANCE_LINKED_UNITS, f"Performance-linked units {len(performance_links)} != {EXPECTED_PERFORMANCE_LINKED_UNITS}")
    ensure(sorted(set(performance_links)) == EXPECTED_PERFORMANCE_IDS, "Performance occurrence coverage is not exact 9/9")

    input_paths = authoritative_input_paths()
    input_hash = aggregate_sha256(input_paths)
    reader_md = render_markdown(records)
    reader_html = render_html(records)
    reader_model = {
        "work_id": "vandikkaran-magan",
        "title": "Vandikkaran Magan — English Reader Edition",
        "title_ta": "வண்டிக்காரன் மகன்",
        "target_language": "en",
        "status": "complete-verified",
        "authority": "works/vandikkaran-magan/translations/records",
        "source_sha256": SOURCE_SHA256,
        "source_numbered_scenes": True,
        "archive_scene_count": EXPECTED_SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "immutable_dialogue_records_linked": EXPECTED_DIALOGUE_RECORDS,
        "source_unlabelled_spoken_units": EXPECTED_UNLABELLED,
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "performance_linked_units": EXPECTED_PERFORMANCE_LINKED_UNITS,
        "performance_occurrence_ids_linked": EXPECTED_PERFORMANCE_IDS,
        "scenes": records,
    }
    reader_json = json.dumps(reader_model, ensure_ascii=False, indent=2) + "\n"

    for uid in units_seen:
        ensure(reader_md.count(f"unit:{uid};") == 1, f"Markdown coverage mismatch for {uid}")
        ensure(reader_html.count(f'data-unit-id="{uid}"') == 1, f"HTML coverage mismatch for {uid}")
    roundtrip = json.loads(reader_json)
    roundtrip_ids = [u["id"] for s in roundtrip["scenes"] for u in s["units"]]
    ensure(len(roundtrip_ids) == len(set(roundtrip_ids)) == EXPECTED_UNITS and set(roundtrip_ids) == units_seen, "Reader JSON unit round-trip coverage failed")

    preflight = f"""# Vandikkaran Magan English reader/export — preflight QA\n\nStatus: **PASS**\n\n- source-numbered scene derivatives: **{EXPECTED_SCENES}/{EXPECTED_SCENES}**;\n- verified English translation units: **{EXPECTED_UNITS:,}/{EXPECTED_UNITS:,}**;\n- immutable dialogue records available and linked 1:1: **{EXPECTED_DIALOGUE_RECORDS}/{EXPECTED_DIALOGUE_RECORDS}**;\n- source-unlabelled spoken units: **{EXPECTED_UNLABELLED}/{EXPECTED_UNLABELLED}**, with **0 inferred speakers**;\n- cross-page English units: **{EXPECTED_CROSS_PAGE}/{EXPECTED_CROSS_PAGE}**;\n- verified performance occurrence identities: **9/9**, across **{EXPECTED_PERFORMANCE_LINKED_UNITS}** linked English units;\n- screenplay provenance bounds: **PDF 6–87 / printed 5–86**, `printed = PDF - 1`;\n- authoritative input files hashed: **{len(input_paths)}**;\n- authoritative-input aggregate SHA-256: `{input_hash}`.\n\nReader generation is authorized only as a downstream derivative. It does not rewrite canonical Tamil, scene, dialogue, character, song/performance or translation authorities.\n"""

    qa = f"""# Vandikkaran Magan English Reader Edition — Whole-work QA\n\n**Status:** PASS  \n**English authority:** `works/vandikkaran-magan/translations/records/`  \n**Source scan SHA-256:** `{SOURCE_SHA256}`\n\n## Verified checks\n\n- source-numbered archive scenes: **{EXPECTED_SCENES}/{EXPECTED_SCENES}** in verified source order;\n- English units: **{EXPECTED_UNITS:,}/{EXPECTED_UNITS:,} unique and verified**;\n- kind counts: **800 dialogue / 316 stage-direction / 10 performance-cue / 53 song / 2 written-text**;\n- immutable labelled dialogue records linked exactly once: **{len(dialogue_links)}/{EXPECTED_DIALOGUE_RECORDS}**;\n- source-unlabelled spoken units retained without invented speakers/dialogue IDs: **{len(unlabelled)}**;\n- cross-page English units: **{len(cross_page)}**;\n- verified song/performance occurrence identities represented: **{len(set(performance_links))}/9**, across **{len(performance_links)}** linked units;\n- all provenance lies inside PDF **6–87** / printed **5–86**, with `printed = PDF - 1`;\n- structural `★` separators rendered as synthetic prose: **0**;\n- editorial placeholder leakage: **0**;\n- reader Markdown and HTML contain every verified English unit exactly once;\n- machine-readable JSON round-trips to all **{EXPECTED_UNITS:,}** validated unit IDs exactly once.\n\nThe generator writes only inside `works/vandikkaran-magan/editions/en/` and does not modify closed Tamil, scene, immutable dialogue, character/entity, song/performance or translation records.\n"""

    OUT.mkdir(parents=True, exist_ok=True)
    payloads = {
        OUT / "reader-edition.md": reader_md.encode("utf-8"),
        OUT / "reader-edition.html": reader_html.encode("utf-8"),
        OUT / "reader-edition.json": reader_json.encode("utf-8"),
        OUT / "PREFLIGHT_QA_REPORT.md": preflight.encode("utf-8"),
        OUT / "QA_REPORT.md": qa.encode("utf-8"),
    }
    for path, payload in payloads.items():
        path.write_bytes(payload)

    manifest = {
        "work_id": "vandikkaran-magan",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "generator": "works/vandikkaran-magan/editions/en/build.py",
        "source_scan_sha256": SOURCE_SHA256,
        "translation_authority": "works/vandikkaran-magan/translations/records",
        "authoritative_input_files": len(input_paths),
        "authoritative_input_aggregate_sha256": input_hash,
        "archive_scenes": EXPECTED_SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "immutable_dialogue_records_linked": len(dialogue_links),
        "source_unlabelled_spoken_units": len(unlabelled),
        "cross_page_units": len(cross_page),
        "performance_linked_units": len(performance_links),
        "performance_occurrence_ids_linked": sorted(set(performance_links)),
        "qa_status": "PASS",
        "outputs": {path.name: {"sha256": sha256(payload), "bytes": len(payload)} for path, payload in payloads.items()},
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = f"""# வண்டிக்காரன் மகன் — deterministic English reader/export\n\nThis directory is the publication-facing downstream reader/export layer for the complete-verified `வண்டிக்காரன் மகன்` English textual archive.\n\n## Authority\n\nThe reader is generated only from verified structured repository data: 72 scene translation records, the reconciled 773-record immutable dialogue corpus, verified scene metadata, and the 9-record source-visible song/performance inventory. The scanned publication and verified canonical Tamil remain upstream authorities.\n\n## Completion checkpoint\n\nStatus: **complete-verified — QA PASS**.\n\n- source-numbered archive scenes: **72/72**;\n- English translation units: **1,181**;\n- immutable dialogue links: **773/773**;\n- source-unlabelled spoken units: **27**, with **0 inferred speakers**;\n- cross-page units: **58**;\n- performance occurrence identities: **9/9** across **66** linked English units;\n- generated Markdown SHA-256: `{manifest['outputs']['reader-edition.md']['sha256']}`;\n- generated HTML SHA-256: `{manifest['outputs']['reader-edition.html']['sha256']}`;\n- generated JSON SHA-256: `{manifest['outputs']['reader-edition.json']['sha256']}`;\n- generated-output QA: `QA_REPORT.md` — **PASS**.\n\n## Outputs\n\n- `build.py` — deterministic reader/export builder and executable whole-work QA;\n- `PREFLIGHT_QA_REPORT.md` — authoritative-input checkpoint;\n- `reader-edition.md` — English Markdown reader;\n- `reader-edition.html` — standalone English HTML reader;\n- `reader-edition.json` — machine-readable reader payload;\n- `QA_REPORT.md` — generated-output QA;\n- `manifest.json` — reproducibility/integrity hashes.\n\nNo PDF or EPUB is created by default. The preferred downstream public destination remains the Kalaignar Digital Library / Reading Room.\n"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")

    print("Vandikkaran Magan English reader/export QA: PASS")
    print(f"Scenes: {EXPECTED_SCENES} | Units: {EXPECTED_UNITS} | Dialogue links: {len(dialogue_links)} | Cross-page: {len(cross_page)} | Performance IDs: {len(set(performance_links))}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"Vandikkaran Magan English reader/export QA: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
