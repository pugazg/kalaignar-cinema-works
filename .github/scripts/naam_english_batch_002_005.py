from pathlib import Path
import json, re

W = Path('works/naam')
T = W / 'translations'
R = T / 'records'

NEXT = (
    "Translate and verify source-numbered scenes 6–10 as the next bounded English batch. "
    "Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance "
    "to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, page provenance, "
    "cross-page units and stage/narrative ownership; translate only source-visible performance text authorized by the reconciled "
    "seven-record song/performance layer, including `naam-perf-001` in scene 7 with its specific `பாரதியார்` attribution and "
    "`naam-perf-002` in scene 8 with unresolved item-level authorship; and do not alter closed Tamil or structured source layers."
)

def read_text(p):
    return Path(p).read_text(encoding='utf-8')

def write_text(p, s):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(s, encoding='utf-8')

def read_json(p):
    return json.loads(read_text(p))

def write_json(p, d):
    write_text(p, json.dumps(d, ensure_ascii=False, indent=2) + '\n')

D = {
2: {
'd001': "Is it fate, doctor, that we should leave a cruel man to enjoy the wealth piled up, while my son and I wander like blind people though we have eyes......?",
'd002': "Vedavalli......",
'd003': "Shh...... Kumaran doesn't know.",
'd004': "Hmm... Narayani... today's zamindar, Mallayappan, doesn't know you. That's fine... Kumaran too must take a job there for a few days.",
'd005': "A job?",
'd006': "Only then will our aim be fulfilled! You may even discover there the life that lies hidden! Kumaran too will learn the ways and customs of the zamindari!",
'd007': "Kumaran doesn't like rich households! It was because he spoke of reform in that town that his life came under threat—and we came to this town.",
'd008': "For now he can talk about every reform and every principle! Later, once the zamindari comes to him, he'll forget them all in that life of pleasure! Narayani... remember what I told you!",
'd009': "Kumara... Kumara...!",
'd010': "What is it, Amma! Finished talking all your secrets?",
'd011': "Kumara! They say we're going to get work at the zamindar's house!",
'd012': "Work! At the zamindar's house?",
'd013': "You must accept what I tell you!",
},
3: {
'd001': "Come... Sanjeevi! Hmm... what's the special matter......",
'd002': "I came thinking I'd see the zamindar before leaving... would I come for nothing?",
'd003': "Who are these people?",
'd004': "They're people I know! I was wondering whether there might be some work for them in your house......",
'd005': "Hmm, I do need a maid! Hey, Annamalai! Take them to Madam!",
'd006': "Hmm...... and then......",
'd007': "(The zamindar's wife) Meenu... Meenu...",
'd008': "(Mallayappan's younger sister) What is it, sister-in-law?",
'd009': "A new maid has come to our house.",
'd010': "Any doubt? From now on this is my home!",
'd011': "Meenu...... tell her the work.",
'd012': "Come! You've barely arrived—what work do you have already?",
'd013': "Yes... what are you to the zamindar?",
'd014': "His younger sister!",
'd015': "Do you have to see this with your own eyes?",
'd016': "Hey, Narayani! What are you doing there, fondling your son? Come quickly!",
'd017': "Hey... where is that lazy fellow? Is he still coming back from the station?",
'd018': "Useless eater! Why are you late? What's that pot?",
'd019': "Amma brought water... I was helping her.",
'd020': "Tch...! As long as you work here, a servant is only a servant! If you start talking mother-and-son affection... dirt will fall into your rice. Careful! Hmm, take the boxes and stack them... stack them, I said.",
'd021': "Shameless dog... why are you so careless? Couldn't your body bear carrying even one pot, poor thing? Puthu il... thundu poachchi......",
'd022': "I didn't break the pot... it got rolled over......",
'd023': "Tch... after doing wrong, are you putting the blame on him?",
'd024': "Amma......",
'd025': "Nothing's happened to me... go and do your work!",
'd026': "Hey... what show are you putting on there... come here... unload the box... unload it quickly...",
'd027': "(Seeing the glassware broken, in fierce anger) What's this? What have you broken?",
'd028': "Amma......",
'd029': "Amma. (Arrogantly) You came here for slave labour! How many times do I have to tell you that this mother-son affection is not allowed?",
'd030': "Hey. Go and bring the doctor... go quickly......",
},
4: {
'd001': "(Knocking at the door) Doctor... doctor...",
'd002': "(The doctor's daughter—opening the door) Come in! Ah... what atrocity is this...",
'd003': "Father isn't here...",
'd004': "Oh no... blood is sprouting all over.",
'd005': "Turn us into a tiger—with red stripes like this. Where is father...?",
'd006': "I'll call him now. Hey, Father... come quickly...”",
'd007': "Isn't the doctor here?",
'd008': "No.",
'd009': "I need some body oil.",
'd010': "Not now.",
'd011': "I've brought money.",
'd012': "Come later! I'm busy right now.",
'd013': "Why, Prema... couldn't you have given it to him and sent him off?",
'd014': "That derappai fellow... he'll come later. That's not important compared with this...",
'd015': "Why... Prema... who is it—Kumara?",
'd016': "Look at this cruelty, Appa—that chandalan has beaten him with a whip.",
'd017': "What is this, Kumara?",
'd018': "These are the kisses my master gave me.",
'd019': "Why, Prema...... that Thangaiyan with joint pain asked for body oil...... why didn't you give it to him and send him off?",
'd020': "There isn't any, Appa!",
'd021': "Keep quiet! Hey, Mathirai! He's leaving angry. Give this to him and collect the money.",
'd022': "(The doctor's servant) What's important now, sir? That he shouldn't get angry? Or the money?",
'd023': "Tch...... take it, give it to him and come back.",
'd024': "All right........ attend to him, Appa!",
'd025': "Kumara... good thing... you came at once... otherwise it would go bad.",
'd026': "I...... didn't come for myself! The zamindar sprained his hand while beating me... I came to take you there for that.",
'd027': "Would God leave without paying wages?",
'd028': "He will...... he will!......",
'd029': "Prema... here... apply this medicine! I'll go and see that komberi-mookkan fellow and come back.",
},
5: {
'd001': "What, Sanjeevi...... come... come. You don't visit our house very often......",
'd002': "Why shouldn't I come... only, a house should not be in a condition where doctors have to visit often.",
'd003': "Must you come to our house only to see illness? You may come to eat a feast too, Sanjeevi!",
'd004': "We may... and what we eat......",
'd005': "Ah......",
'd006': "What we eat is your food anyway.",
'd007': "Sanjeevi! You are a very grateful man. But... in that one matter, I simply cannot trust you.",
'd008': "In what...? In medicine?",
'd009': "Ha... hmm... in that, you're an extraordinary hero! Just hand that life over to me. My worry will end.",
'd010': "Don't worry! Only if that life exists can I give it, right?",
'd011': "Then who has it?",
'd012': "It... is very secret! Don't go reading signs into it! There is no need for agitation! Trust Sanjeevi......!",
'd013': "Hey... where is Kumaran? Has he gone to graze the cattle?",
}}

