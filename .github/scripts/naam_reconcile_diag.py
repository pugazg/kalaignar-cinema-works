from pathlib import Path
import json,re
W=Path('works/naam'); T=W/'translations'
PH=re.compile(r'\b(?:TODO|TBD|PLACEHOLDER|FIXME|TRANSLATE(?:\s+ME)?)\b',re.I)
SYN={'scene ends','scene ends.','end of scene','end of scene.','the scene ends','the scene ends.','[scene ends]','[end of scene]'}
def rj(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def eng(u):
 t=u.get('translation',{})
 if isinstance(t.get('english_text'),str): yield t['english_text']
 for x in t.get('english_lines',[]) or []:
  if isinstance(x,str): yield x
 for x in t.get('line_map',[]) or []:
  if isinstance(x,dict) and isinstance(x.get('english'),str): yield x['english']
def pp(u): return [x['pdf_page'] for x in u['source']['page_provenance']]
written=[];owners={};dup=[];ph=[];sy=[]
for n in range(1,46):
 tr=rj(T/'records'/f'scene-{n:03d}.json')
 for u in tr['units']:
  rid=u['source'].get('source_record_id');occ=u['source'].get('source_occurrence_id')
  if u['kind']=='written-text': written.append(u['id'])
  if rid is None and occ is None and u['kind']!='dialogue':
   loc=u['source'].get('source_locator') or {};key=(u['scene_id'],u['kind'],u['source'].get('source_path'),tuple(pp(u)),loc.get('kind'),loc.get('ordinal'),loc.get('description'))
   if key in owners: dup.append({'first':owners[key],'second':u['id'],'key':key})
   else: owners[key]=u['id']
  for x in eng(u):
   if PH.search(x): ph.append({'unit':u['id'],'text':x})
   if x.strip().lower() in SYN: sy.append({'unit':u['id'],'text':x})
print(json.dumps({'written':written,'duplicate_candidates':dup,'placeholder_hits':ph,'synthetic_hits':sy},ensure_ascii=False,indent=2,default=list))
