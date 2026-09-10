#!/usr/bin/env python3
from pathlib import Path
import json, re

W = Path(__file__).resolve().parents[1]
T = W / 'transcription' / 'pages'
OUT = W / 'notes' / 'song-performance-cue-preflight.json'

terms = [
    'பாட்டு','பாடல்','பாடி','பாடுகிற','பாடிக்','கீதம்','கீத','பின்னணி','இசை',
    'நடனம்','நடன','ஆடுகிற','ஆடிக்','தாலாட்டு','தாலாட்ட','கூத்து','வாத்திய',
    'மேளம்','தம்பட்டம்'
]
rx = re.compile('|'.join(re.escape(x) for x in terms))
rows = []
for path in sorted(T.glob('*.md')):
    m = re.match(r'(\d+)\.md$', path.name)
    if not m:
        continue
    pdf = int(m.group(1))
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if rx.search(line):
            start=max(0,i-3); end=min(len(lines),i+4)
            rows.append({
                'pdf_page': pdf,
                'line_number': i+1,
                'matched_line': line,
                'context': lines[start:end]
            })

payload = {
    'work_id':'vandikkaran-magan',
    'phase':'song-performance-cue-preflight',
    'status':'review-ready',
    'terms':terms,
    'candidate_occurrence_lines':len(rows),
    'candidate_pdf_pages':sorted(set(r['pdf_page'] for r in rows)),
    'candidates':rows,
    'note':'Navigation preflight only. Keyword hits are not automatically song/performance records; source-structure review controls.'
}
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(f"PASS: {len(rows)} cue hits across {len(payload['candidate_pdf_pages'])} PDF pages")
