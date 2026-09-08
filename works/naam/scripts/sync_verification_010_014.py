#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
NEXT=("Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 15–19. "
      "Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen PDF 6–9 or "
      "PDF 11–14 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain explicit physical-source-damage "
      "holds. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete.")
changed=[]

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def write(rel,text):
    p=ROOT/rel; old=p.read_text(encoding='utf-8') if p.exists() else ''
    if old!=text:
        p.write_text(text,encoding='utf-8'); changed.append(rel)

def replace_section(text,heading,next_heading,replacement):
    i=text.find(heading)
    if i<0: return text
    j=text.find(next_heading,i+len(heading)) if next_heading else len(text)
    if j<0: return text
    return text[:i]+replacement.rstrip()+"\n\n"+text[j:]

# Preconditions
idxp='works/naam/transcription/index.json'; idx=json.loads(read(idxp))
for k,v in {'first_pass_pages_completed':67,'verified_pages':4,'visual_fidelity_passed_pages':4,'historical_glyph_verified_pages':5,'open_uncertainty_markers':1}.items():
    if idx.get(k)!=v: raise SystemExit(f'index precondition {k}: {idx.get(k)!r} != {v!r}')
audit=read('works/naam/notes/verification-audit-pdf-010-014.md')
for x in ['PDF 11–14 PASS / VERIFIED','`மகனோடே குலாவுறே?`','`வேலையைப்பாரு!`','`எங்களை புலியா மாத்துறுங்க`','`(மாத்திரை போகிறான்)`','`சங்கேதப் படாதீர்கள்!`']:
    if x not in audit: raise SystemExit(f'audit safeguard missing: {x}')
batch=read('works/naam/transcription/parts/pdf-010-014.md')
for x in ['pdf=10 printed=10 status=needs-review glyph=verified-final','pdf=11 printed=11 status=verified glyph=verified-final','pdf=14 printed=14 status=verified glyph=verified-final','வரைக்⟦தெளிவில்லை','சங்கேதப் படாதீர்கள்!']:
    if x not in batch: raise SystemExit(f'batch safeguard missing: {x}')

# Index
idx.update(status='verification-in-progress',draft_pages=59,verified_pages=8,visual_fidelity_passed_pages=8,
           historical_glyph_verified_pages=10,review_pages=59,open_uncertainty_markers=2,next_action=NEXT)
for x in idx.get('parts',[]):
    if x.get('path')=='parts/pdf-010-014.md':
        x.update(status='mixed-pdf10-needs-review-pdf11-14-verified',historical_glyph_status='verified-final',open_uncertainties=1)
write(idxp,json.dumps(idx,ensure_ascii=False,indent=2)+'\n')

# Metadata
rel='works/naam/metadata.yaml'; t=read(rel)
repls=[
('  draft_pages: 63','  draft_pages: 59'),('  verified_pages: 4','  verified_pages: 8'),('  review_pages: 63','  review_pages: 59'),
('  open_uncertainty_markers: 1','  open_uncertainty_markers: 2'),('  pages_verified: 5','  pages_verified: 10'),
('  visual_fidelity_audit: in-progress-pdf-005-009-4-of-5-pass','  visual_fidelity_audit: in-progress-through-pdf-014-8-of-67-pass'),
('  historical_glyph_audit: final-verification-in-progress-5-of-67','  historical_glyph_audit: final-verification-in-progress-10-of-67')]
for old,new in repls:
    if old in t: t=t.replace(old,new,1)
vp='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-010-014.md"\n  visual_fidelity_passed_pages: 8\n  historical_glyph_final_verified_pages: 10\n  dual_gate_verified_pages: 8\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "15-19"\n'''
t=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',vp+'\nhistorical_glyph:\n',t,count=1,flags=re.S)
t=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',t,count=1,flags=re.S)
write(rel,t)

# Historical-glyph audit
rel='works/naam/notes/historical-glyph-audit.md'; t=read(rel)
t=t.replace('| PDF 10–14 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 10–14 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF10 hold |',1)
t=t.replace('| **Total** | **67** | **67** | **4** | **63** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **8** | **59** | **final-verification-in-progress** |',1)
t=t.replace('| 11 | 11 | old-form cluster in `கண்ணாடிச்` | `கண்ணாடிச்` | `ணா` | enlarged source pixels; positive family occurrence | draft-supported |','| 11 | 11 | old-form cluster in `கண்ணாடிச்` | `கண்ணாடிச்` | `ணா` | enlarged source pixels; positive family occurrence | **final-verified** |',1)
if '## PDF 10–14 final dual-gate audit' not in t:
    t += '''\n## PDF 10–14 final dual-gate audit\n\n- historical-glyph final PASS: **PDF 10–14 / 5 of 5**;\n- visual-fidelity PASS: **PDF 11–14 / 4 pages**;\n- PDF 10 remains held only because the physical right edge removes the ending of a word after visible `வரைக்…`; no reconstruction is permitted;\n- source corrections include `மகனோடே`, `வேலையைப்பாரு`, `கூடாதுன்னு`, `எங்களை`, `இல்லேப்பா`, the restored `(மாத்திரை போகிறான்)`, `உயிரை`, and `சங்கேதப் படாதீர்கள்`;\n- full decision log: `verification-audit-pdf-010-014.md`.\n\nNext final audit range: **PDF 15–19**.\n'''
