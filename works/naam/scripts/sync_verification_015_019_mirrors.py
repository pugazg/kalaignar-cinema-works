#!/usr/bin/env python3
import re
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
def between(s,a,b,r):
 i=s.find(a); j=s.find(b,i+len(a)) if i>=0 else -1
 if i<0 or j<0: raise SystemExit('missing section '+a)
 return s[:i]+r.rstrip()+'\n\n'+s[j:]
# Work README
p='works/naam/README.md'; s=rd(p)
for a,b in [('canonical Tamil verified pages: **8/67**','canonical Tamil verified pages: **13/67**'),('visual fidelity audit: **in progress — 8/67 pages passed**','visual fidelity audit: **in progress — 13/67 pages passed**'),('historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 10/67 final-verified**','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 15/67 final-verified**'),('dual-gate verification pass is in progress: **8/67** pages are now verified','dual-gate verification pass is in progress: **13/67** pages are now verified'),('**8/67** canonical pages are dual-gate VERIFIED: PDF 6–9 and PDF 11–14.','**13/67** canonical pages are dual-gate VERIFIED: PDF 6–9 and PDF 11–19.')]: s=one(s,a,b)
sec='''## Verification audit — through PDF 19\n\n- PDF 6–9 and PDF 11–19: **dual-gate VERIFIED — 13/67 total**;\n- PDF 5 / PDF 10: **HOLD** for physical source loss; no reconstruction;\n- visual-fidelity passed: **13/67**; historical-glyph final verified: **15/67**;\n- open source uncertainties: **2** — PDF 5 and PDF 10;\n- PDF 15–19: **5/5 VERIFIED**, no new uncertainty;\n- detailed audit: `notes/verification-audit-pdf-015-019.md`.\n\n**Next verification range:** PDF 20–24.\n'''
s=between(s,'## Verification audit — through PDF 14','## Song / verse / performance structures mapped or confirmed so far',sec)
s=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S); wr(p,s)
# Transcription README
p='works/naam/transcription/README.md'; s=rd(p)
for a,b in [('- verified pages: **8**;','- verified pages: **13**;'),('- separate visual-fidelity audit: **in progress — 8/67 passed**;','- separate visual-fidelity audit: **in progress — 13/67 passed**;'),('- historical-glyph final verified pages: **10/67**;','- historical-glyph final verified pages: **15/67**;')]: s=one(s,a,b)
if '## Verification audit — PDF 15–19' not in s:
 marker='## PDF 20–24 source decisions'; block='''## Verification audit — PDF 15–19\n\nPDF 15–19 are **5/5 VERIFIED**. Current totals: visual **13/67**, glyph-final **15/67**, dual-gate verified **13/67**, open uncertainties **2** (PDF 5 and PDF 10 only). Detailed log: `../notes/verification-audit-pdf-015-019.md`.\n\n''';
 if marker not in s: raise SystemExit('missing transcription marker')
 s=s.replace(marker,block+marker,1)
s=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S); wr(p,s)
# Project handover
p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
for a,b in [('canonical Tamil verified: **8/67**','canonical Tamil verified: **13/67**'),('visual fidelity audit: **in progress — 8/67 passed**','visual fidelity audit: **in progress — 13/67 passed**'),('historical-glyph final verified: **10/67**','historical-glyph final verified: **15/67**')]: s=one(s,a,b)
if '- `notes/verification-audit-pdf-015-019.md`.' not in s: s=s.replace('- `notes/verification-audit-pdf-010-014.md`.','- `notes/verification-audit-pdf-010-014.md`.\n- `notes/verification-audit-pdf-015-019.md`.',1)
i=s.find('## Verification checkpoint through PDF 14')
if i<0: raise SystemExit('missing project checkpoint')
s=s[:i]+f'''## Verification checkpoint through PDF 19\n\n- PDF 6–9 and PDF 11–19: **VERIFIED — 13/67 total**;\n- PDF 5 / PDF 10 remain physical-source-damage holds;\n- visual-fidelity: **13/67**; glyph-final: **15/67**; dual-gate: **13/67**;\n- open source uncertainties: **2**;\n- PDF 15–19 is fully verified and adds no uncertainty.\n\n## Exact next activity\n\n> **{NEXT}**\n'''; wr(p,s)
# Next prompt
wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCurrent durable checkpoint: first pass **67/67 COMPLETE**; visual-fidelity **13/67**; historical-glyph final **15/67**; dual-gate verified **13/67** (PDF 6–9, 11–19); open source holds **2** (PDF 5, PDF 10). PDF 9 is resolved as `குறுக்கொடிய`. Structured derivatives and English remain blocked.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\nDetailed current audit: `works/naam/notes/verification-audit-pdf-015-019.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')
# Root README: only Naam section
p='README.md'; s=rd(p); sec=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake/map and first-pass Tamil are complete; dual-gate verification is in progress.\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **13/67 / 13/67**;\n- historical-glyph first-pass / final: **67/67 / 15/67**;\n- open source holds: **2** — PDF 5 and PDF 10;\n- current audit: `works/naam/notes/verification-audit-pdf-015-019.md`;\n- derivatives / English remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''; s=between(s,'## நாம் status','## ராஜா ராணி status',sec); wr(p,s)
# Master handover
p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=re.sub(r'- \*\*Naam / நாம்\*\* — active work;.*', '- **Naam / நாம்** — active work; first pass **67/67 COMPLETE**; dual-gate **13/67**; visual **13/67**; glyph-final **15/67**; physical holds PDF 5 / PDF 10; downstream blocked.',s,count=1)
sec=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **13/67 / 13/67**;\n- historical-glyph first-pass / final: **67/67 / 15/67**;\n- open source holds: **2** — PDF 5 and PDF 10;\n- current audit: `works/naam/notes/verification-audit-pdf-015-019.md`;\n- structured derivatives / English / reader remain blocked.\n\n**Exact next activity:** {NEXT}\n'''; s=between(s,'## 8. Naam active checkpoint','## 9. Ammayappan closed checkpoint',sec); wr(p,s)
# Status audit
p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
r='**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** has first pass **67/67 COMPLETE**, dual-gate verification **13/67**, visual-fidelity **13/67**, historical-glyph final **15/67**, and **2 physical-source holds** (PDF 5 and PDF 10). PDF 15–19 is fully verified and adds no uncertainty.'
s=re.sub(r'\*\*PASS for the current repository-wide checkpoint\.\*\*.*?\n\n',r+'\n\n',s,count=1,flags=re.S)
s=re.sub(r'\| Naam / நாம் \|.*','| Naam / நாம் | first pass 67/67 COMPLETE; dual-gate 13/67; 2 physical holds | 45 scenes mapped; derivatives blocked | not-started | not-started |',s,count=1)
sec=f'''## Naam current checkpoint\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **13/67 / 13/67**;\n- historical-glyph first-pass / final: **67/67 / 15/67**;\n- open source holds: **2** — PDF 5 and PDF 10;\n- PDF 15–19: **5/5 VERIFIED**;\n- current audit: `works/naam/notes/verification-audit-pdf-015-019.md`;\n- downstream layers remain blocked.\n\n**Next production phase:** {NEXT}\n'''; s=between(s,'## Naam current checkpoint','## Ammayappan current checkpoint',sec)
i=s.find('## Conclusion')
if i<0: raise SystemExit('missing conclusion')
s=s[:i]+'''## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is active with first pass **67/67 COMPLETE**, dual-gate **13/67**, visual **13/67**, glyph-final **15/67**, and source-damage holds on PDF 5 and PDF 10. Next verification batch: **PDF 20–24**.\n'''; wr(p,s)
print('\n'.join(changed))