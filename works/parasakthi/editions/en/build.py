#!/usr/bin/env python3
"""Build and QA the provenance-safe Parasakthi English reader edition.

The verified scene-sharded translation records are the English authority.
This script validates structure and source links, then emits continuous
Markdown, HTML, and JSON reader exports plus a deterministic QA report and
manifest. It writes only inside works/parasakthi/editions/en/.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 3
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "parasakthi"
TRANSLATIONS = WORK / "translations"
INDEX_PATH = TRANSLATIONS / "index.json"
SONG_INVENTORY_PATH = WORK / "songs" / "inventory.json"
OUT_DIR = WORK / "editions" / "en"

EXPECTED_SCENES = [n for n in range(1, 49) if n not in {23, 34}]
EXPECTED_ABSENT = [23, 34]
EXPECTED_UNITS = 769
EXPECTED_KIND_COUNTS = {
    "dialogue": 641,
    "stage-direction": 114,
    "song": 13,
    "quoted-verse": 1,
}
EXPECTED_CROSS_PAGE = 16
EXPECTED_SOURCE_SHA256 = "b0024315ca2018a63807b8ff44eb02d132868a7250e6399a2144a10e47c4ad4c"
ALLOWED_KINDS = set(EXPECTED_KIND_COUNTS)
UNIT_ID_RE = re.compile(r"^parasakthi-en-s(?P<scene>\d{3})-u(?P<unit>\d{3})$")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[\[\?\]\]|\{\{.+?\}\}", re.IGNORECASE)


class QAError(RuntimeError):
    pass


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"Cannot parse JSON {path.relative_to(ROOT)}: {exc}") from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate_sha256(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda p: p.as_posix()):
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def collect_ids(node: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(node, dict):
        if isinstance(node.get("id"), str):
            found.add(node["id"])
        for value in node.values():
            found.update(collect_ids(value))
    elif isinstance(node, list):
        for value in node:
            found.update(collect_ids(value))
    return found


def source_records(path: Path, cache: dict[Path, dict[str, dict[str, Any]]]) -> dict[str, dict[str, Any]]:
    if path not in cache:
        data = load_json(path)
        records = data.get("records") if isinstance(data, dict) else None
        ensure(isinstance(records, list), f"Source record file has no records array: {path.relative_to(ROOT)}")
        indexed: dict[str, dict[str, Any]] = {}
        for record in records:
            ensure(isinstance(record, dict) and isinstance(record.get("id"), str), f"Malformed source record in {path.relative_to(ROOT)}")
            ensure(record["id"] not in indexed, f"Duplicate source record id {record['id']} in {path.relative_to(ROOT)}")
            indexed[record["id"]] = record
        cache[path] = indexed
    return cache[path]


def translation_parts(unit: dict[str, Any]) -> tuple[str | None, list[str] | None]:
    translation = unit["translation"]
    text = translation.get("english_text")
    lines = translation.get("english_lines")
    return text if isinstance(text, str) else None, lines if isinstance(lines, list) else None


def unit_text(unit: dict[str, Any]) -> str:
    text, lines = translation_parts(unit)
    if text is not None:
        return text
    assert lines is not None
    return "\n".join(lines)


def page_label(provenance: list[dict[str, int]]) -> str:
    if len(provenance) == 1:
        p = provenance[0]
        return f"PDF {p['pdf_page']} / printed {p['printed_page']}"
    first, last = provenance[0], provenance[-1]
    return f"PDF {first['pdf_page']}→{last['pdf_page']} / printed {first['printed_page']}→{last['printed_page']}"


def render_markdown(scenes: list[dict[str, Any]]) -> str:
    out: list[str] = [
        "# Parasakthi — English Reader Edition",
        "",
        "**Status:** complete-verified source-linked English derivative  ",
        "**English authority:** `works/parasakthi/translations/records/`  ",
        f"**Source scan SHA-256:** `{EXPECTED_SOURCE_SHA256}`",
        "",
        "> Editorial note: This edition concatenates the 769 verified English units without rewriting them. Exact Tamil speaker labels are retained where supplied by the source-linked record. Canonical scenes 23 and 34 are absent and are not invented here.",
        "",
        "## Contents",
        "",
    ]
    out.extend(f"- [Scene {scene}](#scene-{scene})" for scene in EXPECTED_SCENES)
    out.extend(["", "---", ""])

    for record in scenes:
        scene = record["canonical_scene"]
        out.extend([f"## Scene {scene}", ""])
        if scene == 43:
            out.extend(["*Source-numbering provenance: canonical scene 43 corresponds to the booklet heading printed as scene 48 on PDF 49.*", ""])
        elif scene == 48:
            out.extend(["*Source-numbering provenance: canonical final scene 48 corresponds to the booklet heading printed as scene 43 on PDF 57.*", ""])

        for unit in record["units"]:
            uid = unit["id"]
            source = unit["source"]
            kind = unit["kind"]
            text, lines = translation_parts(unit)
            out.append(f"<!-- unit:{uid}; source:{page_label(source['page_provenance'])} -->")
            if kind == "dialogue":
                if source.get("speaker_label"):
                    out.append(f"**{source['speaker_label']}**  ")
                if text is not None:
                    out.append(text)
                else:
                    out.extend(f"> {line}  " for line in lines or [])
            elif kind == "stage-direction":
                if text is not None:
                    out.append(f"*{text}*")
                else:
                    out.extend(f"*{line}*  " for line in lines or [])
            else:
                out.append(f"*{'Song' if kind == 'song' else 'Quoted verse'}*  ")
                if lines is not None:
                    out.extend(f"> {line}  " for line in lines)
                elif text is not None:
                    out.append(f"> {text}")
            out.append("")
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(scenes: list[dict[str, Any]]) -> str:
    nav = "\n".join(f'<a href="#scene-{scene}">Scene {scene}</a>' for scene in EXPECTED_SCENES)
    sections: list[str] = []
    for record in scenes:
        scene = record["canonical_scene"]
        body = [f'<section class="scene" id="scene-{scene}">', f"<h2>Scene {scene}</h2>"]
        if scene == 43:
            body.append('<p class="provenance">Source-numbering provenance: canonical scene 43 corresponds to the booklet heading printed as scene 48 on PDF 49.</p>')
        elif scene == 48:
            body.append('<p class="provenance">Source-numbering provenance: canonical final scene 48 corresponds to the booklet heading printed as scene 43 on PDF 57.</p>')

        for unit in record["units"]:
            uid = html.escape(unit["id"], quote=True)
            source = unit["source"]
            kind = unit["kind"]
            text, lines = translation_parts(unit)
            page = html.escape(page_label(source["page_provenance"]), quote=True)
            if kind == "dialogue":
                speaker = source.get("speaker_label")
                speaker_html = f'<span class="speaker">{html.escape(speaker)}</span>' if speaker else ""
                if text is not None:
                    content = html.escape(text).replace("\n", "<br>")
                else:
                    content = "<br>\n".join(html.escape(line) for line in lines or [])
                body.append(f'<p class="unit dialogue" data-unit-id="{uid}" data-source-page="{page}">{speaker_html}<span class="text">{content}</span></p>')
            elif kind == "stage-direction":
                content = html.escape(text).replace("\n", "<br>") if text is not None else "<br>\n".join(html.escape(line) for line in lines or [])
                body.append(f'<p class="unit stage" data-unit-id="{uid}" data-source-page="{page}">{content}</p>')
            else:
                label = "Song" if kind == "song" else "Quoted verse"
                content = "<br>\n".join(html.escape(line) for line in lines) if lines is not None else html.escape(text or "")
                body.append(f'<div class="unit verse" data-unit-id="{uid}" data-source-page="{page}"><p class="verse-label">{label}</p><p>{content}</p></div>')
        body.append('<p class="back"><a href="#contents">Back to contents</a></p>')
        body.append("</section>")
        sections.append("\n".join(body))

    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Parasakthi — English Reader Edition</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ font-family: ui-serif, Georgia, "Times New Roman", serif; max-width: 54rem; margin: 0 auto; padding: 2rem 1.25rem 5rem; line-height: 1.65; }}
h1, h2 {{ line-height: 1.2; }}
.note, .provenance {{ font-style: italic; opacity: .82; }}
nav {{ display: flex; flex-wrap: wrap; gap: .35rem .8rem; margin: 1.5rem 0 2.5rem; }}
nav a {{ white-space: nowrap; }}
.scene {{ padding-top: 1rem; border-top: 1px solid currentColor; margin-top: 2.5rem; }}
.dialogue {{ display: grid; grid-template-columns: minmax(4.5rem, 7rem) 1fr; gap: .75rem; }}
.dialogue:not(:has(.speaker)) {{ display: block; }}
.speaker {{ font-weight: 700; }}
.stage {{ font-style: italic; }}
.verse {{ margin: 1.2rem 0 1.2rem 2rem; }}
.verse-label {{ font-style: italic; font-weight: 600; }}
.back {{ font-size: .9rem; }}
@media (max-width: 36rem) {{ .dialogue {{ display: block; }} .speaker {{ display: block; margin-bottom: .2rem; }} .verse {{ margin-left: 1rem; }} }}
@media print {{ nav, .back {{ display: none; }} body {{ max-width: none; }} .scene {{ break-before: page; }} }}
</style>
</head>
<body>
<header>
<h1>Parasakthi — English Reader Edition</h1>
<p><strong>Status:</strong> complete-verified source-linked English derivative</p>
<p class="note">This edition concatenates the 769 verified English units without rewriting them. Exact Tamil speaker labels are retained where supplied. Canonical scenes 23 and 34 are absent and are not invented.</p>
</header>
<h2 id="contents">Contents</h2>
<nav aria-label="Scene navigation">{nav}</nav>
{''.join(sections)}
</body>
</html>
'''


def main() -> int:
    index = load_json(INDEX_PATH)
    ensure(index.get("status") == "complete-verified", "Translation index is not complete-verified")
    ensure(index.get("target_language") == "en", "Translation index target language is not en")
    ensure(index.get("translation_units") == EXPECTED_UNITS, f"Expected {EXPECTED_UNITS} indexed units")
    ensure(index.get("unit_status_counts") == {"draft": 0, "review": 0, "verified": EXPECTED_UNITS}, "Translation status counts are not 0 draft / 0 review / 769 verified")
    ensure(index.get("unit_kind_counts") == EXPECTED_KIND_COUNTS, "Indexed unit-kind counts differ from the verified checkpoint")
    ensure(index.get("scenes_started") == EXPECTED_SCENES, "scenes_started does not match the 46 observed canonical scenes")
    ensure(index.get("scenes_reviewed") == EXPECTED_SCENES, "scenes_reviewed does not match the 46 observed canonical scenes")
    ensure(index.get("scenes_verified") == EXPECTED_SCENES, "scenes_verified does not match the 46 observed canonical scenes")
    ensure(index.get("scenes_in_review") == [], "scenes_in_review is not empty")
    ensure(index.get("absent_canonical_scenes") == EXPECTED_ABSENT, "Absent canonical scenes are not exactly 23 and 34")

    scene_meta = index.get("scene_records")
    ensure(isinstance(scene_meta, list), "scene_records is missing or malformed")
    ensure([item.get("canonical_scene") for item in scene_meta] == EXPECTED_SCENES, "scene_records order/coverage does not match canonical observed scenes")

    song_ids = {value for value in collect_ids(load_json(SONG_INVENTORY_PATH)) if value.startswith("parasakthi-song-")}
    record_cache: dict[Path, dict[str, dict[str, Any]]] = {}
    seen: set[str] = set()
    kinds: Counter[str] = Counter()
    cross_page: list[str] = []
    direct_labelled: list[str] = []
    direct_unlabelled: list[str] = []
    source_paths_checked: set[Path] = set()
    dialogue_links_checked = 0
    occurrence_links_checked = 0
    input_paths = [INDEX_PATH]
    scenes: list[dict[str, Any]] = []
    previous_scene_page = 0

    for meta in scene_meta:
        scene = meta["canonical_scene"]
        path = TRANSLATIONS / meta["path"]
        ensure(path.exists(), f"Missing translation scene record {path.relative_to(ROOT)}")
        input_paths.append(path)
        record = load_json(path)
        scenes.append(record)
        ensure(record.get("canonical_scene") == scene, f"Scene mismatch in {path.relative_to(ROOT)}")
        ensure(record.get("scene_status", record.get("pilot_status")) == "verified", f"Scene {scene} is not verified")
        units = record.get("units")
        ensure(isinstance(units, list) and units, f"Scene {scene} has no units array")
        ensure(record.get("unit_count") == len(units) == meta.get("unit_count"), f"Scene {scene} unit count mismatch")
        ensure(meta.get("status") == "verified", f"Scene {scene} index status is not verified")

        first_scene_page = min(page["pdf_page"] for unit in units for page in unit["source"]["page_provenance"])
        ensure(first_scene_page >= previous_scene_page, f"Scene {scene} regresses in canonical source-page order")
        previous_scene_page = first_scene_page
        previous_unit_page = 0

        for ordinal, unit in enumerate(units, 1):
            uid = unit.get("id")
            expected = f"parasakthi-en-s{scene:03d}-u{ordinal:03d}"
            ensure(uid == expected and UNIT_ID_RE.match(uid), f"Scene {scene} unit {ordinal} id mismatch: {uid!r}")
            ensure(uid not in seen, f"Duplicate English unit id {uid}")
            seen.add(uid)
            ensure(unit.get("canonical_scene") == scene, f"Unit {uid} canonical_scene mismatch")
            ensure(unit.get("target_language") == "en", f"Unit {uid} target_language is not en")
            ensure(unit.get("status") == "verified", f"Unit {uid} is not verified")
            kind = unit.get("kind")
            ensure(kind in ALLOWED_KINDS, f"Unit {uid} has unsupported kind {kind!r}")
            kinds[kind] += 1

            source = unit.get("source")
            ensure(isinstance(source, dict), f"Unit {uid} has malformed source metadata")
            source_path_text = source.get("source_path")
            ensure(isinstance(source_path_text, str) and source_path_text, f"Unit {uid} has no source_path")
            source_path = ROOT / source_path_text
            ensure(source_path.exists(), f"Unit {uid} source path does not exist: {source_path_text}")
            source_paths_checked.add(source_path)

            record_id = source.get("source_record_id")
            occurrence_id = source.get("source_occurrence_id")
            locator = source.get("source_locator")
            ensure(record_id is not None or occurrence_id is not None or locator is not None, f"Unit {uid} has no record, occurrence, or direct source locator")

            provenance = source.get("page_provenance")
            ensure(isinstance(provenance, list) and provenance, f"Unit {uid} has no page provenance")
            first_unit_page = provenance[0].get("pdf_page")
            ensure(isinstance(first_unit_page, int) and first_unit_page >= previous_unit_page, f"Unit {uid} regresses in source-page order within scene {scene}")
            previous_unit_page = first_unit_page
            for page in provenance:
                pdf_page = page.get("pdf_page")
                printed_page = page.get("printed_page")
                ensure(isinstance(pdf_page, int) and 4 <= pdf_page <= 57, f"Unit {uid} PDF page {pdf_page!r} is outside canonical range 4-57")
                ensure(isinstance(printed_page, int) and printed_page == pdf_page - 1, f"Unit {uid} printed/PDF page mapping is inconsistent")
            if len(provenance) > 1:
                cross_page.append(uid)

            if record_id is not None:
                ensure(isinstance(record_id, str) and record_id, f"Unit {uid} has malformed source_record_id")
                records = source_records(source_path, record_cache)
                ensure(record_id in records, f"Unit {uid} source_record_id {record_id} not found in {source_path_text}")
                source_record = records[record_id]
                ensure(source_record.get("canonical_scene") == scene, f"Unit {uid} source record scene mismatch")
                ensure(source_record.get("speaker_label") == source.get("speaker_label"), f"Unit {uid} speaker label differs from immutable source record")
                ensure(source_record.get("page_provenance") == provenance, f"Unit {uid} page provenance differs from immutable source record")
                dialogue_links_checked += 1

            if occurrence_id is not None:
                ensure(isinstance(occurrence_id, str) and occurrence_id in song_ids, f"Unit {uid} occurrence id {occurrence_id!r} not found in verified song inventory")
                occurrence_links_checked += 1

            if kind == "dialogue" and record_id is None:
                ensure(locator is not None, f"Source-located dialogue {uid} has no source locator")
                (direct_labelled if source.get("speaker_label") else direct_unlabelled).append(uid)

            translation = unit.get("translation")
            ensure(isinstance(translation, dict), f"Unit {uid} has malformed translation")
            text, lines = translation_parts(unit)
            ensure((text is not None) ^ (lines is not None), f"Unit {uid} must have exactly one of english_text or english_lines")
            if text is not None:
                ensure(bool(text.strip()), f"Unit {uid} has empty english_text")
            else:
                ensure(bool(lines) and all(isinstance(line, str) for line in lines), f"Unit {uid} has malformed english_lines")
            ensure(not PLACEHOLDER_RE.search(unit_text(unit)), f"Unit {uid} contains an editorial placeholder token")
            ensure(translation.get("mode") in {"prose-faithful", "semantic-poetic"}, f"Unit {uid} has invalid translation mode")
            ensure(isinstance(translation.get("notes"), list), f"Unit {uid} notes is not an array")

            segments = translation.get("english_page_segments")
            if segments is not None:
                ensure(isinstance(segments, list) and len(segments) >= 2, f"Unit {uid} has malformed english_page_segments")
                segment_pages = [(seg.get("pdf_page"), seg.get("printed_page")) for seg in segments]
                provenance_pages = [(page["pdf_page"], page["printed_page"]) for page in provenance]
                ensure(segment_pages == provenance_pages, f"Unit {uid} english_page_segments do not match page provenance")
                ensure(all(isinstance(seg.get("english_text"), str) and seg["english_text"].strip() for seg in segments), f"Unit {uid} has an empty English page segment")

    ensure(len(seen) == EXPECTED_UNITS, f"Expected {EXPECTED_UNITS} unique units, found {len(seen)}")
    ensure(dict(kinds) == EXPECTED_KIND_COUNTS, f"Aggregated kind counts differ: {dict(kinds)}")
    ensure(cross_page == index.get("cross_page_translation_units"), "Derived cross-page unit list differs from translations/index.json")
    ensure(len(cross_page) == EXPECTED_CROSS_PAGE, f"Expected {EXPECTED_CROSS_PAGE} cross-page units")
    ensure(direct_labelled == index.get("source_linked_labelled_units_without_dialogue_record"), "Direct source-linked labelled dialogue list differs from index")

    direct_non_dialogue = index.get("source_linked_non_dialogue_units_outside_dialogue_derivative", [])
    ensure(isinstance(direct_non_dialogue, list) and len(direct_non_dialogue) == 2, "Expected two indexed direct source-linked non-dialogue units")
    unit_by_id = {unit["id"]: unit for record in scenes for unit in record["units"]}
    for uid in direct_non_dialogue:
        ensure(uid in unit_by_id, f"Indexed direct non-dialogue unit missing: {uid}")
        unit = unit_by_id[uid]
        ensure(unit["kind"] != "dialogue" and unit["source"].get("source_locator") is not None, f"Direct non-dialogue unit {uid} is not source-located")

    reader_json = {
        "work_id": "parasakthi",
        "title": "Parasakthi — English Reader Edition",
        "target_language": "en",
        "status": "complete-verified",
        "authority": "works/parasakthi/translations/records",
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "canonical_scene_order": EXPECTED_SCENES,
        "absent_canonical_scenes": EXPECTED_ABSENT,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KIND_COUNTS,
        "scenes": scenes,
    }
    reader_json_text = json.dumps(reader_json, ensure_ascii=False, indent=2) + "\n"
    reader_md = render_markdown(scenes)
    reader_html = render_html(scenes)

    for uid in seen:
        ensure(reader_md.count(f"unit:{uid};") == 1, f"Reader Markdown does not contain exactly one marker for {uid}")
        ensure(reader_html.count(f'data-unit-id="{uid}"') == 1, f"Reader HTML does not contain exactly one element for {uid}")
    ensure(reader_md.count("\n## Scene ") == len(EXPECTED_SCENES), "Reader Markdown scene heading count mismatch")
    ensure(reader_html.count('<section class="scene" id="scene-') == len(EXPECTED_SCENES), "Reader HTML scene section count mismatch")

    qa_report = f"""# Parasakthi English Reader Edition — Whole-work QA\n\n**Status:** PASS  \n**English authority:** `works/parasakthi/translations/records/`  \n**Source scan SHA-256:** `{EXPECTED_SOURCE_SHA256}`\n\n## Verified checks\n\n- observed canonical scenes: **46/46** (`1–22, 24–33, 35–48`);\n- absent canonical scenes: **23, 34** — no phantom reader sections created;\n- English units: **{EXPECTED_UNITS}/{EXPECTED_UNITS} unique, sequential and verified**;\n- status counts: **769 verified / 0 review / 0 draft**;\n- kind counts: **641 dialogue / 114 stage direction / 13 song / 1 quoted verse**;\n- cross-page units: **{len(cross_page)}**, exactly matching `translations/index.json`;\n- immutable dialogue-record links cross-checked: **{dialogue_links_checked}**;\n- verified song/verse occurrence links cross-checked: **{occurrence_links_checked}**;\n- distinct source paths existence-checked: **{len(source_paths_checked)}**;\n- direct source-linked labelled dialogue units without invented record IDs: **{len(direct_labelled)}**;\n- direct source-linked unlabelled dialogue/performance units retained without invented speaker labels: **{len(direct_unlabelled)}**;\n- additional indexed direct source-linked non-dialogue units retained: **{len(direct_non_dialogue)}**;\n- every provenance page lies inside PDF **4–57** / printed **3–56**, with the verified printed-page mapping;\n- unit order is non-regressing in source-page order within every scene;\n- scene order is non-regressing across the canonical sequence;\n- both prose (`english_text`) and semantic-poetic/performance (`english_lines`) translation payloads are preserved according to the verified record rather than coerced by unit kind;\n- reader Markdown contains every verified unit exactly once;\n- reader HTML contains every verified unit exactly once;\n- no `TODO`, `TBD`, `FIXME`, or template-placeholder token appears in reader text.\n\n## Reader-edition policy\n\nThe reader export does **not** rewrite translation text. Dialogue displays an exact Tamil source `speaker_label` only when that verified metadata exists; source-unlabelled dialogue/performance remains unlabelled. Semantic-poetic `english_lines` remain line-structured even when the archival unit kind is dialogue. Songs and quoted verse preserve verified English line order. Stage directions remain separate. Source-numbering corrections for canonical scenes **43** and **48** are stated explicitly rather than silently normalized.\n\n## Generated derivatives\n\n- `reader-edition.md` — continuous Markdown reader edition with invisible unit/page provenance comments;\n- `reader-edition.html` — standalone responsive/print-friendly HTML reader edition;\n- `reader-edition.json` — concatenated machine-readable edition retaining full source-linked unit metadata;\n- `manifest.json` — deterministic input/output integrity manifest.\n\nThe generator writes only inside `works/parasakthi/editions/en/`; it does not modify canonical Tamil, scene derivatives, dialogue records, character mappings, song inventory, Tamil song derivatives, or transcription files.\n"""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    output_payloads = {
        OUT_DIR / "reader-edition.md": reader_md.encode("utf-8"),
        OUT_DIR / "reader-edition.html": reader_html.encode("utf-8"),
        OUT_DIR / "reader-edition.json": reader_json_text.encode("utf-8"),
        OUT_DIR / "QA_REPORT.md": qa_report.encode("utf-8"),
    }
    for path, payload in output_payloads.items():
        path.write_bytes(payload)

    manifest = {
        "work_id": "parasakthi",
        "edition": "english-reader",
        "status": "complete-verified",
        "build_version": BUILD_VERSION,
        "generator": "works/parasakthi/editions/en/build.py",
        "source_scan_sha256": EXPECTED_SOURCE_SHA256,
        "translation_authority": "works/parasakthi/translations/records",
        "translation_input_files": len(input_paths),
        "translation_input_aggregate_sha256": aggregate_sha256(input_paths),
        "observed_scenes": EXPECTED_SCENES,
        "absent_canonical_scenes": EXPECTED_ABSENT,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KIND_COUNTS,
        "cross_page_units": len(cross_page),
        "direct_source_labelled_dialogue_units": direct_labelled,
        "direct_source_unlabelled_dialogue_units": direct_unlabelled,
        "direct_source_non_dialogue_units": direct_non_dialogue,
        "qa_status": "PASS",
        "outputs": {
            path.name: {"sha256": sha256_bytes(payload), "bytes": len(payload)}
            for path, payload in output_payloads.items()
        },
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Parasakthi English whole-work QA: PASS")
    print(f"Scenes: {len(EXPECTED_SCENES)} | Units: {len(seen)} | Cross-page: {len(cross_page)}")
    print(f"Dialogue source links checked: {dialogue_links_checked} | Song/verse occurrences checked: {occurrence_links_checked}")
    print(f"Direct source dialogue: labelled {len(direct_labelled)} / unlabelled {len(direct_unlabelled)}")
    print(f"Outputs written to {OUT_DIR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print(f"Parasakthi English whole-work QA: FAIL\n{exc}", file=sys.stderr)
        raise SystemExit(1)
