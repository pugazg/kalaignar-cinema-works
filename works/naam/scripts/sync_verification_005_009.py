#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
NEXT=("Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 10–14. "
      "Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen PDF 6–9 absent "
      "genuinely new direct-source evidence; PDF 5 remains an explicit source-damage hold. Structured derivatives and "
      "English translation remain blocked until the verified Tamil gate is complete.")
changed=[]

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')
def write(rel,text):
    p=ROOT/rel; old=p.read_text(encoding='utf-8') if p.exists() else ''
    if old!=text:
        p.write_text(text,encoding='utf-8'); changed.append(rel)

def replace_one(text,old,new,label):
    if old not in text: raise SystemExit(f'missing {label}: {old}')
    return text.replace(old,new,1)

def replace_section(text,heading,next_heading,replacement):
    i=text.find(heading)
    if i<0: return text
    j=text.find(next_heading,i+len(heading)) if next_heading else len(text)
    if j<0: return text
    return text[:i]+replacement.rstrip()+"\n\n"+text[j:]

# Preconditions
idxp='works/naam/transcription/index.json'; idx=json.loads(read(idxp))
if idx.get('first_pass_complete') is not True or idx.get('first_pass_pages_completed')!=67:
    raise SystemExit('Naam first-pass closure precondition failed')
if idx.get('verified_pages') not in (0,4):
    raise SystemExit(f'unexpected preexisting verified_pages={idx.get("verified_pages")}')
audit=read('works/naam/notes/verification-audit-pdf-005-009.md')
for x in ['PDF 6–9 PASS / VERIFIED','`கொண்டாட்டம் ஒண்ணுமில்லையப்பா...`','`அந்த உல்லாசத்திலே அவற்றை எல்லாம் மறந்து விடுவான்!`','`ஆரஞ்சுப்பழம் வருகிறது`','`பாட்டாளி குமரனுக்கு`','`தனது காதல் சுவையுள்ள பொருள்கள்`']:
    if x not in audit: raise SystemExit(f'verification audit safeguard missing: {x}')

# Canonical batch corrections + page statuses
rel='works/naam/transcription/parts/pdf-005-009.md'; t=read(rel)
t=t.replace('Status: **draft / needs-review** — rendered scan controls; open source uncertainties remain explicit.  ','Status: **mixed verification — PDF 5 needs-review; PDF 6–9 VERIFIED** — rendered scan controls.  ',1)
t=t.replace('Historical-glyph first-pass: **checked page-by-page, not final-verified**.','Historical-glyph final verification: **PASS PDF 5–9 / 5 of 5**.',1)
t=t.replace('<!-- source: pdf=5 printed=unknown status=draft glyph=checked-first-pass -->','<!-- source: pdf=5 printed=unknown status=needs-review glyph=verified-final -->',1)
for p in range(6,10):
    t=t.replace(f'<!-- source: pdf={p} printed={p} status=draft glyph=checked-first-pass -->',f'<!-- source: pdf={p} printed={p} status=verified glyph=verified-final -->',1)
t=replace_one(t,'⟦தெளிவில்லை — PDF 5 முதல் அறிமுகப் பத்தியின் சேதமடைந்த வரி; `... சில துரோகிகள் ...` மட்டும் உறுதி⟧','⟦தெளிவில்லை — PDF 5 வரியின் இடதுபுறத் தொடக்கம் உடல் சேதத்தால் இல்லை; நேரடியாகத் தெரியும் பகுதி: `…னைத் கொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`⟧','pdf5 narrowed uncertainty')
for old,new,label in [
('கொண்டாட்டம் ஒன்றுமில்லையப்பா...','கொண்டாட்டம் ஒண்ணுமில்லையப்பா...','pdf5 onnum'),
('அதனால் மாரியாத்தாளுக்கு பூஜை நடத்துகிறோம்.','அதனால் மாரியாத்தாளுக்கு பூசை நடத்துகிறோம்.','pdf5 poosai'),
('அந்த உலகத்திலே அவற்றை எல்லாம் மறந்து விடுவான்!','அந்த உல்லாசத்திலே அவற்றை எல்லாம் மறந்து விடுவான்!','pdf8 ullaasam'),
('புதுவேலைக்காரி வந்திருக்காங்களே.','புதுவேலைக்காரி வந்திருக்காங்க.','pdf9 vandhirukkaanga'),
('குமரன் ⟦தெளிவில்லை: `குறுக்கொடிய` போலத் தோன்றும் சேதமடைந்த சொல்⟧—வியர்வை சிந்த விறகு வெட்டி இருக்கிறான்.','குமரன் குறுக்கொடிய—வியர்வை சிந்த விறகு வெட்டி இருக்கிறான்.','pdf9 kurukkodiya'),
('அடுத்து ஆட்டுப்பழம் வருகிறது—ஆறுதல் பெறுகிறான்.','அடுத்து ஆரஞ்சுப்பழம் வருகிறது—ஆறுதல் பெறுகிறான்.','pdf9 orange'),
('பட்டாளி குமரனுக்கு பால் வருகிறது—பரவசம் அடைகிறான்.','பாட்டாளி குமரனுக்கு பால் வருகிறது—பரவசம் அடைகிறான்.','pdf9 paattaali'),
('மீனு தனது காதில் சுவையுள்ள பொருள்கள் மூலம் குமரனுக்கு அறிவித்தாள்.','மீனு தனது காதல் சுவையுள்ள பொருள்கள் மூலம் குமரனுக்கு அறிவித்தாள்.','pdf9 kaadhal')]:
    t=replace_one(t,old,new,label)
