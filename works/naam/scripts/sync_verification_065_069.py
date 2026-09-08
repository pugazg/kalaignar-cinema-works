#!/usr/bin/env python3
import json,re
from pathlib import Path

R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 70–71. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 or PDF 25–69 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. PDF 70 continues the same scene-45 Kumaran utterance that ends PDF 69 at `படித்தால் பாவம் என்று உன்`; preserve the physical page boundary without duplication or invented completion. PDF 71 closes the canonical main-text range. Preserve only the printed source. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
changed=[]

def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
    q=R/p
    old=q.read_text(encoding='utf-8') if q.exists() else ''
    if old!=s:
        q.parent.mkdir(parents=True,exist_ok=True)
        q.write_text(s,encoding='utf-8')
        changed.append(p)
def one(s,a,b):
    if a not in s: raise SystemExit('missing expected text: '+a)
    return s.replace(a,b,1)
def between(s,a,b,r):
    i=s.find(a); j=s.find(b,i+len(a)) if i>=0 else -1
    if i<0 or j<0: raise SystemExit('missing section: '+a)
    return s[:i]+r.rstrip()+'\n\n'+s[j:]

# Preconditions
ip='works/naam/transcription/index.json'
d=json.loads(rd(ip))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(57,57,60,3)
part='works/naam/transcription/parts/pdf-065-069.md'
s=rd(part)
assert 'Status: `draft / needs-review`' in s
assert 'Historical-glyph first pass: `checked-first-pass`' in s
for pg in range(65,70):
    assert f'pdf={pg} printed={pg} status=draft glyph=checked-first-pass' in s
assert 'உயிலா? இத்தனை நாளும் உன்னிடம் இருந்தது? துரோகி.' in s
assert 'மீனு அவமதிக் கொண்டிருக்கிறாள்' in s
assert s.count('படித்தால் பாவம் என்று உன்')==1

# Canonical PDF 65-69: direct rendered-source corrections and dual-gate promotion.
s=one(s,'# நாம் — canonical Tamil first-pass batch','# நாம் — canonical Tamil verification batch')
s=one(s,'Status: `draft / needs-review`','Status: `verified` — visual-fidelity and final historical-glyph gates PASS for all five pages.')
s=one(s,'Historical-glyph first pass: `checked-first-pass`','Historical-glyph final: `verified-final`')
for pg in range(65,70):
    s=one(s,f'pdf={pg} printed={pg} status=draft glyph=checked-first-pass',f'pdf={pg} printed={pg} status=verified glyph=verified-final')
s=one(s,'உயிலா? இத்தனை நாளும் உன்னிடம் இருந்தது? துரோகி.','உயிலா? இத்தனை நாளும் உன்னிடமா இருந்தது? துரோகி.')
s=one(s,'மீனு அவமதிக் கொண்டிருக்கிறாள்','மீனு அவமதிக்கொண்டிருக்கிறாள்')
marker='\n---\n\n## First-pass audit notes\n'
i=s.find(marker)
if i<0: raise SystemExit('missing first-pass audit tail')
s=s[:i]+'''\n---\n\n## Verification audit notes\n\n- PDF 65–69: **5/5 visual-fidelity PASS; 5/5 historical-glyph final PASS; 5/5 dual-gate VERIFIED**.\n- Direct scan corrections on PDF 68: `உன்னிடம் இருந்தது?` → `உன்னிடமா இருந்தது?`; `அவமதிக் கொண்டிருக்கிறாள்` → `அவமதிக்கொண்டிருக்கிறாள்`.\n- Historical-glyph final positives: PDF 65 `மனிதனாகுகிறதும்` / `மனிதனாகுவதும்` (`னா`) and `அண்ணுமலை` (`லை`); PDF 66 `காலணா` (`ணா`) / `காலை` (`லை`); PDF 67 `மனைவி` (`னை`); PDF 68 `உயிலை` (`லை`); PDF 69 `உன்னை` (`னை`).\n- Source anomaly `உன்மீனு` on PDF 66 is preserved exactly. PDF 69 ends mid-Kumaran utterance at `படித்தால் பாவம் என்று உன்`; PDF 70 must continue the same utterance without duplication or invented completion.\n- PDF 65–69 adds **0** new source uncertainty markers. Repository-wide holds remain PDF 5, PDF 10 and PDF 24; PDF 9 remains resolved as `குறுக்கொடிய`.\n- Next verification batch: **PDF 70–71**.\n'''
wr(part,s)

