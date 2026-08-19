#!/usr/bin/env python3
"""Build and QA the provenance-safe English reader edition for the song anthology."""

from __future__ import annotations

import hashlib
import html
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "kalaignar-thirai-isai-paadalgal"
TRANS = WORK / "translations"
RECORDS = TRANS / "records"
INDEX_PATH = TRANS / "index.json"
PAGE_MAP_PATH = WORK / "songs" / "page-map.json"
SONGS = WORK / "songs"
OUT = WORK / "editions" / "en"

EXPECTED_SONGS = 54
EXPECTED_LINES = 1105
EXPECTED_PILOT = {1, 2, 3}
EXPECTED_CROSS_PAGE = {
    9: [38, 39],
    19: [53, 54],
    23: [58, 59],
    24: [62, 63],
    36: [86, 87],
    37: [90, 91],
    51: [121, 122],
    52: [123, 124],
}
SOURCE_SHA256 = "f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05"


class QAError(RuntimeError):
    pass


def ensure(condition: bool, message: str) -> None:
    if not condition:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def page_label(pages: list[int]) -> str:
    if len(pages) == 1:
        return f"PDF {pages[0]}"
    return "PDF " + "–".join(str(p) for p in (pages[0], pages[-1]))


def line_id(song_no: int, section_no: int, line_no: int) -> str:
    return f"kalaignar-song-en-{song_no:03d}-s{section_no:02d}-l{line_no:03d}"


def authoritative_input_paths() -> list[Path]:
    paths = [INDEX_PATH, PAGE_MAP_PATH]
    paths.extend(RECORDS / f"song-{n:03d}.json" for n in range(1, EXPECTED_SONGS + 1))
    paths.extend(SONGS / f"song-{n:03d}.md" for n in range(1, EXPECTED_SONGS + 1))
    return paths


