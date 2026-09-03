#!/usr/bin/env python3
"""Synchronize Raja Rani completion across all active repository status surfaces."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "raja-rani"

READER_MD_SHA = "6437a0a39cebbaf17ab63f76f7aef6f9f62eb3c4abbd07864974d47be20902c8"
READER_HTML_SHA = "c24ea9ab0f1ee77b3bc795b3134e4ad8bed78f00d6a8f896f9749052ff074ec6"
READER_JSON_SHA = "76827d570f3079c04463e3142a9edf32f35c1497e2b820bfa467f8203d7441e2"
READER_INPUT_SHA = "35cfc21e70eed9e0fb820c3df6a6a1c41fbddc21594f78b0cb5a799ab6a7efc2"
RR_PAYLOAD_SHA = "ab1058cb5a22ba78e68938f50efc586cc53eb07ef544bdf3919bb3c4b8c46c9b"
RR_PAYLOAD_BYTES = 974510
RR_PAYLOAD_INPUT_SHA = "40bb6c42dfda5049a4e030ca5ace5536e1ea54e14ac91c4ff41cbb455ab18078"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one replacement anchor, found {text.count(old)}")
    return text.replace(old, new, 1)


def replace_regex(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: regex anchor not found uniquely")
    return updated


def sync_metadata() -> None:
    path = WORK / "metadata.yaml"
    text = read(path)
    text = replace_once(
        text,
        "  structured_derivatives: bilingual-text-complete-verified-reader-export-next",
        "  structured_derivatives: complete-verified-reader-and-reading-room-payload",
        "metadata structured_derivatives",
    )
    old = "  english_reader_export: not-started\n  reading_room_integration: not-started"
    new = f"""  english_reader_export: complete-verified
  english_reader_directory: works/raja-rani/editions/en
  english_reader_preflight: complete-pass
  english_reader_preflight_path: works/raja-rani/editions/en/PREFLIGHT_QA_REPORT.md
  english_reader_qa: PASS
  english_reader_qa_path: works/raja-rani/editions/en/QA_REPORT.md
  english_reader_manifest_path: works/raja-rani/editions/en/manifest.json
  english_reader_authoritative_input_files: 200
  english_reader_authoritative_input_sha256: {READER_INPUT_SHA}
  english_reader_markdown_sha256: {READER_MD_SHA}
  english_reader_html_sha256: {READER_HTML_SHA}
  english_reader_json_sha256: {READER_JSON_SHA}
  reading_room_integration: payload-complete-verified
  reading_room_payload_path: works/raja-rani/integrations/reading-room/reading-room.json
  reading_room_payload_qa: PASS
  reading_room_payload_qa_path: works/raja-rani/integrations/reading-room/QA_REPORT.md
  reading_room_payload_manifest_path: works/raja-rani/integrations/reading-room/manifest.json
  reading_room_payload_bytes: {RR_PAYLOAD_BYTES}
  reading_room_payload_sha256: {RR_PAYLOAD_SHA}
  reading_room_payload_reader_input_sha256: {RR_PAYLOAD_INPUT_SHA}
  reading_room_site_application: not-applied"""
    text = replace_once(text, old, new, "metadata reader/integration status")
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith("next_action:")]
    if len(matches) != 1:
        raise RuntimeError("metadata next_action anchor not unique")
    lines[matches[0]] = 'next_action: "No required Raja Rani repository-internal archival, translation, reader/export or Reading Room-payload work remains. The verified payload is ready for the separate Reading Room implementation repository only when that repository is explicitly authorized for modification; site application remains not-applied."'
    write(path, "\n".join(lines))


def sync_work_readme() -> None:
    path = WORK / "README.md"
    text = read(path)
    current = """## Current gate

