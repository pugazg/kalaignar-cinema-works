#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, re

from translation_batch_021_040_data import DIALOGUE_TRANSLATIONS as DA, DIALOGUE_NOTES as NA, ND as NDA
from translation_batch_021_040_data_b import DIALOGUE_TRANSLATIONS as DB, DIALOGUE_NOTES as NB, ND as NDB
from translation_batch_021_040_data_c import DIALOGUE_TRANSLATIONS as DC, DIALOGUE_NOTES as NC, ND as NDC
from translation_batch_021_040_data_d import DIALOGUE_TRANSLATIONS as DD, DIALOGUE_NOTES as NDNOTE, ND as NDD

W = Path(__file__).resolve().parents[1]
T = W / 'translations'
R = T / 'records'
D = W / 'dialogues' / 'records'
S = W / 'scenes'
P = W / 'transcription' / 'pages'
R.mkdir(parents=True, exist_ok=True)

TARGET_SCENES = list(range(21, 41))
BATCH_SIZE = 20
NEXT = (
    'Translate and verify archive scene ordinals 41–60 as the next 20-scene English batch. '
    'Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; '
    'keep source-unlabelled speech unassigned; link only verified song/performance occurrences; preserve unresolved item-level '
    'authorship as unresolved; and do not modify closed Tamil, scene, dialogue-record, character-mapping or song-record authorities.'
)

# Merge hand-authored source-faithful translation data.
DIALOGUE_TRANSLATIONS = {}
DIALOGUE_NOTES = {}
ND = {}
for src in (DA, DB, DC, DD):
    overlap = set(DIALOGUE_TRANSLATIONS) & set(src)
    assert not overlap, overlap
    DIALOGUE_TRANSLATIONS.update(src)
for src in (NA, NB, NC, NDNOTE):
    overlap = set(DIALOGUE_NOTES) & set(src)
    assert not overlap, overlap
    DIALOGUE_NOTES.update(src)
for src in (NDA, NDB, NDC, NDD):
    overlap = set(ND) & set(src)
    assert not overlap, overlap
    ND.update(src)
assert set(DIALOGUE_TRANSLATIONS) == set(TARGET_SCENES)
assert set(ND) == set(TARGET_SCENES)

# Closed upstream authority.
didx = json.loads((W / 'dialogues' / 'index.json').read_text(encoding='utf-8'))
cidx = json.loads((W / 'characters' / 'index.json').read_text(encoding='utf-8'))
songidx = json.loads((W / 'songs' / 'index.json').read_text(encoding='utf-8'))
assert didx['status'] == 'complete-verified-reconciled' and didx['dialogue_record_count'] == 773
assert cidx['status'] == 'complete-verified' and cidx['dialogue_record_coverage'] == '773/773'
assert songidx['status'] == 'complete-verified-source-only' and songidx['mapped_source_visible_occurrences'] == 9

scene_index_obj = json.loads((S / 'index.json').read_text(encoding='utf-8'))
scene_rows = scene_index_obj['scenes']
scene_meta = {int(x['ordinal']): x for x in scene_rows}
assert len(scene_meta) == 72
EXPECTED_SOURCE_SCENE_IDS = [scene_meta[n]['scene_id'] for n in TARGET_SCENES]
assert EXPECTED_SOURCE_SCENE_IDS == [
    '17','18','19','20','20-எ','21','22','22-எ','23','24','24-எ','24-பி','24-சி','24-டி','25','26','27','28','29','29-எ'
]

song_inventory = json.loads((W / 'songs' / 'inventory.json').read_text(encoding='utf-8'))
perf = {x['id']: x for x in song_inventory['records']}
assert perf['vandikkaran-magan-perf-003']['source_scene_id'] == '20'
assert perf['vandikkaran-magan-perf-004']['source_scene_id'] == '24-சி'

expected_counts = {n: int(didx['scene_record_counts'][f'vandikkaran-magan-s{n:03d}']) for n in TARGET_SCENES}
for n in TARGET_SCENES:
    assert len(DIALOGUE_TRANSLATIONS[n]) == expected_counts[n], (n, len(DIALOGUE_TRANSLATIONS[n]), expected_counts[n])