def load_and_validate() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    index = load_json(INDEX_PATH)
    page_map = load_json(PAGE_MAP_PATH)

    ensure(index.get("status") == "complete-verified", "translation index is not complete-verified")
    ensure(index.get("translated_songs") == EXPECTED_SONGS, "translation index does not report 54 translated songs")
    ensure(index.get("status_counts") == {"not-started": 0, "draft": 0, "review": 0, "pilot-verified": 3, "verified": 51}, "translation status counts drifted")
    ensure(index.get("mode") == "semantic-poetic-source-faithful", "translation mode drifted")
    ensure(page_map.get("tamil_fidelity_gate") == "complete-verified", "Tamil page map is not complete-verified")

    map_rows = page_map.get("songs")
    ensure(isinstance(map_rows, list) and len(map_rows) == EXPECTED_SONGS, "page map must contain 54 songs")
    page_by_no: dict[int, list[int]] = {}
    for n, row in enumerate(map_rows, 1):
        ensure(row.get("song") == f"{n:03d}", f"page-map order mismatch at song {n:03d}")
        pages = row.get("pdf_pages")
        ensure(isinstance(pages, list) and pages and all(isinstance(p, int) for p in pages), f"bad page map at song {n:03d}")
        page_by_no[n] = pages

    index_rows = index.get("records")
    ensure(isinstance(index_rows, list) and len(index_rows) == EXPECTED_SONGS, "translation index must contain 54 record rows")

    records: list[dict[str, Any]] = []
    reader_songs: list[dict[str, Any]] = []
    seen_translation_ids: set[str] = set()
    seen_song_ids: set[str] = set()
    seen_line_ids: set[str] = set()
    status_counts: Counter[str] = Counter()
    attribution_counts: Counter[str] = Counter()
    cross_page: dict[int, list[int]] = {}
    total_lines = 0

    for n in range(1, EXPECTED_SONGS + 1):
        path = RECORDS / f"song-{n:03d}.json"
        source_path = SONGS / f"song-{n:03d}.md"
        ensure(path.exists(), f"missing translation file {path.relative_to(ROOT)}")
        ensure(source_path.exists(), f"missing Tamil source file {source_path.relative_to(ROOT)}")
        record = load_json(path)
        records.append(record)

        tid = f"kalaignar-song-en-{n:03d}"
        sid = f"kalaignar-song-{n:03d}"
        expected_status = "pilot-verified" if n in EXPECTED_PILOT else "verified"
        expected_source_path = f"works/kalaignar-thirai-isai-paadalgal/songs/song-{n:03d}.md"
        expected_record_path = f"works/kalaignar-thirai-isai-paadalgal/translations/records/song-{n:03d}.json"

        ensure(record.get("id") == tid, f"song {n:03d} translation ID mismatch")
        ensure(record.get("song_id") == sid, f"song {n:03d} song ID mismatch")
        ensure(record.get("anthology_song_number") == n, f"song {n:03d} anthology number mismatch")
        ensure(record.get("status") == expected_status, f"song {n:03d} item status mismatch")
        ensure(record.get("target_language") == "en", f"song {n:03d} target language mismatch")
        ensure(record.get("mode") == "semantic-poetic-source-faithful", f"song {n:03d} mode mismatch")
        ensure(tid not in seen_translation_ids and sid not in seen_song_ids, f"duplicate song/translation ID at {n:03d}")
        seen_translation_ids.add(tid)
        seen_song_ids.add(sid)
        status_counts[expected_status] += 1

        source = record.get("source")
        ensure(isinstance(source, dict), f"song {n:03d} missing source metadata")
        ensure(source.get("song_file") == expected_source_path, f"song {n:03d} source path mismatch")
        ensure(source.get("tamil_status") == "verified", f"song {n:03d} Tamil status mismatch")
        ensure(source.get("pdf_pages") == page_by_no[n], f"song {n:03d} PDF page mismatch")
        ensure(source.get("attribution_status") == "anthology-attributed", f"song {n:03d} attribution drift")
        attribution_counts[source.get("attribution_status")] += 1
        if len(page_by_no[n]) > 1:
            cross_page[n] = page_by_no[n]

        idx = index_rows[n - 1]
        expected_idx = {
            "translation_id": tid,
            "song_id": sid,
            "anthology_song_number": n,
            "status": expected_status,
            "source_song_file": expected_source_path,
            "source_pdf_pages": page_by_no[n],
            "translation_file": expected_record_path,
        }
        for key, value in expected_idx.items():
            ensure(idx.get(key) == value, f"song {n:03d} index mismatch for {key}")

        translation = record.get("translation")
        ensure(isinstance(translation, dict), f"song {n:03d} missing translation object")
        ensure(isinstance(translation.get("english_title"), str) and translation["english_title"].strip(), f"song {n:03d} missing English title")
        sections = translation.get("sections")
        ensure(isinstance(sections, list) and sections, f"song {n:03d} has no sections")

        reader_sections = []
        for s_no, section in enumerate(sections, 1):
            ensure(section.get("ordinal") == s_no, f"song {n:03d} section order mismatch")
            ta = section.get("source_tamil_lines")
            en = section.get("english_lines")
            ensure(isinstance(ta, list) and isinstance(en, list) and ta and en, f"song {n:03d} section {s_no} missing lines")
            ensure(len(ta) == len(en), f"song {n:03d} section {s_no} Tamil/English line-count mismatch")
            ensure(all(isinstance(x, str) and x.strip() for x in ta + en), f"song {n:03d} section {s_no} has empty/non-string lines")

            lines = []
            for l_no, (ta_line, en_line) in enumerate(zip(ta, en), 1):
                lid = line_id(n, s_no, l_no)
                ensure(lid not in seen_line_ids, f"duplicate line ID {lid}")
                seen_line_ids.add(lid)
                total_lines += 1
                lines.append({"id": lid, "source_tamil": ta_line, "english": en_line})

            reader_sections.append({
                "ordinal": s_no,
                "source_label": section.get("source_label"),
                "english_label": section.get("english_label"),
                "lines": lines,
            })

        reader_songs.append({
            "translation_id": tid,
            "song_id": sid,
            "anthology_song_number": n,
            "item_status": expected_status,
            "attribution_status": "anthology-attributed",
            "tamil_title": source.get("tamil_title"),
            "english_title": translation.get("english_title"),
            "film_title_ta": source.get("film_title_ta"),
            "source_pdf_pages": page_by_no[n],
            "source_song_file": expected_source_path,
            "source_translation_file": expected_record_path,
            "sections": reader_sections,
        })

    ensure(status_counts == Counter({"pilot-verified": 3, "verified": 51}), f"item status distribution drifted: {dict(status_counts)}")
    ensure(attribution_counts == Counter({"anthology-attributed": 54}), f"attribution distribution drifted: {dict(attribution_counts)}")
    ensure(cross_page == EXPECTED_CROSS_PAGE, f"cross-page provenance drifted: {cross_page}")
    ensure(total_lines == EXPECTED_LINES, f"mapped English line/cue total {total_lines} != {EXPECTED_LINES}")
    ensure(len(seen_line_ids) == EXPECTED_LINES, "line IDs are not unique")
    return records, reader_songs


