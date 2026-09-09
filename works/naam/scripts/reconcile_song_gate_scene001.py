from pathlib import Path
import json,re

W=Path('works/naam')
NEXT=("Begin Phase 9 source-linked English translation from the complete-verified Tamil, scene, dialogue, "
      "character/entity and reconciled song/performance layers. Preserve source scene order and exact Tamil speaker "
      "labels as metadata; link labelled dialogue to immutable IDs; keep source-unlabelled speech unassigned; translate "
      "all seven retained performance records from their source-visible Tamil only, carrying `பாரதியார்` attribution only "
      "for `ஆயிரம் தெய்வங்கள்` and leaving the other six item-level authorship states unresolved. Follow "
      "`docs/SONG_TRANSLATION_GUIDE.md`, begin with a scene-1 pilot, run source-link/dialogue/performance coverage QA, and "
      "do not alter closed Tamil or structured source layers.")

def readj(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def writej(p,d): Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p,s): Path(p).write_text(s,encoding='utf-8')

# Inventory: append-only stable ID, but sort by source order for reading.
p=W/'songs/inventory.json'; d=readj(p)
new={
  'id':'naam-perf-007','source_pdf_pages':[6,7],'source_scene_number':1,'form':'explicit-song',
  'source_marker':'(பாட்டு)','source_role_cues':['எல்லோரும்','ஆண்','பெண்','எல்லோரும்'],
  'authorship_status':'unresolved-item-level','author_as_printed':None,
  'record_path':'records/naam-perf-007.md','full_or_clearly_bounded_body':True,
  'late_inventory_reconciliation':'identified by whole-work marker re-audit before English; existing IDs retained'
}
records=[x for x in d['records'] if x['id']!='naam-perf-007']
records.append(new)
records.sort(key=lambda x:(min(x['source_pdf_pages']), x['id']))
d['mapped_source_visible_structures']=7; d['records']=records; d['coverage']='7/7'
d['source_attributed_authorship_records']=1; d['unresolved_item_level_authorship_records']=6
d.setdefault('policy',{})['late_inventory_reconciliation']='scene 1 explicit `(பாட்டு)` added as naam-perf-007 without renumbering existing stable IDs'
writej(p,d)

p=W/'songs/index.json'; d=readj(p)
d.update({'mapped_source_visible_structures':7,'retained_performance_records':7,'full_or_clearly_bounded_tamil_derivatives':7,
          'source_attributed_authorship_records':1,'unresolved_item_level_authorship_records':6,
          'english_translation_gate':'ready','next_activity':NEXT})
d['late_inventory_reconciliation']='scene 1 explicit song added as naam-perf-007; existing IDs 001-006 preserved'
writej(p,d)

p=W/'notes/song-performance-qa.json'; d=readj(p)
d.update({'mapped_structures_expected':7,'retained_records':7,'coverage':'7/7','full_or_clearly_bounded_tamil_derivatives':7,
          'source_attributed_authorship_records':1,'unresolved_item_level_authorship_records':6,'next_gate':'english translation ready'})
d['late_inventory_reconciliation']='PASS — scene 1 `(பாட்டு)` restored as naam-perf-007; 45-scene marker re-audit found no other omitted explicit performance structure requiring a new record'
writej(p,d)

# Work-level metadata.
p=W/'metadata.yaml'; s=rt(p)
s=s.replace('high_confidence_blocks: 6','high_confidence_blocks: 7')
s=s.replace('status: verified-canonical-candidates-awaiting-song-gate','status: complete-verified-source-only-reconciled')
if 'pdf_005_009_performance_structures:' not in s:
    s=s.replace('  high_confidence_blocks: 7\n', '  high_confidence_blocks: 7\n  pdf_005_009_performance_structures: 1\n')
block='''    - pdf_pages: "6-7"\n      scene: 1\n      form: explicit-song\n      source_marker: "(பாட்டு)"\n      source_roles: "எல்லோரும் / ஆண் / பெண் / எல்லோரும்"\n      authorship: not-adjudicated\n      record_id: "naam-perf-007"\n'''
if 'record_id: "naam-perf-007"' not in s:
    s=s.replace('  blocks:\n', '  blocks:\n'+block,1)
