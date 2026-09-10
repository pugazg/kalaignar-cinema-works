#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json

W=Path(__file__).resolve().parents[1]
T=W/'translations'; R=T/'records'; D=W/'dialogues'/'records'; S=W/'scenes'
R.mkdir(parents=True,exist_ok=True)

# Closed upstream gates must be reconciled before translation continues.
didx=json.loads((W/'dialogues'/'index.json').read_text(encoding='utf-8'))
cidx=json.loads((W/'characters'/'index.json').read_text(encoding='utf-8'))
sidx=json.loads((W/'songs'/'index.json').read_text(encoding='utf-8'))
assert didx['status']=='complete-verified-reconciled' and didx['dialogue_record_count']==773
assert cidx['status']=='complete-verified' and cidx['dialogue_record_coverage']=='773/773'
assert sidx['status']=='complete-verified-source-only'


def load_records(n):
    rows=json.loads((D/f'scene-{n:03d}.json').read_text(encoding='utf-8'))
    return rows,{r['id']:r for r in rows}

def stage(units,scene_ordinal,source_scene_id,page,text,kind='stage-direction',description='Source stage direction.'):
    units.append({
      'id':f'vandikkaran-magan-en-s{scene_ordinal:03d}-u{len(units)+1:03d}',
      'kind':'stage-direction','status':'verified','target_language':'en',
      'scene_id':f'vandikkaran-magan-s{scene_ordinal:03d}','scene_ordinal':scene_ordinal,'source_scene_id':source_scene_id,
      'source':{
        'source_path':f'works/vandikkaran-magan/scenes/scene-{scene_ordinal:03d}.md',
        'canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{scene_ordinal:03d}.md',
        'source_record_id':None,'source_occurrence_id':None,
        'source_locator':{'kind':kind,'ordinal':sum(1 for u in units if u['source']['source_locator'] is not None)+1,'description':description},
        'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,
        'page_provenance':[{'pdf_page':page,'printed_page':page-1}]},
      'translation':{'english_text':text,'mode':'prose-faithful','notes':[]}
    })

def unlabelled(units,scene_ordinal,source_scene_id,page,text,description):
    units.append({
      'id':f'vandikkaran-magan-en-s{scene_ordinal:03d}-u{len(units)+1:03d}',
      'kind':'dialogue','status':'verified','target_language':'en',
      'scene_id':f'vandikkaran-magan-s{scene_ordinal:03d}','scene_ordinal':scene_ordinal,'source_scene_id':source_scene_id,
      'source':{
        'source_path':f'works/vandikkaran-magan/scenes/scene-{scene_ordinal:03d}.md',
        'canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{scene_ordinal:03d}.md',
        'source_record_id':None,'source_occurrence_id':None,
        'source_locator':{'kind':'source-unlabelled-speech','ordinal':sum(1 for u in units if u['source']['source_locator'] is not None)+1,'description':description},
        'speaker_label':None,'speaker_label_origin':'source-unlabelled','source_delimiter':None,
        'page_provenance':[{'pdf_page':page,'printed_page':page-1}]},
      'translation':{'english_text':text,'mode':'prose-faithful','notes':['The source prints no speaker label for this spoken unit; no speaker or immutable dialogue ID is inferred.']}
    })