write(rel,t)

# Work README
rel='works/naam/README.md'; t=read(rel)
for old,new in [('canonical Tamil verified pages: **4/67**','canonical Tamil verified pages: **8/67**'),
                ('visual fidelity audit: **in progress — 4/67 pages passed**','visual fidelity audit: **in progress — 8/67 pages passed**'),
                ('historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 5/67 final-verified**','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 10/67 final-verified**'),
                ('open source uncertainty markers: **1**','open source uncertainty markers: **2**')]: t=t.replace(old,new,1)
t=t.replace('The first-pass gate is complete; all pages remain draft/needs-review until the separate visual-fidelity and final historical-glyph verification gates close.','The first-pass gate is complete and the dual-gate verification pass is in progress: **8/67** pages are now verified; PDF 5 and PDF 10 remain physical-source-damage holds.',1)
t=t.replace('- two source uncertainties remain explicit rather than guessed: a damaged introductory line on PDF 5 and one unclear montage word on PDF 9;','- two source uncertainties remain explicit rather than guessed: the damaged introductory beginning on PDF 5 and the damaged right-edge word ending on PDF 10; PDF 9 is resolved as `குறுக்கொடிய`;',1)
t=t.replace('- PDF 10–71 adds **0** new uncertainty markers;','- PDF 10 adds one physical-source-damage uncertainty; PDF 11–71 adds no new uncertainty markers;',1)
t=t.replace('- **0** of the sixty-seven canonical pages are called verified yet.','- **8/67** canonical pages are dual-gate VERIFIED: PDF 6–9 and PDF 11–14.',1)
block='''## Verification audit — through PDF 14\n\n- PDF 6–9 and PDF 11–14: **dual-gate VERIFIED — 8/67 total**;\n- PDF 5: **HOLD** for physically missing introductory-line beginning;\n- PDF 10: **HOLD** for physically missing right-edge word ending after visible `வரைக்…`;\n- visual-fidelity passed: **8/67**; historical-glyph final verified: **10/67**;\n- open source uncertainties: **2** — PDF 5 and PDF 10;\n- PDF 9's former uncertainty is resolved as `குறுக்கொடிய`;\n- PDF 10–14 scan-backed corrections include `மகனோடே`, `வேலையைப்பாரு`, `கூடாதுன்னு`, `எங்களை`, `இல்லேப்பா`, `(மாத்திரை போகிறான்)`, `உயிரை`, and `சங்கேதப் படாதீர்கள்`;\n- detailed logs: `notes/verification-audit-pdf-005-009.md` and `notes/verification-audit-pdf-010-014.md`.\n\n**Next verification range:** PDF 15–19.\n'''
t=replace_section(t,'## Verification audit — PDF 5–9','## Song / verse / performance structures mapped or confirmed so far',block)
t=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S)
write(rel,t)

# Transcription README
rel='works/naam/transcription/README.md'; t=read(rel)
t=re.sub(r'- verified pages: \*\*\d+\*\*;','- verified pages: **8**;',t,count=1)
t=re.sub(r'- separate visual-fidelity audit: \*\*.*?\*\*;','- separate visual-fidelity audit: **in progress — 8/67 passed**;',t,count=1)
t=re.sub(r'- historical-glyph final verified pages: \*\*\d+/67\*\*;','- historical-glyph final verified pages: **10/67**;',t,count=1)
t=re.sub(r'- open source uncertainty markers: \*\*\d+\*\*;','- open source uncertainty markers: **2**;',t,count=1)
if '## Verification audit — PDF 10–14' not in t:
    marker='## PDF 15–19 source reconciliation'
    block='''## Verification audit — PDF 10–14\n\nPDF 11–14 are VERIFIED after direct rendered-page comparison and final historical-glyph review. PDF 10 remains on physical-source-damage hold because the right edge removes the ending of the word after visible `வரைக்…`; no completion is inferred. Current totals: visual **8/67**, glyph-final **10/67**, dual-gate verified **8/67**, open uncertainties **2**. Detailed log: `../notes/verification-audit-pdf-010-014.md`.\n\n'''
    if marker in t: t=t.replace(marker,block+marker,1)
t=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S)
write(rel,t)

# Project handover
rel='works/naam/PROJECT_HANDOVER.md'; t=read(rel)
for old,new in [('canonical Tamil verified: **4/67**','canonical Tamil verified: **8/67**'),('visual fidelity audit: **in progress — 4/67 passed**','visual fidelity audit: **in progress — 8/67 passed**'),('historical-glyph final verified: **5/67**','historical-glyph final verified: **10/67**'),('open source uncertainty markers: **1**','open source uncertainty markers: **2**')]: t=t.replace(old,new,1)
if '- `notes/verification-audit-pdf-010-014.md`.' not in t:
    anchor='- `notes/verification-audit-pdf-005-009.md`.'
    if anchor in t: t=t.replace(anchor,anchor+'\n- `notes/verification-audit-pdf-010-014.md`.',1)