# Batch audit.
audit='''# நாம் — visual-fidelity + final historical-glyph verification audit — PDF 65–69\n\nSource: `TVA_BOK_0064201_நாம்.pdf`  \nRange: **PDF 65–69**  \nAudit mode: **dual gate — rendered-pixel lexical fidelity + occurrence-specific historical-glyph verification**  \nResult: **PDF 65–69 PASS / VERIFIED; 5/5 dual-gate verified**.\n\nThe rendered scan is controlling. No OCR, film audio, subtitles, later edition, web text or semantic reconstruction is textual authority.\n\n## PDF 65 — PASS / VERIFIED\n\nThe full page is source-aligned with no canonical correction required. Source-period and colloquial forms are retained, including the rhetoric around `மனிதனே கடவுளாகுகிறதும்`, `கடவுள் மனிதனாகுகிறதும்`, the `காளி பாபா` passage, and `வருமானத்திலேபாதி`. Historical `னா` identity is final-verified in `மனிதனாகுகிறதும்` / `மனிதனாகுவதும்`; `அண்ணுமலை` is final-verified as historical `லை`. Historical-glyph final review: **PASS**.\n\n## PDF 66 — PASS / VERIFIED\n\nThe page is source-aligned with no canonical correction required. The printed speaker-label anomaly `உன்மீனு` is retained exactly; it is not normalized to `மீனு`. The embedded Sundari letter remains distinct from dialogue. `காலணா` is final-verified as historical `ணா`; `காலை` in `சீ...தொடாதே காலை!` is final-verified as historical `லை`. Historical-glyph final review: **PASS**.\n\n## PDF 67 — PASS / VERIFIED\n\nThe page is source-aligned with no canonical correction required. Source-colloquial `ஓங்க அப்பா ஜமீன்தார்!` is retained, and the scene-42/43 transition remains source-bound. `மனைவி` is final-verified as a historical `னை` occurrence. Historical-glyph final review: **PASS**.\n\n## PDF 68 — PASS / VERIFIED\n\nTwo direct source corrections are required. Malaiyappan's line prints **`உன்னிடமா இருந்தது?`**, not first-pass `உன்னிடம் இருந்தது?`; the scene-45 parenthetical prints **`அவமதிக்கொண்டிருக்கிறாள்`** as one source word, not first-pass `அவமதிக் கொண்டிருக்கிறாள்`. The source-irregular `நம்முடைய காமவினையைப்போக்க` and `காளிபாபாவின்` remain untouched. `உயிலை` is final-verified as historical `லை`. Historical-glyph final review: **PASS**.\n\n## PDF 69 — PASS / VERIFIED\n\nThe page is source-aligned with no canonical correction required. Kumaran's hunter/tiger analogy is preserved exactly as the booklet witness. `உன்னை` is final-verified as historical `னை`. The physical page boundary is retained: PDF 69 ends mid-Kumaran utterance at **`படித்தால் பாவம் என்று உன்`**; no completion is inferred from context, and PDF 70 must continue the same utterance. Historical-glyph final review: **PASS**.\n\n## Batch result\n\n| PDF | Visual fidelity | Historical glyph final | Dual-gate status | Open uncertainty |\n|---:|---|---|---|---:|\n| 65 | PASS | PASS | VERIFIED | 0 |\n| 66 | PASS | PASS | VERIFIED | 0 |\n| 67 | PASS | PASS | VERIFIED | 0 |\n| 68 | PASS after 2 corrections | PASS | VERIFIED | 0 |\n| 69 | PASS | PASS | VERIFIED | 0 |\n| **Total** | **5 PASS** | **5 PASS** | **5 VERIFIED** | **0** |\n\nPDF 65–69 introduces no new source uncertainty. Repository-wide holds remain **PDF 5, PDF 10 and PDF 24**; PDF 9 remains resolved as `குறுக்கொடிய`.\n\nAfter synchronization the checkpoint is: first pass **67/67 COMPLETE**; visual-fidelity **62/67**; historical-glyph final **65/67**; dual-gate verified **62/67**; review **5/67**; open source uncertainties **3**.\n\n## Next activity\n\nProceed with dual-gate verification for **PDF 70–71**. PDF 70 must continue the PDF 69 Kumaran utterance without duplication or invented completion. Do not reopen already verified pages absent genuinely new direct-source evidence. Keep PDF 5, PDF 10 and PDF 24 as explicit source-obscuration holds. Structured derivatives and English remain blocked until verified Tamil closes.\n'''
wr('works/naam/notes/verification-audit-pdf-065-069.md',audit)

