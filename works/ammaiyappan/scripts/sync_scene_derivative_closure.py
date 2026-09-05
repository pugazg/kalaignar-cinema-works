#!/usr/bin/env python3
"""Synchronize repository mirrors after Ammayappan scene derivatives close."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "works" / "ammaiyappan"
SCENE_INDEX = WORK / "scenes" / "index.json"
SCENE_QA = WORK / "notes" / "scene-boundary-ownership-qa.md"
SCENE_COMMIT = "6a764137616879d08f5a1ff14431caafa87b11eb"
POST_FIDELITY_CORRECTION_COMMIT = "a38601a0961e8e3035a9aa1c7b6fa3c73c419ed9"


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_section(text: str, start: str, end: str | None, new: str) -> str:
    if start not in text:
        raise SystemExit(f"missing section start: {start}")
    before, rest = text.split(start, 1)
    if end is None:
        return before + new
    if end not in rest:
        raise SystemExit(f"missing section end: {end}")
    _, after = rest.split(end, 1)
    return before + new + end + after


def preflight() -> tuple[dict, int]:
    idx = json.loads(SCENE_INDEX.read_text(encoding="utf-8"))
    qa = SCENE_QA.read_text(encoding="utf-8")
    if idx.get("status") != "complete-verified" or idx.get("archive_scene_count") != 63:
        raise SystemExit("scene index is not 63/63 complete-verified")
    if idx.get("canonical_derivative_body_sha256") != idx.get("joined_scene_spans_sha256"):
        raise SystemExit("scene ownership hashes differ")
    if "Status: **PASS**" not in qa or "gaps between consecutive derivative spans: **0**" not in qa or "overlaps between consecutive derivative spans: **0**" not in qa:
        raise SystemExit("scene boundary QA is not PASS")
    if len(list((WORK / "scenes").glob("scene-*.md"))) != 63:
        raise SystemExit("scene file count is not 63")
    distinct = len({r["heading"] for r in idx["scene_records"]})
    return idx, distinct


def sync_metadata(distinct: int) -> None:
    p = WORK / "metadata.yaml"
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"  structural_heading_occurrences: \d+", "  structural_heading_occurrences: 63", t, count=1)
    t = re.sub(r"  distinct_structural_heading_forms: \d+", f"  distinct_structural_heading_forms: {distinct}", t, count=1)
    if "  scene_segmentation_preflight_path:" not in t:
        t = t.replace('  transition_heading_audit_path: "notes/scene-heading-audit.md"\n', '  transition_heading_audit_path: "notes/scene-heading-audit.md"\n  scene_segmentation_preflight_path: "notes/scene-segmentation-preflight.json"\n  scene_boundary_ownership_qa_path: "notes/scene-boundary-ownership-qa.md"\n')
    t = re.sub(r"  next_action: \"Begin scene-text derivatives.*?\"", '  next_action: "Begin dialogue indexing from the 63/63 verified scene-text derivatives; preserve exact speaker labels and scene/page provenance."', t, count=1)

    # Repair the remaining stale canonical-audit fields left by an older mirror block.
    t = re.sub(r"fidelity_audit:\n  status: .*?\n  canonical_range_audit_complete: true\n  audited_pages: \d+\n  verified_pages: \d+\n  review_pages: \d+\n  unresolved_source_readings: \d+", "fidelity_audit:\n  status: complete-pass\n  canonical_range_audit_complete: true\n  audited_pages: 105\n  verified_pages: 105\n  review_pages: 0\n  unresolved_source_readings: 0", t, count=1)
    t = re.sub(r"final_tamil_verification:\n(.*?)  status: .*?\n", lambda m: "final_tamil_verification:\n" + m.group(1) + "  status: complete-verified\n", t, count=1, flags=re.S)
    if "  post_fidelity_correction_commit:" not in t:
        t = t.replace("  status: complete-verified\n\nstructured_derivatives:", f"  status: complete-verified\n  post_fidelity_correction_commit: \"{POST_FIDELITY_CORRECTION_COMMIT}\"\n\nstructured_derivatives:", 1)

    t = re.sub(
        r"structured_derivatives:\n(?:  .*\n)+?\nstatus:",
        "structured_derivatives:\n"
        "  scene_index: complete-verified-63-of-63\n"
        "  scene_text_derivatives: complete-verified-63-of-63\n"
        "  scene_index_path: \"scenes/index.json\"\n"
        "  scene_boundary_ownership_qa_path: \"notes/scene-boundary-ownership-qa.md\"\n"
        f"  scene_derivative_commit: \"{SCENE_COMMIT}\"\n"
        "  dialogue_index: ready\n"
        "  character_index: blocked-pending-dialogue-index\n"
        "  song_authorship_mapping: not-started\n"
        "  english_translation: blocked\n"
        "  reader_export: blocked\n"
        "  reading_room_integration: blocked\n\n"
        "status:",
        t,
        count=1,
    )
    t = re.sub(r"  scene_derivatives: .*", "  scene_derivatives: complete-verified-63-of-63", t, count=1)
    t = re.sub(r"  dialogue_index: .*", "  dialogue_index: ready", t, count=1)
    t = re.sub(r"next_action: \".*?\"\s*$", 'next_action: "Begin dialogue indexing from the 63/63 verified scene-text derivatives; preserve exact source speaker labels, archive scene IDs and page provenance. Do not normalize character names yet."\n', t)
    if "scene_text_derivatives: complete-verified-63-of-63" not in t or "dialogue_index: ready" not in t:
        raise SystemExit("metadata scene closure synchronization failed")
    write(p, t)


def sync_index() -> None:
    p = WORK / "transcription" / "index.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d["post_fidelity_correction_commit"] = POST_FIDELITY_CORRECTION_COMMIT
    d["structured_derivatives"] = {
        "scene_text_derivatives": "complete-verified-63-of-63",
        "scene_index_path": "../scenes/index.json",
        "scene_boundary_ownership_qa_path": "../notes/scene-boundary-ownership-qa.md",
        "scene_derivative_commit": SCENE_COMMIT,
        "dialogue_index": "ready",
        "character_index": "blocked-pending-dialogue-index",
    }
    d["next_action"] = "Begin dialogue indexing from the 63/63 verified scene-text derivatives; preserve exact speaker labels, archive scene IDs and page provenance."
    write(p, json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def sync_work_readme() -> None:
    p = WORK / "README.md"
    t = p.read_text(encoding="utf-8")
    start = "## Current status"
    section = f"""## Current status

