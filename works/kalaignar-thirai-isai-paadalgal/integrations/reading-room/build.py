#!/usr/bin/env python3
"""Build and QA a provenance-safe Reading Room integration payload for the song anthology."""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path
from typing import Any

BUILD_VERSION = 1
ROOT = Path(__file__).resolve().parents[5]
WORK = ROOT / "works" / "kalaignar-thirai-isai-paadalgal"
READER_PATH = WORK / "editions" / "en" / "reader-edition.json"
READER_MANIFEST_PATH = WORK / "editions" / "en" / "manifest.json"
SONG_INDEX_PATH = WORK / "songs" / "index.json"
PAGE_MAP_PATH = WORK / "songs" / "page-map.json"
TRANSLATION_INDEX_PATH = WORK / "translations" / "index.json"
OUT = WORK / "integrations" / "reading-room"

EXPECTED_FILMS = 23
EXPECTED_SONGS = 54
EXPECTED_LINES = 1105
EXPECTED_CROSS_PAGE = 8
SOURCE_SHA256 = "f0beac14c33ffc73c0231bd54ca57ec4093eef6e85072bd68ce48f7b5e258b05"


class QAError(RuntimeError):
    pass


def ensure(ok: bool, message: str) -> None:
    if not ok:
        raise QAError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise QAError(f"cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ordered_film_groups(song_rows: list[dict[str, Any]]) -> list[tuple[str, int | None, list[dict[str, Any]]]]:
    groups: OrderedDict[tuple[str, int | None], list[dict[str, Any]]] = OrderedDict()
    for row in song_rows:
        key = (row["film_title_ta"], row.get("film_year_printed"))
        groups.setdefault(key, []).append(row)
    return [(title, year, rows) for (title, year), rows in groups.items()]


def build_payload() -> tuple[dict[str, Any], dict[str, Any]]:
    reader = load_json(READER_PATH)
    song_index = load_json(SONG_INDEX_PATH)
    page_map = load_json(PAGE_MAP_PATH)
    translation_index = load_json(TRANSLATION_INDEX_PATH)

    ensure(reader.get("status") == "complete-verified", "reader edition is not complete-verified")
    ensure(reader.get("song_count") == EXPECTED_SONGS, "reader song count is not 54")
    ensure(reader.get("line_cue_count") == EXPECTED_LINES, "reader line/cue count is not 1105")
    ensure(reader.get("translation_mode") == "semantic-poetic-source-faithful", "reader translation mode drift")
    ensure(reader.get("default_attribution_status") == "anthology-attributed", "reader attribution policy drift")
    ensure(reader.get("source_sha256") == SOURCE_SHA256, "reader source checksum drift")

    reader_songs = reader.get("songs")
    ensure(isinstance(reader_songs, list) and len(reader_songs) == EXPECTED_SONGS, "reader must contain 54 songs")
    index_rows = song_index.get("records")
    ensure(isinstance(index_rows, list) and len(index_rows) == EXPECTED_SONGS, "song index must contain 54 records")
    ensure(song_index.get("status") == "complete-verified", "song index is not complete-verified")
    ensure(song_index.get("source_sha256") == SOURCE_SHA256, "song index source checksum drift")
    ensure(translation_index.get("status") == "complete-verified", "translation index is not complete-verified")
    ensure(translation_index.get("translated_songs") == EXPECTED_SONGS, "translation index does not contain 54 translated songs")
    ensure(page_map.get("tamil_fidelity_gate") == "complete-verified", "page map Tamil gate is not complete-verified")

    by_song_id = {row.get("id"): row for row in index_rows}
    ensure(len(by_song_id) == EXPECTED_SONGS, "song index contains duplicate IDs")

    statuses: Counter[str] = Counter()
    attributions: Counter[str] = Counter()
    seen_song_ids: set[str] = set()
    seen_translation_ids: set[str] = set()
    seen_line_ids: set[str] = set()
    total_lines = 0
    cross_page = 0
    integration_songs: list[dict[str, Any]] = []

    for expected_no, reader_song in enumerate(reader_songs, 1):
        sid = reader_song.get("song_id")
        tid = reader_song.get("translation_id")
        ensure(reader_song.get("anthology_song_number") == expected_no, f"reader order mismatch at {expected_no:03d}")
        ensure(sid == f"kalaignar-song-{expected_no:03d}", f"song ID mismatch at {expected_no:03d}")
        ensure(tid == f"kalaignar-song-en-{expected_no:03d}", f"translation ID mismatch at {expected_no:03d}")
        ensure(sid not in seen_song_ids and tid not in seen_translation_ids, f"duplicate ID at {expected_no:03d}")
        seen_song_ids.add(sid)
        seen_translation_ids.add(tid)

        source_row = by_song_id.get(sid)
        ensure(isinstance(source_row, dict), f"song {expected_no:03d} missing from song index")
        ensure(source_row.get("anthology_song_number") == expected_no, f"song index order mismatch at {expected_no:03d}")
        ensure(source_row.get("film_title_ta") == reader_song.get("film_title_ta"), f"film title drift at {expected_no:03d}")
        ensure(source_row.get("lyric_title") == reader_song.get("tamil_title"), f"Tamil title drift at {expected_no:03d}")
        ensure(source_row.get("status") == "verified", f"Tamil status drift at {expected_no:03d}")
        ensure(source_row.get("attribution_status") == reader_song.get("attribution_status") == "anthology-attributed", f"attribution drift at {expected_no:03d}")

        pages = reader_song.get("source_pdf_pages")
        ensure(isinstance(pages, list) and pages, f"missing source pages at {expected_no:03d}")
        map_row = page_map["songs"][expected_no - 1]
        ensure(map_row.get("song") == f"{expected_no:03d}" and map_row.get("pdf_pages") == pages, f"page provenance drift at {expected_no:03d}")
        if len(pages) > 1:
            cross_page += 1

        item_status = reader_song.get("item_status")
        statuses[item_status] += 1
        attributions[reader_song.get("attribution_status")] += 1

        sections = reader_song.get("sections")
        ensure(isinstance(sections, list) and sections, f"song {expected_no:03d} has no sections")
        copied_sections = []
        for section_no, section in enumerate(sections, 1):
            ensure(section.get("ordinal") == section_no, f"section order drift at song {expected_no:03d}")
            lines = section.get("lines")
            ensure(isinstance(lines, list) and lines, f"song {expected_no:03d} section {section_no} has no lines")
            copied_lines = []
            for line in lines:
                lid = line.get("id")
                ensure(isinstance(lid, str) and lid not in seen_line_ids, f"duplicate/invalid line ID {lid!r}")
                ensure(isinstance(line.get("source_tamil"), str) and isinstance(line.get("english"), str), f"malformed line {lid}")
                seen_line_ids.add(lid)
                total_lines += 1
                copied_lines.append({
                    "id": lid,
                    "tamil": line["source_tamil"],
                    "english": line["english"],
                })
            copied_sections.append({
                "ordinal": section_no,
                "source_label": section.get("source_label"),
                "english_label": section.get("english_label"),
                "lines": copied_lines,
            })

        integration_songs.append({
            "song_id": sid,
            "translation_id": tid,
            "anthology_song_number": expected_no,
            "item_status": item_status,
            "attribution_status": "anthology-attributed",
            "film": {
                "title_ta": source_row.get("film_title_ta"),
                "year_printed": source_row.get("film_year_printed"),
            },
            "titles": {
                "tamil": reader_song.get("tamil_title"),
                "english": reader_song.get("english_title"),
                "contents_tamil": source_row.get("contents_title"),
            },
            "credits_as_printed": {
                "music": source_row.get("music_as_printed"),
                "voice": source_row.get("voice_as_printed"),
            },
            "provenance": {
                "pdf_pages": pages,
                "section_pdf_pages": source_row.get("section_pdf_pages"),
                "tamil_source_path": reader_song.get("source_song_file"),
                "english_source_path": reader_song.get("source_translation_file"),
            },
            "sections": copied_sections,
        })

    ensure(total_lines == EXPECTED_LINES and len(seen_line_ids) == EXPECTED_LINES, f"line/cue total drift: {total_lines}")
    ensure(statuses == Counter({"pilot-verified": 3, "verified": 51}), f"status distribution drift: {dict(statuses)}")
    ensure(attributions == Counter({"anthology-attributed": 54}), f"attribution distribution drift: {dict(attributions)}")
    ensure(cross_page == EXPECTED_CROSS_PAGE, f"cross-page record count {cross_page} != 8")

    source_groups = ordered_film_groups(index_rows)
    ensure(len(source_groups) == EXPECTED_FILMS, f"film group count {len(source_groups)} != 23")
    by_no = {s["anthology_song_number"]: s for s in integration_songs}
    film_groups = []
    grouped_numbers: list[int] = []
    for film_ordinal, (title, year, rows) in enumerate(source_groups, 1):
        numbers = [row["anthology_song_number"] for row in rows]
        grouped_numbers.extend(numbers)
        film_groups.append({
            "film_id": f"kalaignar-song-film-{film_ordinal:03d}",
            "film_ordinal": film_ordinal,
            "title_ta": title,
            "year_printed": year,
            "song_count": len(numbers),
            "anthology_song_numbers": numbers,
            "songs": [by_no[n] for n in numbers],
        })
    ensure(grouped_numbers == list(range(1, EXPECTED_SONGS + 1)), "film grouping changed anthology order or coverage")

    payload = {
        "schema_version": 1,
        "integration_target": "Kalaignar Digital Library / Reading Room",
        "preferred_public_surface": "https://nenjukkuneethi.org/read",
        "integration_status": "payload-complete-verified",
        "site_application_status": "not-applied",
        "source_authority": "pugazg/kalaignar-cinema-works verified structured records",
        "work": {
            "id": "kalaignar-thirai-isai-paadalgal",
            "kind": "film-song-anthology",
            "title_ta": song_index.get("title_ta"),
            "presentation_title_en": "Kalaignar Film Songs",
            "presentation_title_en_is_editorial": True,
            "source_sha256": SOURCE_SHA256,
            "status": "complete-verified",
            "translation_mode": "semantic-poetic-source-faithful",
            "languages": ["ta", "en"],
            "default_attribution_status": "anthology-attributed",
            "counts": {
                "films": EXPECTED_FILMS,
                "songs": EXPECTED_SONGS,
                "line_cues": EXPECTED_LINES,
                "cross_page_songs": EXPECTED_CROSS_PAGE,
            },
        },
        "navigation": {
            "primary": "film",
            "secondary": "anthology-song",
            "film_order": "first appearance in anthology",
            "song_order": "anthology song number 001-054",
            "suggested_slug": "kalaignar-thirai-isai-paadalgal",
            "suggested_slug_is_presentation_metadata": True,
        },
        "language_presentation": {
            "default": "ta",
            "available": ["ta", "en", "parallel"],
            "rule": "language switching is presentation only; Tamil and English stored text must not be rewritten",
        },
        "search": {
            "recommended_fields": [
                "titles.tamil",
                "titles.english",
                "film.title_ta",
                "sections.lines.tamil",
                "sections.lines.english",
            ],
            "normalization_rule": "search normalization may create indexes but must not alter stored source or translation text",
        },
        "provenance_policy": {
            "show_source_pages": True,
            "preserve_source_paths": True,
            "attribution_rule": "anthology-attributed is not original-film primary-source verification",
        },
        "films": film_groups,
    }

    # Verify the payload is a lossless repackaging of the reader lines.
    payload_songs = [song for film in payload["films"] for song in film["songs"]]
    ensure([s["song_id"] for s in payload_songs] == [s["song_id"] for s in integration_songs], "payload song order drift")
    payload_lines = [line for song in payload_songs for section in song["sections"] for line in section["lines"]]
    reader_lines = [line for song in reader_songs for section in song["sections"] for line in section["lines"]]
    ensure(len(payload_lines) == len(reader_lines) == EXPECTED_LINES, "payload line coverage drift")
    for p_line, r_line in zip(payload_lines, reader_lines):
        ensure(p_line["id"] == r_line["id"], f"payload line ID drift at {p_line.get('id')}")
        ensure(p_line["tamil"] == r_line["source_tamil"], f"payload Tamil text drift at {p_line['id']}")
        ensure(p_line["english"] == r_line["english"], f"payload English text drift at {p_line['id']}")

    qa = {
        "status": "PASS",
        "film_groups": EXPECTED_FILMS,
        "songs": EXPECTED_SONGS,
        "line_cues": EXPECTED_LINES,
        "cross_page_songs": EXPECTED_CROSS_PAGE,
        "pilot_verified": 3,
        "verified": 51,
        "anthology_attributed": 54,
        "duplicate_song_ids": 0,
        "duplicate_translation_ids": 0,
        "duplicate_line_ids": 0,
        "song_order_drift": 0,
        "film_grouping_coverage_drift": 0,
        "source_page_drift": 0,
        "Tamil_text_drift": 0,
        "English_text_drift": 0,
        "status_drift": 0,
        "attribution_drift": 0,
        "warnings": 0,
        "errors": 0,
    }
    return payload, qa


def render_qa(qa: dict[str, Any]) -> str:
    return f"""# கலைஞர் திரை இசைப் பாடல்கள் — Reading Room Integration Payload QA

Status: **PASS**

This report validates the structured payload prepared for downstream Kalaignar Digital Library / Reading Room integration. It is a deterministic repackaging of the complete-verified reader/song records; it does not modify the Tamil or Kalaignar-language English.

## PASS results

| Check | Result |
|---|---:|
| Film groups | **{qa['film_groups']} / 23** |
| Songs | **{qa['songs']} / 54** |
| Tamil/English line-cues | **{qa['line_cues']} / 1,105** |
| Cross-page songs | **{qa['cross_page_songs']} / 8** |
| Pilot-verified items | **{qa['pilot_verified']}** |
| Verified items | **{qa['verified']}** |
| `anthology-attributed` items | **{qa['anthology_attributed']} / 54** |
| Duplicate song IDs | **0** |
| Duplicate translation IDs | **0** |
| Duplicate line IDs | **0** |
| Anthology-order drift | **0** |
| Film-group coverage/order drift | **0** |
| Source-page drift | **0** |
| Tamil text drift | **0** |
| English text drift | **0** |
| Status drift | **0** |
| Attribution drift | **0** |
| Warnings | **0** |
| Errors | **0** |

## Integration contract

The payload groups songs by the **23 film sections in first-appearance order**, while retaining the canonical anthology song order `001–054`. Each song carries Tamil and English titles, film/year metadata as printed in the anthology inventory, music/voice credits where printed, exact source PDF page arrays, immutable source paths, item status, attribution state, source/English section labels, and all paired Tamil/English lines.

Tamil/English switching, collection labels, a suggested slug and search fields are explicitly presentation metadata. They do not become source authority.

## Kalaignar-language safeguard

All **1,105 English lines/cues** are byte-for-text equal to the complete-verified `reader-edition.json` values. No wording is smoothed, modernized, paraphrased or replaced during Reading Room payload generation.

## Site-application boundary

**The payload is complete-verified; the public Reading Room implementation itself is not modified by this repository build.** Applying the payload to a separate implementation repository requires that repository to be explicitly in scope. This prevents a downstream UI change from silently becoming an archival/source change.

## Gate disposition

**Reading Room integration payload QA: PASS.**

The cinema-works repository is ready to hand this payload to the Reading Room implementation without reopening the verified Tamil, English translation or reader/export layers.
"""


def manifest(inputs: list[Path], outputs: list[Path]) -> dict[str, Any]:
    return {
        "work_id": "kalaignar-thirai-isai-paadalgal",
        "integration": "reading-room",
        "build_version": BUILD_VERSION,
        "status": "payload-complete-verified",
        "site_application_status": "not-applied",
        "deterministic": True,
        "inputs": [
            {"path": p.relative_to(ROOT).as_posix(), "sha256": sha256_path(p), "bytes": p.stat().st_size}
            for p in inputs
        ],
        "outputs": [
            {"path": p.relative_to(ROOT).as_posix(), "sha256": sha256_path(p), "bytes": p.stat().st_size}
            for p in outputs
        ],
        "manifest_note": "manifest.json intentionally does not hash itself to avoid a circular self-hash",
    }


def main() -> int:
    payload, qa = build_payload()
    OUT.mkdir(parents=True, exist_ok=True)
    payload_path = OUT / "reading-room.json"
    qa_path = OUT / "QA_REPORT.md"
    manifest_path = OUT / "manifest.json"

    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    qa_path.write_text(render_qa(qa), encoding="utf-8")

    # Re-open generated JSON and assert stable top-level checkpoint.
    reloaded = load_json(payload_path)
    ensure(reloaded.get("integration_status") == "payload-complete-verified", "generated payload status drift")
    ensure(reloaded.get("work", {}).get("counts", {}).get("songs") == EXPECTED_SONGS, "generated payload song count drift")
    ensure(len(reloaded.get("films", [])) == EXPECTED_FILMS, "generated payload film count drift")

    input_paths = [
        READER_PATH,
        READER_MANIFEST_PATH,
        SONG_INDEX_PATH,
        PAGE_MAP_PATH,
        TRANSLATION_INDEX_PATH,
        Path(__file__).resolve(),
    ]
    output_paths = [payload_path, qa_path]
    manifest_path.write_text(json.dumps(manifest(input_paths, output_paths), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("KALAIGNAR SONG ANTHOLOGY READING ROOM PAYLOAD")
    print("status= PASS")
    print("film_groups=", EXPECTED_FILMS)
    print("songs=", EXPECTED_SONGS)
    print("line_cues=", EXPECTED_LINES)
    print("site_application_status= not-applied")
    print("warnings= 0")
    print("errors= 0")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except QAError as exc:
        print("KALAIGNAR SONG ANTHOLOGY READING ROOM PAYLOAD", file=sys.stderr)
        print("status= FAIL", file=sys.stderr)
        print(f"error= {exc}", file=sys.stderr)
        raise SystemExit(1)