assert sum(expected_counts.values()) == 261, sum(expected_counts.values())


def norm(s: str) -> str:
    s = s.replace('\r\n', '\n').replace('\r', '\n')
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'^[#]+\s*', '', s, flags=re.M)
    s = s.replace('**', '')
    return re.sub(r'\s+', ' ', s).strip()


def source_blocks(n: int):
    text = (S / f'scene-{n:03d}.md').read_text(encoding='utf-8')
    parts = [b.strip() for b in re.split(r'\n[ \t]*\n', text) if b.strip()]
    out = []
    for b in parts:
        if b.startswith('<!-- derivative provenance:'):
            continue
        if b.startswith('## '):
            continue
        if b == '★':
            continue
        out.append(b)
    return out

page_cache = {}
def page_norm(p):
    if p not in page_cache:
        page_cache[p] = norm((P / f'{p:03d}.md').read_text(encoding='utf-8'))
    return page_cache[p]

fallbacks = []
def infer_pages(n, source_text, cursor_page):
    pages = list(scene_meta[n]['pdf_pages'])
    b = norm(source_text)
    exact = [p for p in pages if b and b in page_norm(p)]
    if exact:
        return [exact[0]], exact[0]
    first = b[:80] if len(b) > 80 else b
    last = b[-80:] if len(b) > 80 else b
    first_hits = [p for p in pages if first and first in page_norm(p)]
    last_hits = [p for p in pages if last and last in page_norm(p)]
    if first_hits and last_hits:
        a, z = first_hits[0], last_hits[-1]
        span = [p for p in pages if a <= p <= z]
        return span, z
    p = cursor_page if cursor_page in pages else pages[0]
    fallbacks.append({'scene_ordinal': n, 'source_text': b[:160], 'fallback_pdf_page': p})
    return [p], p


def page_prov(pages):
    return [{'pdf_page': int(p), 'printed_page': int(p)-1} for p in pages]


def consume_dialogue(blocks, i, row):
    """Return (end_index_exclusive, combined_source_text) when row matches blocks[i:].

    This permits a single immutable dialogue record to span a physical-page break represented
    by a blank-line split in the scene derivative (for example archive scene 35).
    """
    prefix = f"{row['speaker_label']}{row['source_delimiter']}"
    first = blocks[i]
    if not first.startswith(prefix):
        return None
    target = norm(row['text'])
    acc = first[len(prefix):].strip()
    j = i
    while True:
        a = norm(acc)
        if a == target:
            return j + 1, acc
        if not target.startswith(a) or j + 1 >= len(blocks):
            return None
        nxt = blocks[j + 1]
        # A continuation must not begin with a new explicit dialogue label that would change ownership.
        if any(nxt.startswith(f"{r['speaker_label']}{r['source_delimiter']}") for r in [row]) and j + 1 > i:
            return None
        acc += '\n' + nxt
        j += 1


def make_dialogue_unit(n, sid, unit_no, row, english, notes):
    return {
        'id': f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}',
        'kind': 'dialogue', 'status': 'verified', 'target_language': 'en',
        'scene_id': f'vandikkaran-magan-s{n:03d}', 'scene_ordinal': n, 'source_scene_id': sid,
        'source': {
            'source_path': f'works/vandikkaran-magan/dialogues/records/scene-{n:03d}.json',
            'canonical_scene_path': f'works/vandikkaran-magan/scenes/scene-{n:03d}.md',
            'source_record_id': row['id'], 'source_occurrence_id': None, 'source_locator': None,
            'speaker_label': row['speaker_label'], 'speaker_label_origin': 'source-explicit',
            'source_delimiter': row['source_delimiter'], 'page_provenance': row['page_provenance']
        },
        'translation': {'english_text': english, 'mode': 'prose-faithful', 'notes': notes}
    }


