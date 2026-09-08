#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 45–49. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–44 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
changed=[]
def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
 q=R/p; old=q.read_text(encoding='utf-8') if q.exists() else ''
 if old!=s: q.write_text(s,encoding='utf-8'); changed.append(p)
def one(s,a,b):
 if a not in s: raise SystemExit('missing '+a)
 return s.replace(a,b,1)
# Preconditions
ip='works/naam/transcription/index.json'; d=json.loads(rd(ip))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(32,32,35,3)
b=rd('works/naam/transcription/parts/pdf-040-044.md')
a=rd('works/naam/notes/verification-audit-pdf-040-044.md')
for x in [
 'pdf=40 printed=40 status=verified glyph=verified-final',
 'pdf=44 printed=44 status=verified glyph=verified-final',
 'விதியற்றவனே!', 'வந்த விளைவு!', 'உயிலைகொடுத்தவுடன்',
 'விவாக சுப முகூர்த்தத்துக்கு', 'மண்டூகங்கள்', 'நம்பிக்கை இல்லே!',
 'ஒரு போட்டி ஆஸ்பத்திரி'
]: assert x in b, x
assert 'PDF 40–44 PASS / VERIFIED' in a
# Index
d.update(draft_pages=30,verified_pages=37,visual_fidelity_passed_pages=37,historical_glyph_verified_pages=40,review_pages=30,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-040-044.md': x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for x,y in [
 ('  draft_pages: 35','  draft_pages: 30'),
 ('  verified_pages: 32','  verified_pages: 37'),
 ('  review_pages: 35','  review_pages: 30'),
 ('  pages_verified: 35','  pages_verified: 40'),
 ('  visual_fidelity_audit: in-progress-through-pdf-039-32-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-044-37-of-67-pass'),
 ('  historical_glyph_audit: final-verification-in-progress-35-of-67','  historical_glyph_audit: final-verification-in-progress-40-of-67')
]: s=one(s,x,y)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-040-044.md"\n  visual_fidelity_passed_pages: 37\n  historical_glyph_final_verified_pages: 40\n  dual_gate_verified_pages: 37\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "45-49"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S)
wr(p,s)
# Historical glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 40–44 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 40–44 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **32** | **35** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **37** | **30** | **final-verification-in-progress** |')
for n in (40,42,43):
 pattern=rf'(^\| {n} \|.*?\| )draft-supported( \|$)'
 s,c=re.subn(pattern,rf'\1**final-verified**\2',s,count=1,flags=re.M)
 if c!=1: raise SystemExit(f'missing glyph row {n}')
if '| 44 | 44 | historical `னை` cluster | `உன்னை`' not in s:
 anchor='| 43 | 43 | historical `னை` cluster | `குமரனை`'
 i=s.find(anchor)
 if i<0: raise SystemExit('missing glyph anchor 43')
 e=s.find('\n',i)
 s=s[:e+1]+'| 44 | 44 | historical `னை` cluster | `உன்னை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |\n'+s[e+1:]
if '## PDF 40–44 final dual-gate audit' not in s:
 s+='''\n## PDF 40–44 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- scan corrections include PDF 40 `விதியற்றவனே`, PDF 41 `விளைவு`, PDF 42 `உயிலைகொடுத்தவுடன்` / `விவாக சுப`, PDF 43 `மண்டூகங்கள்`, PDF 44 `இல்லே` / `போட்டி ஆஸ்பத்திரி`;\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-040-044.md`.\n\nNext final audit range: **PDF 45–49**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-044-37-of-67',historical_glyph_audit='final-verification-in-progress-40-of-67',canonical_tamil_draft_pages=30,canonical_tamil_verified_pages=37,canonical_tamil_review_pages=30,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=40,visual_fidelity_passed_pages=37,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-040-044.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))