NOTES = {
(3,'d018'): ["`தண்டச்சோறு` is retained as a harsh class-inflected insult (`useless eater`) rather than softened."],
(3,'d021'): ["The verified source fragment `புது இல்...துண்டு போச்சி` is irregular/unclear; it is carried by conservative transliteration (`Puthu il... thundu poachchi`) rather than silently emended."],
(4,'d004'): ["The source image `இரத்தம் இரத்தமா தளிர்ச்சிருக்கே` is kept with its unusual 'sprouting' imagery rather than flattened."],
(4,'d014'): ["The verified source form `டேரப்பை` is unclear; `derappai` is retained by transliteration instead of guessing a repair."],
(4,'d016'): ["The caste-loaded source insult `சண்டாளன்` is retained as `chandalan` rather than euphemized or normalized."],
(4,'d029'): ["The source insult `கொம்பேறி மூக்கன்` is retained as `komberi-mookkan` rather than replaced with an invented English equivalent."],
(5,'d004'): ["The unusual verified source form `வாலாம்` is translated conservatively from immediate context without altering the Tamil."],
(5,'d012'): ["The unusual verified form `சங்கேதப் படாதீர்கள்` is rendered conservatively as `Don't go reading signs into it`; it is not silently normalized to a different Tamil word."],
}