- source intake: **complete**
- canonical Tamil / fidelity: **complete-verified — 79/79 source pages**
- scene segmentation: **complete — 58/58 verified**
- dialogue layer: **complete — 1,071 unique records / 58 scenes**
- character/entity layer: **complete-verified — 80/80 labels / 44 entities**
- song/performance authorship derivative: **complete-with-unresolved-authorship — 15 occurrences**
- Tamil numbered songs: **complete-verified — 11/11**
- English screenplay translation: **complete-verified — 58/58 scenes / 1,236 units / 1,071 links**
- English numbered-song translation: **complete-verified — 11/11 / 67 sections / 181 line-cues**
- deterministic bilingual reader/export: **complete-verified — QA PASS**
- Reading Room integration payload: **complete-verified — QA PASS**
- Reading Room site application: **not applied**

Reader/export:

- `editions/en/PREFLIGHT_QA_REPORT.md` — PASS over 200 authoritative inputs;
- `editions/en/reader-edition.md` — 526,184 bytes;
- `editions/en/reader-edition.html` — 675,121 bytes;
- `editions/en/reader-edition.json` — 971,896 bytes;
- `editions/en/QA_REPORT.md` — generated-output PASS;
- `editions/en/manifest.json` — reproducibility hashes.

Reading Room payload:

- `integrations/reading-room/reading-room.json` — **974,510 bytes**, SHA-256 `{RR_PAYLOAD_SHA}`;
- `integrations/reading-room/QA_REPORT.md` — PASS;
- `integrations/reading-room/manifest.json` — site application explicitly `not-applied`.

Repository-wide mirrors (`data/works.json`, root README, project handover and status audit) are synchronized to this same checkpoint.

"""
    text = replace_regex(text, r"## Current gate\n.*?(?=## Source rules\n)", current, "work README current gate")
    next_section = """## Next activity

No required Raja Rani work remains **inside `pugazg/kalaignar-cinema-works`**. The source archive, structured derivatives, English screenplay, numbered-song English layer, deterministic bilingual reader/export and Reading Room payload are complete-verified with QA PASS.

The only downstream step is application of `integrations/reading-room/reading-room.json` in the **separate** Reading Room implementation repository. Do that only when modification of that repository is explicitly authorized. Until then, `site_application_status` remains `not-applied`.

Do not create a standalone PDF or EPUB by default.
"""
    text = replace_regex(text, r"## Next activity\n.*\Z", next_section, "work README next activity")
    write(path, text)


def sync_translation_readme() -> None:
    path = WORK / "translations" / "README.md"
    text = read(path)
    replacement = f"""## Reader/export and Reading Room downstream state

The completed English screenplay and numbered-song records have passed deterministic whole-work publication QA.

- bilingual reader/export: **complete-verified — QA PASS**;
- reader preflight: **58/58 scenes, 1,236 units, 1,071/1,071 immutable links, 11/11 songs, 181/181 song line-cues**;
- generated reader outputs: Markdown / standalone HTML / machine JSON + QA report + manifest;
- Reading Room payload: **complete-verified — QA PASS**;
- payload preserves 11 actual source-numbered songs separately from 58 archival-only screenplay navigation scenes;
- site application: **not-applied**.

Reader QA: `../editions/en/QA_REPORT.md`.  
Reader manifest: `../editions/en/manifest.json`.  
Reading Room QA: `../integrations/reading-room/QA_REPORT.md`.  
Reading Room payload: `../integrations/reading-room/reading-room.json`.

## Next activity

