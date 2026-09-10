#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json

W = Path(__file__).resolve().parents[1]
T = W / 'translations'
R = T / 'records'
N = W / 'notes'
D = W / 'dialogues' / 'records' / 'scene-001.json'
S = W / 'scenes' / 'scene-001.md'
T.mkdir(exist_ok=True); R.mkdir(exist_ok=True)

records = json.loads(D.read_text(encoding='utf-8'))
assert len(records) == 31
by_id = {r['id']: r for r in records}
assert len(by_id) == 31
expected_dialogue_order = [
 'vandikkaran-magan-s001-d001',
 'vandikkaran-magan-s001-d002','vandikkaran-magan-s001-d003','vandikkaran-magan-s001-d004','vandikkaran-magan-s001-d005','vandikkaran-magan-s001-d006','vandikkaran-magan-s001-d007','vandikkaran-magan-s001-d008','vandikkaran-magan-s001-d009','vandikkaran-magan-s001-d010',
 'vandikkaran-magan-s001-d011','vandikkaran-magan-s001-d012','vandikkaran-magan-s001-d013','vandikkaran-magan-s001-d014','vandikkaran-magan-s001-d015','vandikkaran-magan-s001-d016','vandikkaran-magan-s001-d017','vandikkaran-magan-s001-d018','vandikkaran-magan-s001-d019','vandikkaran-magan-s001-d020','vandikkaran-magan-s001-d021','vandikkaran-magan-s001-d022',
 'vandikkaran-magan-s001-d023','vandikkaran-magan-s001-d031','vandikkaran-magan-s001-d024','vandikkaran-magan-s001-d025','vandikkaran-magan-s001-d026','vandikkaran-magan-s001-d027','vandikkaran-magan-s001-d028','vandikkaran-magan-s001-d029','vandikkaran-magan-s001-d030'
]
assert [r['id'] for r in records] == expected_dialogue_order

translations = {
'd001':'Hey, Kalingarayar has arrived! The Zamindar will be here soon!',
'd002':'Zamindar Jambuling Bhoopathi!',
'd003':'Long live!',
'd004':'What is this wild crowd—“long live, long live, long live the sword” and all that! Properly, nicely, in keeping with our shastras and customs, will you shout, “Jai! Jai! to Zamindar Jambuling Bhoopathi”?',
'd005':'To Zamindar Jambuling Bhoopathi...',
'd006':'Jai!',
'd007':'Namaskaram to the elders! Blessings to the young!... Kalingaraya!...',
'd008':'My lord!',
'd009':'Hear their grievances!',
'd010':'As you command, my lord...',
'd011':'Get up... get up... All of you fall at my feet and worship me; what am I—a saint? A maharishi? A mahatma?... No! But one thing: you are not bowing at the feet of Zamindar Jambulingam!... You are touching and worshipping the feet of dharma! The feet of justice—the feet of integrity! What do you say, Kalingaraya?... Am I right?..',
'd012':'Who else can say it? We have to say it ourselves!',
'd013':'(to the woman who fell at his feet) What is your grievance, dear?',
'd014':'My husband drinks arrack all the time... he has brought the family to ruin!',
'd015':'Alas! Alas! Should womankind shed tears? And that too before my eyes? I simply cannot bear the tears of womankind... Kalinga!... Summon this lady’s husband and give him the proper order!... (to the woman) Don’t worry, mother!... It is our responsibility to reform your husband... Kalinga! One more order—and it must take effect immediately. Not even the smell of liquor should be allowed within the boundaries of our estate.',
'd016':'Only within our boundaries, right!... We can enforce that.',
'd018':'Kalinga!: Who is that man?...',
'd019':'A Tamil poet, sir!',
'd020':'You can tell from the flattery itself!..',
'd021':'Don’t say that about all poets! There are poets who stand firm... and there are poets who keep time to suit the occasion!..',
'd022':'Kalinga... don’t hurt the poet’s feelings! Poet! What do you want?',
'd023':'Here... my wife died, leaving me with this girl, Poongodi!... I am struggling with a motherless child!..',
'd031':'(lifting the child) Oh, poor thing!... She is like a little golden doll... Child... Have you got a cold, dear?... (wipes her nose.)',
'd024':'Thank you, sir, thank you!....',
'd025':'Kalinga! Is the carriage ready?.... Where is the coachman?....',
'd026':'Hey, Sadaiya!... Sadaiya!..',
'd027':'Master... the carriage is ready!..',
'd028':'Appa! I’ll come too, Appa!',
'd029':'Uma! No, dear... go and play... Appa will go to the temple and come back!',
'd030':'Children shouldn’t go to the temple!... Come, dear, come with me!'
}
poet_lines = [
 "Even if the rains fail, Pari’s generosity never fails!",
 "Kumanan was ready even to give his head!",
 "Karna gave away as a gift",
 "all the righteous deeds he had done! As Pari—as Kumanan—",
 "as Karna, long live the munificent lord who gives!...",
 "Long live!...."
]
assert set(translations) == {f'd{i:03d}' for i in list(range(1,17))+list(range(18,32)) if i != 17}

