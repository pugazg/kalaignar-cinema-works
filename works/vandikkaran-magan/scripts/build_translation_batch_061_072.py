#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, re

from translation_batch_061_072_data_a import DIALOGUE_TRANSLATIONS as DA, DIALOGUE_NOTES as NA, ND as NDA, DIALOGUE_OCCURRENCE_LINKS as OA
from translation_batch_061_072_data_b import DIALOGUE_TRANSLATIONS as DB, DIALOGUE_NOTES as NB, ND as NDB, DIALOGUE_OCCURRENCE_LINKS as OB

W=Path(__file__).resolve().parents[1]
T=W/'translations'; R=T/'records'; D=W/'dialogues'/'records'; S=W/'scenes'; P=W/'transcription'/'pages'
R.mkdir(parents=True,exist_ok=True)
TARGET_SCENES=list(range(61,73))
NEXT=(
 'Build and verify the deterministic whole-work English reader/export layer from the 72 verified scene translations. '
 'Require every verified translation unit exactly once, all 773 immutable dialogue links complete and unique, all cross-page provenance preserved, '
 'all verified song/performance links valid, no synthetic star-derived prose or placeholders, and no mutation of closed Tamil, scene, dialogue, character or song authorities.'
)

DIALOGUE_TRANSLATIONS={**DA,**DB}; DIALOGUE_NOTES={**NA,**NB}; ND={**NDA,**NDB}; DIALOGUE_OCCURRENCE_LINKS={**OA,**OB}
assert set(DIALOGUE_TRANSLATIONS)==set(TARGET_SCENES)
assert set(ND)==set(TARGET_SCENES)

# Closed upstream authority.
didx=json.loads((W/'dialogues'/'index.json').read_text(encoding='utf-8'))
cidx=json.loads((W/'characters'/'index.json').read_text(encoding='utf-8'))
songidx=json.loads((W/'songs'/'index.json').read_text(encoding='utf-8'))
assert didx['status']=='complete-verified-reconciled' and didx['dialogue_record_count']==773
assert cidx['status']=='complete-verified' and cidx['dialogue_record_coverage']=='773/773'
assert songidx['status']=='complete-verified-source-only' and songidx['mapped_source_visible_occurrences']==9

scene_index_obj=json.loads((S/'index.json').read_text(encoding='utf-8'))
scene_meta={int(x['ordinal']):x for x in scene_index_obj['scenes']}
EXPECTED_SOURCE_SCENE_IDS=[scene_meta[n]['scene_id'] for n in TARGET_SCENES]
assert EXPECTED_SOURCE_SCENE_IDS==['49','50','51','52','53','53-எ','53-பி','53-சி','53-டி','54','55','56']

song_inventory=json.loads((W/'songs'/'inventory.json').read_text(encoding='utf-8'))
perf={x['id']:x for x in song_inventory['records']}
assert perf['vandikkaran-magan-perf-009']['source_scene_id']=='53-சி'
expected_counts={n:int(didx['scene_record_counts'][f'vandikkaran-magan-s{n:03d}']) for n in TARGET_SCENES}
for n in TARGET_SCENES:
    assert set(DIALOGUE_TRANSLATIONS[n])=={r['id'] for r in json.loads((D/f'scene-{n:03d}.json').read_text(encoding='utf-8'))}, (n,len(DIALOGUE_TRANSLATIONS[n]),expected_counts[n])
assert sum(expected_counts.values())==105,sum(expected_counts.values())


def norm(s):
    s=s.replace('\r\n','\n').replace('\r','\n')
    s=re.sub(r'<!--.*?-->',' ',s,flags=re.S)
    s=re.sub(r'^[#]+\s*','',s,flags=re.M).replace('**','')
    return re.sub(r'\s+',' ',s).strip()

def source_blocks(n):
    text=(S/f'scene-{n:03d}.md').read_text(encoding='utf-8')
    parts=[b.strip() for b in re.split(r'\n[ \t]*\n',text) if b.strip()]
    return [b for b in parts if not b.startswith('<!-- derivative provenance:') and not b.startswith('## ') and b!='★']

page_cache={}
def page_norm(p):
    if p not in page_cache: page_cache[p]=norm((P/f'{p:03d}.md').read_text(encoding='utf-8'))
    return page_cache[p]
fallbacks=[]
def infer_pages(n,source_text,cursor_page):
    pages=list(scene_meta[n]['pdf_pages']); b=norm(source_text)
    exact=[p for p in pages if b and b in page_norm(p)]
    if exact:return [exact[0]],exact[0]
    first=b[:80] if len(b)>80 else b; last=b[-80:] if len(b)>80 else b
    fh=[p for p in pages if first and first in page_norm(p)]; lh=[p for p in pages if last and last in page_norm(p)]
    if fh and lh:
        a,z=fh[0],lh[-1]; return [p for p in pages if a<=p<=z],z
    p=cursor_page if cursor_page in pages else pages[0]
    fallbacks.append({'scene_ordinal':n,'source_text':b[:160],'fallback_pdf_page':p}); return [p],p

