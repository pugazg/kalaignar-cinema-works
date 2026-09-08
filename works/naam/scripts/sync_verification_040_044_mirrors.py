#!/usr/bin/env python3
import re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 45–49. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–44 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
changed=[]
def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
 q=R/p; old=q.read_text(encoding='utf-8') if q.exists() else ''
 if old!=s: q.write_text(s,encoding='utf-8'); changed.append(p)
def between(s,a,b,r):
 i=s.find(a); j=s.find(b,i+len(a)) if i>=0 else -1
 if i<0 or j<0: raise SystemExit('missing section '+a)
 return s[:i]+r.rstrip()+'\n\n'+s[j:]
# Work README
p='works/naam/README.md'; s=rd(p)
for a,b in [
 ('canonical Tamil verified pages: **32/67**','canonical Tamil verified pages: **37/67**'),
 ('visual fidelity audit: **in progress — 32/67 pages passed**','visual fidelity audit: **in progress — 37/67 pages passed**'),
 ('historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 35/67 final-verified**','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 40/67 final-verified**'),
 ('dual-gate verification pass is in progress: **32/67** pages are now verified;','dual-gate verification pass is in progress: **37/67** pages are now verified;'),
 ('**32/67** canonical pages are dual-gate VERIFIED:','**37/67** canonical pages are dual-gate VERIFIED:')
]:
 if a in s: s=s.replace(a,b,1)
sec='''## Verification audit — through PDF 44\n\n- PDF 6–9, PDF 11–23 and PDF 25–44: **dual-gate VERIFIED — 37/67 total**;\n- PDF 5 / PDF 10: **HOLD** for physical source loss; PDF 24: **HOLD** for later ink/mark obscuring the post-`தே` printed glyph;\n- visual-fidelity passed: **37/67**; historical-glyph final verified: **40/67**;\n- open source uncertainties: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 40–44: **5/5 VERIFIED**, no new uncertainty;\n- detailed audit: `notes/verification-audit-pdf-040-044.md`.\n\n**Next verification range:** PDF 45–49.\n'''
for old in ['## Verification audit — through PDF 39','## Verification audit — through PDF 34']:
 if old in s:
  s=between(s,old,'## Song / verse / performance structures mapped or confirmed so far',sec); break
s=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S)
wr(p,s)
# Transcription README
p='works/naam/transcription/README.md'; s=rd(p)
for a,b in [
 ('- verified pages: **32**;','- verified pages: **37**;'),
 ('- separate visual-fidelity audit: **in progress — 32/67 passed**;','- separate visual-fidelity audit: **in progress — 37/67 passed**;'),
 ('- historical-glyph final verified pages: **35/67**;','- historical-glyph final verified pages: **40/67**;')
]:
 if a in s: s=s.replace(a,b,1)
if '## Verification audit — PDF 40–44' not in s:
 marker='## PDF 45–49 source decisions'
 block='''## Verification audit — PDF 40–44\n\nPDF 40–44 are **5/5 VERIFIED** after direct source comparison. Corrections include PDF 40 `விதியற்றவனே`; PDF 41 `விளைவு`; PDF 42 `உயிலைகொடுத்தவுடன்`, `விவாக சுப`; PDF 43 `மண்டூகங்கள்`; PDF 44 `இல்லே`, `போட்டி ஆஸ்பத்திரி`. Current totals: visual **37/67**, glyph-final **40/67**, dual-gate verified **37/67**, open uncertainties **3**. Detailed log: `../notes/verification-audit-pdf-040-044.md`.\n\n'''
 if marker in s: s=s.replace(marker,block+marker,1)
s=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S)
wr(p,s)
# Project handover
p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
for a,b in [
 ('canonical Tamil verified: **32/67**','canonical Tamil verified: **37/67**'),
 ('visual fidelity audit: **in progress — 32/67 passed**','visual fidelity audit: **in progress — 37/67 passed**'),
 ('historical-glyph final verified: **35/67**','historical-glyph final verified: **40/67**')
]:
 if a in s: s=s.replace(a,b,1)
if '- `notes/verification-audit-pdf-040-044.md`.' not in s:
 for prev in ['- `notes/verification-audit-pdf-035-039.md`.','- `notes/verification-audit-pdf-030-034.md`.']:
  if prev in s: s=s.replace(prev,prev+'\n- `notes/verification-audit-pdf-040-044.md`.',1); break
