#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

R=Path(__file__).resolve().parents[3]
NEXT=("Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 35–39. "
      "Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, "
      "PDF 11–23, PDF 25–34 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds "
      "and PDF 24 remains an ink/mark-overprint hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete.")
changed=[]

def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
    q=R/p; old=q.read_text(encoding='utf-8') if q.exists() else ''
    if old!=s:
        q.write_text(s,encoding='utf-8'); changed.append(p)
def sub1(s,pat,repl,flags=0):
    out,n=re.subn(pat,repl,s,count=1,flags=flags)
    if n!=1: raise SystemExit('missing regex: '+pat)
    return out

def between(s,a,b,r):
    i=s.find(a); j=s.find(b,i+len(a)) if i>=0 else -1
    if i<0 or j<0: raise SystemExit('missing section '+a)
    return s[:i]+r.rstrip()+'\n\n'+s[j:]

# Preconditions and canonical authority
ip='works/naam/transcription/index.json'; d=json.loads(rd(ip))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(22,22,25,3)
b=rd('works/naam/transcription/parts/pdf-030-034.md')
a=rd('works/naam/notes/verification-audit-pdf-030-034.md')
for x in ['pdf=30 printed=30 status=verified glyph=verified-final','pdf=34 printed=34 status=verified glyph=verified-final','ஜனங்கள் டிக்கட் இல்லாமே பார்த்துட்டுப் போயிடு வாங்க','இருப்பவனை காப்பாற்றும்','ஜரிகைத் தொப்பி','இன்பலோகத்தை','இதற்கெல்லாம்']:
    assert x in b, x
assert 'PDF 30–34 PASS / VERIFIED' in a