def page_prov(pages):return [{'pdf_page':int(p),'printed_page':int(p)-1} for p in pages]

def consume_dialogue(blocks,i,row):
    prefix=f"{row['speaker_label']}{row['source_delimiter']}"; first=blocks[i]
    if not first.startswith(prefix):return None
    target=norm(row['text']); acc=first[len(prefix):].strip(); j=i
    while True:
        a=norm(acc)
        if a==target:return j+1,acc
        if not target.startswith(a) or j+1>=len(blocks):return None
        acc+='\n'+blocks[j+1]; j+=1

def make_dialogue_unit(n,sid,unit_no,row,english):
    occurrence_id=DIALOGUE_OCCURRENCE_LINKS.get((n,row['id']))
    notes=list(DIALOGUE_NOTES.get((n,row['id']),[]))
    if occurrence_id:
        occ=perf[occurrence_id]; assert occ['source_scene_id']==sid
        if occ['authorship_status']=='unresolved-item-level': notes.append('Item-level lyric authorship remains unresolved; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to this occurrence.')
        elif occ['authorship_status']=='not-applicable-non-lyric-performance': notes.append('Linked source occurrence is non-lyric performance material; lyric authorship is not applicable.')
    return {'id':f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}','kind':'dialogue','status':'verified','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,'source':{'source_path':f'works/vandikkaran-magan/dialogues/records/scene-{n:03d}.json','canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{n:03d}.md','source_record_id':row['id'],'source_occurrence_id':occurrence_id,'source_locator':None,'speaker_label':row['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':row['source_delimiter'],'page_provenance':row['page_provenance']},'translation':{'english_text':english,'mode':'prose-faithful','notes':notes}}

def make_nd_unit(n,sid,unit_no,block,spec,locator_no,pages):
    skind=spec.get('kind','stage'); occurrence_id=spec.get('occurrence_id')
    locator_kind=spec.get('locator_kind') or ('source-unlabelled-speech' if skind=='source-unlabelled' else ('song-body' if skind=='song' else ('performance-cue' if skind=='performance-cue' else ('written-text' if skind=='written-text' else 'stage-direction'))))
    notes=list(spec.get('notes',[]))
    if occurrence_id:
        occ=perf[occurrence_id]; assert occ['source_scene_id']==sid
        if occ['authorship_status']=='unresolved-item-level':notes.append('Item-level lyric authorship remains unresolved; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to this occurrence.')
        elif occ['authorship_status']=='not-applicable-non-lyric-performance':notes.append('Linked source occurrence is non-lyric performance material; lyric authorship is not applicable.')
    if skind=='source-unlabelled':notes.append('The source prints no speaker label for this spoken unit; no speaker or immutable dialogue ID is inferred.')
    source={'source_path':f'works/vandikkaran-magan/scenes/scene-{n:03d}.md','canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{n:03d}.md','source_record_id':None,'source_occurrence_id':occurrence_id,'source_locator':{'kind':locator_kind,'ordinal':locator_no,'description':f'Source block {locator_no}: {norm(block)[:140]}'},'speaker_label':None,'speaker_label_origin':'source-unlabelled' if skind=='source-unlabelled' else None,'source_delimiter':None,'page_provenance':page_prov(pages)}
    kind='dialogue' if skind=='source-unlabelled' else ('song' if skind=='song' else ('performance-cue' if skind=='performance-cue' else ('written-text' if skind=='written-text' else 'stage-direction')))
    tr={'mode':'semantic-poetic-source-faithful' if skind=='song' else 'prose-faithful','notes':notes}
    if skind=='song':
        lines=spec['lines']; source_line_count=len([x for x in block.splitlines() if x.strip()]); assert len(lines)==source_line_count,(n,locator_no,len(lines),source_line_count,block); tr['english_lines']=lines
    else: tr['english_text']=spec['text']
    return {'id':f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}','kind':kind,'status':'verified','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,'source':source,'translation':tr}

