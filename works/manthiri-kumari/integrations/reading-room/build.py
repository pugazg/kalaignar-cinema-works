#!/usr/bin/env python3
"""Validate the Manthiri Kumari Reading Room source-linked payload.

Run from the repository root:
    python works/manthiri-kumari/integrations/reading-room/build.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "manthiri-kumari"
HERE = WORK / "integrations" / "reading-room"
PAYLOAD_PATH = HERE / "reading-room.json"
MANIFEST_PATH = HERE / "manifest.json"
STORY_PATH = WORK / "translations" / "story-summary.json"
PERF_DIR = WORK / "translations" / "performances"
SOURCE_SHA = "a64ac0b5ff4adca75d0860d9d52c5324f93f55da3b060cecb43743d0bbc696ee"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    payload = load(PAYLOAD_PATH)
    manifest = load(MANIFEST_PATH)
    story = load(STORY_PATH)
    records = [load(PERF_DIR / f"{i:03d}.json") for i in range(1, 16)]

    assert payload["schema_version"] == 1
    assert payload["integration_status"] == "payload-complete-verified"
    assert payload["site_application_status"] == "not-applied"
    assert payload["payload_mode"] == "source-linked-composition"
    assert payload["work"]["source_sha256"] == SOURCE_SHA
    assert payload["navigation"]["primary_sections"] == ["story-summary", "performances"]
    assert payload["navigation"]["performance_order_is_source_numbering"] is False
    assert payload["navigation"]["source_numbered_scenes"] is False

    summary = payload["story_summary"]
    assert summary["record_id"] == story["source_record_id"]
    assert summary["translation_id"] == story["id"]
    assert summary["title_ta"] == story["source"]["title_ta"]
    assert summary["title_en"] == story["translation"]["english_title"]
    assert summary["pdf_pages"] == story["source"]["pdf_pages"] == [3, 4, 5]
    assert summary["logical_units"] == len(story["translation"]["sections"]) == 13
    cross_story = sum(len(s["source_pdf_pages"]) > 1 for s in story["translation"]["sections"])
    assert summary["cross_page_units"] == cross_story == 1

    pitems = payload["performances"]
    assert len(pitems) == len(records) == 15
    assert [p["source_order"] for p in pitems] == list(range(1, 16))
    assert len({p["performance_id"] for p in pitems}) == 15
    assert len({p["translation_id"] for p in pitems}) == 15

    section_count = 0
    line_count = 0
    cross_page = []
    for item, record in zip(pitems, records):
        assert item["source_order_is_printed_numbering"] is False
        assert item["performance_id"] == record["source_performance_id"]
        assert item["translation_id"] == record["id"]
        assert item["heading_ta"] == record["heading_ta"]
        assert item["heading_en"] == record["heading_en"]
        assert item["pdf_pages"] == record["source"]["pdf_pages"]
        assert item["tamil_source_path"] == record["source"]["record_path"]
        assert item["english_source_path"].endswith(f"/{record['sequence']:03d}.json")
        assert item["authorship_status"] == record["source"]["authorship_status"]
        assert item["cross_witness_status"] == record["source"]["cross_witness_status"]
        assert item["anthology_record_id"] == record["source"].get("anthology_record_id")

        sections = record["translation"]["sections"]
        assert item["sections"] == len(sections)
        lines = 0
        for section in sections:
            ta = section["source_tamil_lines"]
            en = section["english_lines"]
            assert len(ta) == len(en)
            lines += len(ta)
        assert item["line_cues"] == lines
        section_count += len(sections)
        line_count += lines
        if len(item["pdf_pages"]) > 1:
            cross_page.append(item["source_order"])

    assert section_count == 52
    assert line_count == 234
    assert cross_page == [2, 4, 6, 7, 9, 11, 13]

    counts = payload["work"]["counts"]
    assert counts["story_summary_records"] == 1
    assert counts["story_summary_units"] == 13
    assert counts["story_summary_cross_page_units"] == 1
    assert counts["performance_blocks"] == 15
    assert counts["performance_sections"] == 52
    assert counts["performance_line_cues"] == 234
    assert counts["cross_page_performance_blocks"] == 7
    assert counts["confirmed_existing_anthology_witnesses"] == 1
    assert counts["source_only_in_current_anthology"] == 14
    assert counts["item_level_lyric_authorship_verified"] == 0
    assert counts["item_level_lyric_authorship_unresolved"] == 15

    assert pitems[10]["anthology_record_id"] == "kalaignar-song-001"
    assert pitems[10]["cross_witness_status"] == "confirmed-existing-anthology-witness"
    assert pitems[12]["heading_ta"] == "பார்த்திபன்—மந்திரிகுமாரி"
    labels13 = {s["source_label"] for s in records[12]["translation"]["sections"]}
    assert labels13 == {"பார்த்திபன்", "அமுதவல்லி"}

    qa = payload["qa"]
    assert qa["source_link_targets_expected"] == 32
    assert qa["performance_mapping_mismatches"] == 0
    assert qa["synthetic_scene_ids_created"] == 0
    assert qa["canonical_tamil_changed"] is False
    assert qa["authorship_upgrades"] == 0
    assert qa["result"] == "PASS"

    raw = PAYLOAD_PATH.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert len(raw) == manifest["payload"]["bytes"]
    assert digest == manifest["payload"]["sha256"]
    assert manifest["qa"]["result"] == "PASS"
    assert manifest["site_application_status"] == "not-applied"

    print("PASS", f"payload_bytes={len(raw)}", f"payload_sha256={digest}")


if __name__ == "__main__":
    main()