| Layer | Status |
|---|---|
| Source intake | complete |
| Whole-scan inspection | complete — 111/111 |
| Structural mapping | verified |
| Canonical Tamil | **complete-verified — 105/105 dual gate** |
| Visual fidelity | **105/105 PASS** |
| Historical Tamil glyph audit | **105/105 PASS** |
| Open canonical uncertainty markers | **0** |
| Scene segmentation preflight | **PASS — 63 boundaries** |
| Scene-text derivatives | **complete-verified — 63/63** |
| Boundary-ownership QA | **PASS — 0 gaps / 0 overlaps / 105 pages represented** |
| Dialogue index | **READY — next phase** |
| Character index | blocked pending dialogue-index closure |
| Song/performance authorship gate | not-started |
| English translation / reader | blocked by derivative gate order |

Late source correction before scene generation: PDF 10 heading `மடாலயம்` → **`மாடம்`**, direct-scan verified and recorded in `notes/post-fidelity-corrections.md`; no derivative regeneration was needed because scene files did not yet exist. Post-fidelity correction commit: `{POST_FIDELITY_CORRECTION_COMMIT}`.

## Exact next activity

**Begin dialogue indexing from `scenes/index.json` and the 63 verified scene files.** Preserve each source speaker label exactly as printed, record archive scene ID + PDF provenance for each speech turn, and keep character-name normalization/alias resolution for the later character-index phase.
"""
    write(p, replace_section(t, start, None, section))


def sync_handover() -> None:
    p = WORK / "PROJECT_HANDOVER.md"
    t = p.read_text(encoding="utf-8")
    marker = "## Dual verification gate — CLOSED"
    section = f"""## Canonical Tamil and scene-text derivatives — CLOSED

Canonical Tamil:

- visual fidelity: **105/105 PASS**;
- historical glyph audit: **105/105 PASS**;
- final dual-gate Tamil: **105/105 complete-verified**;
- unresolved canonical markers: **0**;
- post-fidelity direct-scan correction: PDF 10 heading `மாடம்`, commit `{POST_FIDELITY_CORRECTION_COMMIT}`.

Scene layer:

- segmentation preflight: **PASS — 63 source-visible canonical boundaries**;
- earlier intake ledger: **58/58 reconciled**;
- canonical additions beyond intake: **5**;
- archive-only scene files: **63/63 complete-verified**;
- source scene numbers invented: **0**;
- boundary ownership QA: **PASS — 0 gaps, 0 overlaps**;
- canonical page representation: **105/105 — PDF 5–109**;
- scene derivative commit: `{SCENE_COMMIT}`.

## Phase gates

- source/canonical Tamil gates: **closed**;
- scene-text derivatives: **closed-verified**;
- dialogue index: **READY — next phase**;
- character index: blocked pending dialogue-index closure;
- song/performance authorship gate: not-started;
- English / reader: blocked by derivative gate order.

## Exact next activity

