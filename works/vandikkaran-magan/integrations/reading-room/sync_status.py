#!/usr/bin/env python3
"""Synchronize current status mirrors after Vandikkaran Magan Reading Room payload PASS."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "vandikkaran-magan"
INTEGRATION = WORK / "integrations" / "reading-room"
MANIFEST = INTEGRATION / "manifest.json"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
assert manifest["status"] == "PASS"
assert manifest["site_application_status"] == "not-applied"
assert manifest["checkpoint"]["screenplay_scenes"] == 72
assert manifest["checkpoint"]["english_units"] == 1181
assert manifest["checkpoint"]["immutable_dialogue_links"] == 773
assert manifest["checkpoint"]["source_unlabelled_spoken_units"] == 27
assert manifest["checkpoint"]["cross_page_units"] == 58
assert manifest["checkpoint"]["performance_occurrence_identities"] == 9
assert manifest["checkpoint"]["performance_linked_units"] == 66

PAYLOAD_SHA = manifest["output"]["sha256"]
PAYLOAD_BYTES = manifest["output"]["bytes"]
INPUT_SHA = manifest["authoritative_input_aggregate_sha256"]
INPUT_FILES = manifest["authoritative_input_files"]

FINAL_NEXT = (
    "No required repository-internal `வண்டிக்காரன் மகன்` production work remains. Keep canonical Tamil, scene, "
    "reconciled immutable dialogue, character/entity, song/performance, English translation, reader/export and "
    "Reading Room payload layers closed. Apply `works/vandikkaran-magan/integrations/reading-room/reading-room.json` "
    "in the separate Kalaignar Digital Library / Reading Room implementation repository only when that repository "
    "is explicitly authorized for modification; fetch its live state first and use a fail-closed importer pinned "
    "to this verified payload/manifest. Site application remains not-applied here."
)


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_section(text: str, start_heading: str, next_heading: str, replacement: str) -> str:
    pattern = re.compile(rf"{re.escape(start_heading)}.*?(?=\n{re.escape(next_heading)})", re.S)
    new, count = pattern.subn(replacement.rstrip(), text, count=1)
    assert count == 1, f"Could not replace section {start_heading!r}"
    return new


# Work metadata: replace the downstream tail as one authoritative current block.
metadata_path = WORK / "metadata.yaml"
metadata = metadata_path.read_text(encoding="utf-8")
metadata = re.sub(
    r"  reading_room_integration:.*?\nnext_action:.*?(?:\n|$)",
    "  reading_room_integration: payload-complete-verified\n"
    "  reading_room_payload_path: works/vandikkaran-magan/integrations/reading-room/reading-room.json\n"
    "  reading_room_qa: PASS\n"
    "  reading_room_qa_path: works/vandikkaran-magan/integrations/reading-room/QA_REPORT.md\n"
    "  reading_room_manifest_path: works/vandikkaran-magan/integrations/reading-room/manifest.json\n"
    f"  reading_room_payload_bytes: {PAYLOAD_BYTES}\n"
    f"  reading_room_payload_sha256: {PAYLOAD_SHA}\n"
    "  reading_room_site_application: not-applied\n"
    f"next_action: \"{FINAL_NEXT}\"\n",
    metadata,
    count=1,
    flags=re.S,
)
assert "reading_room_integration: payload-complete-verified" in metadata
write(metadata_path, metadata)

# Work README.
readme_path = WORK / "README.md"
readme = readme_path.read_text(encoding="utf-8")
readme = readme.split("## Current verified state", 1)[0] + f"""## Current verified state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 unresolved**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue authority: **773 records / 38 exact labels / QA PASS** — **744/744 legacy IDs preserved + 29 append-only repairs**;
- character/entity index: **32 entities — 15 characters / 14 roles / 3 collectives / 38/38 labels / 773/773 records / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS** — 6 bounded Tamil bodies + 3 cue-only;
- item-level lyric authorship: **0 source-attributed / 6 unresolved / 3 not-applicable**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance occurrences / 0 inferred speakers**;
- English reader/export: **COMPLETE-VERIFIED / QA PASS** — deterministic Markdown, HTML and JSON under `editions/en/`;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS** — `integrations/reading-room/reading-room.json`;
- Reading Room payload bytes: **{PAYLOAD_BYTES:,}**;
- Reading Room payload SHA-256: `{PAYLOAD_SHA}`;
- Reading Room authoritative-input aggregate: **{INPUT_FILES} files / `{INPUT_SHA}`**;
- separate Reading Room site application: **not-applied**.