EXTRAS = {
2: {
'loc': ('narrative',7,"Location: Sanjeevi the physician's hut.",'scene-location','Source location line.'),
'enter': ('stage-direction',8,"(Kumaran enters.)",'scene-stage-direction','Kumaran enters after Narayani calls him.'),
'depart': ('stage-direction',8,"(The three set out for Zamindar Mallayappar.)",'scene-stage-direction','Closing departure direction.'),
},
3: {
'loc': ('narrative',8,"Location: Mallayappar's mansion.",'scene-location','Source location line.'),
'servant': ('stage-direction',9,"(The servant is taken along.)",'scene-stage-direction','Source action before Mallayappar resumes speaking.'),
'change': ('stage-direction',9,"(The scene changes.)",'scene-stage-direction','Explicit scene-change direction within source scene 3.'),
'look': ('stage-direction',9,"[Looking at Narayani]",'scene-stage-direction','Bracketed look-direction before unlabelled speech.'),
'unlabelled': ('dialogue',9,"Narayani! Keep the house in order. As though it were your own home.",'source-unlabelled-speech','Source speech has no printed speaker label and remains unassigned.'),
'gnanam-leaves': ('stage-direction',9,"(After Gnanam leaves.)",'scene-stage-direction','Transition after Gnanam exits.'),
'days': ('stage-direction',9,"(Many days pass.)",'scene-stage-direction','Explicit passage-of-time direction.'),
'montage': ('stage-direction',9,"(Kumaran's mother comes carrying a water pot. Kumaran, kurukkodi—has been chopping firewood, sweating. Exhausted, he sits down—idli arrives—he delights. Next an orange arrives—he is comforted. Milk comes for the labourer Kumaran—he is enraptured. In this way, through things carrying the flavour of love, Meenu conveyed her feelings to Kumaran. Finally, the two together lifted that beautiful flower-pot, their faces blossoming into smiles.)",'scene-stage-direction','Long courtship/labour montage on PDF 9.'),
'help': ('stage-direction',10,"(As Kumaran pulls the box-cart along, he sees his mother carrying a water pot and runs to help.)",'scene-stage-direction','Kumaran sees Narayani and runs to help.'),
'cart': ('stage-direction',10,"(Kumaran pulls the cart in—with the water pot.)",'scene-stage-direction','Kumaran returns with cart and water pot.'),
'parallel': ('stage-direction',10,"{ Mallayappan torments Kumaran—on one side / Gnanam scolds Narayani—on the other. }",'scene-stage-direction','Parallel-action brace block.'),
'hit-fall': ('stage-direction',10,"(Saying this, Gnanam strikes Narayani. The next moment Narayani is sent rolling down from the upper floor.)",'scene-stage-direction','Gnanam strikes Narayani; Narayani falls/rolls down.'),
'run': ('stage-direction',11,"(Seeing this, Kumaran drops the box and runs over.)",'scene-stage-direction','Kumaran drops the box and runs.'),
'unload': ('stage-direction',11,"(Kumaran unloads the box.)",'scene-stage-direction','Kumaran unloads the box.'),
'whip': ('stage-direction',11,"(Mallayappar beats Kumaran with a whip. Narayani writhes; Mallayappar's hand is sprained.)",'scene-stage-direction','Whipping and sprained-hand action.'),
'go-doctor': ('stage-direction',11,"(Kumaran goes to the physician.)",'scene-stage-direction','Kumaran leaves to fetch the physician.'),
},
4: {
'loc': ('narrative',11,"Location: The physician's house.",'scene-location','Source location line.'),
'call': ('stage-direction',12,"(From the hut, Prema calls her father.)",'scene-stage-direction','Prema calls her father from the hut.'),
'thangaiyan-enters': ('stage-direction',12,"[Thangaiyan enters.]",'scene-stage-direction','Bracketed entrance direction.'),
'thangaiyan-leaves': ('stage-direction',12,"(After Thangaiyan leaves.)",'scene-stage-direction','Transition after Thangaiyan exits.'),
'mathirai-leaves': ('stage-direction',13,"(Mathirai leaves.)",'scene-stage-direction','Mathirai exits to deliver the medicine.'),
},
5: {
'loc': ('narrative',13,"Location: Mallayappar's mansion.",'scene-location','Source location line.'),
}}

EXTRA_NOTES = {
(3,'servant'): ["Tamil leaves the acting subject implicit; English preserves that ambiguity with a passive construction."],
(3,'unlabelled'): ["The printed source supplies no speaker label or delimiter for this utterance. It is translated as speech but deliberately remains unassigned and unlinked to the immutable labelled-dialogue index."],
(3,'montage'): ["The verified source form `குறுக்கொடிய` is not silently repaired; it is retained as `kurukkodi` within the English stage-direction unit."],
}

