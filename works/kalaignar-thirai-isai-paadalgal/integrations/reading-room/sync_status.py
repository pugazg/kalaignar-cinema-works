#!/usr/bin/env python3
"""Synchronize repository checkpoints after Reading Room integration payload QA PASS."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "kalaignar-thirai-isai-paadalgal"
INTEGRATION = WORK / "integrations" / "reading-room"
WORK_ID = "kalaignar-thirai-isai-paadalgal"
PAYLOAD_REL = "works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/reading-room.json"
QA_REL = "works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/QA_REPORT.md"
MANIFEST_REL = "works/kalaignar-thirai-isai-paadalgal/integrations/reading-room/manifest.json"

qa_text = (INTEGRATION / "QA_REPORT.md").read_text(encoding="utf-8")
if "Status: **PASS**" not in qa_text:
    raise SystemExit("Reading Room integration payload QA is not PASS")
manifest = json.loads((INTEGRATION / "manifest.json").read_text(encoding="utf-8"))
if manifest.get("status") != "payload-complete-verified" or manifest.get("site_application_status") != "not-applied":
    raise SystemExit("Reading Room integration manifest checkpoint is not valid")
payload = json.loads((INTEGRATION / "reading-room.json").read_text(encoding="utf-8"))
if payload.get("integration_status") != "payload-complete-verified" or payload.get("site_application_status") != "not-applied":
    raise SystemExit("Reading Room payload checkpoint is not valid")
counts = payload.get("work", {}).get("counts", {})
if counts != {"films": 23, "songs": 54, "line_cues": 1105, "cross_page_songs": 8}:
    raise SystemExit(f"Reading Room payload count drift: {counts}")

output_hashes = {Path(item["path"]).name: item["sha256"] for item in manifest.get("outputs", [])}
if set(output_hashes) != {"reading-room.json", "QA_REPORT.md"}:
    raise SystemExit(f"unexpected Reading Room manifest outputs: {output_hashes}")


def replace_idempotent(path: Path, old: str, new: str) -> None:
    """Apply a targeted status swap once.

    `new` is checked first on purpose. Several of these updates are append-style,
    where `new` begins with the whole of `old` and adds a line or table row. If
    `old` were tested first it would still match inside the already-updated text
    and the addition would be appended again on every run.
    """
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old in text:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        return
    raise SystemExit(f"status synchronization text not found in {path.relative_to(ROOT)}")


GENERATED_BEGIN = "<!-- BEGIN GENERATED: reading-room-status -->"
GENERATED_END = "<!-- END GENERATED: reading-room-status -->"


def replace_section(path: Path, start: str, end: str | None, new_section: str) -> None:
    """Replace this script's generated block in `path`, idempotently.

    Synchronization must satisfy ``F(F(x)) == F(x)``: a second run has to produce
    no further diff. That requires boundaries the block does not itself reproduce,
    so the block is delimited by explicit markers.

    The earlier implementation anchored only on `start`, while every generated
    block ends by re-emitting `start` as its own trailing heading. Each run then
    found that copy inside the previously generated block and inserted the block
    again ahead of it, so the generated sections grew by one copy per run.

    A document with no markers yet is migrated once. That migration anchors on the
    generated block's own first heading when it is already present, which also
    collapses blocks duplicated by the earlier behaviour; otherwise it falls back
    to `start`. Where the caller supplies `end`, the block stays bounded by it, so
    hand-written prose outside the markers is never touched.
    """
    text = path.read_text(encoding="utf-8")
    block = f"{GENERATED_BEGIN}\n\n" + new_section.rstrip() + f"\n\n{GENERATED_END}\n\n"

    begin_pos = text.find(GENERATED_BEGIN)
    if begin_pos >= 0:
        end_pos = text.find(GENERATED_END, begin_pos)
        if end_pos < 0:
            raise SystemExit(f"unterminated generated block in {path.relative_to(ROOT)}")
        stop = end_pos + len(GENERATED_END)
        while text[stop:stop + 1] == "\n":
            stop += 1
        if text[begin_pos:stop] == block:
            return
        path.write_text(text[:begin_pos] + block + text[stop:], encoding="utf-8")
        return

    generated_head = new_section.strip().split("\n", 1)[0].strip()
    anchor = generated_head if generated_head and generated_head in text else start
    start_pos = text.find(anchor)
    if start_pos < 0:
        raise SystemExit(f"section {anchor!r} not found in {path.relative_to(ROOT)}")
    end_pos = len(text) if end is None else text.find(end, start_pos + len(anchor))
    if end_pos < 0:
        raise SystemExit(f"section end {end!r} not found in {path.relative_to(ROOT)}")
    path.write_text(text[:start_pos] + block + text[end_pos:], encoding="utf-8")


registry_path = ROOT / "data" / "works.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
entry = next((item for item in registry if item.get("id") == WORK_ID), None)
if entry is None:
    raise SystemExit(f"missing {WORK_ID} in data/works.json")
entry.update({
    "reading_room_integration": "payload-complete-verified",
    "reading_room_payload_path": PAYLOAD_REL,
    "reading_room_payload_qa": "PASS",
    "reading_room_payload_qa_report_path": QA_REL,
    "reading_room_payload_manifest_path": MANIFEST_REL,
    "reading_room_payload_film_groups": 23,
    "reading_room_payload_songs": 54,
    "reading_room_payload_line_cues": 1105,
    "reading_room_payload_cross_page_songs": 8,
    "reading_room_payload_errors": 0,
    "reading_room_payload_warnings": 0,
    "reading_room_payload_sha256": output_hashes["reading-room.json"],
    "reading_room_site_application": "not-applied",
    "next_action": "Apply the complete-verified Reading Room payload in the separate Reading Room implementation repository only when that repository is explicitly authorized for modification."
})
registry_path.write_text(json.dumps(registry, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

metadata_path = WORK / "metadata.yaml"
metadata_text = metadata_path.read_text(encoding="utf-8")
block_start = "reading_room_integration:\n"
status_start = "status:\n"
new_block = f'''reading_room_integration:
  status: payload-complete-verified
  payload_path: "integrations/reading-room/reading-room.json"
  qa_report_path: "integrations/reading-room/QA_REPORT.md"
  manifest_path: "integrations/reading-room/manifest.json"
  build_script: "integrations/reading-room/build.py"
  payload_sha256: "{output_hashes['reading-room.json']}"
  film_groups: 23
  songs: 54
  line_cues: 1105
  cross_page_songs: 8
  warnings: 0
  errors: 0
  site_application_status: not-applied
  next_action: "Apply the complete-verified payload in the separate Reading Room implementation repository only when that repository is explicitly authorized for modification."

'''
if block_start in metadata_text:
    b = metadata_text.find(block_start)
    e = metadata_text.find(status_start, b)
    if e < 0:
        raise SystemExit("metadata status section not found after reading_room_integration")
    metadata_text = metadata_text[:b] + new_block + metadata_text[e:]
else:
    s = metadata_text.find(status_start)
    if s < 0:
        raise SystemExit("metadata status section not found")
    metadata_text = metadata_text[:s] + new_block + metadata_text[s:]
if "  reading_room_payload:" in metadata_text:
    metadata_text = metadata_text.replace("  reading_room_payload: not-started", "  reading_room_payload: complete-verified")
else:
    marker = "  reader_export: complete-verified\n"
    if marker not in metadata_text:
        raise SystemExit("metadata reader_export completion marker not found")
    metadata_text = metadata_text.replace(marker, marker + "  reading_room_payload: complete-verified\n", 1)
metadata_path.write_text(metadata_text, encoding="utf-8")

progress = WORK / "PROGRESS.md"
replace_section(progress, "## Next activity", None, f'''## Reading Room integration payload

A deterministic, source-linked Reading Room payload has been prepared under `integrations/reading-room/`.

QA status: **PASS**.

- film groups: **23/23**;
- songs: **54/54**;
- paired Tamil/English lines-cues: **1,105/1,105**;
- cross-page songs: **8/8**;
- item status history: **3 pilot-verified + 51 verified**;
- attribution: **54/54 anthology-attributed**;
- Tamil text drift: **0**;
- English text drift: **0**;
- warnings/errors: **0/0**;
- payload SHA-256: `{output_hashes['reading-room.json']}`.

The payload groups songs by the anthology's 23 film sections while preserving canonical song order `001–054`. It carries source pages, exact archival IDs/paths, printed film/year/music/voice metadata where available, section labels and every verified Tamil/English line.

The public-site implementation itself remains **not applied**; this repository has prepared and verified the downstream contract only.

## Next activity

Apply the complete-verified payload in the separate Kalaignar Digital Library / Reading Room implementation repository **only when that repository is explicitly authorized for modification**. No Tamil, translation, reader/export or integration-payload text should be rewritten for UI convenience.''')

audit = WORK / "AUDIT.md"
replace_section(audit, "## Next activity", None, f'''## Reading Room integration payload gate

**PASS — payload complete-verified; site application not applied.**

`integrations/reading-room/QA_REPORT.md` independently verifies **23 film groups**, **54 songs**, **1,105 paired Tamil/English lines-cues**, all **8 cross-page songs**, the **3 pilot-verified / 51 verified** status history, and **54/54 anthology-attributed** records with zero source-page, Tamil-text, English-text, status or attribution drift.

The generated payload SHA-256 is `{output_hashes['reading-room.json']}`. Its manifest hashes the complete-verified reader payload, reader manifest, song index, page map, translation index and integration builder.

The downstream public-site repository has not been modified by this gate.

## Next activity

Actual Reading Room site application is the only remaining downstream action. It requires explicit authorization for the separate implementation repository. The archive and integration payload must remain immutable inputs to that UI work.''')

work_readme = WORK / "README.md"
replace_section(work_readme, "## Next activity", None, f'''## Reading Room integration payload

A verified structured payload is now available at `integrations/reading-room/reading-room.json`, with QA in `integrations/reading-room/QA_REPORT.md` and deterministic hashes in `integrations/reading-room/manifest.json`.

It contains **23 film groups / 54 songs / 1,105 paired Tamil-English lines-cues / 8 cross-page songs**, retaining exact archive IDs, source pages, item status history, printed credits where available and `anthology-attributed` state. QA reports **0 warnings / 0 errors / 0 Tamil or English text drift**.

The payload is intended for structured-data consumption by the Kalaignar Digital Library / Reading Room. Search/navigation/language-switching are presentation concerns and must not rewrite stored Tamil or the source-faithful Kalaignar-language English.

## Next activity

The public Reading Room implementation itself remains `not-applied`. Apply this payload in the separate implementation repository only when that repository is explicitly authorized for modification.''')

handover = WORK / "PROJECT_HANDOVER.md"
replace_section(handover, "## Exact next activity", "## Repository boundary", f'''## Reading Room integration payload checkpoint

The downstream structured payload is **complete-verified** under `integrations/reading-room/`:

- `reading-room.json` — 23 film groups, 54 songs, 1,105 paired lines-cues;
- `QA_REPORT.md` — **PASS**;
- `manifest.json` — deterministic input/output hashes;
- `build.py` — deterministic payload builder;
- `README.md` — integration contract and authority rules.

Payload SHA-256: `{output_hashes['reading-room.json']}`.

QA confirms zero song/translation/line ID duplication, zero anthology-order or film-group coverage drift, zero source-page drift, zero Tamil or English text drift, zero status/attribution drift, and **0 warnings / 0 errors**.

The payload uses film-first navigation (23 anthology film sections) with anthology-song secondary navigation, preserves exact source IDs/page provenance, and keeps `anthology-attributed` distinct from original-film primary-source verification.

**Site application status remains `not-applied`.** No separate Reading Room implementation repository has been modified by this project checkpoint.

## Exact next activity

Apply the verified `integrations/reading-room/reading-room.json` payload in the separate Kalaignar Digital Library / Reading Room implementation repository only after that repository is explicitly authorized for modification. Preserve the source-faithful Tamil/English strings exactly; UI routing, cards, filters, search indexes and language switching remain presentation metadata.''')

root_readme = ROOT / "README.md"
replace_idempotent(
    root_readme,
    "- English reader/export: **complete-verified, QA PASS** — 54/54 songs, 1,105/1,105 English lines-cues, 8 cross-page records, deterministic Markdown/HTML/JSON + manifest;",
    "- English reader/export: **complete-verified, QA PASS** — 54/54 songs, 1,105/1,105 English lines-cues, 8 cross-page records, deterministic Markdown/HTML/JSON + manifest;\n- Reading Room integration payload: **complete-verified, QA PASS** — 23 film groups / 54 songs / 1,105 paired lines-cues; site application not applied;"
)
replace_idempotent(
    root_readme,
    "**Next:** repository-internal anthology work is complete; downstream Kalaignar Digital Library / Reading Room integration may proceed from the verified reader/export package.",
    "**Next:** apply the verified Reading Room payload in the separate implementation repository only when that repository is explicitly authorized for modification."
)

status_audit = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
replace_idempotent(
    status_audit,
    "| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS — 54 songs / 1,105 lines-cues |",
    "| English reader/export | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS | complete-verified, QA PASS — 54 songs / 1,105 lines-cues |\n| Reading Room payload | downstream | downstream | ready | complete-verified, QA PASS — 23 film groups / 54 songs; site not applied |"
)
replace_idempotent(
    status_audit,
    "The anthology English reader/export is **complete-verified with QA PASS**: 54/54 songs, 1,105/1,105 English lines-cues, all eight cross-page records, deterministic Markdown/HTML/JSON and an integrity manifest, with zero warnings/errors or text drift. No required repository-internal anthology activity remains; downstream Reading Room integration is ready.",
    "The anthology English reader/export is **complete-verified with QA PASS**. A deterministic Reading Room payload is also **complete-verified with QA PASS** at 23 film groups / 54 songs / 1,105 paired Tamil-English lines-cues / 8 cross-page songs, with zero warnings/errors or text drift. The separate public-site implementation remains not applied and requires explicit cross-repository authorization."
)

print("synchronized Reading Room integration payload checkpoint")
