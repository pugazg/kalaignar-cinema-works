#!/usr/bin/env python3
"""Build and QA the deterministic Maruthanattu Ilavarasi English reader/export layer."""
from __future__ import annotations
import hashlib, html, json, re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]; WORK=ROOT/"works"/"maruthanattu-ilavarasi"; OUT=WORK/"editions"/"en"
BUILD_VERSION=1; SOURCE_SHA256="8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f"
SEGMENTS=[("opening","maruthanattu-ilavarasi-opening",1,None,"Unnumbered opening"),("scene-002","maruthanattu-ilavarasi-s002",2,2,"Scene 2"),("scene-003","maruthanattu-ilavarasi-s003",3,3,"Scene 3"),("scene-004","maruthanattu-ilavarasi-s004",4,4,"Scene 4"),("scene-005","maruthanattu-ilavarasi-s005",5,5,"Scene 5"),("scene-006","maruthanattu-ilavarasi-s006",6,6,"Scene 6"),("scene-007","maruthanattu-ilavarasi-s007",7,7,"Scene 7"),("scene-008","maruthanattu-ilavarasi-s008",8,8,"Scene 8"),("scene-009","maruthanattu-ilavarasi-s009",9,9,"Scene 9"),("scene-010","maruthanattu-ilavarasi-s010",10,10,"Scene 10")]
EXPECTED_KINDS={"dialogue":208,"stage-direction":14,"written-text":2,"narrative":1,"chant":1,"structural-separator":2}
BAD_RE=re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b",re.I)
class QAError(RuntimeError): pass
def ensure(c,m):
    if not c: raise QAError(m)
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def sha(b): return hashlib.sha256(b).hexdigest()
def page_label(pp):
    a,b=pp[0],pp[-1]; pr=lambda x:"—" if x.get("printed_page") is None else str(x["printed_page"])
    return f"PDF {a['pdf_page']} / printed {pr(a)}" if len(pp)==1 else f"PDF {a['pdf_page']}→{b['pdf_page']} / printed {pr(a)}→{pr(b)}"
def input_paths():
    return [WORK/"translations"/"index.json",WORK/"dialogues"/"index.json",WORK/"songs"/"index.json",WORK/"metadata.yaml"]+[WORK/"translations"/"records"/f"{fn}.json" for fn,*_ in SEGMENTS]
def aggregate(ps):
    d=hashlib.sha256()
    for p in sorted(ps,key=lambda x:x.as_posix()):
        d.update(p.relative_to(ROOT).as_posix().encode()); d.update(b"\0"); d.update(p.read_bytes()); d.update(b"\0")
    return d.hexdigest()