ORDER = {
2: ['x:loc'] + [f'd{i:03d}' for i in range(1,10)] + ['x:enter'] + [f'd{i:03d}' for i in range(10,14)] + ['x:depart'],
3: ['x:loc','d001','d002','d003','d004','d005','x:servant','d006','x:change','d007','d008','d009','x:look','x:unlabelled','d010','d011','x:gnanam-leaves','d012','d013','d014','x:days','x:montage','x:help','d015','d016','d017','x:cart','d018','d019','d020','x:parallel','d021','d022','d023','x:hit-fall','x:run','d024','d025','d026','x:unload','d027','d028','d029','x:whip','d030','x:go-doctor'],
4: ['x:loc','d001','d002','d003','d004','d005','d006','x:call','x:thangaiyan-enters','d007','d008','d009','d010','d011','d012','d013','d014','x:thangaiyan-leaves','d015','d016','d017','d018','d019','d020','d021','d022','d023','x:mathirai-leaves','d024','d025','d026','d027','d028','d029'],
5: ['x:loc'] + [f'd{i:03d}' for i in range(1,14)],
}

EXPECTED = {2:(16,13), 3:(46,30), 4:(34,29), 5:(14,13)}


def make_dialogue_unit(scene, idx, rec, english):
    key = rec['id'].split('-')[-1]
    return {
        'id': f'naam-en-s{scene:03d}-u{idx:03d}',
        'kind': 'dialogue',
        'status': 'verified',
        'target_language': 'en',
        'scene_id': f'naam-s{scene:03d}',
        'scene_ordinal': scene,
        'source_scene_number': scene,
        'source': {
            'source_path': f'works/naam/dialogues/records/scene-{scene:03d}.json',
            'canonical_scene_path': f'works/naam/scenes/scene-{scene:03d}.md',
            'source_record_id': rec['id'],
            'source_occurrence_id': None,
            'source_locator': None,
            'speaker_label': rec['speaker_label'],
            'speaker_label_origin': 'source-explicit',
            'source_delimiter': rec['source_delimiter'],
            'page_provenance': rec['page_provenance'],
        },
        'translation': {
            'english_text': english,
            'mode': 'prose-faithful',
            'notes': NOTES.get((scene,key), []),
        }
    }


def make_extra_unit(scene, idx, key, extra_ordinal):
    kind, page, english, locator_kind, desc = EXTRAS[scene][key]
    is_unlabelled = locator_kind == 'source-unlabelled-speech'
    return {
        'id': f'naam-en-s{scene:03d}-u{idx:03d}',
        'kind': kind,
        'status': 'verified',
        'target_language': 'en',
        'scene_id': f'naam-s{scene:03d}',
        'scene_ordinal': scene,
        'source_scene_number': scene,
        'source': {
            'source_path': f'works/naam/scenes/scene-{scene:03d}.md',
            'canonical_scene_path': f'works/naam/scenes/scene-{scene:03d}.md',
            'source_record_id': None,
            'source_occurrence_id': None,
            'source_locator': {'kind': locator_kind, 'ordinal': extra_ordinal, 'description': desc},
            'speaker_label': None,
            'speaker_label_origin': None,
            'source_delimiter': None,
            'page_provenance': [{'pdf_page': page, 'printed_page': page}],
        },
        'translation': {
            'english_text': english,
            'mode': 'prose-faithful',
            'notes': EXTRA_NOTES.get((scene,key), []),
        }
    }

