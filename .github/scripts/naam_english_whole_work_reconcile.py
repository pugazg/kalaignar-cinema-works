from pathlib import Path
import collections, hashlib, json, re

W = Path('works/naam')
T = W / 'translations'

NEXT = (
    "Begin Phase 10 whole-work reader/export generation from the complete-verified Tamil and English structured layers. "
    "Build deterministic Markdown, standalone HTML, machine-readable JSON, reader QA, and an integrity manifest; verify all 45 source scenes appear exactly once in canonical order and all 797 verified English units render exactly once; preserve all 590 immutable dialogue links, the seven retained performance records, the distinct scene-34 chant, written text, source-unlabelled speech, exact cross-page provenance, and source-page linkage; prohibit duplicate source-span ownership, synthetic scene-end prose, placeholder/editorial leakage, or upstream source-layer mutation. "
    "After reader QA passes, prepare structured data for Kalaignar Digital Library / Reading Room integration. Do not create a PDF, EPUB, or other publication package unless separately requested."
)

BATCH_QA = [
    T / 'pilot-qa.json',
    T / 'batch-002-005-qa.json',
    T / 'batch-006-015-qa.json',
    T / 'batch-016-025-qa.json',
    T / 'batch-026-035-qa.json',
    T / 'batch-036-045-qa.json',
]
UPSTREAM_ROOTS = [
    W / 'transcription', W / 'scenes', W / 'dialogues', W / 'characters', W / 'songs' / 'records'
]
PLACEHOLDER_RE = re.compile(r'\b(?:TODO|TBD|PLACEHOLDER|FIXME|TRANSLATE(?:\s+ME)?)\b', re.I)
UNLABELLED_ID_RE = re.compile(r'naam-s\d{3}-u\d{3}')
SYNTHETIC_END = {
    'scene ends', 'scene ends.', 'end of scene', 'end of scene.',
    'the scene ends', 'the scene ends.', '[scene ends]', '[end of scene]'
}


def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p, s): Path(p).parent.mkdir(parents=True, exist_ok=True); Path(p).write_text(s, encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p, d): wt(p, json.dumps(d, ensure_ascii=False, indent=2) + '\n')
def digest(root):
    h = hashlib.sha256()
    for p in sorted(Path(root).rglob('*')):
        if p.is_file():
            h.update(str(p).encode()); h.update(b'\0'); h.update(p.read_bytes()); h.update(b'\0')
    return h.hexdigest()

def all_strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, list):
        for x in v: yield from all_strings(x)
    elif isinstance(v, dict):
        for x in v.values(): yield from all_strings(x)

def english_payload_strings(unit):
    tr = unit.get('translation', {})
    if isinstance(tr.get('english_text'), str): yield tr['english_text']
    for x in tr.get('english_lines', []) or []:
        if isinstance(x, str): yield x
    for lm in tr.get('line_map', []) or []:
        if isinstance(lm, dict) and isinstance(lm.get('english'), str): yield lm['english']

def pages(unit): return [x['pdf_page'] for x in unit['source']['page_provenance']]

# Entry gate.
idx = rj(T / 'index.json')
assert idx['status'] == 'scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next'
assert idx['verified_scenes'] == 45 and idx['translation_units_verified'] == 797
assert idx['immutable_dialogue_links_verified'] == 590
assert idx['source_unlabelled_speech_units_verified'] == 20
assert idx['retained_performance_records_translated'] == 7
assert idx['song_line_cue_mappings_verified'] == 138
assert idx['source_chant_units_verified'] == 1 and idx['source_chant_line_cue_mappings_verified'] == 16
assert idx['whole_work_reconciliation_status'] == 'ready-next'

# Batch closure evidence must all be PASS; no batch may have admitted source/authorship corruption.
batch_status = {}
for p in BATCH_QA:
    q = rj(p)
    assert q['status'] == 'PASS', p
    if 'authorship_status_changed_by_translation' in q:
        assert q['authorship_status_changed_by_translation'] is False, p
    if 'external_or_unprinted_lyrics_imported' in q:
        assert q['external_or_unprinted_lyrics_imported'] is False, p
    batch_status[p.name] = q['status']

