#!/usr/bin/env python3
"""Synchronize Ammayappan status mirrors after Reading Room payload QA PASS."""

from __future__ import annotations

import json
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
        raise SystemExit(f"Refusing sync: checkpoint {key} differs")
output = manifest.get("output", {})
payload_sha = output.get("sha256")
payload_bytes = output.get("bytes")
if not isinstance(payload_sha, str) or len(payload_sha) != 64 or not isinstance(payload_bytes, int):
    raise SystemExit("Refusing sync: payload output metadata missing")

changed: list[str] = []

def replace(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"Could not locate status checkpoint in {path}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")
    changed.append(path)

# Translation index: preserve its compact machine-readable shape.
index_path = WORK / "translations" / "index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
index.update({
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
    "next_activity": "No required Ammayappan repository-internal production work remains. Apply the complete-verified Reading Room payload in the separate implementation repository only when explicitly authorized; site application is not applied.",
})
index_path.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
changed.append("works/ammaiyappan/translations/index.json")

# Metadata.
replace(
    "works/ammaiyappan/metadata.yaml",
    "  reading_room_integration: ready-after-reader-export-qa\n\nstatus:",
    f'''  reading_room_integration: payload-complete-verified\n  reading_room_payload_path: "integrations/reading-room/reading-room.json"\n  reading_room_payload_qa_report_path: "integrations/reading-room/QA_REPORT.md"\n  reading_room_payload_manifest_path: "integrations/reading-room/manifest.json"\n  reading_room_payload_sha256: "{payload_sha}"\n  reading_room_payload_bytes: {payload_bytes}\n  reading_room_payload_scenes: 63\n  reading_room_payload_tamil_scene_texts: 63\n  reading_room_payload_english_units: 1210\n  reading_room_payload_dialogue_source_links: 1025\n  reading_room_payload_cross_page_units: 28\n  reading_room_payload_occurrence_identities: 5\n  reading_room_payload_occurrence_source_span_links: 7\n  reading_room_payload_qa_status: PASS\n  reading_room_site_application_status: not-applied\n\nstatus:''',
)
replace(
    "works/ammaiyappan/metadata.yaml",
    '  reading_room_integration: ready-after-reader-export-qa\n\nnext_action: "Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve archive-only scene numbering, exact source provenance, dialogue/source-role distinctions and all five occurrence identities; do not reconstruct absent lyrics, titles or authorship."',
    '  reading_room_integration: payload-complete-verified\n\nnext_action: "No required Ammayappan repository-internal production work remains. Apply the complete-verified Reading Room payload in the separate implementation repository only when explicitly authorized; site application is not applied."',
)

# Work README and translation README.
replace(
    "works/ammaiyappan/README.md",
    "## Exact next activity\n\n**Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve the 63 scene IDs strictly as archive navigation, exact page/source provenance, all dialogue/source-role distinctions and all five source-visible occurrence identities; do not reconstruct absent lyrics, titles or authorship.**",
    f'''## Reading Room payload — PASS\n\nThe deterministic source-linked Reading Room payload is **complete-verified** under `integrations/reading-room/`. It carries **63/63 Tamil scene texts**, all **1,210** verified English units, **1,025/1,025** dialogue/source-role links, all **28** cross-page units, and all **5 occurrence identities / 7 intentional source-span links**. Exact Tamil speaker-label origins are retained: **1,009** source-explicit colon labels, **2** source-explicit semicolon delimiters, and **14** source-context-attributed supplements.\n\nPayload SHA-256: `{payload_sha}`; bytes: **{payload_bytes:,}**. `integrations/reading-room/QA_REPORT.md` records **PASS** and `manifest.json` records reproducibility hashes. The source booklet still has no scene numbering; all 63 scene ordinals remain archive navigation only. No absent lyric, title or authorship is reconstructed.\n\nThe separate Reading Room/public-site repository was **not modified**.\n\n## Exact next activity\n\n**No required Ammayappan repository-internal production work remains. Apply the complete-verified payload in the separate Reading Room implementation repository only when explicitly authorized; site application remains `not-applied`.**''',
)
replace(
    "works/ammaiyappan/translations/README.md",
    "**Next:** create and QA the source-linked Ammayappan Reading Room integration payload from these complete-verified structures; preserve archive-only scene numbering and all source-evidence tiers.",
    f'''## Reading Room payload — PASS\n\nThe deterministic source-linked payload at `../integrations/reading-room/reading-room.json` is **complete-verified / QA PASS**. It preserves 63 Tamil scene texts, all **1,210** verified English units, all **1,025** dialogue/source-role links, all **28** cross-page units, and all **5 occurrence identities / 7 source-span links**. Payload SHA-256: `{payload_sha}`. Site application remains **not-applied**.\n\n**Next:** no repository-internal Ammayappan production step is required; apply the payload to the separate Reading Room implementation only when explicitly authorized.''',
)