if '## Verification checkpoint through PDF 14' not in t:
    t += f'''\n## Verification checkpoint through PDF 14\n\n- PDF 6–9 and PDF 11–14: **VERIFIED**;\n- PDF 5: physical left-edge introductory-line hold;\n- PDF 10: physical right-edge word-ending hold after visible `வரைக்…`;\n- visual-fidelity passed: **8/67**; glyph-final: **10/67**; dual-gate verified: **8/67**;\n- open source uncertainties: **2**;\n- detailed audits: `notes/verification-audit-pdf-005-009.md`, `notes/verification-audit-pdf-010-014.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
else:
    t=re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\s*$',f'## Exact next activity\n\n> **{NEXT}**\n',t,count=1,flags=re.S)
write(rel,t)

# Next chat prompt overwrite
write('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages**;\n- visual-fidelity passed: **8/67**;\n- historical-glyph first-pass checked: **67/67**;\n- historical-glyph final verified: **10/67**;\n- dual-gate canonical verified: **8/67** — PDF 6–9 and PDF 11–14;\n- open uncertainty markers: **2** — PDF 5 damaged introductory beginning and PDF 10 damaged right-edge word ending;\n- structured derivatives / English: **blocked pending verified Tamil**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; canonical screenplay PDF **5–71**.\n\n## Frozen verified pages\n\nDo not reopen PDF 6–9 or PDF 11–14 absent genuinely new direct-source evidence. PDF 5 remains held because its introductory line loses the left beginning. PDF 10 remains held because its right edge physically loses the ending after visible `வரைக்…`; do not reconstruct `வரைக்கும்` or another expected form.\n\nPDF 10–14 corrections include `மகனோடே`, `வேலையைப்பாரு`, `கூடாதுன்னு`, `எங்களை`, `இல்லேப்பா`, restored `(மாத்திரை போகிறான்)`, `உயிரை`, and `சங்கேதப் படாதீர்கள்`.\n\nDetailed audits: `works/naam/notes/verification-audit-pdf-005-009.md` and `works/naam/notes/verification-audit-pdf-010-014.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# data/works.json
rel='data/works.json'; d=json.loads(read(rel)); n=next(x for x in d if x.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-014-8-of-67',historical_glyph_audit='final-verification-in-progress-10-of-67',
         canonical_tamil_draft_pages=59,canonical_tamil_verified_pages=8,canonical_tamil_review_pages=59,canonical_tamil_open_uncertainty_markers=2,
         historical_glyph_pages_verified=10,visual_fidelity_passed_pages=8,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-010-014.md',next_action=NEXT)
write(rel,json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')

# Root README
rel='README.md'; t=read(rel)
t=t.replace('verified pages: **4/67**; visual-fidelity audit: **in progress — 4/67**;','verified pages: **8/67**; visual-fidelity audit: **in progress — 8/67**;',1)
t=t.replace('historical-glyph first-pass checked: **67/67**; final glyph-verified: **5/67**;','historical-glyph first-pass checked: **67/67**; final glyph-verified: **10/67**;',1)
t=t.replace('open source uncertainty markers: **1**','open source uncertainty markers: **2**',1)
pos=t.find('## நாம் status')
if pos>=0:
    end=t.find('\n## ',pos+5)
    if end<0:end=len(t)
    b=t[pos:end]; b=re.sub(r'\*\*Next:\*\* .*$',f'**Next:** {NEXT}',b,flags=re.M); t=t[:pos]+b+t[end:]
write(rel,t)

# Master handover and consistency audit
for rel in ['docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md','docs/STATUS_CONSISTENCY_AUDIT.md']:
    t=read(rel)
    t=t.replace('verified **4/67**','verified **8/67**')
    t=t.replace('verified pages: **4/67**','verified pages: **8/67**')
    t=t.replace('visual-fidelity audit: **in progress — 4/67 passed**','visual-fidelity audit: **in progress — 8/67 passed**')
    t=t.replace('historical-glyph first-pass checked / final verified: **67/67 / 5/67**','historical-glyph first-pass checked / final verified: **67/67 / 10/67**')
    t=t.replace('open source uncertainties: **1**','open source uncertainties: **2**')
    t=t.replace('**1 remaining source uncertainty**','**2 physical-source uncertainties**')
    oldnext='Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 10–14. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen PDF 6–9 absent genuinely new direct-source evidence; PDF 5 remains an explicit source-damage hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete.'
    t=t.replace(oldnext,NEXT)
    write(rel,t)

print('Synchronized Naam verification through PDF 14:')
for x in changed: print('-',x)