scene_index = rj(W / 'scenes' / 'index.json')
scene_meta = {x['source_scene_number']: x for x in scene_index['scene_records']}
assert set(scene_meta) == set(range(1, 46))

song_inv = rj(W / 'songs' / 'inventory.json')
perf_records = song_inv['records']
perf_ids = [x['id'] for x in perf_records]
assert perf_ids == ['naam-perf-007','naam-perf-001','naam-perf-002','naam-perf-003','naam-perf-004','naam-perf-005','naam-perf-006']
assert song_inv['coverage'] == '7/7'
assert song_inv['source_attributed_authorship_records'] == 1
assert song_inv['unresolved_item_level_authorship_records'] == 6
assert next(x for x in perf_records if x['id']=='naam-perf-001')['author_as_printed'] == 'பாரதியார்'
for x in perf_records:
    if x['id'] != 'naam-perf-001':
        assert x['authorship_status'] == 'unresolved-item-level' and x['author_as_printed'] is None
perf_by_id = {x['id']:x for x in perf_records}

unlabelled_audit = rj(W / 'notes' / 'unlabelled-block-audit.json')
audit_blocks = {x['block_id']:x for x in unlabelled_audit['blocks']}

unit_ids = []
linked_dialogue = []
source_dialogue = []
unlabelled_unit_ids = []
unlabelled_block_ids = []
kind_counts = collections.Counter()
perf_first_order = []
perf_unit_ids = collections.defaultdict(list)
perf_map_counts = collections.Counter()
cross_page = []
written_text = []
non_dialogue_owner = {}
duplicate_non_dialogue_owners = []
placeholder_hits = []
synthetic_end_hits = []
source_order_failures = []
page_bound_failures = []
line_map_failures = []
scene_unit_counts = {}

for n in range(1, 46):
    tr = rj(T / 'records' / f'scene-{n:03d}.json')
    src = rj(W / 'dialogues' / 'records' / f'scene-{n:03d}.json')
    sm = scene_meta[n]
    assert tr['work_id'] == 'naam' and tr['target_language'] == 'en'
    assert tr['scene_id'] == f'naam-s{n:03d}' and tr['scene_ordinal'] == n and tr['source_scene_number'] == n
    assert tr['scene_status'] == 'verified' and tr['unit_count'] == len(tr['units'])
    assert [u['id'] for u in tr['units']] == [f'naam-en-s{n:03d}-u{i:03d}' for i in range(1, len(tr['units'])+1)]
    scene_unit_counts[str(n)] = len(tr['units'])

    linked_in_scene = []
    prev_first_page = -1
    scene_pages = set(sm['pdf_pages'])
    for u in tr['units']:
        unit_ids.append(u['id'])
        assert u['status'] == 'verified' and u['target_language'] == 'en'
        assert u['scene_id'] == tr['scene_id'] and u['scene_ordinal'] == n and u['source_scene_number'] == n
        kind_counts[u['kind']] += 1

        pp = pages(u)
        assert pp and pp == sorted(dict.fromkeys(pp)), u['id']
        if pp[0] < prev_first_page: source_order_failures.append(u['id'])
        prev_first_page = pp[0]
        if not set(pp).issubset(scene_pages): page_bound_failures.append(u['id'])
        if len(pp) > 1: cross_page.append(u['id'])

        rid = u['source'].get('source_record_id')
        if rid:
            linked_in_scene.append(rid); linked_dialogue.append(rid)
            r = next(x for x in src if x['id'] == rid)
            assert u['kind'] == 'dialogue'
            assert u['source']['speaker_label'] == r['speaker_label']
            assert u['source']['source_delimiter'] == r['source_delimiter']
            assert u['source']['page_provenance'] == r['page_provenance']
            assert u['source']['speaker_label_origin'] == 'source-explicit'
        elif u['kind'] == 'dialogue':
            assert u['source'].get('speaker_label') is None
            assert u['source'].get('source_delimiter') is None
            assert u['source'].get('speaker_label_origin') is None
            unlabelled_unit_ids.append(u['id'])
            loc = u['source'].get('source_locator') or {}
            m = UNLABELLED_ID_RE.search(loc.get('description',''))
            assert m, u['id']
            bid = m.group(0)
            assert bid in audit_blocks, (u['id'], bid)
            unlabelled_block_ids.append(bid)

        occ = u['source'].get('source_occurrence_id')
        if occ:
            assert occ in perf_by_id, (u['id'], occ)
            if occ not in perf_first_order: perf_first_order.append(occ)
            perf_unit_ids[occ].append(u['id'])
            assert set(pp).issubset(set(perf_by_id[occ]['source_pdf_pages'])), (u['id'], occ, pp)
            lm = u.get('translation',{}).get('line_map',[]) or []
            perf_map_counts[occ] += len(lm)
            if lm:
                if [x.get('ordinal') for x in lm] != list(range(1, len(lm)+1)):
                    line_map_failures.append(u['id'])
                for x in lm:
                    if not str(x.get('tamil','')).strip() or not str(x.get('english','')).strip(): line_map_failures.append(u['id'])
                    if x.get('pdf_page') not in pp: line_map_failures.append(u['id'])

        if u['kind'] == 'written-text':
            written_text.append(u['id'])
            assert rid is None and u['source'].get('speaker_label') is None and u['source'].get('source_delimiter') is None
        if u['kind'] in {'stage-direction','narrative','performance-cue','chant','written-text'}:
            assert u['source'].get('speaker_label') is None and u['source'].get('source_delimiter') is None

        # Exact duplicate scene-local non-dialogue locator = duplicate source-span ownership.
        if rid is None and occ is None and u['kind'] != 'dialogue':
            loc = u['source'].get('source_locator') or {}
            key = (u['scene_id'], u['kind'], u['source'].get('source_path'), tuple(pp), loc.get('kind'), loc.get('ordinal'), loc.get('description'))
            if key in non_dialogue_owner: duplicate_non_dialogue_owners.append([non_dialogue_owner[key],u['id']])
            else: non_dialogue_owner[key] = u['id']

        payload = list(english_payload_strings(u))
        assert payload and any(x.strip() for x in payload), u['id']
        for text in payload:
            if PLACEHOLDER_RE.search(text): placeholder_hits.append(u['id'])
            if text.strip().lower() in SYNTHETIC_END: synthetic_end_hits.append(u['id'])

    assert linked_in_scene == [x['id'] for x in src], n
    source_dialogue.extend(x['id'] for x in src)

