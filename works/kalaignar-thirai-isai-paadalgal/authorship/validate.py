#!/usr/bin/env python3
"""Fail-closed validator for the Kalaignar-authorship inclusion gate.

Checks that authorship/inclusion-evidence.json is a complete, internally
consistent, song-level register over every numbered lyric in the controlling
scan, that it agrees with songs/index.json and metadata.yaml, and that
authorship/public-inclusion.json is exactly the manifest derived from it.

Exit codes (repository validator contract):
  0  success
  1  data-integrity failure
  2  cannot validate (inputs missing or unreadable)

Usage:
  python3 authorship/validate.py            verify public-inclusion.json
  python3 authorship/validate.py --write    regenerate public-inclusion.json
"""

import json
import re
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = WORK / "authorship" / "inclusion-evidence.json"
MANIFEST_PATH = WORK / "authorship" / "public-inclusion.json"
INDEX_PATH = WORK / "songs" / "index.json"
METADATA_PATH = WORK / "metadata.yaml"

EXPECTED_SONGS = 54
INCLUDING_DECISIONS = {"established-kalaignar"}
QUALIFYING_LEVELS = {"A", "B", "C"}
DECISIONS = {
    "established-kalaignar",
    "established-other",
    "unresolved",
    "insufficient-evidence",
}
MATCH_KINDS = {
    "exact",
    "prefix-variant",
    "punctuation-variant",
    "spelling-variant",
    "spacing-variant",
    "internal-line",
    "collective-credit-no-per-song-mapping",
    "no-film-song-list-printed",
}

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
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def derive_manifest(evidence):
    included = [r for r in evidence["records"] if r["public_inclusion"]]
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
        "songs_registered": evidence["counts"]["songs_registered"],
        "songs_included": len(included),
        "songs_withheld": evidence["counts"]["songs_registered"] - len(included),
        "withheld_note": (
            "Songs absent from this manifest are withheld for want of song-level "
            "evidence. Withholding is not a finding that the song is not Kalaignar's."
        ),
        "included_song_ids": [r["id"] for r in included],
        "withheld": [
            {
                "id": r["id"],
                "anthology_song_number": r["anthology_song_number"],
                "decision": r["decision"],
            }
            for r in evidence["records"]
            if not r["public_inclusion"]
        ],
    }


