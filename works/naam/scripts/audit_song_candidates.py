from pathlib import Path
import json,re

SCENES=Path('works/naam/scenes')
rows=[]
for p in sorted(SCENES.glob('scene-*.md')):
    text=p.read_text(encoding='utf-8')
    lines=text.splitlines()
    hits=[]
    for i,line in enumerate(lines,1):
        s=line.strip()
        if not s or s.startswith('<!--'):
            continue
        reasons=[]
        if s.startswith('### '): reasons.append('level3-heading')
        if re.search(r'பாட்டு|பாடல்|பாடிக்|பாடி|கீதம்',s): reasons.append('performance-word')
        if s.startswith('## பின்னணிப் பாடல்'): reasons.append('background-song-heading')
        if reasons:
            hits.append({'line':i,'text':s,'reasons':reasons})
    if hits:
        rows.append({'scene_file':p.name,'hits':hits})

out={
 'work_id':'naam',
 'audit':'song-performance-candidate-recheck-before-english',
 'status':'review-required',
 'scene_files_scanned':45,
 'scenes_with_marker_hits':len(rows),
 'rows':rows,
 'note':'Mechanical candidate scan only. A hit is not automatically a retained performance occurrence; review against verified scene text and the closed inventory.'
}
Path('works/naam/notes/song-candidate-recheck.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md=['# நாம் — song/performance candidate recheck before English','','Status: **REVIEW REQUIRED**','',f'- scene files scanned: **45**',f'- scenes with marker hits: **{len(rows)}**','', 'This is a mechanical marker sweep only; each hit requires source-layer review.','']
for r in rows:
    md.append(f"## {r['scene_file']}")
    md.append('')
    for h in r['hits']:
        md.append(f"- L{h['line']}: `{h['text']}` — {', '.join(h['reasons'])}")
    md.append('')
Path('works/naam/notes/song-candidate-recheck.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps({'scenes_with_hits':len(rows),'hit_count':sum(len(r['hits']) for r in rows)},ensure_ascii=False))