# Whole-work invariants.
assert len(unit_ids) == len(set(unit_ids)) == 797
assert source_order_failures == []
assert page_bound_failures == []
assert line_map_failures == []
assert len(linked_dialogue) == len(set(linked_dialogue)) == 590 and linked_dialogue == source_dialogue
assert len(unlabelled_unit_ids) == 20 and len(set(unlabelled_block_ids)) == 20
assert len(unlabelled_block_ids) == 20
assert perf_first_order == perf_ids
assert set(perf_unit_ids) == set(perf_ids)
assert sum(perf_map_counts.values()) == 138
assert all(perf_map_counts[x] > 0 for x in perf_ids)
assert kind_counts['dialogue'] == 610
assert kind_counts['song'] == 6
assert kind_counts['chant'] == 1
assert kind_counts['performance-cue'] == 6
assert kind_counts['written-text'] == 2
assert kind_counts['stage-direction'] + kind_counts['narrative'] == 172
assert sum(kind_counts.values()) == 797
assert written_text == ['naam-en-s041-u012','naam-en-s045-u025']
assert duplicate_non_dialogue_owners == []
assert placeholder_hits == []
assert synthetic_end_hits == []
assert cross_page == idx['cross_page_translation_units'] and len(cross_page) == 12

# Dedicated chant is distinct from the retained performance inventory and maps 16 source lines/cues.
chant_units = []
chant_maps = 0
for n in range(1,46):
    tr = rj(T / 'records' / f'scene-{n:03d}.json')
    for u in tr['units']:
        if u['kind'] == 'chant':
            chant_units.append(u['id'])
            assert u['scene_id'] == 'naam-s034' and u['source'].get('source_occurrence_id') is None
            chant_maps += len(u['translation'].get('line_map',[]) or [])
assert chant_units == ['naam-en-s034-u002'] and chant_maps == 16

