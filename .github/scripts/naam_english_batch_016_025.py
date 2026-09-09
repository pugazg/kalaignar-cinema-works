from pathlib import Path
import json, re

W=Path('works/naam'); T=W/'translations'; R=T/'records'
NEXT=("Translate and verify source-numbered scenes 26–35 as the next 10-scene English batch. "
      "Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; "
      "keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; "
      "translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-004` in scene 31 with unresolved item-level authorship; "
      "do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; only a final remainder may contain fewer scenes.")

def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p,s): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(s,encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p,d): wt(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

D={
16:[
"Bravo! The chance we had been waiting for so long has arrived. Boxer Paramasivam! Kumara! If you defeat this man, you will be the king of boxing!",
"Where? When...?",
"Everything is in your own village! Zamindar Mallayappar... he is the one who has arranged it.",
"Ah... Mallayappar?",
"Why...? Shall I write back that you agree?",
"All right!"
],
17:[
"What did you think the boxing match was for? To entertain the villagers? Is that our work? That dog must be killed!",
"Is killing such an easy matter? I'll defeat him.",
"What I want is not to crown you with a victory garland as the greatest of warriors—I want him killed.",
"If that's so...",
"Fight by foul means!",
"But fighting that way in boxing is an offence under the law...",
"The law! It will surrender to me! I have the courage to save a man standing on the gallows! Sin, merit, honesty, justice, mercy, law, society—none of these work on me. Act accordingly, Paramasivam! You must kill him! I want my heart cooled by seeing it.",
"How am I to thank you for your love and your cheering?",
"Brother! Only today have we seen happiness. Hunger, starvation, blows and kicks—that is all there is here!",
"What can I do? If only that will comes into my hands, I will make this entire zamindari yours. The zari cap will not rule you! The whip-rider will not drive you! A flick of that jungle king's eye will no longer be an order!",
"For the poor there is a special comfort in imagining a world of happiness.",
"Jeevanandar! This is not the heaven devotees imagine! It can be achieved if we strive! It can happen if we will it! To attain it, you don't need a forehead full of sacred ash! Clarity in the heart—and a commitment to honesty—are enough.",
"Let us await—that good day.",
"The good day will not come toward us! We must walk until our legs ache toward it."
],
18:[
"Come on! Don't be shy!",
"What is it, Mathirai!",
"Without telling you... how could I get hold of you... I didn't even know your address.",
"Tell me what it is, Mathirai.",
"He has become my father-in-law (Jeevanandar), and I've become his son-in-law! My wife is Thailam!",
"Ah... Mathirai—Thailam! That's very good!",
"Even if the horoscopes don't match, by medicinal method it's a very good match.",
"Then...... I give this to you as a gift."
],
19:[
"I've found the money. The will... yes, in Mallayappar's mansion... Meenu was there... oh... conspirator... why should I even look at her? The will... otherwise, life......"
],
20:[
"Gnanam! This silk mattress I lie on! That silk sari you wear! The owner of all this is still alive and roaming. Only when he is gone will I have peace.",
"He'll be gone!",
"How will he be gone? If only you had calmly given him that poison, he would have been gone that very day.",
"What could I do? I mixed the poison into the milk Meenu had kept for him. How was I to know he would give it to his mother!"
],
21:[
"Meenu...",
"Kumaran...... (Don't cry, Meenu)...",
"Forgive me, Meenu! Yes... how do you come alone in this darkness? Should you be coming like this?",
"I shouldn't, of course! But... until now, my aunt's grave has been the only comfort for my withered heart.",
"Is your heart still withered?",
"The beauty within shows on the face...",
"Come... let me see."
],
22:[
"Kumaran isn't stubborn about anything... it's all because of you.",
"Prema...... Kumaran will marry only you—don't worry! Prema! I'll go and make the arrangements too. Stay safe at home! Hey, Mathirai! We are the ones giving medicine to that Kannan's mother, aren't we...",
"Yes, sir.",
"What happened!",
"She's recovered, sir! They say they've sent people out to other towns as well!",
"Oh...... go harness the cart!",
"What if you deceive me after the marriage......?",
"Nectar of the gods that comes without asking! A zamindar's mansion that comes without effort! Doesn't my daughter need these? Look here......",
"You won't lose the will! He won't lose his promise! In the end I alone must lose my love.",
"Love... is it greater than this will? More valuable than this mansion? Prema! Watch—the storm is going to fall at your feet. Careful! Don't even move your lips to anyone!"
],
23:[
"The will... the will... my life!",
"Quietly...",
"Prema... you brought it?",
"Who else would bring it, Zamindar?",
"I'm not a zamindar! A servant of the people—a worker for the people! I won't forget this help, sister!",
"Sister......",
"Amma! I've found the will! The wealth you wandered searching for has been found! The buried treasure has come into my hands. I'm going right now to that wicked man.",
"Kumaran......"
],
24:[
"Interim Zamindar, greetings! Why are you stunned? The man who should have come bowing and calling you master—has somehow come like this... are you wondering what nonsense I'm babbling?",
"Hey, Kumara! (Grinding his teeth)",
"Grinding your teeth—and glaring—will be no use from now on.",
"Don't speak without respect!",
"Respect! From now on you'll have to buy it for a price! Leave the mansion before respect itself is lost!",
"Those who oppose me are left with nothing but bones!",
"Even those bones will not remain for arrogant men like you who fight Yama! The bones you left behind... those bones themselves have become spears and come to oppose you!",
"Kumara! Don't talk like a madman!",
"The zamindar himself has caught janni, afflicted by the frosty wind of pomp—the sun of intrigue—and the rain of arrogance. Yes, I am mad! Because I don't have a heart that clears!",
"What are you babbling?",
"Did I run here so eagerly just to babble!",
"What are you saying?",
"I'm not saying it! This will says that the purana of your divine games is over! I've come to tear to shreds the curtain you hung before the townspeople. What do you say? Hmm... leave respectfully!",
"Kumara...! Don't stumble against a sleeping tiger!",
"Kumaran has set his sights on the mule living inside that tiger skin!",
"Kumara! Don't speak!",
"A corpse doesn't speak!",
"I'm going to kill you.",
"I've heard those same words—in this same mansion—so many times. With those same words, so many bungalows have been levelled to the ground.",
"I am Malayappan!",
"No doubt!",
"Keep your display of valour for the boxing ring.",
"No!",
"This is my house!",
"That's exactly where you're wrong!",
"What's the difference? You man without fate! Wandering spendthrift! If I show loyalty to this fellow as an old servant—giving him the zamindari, property, house and home—the fool doesn't even know how to behave with respect?",
"Malayappa! I'll say it plainly! I'm going to settle my vengeance on you.",
"Kumara......",
"Don't be afraid... not now! I'll wait.",
"Kumara! You must know by heart the list of those who have crumpled at the movement of my little finger!",
"It's because I know it by heart that I haven't forgotten, fool—listen! Parasites like you have been blown away by the furious breath of workers! Here... is the cry of rights that will bring an end to the durbar of your jungle king, hunted by the people of the land! The sledgehammer that will strike you down! What do you say? Why do you stare? Yield that came without sweating! Pleasure that came without hardship! Ecstasy that came without labour! How can you leave all that behind? It will be a little hard! Are you trembling because your 'right' is being snatched away?",
"Even if I die, I'll order that even my corpse be buried here. If you have a right, don't come here roaring and babbling!",
"Didn't your feet walk on the hearts of the poor, making them a cotton mattress? Wasn't the groan of the poor man's heart music to you? Aren't you the one who squeezed the blood of the helpless like grape juice and drank it! We'll meet before the law!",
"Go! Go away! Don't stand here!",
"I'm going. This is your last voice of authority."
],
25:[
"Mad girl! In one moment you've ruined the plan I had laid!",
"Forgive me, Appa!",
"Did you harm me that you need my forgiveness? You've thrown earth on your own head.",
"He said there would be no marriage without the will, Appa!",
"And now, the moment you gave him the will, has he fixed a date for the auspicious wedding hour?",
"He hasn't fixed a date!",
"Then... does that mean the marriage is settled? Go away somehow...",
"Who's that? Go and see, Prema..."
]}

NOTES={
(18,3):["The verified colloquial form `சிக்கணமா` is irregular; English keeps the immediate sense without altering the Tamil."],
(18,5):["The source's medicine-name wordplay `மாத்திரை / தைலம்` is retained through the names Mathirai / Thailam rather than flattened."],
(19,1):["The closing `உயில்... இல்லாவிட்டால் உயிர்` is deliberately kept elliptical rather than expanded into an object not printed in the source."],
(22,5):["The verified line about sending people to other towns is translated literally; its exact referent is not expanded beyond the source."],
(24,9):["`ஜன்னி` is retained as `janni` rather than silently forced into a modern medical diagnosis."],
(24,15):["`கோவேரிக் கழுதை` is rendered as `mule` within the source's animal-image insult; the verified Tamil remains untouched."],
(24,31):["The worker/rights rhetoric and repeated unearned-wealth imagery are kept direct rather than neutralized into summary."]
}

X={
17:{
'fight':('stage-direction',32,"(A boxing match takes place between Kumaran and Paramasivam. Paramasivam is defeated. The villagers welcome Kumaran.)",'scene-stage-direction','Boxing contest and village welcome.',None,[]),
'clothes':('stage-direction',33,"(Kumaran brings clothes.)",'scene-stage-direction','Kumaran brings clothes for distribution.',None,[]),
'unlabel':('dialogue',33,"Jeevanandar! Distribute these among everyone! This is the gift your progressive hearts gave me.",'source-unlabelled-speech','Printed speech after the clothes direction has no source speaker label.',None,["The immediate stage direction points to Kumaran, but the source prints no dialogue label or delimiter; speaker metadata remains unassigned."])
},
18:{
'exit1':('stage-direction',34,"(Kumaran steps out.)",'scene-stage-direction','Kumaran steps out.',None,[]),
'unlabel':('dialogue',34,"Everyone, stay here! I'm going to my mother's house and will return! We'll meet later.",'source-unlabelled-speech','Printed speech between two Kumaran exit directions has no source speaker label.',None,["The surrounding action suggests Kumaran, but the source supplies no explicit dialogue label; no speaker is manufactured."]),
'exit2':('stage-direction',34,"(Kumaran leaves.)",'scene-stage-direction','Kumaran leaves.',None,[]),
'crowd':('stage-direction',34,"(A cry of ‘Long live Kumaran’ rises from the crowd.)",'scene-stage-direction','Crowd acclamation.',None,[])
},
19:{
'loc':('narrative',34,"Location: graveyard.",'scene-location','Source location line.',None,[]),
'q1':('dialogue',34,"Kumara! Somehow find that will.",'source-unlabelled-speech','Quoted remembered speech followed by a source parenthetical identifying Narayani.',None,["The source identifies this as Narayani's plea in a following parenthetical, but does not print an explicit dialogue label or delimiter; speaker metadata remains unassigned."]),
'n1':('narrative',34,"(This is Narayani's plea.)",'scene-narrative','Source parenthetical identifying the preceding remembered speech.',None,[]),
'q2':('dialogue',34,"Money is needed to conduct the case! Then search for the will.",'source-unlabelled-speech','Quoted remembered speech followed by a source parenthetical identifying the physician voice.',None,["The source identifies this as the physician's voice in a following parenthetical, but does not print an explicit dialogue label or delimiter; speaker metadata remains unassigned."]),
'n2':('narrative',34,"(This is the physician's voice.)",'scene-narrative','Source parenthetical identifying the preceding remembered speech.',None,[]),
'run':('stage-direction',34,"(Kumaran runs toward Mallayappar's mansion to steal the will.)",'scene-stage-direction','Kumaran runs toward the mansion in search of the will.',None,[])
},
20:{
'loc':('narrative',34,"Location: Mallayappar's mansion.",'scene-location','Source location line.',None,[]),
'night':('stage-direction',34,"(Night.)",'scene-stage-direction','Night-time setting.',None,[]),
'leave':('stage-direction',35,"(Hearing this, Kumaran realizes that Meenu is innocent and leaves.)",'scene-stage-direction','Kumaran overhears the poisoning explanation and leaves.',None,[])
},
21:{
'loc':('narrative',35,"Location: graveyard.",'scene-location','Source location line.',None,[]),
'cue':('performance-cue',36,"(Meenu is singing sorrowfully. Kumaran comes there.)",'performance-cue','Source-visible cue establishing Meenu as the singer and Kumaran arriving.','naam-perf-003',["This cue is source-visible and does not upgrade the unresolved item-level authorship."]),
'smile':('stage-direction',36,"(Meenu smiles.)",'scene-stage-direction','Meenu smiles after Kumaran asks to see her face.',None,[])
},
22:{
'after':('stage-direction',37,"(After Mathirai leaves.)",'scene-stage-direction','Mathirai exits.',None,[]),
'unlabel1':('dialogue',37,"Prema! Sanjeevi is no fool to hand over the will first! Marriage—then the will.",'source-unlabelled-speech','Printed speech after Mathirai leaves has no source speaker label.',None,["Context points strongly to Sanjeevi, but the source prints no explicit speaker label or delimiter; speaker metadata remains unassigned."]),
'will':('stage-direction',37,"(Holding the will in his hand.)",'scene-stage-direction','The will is taken out and held in hand.',None,[]),
'unlabel2':('dialogue',37,"The will! A boat that will let you roam along the stream of pleasure!",'source-unlabelled-speech','Printed speech while holding the will has no source speaker label.',None,["Context points strongly to Sanjeevi, but the source prints no explicit speaker label or delimiter; speaker metadata remains unassigned."]),
'exit':('stage-direction',37,"(The physician puts the will away at home and leaves town. Prema takes the will to Kumaran.)",'scene-stage-direction','Sanjeevi leaves; Prema carries the will to Kumaran.',None,[])
},
23:{
'loc':('narrative',38,"Location: Kumaran's hut.",'scene-location','Source location line.',None,[]),
'night':('stage-direction',38,"(Night.)",'scene-stage-direction','Night-time setting.',None,[]),
'throw':('stage-direction',38,"(Prema throws the will onto Kumaran. The sleeping Kumaran springs up quickly.)",'scene-stage-direction','Prema throws the will; Kumaran wakes.',None,[]),
'grave':('stage-direction',38,"(Near the grave.)",'scene-stage-direction','Movement to the grave.',None,[]),
'go':('stage-direction',38,"(Kumaran sets out to bring Mallayappan down.)",'scene-stage-direction','Kumaran sets out to confront and humble Mallayappan.',None,[])
},
24:{
'loc':('narrative',38,"Location: Mallayappan's mansion.",'scene-location','Source location line.',None,[]),
'leave':('stage-direction',41,"(Kumaran leaves.)",'scene-stage-direction','Kumaran leaves after the confrontation.',None,[]),
'plot':('stage-direction',41,"(Malayappan plans to set fire to Kumaran's hut.)",'scene-stage-direction','Malayappan plans arson.',None,[]),
'burn':('stage-direction',41,"(The hut catches fire and burns.)",'scene-stage-direction',"Kumaran's hut burns.",None,[])
},
25:{
'knock':('stage-direction',42,"[There is a knock at the door.]",'scene-stage-direction','Door knock.',None,[]),
'open':('stage-direction',42,"(She opens the door.)",'scene-stage-direction','Prema opens the door.',None,[]),
'fall':('stage-direction',42,"[Kumaran enters with his body burned and collapses.]",'scene-stage-direction','Burned Kumaran enters and falls.',None,[])
}}

PERF003_LINES=[
(35,"மணமில்லா மலர் நானம்மா!","I am a flower without fragrance, Amma!"),
(35,"மாதர் உலகில் வாழ்வே அறியா","Knowing nothing of life in the world of women,"),
(35,"மணமில்லா மலர் நானம்மா!","I am a flower without fragrance, Amma!"),
(35,"ஒடிந்து வீண நாதமே இனியேது","The veena is broken—what music remains now?"),
(35,"இடியிதோ வீழ்ந்தே பூங்கா அழிந்ததே","Here the thunderbolt has fallen—the flower garden is destroyed."),
(35,"மணமில்லா மலர் நானம்மா!","I am a flower without fragrance, Amma!"),
(35,"வாழ்விலே விஷமே வீசியே மறைந்ததால்","Because poison was cast into my life and vanished,"),
(35,"மணமில்லா மலர் நானம்மா!","I am a flower without fragrance, Amma!"),
(35,"வாடிடும் கொடியானேன்","I have become a withering creeper"),
(35,"சூறாவளிக் காற்றிலே","in the wind of a cyclone."),
(35,"மகரந்த இதழ்மீது மாசு தோய்ந்து மூடிய","Stain has soaked and covered the nectar-bearing petal,"),
(35,"மணமில்லா மலர் நானம்மா!","I am a flower without fragrance, Amma!"),
(36,"இன்பச் சுடர் காணேனே","I see no flame of joy,"),
(36,"இருள் வீட்டில் தனியானேன்","I am alone in a house of darkness,"),
(36,"துன்பப் புயல் அலை மோதி","Waves of a storm of sorrow batter me,"),
(36,"சோக வாழ்வுச் சோலையில்","in the grove of a life of grief,"),
(36,"மணமில்லா மலர் நானம்மா!","I am a flower without fragrance, Amma!")]

ORDER={
16:[f'd{i:03d}' for i in range(1,7)],
17:[f'd{i:03d}' for i in range(1,8)]+['x:fight']+[f'd{i:03d}' for i in range(8,15)]+['x:clothes','x:unlabel'],
18:[f'd{i:03d}' for i in range(1,9)]+['x:exit1','x:unlabel','x:exit2','x:crowd'],
19:['x:loc','x:q1','x:n1','x:q2','x:n2','d001','x:run'],
20:['x:loc','x:night']+[f'd{i:03d}' for i in range(1,5)]+['x:leave'],
21:['x:loc','p:003','x:cue']+[f'd{i:03d}' for i in range(1,8)]+['x:smile'],
22:[f'd{i:03d}' for i in range(1,7)]+['x:after','x:unlabel1','d007','d008','x:will','x:unlabel2','d009','d010','x:exit'],
23:['x:loc','x:night','x:throw']+[f'd{i:03d}' for i in range(1,7)]+['x:grave','d007','d008','x:go'],
24:['x:loc']+[f'd{i:03d}' for i in range(1,36)]+['x:leave','x:plot','x:burn'],
25:[f'd{i:03d}' for i in range(1,8)]+['x:knock','d008','x:open','x:fall']}
EXPECTED_COUNTS={16:6,17:14,18:8,19:1,20:4,21:7,22:10,23:8,24:35,25:8}
EXPECTED_UNLABELLED=['naam-en-s017-u017','naam-en-s018-u010','naam-en-s019-u002','naam-en-s019-u004','naam-en-s022-u008','naam-en-s022-u012']
EXPECTED_CROSS=['naam-en-s017-u011','naam-en-s020-u003','naam-en-s021-u002']

def source_scene_path(n): return f'works/naam/scenes/scene-{n:03d}.md'
def source_dialogue_path(n): return f'works/naam/dialogues/records/scene-{n:03d}.json'

def d_unit(n,di,uid,src):
    r=src[di-1]
    assert r['id']==f'naam-s{n:03d}-d{di:03d}'
    return {'id':uid,'kind':'dialogue','status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':source_dialogue_path(n),'canonical_scene_path':source_scene_path(n),'source_record_id':r['id'],'source_occurrence_id':None,'source_locator':None,'speaker_label':r['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':r['source_delimiter'],'page_provenance':r['page_provenance']},
      'translation':{'english_text':D[n][di-1],'mode':'prose-faithful','notes':list(NOTES.get((n,di),[]))}}

def x_unit(n,key,uid):
    kind,page,eng,lkind,desc,occ,notes=X[n][key]
    return {'id':uid,'kind':kind,'status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':source_scene_path(n),'canonical_scene_path':source_scene_path(n),'source_record_id':None,'source_occurrence_id':occ,'source_locator':{'kind':lkind,'ordinal':1,'description':desc},'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,'page_provenance':[{'pdf_page':page,'printed_page':page}]},
      'translation':{'english_text':eng,'mode':'prose-faithful','notes':notes}}

def perf003_unit(uid):
    lm=[{'ordinal':i+1,'kind':'lyric-line','pdf_page':page,'tamil':ta,'english':en} for i,(page,ta,en) in enumerate(PERF003_LINES)]
    return {'id':uid,'kind':'song','status':'verified','target_language':'en','scene_id':'naam-s021','scene_ordinal':21,'source_scene_number':21,
      'source':{'source_path':'works/naam/songs/records/naam-perf-003.md','canonical_scene_path':source_scene_path(21),'source_record_id':None,'source_occurrence_id':'naam-perf-003','source_locator':{'kind':'retained-performance-record','ordinal':3,'description':'Full source-visible Meenu lyrical block across PDF 35–36.'},'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,'page_provenance':[{'pdf_page':35,'printed_page':35},{'pdf_page':36,'printed_page':36}]},
      'translation':{'english_lines':[en for _,_,en in PERF003_LINES],'line_map':lm,'mode':'semantic-poetic-source-faithful','notes':['Translated only from the source-visible Tamil retained in `naam-perf-003`.','Source role is Meenu, established by the retained performance record and the following printed cue; no synthetic dialogue speaker label is created.','Item-level authorship remains unresolved; the broad PDF-4 credit is not promoted.']}}

def build_scene(n):
    src=rj(W/f'dialogues/records/scene-{n:03d}.json')
    assert len(src)==EXPECTED_COUNTS[n]==len(D[n])
    units=[]
    for token in ORDER[n]:
        uid=f'naam-en-s{n:03d}-u{len(units)+1:03d}'
        if token.startswith('d'): units.append(d_unit(n,int(token[1:]),uid,src))
        elif token.startswith('x:'): units.append(x_unit(n,token[2:],uid))
        elif token=='p:003': units.append(perf003_unit(uid))
        else: raise AssertionError(token)
    rec={'work_id':'naam','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,'scene_status':'verified','unit_count':len(units),'units':units}
    wj(R/f'scene-{n:03d}.json',rec)
    return rec

idx=rj(T/'index.json')
assert idx['status']=='in-progress-verified-through-scene-015'
assert idx['verified_scenes']==15 and idx['translation_units_verified']==363
assert idx['immutable_dialogue_links_verified']==279
assert idx['source_unlabelled_speech_units_verified']==4
assert idx['retained_performance_records_translated']==3 and idx['song_line_cue_mappings_verified']==57

records=[build_scene(n) for n in range(16,26)]
batch_units=sum(x['unit_count'] for x in records)
batch_links=sum(1 for x in records for u in x['units'] if u['source']['source_record_id'])
unlabelled=[u['id'] for x in records for u in x['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None]
cross=[u['id'] for x in records for u in x['units'] if len(u['source']['page_provenance'])>1]
occ=[]; line_maps=0
for x in records:
    for u in x['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in occ: occ.append(o)
        line_maps += len(u['translation'].get('line_map',[]))
assert batch_units==138,batch_units
assert batch_links==101,batch_links
assert unlabelled==EXPECTED_UNLABELLED,unlabelled
assert cross==EXPECTED_CROSS,cross
assert occ==['naam-perf-003'],occ
assert line_maps==17,line_maps

scene_results=[]
for x in records:
    n=x['source_scene_number']
    linked=sum(1 for u in x['units'] if u['source']['source_record_id'])
    unl=sum(1 for u in x['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None)
    po=[]
    for u in x['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in po: po.append(o)
    scene_results.append({'scene_id':x['scene_id'],'source_scene_number':n,'translation_units':x['unit_count'],'immutable_dialogue_records_expected':EXPECTED_COUNTS[n],'immutable_dialogue_records_linked':linked,'missing_dialogue_links':0,'duplicate_dialogue_links':0,'source_unlabelled_speech_units':unl,'performance_occurrences_linked':po})

qa={'work_id':'naam','phase':'english-translation-batch-016-025-qa','status':'PASS','source_scenes':list(range(16,26)),'translation_units':batch_units,
    'immutable_dialogue_records_expected':101,'immutable_dialogue_records_linked':101,'dialogue_coverage':'101/101 exactly once','missing_dialogue_links':0,'duplicate_dialogue_links':0,
    'exact_tamil_speaker_labels_preserved':True,'source_delimiters_preserved_as_metadata':True,'source_unlabelled_speech_units':len(unlabelled),'source_unlabelled_unit_ids':unlabelled,'inferred_unlabelled_speakers':0,
    'performance_occurrences_expected':['naam-perf-003'],'performance_occurrences_linked':['naam-perf-003'],'performance_coverage':'1/1','performance_line_cue_mappings':17,
    'naam_perf_003_authorship':'unresolved-item-level','cross_page_translation_units':cross,'scene_results':scene_results,
    'authorship_status_changed_by_translation':False,'external_or_unprinted_lyrics_imported':False,'canonical_tamil_modified':0,'scene_text_modified':0,'dialogue_records_modified':0,'character_entity_mappings_modified':0,'song_source_records_modified_by_translation':0,
    'next_gate':'scenes 26-35 translation batch ready; 10 scenes per iteration'}
wj(T/'batch-016-025-qa.json',qa)

idx['status']='in-progress-verified-through-scene-025'
idx['verified_scenes']=25; idx['verified_scene_ids']=[f'naam-s{i:03d}' for i in range(1,26)]
idx['translation_units_verified']=363+batch_units
idx['immutable_dialogue_links_verified']=380
idx['stage_or_narrative_units_verified']=idx.get('stage_or_narrative_units_verified',76)+sum(1 for x in records for u in x['units'] if u['kind'] in ('narrative','stage-direction'))
idx['performance_cue_units_verified']=idx.get('performance_cue_units_verified',2)+sum(1 for x in records for u in x['units'] if u['kind']=='performance-cue')
idx['song_units_verified']=idx.get('song_units_verified',2)+sum(1 for x in records for u in x['units'] if u['kind']=='song')
idx['retained_performance_records_translated']=4
idx['translated_performance_record_ids']=['naam-perf-007','naam-perf-001','naam-perf-002','naam-perf-003']
idx['song_line_cue_mappings_verified']=74
idx['source_unlabelled_speech_units_verified']=10
idx['cross_page_translation_units']=list(dict.fromkeys(idx.get('cross_page_translation_units',[])+cross))
idx['batch_016_025_review']='BATCH_016_025_REVIEW.md'; idx['batch_016_025_qa']='batch-016-025-qa.json'; idx['iteration_scene_batch_size']=10; idx['next_activity']=NEXT
wj(T/'index.json',idx)

rows='\n'.join(f"| {r['source_scene_number']} | {r['translation_units']} | {r['immutable_dialogue_records_linked']}/{r['immutable_dialogue_records_expected']} | {r['source_unlabelled_speech_units']} | {', '.join(r['performance_occurrences_linked']) or '0'} |" for r in scene_results)
review=f'''# நாம் — English batch review / scenes 16–25

**Batch:** source scenes `காட்சி 16`–`காட்சி 25`  
**Status:** **VERIFIED**  
**Units:** **{batch_units}**  
**Immutable dialogue links:** **101/101 exactly once**

## Review result

This 10-scene iteration translates and verifies source-numbered scenes 16–25 in exact source order. All **101/101** immutable explicitly labelled dialogue records are linked exactly once, retaining exact Tamil speaker labels, source delimiters and PDF provenance as metadata. Six source speeches printed without explicit dialogue labels remain deliberately unassigned; no speaker identity is manufactured.

Scene 21 translates the retained `naam-perf-003` lyrical block across PDF 35–36 with **17/17** Tamil→English lyric-line mappings. The source-visible cue identifying Meenu as singing is separately retained and linked to the same performance occurrence. Item-level authorship remains **unresolved**; the broad PDF-4 credit is not promoted.

## Scene counts

| Scene | Units | Immutable dialogue links | Unlabelled speech | Performance links |
|---|---:|---:|---:|---|
{rows}
| **Batch** | **{batch_units}** | **101/101** | **{len(unlabelled)}** | **1 unique record** |

## Fidelity decisions

- Scene 17 keeps the law/gallows threat, class language and the cross-page PDF 32→33 promise to transfer the zamindari without softening its political rhetoric.
- Scene 18 preserves the `மாத்திரை / தைலம்` medicine-name wordplay and keeps the irregular `சிக்கணமா` line conservative rather than silently repairing Tamil.
- Scene 19 retains the two remembered quoted voices as source-unlabelled translation units even though following parentheticals identify Narayani and the physician; explicit speaker-label metadata remains null.
- Scene 20 keeps Mallayappan's mattress/silk-property argument as one logical cross-page PDF 34→35 dialogue unit.
- Scene 21 preserves the flower, veena, poison, cyclone and dark-house imagery line by line; `naam-perf-003` receives no inferred lyricist.
- Scene 22 keeps both source-unlabelled will/marriage speeches unassigned even though context points to Sanjeevi.
- Scene 24 preserves the extended anti-zamindari confrontation, `janni`, animal-image insults, worker-rights rhetoric and the final arson sequence without neutralizing or modernizing the source.
- Scene 25 preserves the source's marriage/will bargain and the abrupt arrival of burned Kumaran without adding explanatory action.

## Integrity checks

- expected / linked immutable dialogue records: **101 / 101**;
- missing / duplicate immutable links: **0 / 0**;
- source-unlabelled speeches: **{len(unlabelled)}**, inferred speakers: **0**;
- performance records expected / linked: **1 / 1 — `naam-perf-003`**;
- new performance line mappings: **17**;
- new cross-page units: **{len(cross)} — {', '.join(cross)}**;
- authorship upgrades: **0**;
- external/unprinted lyric imports: **0**;
- canonical Tamil / scene / dialogue / character / song-source modifications: **0 / 0 / 0 / 0 / 0**.

## Cumulative English checkpoint

After scenes 1–25: **25/45 source scenes**, **{idx['translation_units_verified']} verified English units**, **380 immutable dialogue links**, **10 source-unlabelled speech units retained without inferred labels**, **4/7 performance records translated**, and **74 Tamil→English performance line/cue mappings**.

## Iteration rule

Continue with **10 source scenes per iteration**. Only the final remainder may contain fewer than ten scenes.

## Next batch

{NEXT}
'''
wt(T/'BATCH_016_025_REVIEW.md',review)

p=T/'README.md'; s=rt(p)
s=re.sub(r'\*\*Status:\*\* \*\*.*?\*\*',f"**Status:** **verified through source scene 25 / 45; {idx['translation_units_verified']} units**",s,count=1)
s=re.sub(r'## Next batch\n\n.*?(?=\n##|\Z)',f"## Next batch\n\n{NEXT}\n",s,flags=re.S)
if '## Verified batch — scenes 16–25' not in s:
    s += f'''\n## Verified batch — scenes 16–25\n\n- source scenes: **10 / scenes 16–25**;\n- units: **{batch_units}**;\n- immutable dialogue links: **101/101**;\n- source-unlabelled speech: **{len(unlabelled)} / inferred speakers 0**;\n- performance occurrences: **1/1 — `naam-perf-003`**;\n- new lyric-line mappings: **17**;\n- upstream rewrites: **0**.\n\nProduction cadence remains **10 source scenes per iteration**.\n'''
wt(p,s)

p=W/'metadata.yaml'; s=rt(p)
s=re.sub(r'(?m)^  english_translation: .+$','  english_translation: in-progress-verified-25-of-45',s,count=1)
s=re.sub(r'(?m)^  english_translation_verified_scenes: \d+$','  english_translation_verified_scenes: 25',s,count=1)
s=re.sub(r'(?m)^  english_translation_unit_count: \d+$',f"  english_translation_unit_count: {idx['translation_units_verified']}",s,count=1)
s=re.sub(r'(?m)^  english_dialogue_links_verified: \d+$','  english_dialogue_links_verified: 380',s,count=1)
s=re.sub(r'(?m)^  english_performance_records_translated: \d+$','  english_performance_records_translated: 4',s,count=1)
s=re.sub(r'(?m)^  english_song_line_cue_mappings_verified: \d+$','  english_song_line_cue_mappings_verified: 74',s,count=1)
status_i=s.find('\nstatus:\n')
if status_i>=0:
    pre=s[:status_i]; tail=s[status_i:]; tail=re.sub(r'(?m)^  english_translation: .+$','  english_translation: in-progress-verified-25-of-45',tail,count=1); s=pre+tail
s=re.sub(r'(?m)^next_action:.*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False),s,count=1)
wt(p,s)

p=W/'README.md'; s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*; reader / Reading Room: \*\*not-started\*\*\.',f"- English translation: **25/45 VERIFIED — {idx['translation_units_verified']} units / 380 dialogue links / 4 of 7 performance records / 74 performance mappings**; reader / Reading Room: **not-started**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes [^\n]*','**Next:** '+NEXT,s)
if '## English scenes 16–25 checkpoint' not in s:
    s += f'''\n\n## English scenes 16–25 checkpoint\n\n- English scenes verified: **25/45 cumulative**;\n- cumulative units: **{idx['translation_units_verified']}**;\n- immutable dialogue links: **380**;\n- source-unlabelled speech retained without inferred labels: **10**;\n- translated performance records: **4/7 — `naam-perf-007`, `naam-perf-001`, `naam-perf-002`, `naam-perf-003`**;\n- performance line/cue mappings: **74**;\n- closed upstream-layer changes: **0**.\n\n**Iteration rule:** 10 source scenes per iteration; final remainder may be smaller.\n\n**Next:** {NEXT}\n'''
wt(p,s)

wt(W/'NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 immutable records / QA PASS**; character/entity layer **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**.\n\nEnglish translation is **VERIFIED THROUGH SOURCE SCENE 25**: **25/45 scenes**, **{idx['translation_units_verified']} units**, **380 immutable dialogue links**, **10 source-unlabelled speech units with 0 inferred speaker labels**, **4/7 performance records translated**, and **74 performance line/cue mappings**. `naam-perf-001` retains the specific source attribution **பாரதியார்**; `naam-perf-002` and `naam-perf-003` remain unresolved at item level.\n\nUser directive: **process 10 source scenes in each English-translation iteration**. Only the final remainder may contain fewer than 10.\n\nCurrent English files include `translations/BATCH_016_025_REVIEW.md`, `translations/batch-016-025-qa.json`, and `translations/records/scene-001.json` through `scene-025.json`.\n\nDo not alter closed Tamil or structured source layers except for later direct source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

p=W/'PROJECT_HANDOVER.md'; s=rt(p); tag='## English scenes 16–25 closure checkpoint'
if tag not in s:
    s += f'''\n\n{tag}\n\n- cumulative verified English scenes: **25/45**;\n- cumulative units: **{idx['translation_units_verified']}**;\n- immutable dialogue links: **380**;\n- source-unlabelled speech retained: **10 / inferred labels 0**;\n- performance records translated: **4/7**;\n- performance line/cue mappings: **74**;\n- upstream source-layer changes caused by English: **0**.\n\n**User iteration directive:** 10 source scenes per English iteration; final remainder may be smaller.\n\n## Current exact next activity\n\n> **{NEXT}**\n'''
wt(p,s)

p=Path('data/works.json'); data=rj(p); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({'english_translation':'in-progress-verified-through-scene-025','english_translation_verified_scenes':25,'english_translation_units':idx['translation_units_verified'],'english_dialogue_links_verified':380,
           'english_source_unlabelled_speech_units':10,'english_performance_records_translated':4,'english_song_line_cue_mappings_verified':74,'english_iteration_scene_batch_size':10,'english_translation_index_path':'works/naam/translations/index.json'})
n['next_action']=NEXT; wj(p,data)

p=Path('README.md'); s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*\.',f"- English translation: **25/45 VERIFIED — {idx['translation_units_verified']} units / 380 dialogue links / 4 of 7 performance records / 74 mappings**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes [^\n]*','**Next:** '+NEXT,s)
mark='<!-- Naam English scenes 16-25 current -->'
if mark not in s: s += f'''\n\n{mark}\n**Naam current English checkpoint:** **25/45 source scenes VERIFIED**, **{idx['translation_units_verified']} units**, **380 immutable dialogue links**, **4/7 performance records translated**, **74 performance mappings**, **0 upstream rewrites**. Iteration size remains **10 source scenes**. **Next:** {NEXT}\n'''
wt(p,s)

for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s=rt(p); mark='<!-- Naam English scenes 16-25 current -->'
    if mark not in s: s += f'''\n\n{mark}\n**Naam English scenes 16-25 current:** English **25/45 verified / {idx['translation_units_verified']} units / 380 dialogue links / 4 of 7 performances / 74 mappings**; source-unlabelled speech remains unassigned; upstream rewrites **0**. User cadence: **10 source scenes per iteration**. **Next:** {NEXT}\n'''
    wt(p,s)

print(json.dumps({'status':'PASS','scenes':'16-25','batch_units':batch_units,'batch_dialogue_links':101,'cumulative_scenes':25,'cumulative_units':idx['translation_units_verified'],'cumulative_dialogue_links':380,'batch_unlabelled':len(unlabelled),'performance_records':['naam-perf-003'],'line_maps_added':17,'next':'26-35'},ensure_ascii=False,indent=2))
