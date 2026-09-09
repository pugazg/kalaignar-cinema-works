from pathlib import Path
import json,re

NEXT=("Translate and verify source-numbered scenes 2–5 as the first bounded post-pilot English batch. "
      "Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance "
      "to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, "
      "page provenance, cross-page units and stage/narrative ownership; and use only the reconciled seven-record "
      "song/performance layer for performance links. Do not alter closed Tamil or structured source layers.")

def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s): Path(p).write_text(s,encoding='utf-8')

# metadata exact current fields
p=Path('works/naam/metadata.yaml'); s=read(p)
s=re.sub(r'(?m)^  retained_records: \d+$','  retained_records: 7',s,count=1)
s=re.sub(r'(?m)^  unresolved_item_level_authorship_records: \d+$','  unresolved_item_level_authorship_records: 6',s,count=1)
s=re.sub(r'(?m)^  song_performance_record_count: \d+$','  song_performance_record_count: 7',s,count=1)
s=re.sub(r'(?m)^  song_performance_authorship_unresolved: \d+$','  song_performance_authorship_unresolved: 6',s,count=1)
s=re.sub(r'(?m)^  song_authorship_gate: .+$','  song_authorship_gate: complete-verified-source-only-reconciled-7-of-7',s,count=1)
# remove any repeated prior-workflow suffixes
s=s.replace('-reconciled-7-of-7-reconciled-7-of-7','-reconciled-7-of-7')
s=s.replace('-scene-1-pilot-scene-1-pilot','-scene-1-pilot')
write(p,s)

# song index downstream status after pilot
p=Path('works/naam/songs/index.json'); d=json.loads(read(p))
d['english_translation_gate']='open-pilot-verified'
d['next_activity']=NEXT
write(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# work README normalize every active stale 6-count closure phrase
p=Path('works/naam/README.md'); s=read(p)
s=s.replace('**6/6 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS; 1 source-attributed + 5 unresolved item-level authorships**','**7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED / QA PASS; 1 source-attributed + 6 unresolved item-level authorships**')
s=s.replace('**6/6 retained**','**7/7 retained — reconciled**')
s=s.replace('Tamil performance derivatives: **6**','Tamil performance derivatives: **7**')
s=s.replace('item-level authorship: **5**','item-level authorship: **6**')
write(p,s)

# root README — current Naam block only
p=Path('README.md'); s=read(p)
s=s.replace('- song/performance/authorship gate: **6/6 retained source-visible structures / QA PASS / 1 source-attributed + 5 unresolved item-level authorships**;',
            '- song/performance/authorship gate: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED / QA PASS / 1 source-attributed + 6 unresolved item-level authorships**;')
s=s.replace('- English translation: **ready-next**.', '- English translation: **scene 1/45 PILOT-VERIFIED — 21 units / 14 dialogue links / 1 of 7 performance records / 23 song mappings**.')
s=re.sub(r'\*\*Next:\*\* Begin Phase 9 source-linked English translation[^\n]*', '**Next:** '+NEXT, s, count=1)
write(p,s)

# master handover — normalize current Naam high-level and active blocks
p=Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'); s=read(p)
s=s.replace('song/performance gate **6/6 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS (1 source-attributed, 5 unresolved item-level)**; English translation next.',
            'song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED / QA PASS (1 source-attributed, 6 unresolved item-level)**; English translation **scene 1/45 PILOT-VERIFIED / 21 units**.')
s=s.replace('scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; dialogue index **590 records COMPLETE-VERIFIED / QA PASS**; character/entity index next; English remains downstream.',
            'scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; dialogue index **590 records COMPLETE-VERIFIED / QA PASS**; character/entity index **28 entities COMPLETE-VERIFIED / QA PASS**; song/performance **7/7 reconciled**; English **scene 1/45 PILOT-VERIFIED / 21 units**.')
s=re.sub(r'\*\*Exact next activity:\*\* Begin Phase 9 source-linked English translation[^\n]*', '**Exact next activity:** '+NEXT, s, count=1)
write(p,s)

# consistency audit — update headline, matrix and active next phase
p=Path('docs/STATUS_CONSISTENCY_AUDIT.md'); s=read(p)
s=s.replace('Dialogue indexing is the next gate.', 'Naam is now through a verified English scene-1 pilot after all Tamil and structured gates, including the reconciled 7/7 song/performance gate.')
s=s.replace('| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogue records; 28 character/entities; song/performance 6/6 QA PASS** | English translation next | not-started |',
            '| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scenes; 590 dialogue records; 28 entities; song/performance 7/7 reconciled QA PASS** | **scene 1/45 PILOT-VERIFIED; 21 units; 14 dialogue links; 1/7 performances** | not-started |')
s=re.sub(r'\*\*Next production phase:\*\* Begin Phase 9 source-linked English translation[^\n]*', '**Next production phase:** '+NEXT, s, count=1)
write(p,s)

print(json.dumps({'normalized':True,'song_gate':'7/7','english':'scene 1/45 pilot-verified','next':'scenes 2-5'},ensure_ascii=False))