# Upstream integrity snapshot supplied by workflow; the reconciliation script itself may only mutate translation/mirror surfaces.
up_before_path = Path('/tmp/naam-upstream-before.json')
up_before = json.loads(up_before_path.read_text()) if up_before_path.exists() else {str(p):digest(p) for p in UPSTREAM_ROOTS}
up_after = {str(p):digest(p) for p in UPSTREAM_ROOTS}
assert up_before == up_after

qa = {
    'work_id':'naam',
    'phase':'english-translation-whole-work-reconciliation',
    'status':'PASS',
    'source_scenes_expected':45,
    'source_scenes_verified':45,
    'translation_units_expected':797,
    'translation_units_verified':797,
    'unit_ids_unique_and_sequential':True,
    'source_order_failures':source_order_failures,
    'kind_counts':dict(sorted(kind_counts.items())),
    'stage_or_narrative_units':kind_counts['stage-direction'] + kind_counts['narrative'],
    'immutable_dialogue_records_expected':590,
    'immutable_dialogue_records_linked':590,
    'immutable_dialogue_ids_unique':True,
    'dialogue_source_order_exact':True,
    'source_unlabelled_speech_units':20,
    'source_unlabelled_speaker_assignments':0,
    'source_unlabelled_audit_blocks_referenced_exactly_once':20,
    'retained_performance_records_expected':7,
    'retained_performance_records_translated':7,
    'performance_occurrence_order':perf_first_order,
    'performance_line_cue_mappings':sum(perf_map_counts.values()),
    'performance_mapping_counts':dict(perf_map_counts),
    'specific_source_authorship_preserved':{'naam-perf-001':'பாரதியார்'},
    'unsupported_authorship_upgrades':0,
    'source_local_chant_units':chant_units,
    'source_local_chant_line_cue_mappings':chant_maps,
    'source_local_chant_promoted_to_performance_inventory':False,
    'written_text_units':written_text,
    'cross_page_translation_units':cross_page,
    'cross_page_unit_count':len(cross_page),
    'provenance_out_of_scene_bounds':page_bound_failures,
    'duplicate_non_dialogue_source_owners':duplicate_non_dialogue_owners,
    'placeholder_hits':placeholder_hits,
    'synthetic_scene_end_hits':synthetic_end_hits,
    'batch_qa_status':batch_status,
    'upstream_integrity_before':up_before,
    'upstream_integrity_after':up_after,
    'upstream_source_layers_modified':False,
    'reader_export_gate':'READY-NEXT',
    'next_activity':NEXT,
}
wj(T / 'whole-work-reconciliation.json', qa)

