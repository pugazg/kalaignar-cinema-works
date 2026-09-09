#!/usr/bin/env python3
"""Synchronize Naam reader/Reading Room Phase 10 closure across active status surfaces."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
W = ROOT / "works" / "naam"
READER = W / "editions" / "en"
RR = W / "integrations" / "reading-room"

OLD_NEXT = (
    "Begin Phase 10 whole-work reader/export generation from the complete-verified Tamil and English structured layers. "
    "Build deterministic Markdown, standalone HTML, machine-readable JSON, reader QA, and an integrity manifest; verify all 45 source scenes appear exactly once in canonical order and all 797 verified English units render exactly once; preserve all 590 immutable dialogue links, the seven retained performance records, the distinct scene-34 chant, written text, source-unlabelled speech, exact cross-page provenance, and source-page linkage; prohibit duplicate source-span ownership, synthetic scene-end prose, placeholder/editorial leakage, or upstream source-layer mutation. "
    "After reader QA passes, prepare structured data for Kalaignar Digital Library / Reading Room integration. Do not create a PDF, EPUB, or other publication package unless separately requested."
)
NEW_NEXT = (
    "No required repository-internal processing remains for நாம். Reader/export and the source-linked Reading Room payload are complete-verified with QA PASS. "
    "Keep Tamil, scene, dialogue, character, song-source and English records closed. Apply `works/naam/integrations/reading-room/reading-room.json` in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository is explicitly authorized for modification; before applying it, fetch that repository's live state and use a fail-closed importer pinned to this verified payload/manifest. Site application remains not-applied here. "
    "Do not create a PDF, EPUB or other publication package unless separately requested."
)
HISTORICAL_TRANSLATE_PREFIX = "**Historical next recorded at this earlier English checkpoint:**"


def rt(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def wt(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def rj(p: Path):
    return json.loads(rt(p))


def wj(p: Path, d) -> None:
    wt(p, json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def replace_nexts(s: str) -> str:
    s = s.replace(OLD_NEXT, NEW_NEXT)
    # Old English batch sections remain useful history, but their Next labels must not look active.
    s = re.sub(
        r"\*\*Next:\*\* (Translate and verify source-numbered scenes 36–45[^\n]*)",
        HISTORICAL_TRANSLATE_PREFIX + r" \1",
        s,
    )
    return s


def upsert_marker(path: Path, marker: str, block: str) -> None:
    s = replace_nexts(rt(path))
    if marker in s:
        pattern = re.escape(marker) + r".*?(?=\n<!-- |\Z)"
        s, n = re.subn(pattern, marker + "\n" + block.rstrip() + "\n", s, count=1, flags=re.S)
        if n == 0:
            s += "\n\n" + marker + "\n" + block.rstrip() + "\n"
    else:
        s += "\n\n" + marker + "\n" + block.rstrip() + "\n"
    wt(path, s)


def yaml_replace(s: str, key: str, value: str) -> str:
    pat = rf"(?m)^(\s*){re.escape(key)}:\s*.*$"
    if re.search(pat, s):
        return re.sub(pat, lambda m: f"{m.group(1)}{key}: {value}", s, count=1)
    return s


def main() -> None:
    reader_manifest = rj(READER / "manifest.json")
    rr_manifest = rj(RR / "manifest.json")
    assert reader_manifest["status"] == "complete-verified" and reader_manifest["qa_status"] == "PASS"
    assert rr_manifest["status"] == "payload-complete-verified" and rr_manifest["qa_status"] == "PASS"
    assert rr_manifest["site_application_status"] == "not-applied"
    assert reader_manifest["translation_units"] == 797 and reader_manifest["immutable_dialogue_links"] == 590
    assert rr_manifest["english_units"] == 797 and rr_manifest["immutable_dialogue_links"] == 590
    reader_json = reader_manifest["outputs"]["reader-edition.json"]
    payload = rr_manifest["payload"]

    # Translation-layer status/index: records themselves remain immutable.
    p = W / "translations" / "index.json"
    d = rj(p)
    d["reader_export_status"] = "complete-verified"
    d["reader_export_directory"] = "../editions/en"
    d["reader_export_qa"] = "../editions/en/QA_REPORT.md"
    d["reader_export_manifest"] = "../editions/en/manifest.json"
    d["reading_room_payload_status"] = "payload-complete-verified"
    d["reading_room_payload_path"] = "../integrations/reading-room/reading-room.json"
    d["reading_room_payload_qa"] = "../integrations/reading-room/QA_REPORT.md"
    d["reading_room_site_application"] = "not-applied"
    d["next_activity"] = NEW_NEXT
    wj(p, d)

    # Work metadata.
    p = W / "metadata.yaml"
    s = rt(p)
    s = yaml_replace(s, "english_reader_export", "complete-verified")
    s = yaml_replace(s, "reader_export", "complete-verified")
    s = yaml_replace(s, "reading_room_integration", "payload-complete-verified-site-not-applied")
    insert_anchor = "  english_reader_export: complete-verified"
    additions = [
        '  english_reader_edition_directory: "editions/en"',
        "  english_reader_qa: PASS",
        "  english_reader_qa_units: 797",
        "  english_reader_qa_dialogue_links: 590",
        "  english_reader_qa_source_unlabelled_speech_units: 20",
        "  english_reader_qa_cross_page_units: 12",
        "  english_reader_qa_performance_records: 7",
        "  reading_room_payload: payload-complete-verified",
        '  reading_room_payload_path: "integrations/reading-room/reading-room.json"',
        '  reading_room_payload_qa_path: "integrations/reading-room/QA_REPORT.md"',
        '  reading_room_payload_manifest_path: "integrations/reading-room/manifest.json"',
        "  reading_room_site_application: not-applied",
    ]
    if insert_anchor in s:
        # Remove prior generated keys first so reruns remain idempotent.
        for line in additions:
            key = line.strip().split(":", 1)[0]
            s = re.sub(rf"(?m)^\s{{2}}{re.escape(key)}:.*\n?", "", s)
        s = s.replace(insert_anchor, insert_anchor + "\n" + "\n".join(additions), 1)
    s = replace_nexts(s)
    s = re.sub(r'(?m)^next_action:\s*.*$', "next_action: " + json.dumps(NEW_NEXT, ensure_ascii=False), s, count=1)
    wt(p, s)

    # Work README current status + durable closure section.
    p = W / "README.md"
    s = replace_nexts(rt(p))
    s = re.sub(
        r"- English translation: \*\*45/45 COMPLETE-VERIFIED.*?reader/export: \*\*READY-NEXT\*\*\.",
        "- English translation: **45/45 COMPLETE-VERIFIED / 797 units / whole-work QA PASS**; reader/export: **COMPLETE-VERIFIED / QA PASS**; Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS / site not-applied**.",
        s,
        count=1,
    )
    s = re.sub(r"\*\*Next:\*\* " + re.escape(NEW_NEXT), "**Next:** " + NEW_NEXT, s, count=1)
    marker = "<!-- Naam Phase 10 reader and payload closure -->"
    block = f"""## Phase 10 reader/export + Reading Room closure