def build_model():
    ti=load(WORK/"translations"/"index.json"); di=load(WORK/"dialogues"/"index.json"); si=load(WORK/"songs"/"index.json")
    ensure(ti["status"]=="complete-verified" and ti["translation_units_verified"]==228 and ti["immutable_dialogue_links_verified"]==208,"English index drift")
    ensure(di["dialogue_record_count"]==208,"Dialogue index drift"); ensure(si["retained_performance_records"]==0,"Performance gate drift")
    m={"work_id":"maruthanattu-ilavarasi","title_ta":"மருதநாட்டு இளவரசி","title_en":"Maruthanattu Ilavarasi","edition":"english-reader","status":"complete-verified","source_sha256":SOURCE_SHA256,"source_structure":{"unnumbered_opening":True,"source_scene_numbers":list(range(2,11)),"synthetic_scene_1":False,"retained_performance_records":0},"checkpoint":{"derivative_units":10,"translation_units":228,"immutable_dialogue_links":208,"non_dialogue_units":20,"cross_page_units":5,"performance_translation_units":0},"segments":[]}
    ids=[]; links=[]; cross=[]; kinds=Counter(); non=0
    for fn,seg,ordn,scene,label in SEGMENTS:
        p=WORK/"translations"/"records"/f"{fn}.json"; tr=load(p); ensure(tr["segment_id"]==seg and tr["derivative_ordinal"]==ordn and tr["source_scene_number"]==scene and tr["segment_status"]=="verified",f"Segment drift {seg}")
        us=[]
        for i,u in enumerate(tr["units"],1):
            ensure(u["id"].endswith(f"-u{i:03d}") and u["status"]=="verified" and u["target_language"]=="en",f"Unit drift {u['id']}")
            txt=u["translation"]["english_text"]; ensure(txt.strip() and not BAD_RE.search(txt) and "scene ends" not in txt.lower(),f"Bad text {u['id']}")
            ids.append(u["id"]); kinds[u["kind"]]+=1
            if u["kind"]=="dialogue": links.append(u["source"]["source_record_id"])
            else: ensure(u["source"]["source_record_id"] is None and u["source"]["speaker_label"] is None,f"Invented owner {u['id']}"); non+=1
            if len(u["source"]["page_provenance"])>1: cross.append(u["id"])
            us.append({"id":u["id"],"kind":u["kind"],"status":u["status"],"speaker_label_ta":u["source"]["speaker_label"],"source_delimiter":u["source"]["source_delimiter"],"source_record_id":u["source"]["source_record_id"],"page_provenance":u["source"]["page_provenance"],"english_text":txt,"notes":u["translation"].get("notes",[]),"source_scene_file":u["source"]["canonical_scene_path"]})
        m["segments"].append({"segment_id":seg,"segment_kind":tr["segment_kind"],"derivative_ordinal":ordn,"source_scene_number":scene,"navigation_label":label,"translation_file":p.relative_to(ROOT).as_posix(),"english_units":us})
    ensure(len(ids)==len(set(ids))==228,"Unit ID coverage"); ensure(len(links)==len(set(links))==208,"Dialogue coverage"); ensure(non==20 and dict(kinds)==EXPECTED_KINDS,"Kind/count drift"); ensure(cross==ti["cross_page_translation_units"],"Cross-page drift")
    return m,dict(kinds)
def render_md(m):
    o=["# Maruthanattu Ilavarasi — English Reader Edition","","**Tamil title:** மருதநாட்டு இளவரசி  ","**Status:** complete-verified deterministic English derivative  ",f"**Source scan SHA-256:** `{SOURCE_SHA256}`","","> Source-structure note: the booklet contains an unnumbered opening followed by source-numbered scenes 2–10. This reader preserves that structure exactly and does not invent Scene 1. Exact Tamil speaker labels remain source metadata. Phase 8 retained zero song/performance records.","","## Contents",""]
    for s in m["segments"]: a="unnumbered-opening" if s["source_scene_number"] is None else f"scene-{s['source_scene_number']}"; o.append(f"- [{s['navigation_label']}](#{a})")
    o+=["","---",""]
    for s in m["segments"]:
        a="unnumbered-opening" if s["source_scene_number"] is None else f"scene-{s['source_scene_number']}"; o += [f'<a id="{a}"></a>',f"## {s['navigation_label']}","",f"**English record:** `{s['translation_file']}`",f"**Tamil source derivative:** `{s['english_units'][0]['source_scene_file'] if s['english_units'] else ''}`",""]
        for u in s["english_units"]:
            o.append(f"<!-- unit:{u['id']}; source:{page_label(u['page_provenance'])} -->")
            if u["kind"]=="dialogue": o += [f"**{u['speaker_label_ta']}**  ",u["english_text"],""]
            elif u["kind"]=="stage-direction": o += [f"*{u['english_text']}*",""]
            elif u["kind"]=="structural-separator": o += [u["english_text"],""]
            else: lab={"written-text":"Written text","narrative":"Narrative","chant":"Unlabelled chant"}.get(u["kind"],u["kind"]); o += [f"**{lab}**  ",u["english_text"],""]
        o += ["---",""]
    return "\n".join(o).rstrip()+"\n"
