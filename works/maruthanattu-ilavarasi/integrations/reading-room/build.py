#!/usr/bin/env python3
"""Build and validate the Maruthanattu Ilavarasi Reading Room payload."""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
WORK=ROOT/"works"/"maruthanattu-ilavarasi"; OUT=WORK/"integrations"/"reading-room"
READER=WORK/"editions"/"en"/"reader-edition.json"; READER_MANIFEST=WORK/"editions"/"en"/"manifest.json"
SCENES=[("opening",None,"Unnumbered opening")]+[(f"scene-{n:03d}",n,f"Scene {n}") for n in range(2,11)]
SOURCE_SHA256="8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f"; BUILD_VERSION=1
COMMENT_RE=re.compile(r"<!--.*?-->\s*",re.S); BAD_RE=re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b",re.I)
class QAError(RuntimeError): pass
def ensure(c,m):
    if not c: raise QAError(m)
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def sha(b): return hashlib.sha256(b).hexdigest()
def aggregate(paths):
    d=hashlib.sha256()
    for p in sorted(paths,key=lambda x:x.as_posix()):
        ensure(p.exists(),f"Missing input {p.relative_to(ROOT)}"); d.update(p.relative_to(ROOT).as_posix().encode()); d.update(b"\0"); d.update(p.read_bytes()); d.update(b"\0")
    return d.hexdigest()
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    reader=load(READER); rm=load(READER_MANIFEST)
    ensure(rm["status"]=="PASS" and rm["source_sha256"]==SOURCE_SHA256,"Reader manifest not PASS/current")
    ensure(reader["status"]=="complete-verified" and reader["checkpoint"]["translation_units"]==228 and reader["checkpoint"]["immutable_dialogue_links"]==208,"Reader drift")
    ensure(reader["source_structure"]["unnumbered_opening"] is True and reader["source_structure"]["synthetic_scene_1"] is False and reader["source_structure"]["source_scene_numbers"]==list(range(2,11)),"Source structure drift")
    segs=[]; ids=set(); links=set(); non=0; cross=0
    for i,(fn,scene,label) in enumerate(SCENES):
        rseg=reader["segments"][i]; ensure(rseg["source_scene_number"]==scene and rseg["navigation_label"]==label,f"Segment order drift {fn}")
        sp=WORK/"scenes"/f"{fn}.md"; tamil=COMMENT_RE.sub("",sp.read_text(encoding="utf-8")).strip(); ensure(tamil,f"Empty Tamil scene {fn}")
        expected=sp.relative_to(ROOT).as_posix()
        for u in rseg["english_units"]:
            ensure(u["id"] not in ids,f"Duplicate unit {u['id']}"); ids.add(u["id"]); ensure(u["source_scene_file"]==expected,f"Tamil source path drift {u['id']}")
            if u["kind"]=="dialogue": ensure(u["source_record_id"] and u["source_record_id"] not in links,f"Bad dialogue link {u['id']}"); links.add(u["source_record_id"])
            else: non+=1
            if len(u["page_provenance"])>1: cross+=1
        segs.append({**rseg,"tamil_source_file":expected,"tamil_text":tamil})
    ensure(len(ids)==228 and len(links)==208 and non==20 and cross==5,"Payload count drift")
    payload={"schema_version":1,"integration_target":"Kalaignar Digital Library / Reading Room","preferred_public_surface":"https://nenjukkuneethi.org/read","integration_status":"payload-complete-verified","site_application_status":"not-applied","source_authority":"pugazg/kalaignar-cinema-works verified Maruthanattu Ilavarasi structured records","work":{"id":"maruthanattu-ilavarasi","kind":"film-screenplay","title_ta":"மருதநாட்டு இளவரசி","presentation_title_en":"Maruthanattu Ilavarasi","presentation_title_en_is_editorial":True,"source_sha256":SOURCE_SHA256,"status":"complete-verified","languages":["ta","en"],"counts":{"derivative_units":10,"translation_units":228,"immutable_dialogue_links":208,"non_dialogue_units":20,"cross_page_units":5,"retained_performance_records":0}},"navigation":{"primary_sections":["unnumbered-opening","source-scenes"],"opening_order":"unnumbered source opening before scene 2","source_scene_order":"source numbering 2-10","source_scene_numbers_are_source_numbers":True,"synthetic_scene_1":False,"suggested_slug":"maruthanattu-ilavarasi","suggested_slug_is_presentation_metadata":True},"language_presentation":{"default":"ta","available":["ta","en","parallel"],"rule":"language switching is presentation only; verified Tamil and English stored text must not be rewritten"},"search":{"recommended_fields":["segments.tamil_text","segments.english_units.speaker_label_ta","segments.english_units.english_text"],"normalization_rule":"search normalization may create indexes but must not alter stored source or translation text"},"provenance_policy":{"show_source_pages":True,"preserve_source_paths":True,"scene_numbering_rule":"the opening is unnumbered; scenes 2-10 are source-numbered and must remain so","dialogue_rule":"all 208 immutable dialogue links remain exact source-linked identifiers","cross_page_rule":"all 5 multi-page English units retain complete page provenance","performance_rule":"Phase 8 retained zero song/performance records; the integration must not invent any"},"segments":segs}
    pb=(json.dumps(payload,ensure_ascii=False,indent=2)+"\n").encode(); ensure(not BAD_RE.search(pb.decode()),"Placeholder leakage")
    inputs=[READER,READER_MANIFEST]+[WORK/"scenes"/f"{fn}.md" for fn,_,_ in SCENES]; ih=aggregate(inputs); ph=sha(pb); (OUT/"reading-room.json").write_bytes(pb)
    manifest={"work_id":"maruthanattu-ilavarasi","integration":"reading-room","build_version":BUILD_VERSION,"status":"PASS","site_application_status":"not-applied","source_sha256":SOURCE_SHA256,"authoritative_input_count":len(inputs),"reader_and_tamil_input_aggregate_sha256":ih,"checkpoint":{"segments":10,"unnumbered_opening":1,"source_numbered_scenes":9,"translation_units":228,"immutable_dialogue_links":208,"non_dialogue_units":20,"cross_page_units":5,"retained_performance_records":0},"output":{"path":"works/maruthanattu-ilavarasi/integrations/reading-room/reading-room.json","bytes":len(pb),"sha256":ph}}
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("MARUTHANATTU ILAVARASI READING ROOM PAYLOAD: PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
