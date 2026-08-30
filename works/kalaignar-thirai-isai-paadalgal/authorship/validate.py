#!/usr/bin/env python3
"""Fail-closed validator for the Kalaignar-authorship inclusion gate.

Checks that authorship/inclusion-evidence.json is a complete, internally
consistent, song-level register over every numbered lyric in the controlling
scan; that every record carries structured evidence items with full provenance
from every inspected witness; that the decision and inclusion rules hold for
every record independently of the stored values; that the 1989 cross-witness
mapping agrees with the committed deduplication audit; that the archival
attribution layer is untouched; and that authorship/public-inclusion.json is
exactly the manifest derived from the register, pinning the register's own
bytes and the source-main SHA the gate was adjudicated against.

Exit codes (repository validator contract):
  0  success
  1  data-integrity failure
  2  cannot validate (inputs missing or unreadable)

Usage:
  python3 authorship/validate.py            verify public-inclusion.json
  python3 authorship/validate.py --write    regenerate public-inclusion.json
"""

import hashlib
import json
import re
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = WORK / "authorship" / "inclusion-evidence.json"
MANIFEST_PATH = WORK / "authorship" / "public-inclusion.json"
INDEX_PATH = WORK / "songs" / "index.json"
METADATA_PATH = WORK / "metadata.yaml"
DEDUP_PATH = WORK / "songs" / "SOURCE_WITNESS_0065773_DEDUP.md"

EXPECTED_SONGS = 54
QUALIFYING_LEVELS = {"A", "B", "C"}
LEVELS = {"A", "B", "C", "D"}
DECISIONS = {"established-kalaignar", "established-other", "unresolved", "insufficient-evidence"}
SCOPES = {
    "song-specific", "collection-scoped-listed-song", "film-collective",
    "film-writing-credit", "implicit-collection-placement", "not-present-in-witness",
}
EFFECTS = {
    "supports-kalaignar", "supports-other", "limits-song-level-attribution", "neutral-provenance",
}
ITEM_FIELDS = [
    "source_identifier", "source_year_or_edition", "source_kind", "source_path_or_filename",
    "pdf_page_or_location", "printed_page_if_known", "attribution_scope",
    "attribution_as_printed_or_source_claim", "identity_basis", "evidence_level",
    "evidence_effect", "basis",
]
# Fields that may legitimately be null where the source prints no such value.
NULLABLE = {"printed_page_if_known", "attribution_as_printed_or_source_claim"}

CONTROLLING = "TVA_BOK_0065867"
WITNESS_1989 = "TVA_BOK_0065773"
ARCHIVAL_STATUS = "anthology-attributed"

errors = []


def cannot_validate(message):
    print("KALAIGNAR-AUTHORSHIP INCLUSION GATE")
    print("status= CANNOT-VALIDATE")
    print("reason=", message)
    sys.exit(2)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        cannot_validate(f"missing required input: {path.relative_to(WORK)}")
    except (OSError, ValueError) as exc:
        cannot_validate(f"unreadable input {path.relative_to(WORK)}: {exc}")