## Exact next activity

> **{FINAL_NEXT}**
"""
write(readme_path, readme)

# Work handover.
handover_path = WORK / "PROJECT_HANDOVER.md"
handover = handover_path.read_text(encoding="utf-8")
handover = handover.split("## Durable closed state", 1)[0] + f"""## Durable closed state

- canonical source: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps**;
- dialogue authority: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**; legacy IDs **744/744 preserved**, append-only repairs **29**, action-only exclusions **2**;
- character/entity: **32 entities / 38/38 labels / 773/773 dialogue records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**; 6 bounded bodies / 3 cue-only / 0 source-attributed + 6 unresolved item-level lyric authorships;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 immutable links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance identities / 0 inferred speakers**;
- reader/export: **COMPLETE-VERIFIED / QA PASS** — Markdown / HTML / JSON / manifest under `editions/en/`;
- Reading Room integration payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS** — **{PAYLOAD_BYTES:,} bytes / SHA-256 `{PAYLOAD_SHA}`**;
- Reading Room payload input aggregate: **{INPUT_FILES} authoritative files / SHA-256 `{INPUT_SHA}`**;
- separate public-site application: **not-applied**.

Do not reopen or rewrite closed Tamil, scene, immutable dialogue-record, character-mapping, song/performance, translation, reader or Reading Room payload authority without new direct contradictory source evidence. Historical 744 counts refer only to the preserved pre-reconciliation ID set.

## Exact next activity

> **{FINAL_NEXT}**
"""
write(handover_path, handover)

# Next-chat prompt becomes a closed checkpoint prompt rather than a stale production instruction.
next_path = WORK / "NEXT_CHAT_PROMPT.md"
write(next_path, f"""# Next Chat Prompt — வண்டிக்காரன் மகன் / repository-internal closure

Continue in `pugazg/kalaignar-cinema-works`, branch `main`, work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only.

## Durable closed state

- canonical Tamil: **87/87 COMPLETE-VERIFIED**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / QA PASS**;
- character/entity: **32 entities / 38/38 labels / 773/773 records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- English translation: **72/72 COMPLETE-VERIFIED / 1,181 units / 773 links / 27 source-unlabelled / 58 cross-page / 9/9 performance identities**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS**;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**;
- payload: `integrations/reading-room/reading-room.json` — **{PAYLOAD_BYTES:,} bytes / SHA-256 `{PAYLOAD_SHA}`**;
- payload manifest: `integrations/reading-room/manifest.json` — authoritative-input aggregate `{INPUT_SHA}`;
- separate Reading Room implementation repository: **not modified / not authorized by this checkpoint**.

Do not reopen closed source or derivative layers without new direct contradictory source evidence.

## Exact next activity

> **{FINAL_NEXT}**
""")

# Structural mapping downstream closure.
mapping_path = WORK / "mapping.md"
mapping = mapping_path.read_text(encoding="utf-8")
if "## Exact next activity" in mapping:
    mapping = mapping.split("## Exact next activity", 1)[0]
mapping += f"""## Downstream closure

- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS**;
- source-linked Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS — {PAYLOAD_BYTES:,} bytes / SHA-256 `{PAYLOAD_SHA}`**;
- separate site application: **not-applied**.

## Exact next activity

**{FINAL_NEXT}**
"""
write(mapping_path, mapping)

# Closed upstream layer mirrors should not advertise obsolete English batches.
transcription_path = WORK / "transcription" / "README.md"
transcription = transcription_path.read_text(encoding="utf-8").split("## Downstream state", 1)[0] + f"""## Downstream state

The reconciled immutable dialogue authority is **773 records / 38 exact source labels / QA PASS**, preserving all **744/744** legacy IDs and adding **29** append-only repaired IDs. Character/entity coverage is **773/773**; song/performance is **9/9** source-only QA PASS; English translation is **72/72 COMPLETE-VERIFIED**; reader/export and Reading Room payload are **QA PASS**. Canonical Tamil remains unchanged.

