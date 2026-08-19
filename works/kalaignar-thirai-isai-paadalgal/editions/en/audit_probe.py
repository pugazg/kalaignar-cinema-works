#!/usr/bin/env python3
"""Whole-corpus reader/export preflight for the Kalaignar film-song anthology."""

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "works" / "kalaignar-thirai-isai-paadalgal"
TRANS_DIR = WORK / "translations" / "records"
INDEX_PATH = WORK / "translations" / "index.json"
PAGE_MAP_PATH = WORK / "songs" / "page-map.json"
SONGS_DIR = WORK / "songs"

EXPECTED_SONGS = 54
EXPECTED_PILOT = {1, 2, 3}
EXPECTED_CROSS_PAGE = {
    9: [38, 39],
    19: [53, 54],
    23: [58, 59],
    24: [62, 63],
    36: [86, 87],
    37: [90, 91],
    51: [121, 122],
    52: [123, 124],
}

errors = []
warnings = []

index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
page_map = json.loads(PAGE_MAP_PATH.read_text(encoding="utf-8"))

# ----- machine map ---------------------------------------------------------
map_rows = page_map.get("songs", [])
if len(map_rows) != EXPECTED_SONGS:
    errors.append(f"page-map song count {len(map_rows)} != {EXPECTED_SONGS}")

expected_pages = {}
for ordinal, row in enumerate(map_rows, 1):
    expected_song = f"{ordinal:03d}"
    if row.get("song") != expected_song:
        errors.append(f"page-map order mismatch at {ordinal}: {row.get('song')} != {expected_song}")
    pages = row.get("pdf_pages")
    if not isinstance(pages, list) or not pages or any(not isinstance(p, int) for p in pages):
        errors.append(f"invalid page-map pages for {expected_song}: {pages}")
    elif pages != sorted(pages) or len(pages) != len(set(pages)):
        errors.append(f"non-monotonic/duplicate page-map pages for {expected_song}: {pages}")
    expected_pages[ordinal] = pages

if page_map.get("tamil_fidelity_gate") != "complete-verified":
    errors.append("songs/page-map.json Tamil fidelity gate is not complete-verified")
if page_map.get("processed_draft_song_ids") not in ([], None):
    errors.append("songs/page-map.json still contains draft song IDs")
if page_map.get("next_unprocessed_song") is not None or page_map.get("next_unprocessed_song_page") is not None:
    errors.append("songs/page-map.json still points to an unprocessed Tamil song/page")

# ----- translation index ---------------------------------------------------
expected_index_status = {
    "status": "complete-verified",
    "target_language": "en",
    "mode": "semantic-poetic-source-faithful",
    "source_corpus_status": "complete-verified",
    "source_songs_expected": 54,
    "source_songs_verified": 54,
    "translated_songs": 54,
}
for key, value in expected_index_status.items():
    if index.get(key) != value:
        errors.append(f"translations/index.json {key}={index.get(key)!r}, expected {value!r}")

expected_counts = {"not-started": 0, "draft": 0, "review": 0, "pilot-verified": 3, "verified": 51}
if index.get("status_counts") != expected_counts:
    errors.append(f"translations/index.json status_counts={index.get('status_counts')}, expected {expected_counts}")
if index.get("next_batch") is not None:
    errors.append("translations/index.json next_batch must be null after translation completion")

index_records = index.get("records", [])
if len(index_records) != EXPECTED_SONGS:
    errors.append(f"translation index record count {len(index_records)} != {EXPECTED_SONGS}")

# ----- record/source reconciliation ---------------------------------------
translation_ids = []
song_ids = []
song_numbers = []
record_paths = []
statuses = Counter()
attribution_states = Counter()
cross_page = {}
total_mapped_tamil_lines = 0
total_english_lines = 0
source_linked_records = 0

actual_record_files = sorted(TRANS_DIR.glob("song-*.json"))
expected_record_files = [TRANS_DIR / f"song-{n:03d}.json" for n in range(1, EXPECTED_SONGS + 1)]
if actual_record_files != expected_record_files:
    missing = [str(p.relative_to(ROOT)) for p in expected_record_files if p not in actual_record_files]
    extra = [str(p.relative_to(ROOT)) for p in actual_record_files if p not in expected_record_files]
    if missing:
        errors.append(f"missing translation record files: {missing}")
    if extra:
        errors.append(f"extra translation record files: {extra}")

