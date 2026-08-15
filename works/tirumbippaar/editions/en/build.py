#!/usr/bin/env python3
"""Build and QA the provenance-safe Tirumbippaar English reader edition."""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 2
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "tirumbippaar"
TRANSLATIONS = WORK / "translations"
INDEX_PATH = TRANSLATIONS / "index.json"
DIALOGUES = WORK / "dialogues" / "records"
SONG_INVENTORY_PATH = WORK / "songs" / "inventory.json"
OUT_DIR = WORK / "editions" / "en"

SCENES = list(range(1, 94))
EXPECTED_UNITS = 1329
EXPECTED_KINDS = {
    "dialogue": 1047,
    "stage-direction": 262,
    "song": 0,
    "song-reference": 7,
    "chant": 2,
    "written-text": 11,
}
EXPECTED_DIALOGUE_RECORDS = 1040
EXPECTED_DIRECT_UNLABELLED = 7
EXPECTED_CROSS_PAGE = 12
SOURCE_SHA256 = "973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682"
UNIT_RE = re.compile(r"^tirumbippaar-en-s\d{3}-u\d{3}$")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.I)
SYNTHETIC_END_RE = re.compile(r"^\s*\(Scene ends\.\)\s*$", re.I)


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
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def collect_ids(node: Any) -> set[str]:
    out: set[str] = set()
    if isinstance(node, dict):
        if isinstance(node.get("id"), str):
            out.add(node["id"])
        for value in node.values():
            out |= collect_ids(value)
    elif isinstance(node, list):
        for value in node:
            out |= collect_ids(value)
    return out


def translation_payload(unit: dict[str, Any]) -> tuple[str, list[str] | None]:
    translation = unit.get("translation")
    ensure(isinstance(translation, dict), f"{unit.get('id')} has malformed translation")
    text = translation.get("english_text")
    lines = translation.get("english_lines")
    ensure((isinstance(text, str)) ^ (isinstance(lines, list)), f"{unit.get('id')} must have exactly one English payload")
    if isinstance(text, str):
        ensure(bool(text.strip()), f"{unit.get('id')} has empty English text")
        return text, None
    ensure(bool(lines) and all(isinstance(line, str) and line.strip() for line in lines), f"{unit.get('id')} has malformed English lines")
    return "\n".join(lines), lines


def page_label(provenance: list[dict[str, int]]) -> str:
    if len(provenance) == 1:
        p = provenance[0]
        return f"PDF {p['pdf_page']} / printed {p['printed_page']}"
    a, b = provenance[0], provenance[-1]
    return f"PDF {a['pdf_page']}→{b['pdf_page']} / printed {a['printed_page']}→{b['printed_page']}"


def dialogue_records(scene: int) -> list[dict[str, Any]]:
    path = DIALOGUES / f"scene-{scene:02d}.json"
    ensure(path.exists(), f"Missing dialogue shard {path.relative_to(ROOT)}")
    data = load_json(path)
    records = data if isinstance(data, list) else data.get("records") if isinstance(data, dict) else None
    ensure(isinstance(records, list), f"Malformed dialogue shard {path.relative_to(ROOT)}")
    return records


def render_markdown(records: list[dict[str, Any]]) -> str:
    out = [
        "# Tirumbippaar! — English Reader Edition",
        "",
        "**Tamil title:** திரும்பிப்பார்!  ",
        "**Status:** complete-verified source-linked English derivative  ",
        "**English authority:** `works/tirumbippaar/translations/records/`  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`",
        "",
        f"> Editorial note: This edition concatenates the {EXPECTED_UNITS:,} verified English units without rewriting them. Exact Tamil speaker labels remain visible for labelled dialogue; source-unlabelled speech remains unlabelled. Structural stars are not converted into invented prose.",
        "",
        "## Contents",
        "",
        *[f"- [Scene {scene}](#scene-{scene})" for scene in SCENES],
        "",
        "---",
        "",
    ]
    for record in records:
        scene = record["canonical_scene"]
        out += [f"## Scene {scene}", ""]
        for unit in record["units"]:
            uid, kind, source = unit["id"], unit["kind"], unit["source"]
            text, lines = translation_payload(unit)
            out.append(f"<!-- unit:{uid}; source:{page_label(source['page_provenance'])} -->")
            if kind == "dialogue":
                if source.get("speaker_label"):
                    out.append(f"**{source['speaker_label']}**  ")
                out.extend([text, ""])
            elif kind == "stage-direction":
                out.extend([f"*{text}*", ""])
            else:
                label = {"song":"Song","song-reference":"Song / performance reference","chant":"Chant","written-text":"Written text"}[kind]
                out.append(f"*{label}*  ")
                if lines:
                    out.extend(f"> {line}  " for line in lines)
                else:
                    out.append(f"> {text}")
                out.append("")
        out += ["---", ""]
    return "\n".join(out).rstrip() + "\n"