- reader/export: **COMPLETE-VERIFIED / QA PASS**;
- reader forms: **Markdown / standalone HTML / machine-readable JSON**;
- source scenes rendered: **45/45 source-numbered scenes exactly once**;
- English units rendered: **797/797 exactly once**;
- immutable dialogue links: **590/590**;
- source-unlabelled speech: **20 / inferred speakers 0**;
- retained performance records: **7/7 / 138 mappings**;
- scene-34 chant: **1 / 16 mappings / not promoted to the performance inventory**;
- written-text / cross-page units: **2 / 12**;
- reader JSON: `{reader_json['sha256']}` / **{reader_json['bytes']:,} bytes**;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**;
- payload: `{payload['sha256']}` / **{payload['bytes']:,} bytes**;
- site application: **not-applied**;
- upstream Tamil / scene / dialogue / character / song-source / English-record changes: **0**.

**Next:** {NEW_NEXT}
"""
    if marker in s:
        s = re.sub(re.escape(marker) + r".*\Z", marker + "\n" + block, s, flags=re.S)
    else:
        s += "\n\n" + marker + "\n" + block
    wt(p, s)

    # Active handover: replace top checkpoint and exact next block, append closure evidence.
    p = W / "PROJECT_HANDOVER.md"
    s = replace_nexts(rt(p))
    s = re.sub(r"- reader/export: \*\*READY-NEXT\*\*; Reading Room integration: \*\*not-started\*\*\.", "- reader/export: **COMPLETE-VERIFIED / QA PASS**; Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**; site application: **not-applied**.", s, count=1)
    s = re.sub(r"## Current exact next activity\n\n> \*\*.*?\*\*\n", "## Current exact next activity\n\n> **" + NEW_NEXT + "**\n", s, count=1, flags=re.S)
    closure = f"""## Phase 10 closure evidence

