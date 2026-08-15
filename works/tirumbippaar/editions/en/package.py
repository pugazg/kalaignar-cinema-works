#!/usr/bin/env python3
"""Build a deterministic EPUB 3 package from the verified Tirumbippaar reader JSON.

This is a downstream publication package. It reads the generated reader edition,
verifies its completed checkpoint, writes only inside editions/en/, and never
modifies canonical Tamil or structured source layers.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
EDITION = ROOT / "works" / "tirumbippaar" / "editions" / "en"
READER_JSON = EDITION / "reader-edition.json"
EPUB_PATH = EDITION / "tirumbippaar-en.epub"
QA_PATH = EDITION / "EPUB_QA_REPORT.md"
MANIFEST_PATH = EDITION / "package-manifest.json"

EXPECTED_SCENES = list(range(1, 94))
EXPECTED_UNITS = 1321
EXPECTED_KINDS = {
    "dialogue": 1047,
    "stage-direction": 254,
    "song": 0,
    "song-reference": 7,
    "chant": 2,
    "written-text": 11,
}
SOURCE_SHA256 = "973b9c3f7b84d6a1902a4a472af8799c783bf1ec2d6cd015796fc1df1ce59682"
MODIFIED = "2026-08-15T00:00:00Z"
ZIP_TIME = (1980, 1, 1, 0, 0, 0)
SYNTHETIC_END_RE = re.compile(r"^\s*\(Scene ends\.\)\s*$", re.I)


class PackageError(RuntimeError):
    pass


def ensure(ok: bool, message: str) -> None:
    if not ok:
        raise PackageError(message)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise PackageError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def xhtml_document(title: str, body: str) -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="../styles/book.css" />
</head>
<body>
{body}
</body>
</html>
'''


def unit_text(unit: dict[str, Any]) -> str:
    tr = unit.get("translation", {})
    if isinstance(tr.get("english_text"), str):
        return tr["english_text"]
    lines = tr.get("english_lines")
    ensure(isinstance(lines, list) and lines, f"Unit {unit.get('id')} has no readable English payload")
    return "\n".join(lines)


def render_scene(scene_record: dict[str, Any]) -> str:
    scene = scene_record["canonical_scene"]
    parts = [f'<section class="scene" epub:type="chapter" xmlns:epub="http://www.idpf.org/2007/ops">', f"<h1>Scene {scene}</h1>"]
    for unit in scene_record["units"]:
        uid = html.escape(unit["id"], quote=True)
        kind = unit["kind"]
        source = unit["source"]
        text = unit_text(unit)
        ensure(not SYNTHETIC_END_RE.match(text), f"Synthetic scene-end text survives in {unit['id']}")
        content = html.escape(text).replace("\n", "<br />\n")
        if kind == "dialogue":
            speaker = source.get("speaker_label")
            speaker_html = f'<span class="speaker" lang="ta">{html.escape(speaker)}</span>' if isinstance(speaker, str) and speaker else ""
            parts.append(f'<p class="unit dialogue" data-unit-id="{uid}">{speaker_html}<span class="dialogue-text">{content}</span></p>')
        elif kind == "stage-direction":
            parts.append(f'<p class="unit stage" data-unit-id="{uid}">{content}</p>')
        else:
            label = {
                "song": "Song",
                "song-reference": "Song / performance reference",
                "chant": "Chant",
                "written-text": "Written text",
            }[kind]
            parts.append(f'<aside class="unit special {html.escape(kind)}" data-unit-id="{uid}"><p class="unit-label">{html.escape(label)}</p><p>{content}</p></aside>')
    parts.append("</section>")
    return xhtml_document(f"Scene {scene}", "\n".join(parts))


def build_entries(reader: dict[str, Any]) -> dict[str, bytes]:
    scenes = reader["scenes"]
    scene_files = [f"text/scene-{scene:03d}.xhtml" for scene in EXPECTED_SCENES]

    title_body = '''<section class="title-page" epub:type="titlepage" xmlns:epub="http://www.idpf.org/2007/ops">
<h1>Tirumbippaar!</h1>
<p class="tamil-title" lang="ta">திரும்பிப்பார்!</p>
<p>English reader edition</p>
<p class="credit">Story &amp; dialogue credit as printed: Kalaignar M. Karunanidhi</p>
<p class="edition-note">Source-linked archival English derivative. Canonical Tamil remains authoritative.</p>
</section>'''

    nav_items = "\n".join(f'<li><a href="text/scene-{scene:03d}.xhtml">Scene {scene}</a></li>' for scene in EXPECTED_SCENES)
    nav = xhtml_document("Contents", f'''<nav epub:type="toc" id="toc" xmlns:epub="http://www.idpf.org/2007/ops">
<h1>Contents</h1>
<ol>
{nav_items}
</ol>
</nav>
<nav epub:type="landmarks" hidden="hidden" xmlns:epub="http://www.idpf.org/2007/ops">
<ol><li><a epub:type="bodymatter" href="text/scene-001.xhtml">Start of text</a></li></ol>
</nav>''').replace('href="../styles/book.css"', 'href="styles/book.css"')

    css = '''body { font-family: serif; line-height: 1.55; margin: 5%; }
h1 { text-align: center; margin: 1.5em 0; }
.title-page { text-align: center; margin-top: 20%; }
.tamil-title { font-size: 1.5em; }
.credit, .edition-note { margin-top: 2em; }
.dialogue { margin: 0.75em 0; }
.speaker { display: block; font-weight: bold; margin-bottom: 0.15em; }
.stage { font-style: italic; margin: 0.8em 1em; }
.special { border-left: 0.15em solid currentColor; margin: 1em; padding-left: 0.8em; }
.unit-label { font-style: italic; font-weight: bold; margin-bottom: 0.2em; }
'''

    manifest_items = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav" />',
        '<item id="css" href="styles/book.css" media-type="text/css" />',
        '<item id="title" href="text/title.xhtml" media-type="application/xhtml+xml" />',
    ]
    spine_items = ['<itemref idref="title" linear="yes" />']
    for scene in EXPECTED_SCENES:
        manifest_items.append(f'<item id="scene-{scene:03d}" href="text/scene-{scene:03d}.xhtml" media-type="application/xhtml+xml" />')
        spine_items.append(f'<itemref idref="scene-{scene:03d}" linear="yes" />')

    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">urn:sha256:{SOURCE_SHA256}:tirumbippaar-en-reader</dc:identifier>
    <dc:title>Tirumbippaar! — English Reader Edition</dc:title>
    <dc:language>en</dc:language>
    <dc:creator id="creator">Kalaignar M. Karunanidhi</dc:creator>
    <meta refines="#creator" property="role" scheme="marc:relators">aut</meta>
    <meta property="dcterms:modified">{MODIFIED}</meta>
    <meta property="schema:accessMode">textual</meta>
  </metadata>
  <manifest>
    {' '.join(manifest_items)}
  </manifest>
  <spine>
    {' '.join(spine_items)}
  </spine>
</package>
'''

    container_xml = '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml" />
  </rootfiles>
</container>
'''

    entries: dict[str, bytes] = {
        "mimetype": b"application/epub+zip",
        "META-INF/container.xml": container_xml.encode("utf-8"),
        "EPUB/package.opf": opf.encode("utf-8"),
        "EPUB/nav.xhtml": nav.encode("utf-8"),
        "EPUB/styles/book.css": css.encode("utf-8"),
        "EPUB/text/title.xhtml": xhtml_document("Tirumbippaar!", title_body).encode("utf-8"),
    }
    for scene_record, filename in zip(scenes, scene_files, strict=True):
        entries[f"EPUB/{filename}"] = render_scene(scene_record).encode("utf-8")
    return entries


def write_epub(entries: dict[str, bytes]) -> None:
    # ZIP_STORED for every entry makes package bytes reproducible across zlib versions.
    with zipfile.ZipFile(EPUB_PATH, "w", compression=zipfile.ZIP_STORED, strict_timestamps=True) as zf:
        order = ["mimetype"] + sorted(name for name in entries if name != "mimetype")
        for name in order:
            info = zipfile.ZipInfo(name, ZIP_TIME)
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 0
            info.external_attr = 0
            zf.writestr(info, entries[name])


def validate_epub(reader: dict[str, Any], entries: dict[str, bytes]) -> dict[str, Any]:
    expected_entry_count = 6 + len(EXPECTED_SCENES)
    ensure(EPUB_PATH.exists(), "EPUB file was not created")
    epub_bytes = EPUB_PATH.read_bytes()
    ensure(bool(epub_bytes), "EPUB file is empty")

    with zipfile.ZipFile(EPUB_PATH, "r") as zf:
        names = zf.namelist()
        ensure(names[0] == "mimetype", "EPUB mimetype is not the first ZIP member")
        ensure(zf.read("mimetype") == b"application/epub+zip", "EPUB mimetype content is invalid")
        ensure(zf.getinfo("mimetype").compress_type == zipfile.ZIP_STORED, "EPUB mimetype must be stored without compression")
        ensure(len(names) == expected_entry_count, f"Expected {expected_entry_count} EPUB members, found {len(names)}")
        ensure(set(names) == set(entries), "EPUB member set differs from the deterministic build set")
        for name, expected in entries.items():
            ensure(zf.read(name) == expected, f"EPUB member bytes differ after packaging: {name}")

    all_units: list[str] = []
    all_text: list[str] = []
    for scene_record in reader["scenes"]:
        for unit in scene_record["units"]:
            all_units.append(unit["id"])
            all_text.append(unit_text(unit))
    ensure(len(all_units) == EXPECTED_UNITS == len(set(all_units)), "Reader unit identity count is not exactly 1,321")
    ensure(not any(SYNTHETIC_END_RE.match(text) for text in all_text), "Synthetic '(Scene ends.)' text reached EPUB packaging")

    joined_scene_xhtml = b"\n".join(entries[f"EPUB/text/scene-{scene:03d}.xhtml"] for scene in EXPECTED_SCENES).decode("utf-8")
    for uid in all_units:
        ensure(joined_scene_xhtml.count(f'data-unit-id="{uid}"') == 1, f"EPUB does not contain exactly one instance of {uid}")

    nav_text = entries["EPUB/nav.xhtml"].decode("utf-8")
    for scene in EXPECTED_SCENES:
        ensure(nav_text.count(f'href="text/scene-{scene:03d}.xhtml"') == 1, f"EPUB navigation missing or duplicates scene {scene}")

    opf_text = entries["EPUB/package.opf"].decode("utf-8")
    ensure(opf_text.count('media-type="application/xhtml+xml"') == 94, "OPF XHTML manifest count is not title/nav + 93 scenes")
    ensure(opf_text.count("<itemref ") == 94, "OPF spine count is not title + 93 scenes")

    return {
        "sha256": sha256_bytes(epub_bytes),
        "bytes": len(epub_bytes),
        "zip_members": expected_entry_count,
        "scene_documents": 93,
        "unit_markers": EXPECTED_UNITS,
    }


def main() -> int:
    reader = load_json(READER_JSON)
    ensure(reader.get("work_id") == "tirumbippaar", "Reader JSON work_id mismatch")
    ensure(reader.get("target_language") == "en", "Reader JSON language mismatch")
    ensure(reader.get("status") == "complete-verified", "Reader JSON is not complete-verified")
    ensure(reader.get("source_sha256") == SOURCE_SHA256, "Reader JSON source hash mismatch")
    ensure(reader.get("canonical_scene_order") == EXPECTED_SCENES, "Reader JSON scene order mismatch")
    ensure(reader.get("translation_units") == EXPECTED_UNITS, "Reader JSON unit total mismatch")
    ensure(reader.get("unit_kind_counts") == EXPECTED_KINDS, "Reader JSON kind totals mismatch")
    scenes = reader.get("scenes")
    ensure(isinstance(scenes, list) and len(scenes) == 93, "Reader JSON does not contain 93 scene records")
    ensure([record.get("canonical_scene") for record in scenes] == EXPECTED_SCENES, "Reader JSON scene records are unordered")

    entries = build_entries(reader)
    write_epub(entries)
    result = validate_epub(reader, entries)

    qa = f"""# Tirumbippaar English EPUB — Package QA

