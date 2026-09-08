#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 60–64. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–59 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. PDF 60 continues the numbered booklet performance witness begun on PDF 59 and PDF 64 contains the already mapped பின்னணிப் பாடல் witness; preserve only the printed source. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
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
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(47,47,50,3)
b=rd('works/naam/transcription/parts/pdf-055-059.md')
a=rd('works/naam/notes/verification-audit-pdf-055-059.md')
for x in [
 'pdf=55 printed=55 status=verified glyph=verified-final',
 'pdf=59 printed=59 status=verified glyph=verified-final',
 'கட்டி விடும் கட்டுக் கதைகளுக்கு',
 'நெறி தவறாமல் வாழ்வோம் நாம்—',
 'அறிவாகும் ஏர் முனையிலே...',
 'அண்ணா வாழ்கவே'
]: assert x in b, x
assert 'PDF 55–59 PASS / VERIFIED' in a
# Index
d.update(draft_pages=15,verified_pages=52,visual_fidelity_passed_pages=52,historical_glyph_verified_pages=55,review_pages=15,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-055-059.md': x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for x,y in [
 ('  draft_pages: 20','  draft_pages: 15'),
 ('  verified_pages: 47','  verified_pages: 52'),
 ('  review_pages: 20','  review_pages: 15'),
 ('  pages_verified: 50','  pages_verified: 55'),
 ('  visual_fidelity_audit: in-progress-through-pdf-054-47-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-059-52-of-67-pass'),
 ('  historical_glyph_audit: final-verification-in-progress-50-of-67','  historical_glyph_audit: final-verification-in-progress-55-of-67')
]: s=one(s,x,y)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-055-059.md"\n  visual_fidelity_passed_pages: 52\n  historical_glyph_final_verified_pages: 55\n  dual_gate_verified_pages: 52\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "60-64"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
if '  batch_055_059_consequential_decodings:' not in s:
 anchor='  batch_050_054_consequential_decodings:\n'
 i=s.find(anchor)
 if i<0: raise SystemExit('missing batch 050 metadata anchor')
 # insert immediately before next batch block after the 050 section
 j=s.find('\n  batch_',i+len(anchor))
 if j<0: raise SystemExit('missing next metadata batch anchor')
 block='''\n  batch_055_059_consequential_decodings:\n    - pdf_page: 55\n      source_supported_unicode: "உயிலை"\n      family: "லை"\n    - pdf_page: 57\n      source_supported_unicode: "அண்ணுமலை"\n      family: "லை"\n    - pdf_page: 59\n      source_supported_unicode: "தவறாமல்"\n      family: "றா"\n    - pdf_page: 59\n      source_supported_unicode: "முனையிலே"\n      family: "னை"\n    - pdf_page: 59\n      source_supported_unicode: "அண்ணா"\n      family: "ணா"\n'''
 s=s[:j]+block+s[j:]
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S)
wr(p,s)
# Historical glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 55–59 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 55–59 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **47** | **20** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **52** | **15** | **final-verification-in-progress** |')
# Finalize all occurrence rows for this batch; also repair two already-verified rows left stale by earlier single-row updates.
for n in (49,52,55,57,59):
 pattern=rf'(^\| {n} \|.*?\| )draft-supported( \|$)'
 s=re.sub(pattern,rf'\1**final-verified**\2',s,flags=re.M)
if '## PDF 55–59 final dual-gate audit' not in s:
 s+='''\n## PDF 55–59 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- direct scan reconciliation requires one local word-boundary correction on PDF 57: `கட்டுக்கதைகளுக்கு` → `கட்டுக் கதைகளுக்கு`;\n- final glyph cases include PDF 55 `உயிலை` (`லை`), PDF 57 `அண்ணுமலை` (`லை`), PDF 59 `தவறாமல்` (`றா`), `முனையிலே` (`னை`) and `அண்ணா` (`ணா`);\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- two stale per-occurrence statuses from already-verified PDF 49 / PDF 52 are normalized to final-verified during this synchronization;\n- details: `verification-audit-pdf-055-059.md`.\n\nNext final audit range: **PDF 60–64**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-059-52-of-67',historical_glyph_audit='final-verification-in-progress-55-of-67',canonical_tamil_draft_pages=15,canonical_tamil_verified_pages=52,canonical_tamil_review_pages=15,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=55,visual_fidelity_passed_pages=52,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-055-059.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))