def make_nd_unit(n, sid, unit_no, block, spec, locator_no, pages):
    skind = spec.get('kind', 'stage')
    occurrence_id = spec.get('occurrence_id')
    locator_kind = spec.get('locator_kind') or (
        'source-unlabelled-speech' if skind == 'source-unlabelled' else
        'song-body' if skind == 'song' else
        'performance-cue' if skind == 'performance-cue' else
        'stage-direction'
    )
    notes = list(spec.get('notes', []))
    if occurrence_id:
        occ = perf[occurrence_id]
        if occ['authorship_status'] == 'unresolved-item-level':
            notes.append('Item-level lyric authorship remains unresolved; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to this occurrence.')
        elif occ['authorship_status'] == 'not-applicable-non-lyric-performance':
            notes.append('Linked source occurrence is non-lyric performance material; lyric authorship is not applicable.')
    if skind == 'source-unlabelled':
        notes.append('The source prints no speaker label for this spoken unit; no speaker or immutable dialogue ID is inferred.')
    source = {
        'source_path': f'works/vandikkaran-magan/scenes/scene-{n:03d}.md',
        'canonical_scene_path': f'works/vandikkaran-magan/scenes/scene-{n:03d}.md',
        'source_record_id': None, 'source_occurrence_id': occurrence_id,
        'source_locator': {'kind': locator_kind, 'ordinal': locator_no, 'description': f'Source block {locator_no}: {norm(block)[:140]}'},
        'speaker_label': None,
        'speaker_label_origin': 'source-unlabelled' if skind == 'source-unlabelled' else None,
        'source_delimiter': None,
        'page_provenance': page_prov(pages)
    }
    if skind == 'source-unlabelled':
        kind = 'dialogue'
    elif skind == 'song':
        kind = 'song'
    elif skind == 'performance-cue':
        kind = 'performance-cue'
    elif skind == 'written-text' or locator_kind == 'written-text':
        kind = 'written-text'
    else:
        kind = 'stage-direction'
    tr = {'mode': 'semantic-poetic-source-faithful' if skind == 'song' else 'prose-faithful', 'notes': notes}
    if skind == 'song':
        lines = spec['lines']
        source_line_count = len([x for x in block.splitlines() if x.strip()])
        assert len(lines) == source_line_count, (n, locator_no, len(lines), source_line_count, block)
        tr['english_lines'] = lines
    else:
        tr['english_text'] = spec['text']
    return {
        'id': f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}',
        'kind': kind, 'status': 'verified', 'target_language': 'en',
        'scene_id': f'vandikkaran-magan-s{n:03d}', 'scene_ordinal': n, 'source_scene_id': sid,
        'source': source, 'translation': tr
    }