units=[]
SCENE_PATH='works/vandikkaran-magan/scenes/scene-001.md'
DIALOGUE_PATH='works/vandikkaran-magan/dialogues/records/scene-001.json'

def base(kind, page, translation, locator_kind=None, description=None, notes=None):
    u={
      'id':f'vandikkaran-magan-en-s001-u{len(units)+1:03d}',
      'kind':kind,'status':'verified','target_language':'en','scene_id':'vandikkaran-magan-s001','scene_ordinal':1,'source_scene_id':'1',
      'source':{
        'source_path':SCENE_PATH,'canonical_scene_path':SCENE_PATH,'source_record_id':None,'source_occurrence_id':None,
        'source_locator':({'kind':locator_kind,'ordinal':len([x for x in units if x["source"]["source_locator"] is not None])+1,'description':description} if locator_kind else None),
        'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,
        'page_provenance':[{'pdf_page':page,'printed_page':page-1}]
      },
      'translation':{'english_text':translation,'mode':'prose-faithful','notes':notes or []}
    }
    units.append(u)

def dialog(rid):
    r=by_id[rid]
    suffix=rid.rsplit('-',1)[1]
    if suffix=='d017':
        tr={'english_lines':poet_lines,'mode':'semantic-poetic-source-faithful','notes':['The six printed Tamil lines remain one immutable dialogue-linked translation unit; they are not promoted to a song/performance occurrence.']}
    else:
        tr={'english_text':translations[suffix],'mode':'prose-faithful','notes':[]}
    units.append({
      'id':f'vandikkaran-magan-en-s001-u{len(units)+1:03d}',
      'kind':'dialogue','status':'verified','target_language':'en','scene_id':'vandikkaran-magan-s001','scene_ordinal':1,'source_scene_id':'1',
      'source':{
        'source_path':DIALOGUE_PATH,'canonical_scene_path':SCENE_PATH,'source_record_id':rid,'source_occurrence_id':None,'source_locator':None,
        'speaker_label':r['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':r['source_delimiter'],'page_provenance':r['page_provenance']
      },
      'translation':tr
    })

base('stage-direction',6,'Exterior of the zamindar’s palace.','location-caption','Source location caption `ஜமீன்மாளிகை வெளிப்புறம்`.')
base('stage-direction',6,'(A crowd of townspeople has gathered... They are talking among themselves in a constant murmur.... With a loud cry of “Silence!”, Kalingarayan opens the door and comes out...)','stage-direction','Opening crowd and Kalingarayan entrance.')
dialog('vandikkaran-magan-s001-d001')
base('stage-direction',6,'(Everyone looks toward the entrance—the zamindar arrives.)','stage-direction','The crowd turns toward the entrance.')
for n in range(2,11): dialog(f'vandikkaran-magan-s001-d{n:03d}')
base('stage-direction',7,'(A woman hands a petition to the zamindar—he receives it kindly—and the woman falls at the zamindar’s feet in reverence.)','stage-direction','Petition handover and prostration.')
for n in range(11,23): dialog(f'vandikkaran-magan-s001-d{n:03d}')
dialog('vandikkaran-magan-s001-d023')
dialog('vandikkaran-magan-s001-d031')
base('stage-direction',8,'(The people look on in amazement; the child is handed back to the poet.)','stage-direction','Stage portion of a mixed source block before unlabelled speech.',['The source does not explicitly name the actor handing the child back in this unlabelled block; the English does not infer one.'])
base('dialogue',8,'Poet! Don’t worry. Every month, money will be sent from the estate to raise and educate this child. Leave your address with Manager Kalingarayan before you go...','source-unlabelled-speech','Unlabelled speech following the mixed stage cue.',['The source prints no speaker label for this utterance; it remains unassigned and is not linked to an immutable dialogue record.'])
units[-1]['source']['speaker_label_origin']='source-unlabelled'
dialog('vandikkaran-magan-s001-d024')
base('stage-direction',8,'(Petitions pile up with Kalinga.)','stage-direction','Petitions accumulate with Kalinga.')
dialog('vandikkaran-magan-s001-d025'); dialog('vandikkaran-magan-s001-d026')
base('stage-direction',8,'(Sadaiyan runs in carrying Uma.)','stage-direction','Sadaiyan enters carrying Uma.')
for n in range(27,31): dialog(f'vandikkaran-magan-s001-d{n:03d}')
base('stage-direction',8,'(The zamindar comes and sits in the carriage. Sadaiyan climbs onto the carriage and drives—the carriage departs.)','stage-direction','Scene-closing carriage departure.')

assert len(units)==40
linked=[u['source']['source_record_id'] for u in units if u['source']['source_record_id']]
assert linked==expected_dialogue_order
assert len(linked)==31 and len(set(linked))==31
assert Counter(u['kind'] for u in units)==Counter({'dialogue':32,'stage-direction':8})
assert sum(u['source']['speaker_label_origin']=='source-unlabelled' for u in units)==1
assert all(u['source']['source_occurrence_id'] is None for u in units)

scene={
 'work_id':'vandikkaran-magan','target_language':'en','scene_id':'vandikkaran-magan-s001','scene_ordinal':1,'source_scene_id':'1',
 'pilot_status':'verified','scene_status':'verified','unit_count':40,'units':units
}
(R/'scene-001.json').write_text(json.dumps(scene,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

schema={
 '$schema':'https://json-schema.org/draft/2020-12/schema','$id':'vandikkaran-magan-translation-scene-record-schema',
 'title':'Vandikkaran Magan source-linked English translation scene record','type':'object',
 'required':['work_id','target_language','scene_id','scene_ordinal','source_scene_id','scene_status','unit_count','units'],
 'properties':{
  'work_id':{'const':'vandikkaran-magan'},'target_language':{'const':'en'},'scene_id':{'type':'string','pattern':'^vandikkaran-magan-s[0-9]{3}$'},
  'scene_ordinal':{'type':'integer','minimum':1,'maximum':72},'source_scene_id':{'type':'string','minLength':1},
  'pilot_status':{'enum':['draft','review','verified']},'scene_status':{'enum':['draft','review','verified']},'unit_count':{'type':'integer','minimum':0},
  'units':{'type':'array','items':{'$ref':'#/$defs/unit'}}
 },'additionalProperties':False,
 '$defs':{
  'page':{'type':'object','required':['pdf_page','printed_page'],'properties':{'pdf_page':{'type':'integer','minimum':1},'printed_page':{'type':['integer','null'],'minimum':1}},'additionalProperties':False},
  'locator':{'type':['object','null'],'required':['kind','ordinal','description'],'properties':{'kind':{'type':'string'},'ordinal':{'type':'integer','minimum':1},'description':{'type':'string'}},'additionalProperties':False},
  'source':{'type':'object','required':['source_path','canonical_scene_path','source_record_id','source_occurrence_id','source_locator','speaker_label','speaker_label_origin','source_delimiter','page_provenance'],'properties':{
   'source_path':{'type':'string','minLength':1},'canonical_scene_path':{'type':'string','minLength':1},'source_record_id':{'type':['string','null']},'source_occurrence_id':{'type':['string','null']},
   'source_locator':{'$ref':'#/$defs/locator'},'speaker_label':{'type':['string','null']},'speaker_label_origin':{'type':['string','null'],'enum':['source-explicit','source-unlabelled',None]},'source_delimiter':{'type':['string','null']},
   'page_provenance':{'type':'array','minItems':1,'items':{'$ref':'#/$defs/page'}}},'additionalProperties':False},
  'translation':{'type':'object','properties':{'english_text':{'type':'string','minLength':1},'english_lines':{'type':'array','minItems':1,'items':{'type':'string','minLength':1}},'mode':{'enum':['prose-faithful','semantic-poetic-source-faithful']},'notes':{'type':'array','items':{'type':'string'}}},'oneOf':[{'required':['english_text','mode','notes']},{'required':['english_lines','mode','notes']}],'additionalProperties':False},
  'unit':{'type':'object','required':['id','kind','status','target_language','scene_id','scene_ordinal','source_scene_id','source','translation'],'properties':{
   'id':{'type':'string','pattern':'^vandikkaran-magan-en-s[0-9]{3}-u[0-9]{3}$'},'kind':{'enum':['narrative','dialogue','stage-direction','performance-cue','song','written-text','chant']},'status':{'enum':['draft','review','verified']},'target_language':{'const':'en'},'scene_id':{'type':'string'},'scene_ordinal':{'type':'integer'},'source_scene_id':{'type':'string'},'source':{'$ref':'#/$defs/source'},'translation':{'$ref':'#/$defs/translation'}},'additionalProperties':False}
 }
}
(T/'schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

NEXT='Translate and verify archive scene ordinals 2–5 (source scene IDs `2`, `3`, `4`, `4-எ`) as the first bounded post-pilot English batch. Preserve source order and exact Tamil label/provenance metadata; link each explicit utterance to its reconciled immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; link only verified song/performance occurrences; do not modify closed Tamil, scene, dialogue, character or song records.'
index={
 'work_id':'vandikkaran-magan','target_language':'en','status':'pilot-verified','total_scene_derivatives':72,'verified_scenes':1,
 'verified_scene_ordinals':[1],'verified_source_scene_ids':['1'],'translation_units':40,'unit_kind_counts':{'dialogue':32,'stage-direction':8},
 'immutable_dialogue_records_linked':31,'source_unlabelled_spoken_units':1,'performance_occurrence_links':0,'cross_page_units':0,
 'schema':'schema.json','records_directory':'records/','pilot_qa':'pilot-qa.json','next_activity':NEXT
}
(T/'index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

qa={
 'work_id':'vandikkaran-magan','phase':'english-translation-pilot','status':'PASS','scene_ordinal':1,'source_scene_id':'1','verified_units':40,
 'unit_kind_counts':{'dialogue':32,'stage-direction':8},'immutable_dialogue_records_expected':31,'immutable_dialogue_records_linked':31,
 'source_unlabelled_spoken_units':1,'inferred_speaker_assignments':0,'performance_occurrences_expected':0,'performance_occurrence_links':0,'cross_page_units':0,
 'checks':{
  'all_scene1_immutable_dialogue_records_linked_exactly_once':True,'dialogue_source_order_preserved_including_append_only_d031':True,
  'source_unlabelled_speech_kept_unassigned_and_unlinked':True,'mixed_stage_and_unlabelled_speech_span_not_duplicated':True,
  'structural_star_translated_as_prose':False,'synthetic_scene_end_prose_added':False,'song_or_authorship_invented':False,
  'closed_tamil_scene_dialogue_character_song_records_modified_by_translation':False
 },'next_activity':NEXT
}
(T/'pilot-qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

(T/'PILOT_REVIEW.md').write_text('''# வண்டிக்காரன் மகன் — English translation pilot review\n\nStatus: **PASS / PILOT-VERIFIED**\n\nSource scene **1** (archive scene ordinal 1; PDF 6–8 / printed 5–7) is translated as **40 verified units**: **31 source-explicit dialogue links + 1 source-unlabelled spoken unit + 8 stage/location units**.\n\nThe pilot was built only after reconciling the late dialogue parser collision: scene 1 now contains **31 immutable dialogue records**, including append-only repair `vandikkaran-magan-s001-d031` in its correct source-order position. All 31 are linked exactly once. The following `புலவரே! கவலை வேண்டாம்...` utterance has no printed speaker label and remains unassigned/unlinked. The preceding parenthetical action is a separate stage unit without inferring an actor.\n\nThe poet’s six-line praise remains one dialogue-linked poetic translation unit; it is not reclassified as a song. Scene 1 contains no retained song/performance occurrence. Decorative `★` is not translated as prose. No frozen Tamil, scene, dialogue, character or song record was altered by the translation layer.\n\n**Next:** archive scene ordinals 2–5 (source IDs `2`, `3`, `4`, `4-எ`).\n''',encoding='utf-8')
(T/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — English translation\n\n**Status:** **PILOT-VERIFIED / QA PASS**\n\n- scene 1 / 72 verified;\n- **40** translation units;\n- **31/31** scene-1 immutable dialogue records linked exactly once;\n- **1** source-unlabelled spoken unit retained without speaker inference;\n- **8** stage/location units;\n- **0** scene-1 performance occurrences;\n- upstream source-layer mutations caused by translation: **0**.\n\nSee `records/scene-001.json`, `pilot-qa.json`, and `PILOT_REVIEW.md`.\n\n## Next\n\n{NEXT}\n''',encoding='utf-8')
print(json.dumps({'status':'PASS','scene':1,'units':40,'dialogue_links':31,'unlabelled_speech':1,'stage_units':8},ensure_ascii=False))