def render_html(records: list[dict[str, Any]]) -> str:
    nav = " ".join(f'<a href="#scene-{scene}">{scene}</a>' for scene in SCENES)
    sections: list[str] = []
    for record in records:
        scene = record["canonical_scene"]
        body = [f'<section class="scene" id="scene-{scene}"><h2>Scene {scene}</h2>']
        for unit in record["units"]:
            uid, kind, source = unit["id"], unit["kind"], unit["source"]
            text, _ = translation_payload(unit)
            content = html.escape(text).replace("\n", "<br>")
            attrs = f'data-unit-id="{html.escape(uid, quote=True)}" data-source-page="{html.escape(page_label(source["page_provenance"]), quote=True)}"'
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                lead = f'<span class="speaker">{html.escape(speaker)}</span>' if isinstance(speaker, str) and speaker else ""
                body.append(f'<p class="unit dialogue" {attrs}>{lead}<span>{content}</span></p>')
            elif kind == "stage-direction":
                body.append(f'<p class="unit stage" {attrs}>{content}</p>')
            else:
                label = {"song":"Song","song-reference":"Song / performance reference","chant":"Chant","written-text":"Written text"}[kind]
                body.append(f'<div class="unit special" {attrs}><strong>{html.escape(label)}</strong><p>{content}</p></div>')
        body.append('<p class="back"><a href="#contents">Back to contents</a></p></section>')
        sections.append("\n".join(body))
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tirumbippaar! — English Reader Edition</title>
<style>
body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:56rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}nav{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.5rem 0}}.scene{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}}.dialogue{{display:grid;grid-template-columns:minmax(5rem,8rem) 1fr;gap:.75rem}}.dialogue:not(:has(.speaker)){{display:block}}.speaker{{font-weight:700}}.stage{{font-style:italic}}.special{{margin:1rem 0 1rem 1rem;border-left:2px solid;padding-left:1rem}}@media(max-width:36rem){{.dialogue{{display:block}}.speaker{{display:block}}}}@media print{{nav,.back{{display:none}}.scene{{break-before:page}}}}
</style></head><body>
<h1>Tirumbippaar! — English Reader Edition</h1><p><strong>Tamil title:</strong> திரும்பிப்பார்!</p>
<p><strong>Status:</strong> complete-verified source-linked English derivative</p>
<p>This edition concatenates the {EXPECTED_UNITS:,} verified English units without rewriting them. Exact Tamil speaker labels remain visible for labelled dialogue; source-unlabelled speech remains unlabelled.</p>
<h2 id="contents">Contents</h2><nav>{nav}</nav>{''.join(sections)}</body></html>\n'''


def main() -> int:
    index = load_json(INDEX_PATH)
    ensure(index.get("status") == "complete-verified", "Translation index is not complete-verified")
    ensure(index.get("translation_units") == EXPECTED_UNITS, "Translation unit total differs from reader checkpoint")
    ensure(index.get("unit_status_counts") == {"draft":0,"review":0,"verified":EXPECTED_UNITS}, "Translation status totals differ")
    ensure(index.get("unit_kind_counts") == EXPECTED_KINDS, "Translation kind totals differ")
    ensure(index.get("scenes_started") == SCENES and index.get("scenes_reviewed") == SCENES and index.get("scenes_verified") == SCENES, "Scene coverage differs from 1-93")
    ensure(index.get("scenes_in_review") == [], "A scene remains in review")
    meta = index.get("scene_records")
    ensure(isinstance(meta, list) and [x.get("canonical_scene") for x in meta] == SCENES, "Scene record index is incomplete or unordered")

    dialogue_by_id: dict[str, dict[str, Any]] = {}
    dialogue_paths: list[Path] = []
    for scene in SCENES:
        path = DIALOGUES / f"scene-{scene:02d}.json"
        dialogue_paths.append(path)
        for rec in dialogue_records(scene):
            rid = rec.get("id")
            ensure(isinstance(rid, str) and rid not in dialogue_by_id, f"Bad or duplicate dialogue id {rid!r}")
            dialogue_by_id[rid] = rec
    ensure(len(dialogue_by_id) == EXPECTED_DIALOGUE_RECORDS, f"Expected {EXPECTED_DIALOGUE_RECORDS} immutable dialogue records")

    song_ids = {x for x in collect_ids(load_json(SONG_INVENTORY_PATH)) if x.startswith("tirumbippaar-song-")}
    direct_expected = index.get("direct_source_unlabelled_dialogue_units")
    ensure(isinstance(direct_expected, list) and len(direct_expected) == EXPECTED_DIRECT_UNLABELLED, "Source-unlabelled dialogue index differs")

    units_seen: set[str] = set()
    dialogue_links: list[str] = []
    occurrence_links: list[str] = []
    direct_seen: list[str] = []
    cross_page: list[str] = []
    synthetic_end: list[str] = []
    kinds: Counter[str] = Counter()
    records: list[dict[str, Any]] = []
    translation_paths = [INDEX_PATH]
    previous_scene_page = 0

    for item in meta:
        scene = item["canonical_scene"]
        path = TRANSLATIONS / item["path"]
        translation_paths.append(path)
        record = load_json(path)
        records.append(record)
        ensure(record.get("canonical_scene") == scene and record.get("scene_status", record.get("pilot_status")) == "verified", f"Scene {scene} record mismatch")
        units = record.get("units")
        ensure(isinstance(units, list) and record.get("unit_count") == len(units) == item.get("unit_count"), f"Scene {scene} unit_count mismatch")
        first_page = min(p["pdf_page"] for unit in units for p in unit["source"]["page_provenance"])
        ensure(first_page >= previous_scene_page, f"Scene {scene} regresses in source-page order")
        previous_scene_page = first_page
        previous_unit_page = 0

        for ordinal, unit in enumerate(units, 1):
            uid = unit.get("id")
            ensure(uid == f"tirumbippaar-en-s{scene:03d}-u{ordinal:03d}" and isinstance(uid, str) and UNIT_RE.match(uid), f"Scene {scene} unit {ordinal} id mismatch")
            ensure(uid not in units_seen and unit.get("status") == "verified", f"Duplicate or unverified unit {uid}")
            units_seen.add(uid)
            kind = unit.get("kind")
            ensure(kind in EXPECTED_KINDS, f"Unsupported kind {kind!r} at {uid}")
            kinds[kind] += 1

            source = unit.get("source")
            ensure(isinstance(source, dict), f"Malformed source metadata at {uid}")
            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"No page provenance at {uid}")
            ensure(provenance[0]["pdf_page"] >= previous_unit_page, f"Page order regression at {uid}")
            previous_unit_page = provenance[0]["pdf_page"]
            for page in provenance:
                ensure(9 <= page.get("pdf_page", 0) <= 112 and page.get("printed_page") == page.get("pdf_page") - 8, f"Invalid page provenance at {uid}")
            if len(provenance) > 1:
                cross_page.append(uid)

            record_id = source.get("source_record_id")
            if record_id is not None:
                ensure(record_id in dialogue_by_id, f"Unknown dialogue link {record_id} at {uid}")
                immutable = dialogue_by_id[record_id]
                ensure(immutable.get("canonical_scene") == scene, f"Dialogue scene mismatch at {uid}")
                ensure(immutable.get("speaker_label") == source.get("speaker_label"), f"Speaker-label mismatch at {uid}")
                ensure(immutable.get("page_provenance") == provenance, f"Dialogue provenance mismatch at {uid}")
                dialogue_links.append(record_id)
            elif kind == "dialogue":
                ensure(uid in direct_expected and source.get("speaker_label") in {None,""}, f"Unindexed or labelled source-unlabelled speech at {uid}")
                direct_seen.append(uid)

            occurrence = source.get("source_occurrence_id")
            if occurrence is not None:
                ensure(occurrence in song_ids, f"Unknown song occurrence {occurrence} at {uid}")
                occurrence_links.append(occurrence)

            text, _ = translation_payload(unit)
            ensure(not PLACEHOLDER_RE.search(text), f"Editorial placeholder at {uid}")
            if SYNTHETIC_END_RE.match(text):
                synthetic_end.append(uid)

            segments = unit.get("translation", {}).get("english_page_segments")
            if segments is not None:
                ensure([(x.get("pdf_page"),x.get("printed_page")) for x in segments] == [(x["pdf_page"],x["printed_page"]) for x in provenance], f"English page segments mismatch at {uid}")

    ensure(not synthetic_end, f"Synthetic star-end units remain: {', '.join(synthetic_end)}")
    ensure(len(units_seen) == EXPECTED_UNITS and dict(kinds) == EXPECTED_KINDS, "Derived translation totals differ from index")
    ensure(cross_page == index.get("cross_page_translation_units") and len(cross_page) == EXPECTED_CROSS_PAGE, "Cross-page unit index differs")
    ensure(direct_seen == direct_expected, "Source-unlabelled speech index differs")
    ensure(len(dialogue_links) == len(set(dialogue_links)) == EXPECTED_DIALOGUE_RECORDS and set(dialogue_links) == set(dialogue_by_id), "Immutable dialogue links are not exact 1:1 coverage")
    ensure(occurrence_links == index.get("verified_song_reference_occurrences"), "Song occurrence links differ from translation index")

    reader_md = render_markdown(records)
    reader_html = render_html(records)
    reader_json_obj = {
        "work_id":"tirumbippaar","title":"Tirumbippaar! — English Reader Edition","title_ta":"திரும்பிப்பார்!","target_language":"en","status":"complete-verified","authority":"works/tirumbippaar/translations/records","source_sha256":SOURCE_SHA256,"canonical_scene_order":SCENES,"translation_units":EXPECTED_UNITS,"unit_kind_counts":EXPECTED_KINDS,"scenes":records,
    }
    reader_json = json.dumps(reader_json_obj, ensure_ascii=False, indent=2) + "\n"
    for uid in units_seen:
        ensure(reader_md.count(f"unit:{uid};") == 1, f"Markdown coverage mismatch for {uid}")
        ensure(reader_html.count(f'data-unit-id="{uid}"') == 1, f"HTML coverage mismatch for {uid}")

    qa = f"""# Tirumbippaar English Reader Edition — Whole-work QA

**Status:** PASS  
**English authority:** `works/tirumbippaar/translations/records/`  
**Source scan SHA-256:** `{SOURCE_SHA256}`

## Verified checks

- canonical scenes: **93/93** in source order;
- English units: **{EXPECTED_UNITS:,}/{EXPECTED_UNITS:,} unique, sequential and verified**;
- status counts: **{EXPECTED_UNITS:,} verified / 0 review / 0 draft**;
- kind counts: **1,047 dialogue / 262 stage direction / 7 song-reference / 2 chant / 11 written-text**;
- immutable labelled dialogue records linked exactly once: **{len(dialogue_links)}/1,040**;
- source-visible unlabelled spoken units retained without invented speaker/dialogue IDs: **{len(direct_seen)}**;
- verified song/performance occurrence links cross-checked: **{len(occurrence_links)}**;
- cross-page English units: **{len(cross_page)}**, exactly matching `translations/index.json`;
- all provenance lies inside PDF **9–112** / printed **1–104**, with `printed = PDF - 8`;
- source-only structural stars do not survive as synthetic `(Scene ends.)` units;
- reader Markdown and HTML contain every verified English unit exactly once;
- no editorial placeholder token appears in reader text.

## Source-sensitive structures retained

Scene 31 remains linked to `tirumbippaar-song-006` / `பாண்டியன் என் சொல்லை`. Scene 72 retains its verified source wording variants. Scene 90 retains the dying-breath transition. Scene 91 retains `பத்திரிகை News` as written text. Scene 93 retains final `வணக்கம்.` while the following `★` remains structural.

The generator writes only inside `works/tirumbippaar/editions/en/` and does not modify canonical Tamil or structured source layers.
"""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payloads = {
        OUT_DIR/"reader-edition.md": reader_md.encode(),
        OUT_DIR/"reader-edition.html": reader_html.encode(),
        OUT_DIR/"reader-edition.json": reader_json.encode(),
        OUT_DIR/"QA_REPORT.md": qa.encode(),
    }
    for path, payload in payloads.items():
        path.write_bytes(payload)

    validation_paths = translation_paths + dialogue_paths + [SONG_INVENTORY_PATH]
    manifest = {
        "work_id":"tirumbippaar","edition":"english-reader","status":"complete-verified","build_version":BUILD_VERSION,"generator":"works/tirumbippaar/editions/en/build.py","source_scan_sha256":SOURCE_SHA256,"translation_authority":"works/tirumbippaar/translations/records","translation_input_files":len(translation_paths),"translation_input_aggregate_sha256":aggregate_sha256(translation_paths),"validation_input_files":len(validation_paths),"validation_input_aggregate_sha256":aggregate_sha256(validation_paths),"canonical_scenes":SCENES,"translation_units":EXPECTED_UNITS,"unit_kind_counts":EXPECTED_KINDS,"immutable_dialogue_records_linked":len(dialogue_links),"direct_source_unlabelled_dialogue_units":direct_seen,"cross_page_units":cross_page,"song_occurrence_links":occurrence_links,"qa_status":"PASS","outputs":{path.name:{"sha256":sha256(payload),"bytes":len(payload)} for path,payload in payloads.items()},
    }
    (OUT_DIR/"manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("Tirumbippaar English whole-work QA: PASS")
    print(f"Scenes: 93 | Units: {EXPECTED_UNITS} | Dialogue links: {len(dialogue_links)} | Cross-page: {len(cross_page)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"Tirumbippaar English whole-work QA: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
