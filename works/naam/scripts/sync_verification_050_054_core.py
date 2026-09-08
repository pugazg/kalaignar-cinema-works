#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 55–59. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–54 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. PDF 59 reaches the already mapped poetic/song-like booklet witness between scenes 36 and 37; preserve only the printed source. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
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
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(42,42,45,3)
b=rd('works/naam/transcription/parts/pdf-050-054.md')
a=rd('works/naam/notes/verification-audit-pdf-050-054.md')
for x in [
 'pdf=50 printed=50 status=verified glyph=verified-final',
 'pdf=54 printed=54 status=verified glyph=verified-final',
 'காதல்...        (பேசும்)', 'நேசம்....        (பேசும்)',
 'எஜமான் நமஸ்காரம்', 'மலைய :- சாம்பலாகவில்லையா?',
 'மலையங்களா தான் சரியான இடம்', 'கவலையே இல்லே.',
 'விறுவிறுத்துப்போச்சி', 'வாற வழியிலே', 'வீட்டுக் கதவை',
 'சங்காரமூர்த்தி!', 'காப்பாற்றுவதையே', 'பிறக்கும்குழந்தை',
 '(மீனு உயில் வைத்தியரிடம் கொடுக்கிறாள்)', 'பத்திரமாகவைச்சிரு!'
]: assert x in b, x
assert 'PDF 50–54 PASS / VERIFIED' in a
# Index
d.update(draft_pages=20,verified_pages=47,visual_fidelity_passed_pages=47,historical_glyph_verified_pages=50,review_pages=20,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-050-054.md': x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for x,y in [
 ('  draft_pages: 25','  draft_pages: 20'),
 ('  verified_pages: 42','  verified_pages: 47'),
 ('  review_pages: 25','  review_pages: 20'),
 ('  pages_verified: 45','  pages_verified: 50'),
 ('  visual_fidelity_audit: in-progress-through-pdf-049-42-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-054-47-of-67-pass'),
 ('  historical_glyph_audit: final-verification-in-progress-45-of-67','  historical_glyph_audit: final-verification-in-progress-50-of-67'),
 ('      source_cue: "(பேதம்)"','      source_cue: "(பேசும்)"')
]: s=one(s,x,y)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-050-054.md"\n  visual_fidelity_passed_pages: 47\n  historical_glyph_final_verified_pages: 50\n  dual_gate_verified_pages: 47\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "55-59"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S)
wr(p,s)
# Correct stale first-pass notes where they made explicit source claims later disproved by verification
p='works/naam/notes/textual-notes-pdf-050-054.md'; s=rd(p)
s=s.replace('Preserve the printed `(பேதம்)` cues','Preserve the verified printed `(பேசும்)` cues')
s=s.replace('Source wording `இந்த மூட்டாள் பயல் சிநேகிதன்—சங்கரமூர்த்தி!` is retained from enlarged direct reading.','Final verification corrects the source wording to `இந்த மூட்டாள் பயல் சிநேகிதன்—சங்காரமூர்த்தி!`; enlarged direct pixels control.')
wr(p,s)
# Historical glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 50–54 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 50–54 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **42** | **25** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **47** | **20** | **final-verification-in-progress** |')
for n in (51,52,53,54):
 pattern=rf'(^\| {n} \|.*?\| )draft-supported( \|$)'
 s,c=re.subn(pattern,rf'\1**final-verified**\2',s,count=1,flags=re.M)
 if c!=1: raise SystemExit(f'missing glyph row {n}')
if '| 53 | 53 | historical `றா` cluster | `வாற`' not in s:
 anchor='| 53 | 53 | historical `லை` name ending | `அண்ணுமலை`'
 i=s.find(anchor)
 if i<0: raise SystemExit('missing glyph anchor 53')
 e=s.find('\n',i)
 s=s[:e+1]+'| 53 | 53 | historical `றா` cluster | `வாற` | `றா` | enlarged source pixels; occurrence-specific final review | **final-verified** |\n'+s[e+1:]
if '## PDF 50–54 final dual-gate audit' not in s:
 s+='''\n## PDF 50–54 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- scan corrections include PDF 50 `(பேசும்)` refrain cues, PDF 51 `எஜமான்` / source role `மலைய`, PDF 52 `மலையங்களா தான்` / `கவலையே இல்லே`, PDF 53 `விறுவிறுத்துப்போச்சி` / `வாற` / `வீட்டுக் கதவை` / `சங்காரமூர்த்தி`, and PDF 54 `காப்பாற்றுவதையே` / `பிறக்கும்குழந்தை` / stage-direction `உயில்` / `பத்திரமாகவைச்சிரு`;\n- final glyph cases include `என்னை` (`னை`), `மலையங்களா` / `அண்ணுமலை` (`லை`) and `வாற` (`றா`);\n- scene-31 metadata cue synchronized from stale `(பேதம்)` to verified `(பேசும்)`;\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-050-054.md`.\n\nNext final audit range: **PDF 55–59**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-054-47-of-67',historical_glyph_audit='final-verification-in-progress-50-of-67',canonical_tamil_draft_pages=20,canonical_tamil_verified_pages=47,canonical_tamil_review_pages=20,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=50,visual_fidelity_passed_pages=47,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-050-054.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))