# Project handover.
replace(
    "works/ammaiyappan/PROJECT_HANDOVER.md",
    "## Exact next activity\n\n> **Fetch live `main`; preserve the complete-verified Tamil/structured/English/reader layers. Create and QA the source-linked Ammayappan Reading Room integration payload from the verified reader/translation structures. Preserve the 63 scene IDs as archive-only navigation, exact page/source provenance, all dialogue/source-role distinctions and all five source-visible occurrence identities; do not reconstruct absent lyrics, titles or authorship. Synchronize all mirrors after payload QA before any separate-site application.**",
    f'''## Reading Room payload — PASS\n\n`integrations/reading-room/reading-room.json` is complete-verified with payload QA PASS: **63 Tamil scene texts / 1,210 English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities across 7 source spans**. Payload SHA-256 `{payload_sha}`. The site application status is **not-applied**; no separate implementation repository was changed.\n\n## Exact next activity\n\n> **Fetch live `main`; preserve all closed Ammayappan source, translation, reader and Reading Room payload layers. No required repository-internal production work remains. Apply the complete-verified payload to the separate Reading Room implementation repository only when explicitly authorized; until then keep site application `not-applied`.**''',
)

# Root README.
replace(
    "README.md",
    "- Reading Room integration: **ready after reader/export QA**.",
    "- Reading Room payload: **complete-verified — QA PASS; site application not-applied**.",
)
replace(
    "README.md",
    "**Next:** create and QA the source-linked Ammayappan Reading Room integration payload; preserve the 63 scene IDs strictly as archive navigation and retain all source-provenance/authorship limits.",
    f'''The **Ammayappan Reading Room payload now passes QA**: 63 Tamil scene texts, all 1,210 verified English units, 1,025 dialogue/source-role links, 28 cross-page units and all 5 occurrence identities / 7 source-span links. Payload SHA-256 `{payload_sha}`. The separate site repository has not been modified.\n\n**Next:** apply the verified payload in the separate Reading Room implementation repository only when explicitly authorized; site application remains not-applied.''',
)

# data/works.json: preserve compact formatting of the Ammayappan object.
registry_path = ROOT / "data" / "works.json"
registry = registry_path.read_text(encoding="utf-8")
old = '"reading_room_integration":"ready-after-reader-export-qa","next_structured_derivative":"reading-room-integration"'
new = f'"reading_room_integration":"payload-complete-verified","reading_room_payload_path":"works/ammaiyappan/integrations/reading-room/reading-room.json","reading_room_payload_qa_report_path":"works/ammaiyappan/integrations/reading-room/QA_REPORT.md","reading_room_payload_manifest_path":"works/ammaiyappan/integrations/reading-room/manifest.json","reading_room_payload_sha256":"{payload_sha}","reading_room_payload_bytes":{payload_bytes},"reading_room_payload_scenes":63,"reading_room_payload_tamil_scene_texts":63,"reading_room_payload_english_units":1210,"reading_room_payload_dialogue_source_links":1025,"reading_room_payload_cross_page_units":28,"reading_room_payload_occurrence_identities":5,"reading_room_payload_occurrence_source_span_links":7,"reading_room_payload_qa":"PASS","reading_room_site_application_status":"not-applied","next_structured_derivative":"external-reading-room-application"'
if new not in registry:
    if old not in registry:
        raise SystemExit("Could not locate Ammayappan registry integration checkpoint")
    registry = registry.replace(old, new, 1)
old_action = '"next_action":"Create and QA the source-linked Ammayappan Reading Room integration payload from the complete-verified reader/translation structures. Preserve archive-only scene numbering, exact source provenance, dialogue/source-role distinctions and all five occurrence identities; do not reconstruct absent lyrics, titles or authorship."'
new_action = '"next_action":"No required Ammayappan repository-internal production work remains. Apply the complete-verified Reading Room payload in the separate implementation repository only when explicitly authorized; site application is not applied."'
if new_action not in registry:
    if old_action not in registry:
        raise SystemExit("Could not locate Ammayappan registry next action")
    registry = registry.replace(old_action, new_action, 1)
registry_path.write_text(registry, encoding="utf-8")
changed.append("data/works.json")