No required English/reader/integration-payload work remains in this repository. Apply the verified Reading Room payload only in the separate implementation repository when that repository is explicitly authorized for modification.
"""
    text = replace_regex(text, r"## Next activity\n.*\Z", replacement, "translation README downstream status")
    write(path, text)


def sync_json_indexes() -> None:
    # Work-level English translation index.
    path = WORK / "translations" / "index.json"
    data = json.loads(read(path))
    data["reader_export"] = {
        "status": "complete-verified",
        "directory": "works/raja-rani/editions/en",
        "preflight": "PASS",
        "qa": "PASS",
        "authoritative_input_files": 200,
        "authoritative_input_aggregate_sha256": READER_INPUT_SHA,
        "markdown_sha256": READER_MD_SHA,
        "html_sha256": READER_HTML_SHA,
        "json_sha256": READER_JSON_SHA,
    }
    data["reading_room_integration"] = {
        "status": "payload-complete-verified",
        "payload_path": "works/raja-rani/integrations/reading-room/reading-room.json",
        "qa": "PASS",
        "payload_bytes": RR_PAYLOAD_BYTES,
        "payload_sha256": RR_PAYLOAD_SHA,
        "site_application": "not-applied",
    }
    data["next_activity"] = "No required repository-internal translation, reader/export or Reading Room-payload activity remains. Apply the verified payload in the separate Reading Room implementation repository only when explicitly authorized."
    write(path, json.dumps(data, ensure_ascii=False, indent=2))

    # Dedicated numbered-song English index.
    path = WORK / "translations" / "songs" / "index.json"
    data = json.loads(read(path))
    data["reader_export"] = {"status": "complete-verified", "qa": "PASS", "path": "works/raja-rani/editions/en"}
    data["reading_room_integration"] = {"status": "payload-complete-verified", "qa": "PASS", "site_application": "not-applied"}
    data["next_activity"] = "No numbered-song translation or repository-internal reader/payload work remains; preserve current authorship and performance-link tiers."
    write(path, json.dumps(data, ensure_ascii=False, indent=2))

    # Source song gate index.
    path = WORK / "songs" / "index.json"
    data = json.loads(read(path))
    data["english_numbered_song_translation"] = "complete-verified"
    data["english_numbered_song_translation_verified"] = 11
    data["reader_export"] = "complete-verified"
    data["reading_room_integration"] = "payload-complete-verified"
    data["reading_room_site_application"] = "not-applied"
    data["next_activity"] = "No song/performance, song-translation, reader/export or repository-internal Reading Room payload work remains."
    write(path, json.dumps(data, ensure_ascii=False, indent=2))


def sync_song_docs() -> None:
    path = WORK / "songs" / "README.md"
    text = read(path)
    final = """## Final downstream state

The source song/performance gate remains **complete with unresolved authorship** and its evidence tiers are unchanged:

- Tamil numbered-song derivatives: **11/11 complete-verified**;
- English numbered-song derivatives: **11/11 complete-verified**;
- reader/export: **complete-verified — QA PASS**;
- Reading Room payload: **complete-verified — QA PASS**;
- site application: **not-applied**;
- authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**;
- screenplay performance relations: **3 verified / 1 review**.

No later translation, reader or integration phase upgrades authorship or the scene-58/song-11 review relation.

## Next gate

No repository-internal song/performance work remains. Preserve this evidence state; apply the verified Reading Room payload externally only when that separate repository is explicitly authorized.
"""
    if "## Next gate" in text:
        text = replace_regex(text, r"## Next gate\n.*\Z", final, "songs README final gate")
    else:
        text = text.rstrip() + "\n\n" + final
    write(path, text)

    path = WORK / "notes" / "song-performance-authorship-gate.md"
    text = read(path)
    final_note = """## Final downstream state

The song/authorship evidence gate is unchanged and closed. Downstream completion now also includes:

- 11/11 verified English numbered-song records;
- deterministic whole-work bilingual reader/export — QA PASS;
- deterministic Reading Room payload — QA PASS;
- site application — `not-applied`.

The five later-anthology Kalaignar attributions remain exactly songs 3, 5, 6, 7 and 8; the other six numbered-song lyricists remain unresolved; scene 58 → song 11 remains review-level.

## Next gate

No repository-internal song, translation, reader/export or Reading Room-payload work remains. External site application requires explicit authorization for the separate implementation repository.
"""
    text = replace_regex(text, r"## Next gate\n.*\Z", final_note, "song authorship note final gate")
    write(path, text)

    path = WORK / "translations" / "songs" / "README.md"
    text = read(path)
    if "## Downstream completion" not in text:
        text += """

## Downstream completion

The 11/11 verified song records are now included in the deterministic Raja Rani bilingual reader/export and Reading Room payload. Both downstream QA gates pass. Authorship/performance-link tiers remain unchanged, and site application remains `not-applied`.
"""
    write(path, text)


def sync_edition_docs() -> None:
    path = WORK / "editions" / "en" / "README.md"
    text = read(path)
    completion = f"""## Completion checkpoint

