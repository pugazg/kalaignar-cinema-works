#!/usr/bin/env python3
import json,re
from pathlib import Path

R=Path(__file__).resolve().parents[3]
NEXT='Perform a targeted source-obscuration hold-resolution audit for PDF 5, PDF 10 and PDF 24 using only the controlling scan at enlarged/native resolution. Do not reconstruct missing or obscured text from grammar, OCR, film audio, subtitles, another edition, web text or memory. Re-evaluate each hold separately; if the controlling pixels still do not expose the characters, retain the hold and document the unreadable span explicitly. Do not start structured derivatives or English until the canonical Tamil gate is fully verified or a deliberate documented hold-policy decision is made.'
changed=[]

def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
    q=R/p
    old=q.read_text(encoding='utf-8') if q.exists() else ''
    if old!=s:
        q.parent.mkdir(parents=True,exist_ok=True)
        q.write_text(s,encoding='utf-8')
        changed.append(p)

def rep(s,a,b):
    if a in s:
        return s.replace(a,b,1)
    return s

def between(s,a,b,r):
    i=s.find(a); j=s.find(b,i+len(a)) if i>=0 else -1
    if i<0 or j<0:
        raise SystemExit('missing section: '+a)
    return s[:i]+r.rstrip()+'\n\n'+s[j:]

ip='works/naam/transcription/index.json'
d=json.loads(rd(ip))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(62,62,65,3)
part='works/naam/transcription/parts/pdf-070-071.md'
ps=rd(part)
for x in [
    'Status: `verified`',
    'Historical-glyph final: `verified-final`',
    'pdf=70 printed=70 status=verified glyph=verified-final',
    'pdf=71 printed=71 status=verified glyph=verified-final',
    'உயிர் ... உயிர் ... உரிமைச் சாசனத்தை',
    'இன்று, அதே போலீஸ்காரர்கள்',
    'அப்படி என்னகெடுதி செய்து விட்டேன் நான் உங்களுக்கு?',
    'என் சொத்துக்கள் மக்களுக்கு சொந்த',
    '“ உலகைத்திருத்தும் உத்தமர்களுக் கெல்லாம் இது தான் முடிவா?”'
]:
    assert x in ps, x
audit=rd('works/naam/notes/verification-audit-pdf-070-071.md')
assert 'PDF 70–71 PASS / VERIFIED' in audit

d.update(draft_pages=3,verified_pages=64,visual_fidelity_passed_pages=64,historical_glyph_verified_pages=67,review_pages=3,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
    if x['path']=='parts/pdf-070-071.md':
        x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

p='works/naam/metadata.yaml'; s=rd(p)
for a,b in [
    ('  draft_pages: 5','  draft_pages: 3'),
    ('  verified_pages: 62','  verified_pages: 64'),
    ('  review_pages: 5','  review_pages: 3'),
    ('  pages_verified: 65','  pages_verified: 67'),
    ('  visual_fidelity_audit: in-progress-through-pdf-069-62-of-67-pass','  visual_fidelity_audit: in-progress-with-source-holds-64-of-67-pass'),
    ('  historical_glyph_audit: final-verification-in-progress-65-of-67','  historical_glyph_audit: complete-final-verified-67-of-67'),
    ('  status: final-verification-in-progress','  status: complete-final-verified'),
]: s=rep(s,a,b)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-070-071.md"\n  visual_fidelity_passed_pages: 64\n  historical_glyph_final_verified_pages: 67\n  dual_gate_verified_pages: 64\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "5,10,24"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
s=re.sub(r'next_action: ".*?"\s*$',lambda m:'next_action: "'+NEXT.replace('"','\\"')+'"',s,count=1,flags=re.S)
wr(p,s)

p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=rep(s,'| PDF 70–71 | 2 | 2 | 0 | 2 | first-pass-complete |','| PDF 70–71 | 2 | 2 | 2 | 0 | final-audit: 2 verified |')
s=rep(s,'| **Total** | **67** | **67** | **62** | **5** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **64** | **3** | **historical-glyph-final-complete / visual-holds-remain** |')
for n in (70,71):
    s=re.sub(rf'(^\| {n} \|.*?\| )draft-supported( \|$)',rf'\1**final-verified**\2',s,flags=re.M)
if '## PDF 70–71 final dual-gate audit' not in s:
    s+='''\n\n## PDF 70–71 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **2/2 PASS / 2/2 PASS**;\n- dual-gate canonical: **2/2 VERIFIED**;\n- PDF 70 scan corrections: `உயிர்...உயிர்...` → `உயிர் ... உயிர் ...`; `இன்று அதே` → `இன்று, அதே`; `என்ன கெடுதி` → `என்னகெடுதி`; `என் சொத்துக்களை` → `என் சொத்துக்கள்`;\n- PDF 71 preserves the printed opening-space after the quotation mark in `“ உலகைத்திருத்தும் ...` and the closing `நாம்`;\n- final glyph cases: PDF 70 `சிறைச்சாலை` / `மலையப்பன்` (`லை`), `குமரனால்` (`னா`), `என்னை` (`னை`), `வருகிறாள்` (`றா`); PDF 71 `உங்களை` (`ளை`);\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-070-071.md`.\n\nHistorical-glyph final verification is now **67/67 COMPLETE**. The canonical dual gate remains **64/67** only because the three visual/source-obscuration holds remain.\n\nNext activity: targeted hold-resolution audit for **PDF 5, PDF 10 and PDF 24**.\n'''
wr(p,s)

p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-with-source-holds-64-of-67',historical_glyph_audit='complete-final-verified-67-of-67',canonical_tamil_draft_pages=3,canonical_tamil_verified_pages=64,canonical_tamil_review_pages=3,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=67,visual_fidelity_passed_pages=64,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-070-071.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')

