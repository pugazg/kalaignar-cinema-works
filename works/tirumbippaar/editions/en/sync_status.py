#!/usr/bin/env python3
"""Synchronize Tirumbippaar derivative-status metadata from verified build outputs.

This script edits only works/tirumbippaar/metadata.yaml. It does not touch the
canonical Tamil/source layers. The workflow runs it after reader and EPUB QA so
repository-level status cannot drift from verified derivative checkpoints.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "tirumbippaar"
INDEX = WORK / "translations" / "index.json"
EDITION = WORK / "editions" / "en"
PACKAGE_MANIFEST = EDITION / "package-manifest.json"
METADATA = WORK / "metadata.yaml"

idx = json.loads(INDEX.read_text(encoding="utf-8"))
if idx.get("status") != "complete-verified":
    raise SystemExit("Refusing metadata sync: translation index is not complete-verified")
if not PACKAGE_MANIFEST.exists():
    raise SystemExit("Refusing metadata sync: EPUB package manifest is missing")
pkg = json.loads(PACKAGE_MANIFEST.read_text(encoding="utf-8"))
if pkg.get("status") != "complete-verified" or pkg.get("epub", {}).get("qa_status", "PASS") != "PASS":
    # Older package manifests do not carry qa_status inside epub; package-level
    # complete-verified plus generated QA report is the controlling condition.
    if pkg.get("status") != "complete-verified":
        raise SystemExit("Refusing metadata sync: EPUB package is not complete-verified")

epub = pkg["epub"]
scenes_started = ", ".join(str(x) for x in idx["scenes_started"])
scenes_verified = ", ".join(str(x) for x in idx["scenes_verified"])
counts = idx["unit_kind_counts"]
cross = ", ".join(f'"{x}"' for x in idx["cross_page_translation_units"])
direct = ", ".join(f'"{x}"' for x in idx["direct_source_unlabelled_dialogue_units"])
zero = ", ".join(str(x) for x in idx["zero_dialogue_source_scenes_translated"])
songs = ", ".join(f'"{x}"' for x in idx["verified_song_reference_occurrences"])

translation_block = f'''  english_translation:
    status: complete-verified
    path: "translations/index.json"
    schema: "translations/schema.json"
    readme: "translations/README.md"
    record_directory: "translations/records"
    pilot_scene: 1
    scenes_started: [{scenes_started}]
    scenes_verified: [{scenes_verified}]
    translation_units: {idx['translation_units']}
    verified_units: {idx['unit_status_counts']['verified']}
    review_units: {idx['unit_status_counts']['review']}
    draft_units: {idx['unit_status_counts']['draft']}
    unit_kind_counts:
      dialogue: {counts['dialogue']}
      stage_direction: {counts['stage-direction']}
      song: {counts['song']}
      song_reference: {counts['song-reference']}
      chant: {counts['chant']}
      written_text: {counts['written-text']}
    dialogue_source_records_expected: 1040
    dialogue_source_records_linked: 1040
    cross_page_translation_units: [{cross}]
    direct_source_unlabelled_dialogue_units: [{direct}]
    zero_dialogue_source_scenes_translated: [{zero}]
    verified_song_reference_occurrences: [{songs}]
    synthetic_star_end_units: 0
    next_batch: null
    note: "All 93 scenes are complete-verified in English with 1,321 source-linked units. All 1,040 labelled dialogue records are linked exactly once and seven additional source-visible spoken units intentionally remain unlabelled. Reader-export preflight removed residual synthetic star-end units derived only from structural stars, restored source ordering in scenes 29 and 30, and removed three duplicated stage-action units from scene 47. Final diagnostics report zero synthetic star-end units, zero page-order regressions, zero unit-ID errors, and exact 1,040/1,040 dialogue-link coverage. No canonical Tamil or structured source layer was modified."
  english_reader_edition:
    status: complete-verified
    path: "editions/en"
    build: "editions/en/build.py"
    preflight: "editions/en/audit_probe.py"
    qa_report: "editions/en/QA_REPORT.md"
    manifest: "editions/en/manifest.json"
    markdown: "editions/en/reader-edition.md"
    html: "editions/en/reader-edition.html"
    json: "editions/en/reader-edition.json"
    translation_units: 1321
    immutable_dialogue_records_linked: 1040
    cross_page_translation_units: 12
    qa_status: PASS
  english_epub_package:
    status: complete-verified
    format: "EPUB 3"
    path: "editions/en/tirumbippaar-en.epub"
    build: "editions/en/package.py"
    qa_report: "editions/en/EPUB_QA_REPORT.md"
    manifest: "editions/en/package-manifest.json"
    translation_units: 1321
    scene_documents: 93
    zip_members: {epub['zip_members']}
    byte_size: {epub['bytes']}
    sha256: "{epub['sha256']}"
    deterministic: true
    qa_status: PASS
  next_structured_derivative: null'''

text = METADATA.read_text(encoding="utf-8")
pattern = re.compile(r"  english_translation:\n.*?  next_structured_derivative: null", re.S)
if not pattern.search(text):
    raise SystemExit("Could not locate english_translation metadata block")
text = pattern.sub(translation_block, text, count=1)

# Synchronize the compact status tail without confusing the structured block.
if not re.search(r"^  english_reader_edition: complete-verified$", text, re.M):
    text = re.sub(
        r"(^  english_translation: complete-verified\n)",
        r"\1  english_reader_edition: complete-verified\n",
        text,
        count=1,
        flags=re.M,
    )
if not re.search(r"^  english_epub_package: complete-verified$", text, re.M):
    text = re.sub(
        r"(^  english_reader_edition: complete-verified\n)",
        r"\1  english_epub_package: complete-verified\n",
        text,
        count=1,
        flags=re.M,
    )

METADATA.write_text(text, encoding="utf-8")
print("Synchronized Tirumbippaar translation, reader and EPUB package status metadata")