def render_markdown(songs: list[dict[str, Any]]) -> str:
    out = [
        "# Kalaignar Film Songs — English Reader Edition",
        "",
        "**Tamil source anthology:** கலைஞர் திரை இசைப் பாடல்கள்  ",
        "**Compiler as printed:** நெல்லை ஜெயந்தா  ",
        "**Translation status:** 54/54 complete-verified source-linked English derivative  ",
        "**Translation mode:** `semantic-poetic-source-faithful`  ",
        "**Default attribution:** `anthology-attributed`  ",
        f"**Source scan SHA-256:** `{SOURCE_SHA256}`",
        "",
        "> Editorial note: This reader is generated deterministically from the verified English translation records. It does not rewrite, smooth or modernize the translations. Item-level status history remains visible: songs 001–003 are `pilot-verified`; songs 004–054 are `verified`. `anthology-attributed` does not imply original-film primary-source verification.",
        "",
        "## Contents",
        "",
    ]
    for song in songs:
        n = song["anthology_song_number"]
        out.append(f"- [{n:03d} — {song['english_title']}](#song-{n:03d})")
    out.extend(["", "---", ""])

    for song in songs:
        n = song["anthology_song_number"]
        pages = page_label(song["source_pdf_pages"])
        out.extend([
            f"<a id=\"song-{n:03d}\"></a>",
            f"## {n:03d} — {song['english_title']}",
            "",
            f"**Tamil title:** {song['tamil_title']}  ",
            f"**Film:** {song['film_title_ta']}  ",
            f"**Source:** {pages}  ",
            f"**Item status:** `{song['item_status']}`  ",
            f"**Attribution:** `{song['attribution_status']}`  ",
            f"**Tamil source record:** `{song['source_song_file']}`",
            "",
        ])
        for section in song["sections"]:
            en_label = section.get("english_label")
            ta_label = section.get("source_label")
            if en_label or ta_label:
                label = en_label or ta_label
                out.extend([f"### {label}", ""])
                if ta_label and ta_label != en_label:
                    out.extend([f"*Source label: {ta_label}*", ""])
            for line in section["lines"]:
                out.append(f"<!-- line:{line['id']} -->")
                out.append(line["english"] + "  ")
            out.append("")
        out.extend(["---", ""])
    return "\n".join(out).rstrip() + "\n"