# Index.
d.update(draft_pages=5,verified_pages=62,visual_fidelity_passed_pages=62,historical_glyph_verified_pages=65,review_pages=5,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
    if x['path']=='parts/pdf-065-069.md':
        x.update(status='verified',historical_glyph_status='verified-final',open_uncertainties=0)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# Metadata.
p='works/naam/metadata.yaml'; s=rd(p)
for a,b in [
    ('  draft_pages: 10','  draft_pages: 5'),
    ('  verified_pages: 57','  verified_pages: 62'),
    ('  review_pages: 10','  review_pages: 5'),
    ('  pages_verified: 60','  pages_verified: 65'),
    ('  visual_fidelity_audit: in-progress-through-pdf-064-57-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-069-62-of-67-pass'),
    ('  historical_glyph_audit: final-verification-in-progress-60-of-67','  historical_glyph_audit: final-verification-in-progress-65-of-67')
]:
    if a in s: s=s.replace(a,b,1)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-065-069.md"\n  visual_fidelity_passed_pages: 62\n  historical_glyph_final_verified_pages: 65\n  dual_gate_verified_pages: 62\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "70-71"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S)
wr(p,s)

# Historical-glyph work audit.
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 65–69 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 65–69 | 5 | 5 | 5 | 0 | final-audit: 5 verified |')
s=one(s,'| **Total** | **67** | **67** | **57** | **10** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **62** | **5** | **final-verification-in-progress** |')
for n in range(65,70):
    s=re.sub(rf'(^\| {n} \|.*?\| )draft-supported( \|$)',rf'\1**final-verified**\2',s,flags=re.M)
if '## PDF 65–69 final dual-gate audit' not in s:
    tail='Next final audit range: **PDF 65–69**.'
    pos=s.rfind(tail)
    if pos<0: raise SystemExit('missing PDF65-69 next-range tail')
    block='''## PDF 65–69 final dual-gate audit\n\n- visual-fidelity / historical-glyph final: **5/5 PASS / 5/5 PASS**;\n- dual-gate canonical: **5/5 VERIFIED**;\n- direct scan corrections are confined to PDF 68: `உன்னிடம் இருந்தது?` → `உன்னிடமா இருந்தது?` and `அவமதிக் கொண்டிருக்கிறாள்` → `அவமதிக்கொண்டிருக்கிறாள்`;\n- final glyph cases include PDF 65 `மனிதனாகுகிறதும்` / `மனிதனாகுவதும்` (`னா`) and `அண்ணுமலை` (`லை`); PDF 66 `காலணா` (`ணா`) / `காலை` (`லை`); PDF 67 `மனைவி` (`னை`); PDF 68 `உயிலை` (`லை`); PDF 69 `உன்னை` (`னை`);\n- PDF 66 source anomaly `உன்மீனு` remains exact; PDF 69 closes mid-utterance at `படித்தால் பாவம் என்று உன்`;\n- no new uncertainty; PDF 5, PDF 10 and PDF 24 remain the only source-obscuration holds;\n- details: `verification-audit-pdf-065-069.md`.\n\nNext final audit range: **PDF 70–71**.'''
    s=s[:pos]+block+s[pos+len(tail):]
wr(p,s)

# Machine-wide work mirror.
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-069-62-of-67',historical_glyph_audit='final-verification-in-progress-65-of-67',canonical_tamil_draft_pages=5,canonical_tamil_verified_pages=62,canonical_tamil_review_pages=5,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=65,visual_fidelity_passed_pages=62,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-065-069.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')

