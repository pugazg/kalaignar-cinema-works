#!/usr/bin/env python3
from pathlib import Path
import json, re

W = Path(__file__).resolve().parents[1]
P = W / 'transcription' / 'pages'
OUT = W / 'notes' / 'dialogue-structural-collision-audit.json'
DIALOGUE_RE = re.compile(r'^(?P<label>[^:#\[\]{}<>\n]{1,60}?)(?P<delimiter>:\s*(?:—|–|-)?)\s*(?P<text>\S.*)$')
NON_SPEAKER_LABELS = {'இடம்','நேரம்','காலம்','பாட்டு','வசனம்','டைரக்ஷன்','கடிதத்தில்'}
rows=[]
for pdf in range(6,88):
    path=P/f'{pdf:03d}.md'
    lines=path.read_text(encoding='utf-8').splitlines()[1:]
    for line_no, raw in enumerate(lines,2):
        s=raw.strip()
        if not s or s.startswith(('#','<!--','★','* * *','---','***','___')):
            continue
        m=DIALOGUE_RE.match(s)
        if not m or m.group('label').strip() in NON_SPEAKER_LABELS:
            continue
        collision = (not s.startswith(('(', '[', '{'))) and s.endswith((')',']','}'))
        if collision:
            rows.append({
                'pdf_page':pdf,
                'printed_page':pdf-1,
                'line_number':line_no,
                'speaker_label':m.group('label').strip(),
                'source_delimiter':m.group('delimiter'),
                'text':m.group('text'),
                'raw':s
            })
payload={
  'work_id':'vandikkaran-magan',
  'phase':'dialogue-structural-collision-audit',
  'status':'review-ready' if rows else 'PASS',
  'collision_count':len(rows),
  'collisions':rows,
  'note':'Explicit speaker-labelled source lines that the legacy structural classifier can skip solely because the complete line ends with a bracket. These require reconciliation before English translation.'
}
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'COLLISIONS={len(rows)}')
