#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, re

from translation_batch_041_060_data_a import DIALOGUE_TRANSLATIONS as DA, DIALOGUE_NOTES as NA, ND as NDA, DIALOGUE_OCCURRENCE_LINKS as OA
from translation_batch_041_060_data_b import DIALOGUE_TRANSLATIONS as DB, DIALOGUE_NOTES as NB, ND as NDB, DIALOGUE_OCCURRENCE_LINKS as OB
from translation_batch_041_060_data_c import DIALOGUE_TRANSLATIONS as DC, DIALOGUE_NOTES as NC, ND as NDC, DIALOGUE_OCCURRENCE_LINKS as OC
from translation_batch_041_060_data_d import DIALOGUE_TRANSLATIONS as DD, DIALOGUE_NOTES as NDNOTE, ND as NDD, DIALOGUE_OCCURRENCE_LINKS as OD

W = Path(__file__).resolve().parents[1]
T = W / 'translations'
R = T / 'records'
D = W / 'dialogues' / 'records'
S = W / 'scenes'
P = W / 'transcription' / 'pages'
R.mkdir(parents=True, exist_ok=True)

TARGET_SCENES = list(range(41, 61))
BATCH_SIZE = 20
NEXT = (
    'Translate and verify the remaining archive scene ordinals 61–72 as the final 12-scene English batch. '
    'Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; '
    'keep source-unlabelled speech unassigned; link only verified song/performance occurrences; preserve unresolved item-level '
    'authorship as unresolved; and do not modify closed Tamil, scene, dialogue-record, character-mapping or song-record authorities.'
)

DIALOGUE_TRANSLATIONS = {}; DIALOGUE_NOTES = {}; ND = {}; DIALOGUE_OCCURRENCE_LINKS = {}
for src in (DA, DB, DC, DD):
    assert not (set(DIALOGUE_TRANSLATIONS) & set(src)); DIALOGUE_TRANSLATIONS.update(src)
for src in (NA, NB, NC, NDNOTE):
    assert not (set(DIALOGUE_NOTES) & set(src)); DIALOGUE_NOTES.update(src)
for src in (NDA, NDB, NDC, NDD):
    assert not (set(ND) & set(src)); ND.update(src)
for src in (OA, OB, OC, OD):
    assert not (set(DIALOGUE_OCCURRENCE_LINKS) & set(src)); DIALOGUE_OCCURRENCE_LINKS.update(src)
assert set(DIALOGUE_TRANSLATIONS) == set(TARGET_SCENES)
assert set(ND) == set(TARGET_SCENES)

# Closed upstream authority.
didx = json.loads((W/'dialogues'/'index.json').read_text(encoding='utf-8'))
cidx = json.loads((W/'characters'/'index.json').read_text(encoding='utf-8'))
songidx = json.loads((W/'songs'/'index.json').read_text(encoding='utf-8'))
assert didx['status'] == 'complete-verified-reconciled' and didx['dialogue_record_count'] == 773
assert cidx['status'] == 'complete-verified' and cidx['dialogue_record_coverage'] == '773/773'
assert songidx['status'] == 'complete-verified-source-only' and songidx['mapped_source_visible_occurrences'] == 9

scene_index_obj = json.loads((S/'index.json').read_text(encoding='utf-8'))
scene_rows = scene_index_obj['scenes']
scene_meta = {int(x['ordinal']): x for x in scene_rows}
EXPECTED_SOURCE_SCENE_IDS = [scene_meta[n]['scene_id'] for n in TARGET_SCENES]
assert EXPECTED_SOURCE_SCENE_IDS == ['30','31','32','33','33-எ','34','35','36','37','38','39','40','41','42','42-எ','43','44','45-46','47','48']

song_inventory = json.loads((W/'songs'/'inventory.json').read_text(encoding='utf-8'))
perf = {x['id']: x for x in song_inventory['records']}
assert perf['vandikkaran-magan-perf-005']['source_scene_id'] == '32'
assert perf['vandikkaran-magan-perf-006']['source_scene_id'] == '36'
assert perf['vandikkaran-magan-perf-007']['source_scene_id'] == '42-எ'
assert perf['vandikkaran-magan-perf-008']['source_scene_id'] == '48'

expected_counts = {n: int(didx['scene_record_counts'][f'vandikkaran-magan-s{n:03d}']) for n in TARGET_SCENES}
for n in TARGET_SCENES:
    assert len(DIALOGUE_TRANSLATIONS[n]) == expected_counts[n], (n, len(DIALOGUE_TRANSLATIONS[n]), expected_counts[n])