Status: **complete-verified — QA PASS**.

- preflight authoritative inputs: **200**;
- screenplay: **58/58 scenes / 1,236 units / 1,071 immutable links**;
- numbered songs: **11/11 / 67 sections / 181 line-cues**;
- generated Markdown SHA-256: `{READER_MD_SHA}`;
- generated HTML SHA-256: `{READER_HTML_SHA}`;
- generated JSON SHA-256: `{READER_JSON_SHA}`;
- generated-output QA: `QA_REPORT.md` — **PASS**.

The separate Reading Room payload built from this reader is also QA-PASS under `../../integrations/reading-room/`.

"""
    if "## Completion checkpoint" not in text:
        text = replace_once(text, "## Outputs\n", completion + "## Outputs\n", "edition README completion")
    write(path, text)

    path = WORK / "integrations" / "reading-room" / "README.md"
    text = read(path)
    completion = f"""## Completion checkpoint

Status: **payload-complete-verified — QA PASS**.

- payload: `reading-room.json`;
- payload bytes: **{RR_PAYLOAD_BYTES:,}**;
- payload SHA-256: `{RR_PAYLOAD_SHA}`;
- QA: `QA_REPORT.md` — **PASS**;
- site application: **not-applied**.

The payload is ready for the separate public-site implementation repository when that repository is explicitly authorized for modification.

"""
    if "## Completion checkpoint" not in text:
        text = replace_once(text, "## Outputs\n", completion + "## Outputs\n", "integration README completion")
    write(path, text)


def final_handover_text() -> str:
    return f"""# Raja Rani — Final Repository Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/raja-rani/` — **ராஜா ராணி**

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Do not reopen completed work because an older historical batch file contains an earlier count.

## Controlling source

- `TVA_BOK_0017188_ராஜா_ராணி.pdf`
- 80 PDF pages
- SHA-256: `{SOURCE_SHA}`
- numbered songs: PDF 4–9
- screenplay/dialogue: PDF 10–79 / printed pp.9–78

## Final archival state

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- archival scene derivatives: **58/58**, blocked 0;
- immutable dialogue records: **1,071**;
- exact source labels: **80/80**;
- verified entities/roles/collectives: **44**;
- numbered Tamil songs: **11/11**;
- song/performance occurrences: **15**;
- authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**.

Permanent direct-scan verdicts include PDF27 `இரவெல்லாம்`, PDF48 `வந்தனா` / `திடீர்னு`, PDF57 `முன்னுக்கு பின் முரணாயிகிட்டே போவது?`, and PDF74's `K. N. சங்கரன் ...` as a non-canonical ownership/library stamp.

The T055/T056 correction is permanent: scene 55 owns 25 immutable dialogue records, scene 56 owns 5, and deleted duplicate IDs `s055-d026`–`s055-d030` must never be restored.

## Final English state

Screenplay:

- **58/58 scenes**;
- **1,236 verified units**;
- **1,071/1,071 immutable dialogue links**;
- 19 source-unlabelled spoken units;
- 15 cross-page English units;
- 4/4 screenplay performance references.

Numbered songs:

- **11/11 verified English song records**;
- **67 sections**;
- **181/181 Tamil-English line/cue mappings**;
- 4 cross-page songs;
- authorship/performance tiers unchanged.

## Deterministic reader/export — COMPLETE

Directory: `works/raja-rani/editions/en/`

- preflight: **PASS** over 200 authoritative inputs;
- generated Markdown / HTML / JSON: **QA PASS**;
- Markdown SHA-256: `{READER_MD_SHA}`;
- HTML SHA-256: `{READER_HTML_SHA}`;
- JSON SHA-256: `{READER_JSON_SHA}`.

The reader preserves 11 source-numbered songs separately from 58 archival-only screenplay navigation scenes.

## Reading Room payload — COMPLETE

Directory: `works/raja-rani/integrations/reading-room/`

