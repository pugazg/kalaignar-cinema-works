from pathlib import Path
import json,re

W=Path('works/naam')
NEXT=("Translate and verify source-numbered scenes 2–5 as the first bounded post-pilot English batch. "
      "Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance "
      "to its immutable dialogue ID exactly once; keep source-unlabelled speech unassigned; preserve source order, "
      "page provenance, cross-page units and stage/narrative ownership; and use only the reconciled seven-record "
      "song/performance layer for performance links. Do not alter closed Tamil or structured source layers.")

def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p,s): Path(p).write_text(s,encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p,d): wt(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# metadata.yaml — normalize idempotently, including stale repeated suffixes from the prior reconciliation workflow.
p=W/'metadata.yaml'; s=rt(p)
s=re.sub(r'(?m)^  status: complete-verified-source-only(?:-reconciled)*$', '  status: complete-verified-source-only-reconciled', s, count=1)
s=re.sub(r'(?m)^  retained_records: \d+$', '  retained_records: 7', s, count=1)
s=re.sub(r'(?m)^  source_attributed_authorship_records: \d+$', '  source_attributed_authorship_records: 1', s, count=1)
s=re.sub(r'(?m)^  unresolved_item_level_authorship_records: \d+$', '  unresolved_item_level_authorship_records: 6', s, count=1)
s=re.sub(r'(?m)^  song_performance_index: .+$', '  song_performance_index: complete-verified-source-only-reconciled', s, count=1)
s=re.sub(r'(?m)^  song_performance_record_count: \d+$', '  song_performance_record_count: 7', s, count=1)
s=re.sub(r'(?m)^  song_performance_authorship_resolved: \d+$', '  song_performance_authorship_resolved: 1', s, count=1)
s=re.sub(r'(?m)^  song_performance_authorship_unresolved: \d+$', '  song_performance_authorship_unresolved: 6', s, count=1)
if '  english_translation_index_path:' not in s:
    needle='  song_performance_qa_path: "notes/song-performance-qa.json"\n'
    add=(needle+'  english_translation: pilot-verified\n'
         '  english_translation_index_path: "translations/index.json"\n'
         '  english_translation_verified_scenes: 1\n'
         '  english_translation_unit_count: 21\n'
         '  english_dialogue_links_verified: 14\n'
         '  english_performance_records_translated: 1\n'
         '  english_song_line_cue_mappings_verified: 23\n'
         '  english_pilot_qa_path: "translations/pilot-qa.json"\n')
    s=s.replace(needle,add,1)
else:
    s=re.sub(r'(?m)^  english_translation: .+$','  english_translation: pilot-verified',s,count=1)
    s=re.sub(r'(?m)^  english_translation_verified_scenes: \d+$','  english_translation_verified_scenes: 1',s,count=1)
    s=re.sub(r'(?m)^  english_translation_unit_count: \d+$','  english_translation_unit_count: 21',s,count=1)
    s=re.sub(r'(?m)^  english_dialogue_links_verified: \d+$','  english_dialogue_links_verified: 14',s,count=1)
    s=re.sub(r'(?m)^  english_performance_records_translated: \d+$','  english_performance_records_translated: 1',s,count=1)
    s=re.sub(r'(?m)^  english_song_line_cue_mappings_verified: \d+$','  english_song_line_cue_mappings_verified: 23',s,count=1)
s=re.sub(r'(?m)^  song_authorship_gate: .+$','  song_authorship_gate: complete-verified-source-only-reconciled-7-of-7',s,count=1)
s=re.sub(r'(?m)^  english_translation: ready-next[^\n]*$','  english_translation: pilot-verified-1-of-45',s,count=1)
# The previous replacement may have targeted structured_derivatives; ensure the status-block English field specifically.
status_i=s.find('\nstatus:\n')
if status_i>=0:
    pre=s[:status_i]; tail=s[status_i:]
    tail=re.sub(r'(?m)^  english_translation: .+$','  english_translation: pilot-verified-1-of-45',tail,count=1)
    s=pre+tail
s=re.sub(r'(?m)^next_action:.*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False), s, count=1)
wt(p,s)

# Work README — normalize current status and stale song closure counts.
p=W/'README.md'; s=rt(p)
s=re.sub(r'- song/performance/authorship gate: \*\*.*?\*\*;', '- song/performance/authorship gate: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED / QA PASS; 1 source-attributed + 6 unresolved item-level authorships**;', s, count=1)
s=re.sub(r'- English translation: \*\*.*?\*\*; reader / Reading Room: \*\*not-started\*\*\.', '- English translation: **scene 1/45 PILOT-VERIFIED — 21 units / 14 dialogue links / 1 performance / 23 song mappings**; reader / Reading Room: **not-started**.', s, count=1)
s=s.replace('- mapped source-visible performance structures: **6/6 retained**;', '- mapped source-visible performance structures: **7/7 retained — reconciled**;')
s=s.replace('- clearly bounded Tamil performance derivatives: **6**;', '- clearly bounded Tamil performance derivatives: **7**;')
s=s.replace('- unresolved item-level authorship: **5**;', '- unresolved item-level authorship: **6**;')
s=re.sub(r'\*\*Next:\*\* Begin Phase 9 source-linked English translation[^\n]*', '**Next:** '+NEXT, s)
if '## English translation pilot checkpoint' not in s:
    marker='## Source-visible publication / credit evidence\n'
    block=f'''## English translation pilot checkpoint\n\n- source scene: **1/45 VERIFIED**;\n- translation units: **21**;\n- immutable dialogue links: **14/14 exactly once**;\n- narrative / stage-direction units: **4 / 1**;\n- performance cue / full-song units: **1 / 1**;\n- translated performance occurrence: **`naam-perf-007`**;\n- Tamil→English song role/line mappings: **23/23**;\n- cross-page English units: **1** (`naam-en-s001-u021`, PDF 6–7);\n- inferred source-unlabelled speakers: **0**;\n- authorship upgrades: **0**;\n- upstream source-layer modifications caused by English: **0**.\n\n**Next:** {NEXT}\n\n'''
    s=s.replace(marker,block+marker,1)
wt(p,s)

# Translation index is authoritative for current English checkpoint.
p=W/'translations/index.json'; d=rj(p)
d['status']='pilot-verified'; d['verified_scenes']=1; d['translation_units_verified']=21
d['immutable_dialogue_links_verified']=14; d['retained_performance_records_total']=7
d['retained_performance_records_translated']=1; d['song_line_cue_mappings_verified']=23
d['next_activity']=NEXT; wj(p,d)

# Work next-chat prompt — overwrite active startup state.
wt(W/'NEXT_CHAT_PROMPT.md', f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**. Scenes are **45/45 COMPLETE-VERIFIED**. Dialogue indexing is **590 immutable records / QA PASS**. Character/entity indexing is **28 entities / 45/45 labels / 590/590 records / QA PASS**. Song/performance gating is **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**, with `ஆயிரம் தெய்வங்கள்` → `பாரதியார்` as the only item-level source attribution and six unresolved item-level authorships.\n\nEnglish translation has begun. Source scene 1 is **PILOT-VERIFIED: 21 units, 14/14 immutable dialogue links, 4 narrative units, 1 stage-direction unit, 1 performance-cue unit, 1 full song unit (`naam-perf-007`), 23/23 song role/line mappings, and 1 cross-page unit across PDF 6–7**. No source or structured layer was rewritten.\n\nEnglish index: `works/naam/translations/index.json`; pilot: `works/naam/translations/records/scene-001.json`; review: `works/naam/translations/PILOT_REVIEW.md`; QA: `works/naam/translations/pilot-qa.json`.\n\nDo not alter closed Tamil or structured layers except for later direct source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Project handover — append one durable, unmistakable current checkpoint only once.
p=W/'PROJECT_HANDOVER.md'; s=rt(p)
if '## English pilot closure checkpoint' not in s:
    s += f'''\n\n## English pilot closure checkpoint\n\n- source scene translated/verified: **1/45**;\n- English units: **21**;\n- immutable dialogue links: **14/14**;\n- performance occurrence translated: **`naam-perf-007` / 1 of 7**;\n- song role/line mappings: **23/23**;\n- cross-page English units: **1**;\n- source-unlabelled speaker inference: **0**;\n- authorship upgrades: **0**;\n- upstream source-layer changes caused by translation: **0**.\n\n## Current exact next activity\n\n> **{NEXT}**\n'''
wt(p,s)

# Repository data mirror.
p=Path('data/works.json'); data=rj(p); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({'song_performance_gate':'complete-verified-source-only-reconciled','song_performance_records':7,
           'source_attributed_performance_records':1,'unresolved_item_level_authorship_records':6,
           'english_translation':'pilot-verified','english_translation_verified_scenes':1,
           'english_translation_units':21,'english_dialogue_links_verified':14,
           'english_performance_records_translated':1,'english_song_line_cue_mappings_verified':23,
           'english_translation_index_path':'works/naam/translations/index.json'})
n['next_action']=NEXT; wj(p,data)

# Root README: normalize the active Naam bullet block where possible and append a unique current marker.
p=Path('README.md'); s=rt(p)
s=s.replace('- English remains downstream of scene/dialogue/character/song gates.', '- English translation: **scene 1/45 pilot-verified — 21 units; 14/14 dialogue links; 1/7 performance records translated**.')
s=re.sub(r'\*\*Next:\*\* Begin Phase 9 source-linked English translation[^\n]*', '**Next:** '+NEXT, s)
if '<!-- Naam English pilot current -->' not in s:
    s += f'''\n\n<!-- Naam English pilot current -->\n**Naam current English checkpoint:** source scene **1/45 PILOT-VERIFIED**, **21 units**, **14/14 immutable dialogue links**, **`naam-perf-007` 1/7 performance occurrence translated**, **23/23 song role/line mappings**, and **0 upstream rewrites**. Song/performance gate is **7/7 reconciled**. **Next:** {NEXT}\n'''
wt(p,s)

# Repository handover and consistency audit: append unique current statements; active latest statement is unambiguous.
for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s=rt(p)
    tag='<!-- Naam English pilot current -->'
    if tag not in s:
        s += f'''\n\n{tag}\n**Naam / நாம் current:** English translation **scene 1/45 PILOT-VERIFIED — 21 units / 14 dialogue links / 1 of 7 performance records / 23 song mappings**; song/performance gate **7/7 reconciled**; no source-layer rewrites. **Next:** {NEXT}\n'''
    wt(p,s)

print(json.dumps({'status':'pilot-verified','scene':'1/45','units':21,'dialogue_links':'14/14','performance':'1/7','song_mappings':'23/23','next':NEXT},ensure_ascii=False,indent=2))
