#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 20–24. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9 or PDF 11–19 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain explicit physical-source-damage holds. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
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
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(8,8,10,2)
b=rd('works/naam/transcription/parts/pdf-015-019.md'); a=rd('works/naam/notes/verification-audit-pdf-015-019.md')
for x in ['pdf=15 printed=15 status=verified glyph=verified-final','pdf=19 printed=19 status=verified glyph=verified-final','பரவாயில்லே','அறிவிலிகாள்—பல','மாடிக்கு']:
 assert x in b
assert 'PDF 15–19 PASS / VERIFIED' in a
# Index
d.update(draft_pages=54,verified_pages=13,visual_fidelity_passed_pages=13,historical_glyph_verified_pages=15,review_pages=54,open_uncertainty_markers=2,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-015-019.md': x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for x,y in [('  draft_pages: 59','  draft_pages: 54'),('  verified_pages: 8','  verified_pages: 13'),('  review_pages: 59','  review_pages: 54'),('  pages_verified: 10','  pages_verified: 15'),('  visual_fidelity_audit: in-progress-through-pdf-014-8-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-019-13-of-67-pass'),('  historical_glyph_audit: final-verification-in-progress-10-of-67','  historical_glyph_audit: final-verification-in-progress-15-of-67')]: s=one(s,x,y)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-015-019.md"\n  visual_fidelity_passed_pages: 13\n  historical_glyph_final_verified_pages: 15\n  dual_gate_verified_pages: 13\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "20-24"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
if '  batch_015_019_consequential_decodings:' not in s:
 z='''  batch_015_019_consequential_decodings:\n    - pdf_page: 15\n      source_supported_unicode: "வாறேன்"\n      family: "றா"\n    - pdf_page: 16\n      source_supported_unicode: "காடனை / வேடனை"\n      family: "னை"\n    - pdf_page: 18\n      source_supported_unicode: "தன்னை"\n      family: "னை"\n'''; s=s.replace('  batch_020_024_consequential_decoding:\n',z+'  batch_020_024_consequential_decoding:\n',1)
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S); wr(p,s)
# Glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 15–19 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 15–19 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **8** | **59** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **13** | **54** | **final-verification-in-progress** |')
if '| 15 | 15 | historical `றா` cluster' not in s:
 rows='''| 15 | 15 | historical `றா` cluster | `வாறேன்` | `றா` | enlarged source pixels; occurrence-specific final review | **final-verified** |\n| 16 | 16 | historical `னை` clusters | `காடனை` / `வேடனை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |\n| 18 | 18 | historical `னை` cluster | `தன்னை` | `னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |\n'''; s=s.replace('| 21 | 21 | modern-lookalike',rows+'| 21 | 21 | modern-lookalike',1)
if '## PDF 15–19 final dual-gate audit' not in s: s+='''\n## PDF 15–19 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- no new uncertainty; PDF 5 and PDF 10 remain the only source-damage holds;\n- details: `verification-audit-pdf-015-019.md`.\n\nNext final audit range: **PDF 20–24**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-019-13-of-67',historical_glyph_audit='final-verification-in-progress-15-of-67',canonical_tamil_draft_pages=54,canonical_tamil_verified_pages=13,canonical_tamil_review_pages=54,canonical_tamil_open_uncertainty_markers=2,historical_glyph_pages_verified=15,visual_fidelity_passed_pages=13,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-015-019.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))