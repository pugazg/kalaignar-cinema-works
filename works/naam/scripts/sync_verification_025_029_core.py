#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 30–34. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–29 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
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
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(17,17,20,3)
b=rd('works/naam/transcription/parts/pdf-025-029.md')
a=rd('works/naam/notes/verification-audit-pdf-025-029.md')
for x in [
 'pdf=25 printed=25 status=verified glyph=verified-final',
 'pdf=29 printed=29 status=verified glyph=verified-final',
 'உங்களை உட்காரச்சொல்லி',
 'கடமைசபதம் எடுத்திருக்கிறேன்',
 'லக்ஷ்மி',
 'ஹல்லோ',
 'ஆரஞ்சுப்பழமும் வைக்கப்படுகிறது'
]: assert x in b, x
assert 'PDF 25–29 PASS / VERIFIED' in a
# Index
d.update(draft_pages=45,verified_pages=22,visual_fidelity_passed_pages=22,historical_glyph_verified_pages=25,review_pages=45,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-025-029.md': x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for x,y in [
 ('  draft_pages: 50','  draft_pages: 45'),
 ('  verified_pages: 17','  verified_pages: 22'),
 ('  review_pages: 50','  review_pages: 45'),
 ('  pages_verified: 20','  pages_verified: 25'),
 ('  visual_fidelity_audit: in-progress-through-pdf-024-17-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-029-22-of-67-pass'),
 ('  historical_glyph_audit: final-verification-in-progress-20-of-67','  historical_glyph_audit: final-verification-in-progress-25-of-67')
]: s=one(s,x,y)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-025-029.md"\n  visual_fidelity_passed_pages: 22\n  historical_glyph_final_verified_pages: 25\n  dual_gate_verified_pages: 22\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "30-34"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S)
wr(p,s)
# Historical glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 25–29 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 25–29 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **17** | **50** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **22** | **45** | **final-verification-in-progress** |')
for old,new in [
 ('| 26 | 26 | old-form `லை` cluster in `அலைந்தான்` | `அலைந்தான்` | `லை` | enlarged source pixels + same-edition family comparison | draft-supported |','| 26 | 26 | old-form `லை` cluster in `அலைந்தான்` | `அலைந்தான்` | `லை` | enlarged source pixels + same-edition family comparison | **final-verified** |'),
 ('| 27 | 27 | historical `ணை` cluster | `சாணைக்கல்லிலே` / `சாணைக்கல்லை` | `ணை` | enlarged source pixels; both same-page occurrences checked | draft-supported |','| 27 | 27 | historical `ணை` cluster | `சாணைக்கல்லிலே` / `சாணைக்கல்லை` | `ணை` | enlarged source pixels; both same-page occurrences checked | **final-verified** |'),
 ('| 28 | 28 | historical `லை` / `னா` shapes in phrase | `காதலை நான்` | `லை` / `னா` | enlarged source pixels + same-edition family comparison | draft-supported |','| 28 | 28 | historical `லை` / `னா` shapes in phrase | `காதலை நான்` | `லை` / `னா` | enlarged source pixels + same-edition family comparison | **final-verified** |'),
 ('| 29 | 29 | historical `ணா` cluster in payment wording | `அணா` | `ணா` | enlarged source pixels; repeated source occurrence | draft-supported |','| 29 | 29 | historical `ணா` cluster in payment wording | `அணா` | `ணா` | enlarged source pixels; repeated source occurrence | **final-verified** |')
]: s=one(s,old,new)
if '| 25 | 25 | historical `ளை` cluster in `உங்களை`' not in s:
 row='| 25 | 25 | historical `ளை` cluster in `உங்களை` | `உங்களை` | `ளை` | enlarged source pixels; direct final review | **final-verified** |\n'
 s=s.replace('| 26 | 26 | old-form `லை` cluster',row+'| 26 | 26 | old-form `லை` cluster',1)
if '## PDF 25–29 final dual-gate audit' not in s:
 s+='''\n## PDF 25–29 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- consequential scan corrections include PDF 25 `உங்களை` / `கடமைசபதம் எடுத்திருக்கிறேன்`, PDF 28 `லக்ஷ்மி`, and PDF 29 `ஹல்லோ` / `ஆரஞ்சுப்பழமும்`;\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-025-029.md`.\n\nNext final audit range: **PDF 30–34**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-029-22-of-67',historical_glyph_audit='final-verification-in-progress-25-of-67',canonical_tamil_draft_pages=45,canonical_tamil_verified_pages=22,canonical_tamil_review_pages=45,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=25,visual_fidelity_passed_pages=22,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-025-029.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))