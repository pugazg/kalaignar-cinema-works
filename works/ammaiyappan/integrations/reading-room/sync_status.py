#!/usr/bin/env python3
"""Synchronize Ammayappan mirrors after the Reading Room payload passes QA.

The payload/manifest are already produced by build.py. This script only advances
current-status mirrors; it never edits frozen Tamil, scene, dialogue, character or
song evidence.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "ammaiyappan"
INTEGRATION = WORK / "integrations" / "reading-room"
MANIFEST = INTEGRATION / "manifest.json"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
if manifest.get("status") != "PASS" or manifest.get("site_application_status") != "not-applied":
    raise SystemExit("Refusing sync: Reading Room manifest is not PASS/not-applied")
checkpoint = manifest.get("checkpoint", {})
expected = {
    "screenplay_scenes": 63,
    "tamil_scene_texts": 63,
    "english_units": 1210,
    "dialogue_source_links": 1025,
    "cross_page_units": 28,
    "occurrence_identities": 5,
    "occurrence_source_span_links": 7,
}
for key, value in expected.items():
    if checkpoint.get(key) != value:
        raise SystemExit(f"Refusing sync: checkpoint {key}={checkpoint.get(key)!r} != {value}")

output = manifest.get("output", {})
payload_sha = output.get("sha256")
payload_bytes = output.get("bytes")
if not isinstance(payload_sha, str) or len(payload_sha) != 64 or not isinstance(payload_bytes, int):
    raise SystemExit("Refusing sync: payload output metadata missing")

NEXT_EXTERNAL = (
    "No required Ammayappan repository-internal production work remains. "
    "Apply the complete-verified Reading Room payload in the separate implementation "
    "repository only when explicitly authorized; site application is not applied."
)
changed: list[str] = []


def write_if_changed(path: Path, new_text: str) -> None:
    old_text = path.read_text(encoding="utf-8")
    if old_text != new_text:
        path.write_text(new_text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def must_replace(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise SystemExit(f"Could not locate {label}")
    return text.replace(old, new, 1)


# ---------------------------------------------------------------------------
# Translation index (machine-readable current status)
# ---------------------------------------------------------------------------
index_path = WORK / "translations" / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
index.update(
    {
        "reading_room_payload": "complete-verified",
        "reading_room_payload_directory": "works/ammaiyappan/integrations/reading-room",
        "reading_room_payload_path": "works/ammaiyappan/integrations/reading-room/reading-room.json",
        "reading_room_payload_qa_report": "works/ammaiyappan/integrations/reading-room/QA_REPORT.md",
        "reading_room_payload_manifest": "works/ammaiyappan/integrations/reading-room/manifest.json",
        "reading_room_payload_sha256": payload_sha,
        "reading_room_payload_bytes": payload_bytes,
        "reading_room_payload_scenes": 63,
        "reading_room_payload_tamil_scene_texts": 63,
        "reading_room_payload_english_units": 1210,
        "reading_room_payload_dialogue_source_links": 1025,
        "reading_room_payload_cross_page_units": 28,
        "reading_room_payload_occurrence_identities": 5,
        "reading_room_payload_occurrence_source_span_links": 7,
        "reading_room_payload_qa_status": "PASS",
        "reading_room_site_application_status": "not-applied",
        "next_activity": NEXT_EXTERNAL,
    }
)
write_if_changed(index_path, json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n")


# ---------------------------------------------------------------------------
# metadata.yaml
# ---------------------------------------------------------------------------
metadata_path = WORK / "metadata.yaml"
metadata = metadata_path.read_text(encoding="utf-8")
metadata = re.sub(
    r"^  reading_room_integration: (?:ready-after-reader-export-qa|payload-complete-verified)$",
    "  reading_room_integration: payload-complete-verified",
    metadata,
    flags=re.M,
)
if "  reading_room_payload_path:" not in metadata:
    marker = "  reading_room_integration: payload-complete-verified\n\nstatus:"
    detail = f'''  reading_room_integration: payload-complete-verified
  reading_room_payload_path: "integrations/reading-room/reading-room.json"
  reading_room_payload_qa_report_path: "integrations/reading-room/QA_REPORT.md"
  reading_room_payload_manifest_path: "integrations/reading-room/manifest.json"
  reading_room_payload_sha256: "{payload_sha}"
  reading_room_payload_bytes: {payload_bytes}
  reading_room_payload_scenes: 63
  reading_room_payload_tamil_scene_texts: 63
  reading_room_payload_english_units: 1210
  reading_room_payload_dialogue_source_links: 1025
  reading_room_payload_cross_page_units: 28
  reading_room_payload_occurrence_identities: 5
  reading_room_payload_occurrence_source_span_links: 7
  reading_room_payload_qa_status: PASS
  reading_room_site_application_status: not-applied

status:'''
    metadata = must_replace(metadata, marker, detail, "metadata integration detail insertion point")
metadata = re.sub(r'^next_action: ".*"$', f'next_action: "{NEXT_EXTERNAL}"', metadata, flags=re.M)
write_if_changed(metadata_path, metadata)


# ---------------------------------------------------------------------------
# Work README
# ---------------------------------------------------------------------------
work_readme_path = WORK / "README.md"
work_readme = work_readme_path.read_text(encoding="utf-8")
payload_section = f'''## Reading Room payload — PASS

The deterministic source-linked Reading Room payload is **complete-verified** under `integrations/reading-room/`. It carries **63/63 Tamil scene texts**, all **1,210** verified English units, **1,025/1,025** dialogue/source-role links, all **28** cross-page units, and all **5 occurrence identities / 7 intentional source-span links**. Exact Tamil speaker-label origins are retained: **1,009** source-explicit colon labels, **2** source-explicit semicolon delimiters, and **14** source-context-attributed supplements.

Payload SHA-256: `{payload_sha}`; bytes: **{payload_bytes:,}**. `integrations/reading-room/QA_REPORT.md` records **PASS** and `manifest.json` records reproducibility hashes. The source booklet prints no scene numbers; all 63 scene ordinals remain archive navigation only. No absent lyric, title or authorship is reconstructed.

The separate Reading Room/public-site repository was **not modified**.

## Exact next activity

**No required Ammayappan repository-internal production work remains. Apply the complete-verified payload in the separate Reading Room implementation repository only when explicitly authorized; site application remains `not-applied`.**'''
if "## Reading Room payload — PASS" not in work_readme:
    pattern = r"## Exact next activity\n\n\*\*Create and QA the source-linked Ammayappan Reading Room integration payload.*?\*\*\s*$"
    work_readme, count = re.subn(pattern, payload_section, work_readme, flags=re.S)
    if count != 1:
        raise SystemExit("Could not locate work README payload-next block")
write_if_changed(work_readme_path, work_readme)


# ---------------------------------------------------------------------------
# Translation README
# ---------------------------------------------------------------------------
trans_readme_path = WORK / "translations" / "README.md"
trans_readme = trans_readme_path.read_text(encoding="utf-8")
trans_payload = f'''## Reading Room payload — PASS

The deterministic source-linked payload at `../integrations/reading-room/reading-room.json` is **complete-verified / QA PASS**. It preserves 63 Tamil scene texts, all **1,210** verified English units, all **1,025** dialogue/source-role links, all **28** cross-page units, and all **5 occurrence identities / 7 source-span links**. Payload SHA-256: `{payload_sha}`. Site application remains **not-applied**.

**Next:** no repository-internal Ammayappan production step is required; apply the payload to the separate Reading Room implementation only when explicitly authorized.'''
if "## Reading Room payload — PASS" not in trans_readme:
    trans_readme, count = re.subn(
        r"\*\*Next:\*\* create and QA the source-linked Ammayappan Reading Room integration payload.*?tiers\.\s*$",
        trans_payload,
        trans_readme,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("Could not locate translation README payload-next block")
write_if_changed(trans_readme_path, trans_readme)


# ---------------------------------------------------------------------------
# Work handover
# ---------------------------------------------------------------------------
project_handover_path = WORK / "PROJECT_HANDOVER.md"
project_handover = project_handover_path.read_text(encoding="utf-8")
project_payload = f'''## Reading Room payload — PASS

`integrations/reading-room/reading-room.json` is complete-verified with payload QA PASS: **63 Tamil scene texts / 1,210 English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities across 7 source spans**. Payload SHA-256 `{payload_sha}`. The site application status is **not-applied**; no separate implementation repository was changed.

## Exact next activity

> **Fetch live `main`; preserve all closed Ammayappan source, translation, reader and Reading Room payload layers. No required repository-internal production work remains. Apply the complete-verified payload to the separate Reading Room implementation repository only when explicitly authorized; until then keep site application `not-applied`.**'''
if "## Reading Room payload — PASS" not in project_handover:
    project_handover, count = re.subn(
        r"## Exact next activity\n\n> \*\*Fetch live `main`; preserve the complete-verified Tamil/structured/English/reader layers\..*?\*\*\s*$",
        project_payload,
        project_handover,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit("Could not locate project handover payload-next block")
write_if_changed(project_handover_path, project_handover)


# ---------------------------------------------------------------------------
# Root README
# ---------------------------------------------------------------------------
root_readme_path = ROOT / "README.md"
root_readme = root_readme_path.read_text(encoding="utf-8")
root_readme = root_readme.replace(
    "- Reading Room integration: **ready after reader/export QA**.",
    "- Reading Room payload: **complete-verified — QA PASS; site application not-applied**.",
    1,
)
root_payload = f'''The **Ammayappan Reading Room payload now passes QA**: 63 Tamil scene texts, all 1,210 verified English units, 1,025 dialogue/source-role links, 28 cross-page units and all 5 occurrence identities / 7 source-span links. Payload SHA-256 `{payload_sha}`. The separate site repository has not been modified.

**Next:** apply the verified payload in the separate Reading Room implementation repository only when explicitly authorized; site application remains not-applied.'''
old_root_next = "**Next:** create and QA the source-linked Ammayappan Reading Room integration payload; preserve the 63 scene IDs strictly as archive navigation and retain all source-provenance/authorship limits."
if root_payload not in root_readme:
    root_readme = must_replace(root_readme, old_root_next, root_payload, "root README Ammayappan next action")
write_if_changed(root_readme_path, root_readme)


# ---------------------------------------------------------------------------
# data/works.json — narrow string update to avoid reformatting unrelated works
# ---------------------------------------------------------------------------
registry_path = ROOT / "data" / "works.json"
registry = registry_path.read_text(encoding="utf-8")
old_registry = '"reading_room_integration":"ready-after-reader-export-qa","next_structured_derivative":"reading-room-integration"'
new_registry = (
    f'"reading_room_integration":"payload-complete-verified",'
    f'"reading_room_payload_path":"works/ammaiyappan/integrations/reading-room/reading-room.json",'
    f'"reading_room_payload_qa_report_path":"works/ammaiyappan/integrations/reading-room/QA_REPORT.md",'
    f'"reading_room_payload_manifest_path":"works/ammaiyappan/integrations/reading-room/manifest.json",'
    f'"reading_room_payload_sha256":"{payload_sha}",'
    f'"reading_room_payload_bytes":{payload_bytes},'
    '"reading_room_payload_scenes":63,'
    '"reading_room_payload_tamil_scene_texts":63,'
    '"reading_room_payload_english_units":1210,'
    '"reading_room_payload_dialogue_source_links":1025,'
    '"reading_room_payload_cross_page_units":28,'
    '"reading_room_payload_occurrence_identities":5,'
    '"reading_room_payload_occurrence_source_span_links":7,'
    '"reading_room_payload_qa":"PASS",'
    '"reading_room_site_application_status":"not-applied",'
    '"next_structured_derivative":"external-reading-room-application"'
)
if new_registry not in registry:
    registry = must_replace(registry, old_registry, new_registry, "data/works Ammayappan integration checkpoint")
old_action = '"next_action":"Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve archive-only scene numbering, exact source provenance, dialogue/source-role distinctions and all five occurrence identities; do not reconstruct absent lyrics, titles or authorship."'
new_action = f'"next_action":"{NEXT_EXTERNAL}"'
if new_action not in registry:
    registry = must_replace(registry, old_action, new_action, "data/works Ammayappan next action")
write_if_changed(registry_path, registry)


# ---------------------------------------------------------------------------
# Repository status audit
# ---------------------------------------------------------------------------
status_path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
status = status_path.read_text(encoding="utf-8")
status = status.replace(
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export **QA PASS**; Reading Room ready |",
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export + Reading Room payload **QA PASS**; site not applied |",
    1,
)
status_payload = f'''## Ammayappan Reading Room payload — PASS

The deterministic source-linked payload is complete-verified at `works/ammaiyappan/integrations/reading-room/reading-room.json`: **63 Tamil scene texts / 1,210 verified English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities across 7 source spans**. Payload SHA-256 `{payload_sha}`; QA is PASS. Exact speaker-label/source-role provenance remains **1,009 colon + 2 source-semicolon + 14 context-attributed**. Site application is **not-applied**, and no frozen source layer was modified.

'''
if "## Ammayappan Reading Room payload — PASS" not in status:
    marker = "## Stable downstream checkpoints for other works"
    status = must_replace(status, marker, status_payload + marker, "status audit payload insertion point")
status = status.replace(
    "**Next production phase:** create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures.",
    "**Next production phase:** no repository-internal Ammayappan production phase remains; separate-site application requires explicit authorization and is currently not-applied.",
    1,
)
status = status.replace(
    "The next bounded activity is **source-linked Reading Room payload construction and QA**.",
    "The source-linked Reading Room payload is now **complete-verified / QA PASS**; separate-site application remains **not-applied** and requires explicit authorization.",
    1,
)
write_if_changed(status_path, status)


# ---------------------------------------------------------------------------
# Master handover
# ---------------------------------------------------------------------------
handover_path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
handover = handover_path.read_text(encoding="utf-8")
old_high = "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export **complete-verified with generated-output QA PASS**; Reading Room payload is next."
new_high = "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export QA PASS; Reading Room payload QA PASS; site not applied."
if new_high not in handover:
    handover = must_replace(handover, old_high, new_high, "master handover Ammayappan high-level checkpoint")
handover = handover.replace(
    "- Reading Room integration: **ready for payload construction/QA**.",
    "- Reading Room payload: **complete-verified — QA PASS; site application not-applied**.",
    1,
)
old_exact = "**Exact next activity:** create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve the 63 scene IDs strictly as archive navigation, exact source/page provenance, all speaker-label/source-role distinctions and all five occurrence identities; never reconstruct absent lyrics, titles or authorship."
new_exact = "**Exact next activity:** no required repository-internal Ammayappan production work remains. Apply the complete-verified Reading Room payload in the separate implementation repository only when explicitly authorized; site application remains not-applied."
if new_exact not in handover:
    handover = must_replace(handover, old_exact, new_exact, "master handover Ammayappan exact next activity")
master_payload = f'''### Reading Room payload — complete-verified

`works/ammaiyappan/integrations/reading-room/reading-room.json` is QA PASS with **63 Tamil scene texts / 1,210 English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities / 7 source-span links**. Payload SHA-256 `{payload_sha}`. The source booklet's 63 archival scene ordinals remain derivative navigation only. Site application is **not-applied** and requires separate explicit authorization.

'''
if "### Reading Room payload — complete-verified" not in handover:
    marker = "---\n\n## 9. Downstream dispositions for completed works"
    handover = must_replace(handover, marker, master_payload + marker, "master handover payload insertion point")
write_if_changed(handover_path, handover)


# ---------------------------------------------------------------------------
# NEXT_CHAT_PROMPT — close repository-internal production
# ---------------------------------------------------------------------------
prompt_path = WORK / "NEXT_CHAT_PROMPT.md"
prompt = prompt_path.read_text(encoding="utf-8")
prompt = prompt.replace(
    "- Reading Room integration: **ready for payload construction/QA**.",
    f"- Reading Room payload: **complete-verified — QA PASS**, SHA-256 `{payload_sha}`; site application **not-applied**.",
    1,
)
closed_prompt = "> **Fetch live `main`; preserve all complete-verified Ammayappan Tamil, structured, English, reader/export and Reading Room payload layers. Confirm `integrations/reading-room/QA_REPORT.md` and `manifest.json` remain PASS. No required repository-internal production work remains. Do not apply the payload to the separate Reading Room implementation repository unless explicitly authorized. If external application is authorized later, preserve archive-only scene numbering, exact Tamil speaker/source-role/page provenance, all 1,210 English units, all 1,025 dialogue/source-role links, all 28 cross-page units and all five occurrence identities across seven source-span links; never reconstruct absent lyrics, titles or authorship.**"
if closed_prompt not in prompt:
    prompt, count = re.subn(
        r"> \*\*Fetch live `main`; confirm English translation remains complete-verified.*?separate-site application remains a later explicit step\.\*\*\s*$",
        closed_prompt,
        prompt,
        flags=re.S,
    )
    if count != 1:
        # Current prompts may have no stray quote at the end; accept that variant too.
        prompt, count = re.subn(
            r"> \*\*Fetch live `main`; confirm English translation remains complete-verified.*?separate-site application remains a later explicit step\.\*\*\s*$",
            closed_prompt,
            prompt,
            flags=re.S,
        )
    if count != 1:
        raise SystemExit("Could not locate NEXT_CHAT_PROMPT payload instruction")
write_if_changed(prompt_path, prompt)

print("Synchronized Ammayappan Reading Room payload PASS status")
for path in changed:
    print(path)