records = {}
qa_scenes = []
for scene in range(2,6):
    dialogue_records = read_json(W / f'dialogues/records/scene-{scene:03d}.json')
    by_key = {r['id'].split('-')[-1]: r for r in dialogue_records}
    units = []
    extra_ordinal = 0
    for token in ORDER[scene]:
        idx = len(units) + 1
        if token.startswith('d'):
            units.append(make_dialogue_unit(scene, idx, by_key[token], D[scene][token]))
        else:
            extra_ordinal += 1
            units.append(make_extra_unit(scene, idx, token[2:], extra_ordinal))
    expected_units, expected_dialogues = EXPECTED[scene]
    assert len(units) == expected_units, (scene, len(units), expected_units)
    linked = [u['source']['source_record_id'] for u in units if u['source']['source_record_id']]
    expected_ids = [r['id'] for r in dialogue_records]
    assert len(dialogue_records) == expected_dialogues
    assert linked == expected_ids, (scene, 'dialogue source order/link mismatch')
    for u in units:
        rid = u['source']['source_record_id']
        if rid:
            src = next(r for r in dialogue_records if r['id']==rid)
            assert u['source']['speaker_label'] == src['speaker_label']
            assert u['source']['source_delimiter'] == src['source_delimiter']
    record = {
        'work_id':'naam', 'target_language':'en', 'scene_id':f'naam-s{scene:03d}',
        'scene_ordinal':scene, 'source_scene_number':scene, 'scene_status':'verified',
        'unit_count':len(units), 'units':units,
    }
    records[scene] = record
    write_json(R / f'scene-{scene:03d}.json', record)
    qa_scenes.append({
        'scene_id':f'naam-s{scene:03d}', 'source_scene_number':scene,
        'translation_units':len(units), 'immutable_dialogue_records_expected':len(dialogue_records),
        'immutable_dialogue_records_linked':len(linked), 'missing_dialogue_links':0, 'duplicate_dialogue_links':0,
        'source_unlabelled_speech_units':sum(1 for u in units if u['kind']=='dialogue' and u['source']['source_record_id'] is None),
        'performance_occurrences_expected':[], 'performance_occurrences_linked':[],
    })

batch_units = sum(r['unit_count'] for r in records.values())
batch_dialogues = sum(x['immutable_dialogue_records_linked'] for x in qa_scenes)
unlabelled = sum(x['source_unlabelled_speech_units'] for x in qa_scenes)
assert batch_units == 110
assert batch_dialogues == 85
assert unlabelled == 1
assert all(u['status']=='verified' for r in records.values() for u in r['units'])
assert not any(u['source']['source_occurrence_id'] for r in records.values() for u in r['units'])
assert not any(len(u['source']['page_provenance']) > 1 for r in records.values() for u in r['units'])

qa = {
    'work_id':'naam', 'phase':'english-translation-batch-002-005-qa', 'status':'PASS',
    'source_scenes':[2,3,4,5], 'translation_units':110,
    'immutable_dialogue_records_expected':85, 'immutable_dialogue_records_linked':85,
    'dialogue_coverage':'85/85 exactly once', 'missing_dialogue_links':0, 'duplicate_dialogue_links':0,
    'exact_tamil_speaker_labels_preserved':True, 'source_delimiters_preserved_as_metadata':True,
    'source_unlabelled_speech_units':1, 'inferred_unlabelled_speakers':0,
    'performance_occurrences_expected':[], 'performance_occurrences_linked':[], 'performance_coverage':'0/0',
    'cross_page_translation_units':[], 'scene_results':qa_scenes,
    'authorship_status_changed_by_translation':False, 'external_or_unprinted_lyrics_imported':False,
    'canonical_tamil_modified':0, 'scene_text_modified':0, 'dialogue_records_modified':0,
    'character_entity_mappings_modified':0, 'song_source_records_modified_by_translation':0,
    'next_gate':'scenes 6-10 translation batch ready'
}
write_json(T / 'batch-002-005-qa.json', qa)