new_scene_objects = []
for n in TARGET_SCENES:
    sid = scene_meta[n]['scene_id']
    rows = json.loads((D / f'scene-{n:03d}.json').read_text(encoding='utf-8'))
    blocks = source_blocks(n)
    dtrs = DIALOGUE_TRANSLATIONS[n]
    nds = ND[n]
    ri = di = ni = 0
    i = 0
    cursor = int(scene_meta[n]['pdf_pages'][0])
    units = []
    locator_no = 0
    while i < len(blocks):
        if ri < len(rows):
            matched = consume_dialogue(blocks, i, rows[ri])
            if matched:
                end_i, _combined = matched
                row = rows[ri]
                notes = list(DIALOGUE_NOTES.get((n, di+1), []))
                units.append(make_dialogue_unit(n, sid, len(units)+1, row, dtrs[di], notes))
                for pp in row['page_provenance']:
                    cursor = max(cursor, int(pp['pdf_page']))
                ri += 1; di += 1; i = end_i
                continue
        block = blocks[i]
        if ni >= len(nds):
            raise AssertionError(f'scene {n}: no non-dialogue translation spec left for source block: {block}')
        spec = nds[ni]
        locator_no += 1
        if spec.get('occurrence_id'):
            pages = list(perf[spec['occurrence_id']]['source_pdf_pages'])
            cursor = max(cursor, max(pages))
        else:
            pages, cursor = infer_pages(n, block, cursor)
        units.append(make_nd_unit(n, sid, len(units)+1, block, spec, locator_no, pages))
        ni += 1; i += 1
    assert ri == len(rows), (n, 'dialogue records unconsumed', ri, len(rows), rows[ri]['id'] if ri < len(rows) else None)
    assert di == len(dtrs), (n, 'dialogue translations unconsumed', di, len(dtrs))
    assert ni == len(nds), (n, 'non-dialogue specs unconsumed', ni, len(nds))
    obj = {
        'work_id':'vandikkaran-magan','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}',
        'scene_ordinal':n,'source_scene_id':sid,'scene_status':'verified','unit_count':len(units),'units':units
    }
    (R / f'scene-{n:03d}.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    new_scene_objects.append(obj)

assert not fallbacks, json.dumps(fallbacks, ensure_ascii=False, indent=2)

# Batch QA.
new_units = [u for s in new_scene_objects for u in s['units']]
new_links = [u['source']['source_record_id'] for u in new_units if u['source']['source_record_id']]
new_unlabelled = [u for u in new_units if u['source']['speaker_label_origin'] == 'source-unlabelled']
new_perf_units = [u for u in new_units if u['source']['source_occurrence_id']]
new_perf_ids = sorted({u['source']['source_occurrence_id'] for u in new_perf_units})
assert len(new_links) == 261 and len(set(new_links)) == 261
assert len(new_unlabelled) == 9, len(new_unlabelled)
assert new_perf_ids == ['vandikkaran-magan-perf-003','vandikkaran-magan-perf-004'], new_perf_ids
new_counts = Counter(u['kind'] for u in new_units)
qa = {
    'work_id':'vandikkaran-magan','phase':'english-translation-batch-021-040','status':'PASS',
    'batch_size_scenes':20,'scene_ordinals':TARGET_SCENES,'source_scene_ids':EXPECTED_SOURCE_SCENE_IDS,
    'verified_scenes':20,'verified_units':len(new_units),'unit_kind_counts':dict(sorted(new_counts.items())),
    'immutable_dialogue_records_expected':261,'immutable_dialogue_records_linked':261,
    'source_unlabelled_spoken_units':len(new_unlabelled),'inferred_speaker_assignments':0,
    'performance_linked_units':len(new_perf_units),'performance_occurrence_ids_linked':new_perf_ids,
    'unique_performance_occurrence_links':2,'source_page_provenance_fallbacks':0,
    'checks': {
        'all_20_target_scenes_present_in_source_order': True,
        'all_batch_immutable_dialogue_records_linked_exactly_once': True,
        'cross_page_dialogue_records_preserved_as_single_translation_units': True,
        'source_unlabelled_speech_kept_unassigned_and_unlinked': True,
        'source_scene_20_love_song_linked_to_verified_perf_003_only': True,
        'source_scene_24_ci_song_linked_to_verified_perf_004_only': True,
        'song_lineation_mapped_one_english_line_per_visible_tamil_line': True,
        'item_level_song_authorship_left_unresolved': True,
        'structural_star_translated_as_prose': False,
        'synthetic_scene_end_prose_added': False,
        'closed_tamil_scene_dialogue_character_song_records_modified_by_translation': False
    },
    'next_activity': NEXT
}
(T / 'batch-021-040-qa.json').write_text(json.dumps(qa, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

(T / 'BATCH_021_040_REVIEW.md').write_text(f'''# வண்டிக்காரன் மகன் — English scenes 21–40 review

Status: **PASS / VERIFIED**

This iteration follows the work-specific **20-scene English batch** rule requested by the user.

- archive scene ordinals: **21–40 / 20 scenes**;
- source scene IDs: `{', '.join(EXPECTED_SOURCE_SCENE_IDS)}`;
- verified translation units: **{len(new_units)}**;
- immutable dialogue records linked: **261/261 exactly once**;
- source-unlabelled spoken units: **{len(new_unlabelled)}**, retained without speaker inference;
- verified performance occurrences linked: **2 unique IDs** — `vandikkaran-magan-perf-003` and `vandikkaran-magan-perf-004`;
- item-level authorship of both linked song occurrences remains **unresolved-item-level**;
- page-provenance fallback assignments: **0**;
- upstream canonical Tamil / scene text / immutable dialogue records / character mappings / song records rewritten: **0**.

Archive scene 24/source scene 20 preserves the Vingan–Kokila dream duet in source block and line order. Archive scene 33/source scene `24-சி` preserves Vingan's printed song in source block and line order. The film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to either item-level occurrence.

**Next:** {NEXT}
''', encoding='utf-8')

# Rebuild cumulative translation index through scene 40.
all_scene_objs = []
for n in range(1, 41):
    p = R / f'scene-{n:03d}.json'
    assert p.exists(), p
    obj = json.loads(p.read_text(encoding='utf-8'))
    assert obj['scene_status'] == 'verified' and obj['scene_ordinal'] == n
    all_scene_objs.append(obj)
all_units = [u for s in all_scene_objs for u in s['units']]
all_counts = Counter(u['kind'] for u in all_units)
all_links = [u['source']['source_record_id'] for u in all_units if u['source']['source_record_id']]
all_unlabelled = [u for u in all_units if u['source']['speaker_label_origin'] == 'source-unlabelled']
all_perf_units = [u for u in all_units if u['source']['source_occurrence_id']]
all_perf_ids = sorted({u['source']['source_occurrence_id'] for u in all_perf_units})
assert len(all_links) == len(set(all_links))
assert len(all_links) == 512, len(all_links)
assert len(all_unlabelled) == 13, len(all_unlabelled)
assert all_perf_ids == ['vandikkaran-magan-perf-001','vandikkaran-magan-perf-002','vandikkaran-magan-perf-003','vandikkaran-magan-perf-004']
cross_page_units = sum(1 for u in all_units if len(u['source']['page_provenance']) > 1)
idx = {
    'work_id':'vandikkaran-magan','target_language':'en','status':'verified-through-scene-040',
    'total_scene_derivatives':72,'verified_scenes':40,'verified_scene_ordinals':list(range(1,41)),
    'verified_source_scene_ids':[scene_meta[n]['scene_id'] for n in range(1,41)],
    'translation_units':len(all_units),'unit_kind_counts':dict(sorted(all_counts.items())),
    'immutable_dialogue_records_linked':len(all_links),'source_unlabelled_spoken_units':len(all_unlabelled),
    'performance_linked_units':len(all_perf_units),'performance_occurrence_links':len(all_perf_ids),
    'performance_occurrence_ids_linked':all_perf_ids,'cross_page_units':cross_page_units,
    'batch_size_scenes':20,'schema':'schema.json','records_directory':'records/','pilot_qa':'pilot-qa.json',
    'latest_batch_qa':'batch-021-040-qa.json','latest_batch_review':'BATCH_021_040_REVIEW.md',
    'next_activity':NEXT
}
(T / 'index.json').write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

(T / 'README.md').write_text(f'''# வண்டிக்காரன் மகன் — English translation

**Status:** **VERIFIED THROUGH ARCHIVE SCENE 040 / QA PASS**

- verified scenes: **40/72**;
- verified archive scene ordinals: **1–40**;
- cumulative translation units: **{len(all_units)}**;
- unit kinds: **{', '.join(f'{k}={v}' for k,v in sorted(all_counts.items()))}**;
- immutable dialogue links: **{len(all_links)}**;
- source-unlabelled spoken units: **{len(all_unlabelled)}**, with **0 inferred speakers**;
- unique song/performance occurrence links: **{len(all_perf_ids)}** — `{', '.join(all_perf_ids)}`;
- current production batch size: **20 scenes per iteration**;
- latest batch: **archive scenes 21–40 / PASS / 261 of 261 immutable dialogue records linked exactly once**;
- upstream source-layer mutations caused by translation: **0**.

See `batch-021-040-qa.json`, `BATCH_021_040_REVIEW.md`, `records/scene-021.json` through `records/scene-040.json`, and `index.json`.

## Next

{NEXT}
''', encoding='utf-8')

print(json.dumps({
    'status':'PASS','batch':'21-40','batch_scenes':20,'batch_units':len(new_units),
    'batch_dialogue_links':len(new_links),'batch_source_unlabelled':len(new_unlabelled),
    'cumulative_scenes':40,'cumulative_units':len(all_units),'cumulative_dialogue_links':len(all_links),
    'cumulative_source_unlabelled':len(all_unlabelled),'cumulative_performance_occurrences':len(all_perf_ids),
    'cross_page_units':cross_page_units,'next_activity':NEXT
}, ensure_ascii=False, indent=2))