# Work README.
p='works/naam/README.md'; s=rd(p)
for a,b in [
    ('canonical Tamil verified pages: **57/67**','canonical Tamil verified pages: **62/67**'),
    ('visual fidelity audit: **in progress — 57/67 pages passed**','visual fidelity audit: **in progress — 62/67 pages passed**'),
    ('historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 60/67 final-verified**','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 65/67 final-verified**'),
    ('dual-gate verification pass is in progress: **57/67** pages are now verified;','dual-gate verification pass is in progress: **62/67** pages are now verified;'),
    ('**57/67** canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–64.','**62/67** canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–69.')
]:
    if a in s: s=s.replace(a,b,1)
sec='''## Verification audit — through PDF 69\n\n- PDF 6–9, PDF 11–23 and PDF 25–69: **dual-gate VERIFIED — 62/67 total**;\n- PDF 5 / PDF 10: **HOLD** for physical source loss; PDF 24: **HOLD** for later ink/mark obscuring the post-`தே` printed glyph;\n- visual-fidelity passed: **62/67**; historical-glyph final verified: **65/67**;\n- open source uncertainties: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 65–69: **5/5 VERIFIED**, no new uncertainty;\n- direct PDF 68 corrections: `உன்னிடம் இருந்தது?` → `உன்னிடமா இருந்தது?`; `அவமதிக் கொண்டிருக்கிறாள்` → `அவமதிக்கொண்டிருக்கிறாள்`;\n- detailed audit: `notes/verification-audit-pdf-065-069.md`.\n\n**Next verification range:** PDF 70–71.\n'''
if '## Verification audit — through PDF 64' in s:
    s=between(s,'## Verification audit — through PDF 64','## Song / verse / performance structures mapped or confirmed so far',sec)
s=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S)
wr(p,s)

# Transcription README.
p='works/naam/transcription/README.md'; s=rd(p)
for a,b in [
    ('- verified pages: **57**;','- verified pages: **62**;'),
    ('- separate visual-fidelity audit: **in progress — 57/67 passed**;','- separate visual-fidelity audit: **in progress — 62/67 passed**;'),
    ('- historical-glyph final verified pages: **60/67**;','- historical-glyph final verified pages: **65/67**;')
]:
    if a in s: s=s.replace(a,b,1)
if '## Verification audit — PDF 65–69' not in s:
    marker='## PDF 70–71 source decisions'
    block='''## Verification audit — PDF 65–69\n\nPDF 65–69 are **5/5 VERIFIED** after direct rendered-source comparison. Two corrections are confined to PDF 68: `உன்னிடம் இருந்தது?` → `உன்னிடமா இருந்தது?`, and `அவமதிக் கொண்டிருக்கிறாள்` → `அவமதிக்கொண்டிருக்கிறாள்`. Historical-glyph final positives are `மனிதனாகுகிறதும்` / `மனிதனாகுவதும்` (`னா`), `அண்ணுமலை` / `காலை` / `உயிலை` (`லை`), `காலணா` (`ணா`), and `மனைவி` / `உன்னை` (`னை`). PDF 69 ends at `படித்தால் பாவம் என்று உன்` and must continue on PDF 70. Current totals: visual **62/67**, glyph-final **65/67**, dual-gate verified **62/67**, open uncertainties **3**. Detailed log: `../notes/verification-audit-pdf-065-069.md`.\n\n'''
    if marker in s: s=s.replace(marker,block+marker,1)
s=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',s,count=1,flags=re.S)
wr(p,s)

# Project handover.
p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
for a,b in [
    ('canonical Tamil verified: **57/67**','canonical Tamil verified: **62/67**'),
    ('visual fidelity audit: **in progress — 57/67 passed**','visual fidelity audit: **in progress — 62/67 passed**'),
    ('historical-glyph final verified: **60/67**','historical-glyph final verified: **65/67**')
]:
    if a in s: s=s.replace(a,b,1)
if '- `notes/verification-audit-pdf-065-069.md`.' not in s:
    prev='- `notes/verification-audit-pdf-060-064.md`.'
    if prev in s: s=s.replace(prev,prev+'\n- `notes/verification-audit-pdf-065-069.md`.',1)