review = f'''# நாம் — English batch review / scenes 2–5\n\n**Batch:** source scenes `காட்சி 2`–`காட்சி 5`  \n**Status:** **VERIFIED**  \n**Units:** **110**  \n**Immutable dialogue links:** **85/85 exactly once**\n\n## Review result\n\nThe first post-pilot English batch translates and verifies source-numbered scenes 2–5 in exact source order. It preserves all **85/85** explicitly labelled immutable dialogue records exactly once, keeps exact Tamil speaker labels and `:-` / `:` delimiters as metadata, and represents **25** additional source-owned units without changing the closed Tamil or structured layers.\n\nScene 3 contains one genuinely source-unlabelled utterance after `[நாராயணியைப் பார்த்து]`: `நாராயணி! வீட்டை ஒழுங்காக பார்த்துக்கொள். உன் வீடு மாதிரி.` It is translated as speech but deliberately remains **unassigned** with no manufactured speaker label and no immutable-dialogue ID.\n\nNo reconciled song/performance record belongs to scenes 2–5, so performance linkage for this batch is correctly **0/0**. No soundtrack, subtitle, web lyric or remembered material is introduced.\n\n## Scene counts\n\n| Scene | Units | Immutable dialogue links | Unlabelled speech | Performance records |\n|---|---:|---:|---:|---:|\n| 2 | 16 | 13/13 | 0 | 0 |\n| 3 | 46 | 30/30 | 1 | 0 |\n| 4 | 34 | 29/29 | 0 | 0 |\n| 5 | 14 | 13/13 | 0 | 0 |\n| **Batch** | **110** | **85/85** | **1** | **0** |\n\n## Source-fidelity decisions\n\n- Scene 3 keeps `தண்டச்சோறு` as a harsh insult rather than softening the class register.\n- Scene 3 does not repair `குறுக்கொடிய`; the verified form is carried as `kurukkodi` in the montage note.\n- Scene 3's unclear `புது இல்...துண்டு போச்சி` is transliterated conservatively rather than guessed into a fluent sentence.\n- Scene 4 retains the unusual `இரத்தம் ... தளிர்ச்சிருக்கே` image with the source's 'sprouting' force.\n- Scene 4 leaves `டேரப்பை`, `சண்டாளன்` and `கொம்பேறி மூக்கன்` source-visible through transliteration/notes rather than silently normalizing them.\n- Scene 5 translates `வாலாம்` and `சங்கேதப் படாதீர்கள்` conservatively from immediate context while leaving the verified Tamil untouched.\n- Mallayappar's servant/master rhetoric and the literal `dirt will fall into your rice` image remain direct rather than euphemized.\n\n## Integrity checks\n\n- expected / linked immutable dialogue records: **85 / 85**;\n- missing / duplicate immutable links: **0 / 0**;\n- source-unlabelled speech assigned to a speaker: **0**;\n- exact Tamil speaker-label preservation: **PASS**;\n- source-delimiter preservation: **PASS**;\n- cross-page logical units in this batch: **0**;\n- expected / linked performance occurrences: **0 / 0**;\n- authorship upgrades: **0**;\n- canonical Tamil / scene / dialogue / character / song-source modifications: **0 / 0 / 0 / 0 / 0**.\n\n## Cumulative English checkpoint\n\nAfter the verified pilot plus this batch: **5/45 source scenes**, **131 verified English units**, **99 immutable dialogue links**, **1 translated performance record (`naam-perf-007`)**, and **23/23 song role/line mappings**.\n\n## Next batch\n\n{NEXT}\n'''
write_text(T / 'BATCH_002_005_REVIEW.md', review)

# Update translation index.
p = T / 'index.json'; idx = read_json(p)
idx['status'] = 'in-progress-verified-through-scene-005'
idx['verified_scenes'] = 5
idx['verified_scene_ids'] = [f'naam-s{i:03d}' for i in range(1,6)]
idx['translation_units_verified'] = 131
idx['immutable_dialogue_links_verified'] = 99
idx['stage_or_narrative_units_verified'] = 29
idx['source_unlabelled_speech_units_verified'] = 1
idx['retained_performance_records_total'] = 7
idx['retained_performance_records_translated'] = 1
idx['translated_performance_record_ids'] = ['naam-perf-007']
idx['song_line_cue_mappings_verified'] = 23
idx['batch_002_005_review'] = 'BATCH_002_005_REVIEW.md'
idx['batch_002_005_qa'] = 'batch-002-005-qa.json'
idx['next_activity'] = NEXT
write_json(p, idx)

# Translation README.
p = T / 'README.md'; s = read_text(p)
s = re.sub(r'\*\*Status:\*\* \*\*.*?\*\*', '**Status:** **in progress — source scenes 1–5 / 45 verified; 131 units**', s, count=1)
if '## Batch — source scenes 2–5' not in s:
    s += f'''\n\n## Batch — source scenes 2–5\n\nScenes 2–5 are **VERIFIED** as **110 units** with **85/85 immutable dialogue links**, **1 deliberately unassigned source-unlabelled speech unit**, **0 performance occurrences**, and **0 cross-page units**. Detailed decisions are in `BATCH_002_005_REVIEW.md`; machine QA is `batch-002-005-qa.json`.\n\nCumulative English state is now **5/45 verified scenes / 131 units / 99 immutable dialogue links / 1 of 7 performance records translated / 23 song mappings**.\n\n## Next batch\n\n{NEXT}\n'''
else:
    s = re.sub(r'## Next batch\n\n.*', '## Next batch\n\n'+NEXT+'\n', s, flags=re.S)
write_text(p, s)