new_scene_objects=[]
for n in TARGET_SCENES:
    sid=scene_meta[n]['scene_id']; rows=json.loads((D/f'scene-{n:03d}.json').read_text(encoding='utf-8')); blocks=source_blocks(n)
    dtrs=DIALOGUE_TRANSLATIONS[n]; nds=ND[n]; ri=ni=i=0; cursor=int(scene_meta[n]['pdf_pages'][0]); units=[]; locator_no=0
    while i<len(blocks):
        if ri<len(rows):
            matched=consume_dialogue(blocks,i,rows[ri])
            if matched:
                end_i,_=matched; row=rows[ri]; units.append(make_dialogue_unit(n,sid,len(units)+1,row,dtrs[row['id']]))
                for pp in row['page_provenance']:cursor=max(cursor,int(pp['pdf_page']))
                ri+=1;i=end_i;continue
        block=blocks[i]
        if ni>=len(nds):raise AssertionError(f'scene {n}: no non-dialogue spec left for source block: {block}')
        spec=nds[ni];locator_no+=1
        if spec.get('occurrence_id'):
            pages=[p for p in perf[spec['occurrence_id']]['source_pdf_pages'] if p in scene_meta[n]['pdf_pages']] or list(scene_meta[n]['pdf_pages']);cursor=max(cursor,max(pages))
        else:pages,cursor=infer_pages(n,block,cursor)
        units.append(make_nd_unit(n,sid,len(units)+1,block,spec,locator_no,pages));ni+=1;i+=1
    assert ri==len(rows),(n,'dialogues',ri,len(rows));assert ni==len(nds),(n,'ND',ni,len(nds))
    obj={'work_id':'vandikkaran-magan','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,'scene_status':'verified','unit_count':len(units),'units':units}
    (R/f'scene-{n:03d}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');new_scene_objects.append(obj)

assert not fallbacks,json.dumps(fallbacks,ensure_ascii=False,indent=2)
new_units=[u for s in new_scene_objects for u in s['units']]
new_links=[u['source']['source_record_id'] for u in new_units if u['source']['source_record_id']]
new_unlabelled=[u for u in new_units if u['source']['speaker_label_origin']=='source-unlabelled']
new_perf_units=[u for u in new_units if u['source']['source_occurrence_id']]
new_perf_ids=sorted({u['source']['source_occurrence_id'] for u in new_perf_units})
assert len(new_links)==len(set(new_links))==105
assert len(new_unlabelled)==6,len(new_unlabelled)
assert new_perf_ids==['vandikkaran-magan-perf-009'],new_perf_ids
new_counts=Counter(u['kind'] for u in new_units)
qa={'work_id':'vandikkaran-magan','phase':'english-translation-final-batch-061-072','status':'PASS','batch_size_scenes':12,'scene_ordinals':TARGET_SCENES,'source_scene_ids':EXPECTED_SOURCE_SCENE_IDS,'verified_scenes':12,'verified_units':len(new_units),'unit_kind_counts':dict(sorted(new_counts.items())),'immutable_dialogue_records_expected':105,'immutable_dialogue_records_linked':105,'source_unlabelled_spoken_units':len(new_unlabelled),'inferred_speaker_assignments':0,'performance_linked_units':len(new_perf_units),'performance_occurrence_ids_linked':new_perf_ids,'unique_performance_occurrence_links':1,'source_page_provenance_fallbacks':0,'checks':{'all_12_target_scenes_present_in_source_order':True,'all_batch_immutable_dialogue_records_linked_exactly_once':True,'cross_page_dialogue_records_preserved_as_single_translation_units':True,'source_unlabelled_speech_kept_unassigned_and_unlinked':True,'source_scene_53_ci_dance_song_linked_to_verified_perf_009_only':True,'item_level_song_authorship_left_unresolved':True,'structural_star_translated_as_prose':False,'synthetic_scene_end_prose_added':False,'closed_tamil_scene_dialogue_character_song_records_modified_by_translation':False},'next_activity':NEXT}
(T/'batch-061-072-qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Whole-work reconciliation.
all_objs=[json.loads((R/f'scene-{n:03d}.json').read_text(encoding='utf-8')) for n in range(1,73)]
assert [o['scene_ordinal'] for o in all_objs]==list(range(1,73));assert all(o['scene_status']=='verified' for o in all_objs)
all_units=[u for o in all_objs for u in o['units']];all_counts=Counter(u['kind'] for u in all_units)
all_ids=[u['id'] for u in all_units];assert len(all_ids)==len(set(all_ids))
all_links=[u['source']['source_record_id'] for u in all_units if u['source']['source_record_id']]
all_unlabelled=[u for u in all_units if u['source']['speaker_label_origin']=='source-unlabelled']
all_perf_units=[u for u in all_units if u['source']['source_occurrence_id']];all_perf_ids=sorted({u['source']['source_occurrence_id'] for u in all_perf_units})
assert len(all_links)==len(set(all_links))==773,len(all_links)
expected_all_ids=[]
for n in range(1,73):expected_all_ids.extend(r['id'] for r in json.loads((D/f'scene-{n:03d}.json').read_text(encoding='utf-8')))
assert set(all_links)==set(expected_all_ids)
assert len(all_unlabelled)==27,len(all_unlabelled)
assert all_perf_ids==[f'vandikkaran-magan-perf-{i:03d}' for i in range(1,10)],all_perf_ids
cross_page_units=sum(1 for u in all_units if len(u['source']['page_provenance'])>1)

idx={'work_id':'vandikkaran-magan','target_language':'en','status':'complete-verified','total_scene_derivatives':72,'verified_scenes':72,'verified_scene_ordinals':list(range(1,73)),'verified_source_scene_ids':[scene_meta[n]['scene_id'] for n in range(1,73)],'translation_units':len(all_units),'unit_kind_counts':dict(sorted(all_counts.items())),'immutable_dialogue_records_linked':773,'source_unlabelled_spoken_units':len(all_unlabelled),'performance_linked_units':len(all_perf_units),'performance_occurrence_links':9,'performance_occurrence_ids_linked':all_perf_ids,'cross_page_units':cross_page_units,'latest_batch_size_scenes':12,'schema':'schema.json','records_directory':'records/','pilot_qa':'pilot-qa.json','latest_batch_qa':'batch-061-072-qa.json','latest_batch_review':'BATCH_061_072_REVIEW.md','final_translation_qa':'FINAL_TRANSLATION_QA.md','next_activity':NEXT}
(T/'index.json').write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

(T/'BATCH_061_072_REVIEW.md').write_text(f'''# வண்டிக்காரன் மகன் — English final batch 061–072 review\n\n**PASS** — archive scenes **61–72 / 12 of 12 verified**.\n\n- verified units: **{len(new_units)}**;\n- immutable dialogue links: **105/105 exactly once**;\n- source-unlabelled spoken units: **6 / 0 inferred speakers**;\n- verified performance occurrence linked: **`vandikkaran-magan-perf-009` only**;\n- page-provenance fallbacks: **0**;\n- structural `★` prose: **0**;\n- synthetic scene-end prose: **0**;\n- upstream source-layer mutations: **0**.\n\nThe scene-68 lyrical dance body preserves one English line per visible Tamil line and leaves item-level lyric authorship unresolved. Scene 69 preserves three source-unlabelled spoken blocks without assigning speakers. Scene 71 preserves the unusual immutable `உமா` record that includes narration after her cry as one linked source unit rather than repartitioning closed authority.\n\n## Next\n\n{NEXT}\n''',encoding='utf-8')

(T/'FINAL_TRANSLATION_QA.md').write_text(f'''# வண்டிக்காரன் மகன் — Final English Translation QA\n\n**PASS — ENGLISH TRANSLATION COMPLETE-VERIFIED.**\n\n- scenes: **72/72 verified in canonical archive order**;\n- verified translation units: **{len(all_units)}**;\n- immutable dialogue records linked: **773/773 exactly once**;\n- source-unlabelled spoken units: **{len(all_unlabelled)} / 0 inferred speakers**;\n- verified song/performance occurrence identities linked: **9/9**;\n- cross-page translation units: **{cross_page_units}**;\n- duplicate translation unit IDs: **0**;\n- structural `★` translated as prose: **0**;\n- synthetic scene-end text: **0**;\n- closed Tamil / scene / dialogue / character / song authority modified by English: **no**.\n\nWhole-work reconciliation directly compares the 72 translation records against all immutable dialogue record files and confirms exact **773/773** ID coverage. All nine retained source-visible performance occurrence identities are represented without promoting unresolved item-level authorship.\n\n## Next\n\n{NEXT}\n''',encoding='utf-8')

(T/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — English translation\n\n**Status:** **COMPLETE-VERIFIED / 72 OF 72 / WHOLE-WORK QA PASS**\n\n- verified scenes: **72/72**;\n- cumulative translation units: **{len(all_units)}**;\n- unit kinds: **{', '.join(f'{k}={v}' for k,v in sorted(all_counts.items()))}**;\n- immutable dialogue links: **773/773 exactly once**;\n- source-unlabelled spoken units: **{len(all_unlabelled)}**, with **0 inferred speakers**;\n- unique song/performance occurrence links: **9/9** — `perf-001` through `perf-009`;\n- cross-page units: **{cross_page_units}**;\n- final batch: **archive scenes 61–72 / PASS / 105 of 105 immutable dialogue records linked exactly once**;\n- upstream source-layer mutations caused by translation: **0**.\n\nSee `batch-061-072-qa.json`, `BATCH_061_072_REVIEW.md`, `FINAL_TRANSLATION_QA.md`, `records/scene-061.json` through `records/scene-072.json`, and `index.json`.\n\n## Next\n\n{NEXT}\n''',encoding='utf-8')

print(json.dumps({'status':'PASS','batch_scenes':12,'batch_units':len(new_units),'batch_dialogue_links':105,'cumulative_scenes':72,'cumulative_units':len(all_units),'cumulative_dialogue_links':773,'source_unlabelled_spoken_units':len(all_unlabelled),'performance_occurrence_links':9,'cross_page_units':cross_page_units,'next':'reader-export'},ensure_ascii=False))