i=s.find('## Verification checkpoint through PDF 64')
if i>=0:
    s=s[:i]+f'''## Verification checkpoint through PDF 69\n\n- PDF 6–9, PDF 11–23 and PDF 25–69: **VERIFIED — 62/67 total**;\n- PDF 5 / PDF 10 remain physical-source-damage holds; PDF 24 remains a later-ink/mark source-obscuration hold;\n- visual-fidelity: **62/67**; glyph-final: **65/67**; dual-gate: **62/67**;\n- open source uncertainties: **3**;\n- PDF 65–69 is fully verified and adds no uncertainty; PDF 68 has two direct source corrections (`உன்னிடமா`, `அவமதிக்கொண்டிருக்கிறாள்`).\n\n## Exact next activity\n\n> **{NEXT}**\n'''
wr(p,s)

# Next prompt.
wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCurrent durable checkpoint: first pass **67/67 COMPLETE**; visual-fidelity **62/67**; historical-glyph final **65/67**; dual-gate verified **62/67** (PDF 6–9, PDF 11–23, PDF 25–69); open source holds **3** — PDF 5, PDF 10, PDF 24. PDF 9 is resolved as `குறுக்கொடிய`. PDF 24 scene 11 remains directly readable only through visible `கெளரவம் தே… இருப்பது`; do not restore `தேடி` without new direct-source evidence. PDF 68 has direct source corrections `உன்னிடமா இருந்தது?` and `அவமதிக்கொண்டிருக்கிறாள்`. Structured derivatives and English remain blocked.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\nDetailed current audit: `works/naam/notes/verification-audit-pdf-065-069.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Root README.
p='README.md'; s=rd(p)
sec=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake/map and first-pass Tamil are complete; dual-gate verification is in progress.\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **62/67 / 62/67**;\n- historical-glyph first-pass / final: **67/67 / 65/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-065-069.md`;\n- derivatives / English remain blocked pending verified Tamil.\n\n**Next:** {NEXT}\n'''
s=between(s,'## நாம் status','## ராஜா ராணி status',sec)
wr(p,s)

# Master handover.
p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=re.sub(r'- \*\*Naam / நாம்\*\* — active work;.*','- **Naam / நாம்** — active work; first pass **67/67 COMPLETE**; dual-gate **62/67**; visual **62/67**; glyph-final **65/67**; source holds PDF 5 / PDF 10 / PDF 24; downstream blocked.',s,count=1)
sec=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **62/67 / 62/67**;\n- historical-glyph first-pass / final: **67/67 / 65/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- current audit: `works/naam/notes/verification-audit-pdf-065-069.md`;\n- structured derivatives / English / reader remain blocked.\n\n**Exact next activity:** {NEXT}\n'''
s=between(s,'## 8. Naam active checkpoint','## 9. Ammayappan closed checkpoint',sec)
wr(p,s)

# Repository status consistency mirror.
p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
r='**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** has first pass **67/67 COMPLETE**, dual-gate verification **62/67**, visual-fidelity **62/67**, historical-glyph final **65/67**, and **3 source-obscuration holds** (PDF 5, PDF 10, PDF 24). PDF 65–69 is fully verified and adds no uncertainty.'
s=re.sub(r'\*\*PASS for the current repository-wide checkpoint\.\*\*.*?\n\n',r+'\n\n',s,count=1,flags=re.S)
s=re.sub(r'\| Naam / நாம் \|.*','| Naam / நாம் | first pass 67/67 COMPLETE; dual-gate 62/67; 3 source holds | 45 scenes mapped; derivatives blocked | not-started | not-started |',s,count=1)
sec=f'''## Naam current checkpoint\n\n- first pass: **67/67 COMPLETE**;\n- dual-gate verified / visual-fidelity: **62/67 / 62/67**;\n- historical-glyph first-pass / final: **67/67 / 65/67**;\n- open source holds: **3** — PDF 5, PDF 10, PDF 24;\n- PDF 65–69: **5/5 VERIFIED**;\n- current audit: `works/naam/notes/verification-audit-pdf-065-069.md`;\n- downstream layers remain blocked.\n\n**Next production phase:** {NEXT}\n'''
s=between(s,'## Naam current checkpoint','## Ammayappan current checkpoint',sec)
i=s.find('## Conclusion')
if i>=0:
    s=s[:i]+'''## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** is active with first pass **67/67 COMPLETE**, dual-gate **62/67**, visual **62/67**, glyph-final **65/67**, and source holds on PDF 5, PDF 10 and PDF 24. Next verification batch: **PDF 70–71**.\n'''
wr(p,s)

print('\n'.join(changed))