**Next:** {FINAL_NEXT}
"""
write(transcription_path, transcription)

for relative, heading, body in [
    ("dialogues/README.md", "## Downstream", f"Character/entity and song/performance layers are reconciled and closed against this 773-record authority. English translation is **72/72 COMPLETE-VERIFIED**; reader/export and Reading Room payload are **QA PASS**.\n\n**Next:** {FINAL_NEXT}"),
    ("characters/README.md", "## Downstream", f"Song/performance is closed at 9/9 source-visible occurrences. English translation is **72/72 COMPLETE-VERIFIED**; reader/export and Reading Room payload are **QA PASS**.\n\n**Next:** {FINAL_NEXT}"),
]:
    path = WORK / relative
    text = path.read_text(encoding="utf-8")
    text = text.split(heading, 1)[0] + heading + "\n\n" + body + "\n"
    write(path, text)

songs_path = WORK / "songs" / "README.md"
songs = songs_path.read_text(encoding="utf-8")
cut = songs.find("**Next:**")
if cut != -1:
    songs = songs[:cut]
songs += f"**Next:** {FINAL_NEXT}\n"
write(songs_path, songs)

# Structured repository registry.
works_path = ROOT / "data" / "works.json"
works = json.loads(works_path.read_text(encoding="utf-8"))
entry = next(x for x in works if x.get("id") == "vandikkaran-magan")
sd = entry.setdefault("structured_derivatives", {})
sd.update({
    "english_translation": "complete-verified",
    "reader_export": "complete-verified",
    "reading_room_integration": "payload-complete-verified",
    "next_structured_derivative": None,
    "translation_index_path": "works/vandikkaran-magan/translations/index.json",
    "translation_scenes_verified": 72,
    "translation_units": 1181,
    "translation_verified_units": 1181,
    "translation_review_units": 0,
    "translation_draft_units": 0,
    "translation_unit_kind_counts": EXPECTED_KINDS if False else {
        "dialogue": 800,
        "performance_cue": 10,
        "song": 53,
        "stage_direction": 316,
        "written_text": 2,
    },
    "translation_dialogue_source_records_linked": 773,
    "translation_source_unlabelled_spoken_units": 27,
    "translation_cross_page_units": 58,
    "translation_performance_occurrence_links": 9,
    "translation_latest_batch_qa_path": "works/vandikkaran-magan/translations/batch-061-072-qa.json",
    "translation_final_qa_path": "works/vandikkaran-magan/translations/FINAL_TRANSLATION_QA.md",
    "english_reader_edition": "complete-verified",
    "english_reader_edition_directory": "works/vandikkaran-magan/editions/en",
    "english_reader_qa": "PASS",
    "english_reader_qa_units": 1181,
    "english_reader_qa_dialogue_links": 773,
    "english_reader_qa_source_unlabelled_spoken_units": 27,
    "english_reader_qa_cross_page_units": 58,
    "english_reader_qa_performance_occurrence_links": 9,
    "reading_room_payload": "complete-verified",
    "reading_room_payload_path": "works/vandikkaran-magan/integrations/reading-room/reading-room.json",
    "reading_room_payload_qa": "PASS",
    "reading_room_payload_qa_path": "works/vandikkaran-magan/integrations/reading-room/QA_REPORT.md",
    "reading_room_payload_manifest_path": "works/vandikkaran-magan/integrations/reading-room/manifest.json",
    "reading_room_payload_bytes": PAYLOAD_BYTES,
    "reading_room_payload_sha256": PAYLOAD_SHA,
    "reading_room_site_application": "not-applied",
})
entry["next_action"] = None
write(works_path, json.dumps(works, ensure_ascii=False, indent=2))

# Root README: replace only the Vandikkaran Magan current-status section.
root_readme_path = ROOT / "README.md"
root_readme = root_readme_path.read_text(encoding="utf-8")
root_section = f"""## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is now a **complete-verified Tamil + structured + English reader + Reading Room payload archival work**.

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved / 3 not-applicable**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance occurrences**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS**;
- Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS — {PAYLOAD_BYTES:,} bytes / SHA-256 `{PAYLOAD_SHA}`**;
- Reading Room payload authoritative-input aggregate: **{INPUT_FILES} files / SHA-256 `{INPUT_SHA}`**;
- site application: **not-applied**.