> **Build the dialogue index from the 63 verified scene-text derivatives. Preserve the exact printed speaker label for every dialogue turn, attach archive scene ID and source PDF provenance, do not normalize aliases/character identities in this phase, and run dialogue coverage/ownership QA before opening character indexing.**
"""
    write(p, replace_section(t, marker, None, section))


def sync_registry() -> None:
    p = ROOT / "data" / "works.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    w = next(x for x in d if x.get("id") == "ammaiyappan")
    w.update({
        "structural_heading_occurrences": 63,
        "scene_segmentation_preflight": "pass-63-boundaries",
        "scene_text_derivatives": "complete-verified-63-of-63",
        "scene_count": 63,
        "scene_boundary_ownership_qa": "pass-zero-gaps-zero-overlaps",
        "scene_derivative_commit": SCENE_COMMIT,
        "post_fidelity_correction_commit": POST_FIDELITY_CORRECTION_COMMIT,
        "dialogue_index": "ready",
        "character_index": "blocked-pending-dialogue-index",
        "next_action": "Begin dialogue indexing from the 63 verified scene derivatives; preserve exact source speaker labels and scene/PDF provenance."
    })
    write(p, json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def sync_root_readme() -> None:
    p = ROOT / "README.md"
    t = p.read_text(encoding="utf-8")
    start, end = "## அம்மையப்பன் status", "## கலைஞர் திரை இசைப் பாடல்கள் status"
    section = f"""## அம்மையப்பன் status

`TVA_BOK_0064230_அம்மையப்பன்.pdf` now has **closed canonical Tamil and closed scene-text derivatives**.

- canonical Tamil: **105/105 dual-gate complete-verified**;
- visual fidelity / historical-glyph audit: **105/105 / 105/105 PASS**;
- unresolved canonical markers: **0**;
- late PDF 10 heading correction: **`மாடம்`**, commit `{POST_FIDELITY_CORRECTION_COMMIT}`;
- canonical source-visible scene boundaries: **63**;
- archive-only scene derivatives: **63/63 complete-verified**;
- boundary ownership: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- scene derivative commit: `{SCENE_COMMIT}`;
- dialogue index: **READY**;
- character index: blocked pending dialogue index;
- English / reader: blocked by derivative gate order.

**Next:** build the dialogue index from the 63 verified scene files, preserving exact source speaker labels and page provenance.

"""
    write(p, replace_section(t, start, end, section))


def sync_master_handover() -> None:
    p = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    t = p.read_text(encoding="utf-8")
    marker = "## 16. Ammayappan active checkpoint"
    section = f"""## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- canonical Tamil: **105/105 dual-gate complete-verified**;
- unresolved canonical markers / review pages: **0 / 0**;
- post-fidelity direct-scan correction: PDF 10 `மாடம்`, commit `{POST_FIDELITY_CORRECTION_COMMIT}`;
- scene segmentation preflight: **PASS — 63 boundaries**;
- scene-text derivatives: **63/63 complete-verified**;
- source-numbered scenes invented: **0**;
- boundary ownership QA: **PASS — 0 gaps / 0 overlaps / 105 pages represented**;
- scene derivative commit: `{SCENE_COMMIT}`;
- dialogue index: **READY — next phase**;
- character index: blocked pending dialogue closure;
- song/performance authorship: not-started;
- English / reader: blocked by derivative gate order.

**Exact next activity:** build the dialogue index from `works/ammaiyappan/scenes/`, preserving exact source speaker labels plus scene/PDF provenance. Do not normalize character aliases in the dialogue phase. Run dialogue coverage QA before character indexing.
"""
    write(p, replace_section(t, marker, None, section))


def sync_status_audit() -> None:
    p = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    t = p.read_text(encoding="utf-8")
    lines = t.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| Ammayappan |"):
            lines[i] = "| Ammayappan | canonical Tamil **105/105 complete-verified** | scenes **63/63 complete-verified; boundary QA PASS** | dialogue READY | character blocked |"
            break
    t = "\n".join(lines) + "\n"
    start = "## Ammayappan final dual-gate Tamil closure"
    end = "## Manthiri Kumari reconciliation checkpoint"
    section = f"""## Ammayappan canonical + scene derivative closure

- canonical Tamil: **105/105 dual-gate complete-verified**;
- PDF 10 post-fidelity correction: `மாடம்` — commit `{POST_FIDELITY_CORRECTION_COMMIT}`;
- canonical boundary inventory: **63 source-visible headings**;
- scene derivatives: **63/63 complete-verified**;
- boundary ownership QA: **PASS — 0 gaps / 0 overlaps**;
- canonical PDF representation: **105/105 — PDF 5–109**;
- scene derivative commit: `{SCENE_COMMIT}`;
- next gate: **dialogue index READY**.

Repository-wide scene-closure status is **PASS** when this section, work-local mirrors, root README and `data/works.json` agree on 63/63 scenes and dialogue READY.

"""
    write(p, replace_section(t, start, end, section))


def main() -> None:
    _, distinct = preflight()
    sync_metadata(distinct)
    sync_index()
    sync_work_readme()
    sync_handover()
    sync_registry()
    sync_root_readme()
    sync_master_handover()
    sync_status_audit()
    print(json.dumps({"status":"PASS","scene_derivatives":"63/63","dialogue_index":"ready","distinct_heading_forms":distinct}, ensure_ascii=False))


if __name__ == "__main__":
    main()