# Replace stale audit note block with verified state summary
marker='## First-pass audit notes'
if marker in t:
    t=t[:t.index(marker)] + '''## Dual-gate verification result\n\n- PDF 6–9: **VERIFIED** after full rendered-page comparison and final occurrence-specific historical-glyph review.\n- PDF 5: **needs-review** only because the left beginning of one introductory line is physically missing; the surviving tail is preserved exactly and not reconstructed.\n- Historical-glyph final verification: **5/5 PASS** for PDF 5–9.\n- Visual-fidelity PASS: **4/5**; dual-gate verified: **4/5**.\n- The former PDF 9 uncertainty is resolved as source-visible `குறுக்கொடிய`; cumulative open source uncertainties drop from **2 → 1**.\n- Detailed decisions: `../../notes/verification-audit-pdf-005-009.md`.\n'''
write(rel,t)

# Index
idx=json.loads(read(idxp))
idx.update(status='verification-in-progress',draft_pages=63,verified_pages=4,visual_fidelity_passed_pages=4,
           historical_glyph_verified_pages=5,review_pages=63,open_uncertainty_markers=1,next_action=NEXT)
parts=idx.get('parts',[])
for x in parts:
    if x.get('path')=='parts/pdf-005-009.md':
        x.update(status='mixed-pdf5-needs-review-pdf6-9-verified',historical_glyph_status='verified-final',open_uncertainties=1)
write(idxp,json.dumps(idx,ensure_ascii=False,indent=2)+'\n')

# Metadata
rel='works/naam/metadata.yaml'; t=read(rel)
for old,new,label in [
('  status: first-pass-complete-verification-pending\n  pages_expected: 67','  status: verification-in-progress\n  pages_expected: 67','meta canonical status'),
('  draft_pages: 67','  draft_pages: 63','meta draft'),('  verified_pages: 0','  verified_pages: 4','meta verified'),
('  review_pages: 67','  review_pages: 63','meta review'),('  open_uncertainty_markers: 2','  open_uncertainty_markers: 1','meta uncertainty'),
('  status: first-pass-complete-final-verification-pending\n  main_text_pages_expected: 67','  status: final-verification-in-progress\n  main_text_pages_expected: 67','meta glyph status'),
('  pages_verified: 0','  pages_verified: 5','meta glyph verified'),
('  visual_fidelity_audit: not-started','  visual_fidelity_audit: in-progress-pdf-005-009-4-of-5-pass','meta visual status'),
('  historical_glyph_audit: first-pass-complete-through-pdf-071','  historical_glyph_audit: final-verification-in-progress-5-of-67','meta history status')]:
    t=replace_one(t,old,new,label)
# add explicit verification block before historical_glyph
if 'verification_progress:' not in t:
    anchor='\nhistorical_glyph:\n'
    block='''\nverification_progress:\n  current_audit_path: "notes/verification-audit-pdf-005-009.md"\n  visual_fidelity_passed_pages: 4\n  historical_glyph_final_verified_pages: 5\n  dual_gate_verified_pages: 4\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "10-14"\n'''
    if anchor not in t: raise SystemExit('metadata historical_glyph anchor missing')
    t=t.replace(anchor,block+anchor,1)
t=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',t,count=1,flags=re.S)
write(rel,t)