s=s.replace('song_authorship_gate: complete-verified-source-only','song_authorship_gate: complete-verified-source-only-reconciled-7-of-7')
s=s.replace('english_translation: ready-next','english_translation: ready-next-scene-1-pilot')
s=re.sub(r'next_action:\s*".*"\s*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False), s, flags=re.M)
wt(p,s)

# Song README fully synchronized.
wt(W/'songs/README.md', f'''# நாம் — song / performance inventory\n\nStatus: **COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**\n\n- source-visible performance records: **7/7**;\n- clearly bounded Tamil performance derivatives: **7/7**;\n- item-level source attribution resolved: **1**;\n- unresolved item-level authorship: **6**;\n- upstream canonical / scene / dialogue / character rewrites: **0**.\n\n## Reconciliation before English\n\nThe whole-work pre-English marker re-audit scanned all **45 scene derivatives** and exposed one omission in the initial six-record inventory: scene 1 contains an explicit `(பாட்டு)` on PDF 6–7 with source role cues `எல்லோரும் / ஆண் / பெண் / எல்லோரும்`. It is now retained as append-only `naam-perf-007`. Existing IDs `naam-perf-001`–`006` were not renumbered.\n\n## Occurrences in source order\n\n- `naam-perf-007` — PDF 6–7 / காட்சி 1 — explicit `(பாட்டு)` with `எல்லோரும் / ஆண் / பெண் / எல்லோரும்` — authorship unresolved at item level.\n- `naam-perf-001` — PDF 16 / காட்சி 7 — explicit `[பாட்டு]` — **ஆயிரம் தெய்வங்கள்** — source-attributed to **பாரதியார்** by the specific PDF 4 item credit.\n- `naam-perf-002` — PDF 18 / காட்சி 8 — lyrical duet, source roles `குமரன் / மீனு / இருவர்` — authorship unresolved at item level.\n- `naam-perf-003` — PDF 35–36 / காட்சி 21 — lyrical block sung by `மீனு` — authorship unresolved at item level.\n- `naam-perf-004` — PDF 49–50 / காட்சி-31 — `மீனு` lyrical block with recurring `(பேசும்)` cue — authorship unresolved at item level.\n- `naam-perf-005` — PDF 59–60 / காட்சி 36→37 relation — source-numbered blocks `7    குமரன், கிராமவாசிகள்` and `8    மாத்திரை` retained together in the established record — authorship unresolved at item level.\n- `naam-perf-006` — PDF 64 / காட்சி 39 — explicit `பின்னணிப் பாடல்` — authorship unresolved at item level.\n\n## Authorship rule\n\nPDF 4's broad `கதை, வசனம், பாடல்... மு. கருணாநிதி` credit is preserved but does not create item-level authorship. The specific `பாட்டு 'ஆயிரம் தெய்வங்கள்'—பாரதியார்.` credit controls only `naam-perf-001`.\n\n## Next\n\n{NEXT}\n''')

# Work README status and next activity.
p=W/'README.md'; s=rt(p)
s=s.replace('song/performance/authorship gate: **COMPLETE-VERIFIED-SOURCE-ONLY: 6/6 retained source-visible structures, 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`) and 5 unresolved item-level authorships, QA PASS**.',
            'song/performance/authorship gate: **COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED: 7/7 retained source-visible records, 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`) and 6 unresolved item-level authorships, QA PASS**.')
s=s.replace('song/performance/authorship gate: **ready-next**;','song/performance/authorship gate: **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**;')
s=s.replace('English translation / reader / Reading Room: **not-started**.','English translation: **ready-next — scene 1 pilot**; reader / Reading Room: **not-started**.')
s=re.sub(r'\*\*Next:\*\* Begin Phase 9 source-linked English translation[^\n]*', '**Next:** '+NEXT, s)
if '## Song/performance reconciliation before English' not in s:
    marker='## Source-visible publication / credit evidence\n'
    add='''## Song/performance reconciliation before English\n\n- initial gate: 6 records;\n- pre-English marker sweep: **45/45 scenes scanned**;\n- omitted explicit performance restored: **காட்சி 1 / PDF 6–7 / `(பாட்டு)` → `naam-perf-007`**;\n- reconciled source-visible performance coverage: **7/7**;\n- authorship: **1 source-attributed / 6 unresolved item-level**;\n- existing `naam-perf-001`–`006` IDs preserved unchanged;\n- upstream Tamil / scene / dialogue / character modifications: **0**.\n\n'''
    s=s.replace(marker,add+marker,1)
wt(p,s)

# Next prompt.
wt(W/'NEXT_CHAT_PROMPT.md', f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**. Scene-text derivatives are **45/45 COMPLETE-VERIFIED**. Immutable dialogue indexing is **590 records / COMPLETE-VERIFIED / QA PASS**. Character/entity indexing is **28 entities / 45/45 labels / 590/590 records / COMPLETE-VERIFIED / QA PASS**. Song/performance/authorship is **COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED: 7/7 retained records, 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`), 6 unresolved item-level authorships, QA PASS**.\n\nImportant reconciliation: the pre-English 45-scene marker sweep caught an omitted scene-1 `(பாட்டு)` on PDF 6–7. It is now append-only `naam-perf-007`; existing IDs `naam-perf-001`–`006` remain stable.\n\nDo not alter closed Tamil or structured layers except for later source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Project handover append durable correction.
p=W/'PROJECT_HANDOVER.md'; s=rt(p)
if 'Song/performance pre-English reconciliation' not in s:
    s += f'''\n\n## Song/performance pre-English reconciliation\n\nA whole-work marker sweep before Phase 9 scanned all 45 scene derivatives and found one omitted explicit source performance: scene 1, PDF 6–7, `(பாட்டு)` with role cues `எல்லோரும் / ஆண் / பெண் / எல்லோரும்`. It is retained as append-only `naam-perf-007`; existing IDs 001–006 remain stable. Reconciled coverage is **7/7**, with **1 source-attributed** item (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`) and **6 unresolved** item-level authorships. No upstream source layer changed.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
wt(p,s)

# Repository data mirror.
p=Path('data/works.json'); data=readj(p); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({'song_performance_gate':'complete-verified-source-only-reconciled','song_performance_records':7,'song_performance_qa':'PASS','source_attributed_performance_records':1,'unresolved_item_level_authorship_records':6,'english_translation':'ready-next-scene-1-pilot'})
n['next_action']=NEXT; writej(p,data)

# Repository-wide active mirrors: append a concise current correction if not already present.
for path in [Path('README.md'),Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s=rt(path)
    if 'Naam song gate reconciled 7/7' not in s:
        s += f'''\n\n<!-- Naam song gate reconciled 7/7 -->\n**Naam current structured checkpoint:** song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED** after the pre-English 45-scene sweep restored scene-1 PDF 6–7 `(பாட்டு)` as append-only `naam-perf-007`; 1 item-level source attribution (`ஆயிரம் தெய்வங்கள்` → `பாரதியார்`), 6 unresolved item-level authorships. **Next:** {NEXT}\n'''
    wt(path,s)

print(json.dumps({'song_records':7,'source_attributed':1,'unresolved_authorship':6,'next':NEXT},ensure_ascii=False,indent=2))
