#!/usr/bin/env python3
"""Build the immutable source-preserving dialogue layer for Naam.

Authority is the 45/45 complete-verified source-numbered scene layer. Exact
speaker labels are preserved. Page breaks are provenance boundaries, not
utterance boundaries. Source-unlabelled text is never assigned a speaker by
inference; it is preserved in a separate audit.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

R = Path(__file__).resolve().parents[3]
W = R / "works" / "naam"
SCENES = W / "scenes"
DIALOGUES = W / "dialogues"
RECORDS = DIALOGUES / "records"
NOTES = W / "notes"

SOURCE_RE = re.compile(r"^<!--\s*source:\s*pdf=(?P<pdf>\d+)(?:\s+printed=(?P<printed>[^\s>]+))?[^>]*-->")
DIALOGUE_RE = re.compile(r"^(?P<label>[^:#\[\]{}<>\n]{1,60}?)\s*(?P<delimiter>:-|:)\s*(?P<text>\S.*)$")
NON_SPEAKER_LABELS = {"இடம்", "நேரம்", "காலம்", "பாட்டு", "வசனம்", "டைரக்ஷன்", "கடிதத்தில்"}
ALT_RAW = "ஜீவானந்தர் — குமரன்! குமரன்!"
ALT_SCENE = "naam-s041"
SEPARATORS = {"★", "★★★", "* * *", "---", "***", "___"}
NEXT = ("Begin Phase 7 character/entity indexing from the complete-verified immutable dialogue layer. "
        "Preserve all exact source speaker labels as immutable provenance, map label variants to character/entity IDs only in a separate alias layer, "
        "keep generic roles and source anomalies explicit, and run whole-work label/entity coverage QA before the song/authorship gate. "
        "Do not rewrite canonical Tamil, scene text, or dialogue records.")

changed: list[str] = []
def rd(path: str) -> str: return (R / path).read_text(encoding="utf-8")
def wr(path: str, text: str) -> None:
    p = R / path; old = p.read_text(encoding="utf-8") if p.exists() else None
    if old != text:
        p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8"); changed.append(path)
def sha256_text(text: str) -> str: return hashlib.sha256(text.encode("utf-8")).hexdigest()

def source_anchor(s: str):
    m = SOURCE_RE.match(s)
    if not m: return None
    token = m.group("printed")
    return {"pdf_page": int(m.group("pdf")), "printed_page": int(token) if token and token.isdigit() else None}

def parse_dialogue(scene_id: str, s: str):
    if scene_id == ALT_SCENE and s == ALT_RAW:
        return {"speaker_label": "ஜீவானந்தர்", "source_delimiter": "—", "text": "குமரன்! குமரன்!", "parse_kind": "reviewed-alternate-delimiter"}
    if s.startswith(("(", "[", "{")):
        return None
    m = DIALOGUE_RE.match(s)
    if not m: return None
    label = m.group("label").strip()
    if label in NON_SPEAKER_LABELS or label.startswith(("#", "<!--")):
        return None
    return {"speaker_label": label, "source_delimiter": m.group("delimiter"), "text": m.group("text"), "parse_kind": "standard-colon"}

def is_hard_structure(s: str) -> str | None:
    if s.startswith("<!--") and s.endswith("-->"): return "metadata_comment"
    if s.startswith("#"): return "heading"
    if s in SEPARATORS: return "separator"
    if s.startswith("(") or s.endswith(")"): return "stage_direction_parenthetical"
    if s.startswith("[") or s.endswith("]"): return "stage_direction_square"
    if s.startswith("{") or s.endswith("}"): return "stage_direction_curly"
    m = DIALOGUE_RE.match(s)
    if m and m.group("label").strip() in NON_SPEAKER_LABELS: return "non_speaker_colon_cue"
    return None

def append_piece(obj: dict[str, Any], page: dict[str, Any], text: str, blank_before: bool) -> None:
    segs = obj.setdefault("_segments", [])
    if not segs or segs[-1]["pdf_page"] != page["pdf_page"]:
        segs.append({"pdf_page": page["pdf_page"], "printed_page": page["printed_page"], "lines": [text]}); return
    if blank_before and segs[-1]["lines"] and segs[-1]["lines"][-1] != "": segs[-1]["lines"].append("")
    segs[-1]["lines"].append(text)

def finalize(obj: dict[str, Any]) -> None:
    segs = obj.pop("_segments"); page_segments = []
    for seg in segs:
        lines = list(seg["lines"])
        while lines and lines[0] == "": lines.pop(0)
        while lines and lines[-1] == "": lines.pop()
        text = "\n".join(lines); assert text
        page_segments.append({"pdf_page": seg["pdf_page"], "printed_page": seg["printed_page"], "text": text})
    obj["page_provenance"] = [{"pdf_page": x["pdf_page"], "printed_page": x["printed_page"]} for x in page_segments]
    obj["text"] = "\n".join(x["text"] for x in page_segments)
    if len(page_segments) > 1: obj["page_segments"] = page_segments

def build_scene(scene: dict[str, Any]):
    sid = scene["scene_id"]; lines = (SCENES / scene["file"]).read_text(encoding="utf-8").splitlines()
    records = []; unowned = []; current_page = None; active = None; active_unowned = None
    pending_blank = False; unowned_blank = False; stats = Counter()

    def flush_dialogue():
        nonlocal active, pending_blank
        if active is not None:
            finalize(active); records.append(active); active = None
        pending_blank = False
    def flush_unowned():
        nonlocal active_unowned, unowned_blank
        if active_unowned is not None:
            finalize(active_unowned); active_unowned["block_id"] = f"{sid}-u{len(unowned)+1:03d}"; unowned.append(active_unowned); active_unowned = None
        unowned_blank = False

    for line_no, raw in enumerate(lines, 1):
        s = raw.strip(); anchor = source_anchor(s)
        if anchor:
            current_page = anchor; pending_blank = False; unowned_blank = False; stats["source_anchor"] += 1; continue
        if not s:
            if active is not None: pending_blank = True
            if active_unowned is not None: unowned_blank = True
            stats["blank"] += 1; continue
        parsed = parse_dialogue(sid, s)
        if parsed:
            assert current_page is not None, (sid, line_no, s)
            flush_dialogue(); flush_unowned()
            active = {
                "id": f"{sid}-d{len(records)+1:03d}", "scene_id": sid, "scene_ordinal": scene["ordinal"],
                "source_scene_number": scene["source_scene_number"], "source_heading": scene["heading"],
                "speaker_label": parsed["speaker_label"], "source_delimiter": parsed["source_delimiter"],
                "source_scene_file": scene["file"], "_segments": []
            }
            append_piece(active, current_page, parsed["text"], False); stats["explicit_dialogue_start"] += 1
            if parsed["parse_kind"] == "reviewed-alternate-delimiter": stats["reviewed_alternate_delimiter_start"] += 1
            continue
        kind = is_hard_structure(s)
        if kind:
            flush_dialogue(); flush_unowned(); stats[kind] += 1; continue
        assert current_page is not None, (sid, line_no, s)
        if active is not None:
            append_piece(active, current_page, s, pending_blank); pending_blank = False; stats["owned_unlabelled_continuation"] += 1
        else:
            if active_unowned is None:
                active_unowned = {"scene_id": sid, "scene_ordinal": scene["ordinal"], "source_scene_number": scene["source_scene_number"], "source_heading": scene["heading"], "source_scene_file": scene["file"], "reason": "ordinary source text without an active explicit speaker label", "_segments": []}
            append_piece(active_unowned, current_page, s, unowned_blank); unowned_blank = False; stats["unowned_ordinary_text"] += 1
    flush_dialogue(); flush_unowned()
    for i, rec in enumerate(records, 1): assert rec["id"] == f"{sid}-d{i:03d}"
    return records, unowned, dict(sorted(stats.items()))

def schema() -> dict[str, Any]:
    prov = {"type":"object","required":["pdf_page","printed_page"],"properties":{"pdf_page":{"type":"integer","minimum":5,"maximum":71},"printed_page":{"type":["integer","null"],"minimum":6,"maximum":71}},"additionalProperties":False}
    return {"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"naam-dialogue-record.schema.json","title":"Naam immutable dialogue record","type":"object","required":["id","scene_id","scene_ordinal","source_scene_number","source_heading","speaker_label","source_delimiter","text","page_provenance","source_scene_file"],"properties":{"id":{"type":"string","pattern":"^naam-s[0-9]{3}-d[0-9]{3}$"},"scene_id":{"type":"string","pattern":"^naam-s[0-9]{3}$"},"scene_ordinal":{"type":"integer","minimum":1,"maximum":45},"source_scene_number":{"type":"integer","minimum":1,"maximum":45},"source_heading":{"type":"string","minLength":1},"speaker_label":{"type":"string","minLength":1},"source_delimiter":{"type":"string","enum":[":",":-","—"]},"text":{"type":"string","minLength":1},"page_provenance":{"type":"array","minItems":1,"uniqueItems":True,"items":prov},"page_segments":{"type":"array","minItems":2,"items":{"type":"object","required":["pdf_page","printed_page","text"],"properties":{"pdf_page":{"type":"integer","minimum":5,"maximum":71},"printed_page":{"type":["integer","null"],"minimum":6,"maximum":71},"text":{"type":"string","minLength":1}},"additionalProperties":False}},"source_scene_file":{"type":"string","pattern":"^scene-[0-9]{3}\\.md$"}},"additionalProperties":False}

def main() -> None:
    scene_index = json.loads((SCENES / "index.json").read_text(encoding="utf-8")); preflight = json.loads((NOTES / "dialogue-index-preflight.json").read_text(encoding="utf-8"))
    assert scene_index["status"] == "complete-verified" and scene_index["source_scene_count"] == 45
    assert preflight["status"] == "review-complete-ready-to-build" and preflight["scene_count"] == 45
    scenes = scene_index["scene_records"]; assert len(scenes) == 45
    scene_hashes_before = {x["file"]: hashlib.sha256((SCENES/x["file"]).read_bytes()).hexdigest() for x in scenes}
    canonical_hashes_before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((W/"transcription"/"parts").glob("pdf-*.md"))}

    DIALOGUES.mkdir(exist_ok=True); RECORDS.mkdir(exist_ok=True); NOTES.mkdir(exist_ok=True)
    all_records = []; all_unowned = []; per_scene = []; scene_counts = {}
    for scene in scenes:
        records, unowned, stats = build_scene(scene); all_records += records; all_unowned += unowned; scene_counts[scene["scene_id"]] = len(records)
        per_scene.append({"scene_id":scene["scene_id"],"dialogue_records":len(records),"unlabelled_blocks":len(unowned),"classification_counts":stats})
        wr(f"works/naam/dialogues/records/scene-{scene['ordinal']:03d}.json", json.dumps(records, ensure_ascii=False, indent=2)+"\n")

    assert len(all_records) == preflight["explicit_dialogue_candidates"], (len(all_records), preflight["explicit_dialogue_candidates"])
    assert scene_counts == preflight["scene_dialogue_candidate_counts"]
    labels = Counter(r["speaker_label"] for r in all_records); expected = {x["speaker_label"]:x["count"] for x in preflight["exact_speaker_labels"]}; assert dict(labels) == expected
    delimiters = Counter(r["source_delimiter"] for r in all_records); assert dict(sorted(delimiters.items())) == preflight["delimiter_distribution"]
    ids = [r["id"] for r in all_records]; assert len(ids) == len(set(ids))
    assert all(r["scene_ordinal"] == r["source_scene_number"] for r in all_records)
    assert all(p["printed_page"] is None if p["pdf_page"] == 5 else p["printed_page"] == p["pdf_page"] for r in all_records for p in r["page_provenance"])
    multi = [r for r in all_records if len(r["page_provenance"]) > 1]
    assert all("page_segments" in r and r["text"] == "\n".join(x["text"] for x in r["page_segments"]) for r in multi)
    alt = [r for r in all_records if r["source_delimiter"] == "—"]; assert len(alt) == 1 and alt[0]["scene_id"] == ALT_SCENE and alt[0]["speaker_label"] == "ஜீவானந்தர்"
    assert all(r["speaker_label"] not in NON_SPEAKER_LABELS and not r["speaker_label"].startswith("(") for r in all_records)

    index = {"work_id":"naam","status":"complete-verified","authority":"45/45 complete-verified source-numbered scene derivatives","canonical_tamil_gate":"67/67-dual-gate-complete-verified","source_numbered_scenes":True,"source_scene_count":45,"dialogue_record_count":len(all_records),"distinct_exact_speaker_labels":len(labels),"delimiter_distribution":dict(sorted(delimiters.items())),"multi_page_dialogue_records":len(multi),"scene_record_counts":scene_counts,"zero_dialogue_scenes":[sid for sid,n in scene_counts.items() if n==0],"schema":"schema.json","records_directory":"records/","preflight":"../notes/dialogue-index-preflight.json","unlabelled_block_audit":"../notes/unlabelled-block-audit.json","qa":"../notes/dialogue-index-qa.json","policy":{"immutable_unit":"one explicit source speaker-labelled utterance","speaker_label":"exact source label; never normalized","source_delimiter":"preserved as provenance; standard : / :- plus one reviewed scene-41 em-dash occurrence","page_break":"provenance boundary, not utterance boundary","unlabelled_text_without_active_speaker":"excluded from dialogue records and inventoried; never guessed","character_alias_resolution":"deferred"},"next_action":NEXT}
    wr("works/naam/dialogues/index.json", json.dumps(index, ensure_ascii=False, indent=2)+"\n"); wr("works/naam/dialogues/schema.json", json.dumps(schema(), ensure_ascii=False, indent=2)+"\n")
    readme = f'''# நாம் — immutable dialogue layer\n\nStatus: **COMPLETE-VERIFIED**\n\nAuthority: **45/45 complete-verified source-numbered scene derivatives**, themselves derived from **67/67 complete-verified canonical Tamil**.\n\n## Coverage\n\n- source scenes: **45/45**;\n- immutable explicit dialogue records: **{len(all_records)}**;\n- distinct exact speaker labels: **{len(labels)}**;\n- delimiter distribution: **{dict(sorted(delimiters.items()))}**;\n- multi-page immutable utterances: **{len(multi)}**;\n- zero-explicit-dialogue scenes retained as empty arrays: **{len(index['zero_dialogue_scenes'])}**;\n- speaker-label normalization: **0**;\n- inferred source-unlabelled speakers: **0**.\n\nEvery explicit source label is preserved exactly. The single reviewed alternate delimiter `ஜீவானந்தர் — குமரன்! குமரன்!` remains occurrence-specific; em dash is not made a global speaker delimiter. `கடிதத்தில் :- ...` and location cues remain non-dialogue source structures. Source anomaly `உன்மீனு` remains unchanged as an exact explicit label.\n\nSource-unlabelled ordinary text is preserved separately in `../notes/unlabelled-block-audit.json`; it is not silently assigned to a speaker.\n\n## Next activity\n\n{NEXT}\n'''
    wr("works/naam/dialogues/README.md", readme)

    unowned = {"work_id":"naam","phase":"unlabelled-block-audit","status":"complete-preserved-unlabelled","authority":"45/45 complete-verified scene derivatives","block_count":len(all_unowned),"policy":"Ordinary source text without an active explicit speaker label is preserved here and never assigned to a dialogue speaker by inference.","blocks":all_unowned}
    wr("works/naam/notes/unlabelled-block-audit.json", json.dumps(unowned, ensure_ascii=False, indent=2)+"\n")
    umd = ["# நாம் — source-unlabelled block audit","","Status: **COMPLETE — PRESERVED UNLABELLED**","",f"- unlabelled ordinary blocks: **{len(all_unowned)}**","- inferred speaker assignments: **0**","- these blocks remain available to later song/performance/written-text/source-role layers without altering immutable dialogue provenance.",""]
    for b in all_unowned:
        pages=",".join(str(x["pdf_page"]) for x in b["page_provenance"]); preview=b["text"].replace("\n"," / "); preview=preview if len(preview)<=140 else preview[:137]+"..."; umd.append(f"- `{b['block_id']}` — scene {b['source_scene_number']} — PDF {pages}: {preview}")
    wr("works/naam/notes/unlabelled-block-audit.md", "\n".join(umd)+"\n")

    qa = {"work_id":"naam","phase":"dialogue-index-qa","status":"PASS","scene_coverage":"45/45","explicit_source_labels_expected":preflight["explicit_dialogue_candidates"],"immutable_dialogue_records":len(all_records),"explicit_label_ownership":f"{len(all_records)}/{len(all_records)} exactly once","distinct_exact_speaker_labels":len(labels),"label_distribution_matches_preflight":True,"delimiter_distribution_matches_preflight":True,"speaker_alias_normalizations":0,"inferred_unlabelled_speakers":0,"unlabelled_blocks_preserved":len(all_unowned),"multi_page_dialogue_records":len(multi),"reviewed_alternate_delimiter_dialogues":preflight["reviewed_alternate_delimiter_dialogues"],"reviewed_non_speaker_dash_candidates":preflight["anomalous_delimiter_candidates"],"non_speaker_colon_cues_excluded":len(preflight["colon_rejects"]),"zero_dialogue_scenes":index["zero_dialogue_scenes"],"per_scene":per_scene,"canonical_tamil_modified":0,"scene_text_modified":0,"next_gate":"character/entity index ready"}
    wr("works/naam/notes/dialogue-index-qa.json", json.dumps(qa, ensure_ascii=False, indent=2)+"\n")
    qmd=f'''# நாம் — dialogue-index QA\n\nResult: **PASS**\n\n- source scenes covered: **45/45**;\n- explicit source speaker labels owned exactly once: **{len(all_records)}/{len(all_records)}**;\n- immutable dialogue records: **{len(all_records)}**;\n- distinct exact speaker-label strings: **{len(labels)}**;\n- delimiter distribution matches preflight: **PASS — {dict(sorted(delimiters.items()))}**;\n- multi-page utterances kept as one logical record: **{len(multi)}**;\n- speaker-label normalization: **0**;\n- inferred assignments for source-unlabelled text: **0**;\n- unlabelled blocks preserved separately: **{len(all_unowned)}**;\n- location / written-text colon cues excluded from dialogue: **{len(preflight['colon_rejects'])}**;\n- occurrence-specific scene-41 em-dash speaker verdict: **PASS**;\n- canonical Tamil modified: **0**;\n- scene text modified: **0**.\n\n`உன்மீனு` remains exactly as the source-explicit label; no alias repair occurs in this immutable layer. `கடிதத்தில்` remains written-text provenance rather than a speaker.\n\n## Gate result\n\n**Dialogue indexing CLOSED / COMPLETE-VERIFIED.** Character/entity indexing may now begin.\n\n## Next activity\n\n{NEXT}\n'''
    wr("works/naam/notes/dialogue-index-qa.md", qmd)

    # Synchronize work-local and repository-wide status mirrors without altering canonical or scene text.
    p="works/naam/metadata.yaml"; s=rd(p)
    s=s.replace("  dialogue_index: not-started", f"  dialogue_index: complete-verified\n  dialogue_record_count: {len(all_records)}\n  distinct_exact_speaker_labels: {len(labels)}\n  dialogue_index_path: \"dialogues/index.json\"\n  dialogue_qa_path: \"notes/dialogue-index-qa.json\"")
    s=s.replace("  dialogue_index: ready-next", f"  dialogue_index: complete-verified-{len(all_records)}-records")
    s=s.replace("  character_entity_index: blocked-pending-dialogue-layer", "  character_entity_index: ready-next")
    s=s.replace("  song_authorship_gate: blocked-pending-dialogue-character-layers", "  song_authorship_gate: blocked-pending-character-layer")
    s=re.sub(r'next_action:\s*".*"\s*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False), s, count=1, flags=re.M); wr(p,s)

    p="works/naam/README.md"; s=rd(p)
    s=s.replace("- dialogue / character / song derivatives: **blocked by normal gate order after scenes**;", f"- dialogue index: **{len(all_records)} immutable records / COMPLETE-VERIFIED / QA PASS**;\n- character/entity index: **ready-next**; song derivatives remain downstream;")
    if "## Immutable dialogue checkpoint" not in s:
        marker="## Source-visible publication / credit evidence\n"; block=f'''## Immutable dialogue checkpoint\n\n- source scenes represented: **45/45**;\n- immutable explicit dialogue records: **{len(all_records)}**;\n- distinct exact speaker labels: **{len(labels)}**;\n- multi-page dialogue records: **{len(multi)}**;\n- source-unlabelled speaker inference: **0**;\n- QA: `notes/dialogue-index-qa.json` — **PASS**;\n- dialogue index: `dialogues/index.json`;\n- canonical Tamil / scene text modified by this phase: **0 / 0**.\n\n**Next:** {NEXT}\n\n'''; s=s.replace(marker,block+marker,1)
    s=re.sub(r'\*\*Next:\*\* Begin Phase 6 dialogue indexing[^\n]*', "**Next:** "+NEXT, s); wr(p,s)

    p="works/naam/PROJECT_HANDOVER.md"; s=rd(p)
    if "## Immutable dialogue closure checkpoint" not in s:
        s += f'''\n\n## Immutable dialogue closure checkpoint\n\n- dialogue index: **COMPLETE-VERIFIED**;\n- source scenes covered: **45/45**;\n- immutable dialogue records: **{len(all_records)}**;\n- distinct exact speaker labels: **{len(labels)}**;\n- multi-page dialogue records: **{len(multi)}**;\n- source-unlabelled blocks: **{len(all_unowned)} preserved unlabelled; 0 inferred speakers**;\n- QA: `notes/dialogue-index-qa.json` — **PASS**;\n- canonical Tamil / scene derivative modifications: **0 / 0**.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
    wr(p,s)
    wr("works/naam/NEXT_CHAT_PROMPT.md", f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**. Scene-text derivatives are **45/45 COMPLETE-VERIFIED** with boundary ownership QA PASS. Immutable dialogue indexing is now **COMPLETE-VERIFIED: {len(all_records)} records across 45/45 scenes, {len(labels)} distinct exact source-label strings, {len(multi)} multi-page utterances, dialogue QA PASS, 0 speaker-label normalization, 0 inferred source-unlabelled speakers**.\n\nDialogue index: `works/naam/dialogues/index.json`. QA: `works/naam/notes/dialogue-index-qa.json`. Source-unlabelled blocks remain preserved separately in `works/naam/notes/unlabelled-block-audit.json`.\n\nDo not alter canonical Tamil, scene text or immutable dialogue records except for later source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

    p="data/works.json"; data=json.loads(rd(p)); naam=next(x for x in data if x.get("id")=="naam"); sd=naam.setdefault("structured_derivatives",{})
    sd.update({"dialogue_index":"complete-verified","dialogue_index_path":"works/naam/dialogues/index.json","dialogue_records":len(all_records),"distinct_exact_speaker_labels":len(labels),"multi_page_dialogue_records":len(multi),"dialogue_qa":"PASS","dialogue_qa_path":"works/naam/notes/dialogue-index-qa.json","character_entity_index":"ready-next","next_structured_derivative":"character-entity-index"}); naam["next_action"]=NEXT; wr(p,json.dumps(data,ensure_ascii=False,separators=(",",":"))+"\n")

    p="README.md"; s=rd(p)
    s=s.replace("- scene derivatives: **45/45 COMPLETE-VERIFIED; boundary ownership QA PASS**;", f"- scene derivatives: **45/45 COMPLETE-VERIFIED; boundary ownership QA PASS**;\n- dialogue index: **{len(all_records)} immutable records / COMPLETE-VERIFIED / QA PASS**;")
    s=re.sub(r'\*\*Next:\*\* Begin Phase 6 dialogue indexing[^\n]*', "**Next:** "+NEXT, s); wr(p,s)

    p="docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md"; s=rd(p)
    s=s.replace("- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scene derivatives **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS**; dialogue index next.", f"- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **{len(all_records)} records COMPLETE-VERIFIED / QA PASS**; character/entity index next.")
    s=s.replace("- scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; dialogue index next; English remains downstream.", f"- scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; dialogue index **{len(all_records)} records COMPLETE-VERIFIED / QA PASS**; character/entity index next; English remains downstream.")
    s=re.sub(r'\*\*Exact next activity:\*\* Begin Phase 6 dialogue indexing[^\n]*', "**Exact next activity:** "+NEXT, s); wr(p,s)

    p="docs/STATUS_CONSISTENCY_AUDIT.md"; s=rd(p)
    s=s.replace("| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scene derivatives complete-verified; boundary QA PASS** | dialogue index next | not-started |", f"| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; {len(all_records)} dialogue records; dialogue QA PASS** | character/entity index next | not-started |")
    s=re.sub(r'\*\*Next production phase:\*\* Begin Phase 6 dialogue indexing[^\n]*', "**Next production phase:** "+NEXT, s); wr(p,s)

    scene_hashes_after = {x["file"]: hashlib.sha256((SCENES/x["file"]).read_bytes()).hexdigest() for x in scenes}; canonical_hashes_after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((W/"transcription"/"parts").glob("pdf-*.md"))}
    assert scene_hashes_before == scene_hashes_after and canonical_hashes_before == canonical_hashes_after
    print(json.dumps({"changed":changed,"dialogue_records":len(all_records),"distinct_labels":len(labels),"multi_page_records":len(multi),"unlabelled_blocks":len(all_unowned),"delimiter_distribution":dict(sorted(delimiters.items())),"next_action":NEXT},ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