report = f'''# நாம் — Whole-work English translation reconciliation\n\n**Status:** **PASS / COMPLETE-VERIFIED**  \n**Scope:** source scenes **1–45**  \n**Verified English units:** **797/797**  \n**Immutable dialogue linkage:** **590/590 exactly once**\n\n## Closure result\n\nThe entire 45-scene English layer was reconciled as one work-level gate rather than trusted as a concatenation of batch results. All **797** translation units have unique sequential scene-local IDs and remain in non-decreasing source-page order. All **590** immutable dialogue records are linked exactly once and in the exact source dialogue order with Tamil speaker labels, delimiters, and page provenance preserved.\n\nThe **20** source-unlabelled speech units remain explicitly unassigned and map to **20 distinct audited source blocks**; inferred speakers: **0**. The two written-text units remain non-dialogue (`naam-en-s041-u012`, `naam-en-s045-u025`).\n\nAll **7/7** retained performance occurrences are represented in source order with **138** Tamil→English line/cue mappings. `naam-perf-001` retains the specific source attribution **பாரதியார்**; the other six retain unresolved item-level authorship. Translation introduced **0** authorship upgrades. Scene 34's villagers' street-play remains a distinct **chant** with **16** mappings and is not promoted into the seven-record performance inventory.\n\n## Whole-work QA\n\n- scenes: **45/45 exactly once and canonical order**;\n- English units: **797/797 unique and sequential**;\n- dialogue records: **590/590 exactly once**;\n- dialogue units total: **{kind_counts['dialogue']}** = 590 labelled + 20 source-unlabelled;\n- stage/narrative units: **{kind_counts['stage-direction'] + kind_counts['narrative']}**;\n- performance-cue units: **{kind_counts['performance-cue']}**;\n- song units: **{kind_counts['song']}**;\n- chant units: **1 / 16 mappings**;\n- written-text units: **2**;\n- performance records: **7/7 / 138 mappings**;\n- cross-page units: **{len(cross_page)}**, exact list reconciled;\n- provenance outside source-scene bounds: **0**;\n- duplicate non-dialogue source-span owners: **0**;\n- placeholder/editorial leakage: **0**;\n- synthetic scene-end prose: **0**;\n- upstream Tamil / scenes / dialogues / characters / Tamil performance records changed: **0**.\n\n## Batch evidence\n\nAll six prior English QA checkpoints remain **PASS**: pilot, scenes 2–5, 6–15, 16–25, 26–35, and 36–45. The whole-work gate independently rechecked their merged result.\n\n## English phase disposition\n\nEnglish translation is now **COMPLETE-VERIFIED**. Reader/export work is authorized as the next downstream phase; closed source and translation records remain immutable inputs.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
wt(T / 'WHOLE_WORK_RECONCILIATION.md', report)

# Translation index closure.
idx['status'] = 'complete-verified'
idx['whole_work_reconciliation_status'] = 'PASS'
idx['whole_work_reconciliation_qa'] = 'whole-work-reconciliation.json'
idx['whole_work_reconciliation_report'] = 'WHOLE_WORK_RECONCILIATION.md'
idx['reader_export_status'] = 'ready-next'
idx['next_activity'] = NEXT
idx['translation_units_verified'] = 797
idx['immutable_dialogue_links_verified'] = 590
idx['retained_performance_records_translated'] = 7
idx['song_line_cue_mappings_verified'] = 138
idx['source_unlabelled_speech_units_verified'] = 20
idx['source_chant_units_verified'] = 1
idx['source_chant_line_cue_mappings_verified'] = 16
idx['whole_work_kind_counts'] = dict(sorted(kind_counts.items()))
wj(T / 'index.json', idx)

# Translation README active state.
p = T / 'README.md'; s = rt(p)
s = re.sub(r'\*\*Status:\*\* \*\*.*?\*\*', '**Status:** **COMPLETE-VERIFIED / whole-work reconciliation PASS**', s, count=1)
s = re.sub(r'## Next gate\n\n.*?(?=\n##|\Z)', f'## Next gate\n\n{NEXT}\n', s, flags=re.S)
if '## Whole-work English closure' not in s:
    s += f'''\n## Whole-work English closure\n\n- scenes: **45/45**;\n- units: **797/797**;\n- immutable dialogue links: **590/590 exactly once**;\n- source-unlabelled speech: **20 / inferred speakers 0**;\n- retained performances: **7/7 / 138 mappings**;\n- scene-local chant: **1 / 16 mappings**;\n- written text: **2 units**;\n- cross-page units: **12**;\n- duplicate source ownership / placeholders / synthetic scene-end prose: **0 / 0 / 0**;\n- reconciliation: `whole-work-reconciliation.json` — **PASS**;\n- upstream source-layer mutations: **0**.\n\n**Next:** {NEXT}\n'''
wt(p,s)

# Work metadata: close both structured derivative and active status surfaces.
p = W / 'metadata.yaml'; s = rt(p)
s = re.sub(r'(?m)^  english_translation: scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next$', '  english_translation: complete-verified', s, count=1)
s = re.sub(r'(?m)^  english_whole_work_reconciliation: ready-next$', '  english_whole_work_reconciliation: PASS', s, count=1)
anchor = '  english_whole_work_reconciliation: PASS'
if '  english_whole_work_reconciliation_qa_path:' not in s:
    s = s.replace(anchor, anchor + '\n  english_whole_work_reconciliation_qa_path: "translations/whole-work-reconciliation.json"\n  english_reader_export: ready-next', 1)
else:
    s = re.sub(r'(?m)^  english_whole_work_reconciliation_qa_path:.*$', '  english_whole_work_reconciliation_qa_path: "translations/whole-work-reconciliation.json"', s, count=1)
    s = re.sub(r'(?m)^  english_reader_export:.*$', '  english_reader_export: ready-next', s, count=1)