def serialise(payload):
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def parse_dedup_map(text):
    """section number -> current song number, from the committed cross-witness audit."""
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*`[^`]*`\s*\|\s*[0-9–-]+\s*\|\s*`song-(\d{3})\.md`", text, re.M)
    return {int(sec): int(song) for sec, song in rows}


def decide(items):
    """Recompute decision, conflict and inclusion from evidence items alone."""
    pos_k = [i for i in items
             if i.get("evidence_effect") == "supports-kalaignar" and i.get("evidence_level") in QUALIFYING_LEVELS]
    pos_o = [i for i in items
             if i.get("evidence_effect") == "supports-other" and i.get("evidence_level") in QUALIFYING_LEVELS]
    limiting = [i for i in items if i.get("evidence_effect") == "limits-song-level-attribution"]
    conflict = bool(pos_k and pos_o)
    if conflict:
        decision = "unresolved"
    elif pos_k:
        decision = "established-kalaignar"
    elif pos_o:
        decision = "established-other"
    elif limiting:
        decision = "unresolved"
    else:
        decision = "insufficient-evidence"
    return decision, conflict, decision == "established-kalaignar" and not conflict


def derive_manifest(evidence, register_sha256):
    included = [r for r in evidence["records"] if r["public_inclusion"]]
    counts = evidence["counts"]
    return {
        "work_id": evidence["work_id"],
        "manifest": "kalaignar-authorship-public-inclusion",
        "manifest_version": evidence["register_version"],
        "derived_from": "authorship/inclusion-evidence.json",
        "derivation": (
            "Every record in the evidence register whose public_inclusion is true, "
            "in ascending anthology song number. This file is generated; edit the "
            "evidence register and regenerate."
        ),
        "inclusion_rule": evidence["inclusion_rule"],
        "controlling_source_sha256": evidence["controlling_source"]["sha256"],
        "evidence_register_sha256": register_sha256,
        "source_main_sha": evidence["adjudicated_against_source_main_sha"],
        "witness_sha256": {
            w["identifier"]: w["sha256"] for w in evidence["witnesses"].values()
        },
        "decision_counts": {
            "established-kalaignar": counts["established_kalaignar"],
            "established-other": counts["established_other"],
            "unresolved": counts["unresolved"],
            "insufficient-evidence": counts["insufficient_evidence"],
        },
        "material_conflicts": counts["material_conflicts"],
        "songs_registered": counts["songs_registered"],
        "songs_included": len(included),
        "songs_withheld": counts["songs_registered"] - len(included),
        "withheld_note": (
            "Songs absent from this manifest are withheld for want of song-level "
            "evidence. Withholding is not a finding that the song is not Kalaignar's."
        ),
        "included_song_ids": [r["id"] for r in included],
        "withheld": [
            {"id": r["id"], "anthology_song_number": r["anthology_song_number"], "decision": r["decision"]}
            for r in evidence["records"] if not r["public_inclusion"]
        ],
    }


def main():
    write_mode = "--write" in sys.argv[1:]
    unknown = [a for a in sys.argv[1:] if a != "--write"]
    if unknown:
        cannot_validate(f"unrecognised arguments: {unknown}")

    raw_evidence = None
    try:
        raw_evidence = EVIDENCE_PATH.read_bytes()
    except (OSError, FileNotFoundError):
        cannot_validate("missing required input: authorship/inclusion-evidence.json")
    register_sha256 = hashlib.sha256(raw_evidence).hexdigest()

    evidence = load_json(EVIDENCE_PATH)
    index = load_json(INDEX_PATH)
    if not METADATA_PATH.exists():
        cannot_validate("missing required input: metadata.yaml")
    metadata_text = METADATA_PATH.read_text(encoding="utf-8")
    if not DEDUP_PATH.exists():
        cannot_validate("missing required input: songs/SOURCE_WITNESS_0065773_DEDUP.md")
    dedup_map = parse_dedup_map(DEDUP_PATH.read_text(encoding="utf-8"))
    if not dedup_map:
        cannot_validate("songs/SOURCE_WITNESS_0065773_DEDUP.md yielded no cross-witness mapping rows")

    for key in ("records", "witnesses", "counts", "inclusion_rule", "adjudicated_against_source_main_sha"):
        if key not in evidence:
            cannot_validate(f"inclusion-evidence.json is missing required top-level key {key!r}")
    records = evidence["records"]
    if not isinstance(records, list):
        cannot_validate("inclusion-evidence.json records is not an array")

    # ----- pins ------------------------------------------------------------
    sha = evidence.get("controlling_source", {}).get("sha256")
    if sha != index.get("source_sha256"):
        errors.append(
            f"controlling_source.sha256 {sha!r} != songs/index.json source_sha256 {index.get('source_sha256')!r}"
        )
    if sha and f'sha256: "{sha}"' not in metadata_text:
        errors.append("controlling_source.sha256 is not the sha256 recorded in metadata.yaml")
    main_sha = evidence["adjudicated_against_source_main_sha"]
    if not (isinstance(main_sha, str) and re.fullmatch(r"[0-9a-f]{40}", main_sha)):
        errors.append(f"adjudicated_against_source_main_sha is not a 40-character hex SHA: {main_sha!r}")
    for name, witness in evidence["witnesses"].items():
        if not re.fullmatch(r"[0-9a-f]{64}", witness.get("sha256", "")):
            errors.append(f"witnesses.{name}.sha256 is not a 64-character hex SHA-256")

    # ----- 1989 cross-witness mapping agrees with the committed audit -------
    expected_1989 = {}
    for section, song in dedup_map.items():
        expected_1989.setdefault(song, []).append(section)
    for song in expected_1989:
        expected_1989[song].sort()

    # ----- completeness over the numbered corpus ---------------------------
    if len(records) != EXPECTED_SONGS:
        errors.append(f"register holds {len(records)} records, expected {EXPECTED_SONGS}")
    index_records = {r["anthology_song_number"]: r for r in index.get("records", [])}
    if len(index_records) != EXPECTED_SONGS:
        errors.append(f"songs/index.json holds {len(index_records)} records, expected {EXPECTED_SONGS}")

    # ----- archival attribution layer must be untouched --------------------
    stray = sorted(
        r["anthology_song_number"] for r in index.get("records", [])
        if r.get("attribution_status") != ARCHIVAL_STATUS
    )
    if stray:
        errors.append(
            f"songs/index.json attribution_status is no longer {ARCHIVAL_STATUS!r} for songs {stray}; "
            "this gate must not alter the archival attribution layer"
        )

    seen = []
    for position, rec in enumerate(records, 1):
        number = rec.get("anthology_song_number")
        seen.append(number)
        label = rec.get("id", f"position {position}")
        if number != position:
            errors.append(f"{label}: register is not in ascending song order at position {position}")
            continue
        tag = f"song {number:03d}"

        source = index_records.get(number)
        if source is None:
            errors.append(f"{tag}: no songs/index.json record for this song")
            continue
        if rec.get("id") != source["id"]:
            errors.append(f"{tag}: id {rec.get('id')!r} != index id {source['id']!r}")
        for field, key in (("film_title_ta", "film_title_ta"),
                           ("lyric_title_as_printed", "lyric_title"),
                           ("lyric_pdf_pages", "lyric_pdf_pages")):
            if rec.get(field) != source[key]:
                errors.append(f"{tag}: {field} {rec.get(field)!r} != index {key} {source[key]!r}")

        items = rec.get("evidence_items")
        if not isinstance(items, list) or not items:
            errors.append(f"{tag}: evidence_items is missing or empty")
            continue

        for ordinal, item in enumerate(items, 1):
            if not isinstance(item, dict):
                errors.append(f"{tag}: evidence item {ordinal} is not an object")
                continue
            for field in ITEM_FIELDS:
                if field not in item:
                    errors.append(f"{tag}: evidence item {ordinal} is missing {field}")
                elif item[field] is None and field not in NULLABLE:
                    errors.append(f"{tag}: evidence item {ordinal} has null {field}")
                elif field not in NULLABLE and isinstance(item[field], str) and not item[field].strip():
                    errors.append(f"{tag}: evidence item {ordinal} has empty {field}")
            if item.get("evidence_level") not in LEVELS:
                errors.append(f"{tag}: evidence item {ordinal} has unknown evidence_level "
                              f"{item.get('evidence_level')!r}")
            if item.get("attribution_scope") not in SCOPES:
                errors.append(f"{tag}: evidence item {ordinal} has unknown attribution_scope "
                              f"{item.get('attribution_scope')!r}")
            if item.get("evidence_effect") not in EFFECTS:
                errors.append(f"{tag}: evidence item {ordinal} has unknown evidence_effect "
                              f"{item.get('evidence_effect')!r}")
            if not isinstance(item.get("basis"), str) or len(item.get("basis", "").strip()) < 40:
                errors.append(f"{tag}: evidence item {ordinal} basis is missing or too thin to audit")
            if item.get("source_identifier") not in {CONTROLLING, WITNESS_1989}:
                errors.append(f"{tag}: evidence item {ordinal} cites unknown source "
                              f"{item.get('source_identifier')!r}")
            # A qualifying positive item must be song-specific and name its printed claim.
            if (item.get("evidence_effect") == "supports-kalaignar"
                    and item.get("evidence_level") in QUALIFYING_LEVELS):
                if item.get("attribution_scope") != "song-specific":
                    errors.append(f"{tag}: evidence item {ordinal} qualifies for inclusion at level "
                                  f"{item.get('evidence_level')} but its scope is "
                                  f"{item.get('attribution_scope')!r}, not song-specific")
                if not item.get("attribution_as_printed_or_source_claim"):
                    errors.append(f"{tag}: evidence item {ordinal} qualifies for inclusion without recording "
                                  "the printed attribution it rests on")
            # established-other requires a named other author.
            if item.get("evidence_effect") == "supports-other":
                claim = item.get("attribution_as_printed_or_source_claim") or ""
                if not claim.strip():
                    errors.append(f"{tag}: evidence item {ordinal} supports another writer without naming one")

        # 2024 evidence must be present for every record.
        if not any(i.get("source_identifier") == CONTROLLING for i in items if isinstance(i, dict)):
            errors.append(f"{tag}: no evidence item from the controlling 2024 source")

        # 1989 provenance must agree with the committed mapping.
        sections = rec.get("witness_1989_sections")
        if not isinstance(sections, list):
            errors.append(f"{tag}: witness_1989_sections is missing or not a list")
        else:
            if sections != expected_1989.get(number, []):
                errors.append(f"{tag}: witness_1989_sections {sections} != committed cross-witness mapping "
                              f"{expected_1989.get(number, [])}")
            items_1989 = [i for i in items if isinstance(i, dict) and i.get("source_identifier") == WITNESS_1989]
            if not items_1989:
                errors.append(f"{tag}: no evidence item records the 1989 witness (presence or absence)")
            elif sections:
                if any(i.get("attribution_scope") == "not-present-in-witness" for i in items_1989):
                    errors.append(f"{tag}: mapped to 1989 sections {sections} but an item claims it is absent")
                for i in items_1989:
                    loc = i.get("pdf_page_or_location") or ""
                    if not any(f"section {s}" in loc for s in sections) and "contents" not in loc:
                        errors.append(f"{tag}: 1989 evidence item does not cite a mapped section location")
            else:
                if not any(i.get("attribution_scope") == "not-present-in-witness" for i in items_1989):
                    errors.append(f"{tag}: absent from the 1989 witness but no absence item is recorded")

        # Decision, conflict and inclusion are recomputed, never trusted.
        decision, conflict, included = decide([i for i in items if isinstance(i, dict)])
        if rec.get("decision") not in DECISIONS:
            errors.append(f"{tag}: unknown decision {rec.get('decision')!r}")
        elif rec.get("decision") != decision:
            errors.append(f"{tag}: decision {rec.get('decision')!r} contradicts its evidence items, "
                          f"which give {decision!r}")
        if rec.get("material_conflict") is not conflict:
            errors.append(f"{tag}: material_conflict={rec.get('material_conflict')!r} contradicts its "
                          f"evidence items, which give {conflict}")
        if not isinstance(rec.get("public_inclusion"), bool):
            errors.append(f"{tag}: public_inclusion is not a boolean")
        elif rec.get("public_inclusion") is not included:
            errors.append(f"{tag}: public_inclusion={rec.get('public_inclusion')} contradicts the inclusion "
                          f"rule, which gives {included}")
        if rec.get("public_inclusion") and conflict:
            errors.append(f"{tag}: included despite a declared material conflict")
        if rec.get("public_inclusion") and rec.get("decision") in {"unresolved", "insufficient-evidence"}:
            errors.append(f"{tag}: included while decided {rec.get('decision')!r}")

        basis = rec.get("decision_basis")
        if not isinstance(basis, str) or len(basis.strip()) < 40:
            errors.append(f"{tag}: decision_basis is missing or too thin to audit")
        if rec.get("decision") in {"unresolved", "insufficient-evidence"} and isinstance(basis, str):
            if re.search(r"not\s+(?:a\s+)?Kalaignar['’]?s?\b", basis) and "not a finding" not in basis:
                errors.append(f"{tag}: {rec.get('decision')} basis reads as a finding of non-authorship")

    if sorted(seen) != list(range(1, EXPECTED_SONGS + 1)):
        errors.append("register does not cover songs 001-054 exactly once each")

    # ----- declared counts must match the records --------------------------
    tally = {name: 0 for name in DECISIONS}
    for rec in records:
        if rec.get("decision") in tally:
            tally[rec["decision"]] += 1
    item_total = sum(len(r.get("evidence_items") or []) for r in records)
    declared = evidence.get("counts", {})
    for key, value in (
        ("songs_registered", len(records)),
        ("established_kalaignar", tally["established-kalaignar"]),
        ("established_other", tally["established-other"]),
        ("unresolved", tally["unresolved"]),
        ("insufficient_evidence", tally["insufficient-evidence"]),
        ("material_conflicts", sum(1 for r in records if r.get("material_conflict"))),
        ("proposed_public_inclusion", sum(1 for r in records if r.get("public_inclusion"))),
        ("evidence_items_total", item_total),
    ):
        if declared.get(key) != value:
            errors.append(f"counts.{key} is {declared.get(key)!r}, records give {value}")

    # ----- derived manifest ------------------------------------------------
    try:
        expected_manifest = serialise(derive_manifest(evidence, register_sha256))
    except (KeyError, TypeError) as exc:
        cannot_validate(f"cannot derive the manifest from the register: {exc}")
    if write_mode:
        MANIFEST_PATH.write_text(expected_manifest, encoding="utf-8")
    elif not MANIFEST_PATH.exists():
        cannot_validate("missing required input: authorship/public-inclusion.json")
    else:
        actual = MANIFEST_PATH.read_text(encoding="utf-8")
        if actual != expected_manifest:
            detail = ""
            try:
                stored = json.loads(actual).get("evidence_register_sha256")
                if stored != register_sha256:
                    detail = (f" (its evidence_register_sha256 {stored!r} is stale; the register now hashes to "
                              f"{register_sha256})")
            except ValueError:
                detail = " (it is not readable JSON)"
            errors.append(
                "authorship/public-inclusion.json is not the byte-exact derivation of the evidence register"
                + detail + "; regenerate with --write"
            )

    print("KALAIGNAR-AUTHORSHIP INCLUSION GATE")
    print("status=", "PASS" if not errors else "FAIL")
    print("songs_registered=", len(records))
    print("decision_counts=", json.dumps(tally, ensure_ascii=False, sort_keys=True))
    print("material_conflicts=", sum(1 for r in records if r.get("material_conflict")))
    print("evidence_items=", item_total)
    print("proposed_public_inclusion=", sum(1 for r in records if r.get("public_inclusion")))
    print("evidence_register_sha256=", register_sha256)
    print("source_main_sha=", evidence.get("adjudicated_against_source_main_sha"))
    print("manifest_mode=", "written" if write_mode else "verified")
    if errors:
        print("errors=")
        for err in errors:
            print(" -", err)
        sys.exit(1)
    print("errors= []")
    sys.exit(0)


if __name__ == "__main__":
    main()