# metadata.yaml.
p = W / 'metadata.yaml'; s = read_text(p)
s = re.sub(r'(?m)^  english_translation: .+$', '  english_translation: in-progress-verified-through-scene-005', s, count=1)
s = re.sub(r'(?m)^  english_translation_verified_scenes: \d+$', '  english_translation_verified_scenes: 5', s, count=1)
s = re.sub(r'(?m)^  english_translation_unit_count: \d+$', '  english_translation_unit_count: 131', s, count=1)
s = re.sub(r'(?m)^  english_dialogue_links_verified: \d+$', '  english_dialogue_links_verified: 99', s, count=1)
s = re.sub(r'(?m)^  english_performance_records_translated: \d+$', '  english_performance_records_translated: 1', s, count=1)
s = re.sub(r'(?m)^  english_song_line_cue_mappings_verified: \d+$', '  english_song_line_cue_mappings_verified: 23', s, count=1)
status_i = s.find('\nstatus:\n')
if status_i >= 0:
    pre, tail = s[:status_i], s[status_i:]
    tail = re.sub(r'(?m)^  english_translation: .+$', '  english_translation: in-progress-verified-5-of-45', tail, count=1)
    s = pre + tail
s = re.sub(r'(?m)^next_action:.*$', 'next_action: ' + json.dumps(NEXT, ensure_ascii=False), s, count=1)
write_text(p, s)

# Work README active checkpoint and English section.
p = W / 'README.md'; s = read_text(p)
s = re.sub(r'- English translation: \*\*.*?\*\*; reader / Reading Room: \*\*not-started\*\*\.', '- English translation: **5/45 VERIFIED — 131 units / 99 immutable dialogue links / 1 of 7 performance records / 23 song mappings**; reader / Reading Room: **not-started**.', s, count=1)
s = re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes 2–5[^\n]*', '**Next:** ' + NEXT, s)
if '## English scenes 2–5 checkpoint' not in s:
    marker = '## Source-visible publication / credit evidence\n'
    block = f'''## English scenes 2–5 checkpoint\n\n- cumulative verified source scenes: **5/45**;\n- cumulative verified English units: **131**;\n- cumulative immutable dialogue links: **99**;\n- batch scenes 2–5: **110 units / 85/85 immutable dialogue links**;\n- source-unlabelled speech: **1 unit, deliberately unassigned**;\n- performance records in batch: **0**; cumulative translated performance records: **1/7**;\n- song mappings remain **23/23** from scene 1;\n- upstream source-layer modifications caused by this batch: **0**.\n\n**Next:** {NEXT}\n\n'''
    s = s.replace(marker, block + marker, 1)
write_text(p, s)