**Status:** PASS  
**Package:** `tirumbippaar-en.epub`  
**Format:** EPUB 3  
**Authority:** `reader-edition.json` generated from the verified translation layer

## Verified checks

- canonical scenes packaged: **93/93**;
- verified English units packaged exactly once: **1,321/1,321**;
- immutable reader kind checkpoint retained: **1,047 dialogue / 254 stage direction / 7 song-reference / 2 chant / 11 written-text / 0 full-song**;
- EPUB scene XHTML documents: **93**;
- package ZIP members: **{result['zip_members']}**;
- `mimetype` is first, exact and uncompressed;
- OPF manifest contains navigation, stylesheet, title page and all 93 scene documents;
- OPF spine contains title page + all 93 scenes in canonical order;
- EPUB navigation contains every scene exactly once;
- every English unit ID appears in scene XHTML exactly once;
- no synthetic `(Scene ends.)` text is packaged;
- package is written with fixed ZIP timestamps and uncompressed deterministic members.

## Integrity

- source scan SHA-256: `{SOURCE_SHA256}`
- EPUB SHA-256: `{result['sha256']}`
- EPUB bytes: **{result['bytes']}**

This package is a downstream publication derivative. Canonical Tamil, scene derivatives, dialogue records, character mappings and song inventory are not modified by packaging.
"""
    QA_PATH.write_text(qa, encoding="utf-8")

    package_manifest = {
        "work_id": "tirumbippaar",
        "package": "english-reader-epub3",
        "status": "complete-verified",
        "source_scan_sha256": SOURCE_SHA256,
        "reader_authority": "works/tirumbippaar/editions/en/reader-edition.json",
        "reader_sha256": sha256_bytes(READER_JSON.read_bytes()),
        "canonical_scenes": EXPECTED_SCENES,
        "translation_units": EXPECTED_UNITS,
        "unit_kind_counts": EXPECTED_KINDS,
        "epub": {
            "path": "tirumbippaar-en.epub",
            **result,
        },
        "qa_report": "EPUB_QA_REPORT.md",
        "deterministic_zip_timestamp": "1980-01-01T00:00:00",
        "epub_modified_metadata": MODIFIED,
    }
    MANIFEST_PATH.write_text(json.dumps(package_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Tirumbippaar English EPUB package QA: PASS")
    print(f"Scenes: 93 | Units: {EXPECTED_UNITS} | EPUB bytes: {result['bytes']} | SHA-256: {result['sha256']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PackageError as exc:
        print(f"Tirumbippaar English EPUB package QA: FAIL: {exc}")
        raise SystemExit(1)