def dialog(units,scene_ordinal,source_scene_id,by_id,rid,english,notes=None):
    r=by_id[rid]
    units.append({
      'id':f'vandikkaran-magan-en-s{scene_ordinal:03d}-u{len(units)+1:03d}',
      'kind':'dialogue','status':'verified','target_language':'en',
      'scene_id':f'vandikkaran-magan-s{scene_ordinal:03d}','scene_ordinal':scene_ordinal,'source_scene_id':source_scene_id,
      'source':{
        'source_path':f'works/vandikkaran-magan/dialogues/records/scene-{scene_ordinal:03d}.json',
        'canonical_scene_path':f'works/vandikkaran-magan/scenes/scene-{scene_ordinal:03d}.md',
        'source_record_id':rid,'source_occurrence_id':None,'source_locator':None,
        'speaker_label':r['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':r['source_delimiter'],
        'page_provenance':r['page_provenance']},
      'translation':{'english_text':english,'mode':'prose-faithful','notes':notes or []}
    })

def write_scene(n,sid,units,pilot=False):
    obj={'work_id':'vandikkaran-magan','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}','scene_ordinal':n,'source_scene_id':sid,'scene_status':'verified','unit_count':len(units),'units':units}
    if pilot: obj['pilot_status']='verified'
    (R/f'scene-{n:03d}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return obj

# Scene 2 / source 2: intentionally zero immutable dialogue records.
rows2,by2=load_records(2); assert rows2==[]
u2=[]
stage(u2,2,'2',8,'(The zamindar arrives in the carriage, with coachman Sadaiyan driving it.)',description='Entire source-visible action of scene 2.')
sc2=write_scene(2,'2',u2)

# Scene 3 / source 3: intentionally zero immutable dialogue records.
rows3,by3=load_records(3); assert rows3==[]
u3=[]
stage(u3,3,'3',9,'Entrance of the estate temple.',kind='location-caption',description='Source location caption `ஜமீன் தேவாலயம் வாயில்`.')
stage(u3,3,'3',9,'(The zamindar’s carriage stops. Sadaiyan gets down first and respectfully helps the zamindar alight. When the zamindar reaches the entrance, the middle-aged guard there bows in greeting and opens the door. Sadaiyan follows behind the zamindar with great reverence, carrying on a silver tray a coconut, fruit and incense.)',description='Carriage arrival, guard greeting and Sadaiyan following with the offering tray.')
sc3=write_scene(3,'3',u3)

# Scene 4 / source 4: one labelled prayer plus one source-unlabelled spoken unit.
rows4,by4=load_records(4); assert [r['id'] for r in rows4]==['vandikkaran-magan-s004-d001']
u4=[]
stage(u4,4,'4',9,'Interior of the estate temple.',kind='location-caption',description='Source location caption `ஜமீன் தேவாலயம் உட்புறம்`.')
stage(u4,4,'4',9,'(The goddess idol is decorated. Behind the pedestal on which the idol stands is what looks like a partition wall. The zamindar enters, removes his footwear by the doorway, ties the silk cloth draped over him around his waist, breaks the coconut, places the fruit before the idol, lights the camphor and waves it before the idol...)',description='Opening worship action before the prayer.')
dialog(u4,4,'4',by4,'vandikkaran-magan-s004-d001','Devi! Parasakthi! Jagan Mata!.. Om Sakthi! Om Sakthi! Om! Om Sakthi, Om Sakthi, Om Sakthi, Om!...')
stage(u4,4,'4',9,'(He stands with his eyes closed in meditation, touches his cheeks, opens his eyes and looks at Sadaiyan....)',description='Meditation gesture immediately after the prayer.')
unlabelled(u4,4,'4',9,'Sadaiya!... Once I sit down for puja, I don’t know when I’ll get up... Go see to the other work and come back leisurely... go!...','Unlabelled speech addressed to Sadaiyan after the meditation gesture.')
stage(u4,4,'4',9,'(Sadaiyan bows to him and then to the goddess idol and leaves with great humility. The zamindar bolts the door. Then he turns the goddess idol. A secret door opens behind the idol, and through it the zamindar enters his private luxurious room.)',description='Sadaiyan exits; the zamindar opens the concealed passage and enters the private room.')
sc4=write_scene(4,'4',u4)

# Scene 5 / source 4-எ: 33 reconciled immutable dialogue records.
rows5,by5=load_records(5)
expected5=[*(f'vandikkaran-magan-s005-d{i:03d}' for i in range(1,12)),'vandikkaran-magan-s005-d032',*(f'vandikkaran-magan-s005-d{i:03d}' for i in range(12,17)),'vandikkaran-magan-s005-d033',*(f'vandikkaran-magan-s005-d{i:03d}' for i in range(17,32))]
assert [r['id'] for r in rows5]==expected5, [r['id'] for r in rows5]
tr={
'd001':'(in a coaxing voice toward the cot) Maragatham!... Asleep? Ah!... Even the beauty of you lying turned away is endlessly delightful!.. (going closer) Is it sleep? Sulking?... I’ll die without seeing your radiant face!... My sugarcane vine! Turn this way a little!....',
'd002':'Do you know how long I’ve been waiting?...',
'd003':'I too flew here yearning to embrace my lovely peahen... but meanwhile, as usual, a herd of donkeys with mercy petitions at the estate palace gate!..',
'd004':'Couldn’t you have chased them away and come quickly?... I’m burning here with the torment of separation—go away!',
'd005':'(drawing away) Maragatham! Don’t touch my hand! Pour a little “Dettol” on my hand!... (going to the washbasin) Some poet—and I wiped his child’s nose... damn it!..',
'd006':'Then whose grievances did you settle today?....',
'd007':'An old woman gets a monthly allowance of one hundred rupees for as long as she lives.',
'd008':'That much money!...',
'd009':'That old woman won’t live even one more month!..',
'd010':'Hmm... then... any new order...',
'd011':'I’ve issued a new order that from now on not even the smell of liquor should enter our estate!..',
'd032':'Oh!.. (As she says this, she turns the bookcase—the cabinet of liquor bottles swings into view. Maragatham pours some into a glass and gives it to the zamindar...)',
'd012':'Maragatham... you too, a little... (He places the glass at her lips. She drinks. As the zamindar drinks from the same glass) The taste of liquor and the taste of Maragatham’s lips—both together give me a double intoxication... Ah!..',
'd013':'You yourself are a double man, aren’t you!...',
'd014':'So that was a jab... are you making fun of me?..',
'd015':'I said you alone have the strength of two men... isn’t that right, my beloved?....',
'd016':'Maragatham! You’re speaking from your own experience, aren’t you?...',
'd033':'Go away!.. (Shyly she lies back on the bed. The zamindar follows and embraces her..)',
'd017':'Maragatham... where is it?.. (He puckers his lips, asking for a kiss.) Give me one...',
'd018':'Uh-uh... I’m shy!..',
'd019':'What’s this sudden new shyness! There’s no one here—just the two of us... give it!...',
'd020':'There’s a third person too!..',
'd021':'A third person? What are you saying?',
'd022':'Watching from inside my belly..?',
'd023':'(startled) What? Pregnant?...',
'd024':'Yes... four months!..',
'd025':'Four months? Maragatham!... What foolishness is this? Why haven’t you got rid of it until now? You’re only telling me now?... Are you planning to claim a quarter share of the estate property?',
'd026':'Who wants your property? I don’t need it!... I want a child!',
'd027':'What did you say? Only if I leave you alive can you have children and all that... I’ll send you where you belong right now!...',
'd028':'Mr. Jambuling Bhoopathi!... Until now Maragatham was a fawn that leapt and played in your lap!... From now on, a tiger cub that will drink your life!...',
'd029':'(frightened and shaken) Maragatham, forgive me!... Let us come to an understanding between ourselves..?',
'd030':'From now on, neither I nor the child I’m going to bear will live here! We will live in the estate palace!... That is where we are going to live—',
'd031':'All right, Maragatham!... In the estate palace, you’ll be the teacher who gives lessons to my daughter Uma!... We can live that way!..'
}
assert set(tr)=={rid.rsplit('-',1)[1] for rid in expected5}
u5=[]
stage(u5,5,'4-எ',10,'Private room of the temple.',kind='location-caption',description='Source location caption `தேவாலய அந்தரங்க அறை`.')
stage(u5,5,'4-எ',10,'(The zamindar enters... an opulent room... On the cot, Maragatham lies turned the other way, in decorative attire, with a strikingly alluring appearance...)',description='Opening view of Maragatham in the private room.')
dialog(u5,5,'4-எ',by5,expected5[0],tr['d001'])
stage(u5,5,'4-எ',10,'(Maragatham turns and sits up....)',description='Maragatham turns and rises.')
for rid in expected5[1:4]: dialog(u5,5,'4-எ',by5,rid,tr[rid.rsplit('-',1)[1]])
stage(u5,5,'4-எ',10,'(Comes forward to touch.)',description='Source stage direction omits an explicit subject; the English preserves that omission rather than assigning one.')
dialog(u5,5,'4-எ',by5,'vandikkaran-magan-s005-d005',tr['d005'])
stage(u5,5,'4-எ',10,'(Maragatham pours Dettol; the zamindar washes his hands. Maragatham gives him a towel and he wipes them...)',description='Hand-washing action after the Dettol request.')
# d006 through d011, then reconciled d032.
for rid in expected5[5:12]: dialog(u5,5,'4-எ',by5,rid,tr[rid.rsplit('-',1)[1]])
# d012 through d016, reconciled d033, then d017 through d027.
for rid in expected5[12:29]: dialog(u5,5,'4-எ',by5,rid,tr[rid.rsplit('-',1)[1]])
stage(u5,5,'4-எ',11,'(He grips Maragatham by the throat and throws her onto the bed. Maragatham, fallen on the bed, takes the revolver from beneath the pillow, first fires upward, and then aims at the zamindar.)',description='Strangling, warning shot and revolver aim before Maragatham’s threat.')
for rid in expected5[29:]: dialog(u5,5,'4-எ',by5,rid,tr[rid.rsplit('-',1)[1]])
sc5=write_scene(5,'4-எ',u5)

# Batch QA: source order, exact immutable links, unlabelled speech, no song promotion.
scenes=[sc2,sc3,sc4,sc5]
all_units=[u for s in scenes for u in s['units']]
linked=[u['source']['source_record_id'] for u in all_units if u['source']['source_record_id']]
expected_linked=['vandikkaran-magan-s004-d001',*expected5]
assert linked==expected_linked and len(linked)==34 and len(set(linked))==34
assert len(all_units)==48, len(all_units)
assert Counter(u['kind'] for u in all_units)==Counter({'dialogue':35,'stage-direction':13})
assert sum(u['source']['speaker_label_origin']=='source-unlabelled' for u in all_units)==1
assert all(u['source']['source_occurrence_id'] is None for u in all_units)
assert all('★' not in (u['translation'].get('english_text') or '') for u in all_units)

qa={
 'work_id':'vandikkaran-magan','phase':'english-translation-batch-002-005','status':'PASS',
 'scene_ordinals':[2,3,4,5],'source_scene_ids':['2','3','4','4-எ'],'verified_scenes':4,'verified_units':48,
 'unit_kind_counts':{'dialogue':35,'stage-direction':13},'immutable_dialogue_records_expected':34,'immutable_dialogue_records_linked':34,
 'source_unlabelled_spoken_units':1,'inferred_speaker_assignments':0,'performance_occurrences_expected':0,'performance_occurrence_links':0,'cross_page_units':0,
 'checks':{
  'scene2_and_scene3_zero_dialogue_status_preserved':True,
  'all_batch_immutable_dialogue_records_linked_exactly_once':True,
  'reconciled_append_only_ids_d032_and_d033_preserved_in_source_order':True,
  'source_unlabelled_scene4_speech_kept_unassigned_and_unlinked':True,
  'structural_star_translated_as_prose':False,
  'synthetic_scene_end_prose_added':False,
  'song_or_authorship_invented':False,
  'closed_tamil_scene_dialogue_character_song_records_modified_by_translation':False
 },
 'next_activity':'Translate and verify archive scene ordinals 6–10 as the next bounded English batch. Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; keep source-unlabelled speech unassigned; link only verified song/performance occurrences; do not modify closed Tamil, scene, dialogue, character or song records.'
}
(T/'batch-002-005-qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Recalculate translation checkpoint from scene 1 plus the new batch.
all_scene_files=sorted(R.glob('scene-*.json'))
objs=[json.loads(p.read_text(encoding='utf-8')) for p in all_scene_files]
assert [o['scene_ordinal'] for o in objs]==[1,2,3,4,5]
allv=[u for o in objs for u in o['units']]
counts=Counter(u['kind'] for u in allv)
linked_all=[u['source']['source_record_id'] for u in allv if u['source']['source_record_id']]
unlabelled_all=sum(u['source']['speaker_label_origin']=='source-unlabelled' for u in allv)
assert len(allv)==88 and counts==Counter({'dialogue':67,'stage-direction':21})
assert len(linked_all)==65 and len(set(linked_all))==65 and unlabelled_all==2
NEXT=qa['next_activity']
index={
 'work_id':'vandikkaran-magan','target_language':'en','status':'verified','total_scene_derivatives':72,'verified_scenes':5,
 'verified_scene_ordinals':[1,2,3,4,5],'verified_source_scene_ids':['1','2','3','4','4-எ'],'translation_units':88,
 'unit_kind_counts':{'dialogue':67,'stage-direction':21},'immutable_dialogue_records_linked':65,'source_unlabelled_spoken_units':2,
 'performance_occurrence_links':0,'cross_page_units':0,'schema':'schema.json','records_directory':'records/','pilot_qa':'pilot-qa.json','latest_batch_qa':'batch-002-005-qa.json','next_activity':NEXT
}
(T/'index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(T/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — English translation\n\n**Status:** **VERIFIED THROUGH ARCHIVE SCENE 5 / QA PASS**\n\n- scenes verified: **5 / 72** — source scene IDs `1`, `2`, `3`, `4`, `4-எ`;\n- translation units: **88** — **67 dialogue / 21 stage-direction**;\n- reconciled immutable dialogue records linked: **65/65 for translated scenes**;\n- source-unlabelled spoken units retained without speaker inference: **2**;\n- performance occurrence links in scenes 1–5: **0**;\n- upstream source-layer mutations caused by translation: **0**.\n\nScene 1 remains the verified pilot. `batch-002-005-qa.json` closes the first post-pilot batch and preserves the reconciled append-only dialogue IDs in source order. Structural `★` separators are not translated into synthetic prose.\n\n## Next\n\n{NEXT}\n''',encoding='utf-8')
print(json.dumps({'status':'PASS','verified_scenes':5,'translation_units':88,'dialogue_units':67,'stage_units':21,'immutable_links':65,'source_unlabelled':2},ensure_ascii=False))