p='works/naam/README.md'; s=rd(p)
for a,b in [
    ('canonical Tamil verified pages: **62/67**','canonical Tamil verified pages: **64/67**'),
    ('visual fidelity audit: **in progress — 62/67 pages passed**','visual fidelity audit: **in progress — 64/67 pages passed; 3 source holds remain**'),
    ('historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 65/67 final-verified**','historical-Tamil-glyph audit: **final verification complete — 67/67 final-verified**'),
    ('dual-gate verification pass is in progress: **62/67** pages are now verified;','dual-gate verification pass is in progress: **64/67** pages are now verified;'),
    ('**62/67** canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–69.','**64/67** canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–71.'),
]: s=rep(s,a,b)
sec='''## Verification audit — through PDF 71\n\n- PDF 6–9, PDF 11–23 and PDF 25–71: **dual-gate VERIFIED — 64/67 total**;\n- PDF 5 / PDF 10: **HOLD** for physical source loss; PDF 24: **HOLD** for later ink/mark obscuring the post-`தே` printed glyph;\n- visual-fidelity passed: **64/67**; historical-glyph final verified: **67/67 COMPLETE**;\n- open source uncertainties: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 70–71: **2/2 VERIFIED**, no new uncertainty;\n- direct PDF 70 corrections: `உயிர்...உயிர்...` → `உயிர் ... உயிர் ...`; `இன்று அதே` → `இன்று, அதே`; `என்ன கெடுதி` → `என்னகெடுதி`; `என் சொத்துக்களை` → `என் சொத்துக்கள்`;\n- PDF 71 preserves the source quotation spacing and final `நாம்`;\n- detailed audit: `notes/verification-audit-pdf-070-071.md`.\n\n**Next:** targeted hold-resolution for PDF 5, PDF 10 and PDF 24.\n'''
s=between(s,'## Verification audit — through PDF 69','## Song / verse / performance structures mapped or confirmed so far',sec)
s=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S)
wr(p,s)

p='works/naam/transcription/README.md'; s=rd(p)
for a,b in [
    ('- verified pages: **62**;','- verified pages: **64**;'),
    ('- separate visual-fidelity audit: **in progress — 62/67 passed**;','- separate visual-fidelity audit: **in progress — 64/67 passed; 3 source holds remain**;'),
    ('- historical-glyph final verified pages: **65/67**;','- historical-glyph final verified pages: **67/67 — COMPLETE**;'),
]: s=rep(s,a,b)
if '## Verification audit — PDF 70–71' not in s:
    marker='## Next activity'
    block='''## Verification audit — PDF 70–71\n\nPDF 70–71 are **2/2 VERIFIED** after direct source comparison. PDF 70 corrections: `உயிர்...உயிர்...` → `உயிர் ... உயிர் ...`; `இன்று அதே` → `இன்று, அதே`; `என்ன கெடுதி` → `என்னகெடுதி`; `என் சொத்துக்களை` → `என் சொத்துக்கள்`. PDF 71 preserves the source-visible opening quote spacing and closes with final `நாம்`. Current totals: visual **64/67**, glyph-final **67/67 COMPLETE**, dual-gate verified **64/67**, open uncertainties **3**. Detailed log: `../notes/verification-audit-pdf-070-071.md`.\n\n'''
    if marker in s: s=s.replace(marker,block+marker,1)
s=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S)
wr(p,s)