- payload QA: **PASS**;
- payload bytes: **{RR_PAYLOAD_BYTES:,}**;
- payload SHA-256: `{RR_PAYLOAD_SHA}`;
- site application: **not-applied**.

The payload is ready for the separate Reading Room implementation repository but has not been applied there.

## Mandatory startup for any future Raja Rani work

Read:

1. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`
2. `docs/STATUS_CONSISTENCY_AUDIT.md`
3. this handover
4. `docs/NEXT_CHAT_PROMPT_RAJA_RANI.md`
5. `works/raja-rani/README.md`
6. `works/raja-rani/metadata.yaml`
7. `works/raja-rani/editions/en/QA_REPORT.md`
8. `works/raja-rani/editions/en/manifest.json`
9. `works/raja-rani/integrations/reading-room/QA_REPORT.md`
10. `works/raja-rani/integrations/reading-room/manifest.json`

## Exact next activity

There is **no required Raja Rani repository-internal activity** remaining.

If the user explicitly authorizes modification of the separate Kalaignar Digital Library / Reading Room implementation repository, apply `works/raja-rani/integrations/reading-room/reading-room.json` there while preserving its navigation, provenance, authorship and language-presentation rules. Otherwise make no further production changes merely to generate another standalone format.
"""


def final_next_prompt_text() -> str:
    return """# Next Chat Prompt — Raja Rani — Completed Archive / Reading Room Handoff

Continue from live `main` in `pugazg/kalaignar-cinema-works`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Raja Rani is complete inside this repository; do not repeat source, transcription, scene, dialogue, character, translation, reader or payload work because an older historical file records an earlier checkpoint.

## Final checkpoint

- 79/79 source pages verified;
- 70/70 screenplay pages verified;
- 58/58 archival scenes;
- 1,071 immutable dialogue records;
- 80/80 exact source labels / 44 verified entities/roles/collectives;
- 58/58 English screenplay scenes / 1,236 units / 1,071 links;
- 11/11 numbered Tamil songs and 11/11 numbered English songs;
- 67 song sections / 181 Tamil-English line-cue mappings;
- deterministic bilingual reader/export: QA PASS;
- Reading Room payload: QA PASS;
- public-site application: not applied.

Reader QA: `works/raja-rani/editions/en/QA_REPORT.md`.  
Reading Room payload: `works/raja-rani/integrations/reading-room/reading-room.json`.  
Reading Room QA: `works/raja-rani/integrations/reading-room/QA_REPORT.md`.

## Exact next activity

No required work remains in `pugazg/kalaignar-cinema-works` for Raja Rani.

Only if the user explicitly authorizes modifying the **separate** Reading Room implementation repository, apply the verified payload there. Preserve:

- 11 numbered songs as actual source-numbered front-matter structures;
- 58 screenplay ordinals as archival navigation only, never source scene numbers;
- Tamil/English text without rewriting;
- page/source provenance;
- 5 later-anthology Kalaignar-attributed / 6 unresolved song authorship state;
- scene 58 → song 11 as review-level only.

Do not create a standalone PDF or EPUB by default.
"""

SOURCE_SHA = "26ecc026b89deafac94bb3b107ee7c5f361c68796c4a1cdf4d01ad7c1c0d31a4"


def sync_handovers() -> None:
    write(ROOT / "docs" / "HANDOVER_RAJA_RANI.md", final_handover_text())
    write(ROOT / "docs" / "NEXT_CHAT_PROMPT_RAJA_RANI.md", final_next_prompt_text())


def sync_registry() -> None:
    path = ROOT / "data" / "works.json"
    data = json.loads(read(path))
    matches = [w for w in data if w.get("id") == "raja-rani"]
    if len(matches) != 1:
        raise RuntimeError("data/works.json must contain exactly one raja-rani entry")
    w = matches[0]
    sd = w.setdefault("structured_derivatives", {})
    sd["reader_export"] = "complete-verified"
    sd["english_reader_edition"] = "complete-verified"
    sd["english_reader_edition_directory"] = "works/raja-rani/editions/en"
    sd["english_reader_preflight"] = "complete-pass"
    sd["english_reader_qa"] = "PASS"
    sd["english_reader_qa_units"] = 1236
    sd["english_reader_qa_dialogue_links"] = 1071
    sd["english_reader_qa_song_line_cues"] = 181
    sd["english_reader_authoritative_input_files"] = 200
    sd["english_reader_markdown_sha256"] = READER_MD_SHA
    sd["english_reader_html_sha256"] = READER_HTML_SHA
    sd["english_reader_json_sha256"] = READER_JSON_SHA
    sd["reading_room_integration"] = "payload-complete-verified"
    sd["reading_room_payload_path"] = "works/raja-rani/integrations/reading-room/reading-room.json"
    sd["reading_room_payload_qa"] = "PASS"
    sd["reading_room_payload_bytes"] = RR_PAYLOAD_BYTES
    sd["reading_room_payload_sha256"] = RR_PAYLOAD_SHA
    sd["reading_room_site_application"] = "not-applied"
    sd["next_structured_derivative"] = None
    w["next_action"] = "No required Raja Rani repository-internal work remains. Apply the complete-verified Reading Room payload in the separate implementation repository only when explicitly authorized; site application is not applied."
    write(path, json.dumps(data, ensure_ascii=False, indent=2))


def sync_root_readme() -> None:
    path = ROOT / "README.md"
    text = read(path)
    section = f"""## ராஜா ராணி status

`TVA_BOK_0017188_ராஜா_ராணி.pdf` is now a **complete-verified bilingual archival work with deterministic reader/export and Reading Room payload QA PASS**.

- source scan: **80 PDF pages**; SHA-256 `{SOURCE_SHA}`;
- verified canonical source pages: **79/79**;
- verified screenplay pages: **70/70**;
- archival scene derivatives: **58/58**, blocked 0;
- immutable dialogue records: **1,071**;
- exact source labels / entities: **80/80 / 44**;
- numbered Tamil songs: **11/11**;
- English screenplay: **58/58 scenes / 1,236 verified units / 1,071/1,071 dialogue links**;
- English numbered songs: **11/11 / 67 sections / 181 Tamil-English line-cue mappings**;
- song authorship: **5 later-anthology Kalaignar-attributed / 6 unresolved**;
- deterministic bilingual reader/export: **complete-verified, QA PASS**;
- reader outputs: Markdown / standalone HTML / machine JSON + QA report + manifest;
- Reading Room payload: **complete-verified, QA PASS** — `{RR_PAYLOAD_BYTES:,}` bytes, SHA-256 `{RR_PAYLOAD_SHA}`;
- Reading Room site application: **not-applied**.

The booklet prints **11 numbered front-matter songs but no numbered screenplay scenes**. Reader/integration data therefore preserves songs 1–11 as actual source numbering while `raja-rani-s001`–`s058` remain archival navigation only.

Final QA also permanently removes the old T055/T056 duplicate derivative ownership: scene 55 has 25 immutable dialogue records, scene 56 has 5, and old duplicate `s055-d026`–`s055-d030` IDs are invalid.

**Next:** no required Raja Rani work remains in this repository. Apply the verified Reading Room payload in the separate public-site implementation repository only when that repository is explicitly authorized for modification.

"""
    text = replace_regex(text, r"## ராஜா ராணி status\n.*?(?=## மந்திரி குமாரி status\n)", section, "root README Raja Rani section")
    write(path, text)


def sync_master_handover() -> None:
    path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    text = read(path)
    tail = f"""## 13. Current high-level project checkpoint — 2026-09-03

- **Parasakthi** — complete-verified canonical/structured English reader work.
- **Tirumbippaar!** — complete-verified Tamil, scene/dialogue/character/song disposition, English translation, reader QA and deterministic EPUB package QA.
- **Manohara** — complete-verified Tamil, 57/57 scenes, 983 dialogue records and 1,190 English units; deterministic reader/export QA PASS; Reading Room integration ready.
- **Kalaignar Thirai Isai Paadalgal** — 54/54 verified Tamil and English songs; reader/export and Reading Room payload QA PASS; site not applied.
- **Manthiri Kumari** — source intake/structural mapping complete for the 14-page story-and-song booklet; canonical Tamil first pass remains its next source-processing phase.
- **Raja Rani** — 79/79 source pages and 70/70 screenplay pages verified; 58/58 scene derivatives; 1,071 immutable dialogue records; 80/80 labels / 44 entities; screenplay English 58/58 at 1,236 units; numbered-song English 11/11 at 67 sections / 181 mapped line-cues; deterministic bilingual reader/export QA PASS; Reading Room payload QA PASS; site application not applied.

`data/works.json`, root README, work metadata/handover and this master handover are synchronized to this checkpoint.

---

## 14. Raja Rani downstream disposition

No required Raja Rani production work remains inside `pugazg/kalaignar-cinema-works`.

Its verified Reading Room payload is:

`works/raja-rani/integrations/reading-room/reading-room.json`

Payload SHA-256: `{RR_PAYLOAD_SHA}`.

Only when the separate Kalaignar Digital Library / Reading Room implementation repository is explicitly authorized for modification should that payload be applied there. The public site must preserve source-numbered songs separately from archival-only screenplay scene navigation, retain provenance, and keep song authorship/performance-link evidence tiers unchanged.

For repository-internal work, continue with another work's documented next activity rather than reopening Raja Rani solely to create an additional standalone format.
"""
    text = replace_regex(text, r"## 13\. Current high-level project checkpoint — 2026-09-03\n.*\Z", tail, "master handover tail")
    write(path, text)


def sync_status_audit() -> None:
    path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
    text = f"""# Kalaignar Cinema Works — Status Consistency Audit

Audit date: 2026-09-03  
Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`