**Next:** {FINAL_NEXT}
"""
root_readme = replace_section(root_readme, "## வண்டிக்காரன் மகன் status", "## நாம் status", root_section)
write(root_readme_path, root_readme)

# Master handover: update the high-level row and the active-production statement.
master_path = ROOT / "docs" / "HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
master = master_path.read_text(encoding="utf-8")
master = re.sub(
    r"- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*",
    f"- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72**; dialogues **773 / 38 labels / reconciled QA PASS**; characters **32 / 38/38 / 773/773**; song/performance **9/9 source-only QA PASS**; English **72/72 COMPLETE-VERIFIED / 1,181 units / 773 dialogue links / 27 source-unlabelled / 58 cross-page / 9/9 performance identities**; reader/export **QA PASS**; Reading Room payload **QA PASS — {PAYLOAD_BYTES:,} bytes / `{PAYLOAD_SHA}`**; site not applied.",
    master,
    count=1,
)
master = re.sub(
    r"Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*",
    "Ammayappan and Naam remain closed at their recorded checkpoints. **Vandikkaran Magan now has no required repository-internal production phase remaining: source/Tamil, structured derivatives, English translation, deterministic reader/export and source-linked Reading Room payload are complete-verified / QA PASS. The separate Reading Room site remains not-applied and requires explicit authorization before modification.**",
    master,
    count=1,
    flags=re.S,
)
write(master_path, master)

# Status audit: result, matrix row and current checkpoint section.
audit_path = ROOT / "docs" / "STATUS_CONSISTENCY_AUDIT.md"
audit = audit_path.read_text(encoding="utf-8")
audit = re.sub(
    r"\*\*PASS for the current repository-wide checkpoint\.\*\* Vandikkaran Magan.*?All closed Tamil/scene/dialogue/character/song authorities remain unchanged\.",
    f"**PASS for the current repository-wide checkpoint.** Vandikkaran Magan is complete-verified through its deterministic source-linked Reading Room payload: **72/72 scenes / 1,181 English units / 773 immutable dialogue links / 27 source-unlabelled spoken units / 58 cross-page units / 9/9 performance identities**. Reader/export QA and Reading Room payload QA both PASS. Payload SHA-256 is `{PAYLOAD_SHA}` ({PAYLOAD_BYTES:,} bytes). All closed Tamil/scene/dialogue/character/song/translation/reader authorities remain unchanged and the separate site is not applied.",
    audit,
    count=1,
    flags=re.S,
)
audit = re.sub(
    r"\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*",
    f"| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 773 dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **72/72 COMPLETE-VERIFIED / 1,181 units / 773 dialogue links / 27 unlabelled / 58 cross-page / 9/9 performance IDs** | **reader/export + Reading Room payload QA PASS; site not applied** |",
    audit,
    count=1,
)
audit_section = f"""## Vandikkaran Magan current checkpoint

- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue index: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS** — 6 bounded bodies + 3 cue-only;
- item-level lyric authorship: **0 source-attributed / 6 unresolved / 3 not-applicable**;
- English translation: **72/72 COMPLETE-VERIFIED / WHOLE-WORK QA PASS — 1,181 units / 773 links / 27 source-unlabelled / 58 cross-page / 9/9 performance identities**;
- deterministic English reader/export: **COMPLETE-VERIFIED / QA PASS**;
- source-linked Reading Room payload: **PAYLOAD-COMPLETE-VERIFIED / QA PASS**;
- payload: `works/vandikkaran-magan/integrations/reading-room/reading-room.json` — **{PAYLOAD_BYTES:,} bytes / SHA-256 `{PAYLOAD_SHA}`**;
- payload authoritative-input aggregate: **{INPUT_FILES} files / SHA-256 `{INPUT_SHA}`**;
- site application: **not-applied**;
- upstream source/translation/reader mutation from payload generation: **0**.

**Next production phase:** {FINAL_NEXT}
"""
audit = replace_section(audit, "## Vandikkaran Magan current checkpoint", "## Naam current checkpoint", audit_section)
audit = re.sub(
    r"Vandikkaran Magan is the active production work\..*?(?=\n\n|$)",
    "Vandikkaran Magan repository-internal production is closed through Reading Room payload QA PASS; separate-site application remains not-applied and requires explicit authorization.",
    audit,
    flags=re.S,
)
write(audit_path, audit)

# Fail if the active VM mirrors still advertise the old pending payload phase.
active_paths = [
    metadata_path, readme_path, handover_path, next_path, mapping_path,
    transcription_path, WORK / "dialogues" / "README.md", WORK / "characters" / "README.md", songs_path,
    works_path, root_readme_path, master_path, audit_path,
]
for path in active_paths:
    text = path.read_text(encoding="utf-8")
    assert "Reading Room payload: **READY-NEXT" not in text, path
    assert "Reading Room payload: **not built**" not in text, path
    assert "reader/export and Reading Room: **BLOCKED" not in text, path

print("VANDIKKARAN MAGAN READING ROOM STATUS SYNC")
print("status= PASS")
print(f"payload_bytes= {PAYLOAD_BYTES}")
print(f"payload_sha256= {PAYLOAD_SHA}")
print("site_application_status= not-applied")