s = re.sub(r'(?m)^  english_translation: in-progress-verified-25-of-45$', '  english_translation: complete-verified-45-of-45', s, count=1)
s = re.sub(r'(?m)^  reader_export: not-started$', '  reader_export: ready-next', s, count=1)
s = re.sub(r'(?m)^next_action:.*$', 'next_action: ' + json.dumps(NEXT, ensure_ascii=False), s, count=1)
wt(p,s)

# Work README: active checkpoint only; historical checkpoints remain historical.
p = W / 'README.md'; s = rt(p)
s = re.sub(r'- English translation: \*\*45/45 SCENE LAYER VERIFIED.*?\*\*; reader / Reading Room: \*\*blocked until reconciliation PASS\*\*\.', '- English translation: **45/45 COMPLETE-VERIFIED / 797 units / 590/590 dialogue links / 7/7 performance records / 138 performance mappings / 1 chant (16 mappings) / whole-work QA PASS**; reader/export: **READY-NEXT**.', s, count=1)
s = re.sub(r'\*\*Next:\*\* Run whole-work English translation reconciliation.*?(?=\n|$)', '**Next:** ' + NEXT, s, count=1)
if '## English whole-work reconciliation closure' not in s:
    s += f'''\n\n## English whole-work reconciliation closure\n\n- English translation: **COMPLETE-VERIFIED**;\n- whole-work QA: **PASS**;\n- source scenes: **45/45**;\n- verified English units: **797/797**;\n- immutable dialogue links: **590/590 exactly once**;\n- source-unlabelled speech: **20 / inferred labels 0**;\n- performances: **7/7 / 138 mappings**;\n- chant: **1 / 16 mappings**;\n- cross-page units: **12**;\n- duplicate source owners / placeholders / synthetic scene ends: **0 / 0 / 0**;\n- upstream changes: **0**;\n- reader/export: **READY-NEXT**.\n\n**Next:** {NEXT}\n'''
wt(p,s)

# Rewrite active top of project handover; preserve the long historical audit below Source identity.
p = W / 'PROJECT_HANDOVER.md'; s = rt(p)
new_current = f'''## Current checkpoint\n\n- source intake / whole scan / mapping: **complete / 72/72 / verified**;\n- canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- visual fidelity / historical glyph: **67/67 PASS / 67/67 final-verified**;\n- source-numbered scene derivatives: **45/45 COMPLETE-VERIFIED / boundary QA PASS**;\n- immutable dialogue index: **590 records / COMPLETE-VERIFIED / QA PASS**;\n- character/entity index: **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED**;\n- song/performance gate: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY / 1 source-attributed + 6 unresolved item-level**;\n- English translation: **45/45 COMPLETE-VERIFIED / 797 units / 590/590 dialogue links / 20 unlabelled with 0 inferred speakers / 7/7 performances / 138 mappings / 1 chant (16 mappings)**;\n- whole-work English reconciliation: **PASS**;\n- reader/export: **READY-NEXT**; Reading Room integration: **not-started**.\n\nCurrent authoritative downstream files:\n\n- `translations/index.json`;\n- `translations/whole-work-reconciliation.json`;\n- `translations/WHOLE_WORK_RECONCILIATION.md`;\n- `translations/records/scene-001.json`–`scene-045.json`;\n- `dialogues/index.json`;\n- `characters/index.json`;\n- `songs/index.json`;\n- `scenes/index.json`;\n- `transcription/index.json`.\n\n## Current exact next activity\n\n> **{NEXT}**\n\n'''
s = re.sub(r'## Current checkpoint\n.*?(?=## Source identity\n)', new_current, s, count=1, flags=re.S)
wt(p,s)