## Scope

This audit reconciles current repository-wide status mirrors with the authoritative work checkpoints for all six registered works. `data/works.json`, root README, project handover and active work-local metadata/handovers must agree before a major phase is considered closed.

## Result

**PASS — current status mirrors synchronized across all six works.**

## Current work matrix

| Work | Source/Tamil | Structured text | English | Reader / integration |
|---|---|---|---|---|
| Parasakthi | 54/54 canonical pages verified | 46 observed scenes / 642 dialogue records | 769 verified units | reader/export QA PASS |
| Tirumbippaar! | 104/104 canonical pages verified | 93/93 scenes / 1,040 dialogue records | 1,321 verified units | reader/export + deterministic EPUB QA PASS |
| Manohara | 82/82 canonical pages verified | 57/57 scenes / 983 dialogue records | 1,190 verified units | reader/export QA PASS; Reading Room ready |
| Kalaignar Thirai Isai Paadalgal | 54/54 numbered Tamil songs verified | 54 song records | 54/54 songs / 1,105 line-cues | reader/export + Reading Room payload QA PASS; site not applied |
| Manthiri Kumari | intake/mapping complete; Tamil first pass not started | blocked pending verified Tamil | blocked | next: canonical Tamil PDF2–13 |
| Raja Rani | 79/79 source pages; 70/70 screenplay pages verified | 58/58 scenes / 1,071 dialogue records / 80 labels / 44 entities | screenplay 1,236 units + 11/11 songs / 181 song line-cues | bilingual reader QA PASS + Reading Room payload QA PASS; site not applied |