for old in ['## Verification checkpoint through PDF 39','## Verification checkpoint through PDF 34']:
 i=s.find(old)
 if i>=0:
  s=s[:i]+f'''## Verification checkpoint through PDF 44\n\n- PDF 6–9, PDF 11–23 and PDF 25–44: **VERIFIED — 37/67 total**;\n- PDF 5 / PDF 10 remain physical-source-damage holds; PDF 24 remains a later-ink/mark source-obscuration hold;\n- visual-fidelity: **37/67**; glyph-final: **40/67**; dual-gate: **37/67**;\n- open source uncertainties: **3**;\n- PDF 40–44 is fully verified and adds no uncertainty.\n\n## Exact next activity\n\n> **{NEXT}**\n'''; break
wr(p,s)
# Next prompt
wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCurrent durable checkpoint: first pass **67/67 COMPLETE**; visual-fidelity **37/67**; historical-glyph final **40/67**; dual-gate verified **37/67** (PDF 6–9, PDF 11–23, PDF 25–44); open source holds **3** — PDF 5, PDF 10, PDF 24. PDF 9 is resolved as `குறுக்கொடிய`. PDF 24 scene 11 remains directly readable only through visible `கெளரவம் தே… இருப்பது`; do not restore `தேடி` without new direct-source evidence. Structured derivatives and English remain blocked.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\nDetailed current audit: `works/naam/notes/verification-audit-pdf-040-044.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')
# Root README
p='README.md'; s=rd(p)
sec=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake/map and first-pass Tamil are complete; dual-gate verification is in progress.\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **37/67 / 37/67**;\n- historical-glyph first-pass / final: **67/67 / 40/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-040-044.md`;\n- derivatives / English remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''
s=between(s,'## நாம் status','## ராஜா ராணி status',sec)
wr(p,s)
# Master handover
p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=re.sub(r'- \*\*Naam / நாம்\*\* — active work;.*','- **Naam / நாம்** — active work; first pass **67/67 COMPLETE**; dual-gate **37/67**; visual **37/67**; glyph-final **40/67**; source holds PDF 5 / PDF 10 / PDF 24; downstream blocked.',s,count=1)
sec=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **37/67 / 37/67**;\n- historical-glyph first-pass / final: **67/67 / 40/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-040-044.md`;\n- structured derivatives / English / reader remain blocked.\n\n**Exact next activity:** {NEXT}\n'''
s=between(s,'## 8. Naam active checkpoint','## 9. Ammayappan closed checkpoint',sec)
wr(p,s)
# Status consistency audit
p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
r='**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** has first pass **67/67 COMPLETE**, dual-gate verification **37/67**, visual-fidelity **37/67**, historical-glyph final **40/67**, and **3 source-obscuration holds** (PDF 5, PDF 10, PDF 24). PDF 40–44 is fully verified and adds no uncertainty.'
s=re.sub(r'\*\*PASS for the current repository-wide checkpoint\.\*\*.*?\n\n',r+'\n\n',s,count=1,flags=re.S)
s=re.sub(r'\| Naam / நாம் \|.*','| Naam / நாம் | first pass 67/67 COMPLETE; dual-gate 37/67; 3 source holds | 45 scenes mapped; derivatives blocked | not-started | not-started |',s,count=1)
sec=f'''## Naam current checkpoint\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **37/67 / 37/67**;\n- historical-glyph first-pass / final: **67/67 / 40/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 40–44: **5/5 VERIFIED**;\n- current audit: `works/naam/notes/verification-audit-pdf-040-044.md`;\n- downstream layers remain blocked.\n\n**Next production phase:** {NEXT}\n'''
s=between(s,'## Naam current checkpoint','## Ammayappan current checkpoint',sec)
i=s.find('## Conclusion')
if i>=0:
 s=s[:i]+'''## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is active with first pass **67/67 COMPLETE**, dual-gate **37/67**, visual **37/67**, glyph-final **40/67**, and source holds on PDF 5, PDF 10 and PDF 24. Next verification batch: **PDF 45–49**.\n'''
wr(p,s)
print('\n'.join(changed))
