#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 65–69. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–64 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. PDF 65–69 covers the late scene sequence through the opening portion of காட்சி-45; PDF 69 ends mid-Kumaran utterance that continues on PDF 70. Preserve only the printed source. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
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
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(52,52,55,3)
b=rd('works/naam/transcription/parts/pdf-060-064.md')
a=rd('works/naam/notes/verification-audit-pdf-060-064.md')
for x in [
 'pdf=60 printed=60 status=verified glyph=verified-final',
 'pdf=64 printed=64 status=verified glyph=verified-final',
 'புழுவாகத் துடிக்கின்ற ஏழை', 'புலியாக தருகின்ற இளமை', 'பணத்தோட்டம்',
 'கெடுத்துட்டான்', 'கண்ணீர்த்துளி', 'இதை யெல்லாம்',
 'ஆச்சரியக்குறி தான்!', 'கேள்விக் குறியாக', 'கேள்விக் குறிக்கும்',
 'அறிவாளுக்கும்', 'விளைவிக்காதீர்கள்!', 'அதே குமரனை வெறுக்கின்றனர்'
]: assert x in b, x
assert 'PDF 60–64 PASS / VERIFIED' in a
# Index
d.update(draft_pages=10,verified_pages=57,visual_fidelity_passed_pages=57,historical_glyph_verified_pages=60,review_pages=10,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-060-064.md': x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for x,y in [
 ('  draft_pages: 15','  draft_pages: 10'),
 ('  verified_pages: 52','  verified_pages: 57'),
 ('  review_pages: 15','  review_pages: 10'),
 ('  pages_verified: 55','  pages_verified: 60'),
 ('  visual_fidelity_audit: in-progress-through-pdf-059-52-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-064-57-of-67-pass'),
 ('  historical_glyph_audit: final-verification-in-progress-55-of-67','  historical_glyph_audit: final-verification-in-progress-60-of-67')
]: s=one(s,x,y)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-060-064.md"\n  visual_fidelity_passed_pages: 57\n  historical_glyph_final_verified_pages: 60\n  dual_gate_verified_pages: 57\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "65-69"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
if '  batch_060_064_consequential_decodings:' not in s:
 anchor='  batch_065_069_consequential_decodings:'
 i=s.find(anchor)
 if i<0: raise SystemExit('missing batch 065 metadata anchor')
 block='''  batch_060_064_consequential_decodings:\n    - pdf_page: 60\n      source_supported_unicode: "அண்ணா"\n      family: "ணா"\n    - pdf_page: 61\n      source_supported_unicode: "அண்ணுமலை"\n      family: "லை"\n    - pdf_page: 62\n      source_supported_unicode: "அண்ணுமலை / ஜமீனை"\n      family: "லை / னை"\n    - pdf_page: 64\n      source_supported_unicode: "விளைவிக்காதீர்கள்"\n      family: "ளை"\n    - pdf_page: 64\n      source_supported_unicode: "வாடினான் / குமரனால் / குமரனை"\n      family: "னா / னை"\n\n'''
 s=s[:i]+block+s[i:]
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S)
wr(p,s)
# Historical glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 60–64 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 60–64 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **52** | **15** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **57** | **10** | **final-verification-in-progress** |')
for n in (60,61,62,64):
 pattern=rf'(^\| {n} \|.*?\| )draft-supported( \|$)'
 s=re.sub(pattern,rf'\1**final-verified**\2',s,flags=re.M)
old='| 64 | 64 | historical `னா` cluster | `வாடினான்` | `னா` | enlarged source pixels | **final-verified** |'
extra='''| 64 | 64 | historical `னா` cluster | `வாடினான்` | `னா` | enlarged source pixels | **final-verified** |\n| 64 | 64 | historical `ளை` cluster misread lexically in first pass | `விளைவிக்காதீர்கள்` | `ளை` | enlarged source pixels + cross-page sentence context; source glyph positively resolved | **final-verified** |\n| 64 | 64 | historical `னா / னை` clusters in closing parenthetical | `குமரனால்` / `குமரனை` | `னா / னை` | enlarged source pixels; occurrence-specific final review | **final-verified** |'''
if old in s and 'historical `ளை` cluster misread lexically in first pass' not in s:
 s=s.replace(old,extra,1)
if '## PDF 60–64 final dual-gate audit' not in s:
 s+='''\n## PDF 60–64 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- direct scan corrections include PDF 60 `புழுவாகத்`, `புலியாக தருகின்ற`, `பணத்தோட்டம்`; PDF 61 `கெடுத்துட்டான்`; PDF 62 `கண்ணீர்த்துளி`; PDF 63 `இதை யெல்லாம்`, `ஆச்சரியக்குறி தான்`, `கேள்விக் குறியாக`, `கேள்விக் குறிக்கும்`, `அறிவாளுக்கும்`; and PDF 64 `விளைவிக்காதீர்கள்`, `அதே குமரனை`;\n- final glyph cases include PDF 60 `அண்ணா` (`ணா`), PDF 61–62 `அண்ணுமலை` (`லை`), PDF 62 `ஜமீனை` (`னை`), and PDF 64 `விளைவிக்காதீர்கள்` (`ளை`), `வாடினான்` / `குமரனால்` (`னா`), `குமரனை` (`னை`);\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-060-064.md`.\n\nNext final audit range: **PDF 65–69**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-064-57-of-67',historical_glyph_audit='final-verification-in-progress-60-of-67',canonical_tamil_draft_pages=10,canonical_tamil_verified_pages=57,canonical_tamil_review_pages=10,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=60,visual_fidelity_passed_pages=57,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-060-064.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))