## Raja Rani final reconciliation

- source pages: **79/79 verified**;
- screenplay pages: **70/70 verified**;
- archival scenes: **58/58**, blocked 0;
- immutable dialogue records: **1,071**;
- exact labels / entities: **80/80 / 44**;
- screenplay English: **58/58 scenes / 1,236 units / 1,071 links**;
- numbered-song English: **11/11 / 67 sections / 181 Tamil-English line-cues**;
- deterministic bilingual reader/export: **QA PASS** over **200 authoritative inputs**;
- reader Markdown SHA-256: `{READER_MD_SHA}`;
- reader HTML SHA-256: `{READER_HTML_SHA}`;
- reader JSON SHA-256: `{READER_JSON_SHA}`;
- Reading Room payload: **QA PASS**, **{RR_PAYLOAD_BYTES:,} bytes**, SHA-256 `{RR_PAYLOAD_SHA}`;
- site application: **not-applied**.

Permanent safeguards remain unchanged: T055/T056 duplicate IDs are absent; songs 3/5/6/7/8 remain later-anthology Kalaignar-attributed, songs 1/2/4/9/10/11 unresolved; scene 58 → song 11 remains review-level; screenplay ordinals remain archival navigation only.

## Repository-wide synchronization rule

A major phase is not complete while an active current-status document still advertises the prior checkpoint. At phase closure synchronize work-local metadata/README/index/QA/handover plus `data/works.json`, root README, master handover/status audit and any shared guide changed by reusable lessons. Historical batch records may retain their historical state when clearly labelled historical.