def main():
    write_mode = "--write" in sys.argv[1:]
    unknown = [a for a in sys.argv[1:] if a != "--write"]
    if unknown:
        cannot_validate(f"unrecognised arguments: {unknown}")

    evidence = load_json(EVIDENCE_PATH)
    index = load_json(INDEX_PATH)
    if not METADATA_PATH.exists():
        cannot_validate("missing required input: metadata.yaml")
    metadata_text = METADATA_PATH.read_text(encoding="utf-8")

    records = evidence.get("records")
    if not isinstance(records, list):
        cannot_validate("inclusion-evidence.json has no records array")

    # ----- pin the register to the controlling scan ------------------------
    sha = evidence.get("controlling_source", {}).get("sha256")
    if sha != index.get("source_sha256"):
        errors.append(
            f"controlling_source.sha256 {sha!r} != songs/index.json source_sha256 "
            f"{index.get('source_sha256')!r}"
        )
    if sha and f'sha256: "{sha}"' not in metadata_text:
        errors.append("controlling_source.sha256 is not the sha256 recorded in metadata.yaml")

    # ----- completeness over the numbered corpus ---------------------------
    if len(records) != EXPECTED_SONGS:
        errors.append(f"register holds {len(records)} records, expected {EXPECTED_SONGS}")

    index_records = {r["anthology_song_number"]: r for r in index.get("records", [])}
    if len(index_records) != EXPECTED_SONGS:
        errors.append(
            f"songs/index.json holds {len(index_records)} records, expected {EXPECTED_SONGS}"
        )

    seen = []
    for position, rec in enumerate(records, 1):
        number = rec.get("anthology_song_number")
        seen.append(number)
        label = rec.get("id", f"position {position}")

        if number != position:
            errors.append(f"{label}: register is not in ascending song order at position {position}")
            continue

        source = index_records.get(number)
        if source is None:
            errors.append(f"{label}: no songs/index.json record for song {number}")
            continue

        if rec.get("id") != source["id"]:
            errors.append(f"song {number:03d}: id {rec.get('id')!r} != index id {source['id']!r}")
        for field, key in (
            ("film_title_ta", "film_title_ta"),
            ("lyric_title_as_printed", "lyric_title"),
            ("lyric_pdf_pages", "lyric_pdf_pages"),
        ):
            if rec.get(field) != source[key]:
                errors.append(
                    f"song {number:03d}: {field} {rec.get(field)!r} != index {key} {source[key]!r}"
                )

        decision = rec.get("decision")
        level = rec.get("evidence_level")
        included = rec.get("public_inclusion")
        match = rec.get("list_to_lyric_match")

        if decision not in DECISIONS:
            errors.append(f"song {number:03d}: unknown decision {decision!r}")
        if level not in {"A", "B", "C", "D"}:
            errors.append(f"song {number:03d}: unknown evidence_level {level!r}")
        if match not in MATCH_KINDS:
            errors.append(f"song {number:03d}: unknown list_to_lyric_match {match!r}")
        if not isinstance(included, bool):
            errors.append(f"song {number:03d}: public_inclusion is not a boolean")

        # The inclusion rule is enforced, not merely described.
        expected_inclusion = decision in INCLUDING_DECISIONS and level in QUALIFYING_LEVELS
        if included is not expected_inclusion:
            errors.append(
                f"song {number:03d}: public_inclusion={included} contradicts the inclusion rule "
                f"for decision={decision!r} at evidence level {level!r}"
            )

        # A qualifying song must name the printed attribution it rests on.
        if expected_inclusion:
            for field in ("film_song_list_pdf_page", "film_song_list_entry_as_printed",
                          "attributed_lyricist_as_printed"):
                if not rec.get(field):
                    errors.append(
                        f"song {number:03d}: included without a printed {field}"
                    )
            if rec.get("attributed_lyricist_as_printed") != "கலைஞர்":
                errors.append(
                    f"song {number:03d}: included but the printed lyricist is "
                    f"{rec.get('attributed_lyricist_as_printed')!r}"
                )

        basis = rec.get("decision_basis")
        if not isinstance(basis, str) or len(basis.strip()) < 40:
            errors.append(f"song {number:03d}: decision_basis is missing or too thin to audit")

        # unresolved must never be phrased as a negative authorship finding.
        if decision in {"unresolved", "insufficient-evidence"} and isinstance(basis, str):
            if re.search(r"not\s+(?:a\s+)?Kalaignar['’]?s?\b", basis) and "not a finding" not in basis:
                errors.append(
                    f"song {number:03d}: {decision} basis reads as a finding of non-authorship"
                )

    if sorted(seen) != list(range(1, EXPECTED_SONGS + 1)):
        errors.append("register does not cover songs 001-054 exactly once each")

    # ----- declared counts must match the records --------------------------
    tally = {name: 0 for name in DECISIONS}
    for rec in records:
        if rec.get("decision") in tally:
            tally[rec["decision"]] += 1
    declared = evidence.get("counts", {})
    for key, value in (
        ("songs_registered", len(records)),
        ("established_kalaignar", tally["established-kalaignar"]),
        ("established_other", tally["established-other"]),
        ("unresolved", tally["unresolved"]),
        ("insufficient_evidence", tally["insufficient-evidence"]),
        ("proposed_public_inclusion", sum(1 for r in records if r.get("public_inclusion"))),
    ):
        if declared.get(key) != value:
            errors.append(f"counts.{key} is {declared.get(key)!r}, records give {value}")

    # ----- derived manifest ------------------------------------------------
    expected_manifest = serialise(derive_manifest(evidence))
    if write_mode:
        MANIFEST_PATH.write_text(expected_manifest, encoding="utf-8")
    elif not MANIFEST_PATH.exists():
        cannot_validate("missing required input: authorship/public-inclusion.json")
    else:
        actual = MANIFEST_PATH.read_text(encoding="utf-8")
        if actual != expected_manifest:
            errors.append(
                "authorship/public-inclusion.json is not the byte-exact derivation of the "
                "evidence register; regenerate with --write"
            )

    print("KALAIGNAR-AUTHORSHIP INCLUSION GATE")
    print("status=", "PASS" if not errors else "FAIL")
    print("songs_registered=", len(records))
    print("decision_counts=", json.dumps(tally, ensure_ascii=False, sort_keys=True))
    print("proposed_public_inclusion=", sum(1 for r in records if r.get("public_inclusion")))
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
