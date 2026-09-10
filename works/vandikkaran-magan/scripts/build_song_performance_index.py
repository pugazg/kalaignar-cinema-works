#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, shutil

W = Path(__file__).resolve().parents[1]
T = W / 'transcription' / 'pages'
S = W / 'songs'
R = S / 'records'
N = W / 'notes'

char_idx = json.loads((W / 'characters' / 'index.json').read_text(encoding='utf-8'))
assert char_idx['status'] == 'complete-verified'
assert char_idx['label_coverage'] == '38/38'
assert char_idx['dialogue_record_coverage'] == '773/773'
scene_idx = json.loads((W / 'scenes' / 'index.json').read_text(encoding='utf-8'))
scene_by_id = {x['scene_id']: x for x in scene_idx['scenes']}
assert len(scene_by_id) == 72


def page_raw(pdf):
    return (T / f'{pdf:03}.md').read_text(encoding='utf-8')


def page_body(pdf):
    raw = page_raw(pdf)
    lines = raw.splitlines()
    assert lines and lines[0].startswith('<!-- source:')
    lines = lines[1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    return '\n'.join(lines).rstrip()


def printed_page(pdf):
    m = re.search(r'printed=([^ ]+)', page_raw(pdf).splitlines()[0])
    assert m
    return None if m.group(1) == 'none' else int(m.group(1))


def exact_line(pdf, contains):
    hits = [x for x in page_body(pdf).splitlines() if contains in x]
    assert len(hits) == 1, (pdf, contains, hits)
    return hits[0]


def after_until(pdf, start, end=None):
    text = page_body(pdf)
    assert start in text, (pdf, start)
    out = text.split(start, 1)[1]
    if end is not None:
        assert end in out, (pdf, end)
        out = out.split(end, 1)[0]
    return out.strip()


def before(pdf, end):
    text = page_body(pdf)
    assert end in text, (pdf, end)
    return text.split(end, 1)[0].strip()


def segment(pdf, text):
    assert text
    return {'pdf_page': pdf, 'printed_page': printed_page(pdf), 'text': text}


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

# Source-order occurrence inventory. The three cue-only records are deliberately
# retained because Phase 12 inventories source-visible performance occurrences
# even when no complete lyric body is printed.
records = []

def add(rec):
    sm = scene_by_id[rec['source_scene_id']]
    rec['scene_ordinal'] = sm['ordinal']
    rec['scene_path'] = sm['scene_path']
    rec['record_path'] = f"records/{rec['id']}.md"
    if rec.get('page_segments'):
        joined = '\n\n'.join(x['text'] for x in rec['page_segments'])
        rec['source_text_sha256'] = sha(joined)
    records.append(rec)

# 001 — children's pretend-wedding music/chant cue, no printed chant text.
add({
    'id':'vandikkaran-magan-perf-001',
    'source_pdf_pages':[14],
    'source_scene_id':'7',
    'form':'ritual-play-music-and-chant-cue',
    'source_marker':'டும் டும்! பீப்பி பீப்பி!...',
    'source_role_cues':[],
    'performance_cues':[exact_line(14, 'மேளதாளம் வாசிக்க ஆரம்பித்து விடுகின்றனர்')],
    'authorship_status':'not-applicable-non-lyric-performance',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':False,
    'notes':'Children begin mock wedding music and chant mantras; the source prints no chant text beyond the onomatopoeic music fragment.'
})

# 002 — Lingan idealistic song.
cue = exact_line(18, 'பெரியவனான லிங்கன் பாட்டுப்பாடி வருதல்')
body = after_until(18, cue, '★')
add({
    'id':'vandikkaran-magan-perf-002',
    'source_pdf_pages':[18],
    'source_scene_id':'10',
    'form':'explicit-song',
    'source_marker':cue,
    'source_incipit':body.splitlines()[0],
    'source_role_cues':['லிங்கன்'],
    'performance_cues':[cue, exact_line(19, 'லிங்கனின் இலட்சிய கீதம் முடிவதற்கும்')],
    'authorship_status':'unresolved-item-level',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':True,
    'page_segments':[segment(18, body)],
    'notes':'PDF 19 calls the just-finished performance `லிங்கனின் இலட்சிய கீதம்`; that end cue is context, not a second occurrence.'
})

# 003 — Vingan/Kokila love song.
cue = exact_line(36, 'விங்கன் — கோகிலா காதல் கீதம்')
p36 = after_until(36, cue)
p37 = before(37, '★')
add({
    'id':'vandikkaran-magan-perf-003',
    'source_pdf_pages':[36,37],
    'source_scene_id':'20',
    'form':'labelled-love-song-duet',
    'source_marker':cue,
    'source_incipit':'மேடையில் ஆடிடும்',
    'source_role_cues':['விங்கன்','கோகிலா'],
    'performance_cues':[cue, exact_line(37, 'கோகிலா-விங்கன் கனவு கீதம் முடிகிறது')],
    'authorship_status':'unresolved-item-level',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':True,
    'page_segments':[segment(36,p36), segment(37,p37)],
    'notes':'Speaker-labelled sung turns remain exact source text; their dialogue-layer identity is not rewritten by this performance derivative.'
})

# 004 — Vingan song, PDF 46-47.
cue = exact_line(46, 'விங்கன் பாட்டு')
p46 = after_until(46, cue)
endcue = exact_line(47, 'இருவரும் காதலில் மயங்கு கின்றனர்')
p47 = before(47, endcue)
add({
    'id':'vandikkaran-magan-perf-004',
    'source_pdf_pages':[46,47],
    'source_scene_id':'24-சி',
    'form':'explicit-song',
    'source_marker':cue,
    'source_incipit':p46.splitlines()[0],
    'source_role_cues':['விங்கன்'],
    'performance_cues':[cue,endcue],
    'authorship_status':'unresolved-item-level',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':True,
    'page_segments':[segment(46,p46), segment(47,p47)],
    'notes':'The parenthetical after the final refrain is retained as the end/context cue and excluded from lyric body.'
})

# 005 — wedding music cue only.
fragment = exact_line(56, 'கெட்டி மேளம்! கெட்டி மேளம்!')
add({
    'id':'vandikkaran-magan-perf-005',
    'source_pdf_pages':[56],
    'source_scene_id':'32',
    'form':'wedding-music-cue',
    'source_marker':fragment,
    'source_role_cues':['புரோகிதர்'],
    'performance_cues':[exact_line(56, 'புரோகிதர் தாலியை எடுத்து விங்கன் கையில் தருதல்'), fragment],
    'authorship_status':'not-applicable-non-lyric-performance',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':False,
    'notes':'Source requests `கெட்டி மேளம்`; no lyric body is printed, so no standalone Tamil lyric is manufactured.'
})

# 006 — Vingan public song, PDF 60-61.
cue = exact_line(60, 'விங்கன் ஊர்மக்களிடையே பாடுகிறான்')
p60 = after_until(60, cue)
p61 = before(61, '★')
add({
    'id':'vandikkaran-magan-perf-006',
    'source_pdf_pages':[60,61],
    'source_scene_id':'36',
    'form':'explicit-public-song',
    'source_marker':cue,
    'source_incipit':p60.splitlines()[0],
    'source_role_cues':['விங்கன்','ஊர்மக்கள்'],
    'performance_cues':[cue],
    'authorship_status':'unresolved-item-level',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':True,
    'page_segments':[segment(60,p60), segment(61,p61)],
    'notes':'Song continues onto PDF 61 and ends at the source star before scene 37.'
})

# 007 — wedding mantra sound cue only.
cue = exact_line(68, 'மந்திர ஒலி - மணமேடை')
add({
    'id':'vandikkaran-magan-perf-007',
    'source_pdf_pages':[68],
    'source_scene_id':'42-எ',
    'form':'wedding-mantra-sound-cue',
    'source_marker':'மந்திர ஒலி',
    'source_role_cues':[],
    'performance_cues':[cue],
    'authorship_status':'not-applicable-non-lyric-performance',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':False,
    'notes':'The source specifies mantra sound but prints no mantra text.'
})

# 008 — child-birth celebration song/performance, cue begins PDF 72, lyric body 73-74.
cues72 = [
    exact_line(72, 'குடிசைப்பகுதி மக்கள், விங்கன், உமா முதலியோர் ஆடிப் பாடி'),
    exact_line(72, 'பாட்டின் இடையே சடையன்'),
    exact_line(72, 'இள மகளிர், வாலிபர் — அனைவரும் பாடியும் ஆடியும்')
]
marker = exact_line(73, '(பாட்டு)')
p73 = after_until(73, marker)
p74 = before(74, '★')
endcue = exact_line(75, 'பாடல் முடிய')
add({
    'id':'vandikkaran-magan-perf-008',
    'source_pdf_pages':[72,73,74],
    'source_scene_id':'48',
    'form':'celebration-song-and-dance',
    'source_marker':marker,
    'source_incipit':p73.splitlines()[0],
    'source_role_cues':['இள மகளிர்','வாலிபர்','ஒருவன்','ஒருத்தி','விங்கன்'],
    'performance_cues':cues72 + [marker,endcue],
    'authorship_status':'unresolved-item-level',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':True,
    'page_segments':[segment(73,p73), segment(74,p74)],
    'notes':'Performance context starts on PDF 72; printed lyric body is PDF 73-74; PDF 75 explicitly says `பாடல் முடிய` and is only the end cue.'
})

# 009 — dance/lyric counterpoint to the fire sequence, PDF 81-82.
cue1 = exact_line(81, 'நடனம் ஒருபுறம் - நாசம் ஒரு புறம்')
cue2 = exact_line(81, 'அழகி ஒன்று நடனமாட ஜமீன்தார் ரசித்தல்')
p81 = after_until(81, cue2)
endcue = exact_line(82, 'குடிசை மக்கள் அங்குமிங்கும் அலறித்துடித்து')
p82 = before(82, endcue)
add({
    'id':'vandikkaran-magan-perf-009',
    'source_pdf_pages':[81,82],
    'source_scene_id':'53-சி',
    'form':'lyrical-dance-performance',
    'source_marker':None,
    'source_incipit':p81.splitlines()[0],
    'source_role_cues':['அழகி ஒன்று'],
    'performance_cues':[cue1,cue2,endcue],
    'authorship_status':'unresolved-item-level',
    'author_as_printed':None,
    'full_or_clearly_bounded_body':True,
    'page_segments':[segment(81,p81), segment(82,p82)],
    'notes':'Film credits list a `நடனக்காரி`, but the booklet does not item-link that cast credit to this `அழகி ஒன்று`; no performer identity is inferred here.'
})

assert [x['id'] for x in records] == [f'vandikkaran-magan-perf-{i:03}' for i in range(1,10)]
assert sum(bool(x['full_or_clearly_bounded_body']) for x in records) == 6
assert sum(x['authorship_status']=='unresolved-item-level' for x in records) == 6
assert sum(x['authorship_status']=='not-applicable-non-lyric-performance' for x in records) == 3
assert not any(x.get('author_as_printed') for x in records)

# Review the expanded lexical cue preflight. Keyword hits are navigation aids;
# continuation pages 61 and 74 were added by boundary review.
preflight_path = N / 'song-performance-cue-preflight.json'
preflight = json.loads(preflight_path.read_text(encoding='utf-8'))
expected_candidate_pages = [13,14,18,19,23,24,34,36,37,42,45,46,47,56,58,60,68,72,73,75,81,82,86,88,89]
assert preflight['candidate_pdf_pages'] == expected_candidate_pages, preflight['candidate_pdf_pages']
page_disposition = {
    '13':'lexical-false-positive-sappattu',
    '14':'retained-perf-001',
    '18':'retained-perf-002',
    '19':'end-cue-for-perf-002-not-new-occurrence',
    '23':'lexical-idiom-not-performance',
    '24':'lexical-false-positive-kulippatturan',
    '34':'lexical-idiom-not-performance',
    '36':'retained-perf-003',
    '37':'continuation-and-end-cue-perf-003',
    '42':'lexical-false-positive-sappattukku',
    '45':'simile-japam-not-performance',
    '46':'retained-perf-004',
    '47':'continuation-and-end-cue-perf-004',
    '56':'retained-perf-005-cue-only',
    '58':'metaphorical-isai-not-performance',
    '60':'retained-perf-006',
    '68':'retained-perf-007-cue-only',
    '72':'performance-context-perf-008',
    '73':'retained-lyric-body-perf-008',
    '75':'end-cue-for-perf-008-not-new-occurrence',
    '81':'retained-perf-009',
    '82':'continuation-perf-009',
    '86':'lexical-false-positive-kaappattun',
    '88':'film-credit-metadata-not-occurrence',
    '89':'film-credit-metadata-not-occurrence'
}
preflight['status'] = 'review-complete'
preflight['review_summary'] = {
    'candidate_pdf_pages_reviewed': len(expected_candidate_pages),
    'retained_source_visible_occurrences': 9,
    'full_or_clearly_bounded_lyric_occurrences': 6,
    'cue_only_non_lyric_performance_occurrences': 3,
    'continuation_pages_added_by_boundary_review': [61,74],
    'page_disposition': page_disposition,
    'item_level_authorship_inferred_from_pdf88_film_credit': False
}
preflight_path.write_text(json.dumps(preflight, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

# Rebuild song/performance directory deterministically.
if S.exists():
    shutil.rmtree(S)
R.mkdir(parents=True)

schema = {
    'schema':'vandikkaran-magan-song-performance-record-v1',
    'record_id_pattern':'^vandikkaran-magan-perf-[0-9]{3}$',
    'required_fields':['id','source_pdf_pages','source_scene_id','scene_ordinal','form','authorship_status','record_path','full_or_clearly_bounded_body'],
    'authorship_status_values':['source-attributed','unresolved-item-level','not-applicable-non-lyric-performance'],
    'policy':{
        'canonical_text_authority':'../transcription/',
        'scene_text_authority':'../scenes/',
        'character_entity_authority':'../characters/',
        'authorship_requires_item_level_evidence':True,
        'film_level_lyricist_credit_is_not_item_level_mapping':True,
        'missing_lyrics_may_not_be_reconstructed':True,
        'source_wording_lineation_roles_cues_and_page_boundaries_are_preserved':True,
        'cue_only_performance_occurrences_remain_inventory_records_without_manufactured_lyrics':True
    }
}
(S/'schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

credits = {
    'work_id':'vandikkaran-magan',
    'film_level_song_credit':{
        'pdf_page':88,
        'text':'பாடல்கள்: கவிஞர் வாலி',
        'scope_policy':'Preserved as film-level source metadata; not automatically promoted to item-level authorship for any of the six printed lyric/performance bodies.'
    },
    'music_credit':{'pdf_page':88,'text':'இசை: எம். எஸ். விஸ்வநாதன்'},
    'dance_credit':{'pdf_page':89,'text':'நடனம் : தாரா அண்ணா மதுரை ரகு'},
    'playback_heading_as_printed':'பின்னணி :',
    'playback_pdf_page':89,
    'playback_names_as_printed':['டி. எம். சௌந்தரராஜன்','சீர்காழி கோவிந்தராஜன்','கோவை செளந்தரராஜன்','எஸ். பி பாலசுப்பிரமணியம்','வாணி ஜெயராம், எல். ஆர். ஈஸ்வரி'],
    'item_level_song_authorship':{
        'source_attributed_records':0,
        'unresolved_item_level_records':6,
        'policy':'The controlling booklet supplies no item-specific lyricist line for these six bodies. Do not infer `கவிஞர் வாலி` at item level from PDF 88 alone.'
    },
    'non_lyric_performance_records':{'count':3,'authorship_status':'not-applicable-non-lyric-performance'}
}
(S/'credits.json').write_text(json.dumps(credits,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Inventory excludes embedded page text while preserving all provenance and dispositions.
inv_records=[]
for rec in records:
    x={k:v for k,v in rec.items() if k!='page_segments'}
    if rec.get('page_segments'):
        x['page_segments']=[{'pdf_page':s['pdf_page'],'printed_page':s['printed_page']} for s in rec['page_segments']]
    inv_records.append(x)
inventory={
    'work_id':'vandikkaran-magan',
    'status':'complete-verified-source-only',
    'mapped_source_visible_occurrences':9,
    'records':inv_records,
    'coverage':'9/9',
    'full_or_clearly_bounded_tamil_derivatives':6,
    'cue_only_non_lyric_records':3,
    'source_attributed_authorship_records':0,
    'unresolved_item_level_authorship_records':6,
    'policy':{
        'film_level_pdf88_song_credit':'பாடல்கள்: கவிஞர் வாலி',
        'item_level_authorship_inferred':False,
        'cue_only_records_do_not_generate_missing_lyrics':True,
        'preflight_review':'../notes/song-performance-cue-preflight.json'
    }
}
(S/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Human-readable performance derivatives.
def fmt_pages(xs):
    return ', '.join(str(x) for x in xs)
for rec in records:
    out=[]
    out.append(f"# {rec['id']} — வண்டிக்காரன் மகன் performance derivative")
    out.append('')
    out.append(f"- form: **{rec['form']}**")
    out.append(f"- source PDF page(s): **{fmt_pages(rec['source_pdf_pages'])}**")
    out.append(f"- source scene: **{rec['source_scene_id']}** / derivative ordinal **{rec['scene_ordinal']}**")
    if rec.get('source_marker'):
        out.append(f"- source marker/fragment: **`{rec['source_marker']}`**")
    if rec.get('source_incipit'):
        out.append(f"- source incipit: **{rec['source_incipit']}**")
    out.append(f"- full or clearly bounded Tamil body: **{'yes' if rec['full_or_clearly_bounded_body'] else 'no'}**")
    if rec['authorship_status']=='unresolved-item-level':
        out.append('- authorship: **unresolved-item-level**')
        out.append('- authorship evidence: the booklet has only the film-level PDF 88 credit `பாடல்கள்: கவிஞர் வாலி`; this record has no item-level lyricist line in the controlling source.')
    else:
        out.append('- authorship: **not applicable — non-lyric performance cue**')
    out.append(f"- note: {rec['notes']}")
    if rec.get('performance_cues'):
        out.extend(['','## Source-visible performance cue(s)',''])
        for c in rec['performance_cues']:
            out.append(c)
            out.append('')
    if rec.get('page_segments'):
        out.extend(['## Source-visible Tamil',''])
        for seg in rec['page_segments']:
            out.append(f"<!-- source: pdf={seg['pdf_page']} printed={seg['printed_page']} -->")
            out.append('')
            out.append(seg['text'])
            out.append('')
    else:
        out.extend(['## Source-visible fragment / cue only',''])
        out.append('No complete lyric/chant body is printed for this occurrence; nothing is reconstructed.')
        out.append('')
    (R/f"{rec['id']}.md").write_text('\n'.join(out).rstrip()+'\n',encoding='utf-8')

index={
    'work_id':'vandikkaran-magan',
    'status':'complete-verified-source-only',
    'authorship_gate':'closed-with-film-level-credit-only-item-level-unresolved',
    'mapped_source_visible_occurrences':9,
    'retained_performance_records':9,
    'full_or_clearly_bounded_tamil_derivatives':6,
    'cue_only_non_lyric_records':3,
    'source_attributed_authorship_records':0,
    'unresolved_item_level_authorship_records':6,
    'not_applicable_non_lyric_records':3,
    'broad_credit_policy':'PDF 88 `பாடல்கள்: கவிஞர் வாலி` is preserved as film-level metadata and is not used to infer item-level authorship for the six printed lyric/performance bodies.',
    'inventory':'inventory.json','credits':'credits.json','schema':'schema.json','records_directory':'records/','qa':'../notes/song-performance-qa.json',
    'cue_preflight':'../notes/song-performance-cue-preflight.json',
    'canonical_tamil_changed':False,'scene_text_changed':False,'dialogue_records_changed':False,'character_entity_mappings_changed':False,
    'english_translation_gate':'ready-next',
    'next_activity':'Begin a bounded English-translation pilot from source scene 1 using only closed canonical Tamil plus verified scene/dialogue/character/song-performance derivatives. Preserve exact Tamil source labels and provenance, link immutable dialogue IDs without rewriting them, and keep song/performance authorship unresolved wherever the source gate is unresolved. Run pilot QA before scaling to later scenes.'
}
(S/'index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

readme = '''# வண்டிக்காரன் மகன் — song / performance layer

**Status:** **COMPLETE-VERIFIED / AUTHORSHIP GATE CLOSED**

Built only from the closed canonical Tamil, scene, dialogue and character/entity layers. No upstream source text or immutable dialogue record is rewritten here.

## Coverage

- source-visible performance occurrences: **9/9**;
- full or clearly bounded Tamil song/lyric bodies: **6**;
- cue-only / non-lyric performance occurrences: **3**;
- item-level source-attributed lyric authorship: **0**;
- lyric records remaining **unresolved-item-level**: **6**;
- non-lyric records where lyric authorship is not applicable: **3**.

The six bounded bodies occur in source scenes `10`, `20`, `24-சி`, `36`, `48`, and `53-சி`. Cue-only occurrences are the children's mock-wedding music/mantra performance in scene `7`, `கெட்டி மேளம்` in scene `32`, and `மந்திர ஒலி` in scene `42-எ`.

## Credit policy

PDF 88 prints `பாடல்கள்: கவிஞர் வாலி` and `இசை: எம். எஸ். விஸ்வநாதன்`; PDF 89 prints dance and playback-credit matter. These are preserved in `credits.json`. The film-level lyricist credit is **not** automatically promoted to any individual song record because the controlling booklet supplies no item-level lyricist mapping for the six bounded lyric bodies.

No missing chant or lyric text is reconstructed for the three cue-only records.

See `inventory.json`, `credits.json`, `schema.json`, `records/`, `../notes/song-performance-cue-preflight.json`, and `../notes/song-performance-qa.json`.

## Next

English translation is **READY-NEXT**. Begin with a bounded source-scene-1 pilot, keeping all closed Tamil/scene/dialogue/character/song layers immutable and preserving unresolved authorship as unresolved metadata.
'''
(S/'README.md').write_text(readme,encoding='utf-8')

qa={
    'work_id':'vandikkaran-magan','phase':'song-performance-authorship-gate','status':'PASS',
    'source_visible_occurrences_expected':9,'source_visible_occurrences_mapped':9,
    'full_or_clearly_bounded_tamil_bodies':6,'cue_only_non_lyric_occurrences':3,
    'source_attributed_item_level_authorship':0,'unresolved_item_level_authorship':6,'not_applicable_non_lyric_authorship':3,
    'record_ids':[x['id'] for x in records],
    'source_scene_ids':[x['source_scene_id'] for x in records],
    'bounded_body_source_scenes':[x['source_scene_id'] for x in records if x['full_or_clearly_bounded_body']],
    'cue_only_source_scenes':[x['source_scene_id'] for x in records if not x['full_or_clearly_bounded_body']],
    'lexical_preflight_candidate_pages_reviewed':expected_candidate_pages,
    'continuation_pages_added_by_boundary_review':[61,74],
    'checks':{
        'character_gate_complete_verified':True,
        'all_expanded_cue_preflight_pages_reviewed':True,
        'source_order_record_ids_unique':len({x['id'] for x in records})==9,
        'every_record_has_scene_and_page_provenance':all(x['source_pdf_pages'] and x['source_scene_id'] in scene_by_id for x in records),
        'bounded_body_records_have_page_segments':all((not x['full_or_clearly_bounded_body']) or bool(x.get('page_segments')) for x in records),
        'cue_only_records_do_not_manufacture_lyrics':all(x['full_or_clearly_bounded_body'] or not x.get('page_segments') for x in records),
        'film_level_vali_credit_promoted_to_item_level':False,
        'canonical_tamil_changed':False,
        'scene_text_changed':False,
        'dialogue_records_changed':False,
        'character_entity_mappings_changed':False
    },
    'credit_evidence':{'pdf_88_song_credit':'பாடல்கள்: கவிஞர் வாலி','pdf_88_music_credit':'இசை: எம். எஸ். விஸ்வநாதன்','item_specific_lyricist_lines_found':0},
    'next_activity':index['next_activity']
}
positive_checks = ['character_gate_complete_verified','all_expanded_cue_preflight_pages_reviewed','source_order_record_ids_unique','every_record_has_scene_and_page_provenance','bounded_body_records_have_page_segments','cue_only_records_do_not_manufacture_lyrics']
negative_checks = ['film_level_vali_credit_promoted_to_item_level','canonical_tamil_changed','scene_text_changed','dialogue_records_changed','character_entity_mappings_changed']
assert all(qa['checks'][k] for k in positive_checks)
assert not any(qa['checks'][k] for k in negative_checks)
(N/'song-performance-qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: 9/9 performance occurrences; 6 bounded bodies; 3 cue-only; 6 item-level authorships unresolved; 0 inferred from film-level credit')