def render_html(songs: list[dict[str, Any]]) -> str:
    nav = "".join(
        f'<li><a href="#song-{s["anthology_song_number"]:03d}">{s["anthology_song_number"]:03d} — {html.escape(s["english_title"])}</a></li>'
        for s in songs
    )
    blocks: list[str] = []
    for song in songs:
        n = song["anthology_song_number"]
        meta = (
            f'<dl><dt>Tamil title</dt><dd lang="ta">{html.escape(str(song["tamil_title"]))}</dd>'
            f'<dt>Film</dt><dd lang="ta">{html.escape(str(song["film_title_ta"]))}</dd>'
            f'<dt>Source</dt><dd>{html.escape(page_label(song["source_pdf_pages"]))}</dd>'
            f'<dt>Item status</dt><dd><code>{html.escape(song["item_status"])}</code></dd>'
            f'<dt>Attribution</dt><dd><code>{html.escape(song["attribution_status"])}</code></dd>'
            f'<dt>Tamil source record</dt><dd><code>{html.escape(song["source_song_file"])}</code></dd></dl>'
        )
        sections = []
        for section in song["sections"]:
            parts = ['<section class="lyric-section">']
            en_label = section.get("english_label")
            ta_label = section.get("source_label")
            if en_label or ta_label:
                parts.append(f'<h3>{html.escape(str(en_label or ta_label))}</h3>')
                if ta_label and ta_label != en_label:
                    parts.append(f'<p class="source-label" lang="ta">Source label: {html.escape(str(ta_label))}</p>')
            for line in section["lines"]:
                parts.append(f'<div class="lyric-line" data-line-id="{line["id"]}">{html.escape(line["english"])}</div>')
            parts.append("</section>")
            sections.append("\n".join(parts))
        blocks.append(
            f'<article class="song" id="song-{n:03d}" data-song-id="{song["song_id"]}" data-translation-id="{song["translation_id"]}">'
            f'<h2>{n:03d} — {html.escape(song["english_title"])}</h2>{meta}{"".join(sections)}'
            '<p class="back"><a href="#contents">Back to contents</a></p></article>'
        )

    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kalaignar Film Songs — English Reader Edition</title>