# Historical glyph audit
rel='works/naam/notes/historical-glyph-audit.md'; t=read(rel)
t=t.replace('Status: **first-pass-complete / final-verification-pending**','Status: **final-verification-in-progress**',1)
t=t.replace('| PDF 5–9 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 5–9 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF5 hold |',1)
t=t.replace('| **Total** | **67** | **67** | **0** | **67** | **first-pass-complete / final-verification-pending** |','| **Total** | **67** | **67** | **4** | **63** | **final-verification-in-progress** |',1)
t=t.replace('| 6 | 6 | apparent bare-`ள்` surface in `அவள்...` cluster | `அவளை` | `ளை` | enlarged source cluster + same-word syntax; old `ளை` identity | draft-supported |','| 6 | 6 | apparent bare-`ள்` surface in `அவள்...` cluster | `அவளை` | `ளை` | enlarged source cluster + same-word syntax; old `ளை` identity | **final-verified** |',1)
t=t.replace('| 6 | 6 | old `னா` form in `சூரியனால்` | `சூரியனால்` | `னா` | enlarged source pixels; family explicitly checked before Unicode encoding | draft-supported |','| 6 | 6 | old `னா` form in `சூரியனால்` | `சூரியனால்` | `னா` | enlarged source pixels; family explicitly checked before Unicode encoding | **final-verified** |',1)
if '## PDF 5–9 final dual-gate audit' not in t:
    t += '''\n## PDF 5–9 final dual-gate audit\n\n- historical-glyph final PASS: **PDF 5–9 / 5 of 5**;\n- visual-fidelity PASS: **PDF 6–9 / 4 pages**;\n- PDF 5 remains held only for a physically missing lexical beginning, not for unresolved historical-glyph identity;\n- PDF 9 historical/lexical reinspection resolves `குறுக்கொடிய` and confirms source `காதல்`;\n- full decision log: `verification-audit-pdf-005-009.md`.\n\nNext final audit range: **PDF 10–14**.\n'''
write(rel,t)

# Work README
rel='works/naam/README.md'; t=read(rel)
for old,new,label in [
('canonical Tamil verified pages: **0**','canonical Tamil verified pages: **4/67**','readme verified'),
('visual fidelity audit: **not-started**','visual fidelity audit: **in progress — 4/67 pages passed**','readme visual'),
('historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 0 final-verified**','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 5/67 final-verified**','readme glyph'),
('open source uncertainty markers: **2**','open source uncertainty markers: **1**','readme uncertainty')]:
    t=replace_one(t,old,new,label)
if '## Verification audit — PDF 5–9' not in t:
    marker='## Song / verse / performance structures mapped or confirmed so far'
    block='''## Verification audit — PDF 5–9\n\n- PDF 6–9: **dual-gate VERIFIED**;\n- PDF 5: **HOLD** for one physically damaged introductory-line beginning;\n- visual-fidelity passed: **4/67**; historical-glyph final verified: **5/67**; canonical dual-gate verified: **4/67**;\n- PDF 9 uncertainty resolved as `குறுக்கொடிய`; cumulative open uncertainties are now **1**;\n- scan-backed lexical corrections include PDF 5 `ஒண்ணுமில்லையப்பா` / `பூசை`, PDF 8 `உல்லாசத்திலே`, and PDF 9 `வந்திருக்காங்க`, `ஆரஞ்சுப்பழம்`, `பாட்டாளி`, `காதல்`;\n- detailed log: `notes/verification-audit-pdf-005-009.md`.\n\n**Next verification range:** PDF 10–14.\n\n'''
    if marker in t: t=t.replace(marker,block+marker,1)
t=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S)
write(rel,t)

# Transcription README
rel='works/naam/transcription/README.md'; t=read(rel)
for old,new,label in [('verified pages: **0**','verified pages: **4**','tr verified'),('visual-fidelity passed pages: **0**','visual-fidelity passed pages: **4**','tr visual'),('historical-glyph final verified pages: **0/67**','historical-glyph final verified pages: **5/67**','tr glyph'),('open uncertainty markers: **2**','open uncertainty markers: **1**','tr uncertainty')]:
    if old in t: t=t.replace(old,new,1)
if 'verification-audit-pdf-005-009.md' not in t:
    t += f'''\n## Verification progress\n\nPDF 5–9 final dual-gate audit is recorded at `../notes/verification-audit-pdf-005-009.md`. PDF 6–9 are VERIFIED; PDF 5 remains on physical-source-damage hold. Current totals: visual **4/67**, glyph-final **5/67**, dual-gate verified **4/67**, open uncertainty **1**.\n\n## Next activity\n\n**{NEXT}**\n'''
else:
    t=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S)
write(rel,t)

# Project handover
rel='works/naam/PROJECT_HANDOVER.md'; t=read(rel)
for old,new in [('canonical Tamil verified: **0/67**','canonical Tamil verified: **4/67**'),('visual fidelity audit: **not-started**','visual fidelity audit: **in progress — 4/67 passed**'),('historical-glyph final verified: **0/67**','historical-glyph final verified: **5/67**'),('open source uncertainty markers: **2**','open source uncertainty markers: **1**')]:
    t=t.replace(old,new,1)