# Index
d.update(draft_pages=40,verified_pages=27,visual_fidelity_passed_pages=27,historical_glyph_verified_pages=30,review_pages=40,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
    if x['path']=='parts/pdf-030-034.md':
        x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
s=sub1(s,r'  draft_pages: 45\b','  draft_pages: 40')
s=sub1(s,r'  verified_pages: 22\b','  verified_pages: 27')
s=sub1(s,r'  review_pages: 45\b','  review_pages: 40')
s=sub1(s,r'  pages_verified: 25\b','  pages_verified: 30')
s=sub1(s,r'  visual_fidelity_audit: in-progress-through-pdf-029-22-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-034-27-of-67-pass')
s=sub1(s,r'  historical_glyph_audit: final-verification-in-progress-25-of-67','  historical_glyph_audit: final-verification-in-progress-30-of-67')
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-030-034.md"\n  visual_fidelity_passed_pages: 27\n  historical_glyph_final_verified_pages: 30\n  dual_gate_verified_pages: 27\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "35-39"\n'''
s=sub1(s,r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',flags=re.S)
s=sub1(s,r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',flags=re.S)
wr(p,s)

# Historical-glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=sub1(s,r'\| PDF 30–34 \| 5 \| 5 \| 0 \| 5 \| partial-first-pass \|','| PDF 30–34 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=sub1(s,r'\| \*\*Total\*\* \| \*\*67\*\* \| \*\*67\*\* \| \*\*22\*\* \| \*\*45\*\* \| \*\*final-verification-in-progress\*\* \|','| **Total** | **67** | **67** | **27** | **40** | **final-verification-in-progress** |')
for src in [
'| 31 | 31 | historical `றா` cluster | `தவறான` | `றா` | enlarged source pixels | draft-supported |',
'| 31 | 31 | historical `னை` cluster | `இவனை` | `னை` | enlarged source pixels | draft-supported |',
'| 32 | 32 | historical `னை` clusters | `அவனை` / `ஜமீனையே` | `னை` | enlarged source pixels | draft-supported |',
'| 34 | 34 | historical `ளை` cluster | `அவளை` | `ளை` | enlarged source pixels | draft-supported |',
'| 34 | 34 | historical `ணை` cluster | `பஞ்சணை` | `ணை` | enlarged source pixels | draft-supported |']:
    assert src in s, src
    s=s.replace(src,src.replace('draft-supported','**final-verified**'),1)
if '## PDF 30–34 final dual-gate audit' not in s:
    s+='''\n## PDF 30–34 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- consequential scan corrections: PDF 30 `ஜனங்கள்` / `இல்லாமே` / `போயிடு வாங்க`; PDF 32 `இருப்பவனை`; PDF 33 `ஜரிகைத்` / `இன்பலோகத்தை`; PDF 34 `இதற்கெல்லாம்`;\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-030-034.md`.\n\nNext final audit range: **PDF 35–39**.\n'''
wr(p,s)

# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-034-27-of-67',historical_glyph_audit='final-verification-in-progress-30-of-67',canonical_tamil_draft_pages=40,canonical_tamil_verified_pages=27,canonical_tamil_review_pages=40,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=30,visual_fidelity_passed_pages=27,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-030-034.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')

# Work README
p='works/naam/README.md'; s=rd(p)
s=sub1(s,r'canonical Tamil verified pages: \*\*22/67\*\*','canonical Tamil verified pages: **27/67**')
s=sub1(s,r'visual fidelity audit: \*\*in progress — 22/67 pages passed\*\*','visual fidelity audit: **in progress — 27/67 pages passed**')
s=sub1(s,r'historical-Tamil-glyph audit: \*\*first pass complete — 67/67 checked / 25/67 final-verified\*\*','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 30/67 final-verified**')
s=sub1(s,r'dual-gate verification pass is in progress: \*\*22/67\*\* pages are now verified;','dual-gate verification pass is in progress: **27/67** pages are now verified;')
s=sub1(s,r'\*\*22/67\*\* canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–29\.','**27/67** canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–34.')
sec='''## Verification audit — through PDF 34\n\n- PDF 6–9, PDF 11–23 and PDF 25–34: **dual-gate VERIFIED — 27/67 total**;\n- PDF 5 / PDF 10: **HOLD** for physical source loss; PDF 24: **HOLD** for later ink/mark obscuring the post-`தே` printed glyph;\n- visual-fidelity passed: **27/67**; historical-glyph final verified: **30/67**;\n- open source uncertainties: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 30–34: **5/5 VERIFIED**, no new uncertainty;\n- detailed audit: `notes/verification-audit-pdf-030-034.md`.\n\n**Next verification range:** PDF 35–39.\n'''
s=between(s,'## Verification audit — through PDF 29','## Song / verse / performance structures mapped or confirmed so far',sec)
s=sub1(s,r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',flags=re.S)
wr(p,s)

# Transcription README
p='works/naam/transcription/README.md'; s=rd(p)
s=sub1(s,r'- verified pages: \*\*22\*\*;','- verified pages: **27**;')
s=sub1(s,r'- separate visual-fidelity audit: \*\*in progress — 22/67 passed\*\*;','- separate visual-fidelity audit: **in progress — 27/67 passed**;')
s=sub1(s,r'- historical-glyph final verified pages: \*\*25/67\*\*;','- historical-glyph final verified pages: **30/67**;')
if '## Verification audit — PDF 30–34' not in s:
    marker='## PDF 35–39 source decisions'
    if marker not in s: raise SystemExit('missing transcription marker')
    block='''## Verification audit — PDF 30–34\n\nPDF 30–34 are **5/5 VERIFIED** after direct scan comparison. Consequential corrections: PDF 30 `ஜனங்கள்`, `இல்லாமே`, `போயிடு வாங்க`; PDF 32 `இருப்பவனை`; PDF 33 `ஜரிகைத்`, `இன்பலோகத்தை`; PDF 34 `இதற்கெல்லாம்`. Current totals: visual **27/67**, glyph-final **30/67**, dual-gate verified **27/67**, open uncertainties **3**. Detailed log: `../notes/verification-audit-pdf-030-034.md`.\n\n'''
    s=s.replace(marker,block+marker,1)
s=sub1(s,r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',flags=re.S)
wr(p,s)

# Work handover
p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
s=sub1(s,r'canonical Tamil verified: \*\*22/67\*\*','canonical Tamil verified: **27/67**')
s=sub1(s,r'visual fidelity audit: \*\*in progress — 22/67 passed\*\*','visual fidelity audit: **in progress — 27/67 passed**')
s=sub1(s,r'historical-glyph final verified: \*\*25/67\*\*','historical-glyph final verified: **30/67**')
if '- `notes/verification-audit-pdf-030-034.md`.' not in s:
    s=s.replace('- `notes/verification-audit-pdf-025-029.md`.','- `notes/verification-audit-pdf-025-029.md`.\n- `notes/verification-audit-pdf-030-034.md`.',1)
i=s.find('## Verification checkpoint through PDF 29')
if i<0: raise SystemExit('missing project checkpoint')
s=s[:i]+f'''## Verification checkpoint through PDF 34\n\n- PDF 6–9, PDF 11–23 and PDF 25–34: **VERIFIED — 27/67 total**;\n- PDF 5 / PDF 10 remain physical-source-damage holds; PDF 24 remains a later-ink/mark source-obscuration hold;\n- visual-fidelity: **27/67**; glyph-final: **30/67**; dual-gate: **27/67**;\n- open source uncertainties: **3**;\n- PDF 30–34 is fully verified and adds no uncertainty.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
wr(p,s)

# Next-chat prompt
wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCurrent durable checkpoint: first pass **67/67 COMPLETE**; visual-fidelity **27/67**; historical-glyph final **30/67**; dual-gate verified **27/67** (PDF 6–9, PDF 11–23, PDF 25–34); open source holds **3** — PDF 5, PDF 10, PDF 24. PDF 9 is resolved as `குறுக்கொடிய`. PDF 24 scene 11 remains directly readable only through visible `கெளரவம் தே… இருப்பது`; do not restore `தேடி` without new direct-source evidence. Structured derivatives and English remain blocked.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\nDetailed current audit: `works/naam/notes/verification-audit-pdf-030-034.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Root README section
p='README.md'; s=rd(p)
sec=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake/map and first-pass Tamil are complete; dual-gate verification is in progress.\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **27/67 / 27/67**;\n- historical-glyph first-pass / final: **67/67 / 30/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-030-034.md`;\n- derivatives / English remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''
s=between(s,'## நாம் status','## ராஜா ராணி status',sec); wr(p,s)

# Master handover
p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=sub1(s,r'- \*\*Naam / நாம்\*\* — active work;.*','- **Naam / நாம்** — active work; first pass **67/67 COMPLETE**; dual-gate **27/67**; visual **27/67**; glyph-final **30/67**; source holds PDF 5 / PDF 10 / PDF 24; downstream blocked.')
sec=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **27/67 / 27/67**;\n- historical-glyph first-pass / final: **67/67 / 30/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-030-034.md`;\n- structured derivatives / English / reader remain blocked.\n\n**Exact next activity:** {NEXT}\n'''
s=between(s,'## 8. Naam active checkpoint','## 9. Ammayappan closed checkpoint',sec); wr(p,s)

# Status consistency audit
p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
r='**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** has first pass **67/67 COMPLETE**, dual-gate verification **27/67**, visual-fidelity **27/67**, historical-glyph final **30/67**, and **3 source-obscuration holds** (PDF 5, PDF 10, PDF 24). PDF 30–34 is fully verified and adds no uncertainty.'
s=sub1(s,r'\*\*PASS for the current repository-wide checkpoint\.\*\*.*?\n\n',r+'\n\n',flags=re.S)
s=sub1(s,r'\| Naam / நாம் \|.*','| Naam / நாம் | first pass 67/67 COMPLETE; dual-gate 27/67; 3 source holds | 45 scenes mapped; derivatives blocked | not-started | not-started |')
sec=f'''## Naam current checkpoint\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **27/67 / 27/67**;\n- historical-glyph first-pass / final: **67/67 / 30/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 30–34: **5/5 VERIFIED**;\n- current audit: `works/naam/notes/verification-audit-pdf-030-034.md`;\n- downstream layers remain blocked.\n\n**Next production phase:** {NEXT}\n'''
s=between(s,'## Naam current checkpoint','## Ammayappan current checkpoint',sec)
i=s.find('## Conclusion')
if i<0: raise SystemExit('missing conclusion')
s=s[:i]+'''## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is active with first pass **67/67 COMPLETE**, dual-gate **27/67**, visual **27/67**, glyph-final **30/67**, and source holds on PDF 5, PDF 10 and PDF 24. Next verification batch: **PDF 35–39**.\n'''
wr(p,s)

print('\n'.join(changed))