for n in range(1, EXPECTED_SONGS + 1):
    tpath = TRANS_DIR / f"song-{n:03d}.json"
    spath = SONGS_DIR / f"song-{n:03d}.md"
    if not tpath.exists() or not spath.exists():
        continue

    try:
        tr = json.loads(tpath.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {tpath.relative_to(ROOT)}: {exc}")
        continue

    song_text = spath.read_text(encoding="utf-8")
    expected_translation_id = f"kalaignar-song-en-{n:03d}"
    expected_song_id = f"kalaignar-song-{n:03d}"
    expected_status = "pilot-verified" if n in EXPECTED_PILOT else "verified"
    expected_song_path = f"works/kalaignar-thirai-isai-paadalgal/songs/song-{n:03d}.md"
    expected_translation_path = f"works/kalaignar-thirai-isai-paadalgal/translations/records/song-{n:03d}.json"

    if tr.get("id") != expected_translation_id:
        errors.append(f"song {n:03d}: translation id {tr.get('id')!r} != {expected_translation_id}")
    if tr.get("song_id") != expected_song_id:
        errors.append(f"song {n:03d}: song_id {tr.get('song_id')!r} != {expected_song_id}")
    if tr.get("anthology_song_number") != n:
        errors.append(f"song {n:03d}: anthology_song_number {tr.get('anthology_song_number')!r} != {n}")
    if tr.get("target_language") != "en":
        errors.append(f"song {n:03d}: target_language is not en")
    if tr.get("mode") != "semantic-poetic-source-faithful":
        errors.append(f"song {n:03d}: translation mode drift: {tr.get('mode')!r}")
    if tr.get("status") != expected_status:
        errors.append(f"song {n:03d}: status {tr.get('status')!r} != {expected_status}")

    translation_ids.append(tr.get("id"))
    song_ids.append(tr.get("song_id"))
    song_numbers.append(tr.get("anthology_song_number"))
    record_paths.append(expected_translation_path)
    statuses[tr.get("status")] += 1

    source = tr.get("source") or {}
    if source.get("song_file") != expected_song_path:
        errors.append(f"song {n:03d}: source song path mismatch: {source.get('song_file')!r}")
    else:
        source_linked_records += 1
    if source.get("tamil_status") != "verified":
        errors.append(f"song {n:03d}: source Tamil status is not verified")
    if source.get("pdf_pages") != expected_pages.get(n):
        errors.append(f"song {n:03d}: source pages {source.get('pdf_pages')} != page-map {expected_pages.get(n)}")
    if source.get("attribution_status") != "anthology-attributed":
        errors.append(f"song {n:03d}: attribution drift: {source.get('attribution_status')!r}")
    attribution_states[source.get("attribution_status")] += 1
    if isinstance(source.get("pdf_pages"), list) and len(source["pdf_pages"]) > 1:
        cross_page[n] = source["pdf_pages"]

    # Reconcile translation-source metadata against the immutable Tamil Markdown.
    heading = re.search(r"^#\s+(\d{3})\s+—\s+(.+)$", song_text, re.M)
    if not heading:
        errors.append(f"song {n:03d}: Tamil source heading missing/unparseable")
    else:
        if heading.group(1) != f"{n:03d}":
            errors.append(f"song {n:03d}: Tamil heading number mismatch {heading.group(1)}")
        if source.get("tamil_title") != heading.group(2).strip():
            errors.append(f"song {n:03d}: Tamil title mismatch translation={source.get('tamil_title')!r} source={heading.group(2).strip()!r}")

    film = re.search(r"^- film:\s+`([^`]+)`\s*$", song_text, re.M)
    if not film:
        errors.append(f"song {n:03d}: Tamil source film metadata missing")
    elif source.get("film_title_ta") != film.group(1):
        errors.append(f"song {n:03d}: film title mismatch translation={source.get('film_title_ta')!r} source={film.group(1)!r}")

    attr = re.search(r"^- attribution status:\s+`([^`]+)`\s*$", song_text, re.M)
    if not attr or attr.group(1) != "anthology-attributed":
        errors.append(f"song {n:03d}: Tamil source attribution is not anthology-attributed")
    trans_status = re.search(r"^- transcription status:\s+`([^`]+)`\s*$", song_text, re.M)
    if not trans_status or trans_status.group(1) != "verified":
        errors.append(f"song {n:03d}: Tamil source transcription status is not verified")

    source_comment = re.search(r"<!--\s*source:\s*pdf=([0-9-]+).*?anthology_song=(\d{3})\s+status=([a-z-]+)\s*-->", song_text)
    if not source_comment:
        errors.append(f"song {n:03d}: Tamil source provenance comment missing/unparseable")
    else:
        comment_pages = []
        for part in source_comment.group(1).split("-"):
            if part.isdigit():
                comment_pages.append(int(part))
        # Single-page comments yield one number; two-page comments yield both bounds and all current cross-page records are two contiguous pages.
        if len(comment_pages) == 2 and comment_pages[1] == comment_pages[0] + 1:
            comment_pages = list(range(comment_pages[0], comment_pages[1] + 1))
        if comment_pages != expected_pages.get(n):
            errors.append(f"song {n:03d}: Tamil source comment pages {comment_pages} != page-map {expected_pages.get(n)}")
        if source_comment.group(2) != f"{n:03d}" or source_comment.group(3) != "verified":
            errors.append(f"song {n:03d}: Tamil source provenance comment number/status mismatch")

    translation = tr.get("translation") or {}
    if not isinstance(translation.get("english_title"), str) or not translation.get("english_title", "").strip():
        errors.append(f"song {n:03d}: missing English title")
    sections = translation.get("sections")
    if not isinstance(sections, list) or not sections:
        errors.append(f"song {n:03d}: translation sections missing/empty")
        continue

    expected_ordinals = list(range(1, len(sections) + 1))
    actual_ordinals = [s.get("ordinal") for s in sections]
    if actual_ordinals != expected_ordinals:
        errors.append(f"song {n:03d}: section ordinals {actual_ordinals} != {expected_ordinals}")

    for section in sections:
        ta_lines = section.get("source_tamil_lines")
        en_lines = section.get("english_lines")
        if not isinstance(ta_lines, list) or not isinstance(en_lines, list) or not ta_lines or not en_lines:
            errors.append(f"song {n:03d} section {section.get('ordinal')}: missing Tamil/English line arrays")
            continue
        if len(ta_lines) != len(en_lines):
            errors.append(f"song {n:03d} section {section.get('ordinal')}: line mapping {len(ta_lines)} Tamil != {len(en_lines)} English")
        if any(not isinstance(line, str) or not line.strip() for line in ta_lines):
            errors.append(f"song {n:03d} section {section.get('ordinal')}: empty/non-string Tamil line")
        if any(not isinstance(line, str) or not line.strip() for line in en_lines):
            errors.append(f"song {n:03d} section {section.get('ordinal')}: empty/non-string English line")
        total_mapped_tamil_lines += len(ta_lines)
        total_english_lines += len(en_lines)

    # Check the parallel index row without trusting it as the sole authority.
    if n <= len(index_records):
        row = index_records[n - 1]
        expected_row = {
            "translation_id": expected_translation_id,
            "song_id": expected_song_id,
            "anthology_song_number": n,
            "status": expected_status,
            "source_song_file": expected_song_path,
            "source_pdf_pages": expected_pages.get(n),
            "translation_file": expected_translation_path,
        }
        for key, value in expected_row.items():
            if row.get(key) != value:
                errors.append(f"song {n:03d}: index row {key}={row.get(key)!r}, expected {value!r}")

# ----- aggregate uniqueness/order/status gates -----------------------------
def dupes(values):
    c = Counter(values)
    return sorted(v for v, count in c.items() if count > 1)

if song_numbers != list(range(1, EXPECTED_SONGS + 1)):
    errors.append(f"record anthology order is not 1..54: {song_numbers}")
for name, values in (("translation IDs", translation_ids), ("song IDs", song_ids), ("record paths", record_paths)):
    d = dupes(values)
    if d:
        errors.append(f"duplicate {name}: {d}")

if statuses != Counter({"pilot-verified": 3, "verified": 51}):
    errors.append(f"record status distribution {dict(statuses)} != pilot-verified 3 / verified 51")
if attribution_states != Counter({"anthology-attributed": 54}):
    errors.append(f"record attribution distribution {dict(attribution_states)} != anthology-attributed 54")
if source_linked_records != EXPECTED_SONGS:
    errors.append(f"source-linked record count {source_linked_records} != {EXPECTED_SONGS}")
if cross_page != EXPECTED_CROSS_PAGE:
    errors.append(f"cross-page provenance {cross_page} != expected {EXPECTED_CROSS_PAGE}")
if total_mapped_tamil_lines != total_english_lines:
    errors.append(f"whole-corpus mapped Tamil/English line totals differ: {total_mapped_tamil_lines}/{total_english_lines}")

# Cross-check index ID lists.
expected_pilot_ids = [f"kalaignar-song-{n:03d}" for n in range(1, 4)]
expected_verified_ids = [f"kalaignar-song-{n:03d}" for n in range(4, 55)]
if index.get("pilot_song_ids") != expected_pilot_ids:
    errors.append("translations/index.json pilot_song_ids does not equal songs 001-003 in order")
if index.get("verified_song_ids") != expected_verified_ids:
    errors.append("translations/index.json verified_song_ids does not equal songs 004-054 in order")

print("KALAIGNAR FILM-SONG ANTHOLOGY ENGLISH READER PREFLIGHT")
print("status=", "PASS" if not errors else "FAIL")
print("translation_record_files=", len(actual_record_files), "expected=", EXPECTED_SONGS)
print("source_linked_records=", source_linked_records)
print("status_counts=", dict(statuses))
print("attribution_counts=", dict(attribution_states))
print("mapped_tamil_lines=", total_mapped_tamil_lines)
print("mapped_english_lines=", total_english_lines)
print("cross_page_records=", json.dumps({f"{k:03d}": v for k, v in cross_page.items()}, sort_keys=True))
print("warnings=", warnings)
if errors:
    print("errors=")
    for err in errors:
        print(" -", err)
    sys.exit(1)
print("errors= []")