- reader: `editions/en/reader-edition.md`, `.html`, `.json`;
- reader QA / manifest: `editions/en/QA_REPORT.md`, `editions/en/manifest.json` — **PASS / complete-verified**;
- reader JSON SHA-256: `{reader_json['sha256']}`;
- Reading Room payload: `integrations/reading-room/reading-room.json`;
- payload QA / manifest: `integrations/reading-room/QA_REPORT.md`, `integrations/reading-room/manifest.json` — **PASS / payload-complete-verified**;
- payload SHA-256: `{payload['sha256']}`;
- site application: **not-applied**;
- no PDF/EPUB/publication package created.

"""
    if "## Phase 10 closure evidence" in s:
        s = re.sub(r"## Phase 10 closure evidence\n.*?(?=\n## |\Z)", closure.rstrip() + "\n", s, count=1, flags=re.S)
    else:
        s = s.replace("## Source identity", closure + "## Source identity", 1)
    wt(p, s)

    # Next-chat prompt is an active startup file, so rewrite it completely.
    wt(W / "NEXT_CHAT_PROMPT.md", f"""# Next Chat Prompt — நாம்

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**

Canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 immutable records / QA PASS**; character/entity **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance **7/7 COMPLETE-VERIFIED-SOURCE-ONLY**; English **45/45 / 797 units / COMPLETE-VERIFIED / whole-work QA PASS**.

Phase 10 is **CLOSED**:

- reader/export: **COMPLETE-VERIFIED / QA PASS**;
- `editions/en/reader-edition.md`, `.html`, `.json`;
- reader JSON SHA-256 `{reader_json['sha256']}`;
- **797/797** verified English units rendered exactly once;
- **590/590** immutable dialogue links preserved;
- **20** source-unlabelled speech units / 0 inferred speakers;
- **7/7** retained performances / **138** mappings;
- scene-34 chant **1 / 16 mappings**, still outside the performance inventory;
- **2** written-text / **12** cross-page units;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**;
- payload SHA-256 `{payload['sha256']}`;
- public-site application: **not-applied**;
- no PDF or EPUB generated.

All Tamil, scene, dialogue, character, song-source and English scene-record layers remain immutable downstream authority.

## Exact next activity

> **{NEW_NEXT}**
""")

    # Repository structured-data mirror.
    p = ROOT / "data" / "works.json"
    data = rj(p)
    item = next(x for x in data if x.get("id") == "naam")
    sd = item.setdefault("structured_derivatives", {})
    sd.update({
        "english_translation": "complete-verified",
        "english_whole_work_reconciliation": "PASS",
        "reader_export": "complete-verified",
        "english_reader_edition_directory": "works/naam/editions/en",
        "english_reader_qa": "PASS",
        "english_reader_qa_units": 797,
        "english_reader_qa_dialogue_links": 590,
        "english_reader_qa_source_unlabelled_speech_units": 20,
        "english_reader_qa_cross_page_units": 12,
        "english_reader_qa_performance_records": 7,
        "english_reader_json_sha256": reader_json["sha256"],
        "reading_room_integration": "payload-complete-verified",
        "reading_room_payload_path": "works/naam/integrations/reading-room/reading-room.json",
        "reading_room_payload_qa_report_path": "works/naam/integrations/reading-room/QA_REPORT.md",
        "reading_room_payload_manifest_path": "works/naam/integrations/reading-room/manifest.json",
        "reading_room_payload_sha256": payload["sha256"],
        "reading_room_payload_bytes": payload["bytes"],
        "reading_room_site_application": "not-applied",
        "next_structured_derivative": None,
    })
    item["next_action"] = NEW_NEXT
    wj(p, data)

    current_block = f"""**Naam Phase 10 current:** reader/export **COMPLETE-VERIFIED / QA PASS** — 45 source-numbered scenes / 797 English units / 590 immutable dialogue links / 7 retained performances / 138 performance mappings / 1 distinct chant (16 mappings) / 12 cross-page units. Reading Room payload **PAYLOAD-COMPLETE-VERIFIED / QA PASS**, SHA-256 `{payload['sha256']}`, site application **not-applied**. No PDF/EPUB was generated. **Next:** {NEW_NEXT}
"""
    upsert_marker(ROOT / "README.md", "<!-- Naam Phase 10 current -->", current_block)
    upsert_marker(ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md", "<!-- Naam Phase 10 current -->", current_block)
    upsert_marker(ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md", "<!-- Naam Phase 10 current -->", current_block)

    print(json.dumps({
        "status": "PASS",
        "reader_export": "complete-verified",
        "reader_json_sha256": reader_json["sha256"],
        "reading_room_payload": "payload-complete-verified",
        "payload_sha256": payload["sha256"],
        "payload_bytes": payload["bytes"],
        "site_application": "not-applied",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