# Status audit: advance matrix and add durable payload gate before stable downstream checkpoints.
replace(
    "docs/STATUS_CONSISTENCY_AUDIT.md",
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export **QA PASS**; Reading Room ready |",
    "| Ammayappan | canonical Tamil **105/105 complete-verified** | **63/63 scenes; 1,025 dialogue units; 62 labels / 26 entities; song gate closed** | **complete-verified 63/63 / 1,210 units** | reader/export + Reading Room payload **QA PASS**; site not applied |",
)
status_path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
status = status_path.read_text(encoding="utf-8")
section = f'''## Ammayappan Reading Room payload — PASS\n\nThe deterministic source-linked payload is complete-verified at `works/ammaiyappan/integrations/reading-room/reading-room.json`: **63 Tamil scene texts / 1,210 verified English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities across 7 source spans**. Payload SHA-256 `{payload_sha}`; QA is PASS. Exact speaker-label/source-role provenance remains **1,009 colon + 2 source-semicolon + 14 context-attributed**. Site application is **not-applied**, and no frozen source layer was modified.\n\n'''
marker = "## Stable downstream checkpoints for other works"
if section.strip() not in status:
    if marker not in status:
        raise SystemExit("Could not locate status-audit insertion point")
    status = status.replace(marker, section + marker, 1)
    status_path.write_text(status, encoding="utf-8")
    if "docs/STATUS_CONSISTENCY_AUDIT.md" not in changed:
        changed.append("docs/STATUS_CONSISTENCY_AUDIT.md")

# Master handover: advance high-level line and add closed payload checkpoint.
replace(
    "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
    "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**, whole-work reconciliation PASS; executable reader/export preflight **PASS**; deterministic reader/export generation is next.",
    "- **Ammayappan** — canonical Tamil **105/105 dual-gate complete-verified**; **63/63** scene derivatives; dialogue authority **1,009 explicit + 16 supplements = 1,025 downstream units**; character/entity coverage **1,025/1,025 / 62/62 labels / 26 entities**; song/performance gate **64/64 candidates / 5 retained occurrences / 0 standalone lyric files**; English translation **complete-verified 63/63 / 1,210 units**; reader/export QA PASS; Reading Room payload QA PASS; site not applied.",
)
handover_path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
handover = handover_path.read_text(encoding="utf-8")
section2 = f'''### Reading Room payload — complete-verified\n\n`works/ammaiyappan/integrations/reading-room/reading-room.json` is QA PASS with **63 Tamil scene texts / 1,210 English units / 1,025 dialogue-source links / 28 cross-page units / 5 occurrence identities / 7 source-span links**. Payload SHA-256 `{payload_sha}`. The source booklet's 63 archival scene ordinals remain derivative navigation only. Site application is **not-applied** and requires separate explicit authorization.\n\n'''
marker2 = "---\n\n## 9. Downstream dispositions for completed works"
if section2.strip() not in handover:
    if marker2 not in handover:
        raise SystemExit("Could not locate master-handover insertion point")
    handover = handover.replace(marker2, section2 + marker2, 1)
    handover_path.write_text(handover, encoding="utf-8")
    if "docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md" not in changed:
        changed.append("docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md")

# Continuation prompt: close payload construction and leave only explicitly authorized external application.
prompt_path = WORK / "NEXT_CHAT_PROMPT.md"
prompt = prompt_path.read_text(encoding="utf-8")
prompt = prompt.replace(
    "- Reading Room integration: **ready for payload construction/QA**.",
    f"- Reading Room payload: **complete-verified — QA PASS**, SHA-256 `{payload_sha}`; site application **not-applied**.",
)
old_prompt = "> **Fetch live `main`; confirm English translation remains complete-verified at 63/63 scenes / 1,210 units, `editions/en/PREFLIGHT_QA_REPORT.md` is PASS, and the deterministic reader/export package is complete-verified with `editions/en/QA_REPORT.md` + `manifest.json` PASS. Then create and QA the source-linked Ammayappan Reading Room integration payload from the verified reader/translation structures. Preserve all 1,210 units, all 1,025 dialogue/source-role links, all 28 cross-page units, all five occurrence identities across seven intentional source-span links, exact Tamil speaker-label/source-role provenance, page provenance and archive-only scene numbering. Do not alter frozen Tamil/dialogue/character/song evidence and do not reconstruct absent lyrics, titles or authorship. Synchronize all current mirrors after payload QA; separate-site application remains a later explicit step.**"
new_prompt = "> **Fetch live `main`; preserve all complete-verified Ammayappan Tamil, structured, English, reader/export and Reading Room payload layers. Confirm `integrations/reading-room/QA_REPORT.md` and `manifest.json` remain PASS. No required repository-internal production work remains. Do not apply the payload to the separate Reading Room implementation repository unless explicitly authorized. If external application is authorized later, preserve archive-only scene numbering, exact Tamil speaker/source-role/page provenance, all 1,210 English units, all 1,025 dialogue/source-role links, all 28 cross-page units and all five occurrence identities across seven source-span links; never reconstruct absent lyrics, titles or authorship.**"
if old_prompt in prompt:
    prompt = prompt.replace(old_prompt, new_prompt, 1)
elif new_prompt not in prompt:
    raise SystemExit("Could not locate next-chat payload instruction")
prompt_path.write_text(prompt, encoding="utf-8")
changed.append("works/ammaiyappan/NEXT_CHAT_PROMPT.md")

print("Synchronized Ammayappan Reading Room payload PASS status")
for path in changed:
    print(path)