<style>body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:58rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}a{{text-underline-offset:.15em}}.song{{border-top:1px solid #aaa;margin-top:2.75rem;padding-top:1.25rem}}dl{{display:grid;grid-template-columns:max-content 1fr;gap:.2rem 1rem;font-size:.92rem}}dt{{font-weight:700}}dd{{margin:0}}.lyric-section{{margin:1.25rem 0}}.lyric-section h3{{font-size:1rem;margin-bottom:.4rem}}.source-label{{font-size:.9rem;font-style:italic}}.lyric-line{{white-space:pre-wrap}}@media(max-width:36rem){{dl{{display:block}}dt{{margin-top:.45rem}}}}@media print{{#contents,.back{{display:none}}.song{{break-before:page}}}}</style>
</head><body><header><h1>Kalaignar Film Songs — English Reader Edition</h1><p><strong>Tamil source anthology:</strong> <span lang="ta">கலைஞர் திரை இசைப் பாடல்கள்</span></p><p><strong>Translation status:</strong> 54/54 complete-verified source-linked English derivative</p><p><strong>Translation mode:</strong> <code>semantic-poetic-source-faithful</code></p><p><strong>Editorial note:</strong> Generated deterministically from the verified English records without smoothing or rewriting. Songs 001–003 remain <code>pilot-verified</code>; 004–054 remain <code>verified</code>. All 54 remain <code>anthology-attributed</code>.</p></header><section id="contents"><h2>Contents</h2><ol>{nav}</ol></section>{''.join(blocks)}</body></html>\n'''


def reader_json(songs: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "work_id": "kalaignar-thirai-isai-paadalgal",
        "edition": "english-reader",
        "build_version": BUILD_VERSION,
        "status": "complete-verified",
        "translation_mode": "semantic-poetic-source-faithful",
        "default_attribution_status": "anthology-attributed",
        "source_sha256": SOURCE_SHA256,
        "song_count": EXPECTED_SONGS,
        "line_cue_count": EXPECTED_LINES,
        "item_status_counts": {"pilot-verified": 3, "verified": 51},
        "songs": songs,
    }


def qa_outputs(songs: list[dict[str, Any]], md: str, html_text: str, json_payload: dict[str, Any]) -> dict[str, Any]:
    expected_song_ids = [s["song_id"] for s in songs]
    expected_translation_ids = [s["translation_id"] for s in songs]
    expected_line_ids = [line["id"] for s in songs for section in s["sections"] for line in section["lines"]]

    ensure(len(expected_song_ids) == len(set(expected_song_ids)) == EXPECTED_SONGS, "source song IDs are not unique")
    ensure(len(expected_translation_ids) == len(set(expected_translation_ids)) == EXPECTED_SONGS, "translation IDs are not unique")
    ensure(len(expected_line_ids) == len(set(expected_line_ids)) == EXPECTED_LINES, "line IDs are not unique")

    json_songs = json_payload.get("songs")
    ensure(isinstance(json_songs, list) and [s.get("song_id") for s in json_songs] == expected_song_ids, "reader JSON song order/coverage mismatch")
    ensure([s.get("translation_id") for s in json_songs] == expected_translation_ids, "reader JSON translation ID order mismatch")
    ensure(json_payload.get("line_cue_count") == EXPECTED_LINES, "reader JSON line total mismatch")

    md_song_markers = [f'<a id="song-{n:03d}"></a>' for n in range(1, EXPECTED_SONGS + 1)]
    ensure(all(md.count(marker) == 1 for marker in md_song_markers), "Markdown missing/duplicate song anchors")
    ensure(all(md.count(f"<!-- line:{lid} -->") == 1 for lid in expected_line_ids), "Markdown missing/duplicate line markers")

    ensure(all(html_text.count(f'data-song-id="{sid}"') == 1 for sid in expected_song_ids), "HTML missing/duplicate song IDs")
    ensure(all(html_text.count(f'data-translation-id="{tid}"') == 1 for tid in expected_translation_ids), "HTML missing/duplicate translation IDs")
    ensure(all(html_text.count(f'data-line-id="{lid}"') == 1 for lid in expected_line_ids), "HTML missing/duplicate line IDs")

    # Confirm every English line is preserved exactly in JSON and as escaped text in HTML.
    json_line_by_id = {
        line["id"]: line["english"]
        for s in json_songs
        for section in s["sections"]
        for line in section["lines"]
    }
    ensure(len(json_line_by_id) == EXPECTED_LINES, "reader JSON line ID coverage mismatch")
    for s in songs:
        for section in s["sections"]:
            for line in section["lines"]:
                lid, text = line["id"], line["english"]
                ensure(json_line_by_id.get(lid) == text, f"reader JSON text drift at {lid}")
                expected_html = f'data-line-id="{lid}">{html.escape(text)}</div>'
                ensure(html_text.count(expected_html) == 1, f"HTML text drift at {lid}")

    cross = {s["anthology_song_number"]: s["source_pdf_pages"] for s in songs if len(s["source_pdf_pages"]) > 1}
    ensure(cross == EXPECTED_CROSS_PAGE, f"generated cross-page metadata drifted: {cross}")
    ensure(Counter(s["item_status"] for s in songs) == Counter({"pilot-verified": 3, "verified": 51}), "generated status distribution drifted")
    ensure(Counter(s["attribution_status"] for s in songs) == Counter({"anthology-attributed": 54}), "generated attribution distribution drifted")

    return {
        "status": "PASS",
        "songs": EXPECTED_SONGS,
        "line_cues": EXPECTED_LINES,
        "pilot_verified": 3,
        "verified": 51,
        "cross_page_records": 8,
        "markdown_song_anchors": EXPECTED_SONGS,
        "markdown_line_markers": EXPECTED_LINES,
        "html_song_markers": EXPECTED_SONGS,
        "html_line_markers": EXPECTED_LINES,
        "json_song_records": EXPECTED_SONGS,
        "json_line_records": EXPECTED_LINES,
        "warnings": 0,
        "errors": 0,
    }


def render_qa(qa: dict[str, Any]) -> str:
    return f"""# கலைஞர் திரை இசைப் பாடல்கள் — English Reader/Export Generated-Output QA

Status: **PASS**

This report validates the deterministic reader/export package generated from the 54 complete-verified source-linked English translation records. The build does not edit the Tamil or English source-linked layers.

## Generated package

- `reader-edition.md`
- `reader-edition.html`
- `reader-edition.json`
- `QA_REPORT.md`
- `manifest.json`

## PASS results

| Check | Result |
|---|---:|
| Songs in anthology order | **{qa['songs']} / {qa['songs']}** |
| English lyric lines/cues | **{qa['line_cues']} / {qa['line_cues']}** |
| Pilot-verified items | **{qa['pilot_verified']}** (`001–003`) |
| Verified items | **{qa['verified']}** (`004–054`) |
| Cross-page records | **{qa['cross_page_records']} / 8** |
| Markdown song anchors | **{qa['markdown_song_anchors']} / 54** |
| Markdown line markers | **{qa['markdown_line_markers']} / 1,105** |
| HTML song markers | **{qa['html_song_markers']} / 54** |
| HTML line markers | **{qa['html_line_markers']} / 1,105** |
| JSON song records | **{qa['json_song_records']} / 54** |
| JSON line records | **{qa['json_line_records']} / 1,105** |
| Attribution drift | **0** |
| Status drift | **0** |
| Source-page drift | **0** |
| Missing/extra/duplicate song IDs | **0** |
| Missing/extra/duplicate translation IDs | **0** |
| Missing/extra/duplicate line IDs | **0** |
| English-line text drift in JSON/HTML | **0** |
| Warnings | **{qa['warnings']}** |
| Errors | **{qa['errors']}** |

## Provenance safeguards

All 54 generated song entries retain Tamil title, English title, film title, source PDF page array, immutable Tamil source path, item status and `anthology-attributed` state. All eight cross-page records retain their full arrays: `009` 38–39, `019` 53–54, `023` 58–59, `024` 62–63, `036` 86–87, `037` 90–91, `051` 121–122 and `052` 123–124.

## Kalaignar-language safeguard

The build concatenates the stored English lines/cues exactly. It does not smooth, paraphrase, modernize or replace source-shaped English during publication generation. The 1,105 stored English lines/cues are represented exactly once in each machine-addressable output layer.

## Gate disposition

**Generated-output QA: PASS.**

The deterministic English reader/export package is complete-verified and may proceed to downstream Reading Room integration without reopening the verified Tamil or English source-linked layers.
"""


def build_manifest(input_paths: list[Path], output_paths: list[Path]) -> dict[str, Any]:
    return {
        "work_id": "kalaignar-thirai-isai-paadalgal",
        "edition": "english-reader",
        "build_version": BUILD_VERSION,
        "status": "complete-verified",
        "source_sha256": SOURCE_SHA256,
        "deterministic": True,
        "input_count": len(input_paths),
        "inputs": [
            {"path": p.relative_to(ROOT).as_posix(), "sha256": sha256_path(p), "bytes": p.stat().st_size}
            for p in sorted(input_paths, key=lambda p: p.as_posix())
        ],
        "outputs": [
            {"path": p.relative_to(ROOT).as_posix(), "sha256": sha256_path(p), "bytes": p.stat().st_size}
            for p in output_paths
        ],
        "manifest_note": "manifest.json intentionally does not hash itself to avoid a circular self-hash",
    }


def main() -> int:
    _, songs = load_and_validate()
    OUT.mkdir(parents=True, exist_ok=True)

    md = render_markdown(songs)
    html_text = render_html(songs)
    json_payload = reader_json(songs)
    json_text = json.dumps(json_payload, ensure_ascii=False, indent=2) + "\n"

    md_path = OUT / "reader-edition.md"
    html_path = OUT / "reader-edition.html"
    json_path = OUT / "reader-edition.json"
    qa_path = OUT / "QA_REPORT.md"
    manifest_path = OUT / "manifest.json"

    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html_text, encoding="utf-8")
    json_path.write_text(json_text, encoding="utf-8")

    # Read generated files back from disk for the generated-output gate.
    qa = qa_outputs(
        songs,
        md_path.read_text(encoding="utf-8"),
        html_path.read_text(encoding="utf-8"),
        load_json(json_path),
    )
    qa_path.write_text(render_qa(qa), encoding="utf-8")

    inputs = authoritative_input_paths()
    ensure(all(p.exists() for p in inputs), "one or more authoritative manifest inputs are missing")
    outputs = [md_path, html_path, json_path, qa_path]
    manifest = build_manifest(inputs, outputs)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("KALAIGNAR SONG ANTHOLOGY ENGLISH READER BUILD")
    print("status= PASS")
    print("songs=", EXPECTED_SONGS)
    print("line_cues=", EXPECTED_LINES)
    print("input_files_hashed=", len(inputs))
    print("generated_outputs=", [p.name for p in outputs] + [manifest_path.name])
    print("warnings= 0")
    print("errors= 0")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print("KALAIGNAR SONG ANTHOLOGY ENGLISH READER BUILD", file=sys.stderr)
        print("status= FAIL", file=sys.stderr)
        print(f"error= {exc}", file=sys.stderr)
        raise SystemExit(1)