p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
for a,b in [
    ('canonical Tamil verified: **62/67**','canonical Tamil verified: **64/67**'),
    ('visual fidelity audit: **in progress — 62/67 passed**','visual fidelity audit: **in progress — 64/67 passed; 3 source holds remain**'),
    ('historical-glyph final verified: **65/67**','historical-glyph final verified: **67/67 COMPLETE**'),
]: s=rep(s,a,b)
if '- `notes/verification-audit-pdf-070-071.md`.' not in s:
    anchor='- `notes/verification-audit-pdf-065-069.md`.'
    if anchor in s: s=s.replace(anchor,anchor+'\n- `notes/verification-audit-pdf-070-071.md`.',1)
sec=f'''## Verification checkpoint through PDF 71\n\n- PDF 6–9, PDF 11–23 and PDF 25–71: **VERIFIED — 64/67 total**;\n- PDF 5 / PDF 10 remain physical-source-damage holds; PDF 24 remains a later-ink/mark source-obscuration hold;\n- visual-fidelity: **64/67**; glyph-final: **67/67 COMPLETE**; dual-gate: **64/67**;\n- open source uncertainties: **3**;\n- PDF 70–71 is fully verified and adds no uncertainty.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
i=s.find('## Verification checkpoint through PDF 69')
if i>=0: s=s[:i]+sec
wr(p,s)

wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCurrent durable checkpoint: first pass **67/67 COMPLETE**; visual-fidelity **64/67**; historical-glyph final **67/67 COMPLETE**; dual-gate verified **64/67** (PDF 6–9, PDF 11–23, PDF 25–71); open source holds **3** — PDF 5, PDF 10, PDF 24. PDF 9 is resolved as `குறுக்கொடிய`. PDF 24 scene 11 remains directly readable only through visible `கெளரவம் தே… இருப்பது`; do not restore `தேடி` without new direct-source evidence. Structured derivatives and English remain blocked.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\nLatest normal-range audit: `works/naam/notes/verification-audit-pdf-070-071.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

p='README.md'; s=rd(p)
sec=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake/map and first-pass Tamil are complete; normal-range dual-gate verification is complete except for three explicit source-obscuration holds.\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **64/67 / 64/67**;\n- historical-glyph first-pass / final: **67/67 / 67/67 COMPLETE**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-070-071.md`;\n- derivatives / English remain blocked pending canonical hold resolution.\n\n**Next:** {NEXT}\n'''
s=between(s,'## நாம் status','## ராஜா ராணி status',sec)
wr(p,s)

p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=re.sub(r'- \*\*Naam / நாம்\*\* — active work;.*','- **Naam / நாம்** — active work; first pass **67/67 COMPLETE**; dual-gate **64/67**; visual **64/67**; glyph-final **67/67 COMPLETE**; source holds PDF 5 / PDF 10 / PDF 24; downstream blocked.',s,count=1)
sec=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **64/67 / 64/67**;\n- historical-glyph first-pass / final: **67/67 / 67/67 COMPLETE**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-070-071.md`;\n- structured derivatives / English / reader remain blocked.\n\n**Exact next activity:** {NEXT}\n'''
s=between(s,'## 8. Naam active checkpoint','## 9. Ammayappan closed checkpoint',sec)
wr(p,s)

p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
r='**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** has first pass **67/67 COMPLETE**, dual-gate verification **64/67**, visual-fidelity **64/67**, historical-glyph final **67/67 COMPLETE**, and **3 source-obscuration holds** (PDF 5, PDF 10, PDF 24). PDF 70–71 is fully verified and adds no uncertainty.'
s=re.sub(r'\*\*PASS for the current repository-wide checkpoint\.\*\*.*?\n\n',r+'\n\n',s,count=1,flags=re.S)
s=re.sub(r'\| Naam / நாம் \|.*','| Naam / நாம் | first pass 67/67 COMPLETE; dual-gate 64/67; 3 source holds | 45 scenes mapped; derivatives blocked | not-started | not-started |',s,count=1)
sec=f'''## Naam current checkpoint\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **64/67 / 64/67**;\n- historical-glyph first-pass / final: **67/67 / 67/67 COMPLETE**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 70–71: **2/2 VERIFIED**;\n- current audit: `works/naam/notes/verification-audit-pdf-070-071.md`;\n- downstream layers remain blocked.\n\n**Next production phase:** {NEXT}\n'''
s=between(s,'## Naam current checkpoint','## Ammayappan current checkpoint',sec)
i=s.find('## Conclusion')
if i>=0: s=s[:i]+'''## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is active with first pass **67/67 COMPLETE**, dual-gate **64/67**, visual **64/67**, glyph-final **67/67 COMPLETE**, and source holds on PDF 5, PDF 10 and PDF 24. Next activity: targeted hold resolution for those three pages.\n'''
wr(p,s)

print('\n'.join(changed))
