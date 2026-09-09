#!/usr/bin/env python3
"""Build and QA the deterministic source-linked English reader for நாம்."""

from __future__ import annotations

import copy
import hashlib
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "naam"
TRANSLATIONS = WORK / "translations"
TRANS_RECORDS = TRANSLATIONS / "records"
SCENES_DIR = WORK / "scenes"
DIALOGUES_DIR = WORK / "dialogues" / "records"
SONG_INVENTORY = WORK / "songs" / "inventory.json"
OUT = WORK / "editions" / "en"

SOURCE_SHA256 = "0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad"
SCENES = list(range(1, 46))
EXPECTED_UNITS = 797
EXPECTED_KINDS = {
    "dialogue": 610,
    "narrative": 35,
    "performance-cue": 6,
    "song": 6,
    "stage-direction": 137,
    "written-text": 2,
    "chant": 1,
}
EXPECTED_DIALOGUE_LINKS = 590
EXPECTED_UNLABELLED = 20
EXPECTED_CROSS_PAGE = [
    "naam-en-s001-u021",
    "naam-en-s008-u009",
    "naam-en-s017-u011",
    "naam-en-s020-u003",
    "naam-en-s021-u002",
    "naam-en-s030-u016",
    "naam-en-s031-u002",
    "naam-en-s036-u007",
    "naam-en-s039-u017",
    "naam-en-s041-u002",
    "naam-en-s045-u013",
    "naam-en-s045-u022",
]
EXPECTED_WRITTEN = ["naam-en-s041-u012", "naam-en-s045-u025"]
EXPECTED_PERFORMANCES = [
    "naam-perf-007",
    "naam-perf-001",
    "naam-perf-002",
    "naam-perf-003",
    "naam-perf-004",
    "naam-perf-005",
    "naam-perf-006",
]
EXPECTED_PERFORMANCE_MAPS = {
    "naam-perf-007": 23,
    "naam-perf-001": 12,
    "naam-perf-002": 22,
    "naam-perf-003": 17,
    "naam-perf-004": 10,
    "naam-perf-005": 39,
    "naam-perf-006": 15,
}
EXPECTED_CHANT_UNIT = "naam-en-s034-u002"
EXPECTED_CHANT_MAPS = 16
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|TRANSLATE(?:\s+ME)?)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
SYNTHETIC_END_RE = re.compile(r"^\s*[\[(]?\s*(?:the\s+)?(?:end\s+of\s+)?scene\s+ends?\.?\s*[\])]?\s*$", re.I)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    h = hashlib.sha256()
    for path in sorted(set(paths), key=lambda p: p.as_posix()):
        ensure(path.exists(), f"Missing input {path.relative_to(ROOT)}")
        h.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        h.update(b"\0")
        h.update(path.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def extract_source_heading(path: Path) -> str:
    raw = COMMENT_RE.sub("", path.read_text(encoding="utf-8"))
    for line in raw.splitlines():
        m = HEADING_RE.match(line.strip())
        if m:
            return m.group(1).strip()
    raise QAError(f"No scene heading in {path.relative_to(ROOT)}")


def provenance_pages(unit: dict[str, Any]) -> list[int]:
    source = unit.get("source")
    ensure(isinstance(source, dict), f"Malformed source metadata at {unit.get('id')}")
    prov = source.get("page_provenance")
    ensure(isinstance(prov, list) and prov, f"Missing page provenance at {unit.get('id')}")
    pages: list[int] = []
    for item in prov:
        ensure(isinstance(item, dict), f"Malformed provenance at {unit.get('id')}")
        p = item.get("pdf_page")
        ensure(isinstance(p, int) and 5 <= p <= 71, f"Out-of-range PDF provenance at {unit.get('id')}")
        printed = item.get("printed_page")
        ensure((p == 5 and printed is None) or (p >= 6 and printed == p), f"Printed-page provenance differs at {unit.get('id')}: {item}")
        pages.append(p)
    ensure(pages == sorted(dict.fromkeys(pages)), f"Unordered/repeated provenance at {unit.get('id')}")
    return pages


def page_label(prov: list[dict[str, Any]]) -> str:
    def one(x: dict[str, Any]) -> str:
        printed = x.get("printed_page")
        return f"PDF {x['pdf_page']}" if printed is None else f"PDF {x['pdf_page']} / printed {printed}"
    return one(prov[0]) if len(prov) == 1 else f"{one(prov[0])} → {one(prov[-1])}"


def translation_payload(unit: dict[str, Any]) -> tuple[str, list[str] | None]:
    tr = unit.get("translation")
    ensure(isinstance(tr, dict), f"Malformed translation at {unit.get('id')}")
    text = tr.get("english_text")
    lines = tr.get("english_lines")
    ensure(isinstance(text, str) ^ isinstance(lines, list), f"{unit.get('id')} must have exactly one English payload shape")
    if isinstance(text, str):
        ensure(text.strip(), f"Empty English text at {unit.get('id')}")
        ensure(not PLACEHOLDER_RE.search(text), f"Placeholder in {unit.get('id')}")
        ensure(not SYNTHETIC_END_RE.match(text.strip()), f"Synthetic scene-end prose at {unit.get('id')}")
        return text, None
    ensure(bool(lines) and all(isinstance(x, str) and x.strip() for x in lines), f"Malformed English lines at {unit.get('id')}")
    for line in lines:
        ensure(not PLACEHOLDER_RE.search(line), f"Placeholder in {unit.get('id')}")
        ensure(not SYNTHETIC_END_RE.match(line.strip()), f"Synthetic scene-end prose at {unit.get('id')}")
    return "\n".join(lines), lines


def speaker_display(source: dict[str, Any]) -> str | None:
    label = source.get("speaker_label")
    if not isinstance(label, str) or not label:
        return None
    delim = source.get("source_delimiter") or ""
    if delim == "—":
        return f"{label} —"
    return f"{label} {delim}".rstrip()


def render_markdown(records: list[dict[str, Any]]) -> str:
    out = [
        "# நாம் — English Reader Edition",
        "",
        "**Source title:** நாம்  ",
        "**Source scene numbering:** printed `காட்சி 1–45`  ",
        "**Status:** complete-verified deterministic reader derivative  ",
        "**English authority:** `works/naam/translations/records/`  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`",
        "",
        "> This reader is generated from the verified source-linked English records. Tamil source speaker labels and source delimiters are retained as provenance; source-unlabelled speech remains visibly unlabelled. Performance, chant, written-text, narrative and stage-direction units remain structurally distinct. Cross-page units stay single logical units. No source `★` separator is converted into synthetic scene-end prose.",
        "",
        "## Contents",
        "",
        *[f"- [Scene {n}](#scene-{n})" for n in SCENES],
        "",
        "---",
        "",
    ]
    labels = {
        "narrative": "Narrative",
        "performance-cue": "Performance cue",
        "song": "Song / performance",
        "written-text": "Written text",
        "chant": "Chant",
    }
    for record in records:
        n = record["source_scene_number"]
        out.extend([f"## Scene {n}", "", f"**Source heading:** `{record['source_heading_ta']}`  ", f"**Source pages:** {record['page_label']}", ""])
        for unit in record["units"]:
            uid = unit["id"]
            source = unit["source"]
            text, lines = translation_payload(unit)
            out.append(f"<!-- unit:{uid} | kind:{unit['kind']} | source:{page_label(source['page_provenance'])} | record:{source.get('source_record_id') or ''} | occurrence:{source.get('source_occurrence_id') or ''} -->")
            kind = unit["kind"]
            if kind == "dialogue":
                speaker = speaker_display(source)
                if speaker:
                    out.extend([f"**{speaker}**  ", text, ""])
                else:
                    out.extend([text, ""])
            elif kind == "stage-direction":
                out.extend([f"*{text}*", ""])
            elif kind == "narrative":
                out.extend([f"*{labels[kind]}*  ", text, ""])
            elif kind == "performance-cue":
                out.extend([f"*{labels[kind]}*  ", f"*{text}*", ""])
            elif kind in {"song", "chant"}:
                out.append(f"**{labels[kind]}**  ")
                if lines:
                    out.extend([*(f"> {line}  " for line in lines), ""])
                else:
                    out.extend([f"> {text}", ""])
            elif kind == "written-text":
                out.extend([f"**{labels[kind]}**  ", f"> {text}", ""])
            else:
                raise QAError(f"Unsupported kind {kind} at {uid}")
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(records: list[dict[str, Any]]) -> str:
    nav = " ".join(f'<a href="#scene-{n}">{n}</a>' for n in SCENES)
    labels = {
        "narrative": "Narrative",
        "performance-cue": "Performance cue",
        "song": "Song / performance",
        "written-text": "Written text",
        "chant": "Chant",
    }
    sections: list[str] = []
    for record in records:
        n = record["source_scene_number"]
        body = [
            f'<section class="scene" id="scene-{n}">',
            f'<h2>Scene {n}</h2>',
            f'<p class="source-meta"><strong>Source heading:</strong> <span lang="ta">{html.escape(record["source_heading_ta"])}</span><br><strong>Source pages:</strong> {html.escape(record["page_label"])}</p>',
        ]
        for unit in record["units"]:
            uid = unit["id"]
            source = unit["source"]
            text, lines = translation_payload(unit)
            attrs = (
                f'data-unit-id="{html.escape(uid, quote=True)}" '
                f'data-kind="{html.escape(unit["kind"], quote=True)}" '
                f'data-source-record-id="{html.escape(source.get("source_record_id") or "", quote=True)}" '
                f'data-source-occurrence-id="{html.escape(source.get("source_occurrence_id") or "", quote=True)}" '
                f'data-source-pages="{html.escape(page_label(source["page_provenance"]), quote=True)}"'
            )
            kind = unit["kind"]
            safe_text = html.escape(text).replace("\n", "<br>")
            if kind == "dialogue":
                speaker = speaker_display(source)
                sh = f'<span class="speaker" lang="ta">{html.escape(speaker)}</span>' if speaker else ""
                body.append(f'<p class="unit dialogue" {attrs}>{sh}<span class="text">{safe_text}</span></p>')
            elif kind == "stage-direction":
                body.append(f'<p class="unit stage" {attrs}>{safe_text}</p>')
            elif kind in {"narrative", "performance-cue", "written-text"}:
                body.append(f'<div class="unit special {kind}" {attrs}><strong>{html.escape(labels[kind])}</strong><p>{safe_text}</p></div>')
            elif kind in {"song", "chant"}:
                lyric = "<br>".join(html.escape(x) for x in (lines or [text]))
                body.append(f'<div class="unit special {kind}" {attrs}><strong>{html.escape(labels[kind])}</strong><blockquote>{lyric}</blockquote></div>')
            else:
                raise QAError(f"Unsupported kind {kind} at {uid}")
        body.append('<p class="back"><a href="#contents">Back to contents</a></p></section>')
        sections.append("\n".join(body))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Naam — English Reader Edition</title>
<style>body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:60rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}nav{{display:flex;flex-wrap:wrap;gap:.55rem;margin:1.5rem 0}}.scene{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}}.source-meta{{font-size:.92rem;opacity:.8}}.dialogue{{display:grid;grid-template-columns:minmax(8rem,14rem) 1fr;gap:.75rem}}.dialogue:not(:has(.speaker)){{display:block}}.speaker{{font-weight:700}}.stage{{font-style:italic}}.special{{margin:1rem 0 1rem 1rem;border-left:2px solid;padding-left:1rem}}blockquote{{margin:.5rem 0}}@media(max-width:42rem){{.dialogue{{display:block}}.speaker{{display:block;margin-bottom:.2rem}}}}@media print{{nav,.back{{display:none}}.scene{{break-before:page}}}}</style>
</head><body><h1>Naam — English Reader Edition</h1><p><strong>Tamil title:</strong> <span lang="ta">நாம்</span></p><p><strong>Status:</strong> complete-verified deterministic reader derivative</p><p><strong>Source scene numbering:</strong> printed scenes 1–45.</p><p>This edition renders all {EXPECTED_UNITS} verified English units exactly once while retaining source-linked speaker, delimiter, performance and page provenance.</p><h2 id="contents">Contents</h2><nav>{nav}</nav>{''.join(sections)}</body></html>\n'''


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    tindex = load_json(TRANSLATIONS / "index.json")
    reconc = load_json(TRANSLATIONS / "whole-work-reconciliation.json")
    scene_index = load_json(SCENES_DIR / "index.json")
    songs = load_json(SONG_INVENTORY)

    ensure(tindex.get("status") == "complete-verified", "English translation is not complete-verified")
    ensure(tindex.get("whole_work_reconciliation_status") == "PASS", "English whole-work reconciliation is not PASS")
    ensure(tindex.get("translation_units_verified") == EXPECTED_UNITS, "English unit total drifted")
    ensure(tindex.get("immutable_dialogue_links_verified") == EXPECTED_DIALOGUE_LINKS, "Dialogue-link total drifted")
    ensure(reconc.get("status") == "PASS" and reconc.get("reader_export_gate") == "READY-NEXT", "Reader entry gate is not open")
    ensure(reconc.get("kind_counts") == EXPECTED_KINDS, "Whole-work kind counts drifted")
    ensure(scene_index.get("status") == "complete-verified" and scene_index.get("source_scene_count") == 45, "Scene index is not closed")
    scene_meta = scene_index.get("scene_records")
    ensure(isinstance(scene_meta, list) and [x.get("source_scene_number") for x in scene_meta] == SCENES, "Source scene order drifted")
    ensure(songs.get("coverage") == "7/7", "Performance inventory drifted")
    perf_records = songs.get("records")
    ensure(isinstance(perf_records, list), "Malformed performance inventory")
    perf_ids = [x.get("id") for x in perf_records]
    ensure(perf_ids == EXPECTED_PERFORMANCES, f"Performance order drifted: {perf_ids}")
    perf_by_id = {x["id"]: x for x in perf_records}
    ensure(next(x for x in perf_records if x["id"] == "naam-perf-001").get("author_as_printed") == "பாரதியார்", "Bharathiyar source attribution drifted")
    for x in perf_records:
        if x["id"] != "naam-perf-001":
            ensure(x.get("authorship_status") == "unresolved-item-level" and x.get("author_as_printed") is None, f"Unsupported authorship state at {x['id']}")

    input_paths = [TRANSLATIONS / "index.json", TRANSLATIONS / "whole-work-reconciliation.json", SCENES_DIR / "index.json", SONG_INVENTORY]
    records: list[dict[str, Any]] = []
    unit_ids: list[str] = []
    kinds: Counter[str] = Counter()
    linked: list[str] = []
    source_linked: list[str] = []
    unlabelled: list[str] = []
    cross_page: list[str] = []
    written: list[str] = []
    perf_first_order: list[str] = []
    perf_map_counts: Counter[str] = Counter()
    chant_units: list[str] = []
    chant_maps = 0
    page_failures: list[str] = []
    source_order_failures: list[str] = []

    for n, sm in zip(SCENES, scene_meta):
        tr_path = TRANS_RECORDS / f"scene-{n:03d}.json"
        dg_path = DIALOGUES_DIR / f"scene-{n:03d}.json"
        scene_path = SCENES_DIR / f"scene-{n:03d}.md"
        input_paths.extend([tr_path, dg_path, scene_path])
        tr = load_json(tr_path)
        dg = load_json(dg_path)
        ensure(isinstance(dg, list), f"Dialogue shard {n} is malformed")
        ensure(tr.get("scene_status") == "verified" and tr.get("source_scene_number") == n and tr.get("scene_id") == f"naam-s{n:03d}", f"Translation scene identity drifted at {n}")
        units = tr.get("units")
        ensure(isinstance(units, list) and tr.get("unit_count") == len(units), f"Translation scene unit count drifted at {n}")
        ensure([u.get("id") for u in units] == [f"naam-en-s{n:03d}-u{i:03d}" for i in range(1, len(units)+1)], f"Unit sequence drifted at scene {n}")
        source_heading = extract_source_heading(scene_path)
        ensure(source_heading == sm.get("heading"), f"Source heading differs between scene index and scene file at {n}")
        scene_pages = set(sm.get("pdf_pages") or [])
        ensure(scene_pages, f"Scene {n} has no page map")
        prev_page = -1
        linked_in_scene: list[str] = []
        dg_by_id = {x["id"]: x for x in dg}
        for u in units:
            uid = u.get("id")
            ensure(isinstance(uid, str) and uid not in unit_ids, f"Bad/duplicate unit id {uid!r}")
            unit_ids.append(uid)
            ensure(u.get("status") == "verified" and u.get("target_language") == "en", f"Unverified unit {uid}")
            kind = u.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported unit kind {kind!r} at {uid}")
            kinds[kind] += 1
            pp = provenance_pages(u)
            if pp[0] < prev_page:
                source_order_failures.append(uid)
            prev_page = pp[0]
            if not set(pp).issubset(scene_pages):
                page_failures.append(uid)
            if len(pp) > 1:
                cross_page.append(uid)
            translation_payload(u)

            source = u["source"]
            rid = source.get("source_record_id")
            if rid:
                ensure(kind == "dialogue" and rid in dg_by_id, f"Unknown dialogue link at {uid}")
                d = dg_by_id[rid]
                ensure(source.get("speaker_label") == d.get("speaker_label"), f"Speaker label drifted at {uid}")
                ensure(source.get("source_delimiter") == d.get("source_delimiter"), f"Source delimiter drifted at {uid}")
                ensure(source.get("page_provenance") == d.get("page_provenance"), f"Dialogue provenance drifted at {uid}")
                linked.append(rid)
                linked_in_scene.append(rid)
            elif kind == "dialogue":
                ensure(source.get("speaker_label") is None and source.get("source_delimiter") is None and source.get("speaker_label_origin") is None, f"Unlabelled dialogue acquired speaker metadata at {uid}")
                unlabelled.append(uid)
            if kind in {"narrative", "performance-cue", "song", "stage-direction", "written-text", "chant"}:
                ensure(source.get("speaker_label") is None and source.get("source_delimiter") is None, f"Non-dialogue speaker metadata at {uid}")
            if kind == "written-text":
                written.append(uid)

            occ = source.get("source_occurrence_id")
            if occ:
                ensure(occ in perf_by_id, f"Unknown performance occurrence {occ} at {uid}")
                ensure(set(pp).issubset(set(perf_by_id[occ].get("source_pdf_pages") or [])), f"Performance provenance outside inventory at {uid}")
                if occ not in perf_first_order:
                    perf_first_order.append(occ)
                lm = u.get("translation", {}).get("line_map") or []
                ensure(isinstance(lm, list), f"Malformed line map at {uid}")
                perf_map_counts[occ] += len(lm)
            if kind == "chant":
                chant_units.append(uid)
                ensure(occ is None, "Scene-local chant was promoted into performance inventory")
                chant_maps += len(u.get("translation", {}).get("line_map") or [])
        ensure(linked_in_scene == [x["id"] for x in dg], f"Dialogue source order/coverage differs at scene {n}")
        source_linked.extend(x["id"] for x in dg)
        records.append({
            "scene_id": f"naam-s{n:03d}",
            "source_scene_number": n,
            "source_heading_ta": source_heading,
            "source_scene_file": f"works/naam/scenes/scene-{n:03d}.md",
            "pdf_pages": sm["pdf_pages"],
            "start_pdf": sm["start_pdf"],
            "start_printed": sm.get("start_printed"),
            "end_pdf": sm["end_pdf"],
            "end_printed": sm.get("end_printed"),
            "page_label": f"PDF {sm['start_pdf']}–{sm['end_pdf']}",
            "unit_count": len(units),
            "units": copy.deepcopy(units),
        })

    ensure(len(unit_ids) == len(set(unit_ids)) == EXPECTED_UNITS, "Reader unit identity coverage is not exact")
    ensure({k: kinds.get(k, 0) for k in EXPECTED_KINDS} == EXPECTED_KINDS and not (set(kinds) - set(EXPECTED_KINDS)), f"Reader kind counts drifted: {dict(kinds)}")
    ensure(source_order_failures == [], f"Units out of source order: {source_order_failures}")
    ensure(page_failures == [], f"Units outside mapped scene pages: {page_failures}")
    ensure(len(linked) == len(set(linked)) == EXPECTED_DIALOGUE_LINKS and linked == source_linked, "Immutable dialogue coverage is not exactly once/in source order")
    ensure(len(unlabelled) == EXPECTED_UNLABELLED, f"Unlabelled speech total drifted: {len(unlabelled)}")
    ensure(cross_page == EXPECTED_CROSS_PAGE, f"Cross-page unit list drifted: {cross_page}")
    ensure(written == EXPECTED_WRITTEN, f"Written-text list drifted: {written}")
    ensure(perf_first_order == EXPECTED_PERFORMANCES, f"Performance occurrence order drifted: {perf_first_order}")
    ensure(dict(perf_map_counts) == EXPECTED_PERFORMANCE_MAPS, f"Performance line/cue mapping counts drifted: {dict(perf_map_counts)}")
    ensure(chant_units == [EXPECTED_CHANT_UNIT] and chant_maps == EXPECTED_CHANT_MAPS, "Scene-34 chant state drifted")

    reader = {
        "schema_version": 1,
        "work_id": "naam",
        "title_ta": "நாம்",
        "title_en": "Naam",
        "work_type": "film-screenplay-dialogue-booklet",
        "status": "complete-verified",
        "source_scan_sha256": SOURCE_SHA256,
        "source_scene_numbering": "printed-1-45",
        "scene_navigation_is_source_numbering": True,
        "scene_count": 45,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "immutable_dialogue_links": EXPECTED_DIALOGUE_LINKS,
        "source_unlabelled_speech_units": EXPECTED_UNLABELLED,
        "retained_performance_records": EXPECTED_PERFORMANCES,
        "performance_line_cue_mappings": sum(EXPECTED_PERFORMANCE_MAPS.values()),
        "source_local_chant_unit": EXPECTED_CHANT_UNIT,
        "source_local_chant_line_cue_mappings": EXPECTED_CHANT_MAPS,
        "written_text_units": EXPECTED_WRITTEN,
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "authorship": {
            "source_attributed": {"naam-perf-001": "பாரதியார்"},
            "unresolved_item_level": [x for x in EXPECTED_PERFORMANCES if x != "naam-perf-001"],
        },
        "scenes": records,
    }

    md = render_markdown(records)
    html_text = render_html(records)
    json_text = json.dumps(reader, ensure_ascii=False, indent=2) + "\n"
    md_path = OUT / "reader-edition.md"
    html_path = OUT / "reader-edition.html"
    json_path = OUT / "reader-edition.json"
    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html_text, encoding="utf-8")
    json_path.write_text(json_text, encoding="utf-8")

    # Generated-output QA: every verified unit appears exactly once in all three reader forms.
    ensure(md.count("<!-- unit:") == EXPECTED_UNITS, "Markdown unit marker total differs")
    ensure(html_text.count('data-unit-id="') == EXPECTED_UNITS, "HTML unit marker total differs")
    for uid in unit_ids:
        ensure(md.count(f"<!-- unit:{uid} ") == 1, f"Markdown does not own {uid} exactly once")
        ensure(html_text.count(f'data-unit-id="{uid}"') == 1, f"HTML does not own {uid} exactly once")
    parsed_reader = json.loads(json_text)
    json_ids = [u["id"] for s in parsed_reader["scenes"] for u in s["units"]]
    ensure(json_ids == unit_ids and len(set(json_ids)) == EXPECTED_UNITS, "Reader JSON unit order/coverage differs")

    qa = {
        "work_id": "naam",
        "phase": "whole-work-reader-export",
        "status": "PASS",
        "source_scenes_expected": 45,
        "source_scenes_rendered": 45,
        "source_scene_numbers": SCENES,
        "translation_units_expected": EXPECTED_UNITS,
        "translation_units_rendered_markdown": EXPECTED_UNITS,
        "translation_units_rendered_html": EXPECTED_UNITS,
        "translation_units_rendered_json": EXPECTED_UNITS,
        "unit_ids_unique_and_sequential": True,
        "unit_kind_counts": dict(kinds),
        "immutable_dialogue_links_expected": EXPECTED_DIALOGUE_LINKS,
        "immutable_dialogue_links_rendered": EXPECTED_DIALOGUE_LINKS,
        "immutable_dialogue_links_unique_and_source_ordered": True,
        "source_unlabelled_speech_units": EXPECTED_UNLABELLED,
        "source_unlabelled_speaker_assignments": 0,
        "retained_performance_records": EXPECTED_PERFORMANCES,
        "performance_mapping_counts": EXPECTED_PERFORMANCE_MAPS,
        "performance_line_cue_mappings": sum(EXPECTED_PERFORMANCE_MAPS.values()),
        "source_local_chant_unit": EXPECTED_CHANT_UNIT,
        "source_local_chant_line_cue_mappings": EXPECTED_CHANT_MAPS,
        "source_local_chant_promoted_to_performance_inventory": False,
        "written_text_units": EXPECTED_WRITTEN,
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "cross_page_unit_count": len(EXPECTED_CROSS_PAGE),
        "provenance_out_of_scene_bounds": page_failures,
        "source_order_failures": source_order_failures,
        "placeholder_hits": [],
        "synthetic_scene_end_hits": [],
        "unsupported_authorship_upgrades": 0,
        "canonical_tamil_modified": False,
        "scene_text_modified": False,
        "dialogue_records_modified": False,
        "character_entity_mappings_modified": False,
        "song_source_records_modified": False,
        "reader_outputs": ["reader-edition.md", "reader-edition.html", "reader-edition.json"],
        "reading_room_gate": "READY-NEXT",
    }
    qa_path = OUT / "QA_REPORT.md"
    qa_path.write_text(
        "# நாம் — English reader/export QA\n\n"
        "**Status:** **PASS / COMPLETE-VERIFIED**\n\n"
        f"- source scenes: **45/45**, printed scene numbers 1–45 preserved;\n"
        f"- verified English units rendered: **{EXPECTED_UNITS}/{EXPECTED_UNITS} exactly once** in Markdown, HTML and JSON;\n"
        f"- immutable dialogue links: **{EXPECTED_DIALOGUE_LINKS}/{EXPECTED_DIALOGUE_LINKS} exactly once / source ordered**;\n"
        f"- source-unlabelled speech: **{EXPECTED_UNLABELLED} / inferred speakers 0**;\n"
        f"- retained performances: **7/7 / {sum(EXPECTED_PERFORMANCE_MAPS.values())} line-cue mappings**;\n"
        f"- scene-34 chant: **1 / {EXPECTED_CHANT_MAPS} mappings / not promoted to performance inventory**;\n"
        f"- written-text units: **2**; cross-page units: **{len(EXPECTED_CROSS_PAGE)}**;\n"
        "- provenance outside mapped scene bounds: **0**;\n"
        "- placeholders / synthetic scene-end prose / unsupported authorship upgrades: **0 / 0 / 0**;\n"
        "- frozen Tamil / scene / dialogue / character / song-source edits by reader build: **0 / 0 / 0 / 0 / 0**.\n\n"
        "Reader generation is deterministic from the complete-verified translation and closed source-linked structured layers. `naam-perf-001` retains the source-specific `பாரதியார்` attribution; the other six retained performances remain unresolved at item level.\n\n"
        "**Next gate:** build and QA the source-linked Reading Room payload; public-site application remains separate and not applied by this repository step.\n",
        encoding="utf-8",
    )

    input_sha = aggregate_sha256(input_paths)
    output_paths = [md_path, html_path, json_path, qa_path]
    manifest = {
        "schema_version": 1,
        "work_id": "naam",
        "build_version": BUILD_VERSION,
        "status": "complete-verified",
        "qa_status": "PASS",
        "source_scan_sha256": SOURCE_SHA256,
        "source_scene_numbering": "printed-1-45",
        "scene_count": 45,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "immutable_dialogue_links": EXPECTED_DIALOGUE_LINKS,
        "source_unlabelled_speech_units": EXPECTED_UNLABELLED,
        "retained_performance_records": EXPECTED_PERFORMANCES,
        "performance_line_cue_mappings": sum(EXPECTED_PERFORMANCE_MAPS.values()),
        "source_local_chant_line_cue_mappings": EXPECTED_CHANT_MAPS,
        "cross_page_units": EXPECTED_CROSS_PAGE,
        "authoritative_input_file_count": len(set(input_paths)),
        "authoritative_input_aggregate_sha256": input_sha,
        "closed_source_layer_hashes": reconc.get("upstream_integrity_after"),
        "outputs": {
            p.name: {"sha256": sha256_bytes(p.read_bytes()), "bytes": p.stat().st_size}
            for p in output_paths
        },
        "reader_json_sha256": sha256_bytes(json_path.read_bytes()),
        "reading_room_gate": "READY-NEXT",
    }
    write_json(OUT / "manifest.json", manifest)
    (OUT / "README.md").write_text(
        "# நாம் — English reader/export\n\n"
        "Deterministic downstream reader package generated from the complete-verified English scene records and closed source-linked structured layers.\n\n"
        "## Outputs\n\n"
        "- `reader-edition.md` — human-readable Markdown;\n"
        "- `reader-edition.html` — standalone HTML;\n"
        "- `reader-edition.json` — machine-readable source-linked reader data;\n"
        "- `QA_REPORT.md` — generated-output whole-work QA;\n"
        "- `manifest.json` — authoritative-input and output integrity hashes;\n"
        "- `build.py` — deterministic builder and fail-closed QA gate.\n\n"
        "Status: **COMPLETE-VERIFIED / QA PASS**. Source-numbered scenes remain source numbering, source-unlabelled speech remains unassigned, and no PDF/EPUB is generated here.\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "status": "PASS",
        "scenes": 45,
        "units": EXPECTED_UNITS,
        "dialogue_links": EXPECTED_DIALOGUE_LINKS,
        "performances": 7,
        "performance_mappings": sum(EXPECTED_PERFORMANCE_MAPS.values()),
        "chant_mappings": EXPECTED_CHANT_MAPS,
        "cross_page_units": len(EXPECTED_CROSS_PAGE),
        "reader_json_sha256": manifest["reader_json_sha256"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"QA FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