# Next chat prompt: active startup source must contain no obsolete gate.
wt(W / 'NEXT_CHAT_PROMPT.md', f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**\n\nCanonical Tamil **67/67 COMPLETE-VERIFIED**; scene derivatives **45/45 COMPLETE-VERIFIED**; immutable dialogue index **590 records / QA PASS**; character/entity layer **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY**.\n\nEnglish translation is now **COMPLETE-VERIFIED** after whole-work reconciliation: **45/45 scenes**, **797 verified units**, **590/590 immutable dialogue links**, **20 source-unlabelled speech units with 0 inferred speakers**, **7/7 retained performance records**, **138 performance line/cue mappings**, **1 distinct scene-34 chant / 16 mappings**, **2 written-text units**, and **12 cross-page units**. Whole-work reconciliation: `translations/whole-work-reconciliation.json` — **PASS**.\n\nAuthorship remains source-honest: `naam-perf-001` → **பாரதியார்**; the other six retained performance records remain unresolved at item level. Scene 34's chant is not a `naam-perf-*` record. Scene 41 `கடிதத்தில் :-` remains written text, `ஜீவானந்தர் —` retains the source em dash, and `உன்மீனு` remains the exact source label. Scene 45's closing rhetorical questions remain source-unlabelled.\n\nReader/export is **READY-NEXT**. Closed Tamil, scene, dialogue, character, song-source, and English records are immutable downstream inputs.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Data mirror.
p = Path('data/works.json'); data = rj(p); work = next(x for x in data if x.get('id') == 'naam'); sd = work.setdefault('structured_derivatives', {})
sd.update({
    'english_translation':'complete-verified', 'english_translation_verified_scenes':45,
    'english_translation_units':797, 'english_dialogue_links_verified':590,
    'english_source_unlabelled_speech_units':20, 'english_performance_records_translated':7,
    'english_song_line_cue_mappings_verified':138, 'english_chant_units_verified':1,
    'english_chant_line_cue_mappings_verified':16, 'english_whole_work_reconciliation':'PASS',
    'english_whole_work_reconciliation_qa_path':'works/naam/translations/whole-work-reconciliation.json',
    'reader_export':'ready-next'
})
work['next_action'] = NEXT
wj(p, data)

# Root/readme project mirrors: append a newest explicit marker and update active English line where present.
p = Path('README.md'); s = rt(p)
s = re.sub(r'- English translation: \*\*45/45 scene layer VERIFIED.*?\*\*\.', '- English translation: **45/45 COMPLETE-VERIFIED — 797 units / 590/590 dialogue links / 7/7 performance records / 138 mappings / 1 chant; whole-work reconciliation PASS; reader/export READY-NEXT**.', s, count=1)
s = re.sub(r'\*\*Next:\*\* Run whole-work English translation reconciliation.*?(?=\n|$)', '**Next:** ' + NEXT, s, count=1)
mark = '<!-- Naam English whole-work closure current -->'
if mark not in s:
    s += f'''\n\n{mark}\n**Naam current:** English translation **COMPLETE-VERIFIED**, whole-work reconciliation **PASS**, **45/45 scenes / 797 units / 590/590 dialogue links / 7/7 performances / 138 mappings / 1 chant (16 mappings)**, reader/export **READY-NEXT**, upstream rewrites **0**. **Next:** {NEXT}\n'''
wt(p,s)

for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'), Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s = rt(p); mark = '<!-- Naam English whole-work closure current -->'
    if mark not in s:
        s += f'''\n\n{mark}\n**Naam English whole-work closure:** **PASS / COMPLETE-VERIFIED** — **45/45 scenes / 797 units / 590/590 dialogue links / 20 source-unlabelled with 0 inferred speakers / 7/7 performances / 138 mappings / 1 chant (16 mappings) / 12 cross-page units**; duplicate source ownership, placeholders, synthetic scene ends and upstream rewrites: **0**. Reader/export **READY-NEXT**. **Next:** {NEXT}\n'''
    wt(p,s)

# Final local post-write upstream check.
up_final = {str(p):digest(p) for p in UPSTREAM_ROOTS}
assert up_final == up_before

print(json.dumps({
    'status':'PASS', 'english':'complete-verified', 'scenes':'45/45', 'units':797,
    'dialogue_links':'590/590', 'source_unlabelled':20, 'performance_records':'7/7',
    'performance_mappings':138, 'chant':'1/16', 'written_text':2, 'cross_page_units':12,
    'duplicate_source_owners':0, 'placeholders':0, 'synthetic_scene_ends':0,
    'upstream_modifications':0, 'next':'Phase 10 reader/export'
}, ensure_ascii=False, indent=2))