def render_html(m):
    nav=" ".join(f'<a href="#{"unnumbered-opening" if s["source_scene_number"] is None else "scene-"+str(s["source_scene_number"])}">{html.escape(s["navigation_label"])}</a>' for s in m["segments"]); blocks=[]
    for s in m["segments"]:
        a="unnumbered-opening" if s["source_scene_number"] is None else f"scene-{s['source_scene_number']}"; us=[]
        for u in s["english_units"]:
            attrs=f'data-unit-id="{html.escape(u["id"],quote=True)}" data-source-page="{html.escape(page_label(u["page_provenance"]),quote=True)}"'; t=html.escape(u["english_text"]).replace("\n","<br>")
            if u["kind"]=="dialogue": us.append(f'<div class="unit dialogue" {attrs}><span class="speaker" lang="ta">{html.escape(str(u["speaker_label_ta"]))}</span><span lang="en">{t}</span></div>')
            elif u["kind"]=="stage-direction": us.append(f'<div class="unit stage" {attrs} lang="en">{t}</div>')
            elif u["kind"]=="structural-separator": us.append(f'<div class="unit separator" {attrs}>{t}</div>')
            else: lab={"written-text":"Written text","narrative":"Narrative","chant":"Unlabelled chant"}.get(u["kind"],u["kind"]); us.append(f'<div class="unit special" {attrs}><strong>{html.escape(lab)}</strong><div lang="en">{t}</div></div>')
        blocks.append(f'<section class="segment" id="{a}"><h2>{html.escape(s["navigation_label"])}</h2><p><strong>English record:</strong> <code>{html.escape(s["translation_file"])}</code><br><strong>Tamil source derivative:</strong> <code>{html.escape(s["english_units"][0]["source_scene_file"] if s["english_units"] else "")}</code></p>{"".join(us)}<p class="back"><a href="#contents">Back to contents</a></p></section>')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Maruthanattu Ilavarasi — English Reader Edition</title><style>body{{font-family:ui-serif,Georgia,"Times New Roman",serif;max-width:62rem;margin:auto;padding:2rem 1.25rem 5rem;line-height:1.65}}nav{{display:flex;flex-wrap:wrap;gap:.75rem}}.segment{{border-top:1px solid;margin-top:2.5rem;padding-top:1rem}}.unit{{margin:.8rem 0}}.dialogue{{display:grid;grid-template-columns:minmax(5rem,9rem) 1fr;gap:.75rem}}.speaker{{font-weight:700}}.stage{{font-style:italic}}.special{{border-left:2px solid;padding-left:.75rem}}.separator{{text-align:center}}.back{{margin-top:1.5rem}}@media(max-width:42rem){{.dialogue{{display:block}}.speaker{{display:block;margin-bottom:.25rem}}}}@media print{{nav,.back{{display:none}}.segment{{break-before:page}}}}</style></head><body><h1>Maruthanattu Ilavarasi — English Reader Edition</h1><p><strong>Tamil title:</strong> <span lang="ta">மருதநாட்டு இளவரசி</span></p><p><strong>Status:</strong> complete-verified deterministic English derivative</p><p><strong>Source-structure note:</strong> Unnumbered opening followed by source-numbered scenes 2–10; no synthetic Scene 1. Exact Tamil speaker labels are retained as metadata.</p><h2 id="contents">Contents</h2><nav>{nav}</nav>{"".join(blocks)}</body></html>
'''
def main():
    OUT.mkdir(parents=True,exist_ok=True); m,kinds=build_model(); ps=input_paths(); ih=aggregate(ps); md=render_md(m).encode(); hb=render_html(m).encode(); jb=(json.dumps(m,ensure_ascii=False,indent=2)+"\n").encode()
    ids=[u["id"] for s in m["segments"] for u in s["english_units"]]
    for uid in ids: ensure(md.decode().count(f"unit:{uid};")==1 and hb.decode().count(f'data-unit-id="{uid}"')==1 and jb.decode().count(f'"id": "{uid}"')==1,f"Render count {uid}")
    for name,data in [("reader-edition.md",md),("reader-edition.html",hb),("reader-edition.json",jb)]: (OUT/name).write_bytes(data)
    manifest={"work_id":"maruthanattu-ilavarasi","edition":"english-reader","build_version":BUILD_VERSION,"status":"PASS","source_sha256":SOURCE_SHA256,"authoritative_input_count":len(ps),"authoritative_input_aggregate_sha256":ih,"checkpoint":{"derivative_units":10,"translation_units":228,"unit_kind_counts":kinds,"immutable_dialogue_links":208,"non_dialogue_units":20,"cross_page_units":5,"retained_performance_records":0},"outputs":{n:{"bytes":len(d),"sha256":sha(d)} for n,d in [("reader-edition.md",md),("reader-edition.html",hb),("reader-edition.json",jb)]}}
    (OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("MARUTHANATTU ILAVARASI ENGLISH READER BUILD: PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