if 'verification-audit-pdf-005-009.md' not in t:
    anchor='- `notes/historical-glyph-audit.md`.'
    if anchor in t: t=t.replace(anchor,anchor+'\n- `notes/verification-audit-pdf-005-009.md`.',1)
t=re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\s*$',f'## Exact next activity\n\n> **{NEXT}**\n',t,count=1,flags=re.S)
write(rel,t)

# Next chat prompt overwrite
write('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages**;\n- visual-fidelity passed: **4/67**;\n- historical-glyph first-pass checked: **67/67**;\n- historical-glyph final verified: **5/67**;\n- dual-gate canonical verified: **4/67** — PDF 6–9;\n- open uncertainty markers: **1** — only PDF 5's physically damaged introductory-line beginning;\n- PDF 9's former uncertainty is resolved as source-visible `குறுக்கொடிய`;\n- structured derivatives / English: **blocked pending verified Tamil**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; canonical screenplay PDF **5–71**.\n\n## Verification checkpoint\n\nPDF 6–9 are frozen as VERIFIED absent genuinely new direct-source evidence. PDF 5 remains held because the source physically loses the beginning of one introductory line; preserve only the surviving tail `…னைத் கொலைத்துவிட சில துரோகிகள் கிளம்பினர்.` and do not reconstruct the missing characters.\n\nScan-backed corrections made in the PDF 5–9 audit include `ஒண்ணுமில்லையப்பா`, occurrence-specific `பூசை`, PDF 8 `உல்லாசத்திலே`, and PDF 9 `வந்திருக்காங்க`, `குறுக்கொடிய`, `ஆரஞ்சுப்பழம்`, `பாட்டாளி`, `காதல்`.\n\nDetailed log: `works/naam/notes/verification-audit-pdf-005-009.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# data/works.json
rel='data/works.json'; d=json.loads(read(rel)); n=next(x for x in d if x.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-pdf-005-009-4-of-67',historical_glyph_audit='final-verification-in-progress-5-of-67',
         canonical_tamil_draft_pages=63,canonical_tamil_verified_pages=4,canonical_tamil_review_pages=63,canonical_tamil_open_uncertainty_markers=1,
         historical_glyph_pages_verified=5,visual_fidelity_passed_pages=4,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-005-009.md',next_action=NEXT)
write(rel,json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')

# Root README lightweight mirror
rel='README.md'; t=read(rel)
t=t.replace('verified pages: **0**; visual-fidelity audit: **not-started**;','verified pages: **4/67**; visual-fidelity audit: **in progress — 4/67**;',1)
t=t.replace('historical-glyph first-pass checked: **67/67**; final glyph-verified: **0/67**;','historical-glyph first-pass checked: **67/67**; final glyph-verified: **5/67**;',1)
t=t.replace('open source uncertainty markers: **2**','open source uncertainty markers: **1**',1)
# replace first Naam Next line after block if possible
pos=t.find('## நாம் status')
if pos>=0:
    end=t.find('\n## ',pos+5)
    if end<0:end=len(t)
    block=t[pos:end]
    block=re.sub(r'\*\*Next:\*\* .*$',f'**Next:** {NEXT}',block,flags=re.M)
    t=t[:pos]+block+t[end:]
write(rel,t)

# Master handover and consistency audit: focused numeric mirrors
for rel in ['docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md','docs/STATUS_CONSISTENCY_AUDIT.md']:
    t=read(rel)
    t=t.replace('verified **0/67**','verified **4/67**')
    t=t.replace('verified pages: **0**','verified pages: **4/67**')
    t=t.replace('visual-fidelity audit: **not-started**','visual-fidelity audit: **in progress — 4/67 passed**')
    t=t.replace('historical-glyph first-pass checked / final verified: **67/67 / 0/67**','historical-glyph first-pass checked / final verified: **67/67 / 5/67**')
    t=t.replace('open source uncertainties: **2**','open source uncertainties: **1**')
    t=t.replace('**2 carried source uncertainties**','**1 remaining source uncertainty**')
    # keep next-action mirror current when a Naam section contains it
    t=t.replace('Begin the separate visual-fidelity and final historical-glyph verification audit with PDF 5–9. Compare every canonical token against enlarged source pixels, preserve source irregularity, and adjudicate the two carried source uncertainties only when direct scan evidence positively supports a reading. Mark a page verified only when both the visual-fidelity and occurrence-specific historical-glyph gates pass; keep any unresolved page/reason explicit. Structured derivatives and English translation remain blocked until verified Tamil.',NEXT)
    write(rel,t)

print('Synchronized Naam verification PDF 5–9:')
for x in changed: print('-',x)
