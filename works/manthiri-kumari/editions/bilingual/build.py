#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
TRANSLATIONS = WORK / "translations"

EXPECTED_INPUT_BLOBS = {
    "works/manthiri-kumari/translations/story-summary.json": "d8867d7d3622aa9ec1976a27c888c38ed9067509",
    "works/manthiri-kumari/translations/performances/001.json": "2a9795a755f6648c4369f6b1ee5d2f3264fae96d",
    "works/manthiri-kumari/translations/performances/002.json": "c67708317ce1255a67fa940ecc168696831785e7",
    "works/manthiri-kumari/translations/performances/003.json": "3831acdaa412e3fe7e85a136059544ce3d7ea312",
    "works/manthiri-kumari/translations/performances/004.json": "63883e7dd812cba01d96cc75cff8f1786b4ca93e",
    "works/manthiri-kumari/translations/performances/005.json": "ec42ab375e03936b5c577b8590bf5193ef3d4297",
    "works/manthiri-kumari/translations/performances/006.json": "1e990b1caad4c58ea9070d97cf9f2b2cd9d800db",
    "works/manthiri-kumari/translations/performances/007.json": "dd0cff587a6abe056acf8c6a1386175e518953f8",
    "works/manthiri-kumari/translations/performances/008.json": "6cb5b981ff89f4b3c859f930e8d2d84d7bf74298",
    "works/manthiri-kumari/translations/performances/009.json": "356aaccc7b5e2bd545c1b26e58191fc436b23b74",
    "works/manthiri-kumari/translations/performances/010.json": "f8693cca434ddc9604f298b40e8172546b6e4868",
    "works/manthiri-kumari/translations/performances/011.json": "a2fe5343284dd9e29ace3b270e61e3ba7cef4f4c",
    "works/manthiri-kumari/translations/performances/012.json": "2092670d909a46f94bc15a9ca524cf2aeb12c9f6",
    "works/manthiri-kumari/translations/performances/013.json": "44060525bffa12c2b5e1c4324173328f44a0c960",
    "works/manthiri-kumari/translations/performances/014.json": "881d16ab4a87ab6806bba7492d75e8cb80f01a25",
    "works/manthiri-kumari/translations/performances/015.json": "7eef4759c46da3079d953fb0396ba7bec641b20e",
}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    repo_root = HERE.parents[3]
    story_path = TRANSLATIONS / "story-summary.json"
    perf_paths = [TRANSLATIONS / "performances" / f"{i:03d}.json" for i in range(1, 16)]
    actual_blobs = {}
    for path in [story_path, *perf_paths]:
        rel = path.relative_to(repo_root).as_posix()
        got = git_blob_sha(path.read_bytes())
        want = EXPECTED_INPUT_BLOBS[rel]
        if got != want:
            raise SystemExit(f"input changed: {rel}: expected {want}, got {got}")
        actual_blobs[rel] = got

    aggregate = hashlib.sha256(
        "\n".join(f"{p}\t{actual_blobs[p]}" for p in EXPECTED_INPUT_BLOBS).encode()
    ).hexdigest()
    if aggregate != "4016ae611897dbfd1b8ad7ba3d9eda167d0efd774d8abe04c911a2b2321622ba":
        raise SystemExit("input aggregate changed")

    story = json.loads(story_path.read_text(encoding="utf-8"))
    perfs = [json.loads(path.read_text(encoding="utf-8")) for path in perf_paths]
    if story.get("status") != "verified" or len(story["translation"]["sections"]) != 13:
        raise SystemExit("story-summary gate failed")
    if [p["sequence"] for p in perfs] != list(range(1, 16)):
        raise SystemExit("performance sequence gate failed")
    if any(p.get("status") != "verified" for p in perfs):
        raise SystemExit("performance verification gate failed")

    sections = sum(len(p["translation"]["sections"]) for p in perfs)
    ta = sum(len(s["source_tamil_lines"]) for p in perfs for s in p["translation"]["sections"])
    en = sum(len(s["english_lines"]) for p in perfs for s in p["translation"]["sections"])
    mismatches = sum(
        len(s["source_tamil_lines"]) != len(s["english_lines"])
        for p in perfs for s in p["translation"]["sections"]
    )
    if (sections, ta, en, mismatches) != (52, 234, 234, 0):
        raise SystemExit(f"line mapping gate failed: {(sections, ta, en, mismatches)}")
    if sum(p["source"]["authorship_status"] == "unresolved" for p in perfs) != 15:
        raise SystemExit("authorship tier changed")
    if sum(p["source"]["cross_witness_status"] == "confirmed-existing-anthology-witness" for p in perfs) != 1:
        raise SystemExit("cross-witness tier changed")

    expected_perfs = []
    for p in perfs:
        expected_perfs.append({
            "sequence": p["sequence"],
            "heading_ta": p["heading_ta"],
            "heading_en": p["heading_en"],
            "translation_path": f"../../translations/performances/{p['sequence']:03d}.json",
            "source_record_path": f"../../songs/records/{p['sequence']:03d}.json",
            "source_pdf_pages": p["source"]["pdf_pages"],
            "sections": len(p["translation"]["sections"]),
            "line_cues": sum(len(s["source_tamil_lines"]) for s in p["translation"]["sections"]),
            "authorship_status": p["source"]["authorship_status"],
            "cross_witness_status": p["source"]["cross_witness_status"],
        })

    reader = json.loads((HERE / "reader-edition.json").read_text(encoding="utf-8"))
    if reader["navigation_model"] != "story-summary-plus-performance-blocks":
        raise SystemExit("reader navigation model changed")
    if reader["story_summary"]["logical_units"] != 13 or reader["performances"] != expected_perfs:
        raise SystemExit("reader composition does not match verified translation inputs")
    if reader["qa"]["result"] != "PASS" or reader["qa"]["synthetic_scene_ids_created"] != 0:
        raise SystemExit("reader QA state is not PASS")

    manifest = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
    if manifest["translation_input_blob_list_aggregate_sha256"] != aggregate:
        raise SystemExit("manifest input aggregate mismatch")
    if manifest["qa_status"] != "PASS":
        raise SystemExit("manifest QA is not PASS")
    for name, meta in manifest["outputs"].items():
        path = HERE / name
        if file_sha256(path) != meta["sha256"] or path.stat().st_size != meta["bytes"]:
            raise SystemExit(f"output integrity mismatch: {name}")

    print("Manthiri Kumari bilingual reader QA: PASS")


if __name__ == "__main__":
    main()