assert sum(expected_counts.values()) == 156, sum(expected_counts.values())


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
def infer_pages(n, source_text, cursor_page):
    pages=list(scene_meta[n]['pdf_pages']); b=norm(source_text)
    exact=[p for p in pages if b and b in page_norm(p)]
    if exact: return [exact[0]], exact[0]
    first=b[:80] if len(b)>80 else b; last=b[-80:] if len(b)>80 else b
    fh=[p for p in pages if first and first in page_norm(p)]; lh=[p for p in pages if last and last in page_norm(p)]
    if fh and lh:
        a,z=fh[0],lh[-1]; return [p for p in pages if a<=p<=z], z
    p=cursor_page if cursor_page in pages else pages[0]
    fallbacks.append({'scene_ordinal':n,'source_text':b[:160],'fallback_pdf_page':p}); return [p],p

def page_prov(pages): return [{'pdf_page':int(p),'printed_page':int(p)-1} for p in pages]

def consume_dialogue(blocks,i,row):
    prefix=f"{row['speaker_label']}{row['source_delimiter']}"
    first=blocks[i]
    if not first.startswith(prefix): return None
    target=norm(row['text']); acc=first[len(prefix):].strip(); j=i
    while True:
        a=norm(acc)
        if a==target: return j+1,acc
        if not target.startswith(a) or j+1>=len(blocks): return None
        acc += '\n' + blocks[j+1]; j += 1

def make_dialogue_unit(n,sid,unit_no,row,english,notes):
    occurrence_id=DIALOGUE_OCCURRENCE_LINKS.get((n,row['id']))
    if occurrence_id:
        occ=perf[occurrence_id]
        assert occ['source_scene_id']==sid
        if occ['authorship_status']=='unresolved-item-level':
            notes=list(notes)+['Item-level lyric authorship remains unresolved; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to this occurrence.']
        elif occ['authorship_status']=='not-applicable-non-lyric-performance':
            notes=list(notes)+['Linked source occurrence is non-lyric performance material; lyric authorship is not applicable.']
    return {
      'id':f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}','kind':'dialogue','status':'verified','target_language':'en',
      'scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,
      'source':{'source_path':f'works/vandikkaran-magan/dialogues/records/scene-{n:03d}.json','canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{n:03d}.md','source_record_id':row['id'],'source_occurrence_id':occurrence_id,'source_locator':None,'speaker_label':row['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':row['source_delimiter'],'page_provenance':row['page_provenance']},
      'translation':{'english_text':english,'mode':'prose-faithful','notes':notes}}

def make_nd_unit(n,sid,unit_no,block,spec,locator_no,pages):
    skind=spec.get('kind','stage'); occurrence_id=spec.get('occurrence_id')
    locator_kind=spec.get('locator_kind') or ('source-unlabelled-speech' if skind=='source-unlabelled' else ('song-body' if skind=='song' else ('performance-cue' if skind=='performance-cue' else 'stage-direction')))
    notes=list(spec.get('notes',[]))
    if occurrence_id:
        occ=perf[occurrence_id]; assert occ['source_scene_id']==sid
        if occ['authorship_status']=='unresolved-item-level': notes.append('Item-level lyric authorship remains unresolved; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to this occurrence.')
        elif occ['authorship_status']=='not-applicable-non-lyric-performance': notes.append('Linked source occurrence is non-lyric performance material; lyric authorship is not applicable.')
    if skind=='source-unlabelled': notes.append('The source prints no speaker label for this spoken unit; no speaker or immutable dialogue ID is inferred.')
    source={'source_path':f'works/vandikkaran-magan/scenes/scene-{n:03d}.md','canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{n:03d}.md','source_record_id':None,'source_occurrence_id':occurrence_id,'source_locator':{'kind':locator_kind,'ordinal':locator_no,'description':f'Source block {locator_no}: {norm(block)[:140]}'},'speaker_label':None,'speaker_label_origin':'source-unlabelled' if skind=='source-unlabelled' else None,'source_delimiter':None,'page_provenance':page_prov(pages)}
    kind='dialogue' if skind=='source-unlabelled' else ('song' if skind=='song' else ('performance-cue' if skind=='performance-cue' else 'stage-direction'))
    tr={'mode':'semantic-poetic-source-faithful' if skind=='song' else 'prose-faithful','notes':notes}
    if skind=='song':
        lines=spec['lines']; source_line_count=len([x for x in block.splitlines() if x.strip()]); assert len(lines)==source_line_count,(n,locator_no,len(lines),source_line_count,block); tr['english_lines']=lines
    else: tr['english_text']=spec['text']
    return {'id':f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}','kind':kind,'status':'verified','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,'source':source,'translation':tr}