## Conclusion

Raja Rani has **no required repository-internal archival, translation, reader/export or Reading Room-payload work remaining**. Its payload is ready for the separate public-site implementation repository only when that repository is explicitly authorized. No public-site application has been performed by this repository work.
"""
    write(path, text)


def stale_assertions() -> None:
    current_paths = [
        WORK / "metadata.yaml",
        WORK / "README.md",
        WORK / "translations" / "README.md",
        WORK / "translations" / "index.json",
        WORK / "translations" / "songs" / "index.json",
        WORK / "songs" / "index.json",
        ROOT / "docs" / "HANDOVER_RAJA_RANI.md",
        ROOT / "docs" / "NEXT_CHAT_PROMPT_RAJA_RANI.md",
        ROOT / "README.md",
        ROOT / "data" / "works.json",
        ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md",
        ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md",
    ]
    forbidden = [
        "whole-work bilingual reader/export: **not started**",
        "Reading Room integration: **not started**",
        "english_reader_export: not-started",
        '"reader_export": "not-started"',
        '"reading_room_integration": "not-started"',
        "Build and QA a deterministic Raja Rani whole-work bilingual reader/export",
        "Translate the **11 numbered front-matter song bodies**",
        "scene 1 / 50 eligible verified scenes",
        "892 immutable records",
    ]
    registry_path = ROOT / "data" / "works.json"
    registry = json.loads(read(registry_path))
    matches = [work for work in registry if work.get("id") == "raja-rani"]
    if len(matches) != 1:
        raise RuntimeError("data/works.json must contain exactly one raja-rani entry during stale assertion")
    raja_rani_text = json.dumps(matches[0], ensure_ascii=False)
    registry_forbidden = [
        '"reader_export": "not-started"',
        '"reading_room_integration": "not-started"',
    ]
    for needle in registry_forbidden:
        if needle in raja_rani_text:
            raise RuntimeError(f"stale Raja Rani registry state remains: {needle}")

    non_registry_forbidden = [needle for needle in forbidden if needle not in registry_forbidden]
    for current_path in current_paths:
        if current_path == registry_path:
            continue
        current_text = read(current_path)
        for needle in non_registry_forbidden:
            if needle in current_text:
                raise RuntimeError(
                    f"stale current-state phrase remains in {current_path.relative_to(ROOT)}: {needle}"
                )


def main() -> int:
    metadata_text = read(WORK / "metadata.yaml")
    already_final = all(
        marker in metadata_text
        for marker in (
            "structured_derivatives: complete-verified-reader-and-reading-room-payload",
            "english_reader_export: complete-verified",
            "reading_room_integration: payload-complete-verified",
            "reading_room_site_application: not-applied",
        )
    )
    if already_final:
        stale_assertions()
        print("RAJA RANI FINAL REPOSITORY STATUS SYNC: PASS (already synchronized)")
        return 0

    sync_metadata()
    sync_work_readme()
    sync_translation_readme()
    sync_json_indexes()
    sync_song_docs()
    sync_edition_docs()
    sync_handovers()
    sync_registry()
    sync_root_readme()
    sync_master_handover()
    sync_status_audit()
    stale_assertions()
    print("RAJA RANI FINAL REPOSITORY STATUS SYNC: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