# Active next prompt.
write_text(W / 'NEXT_CHAT_PROMPT.md', f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**. Scenes are **45/45 COMPLETE-VERIFIED**. Dialogue indexing is **590 immutable records / QA PASS**. Character/entity indexing is **28 entities / 45/45 labels / 590/590 records / QA PASS**. Song/performance gating is **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**, with `ஆயிரம் தெய்வங்கள்` → `பாரதியார்` as the only item-level source attribution and six unresolved item-level authorships.\n\nEnglish translation is **VERIFIED THROUGH SOURCE SCENE 5: 5/45 scenes, 131 units, 99 immutable dialogue links, 1/7 performance records translated, 23/23 song role/line mappings**. Scenes 2–5 add **110 units / 85/85 immutable dialogue links / one source-unlabelled speech unit deliberately left unassigned / 0 performance records / 0 cross-page units**. No source or structured layer was rewritten.\n\nEnglish index: `works/naam/translations/index.json`; records: `works/naam/translations/records/scene-001.json`–`scene-005.json`; pilot review: `works/naam/translations/PILOT_REVIEW.md`; batch review: `works/naam/translations/BATCH_002_005_REVIEW.md`; batch QA: `works/naam/translations/batch-002-005-qa.json`.\n\nDo not alter closed Tamil or structured layers except for later direct source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Project handover append current marker.
p = W / 'PROJECT_HANDOVER.md'; s = read_text(p)
tag = '<!-- Naam English scenes 2-5 current -->'
block = f'''\n\n{tag}\n## English scenes 2–5 verified checkpoint\n\n- English verified scenes: **5/45**;\n- verified English units: **131**;\n- immutable dialogue links: **99**;\n- scenes 2–5 batch: **110 units / 85/85 labelled-dialogue links**;\n- source-unlabelled speech in batch: **1**, deliberately unassigned;\n- translated performance records: **1/7** cumulative;\n- song mappings: **23/23** cumulative;\n- upstream source-layer modifications: **0**.\n\n**Current exact next activity:** {NEXT}\n'''
if tag in s:
    s = s[:s.index(tag)] + block.lstrip('\n')
else:
    s += block
write_text(p, s)

# data/works.json mirror.
p = Path('data/works.json'); data = read_json(p); n = next(x for x in data if x.get('id')=='naam'); sd = n.setdefault('structured_derivatives', {})
sd.update({
    'song_performance_gate':'complete-verified-source-only-reconciled', 'song_performance_records':7,
    'source_attributed_performance_records':1, 'unresolved_item_level_authorship_records':6,
    'english_translation':'in-progress-verified-through-scene-005', 'english_translation_verified_scenes':5,
    'english_translation_units':131, 'english_dialogue_links_verified':99,
    'english_source_unlabelled_speech_units':1, 'english_performance_records_translated':1,
    'english_song_line_cue_mappings_verified':23, 'english_translation_index_path':'works/naam/translations/index.json'
})
n['next_action'] = NEXT
write_json(p, data)

# Root README Naam section.
p = Path('README.md'); s = read_text(p)
start = s.index('## நாம் status')
end = s.index('\n## ராஜா ராணி status', start)
section = s[start:end]
section = re.sub(r'- English translation: \*\*.*?\*\*\.', '- English translation: **5/45 VERIFIED — 131 units / 99 immutable dialogue links / 1 of 7 performance records / 23 song mappings**.', section, count=1)
section = re.sub(r'\*\*Next:\*\*.*', '**Next:** ' + NEXT, section, count=1)
s = s[:start] + section + s[end:]
write_text(p, s)

# Master handover: normalize current high-level Naam line and active checkpoint, then append current marker.
p = Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'); s = read_text(p)
s = re.sub(r'(?m)^- \*\*Naam / நாம்\*\* — .*$', '- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scenes **45/45**; dialogues **590**; characters **28 / 45/45 / 590/590**; song/performance gate **7/7 reconciled**; English **5/45 verified / 131 units / 99 immutable dialogue links / 1 of 7 performance records translated**.', s, count=1)
s = re.sub(r'(?m)^\*\*Exact next activity:\*\* Begin Phase 9.*$', '**Exact next activity:** ' + NEXT, s, count=1)
tag = '<!-- Naam English scenes 2-5 current -->'
current = f'''\n\n{tag}\n**Naam / நாம் current English checkpoint:** **5/45 scenes VERIFIED / 131 units / 99 immutable dialogue links / 1 of 7 performance records translated / 23 song mappings**. Scenes 2–5 are **110 units / 85/85 labelled-dialogue links**, with one source-unlabelled utterance deliberately unassigned and 0 performance occurrences. No closed source layer changed. **Next:** {NEXT}\n'''
if tag in s:
    s = s[:s.index(tag)] + current.lstrip('\n')
else:
    s += current
write_text(p, s)

# Status consistency audit: update matrix row and next production phase, append current marker.
p = Path('docs/STATUS_CONSISTENCY_AUDIT.md'); s = read_text(p)
s = re.sub(r'(?m)^\| Naam / நாம் \|.*$', '| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogue records; 28 character/entities; song/performance 7/7 reconciled** | **5/45 verified / 131 units / 99 immutable dialogue links / 1 of 7 performances translated** | not-started |', s, count=1)
s = re.sub(r'(?m)^\*\*Next production phase:\*\*.*$', '**Next production phase:** ' + NEXT, s, count=1)
tag = '<!-- Naam English scenes 2-5 current -->'
current = f'''\n\n{tag}\n**Naam current consistency checkpoint:** source layers remain closed; song/performance gate **7/7 reconciled**; English **5/45 scenes / 131 units / 99 immutable dialogue links / 1 of 7 performances / 23 song mappings**. Scenes 2–5 QA is **PASS** with **85/85** labelled-dialogue links and one unassigned source-unlabelled speech unit. **Next:** {NEXT}\n'''
if tag in s:
    s = s[:s.index(tag)] + current.lstrip('\n')
else:
    s += current
write_text(p, s)

print(json.dumps({
    'status':'verified-through-scene-005', 'verified_scenes':'5/45', 'batch_units':110,
    'cumulative_units':131, 'batch_dialogue_links':'85/85', 'cumulative_dialogue_links':99,
    'unlabelled_speech_units':1, 'performance_batch':'0/0', 'performance_cumulative':'1/7',
    'song_mappings':'23/23', 'next':NEXT
}, ensure_ascii=False, indent=2))