new_scene_objects=[]
for n in TARGET_SCENES:
    sid=scene_meta[n]['scene_id']; rows=json.loads((D/f'scene-{n:03d}.json').read_text(encoding='utf-8')); blocks=source_blocks(n)
    dtrs=DIALOGUE_TRANSLATIONS[n]; nds=ND[n]; ri=di=ni=i=0; cursor=int(scene_meta[n]['pdf_pages'][0]); units=[]; locator_no=0
    while i<len(blocks):
        if ri<len(rows):
            matched=consume_dialogue(blocks,i,rows[ri])
            if matched:
                end_i,_=matched; row=rows[ri]; notes=list(DIALOGUE_NOTES.get((n,di+1),[])); units.append(make_dialogue_unit(n,sid,len(units)+1,row,dtrs[di],notes))
                for pp in row['page_provenance']: cursor=max(cursor,int(pp['pdf_page']))
                ri+=1; di+=1; i=end_i; continue
        block=blocks[i]
        if ni>=len(nds): raise AssertionError(f'scene {n}: no non-dialogue spec left for source block: {block}')
        spec=nds[ni]; locator_no+=1
        if spec.get('occurrence_id'):
            pages=list(perf[spec['occurrence_id']]['source_pdf_pages']); pages=[p for p in pages if p in scene_meta[n]['pdf_pages']] or list(scene_meta[n]['pdf_pages']); cursor=max(cursor,max(pages))
        else: pages,cursor=infer_pages(n,block,cursor)
        units.append(make_nd_unit(n,sid,len(units)+1,block,spec,locator_no,pages)); ni+=1; i+=1
    assert ri==len(rows),(n,'dialogues',ri,len(rows)); assert di==len(dtrs); assert ni==len(nds),(n,'ND',ni,len(nds))
    obj={'work_id':'vandikkaran-magan','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,'scene_status':'verified','unit_count':len(units),'units':units}
    (R/f'scene-{n:03d}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); new_scene_objects.append(obj)

assert not fallbacks, json.dumps(fallbacks,ensure_ascii=False,indent=2)
new_units=[u for s in new_scene_objects for u in s['units']]
new_links=[u['source']['source_record_id'] for u in new_units if u['source']['source_record_id']]
new_unlabelled=[u for u in new_units if u['source']['speaker_label_origin']=='source-unlabelled']
new_perf_units=[u for u in new_units if u['source']['source_occurrence_id']]
new_perf_ids=sorted({u['source']['source_occurrence_id'] for u in new_perf_units})
assert len(new_links)==156 and len(set(new_links))==156
assert len(new_unlabelled)==8,len(new_unlabelled)
assert new_perf_ids==['vandikkaran-magan-perf-005','vandikkaran-magan-perf-006','vandikkaran-magan-perf-007','vandikkaran-magan-perf-008'],new_perf_ids
new_counts=Counter(u['kind'] for u in new_units)
qa={'work_id':'vandikkaran-magan','phase':'english-translation-batch-041-060','status':'PASS','batch_size_scenes':20,'scene_ordinals':TARGET_SCENES,'source_scene_ids':EXPECTED_SOURCE_SCENE_IDS,'verified_scenes':20,'verified_units':len(new_units),'unit_kind_counts':dict(sorted(new_counts.items())),'immutable_dialogue_records_expected':156,'immutable_dialogue_records_linked':156,'source_unlabelled_spoken_units':len(new_unlabelled),'inferred_speaker_assignments':0,'performance_linked_units':len(new_perf_units),'performance_occurrence_ids_linked':new_perf_ids,'unique_performance_occurrence_links':4,'source_page_provenance_fallbacks':0,'checks':{'all_20_target_scenes_present_in_source_order':True,'all_batch_immutable_dialogue_records_linked_exactly_once':True,'cross_page_dialogue_records_preserved_as_single_translation_units':True,'source_unlabelled_speech_kept_unassigned_and_unlinked':True,'source_scene_32_wedding_music_cue_linked_to_verified_perf_005':True,'source_scene_36_song_linked_to_verified_perf_006':True,'source_scene_42_e_mantra_cue_linked_to_verified_perf_007':True,'source_scene_48_celebration_song_linked_to_verified_perf_008':True,'item_level_song_authorship_left_unresolved_where_applicable':True,'structural_star_translated_as_prose':False,'synthetic_scene_end_prose_added':False,'closed_tamil_scene_dialogue_character_song_records_modified_by_translation':False},'next_activity':NEXT}
(T/'batch-041-060-qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(T/'BATCH_041_060_REVIEW.md').write_text(f'''# வண்டிக்காரன் மகன் — English scenes 41–60 review

Status: **PASS / VERIFIED**

This iteration follows the user-requested **20-scene English batch** rule.

- archive scene ordinals: **41–60 / 20 scenes**;
- source scene IDs: `{', '.join(EXPECTED_SOURCE_SCENE_IDS)}`;
- verified translation units: **{len(new_units)}**;
- immutable dialogue records linked: **156/156 exactly once**;
- source-unlabelled spoken units: **{len(new_unlabelled)}**, retained without speaker inference;
- verified performance occurrences linked: **4** — `perf-005` through `perf-008`;
- source-page provenance fallbacks: **0**;
- upstream canonical Tamil / scene text / immutable dialogue records / character mappings / song records rewritten: **0**.

The source-scene-32 wedding-music cue is linked as non-lyric performance material; source scene 36's complete printed song is linked to `perf-006`; source scene `42-எ` retains only its printed mantra-sound cue under `perf-007`; and source scene 48's celebration song is linked to `perf-008` without promoting the film-level Vaali credit to item-level authorship.

**Next:** {NEXT}
''',encoding='utf-8')

all_scene_objs=[]
for n in range(1,61):
    obj=json.loads((R/f'scene-{n:03d}.json').read_text(encoding='utf-8')); assert obj['scene_status']=='verified' and obj['scene_ordinal']==n; all_scene_objs.append(obj)
all_units=[u for s in all_scene_objs for u in s['units']]; all_counts=Counter(u['kind'] for u in all_units)
all_links=[u['source']['source_record_id'] for u in all_units if u['source']['source_record_id']]
all_unlabelled=[u for u in all_units if u['source']['speaker_label_origin']=='source-unlabelled']
all_perf_units=[u for u in all_units if u['source']['source_occurrence_id']]; all_perf_ids=sorted({u['source']['source_occurrence_id'] for u in all_perf_units})
assert len(all_links)==len(set(all_links))==668,len(all_links)
assert len(all_unlabelled)==21,len(all_unlabelled)
assert all_perf_ids==[f'vandikkaran-magan-perf-{i:03d}' for i in range(1,9)],all_perf_ids
cross_page_units=sum(1 for u in all_units if len(u['source']['page_provenance'])>1)
idx={'work_id':'vandikkaran-magan','target_language':'en','status':'verified-through-scene-060','total_scene_derivatives':72,'verified_scenes':60,'verified_scene_ordinals':list(range(1,61)),'verified_source_scene_ids':[scene_meta[n]['scene_id'] for n in range(1,61)],'translation_units':len(all_units),'unit_kind_counts':dict(sorted(all_counts.items())),'immutable_dialogue_records_linked':len(all_links),'source_unlabelled_spoken_units':len(all_unlabelled),'performance_linked_units':len(all_perf_units),'performance_occurrence_links':len(all_perf_ids),'performance_occurrence_ids_linked':all_perf_ids,'cross_page_units':cross_page_units,'batch_size_scenes':20,'schema':'schema.json','records_directory':'records/','pilot_qa':'pilot-qa.json','latest_batch_qa':'batch-041-060-qa.json','latest_batch_review':'BATCH_041_060_REVIEW.md','next_activity':NEXT}
(T/'index.json').write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(T/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — English translation

**Status:** **VERIFIED THROUGH ARCHIVE SCENE 060 / QA PASS**

- verified scenes: **60/72**;
- verified archive scene ordinals: **1–60**;
- cumulative translation units: **{len(all_units)}**;
- unit kinds: **{', '.join(f'{k}={v}' for k,v in sorted(all_counts.items()))}**;
- immutable dialogue links: **{len(all_links)}**;
- source-unlabelled spoken units: **{len(all_unlabelled)}**, with **0 inferred speakers**;
- unique song/performance occurrence links: **{len(all_perf_ids)}** — `perf-001` through `perf-008`;
- production batch size: **20 scenes per full iteration**;
- latest batch: **archive scenes 41–60 / PASS / 156 of 156 immutable dialogue records linked exactly once**;
- upstream source-layer mutations caused by translation: **0**.

See `batch-041-060-qa.json`, `BATCH_041_060_REVIEW.md`, `records/scene-041.json` through `records/scene-060.json`, and `index.json`.

## Next

{NEXT}
''',encoding='utf-8')
print(json.dumps({'status':'PASS','batch':'41-60','batch_scenes':20,'batch_units':len(new_units),'batch_dialogue_links':len(new_links),'batch_source_unlabelled':len(new_unlabelled),'cumulative_scenes':60,'cumulative_units':len(all_units),'cumulative_dialogue_links':len(all_links),'cumulative_source_unlabelled':len(all_unlabelled),'cumulative_performance_occurrences':len(all_perf_ids),'cross_page_units':cross_page_units,'next':'61-72'},ensure_ascii=False,indent=2))
