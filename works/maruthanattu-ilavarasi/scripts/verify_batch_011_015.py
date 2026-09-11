#!/usr/bin/env python3
from pathlib import Path
import json, re

R=Path('.')
W=R/'works'/'maruthanattu-ilavarasi'
T=W/'transcription'
P=T/'pages'
N=W/'notes'
idxp=T/'index.json'
idx=json.loads(idxp.read_text(encoding='utf-8'))

assert idx['visual_verified_pages']==10
assert idx['historical_glyph_final_verified_pages']==10
assert idx['draft_pages']==11
assert idx['open_uncertainty_markers']==0
assert all(r['status']=='verified' for r in idx['page_records'][:10])
assert all(r['status']=='draft' for r in idx['page_records'][10:])

corrections={
'pages/012.md':[
('பழக்கொலை நீ!','பழக்கொடி நீ!'),
],
'pages/014.md':[
('அரசே இவன் கைது செய்த அத்தனை சிப்பாய்களையும் கேளுங்கள்.','அரசே இவனை கைது செய்த அத்தனை சிப்பாய்களையும் கேளுங்கள்.'),
],
'pages/016.md':[
('இவன் கைது செய்த அத்தனை சிப்பாய்களுக்கும் தெரியாமல்','இவனை கைது செய்த அத்தனை சிப்பாய்களுக்கும் தெரியாமல்'),
('அந்த சுத்தவீரன் இவனே கொன்றிருந்தால்!','அந்த சுத்தவீரனை இவனே கொன்றிருந்தால்!'),
('இந்நாட்டு மக்கள் காட்டு மிருகம்போல் நடத்தியது','இந்நாட்டு மக்களை காட்டு மிருகம்போல் நடத்தியது'),
],
}
applied=[]
for rel,reps in corrections.items():
    fp=T/rel
    s=fp.read_text(encoding='utf-8')
    for old,new in reps:
        if old not in s:
            raise SystemExit(f'expected V3 source text absent in {rel}: {old}')
        s=s.replace(old,new,1)
        applied.append((rel,old,new))
    fp.write_text(s,encoding='utf-8')

# Verify logical printed pages 11-15 and update source anchors.
for rec in idx['page_records']:
    p=rec['printed_page']
    if 11 <= p <= 15:
        rec['status']='verified'
        fp=T/rec['path']
        lines=fp.read_text(encoding='utf-8').splitlines()
        if not lines or not lines[0].startswith('<!-- source:'):
            raise SystemExit(f'missing source anchor {fp}')
        lines[0]=lines[0].replace('status=draft','status=verified')
        fp.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

idx.update({
    'status':'verification-in-progress',
    'draft_pages':6,
    'visual_verified_pages':15,
    'historical_glyph_final_verified_pages':15,
    'verification_current_through_logical_printed':15,
    'verification_batches_completed':3,
    'open_uncertainty_markers':0,
    'next_action':'Independently verify logical printed pages 16–20 as the next five-page dual-gate batch. Use representative source pixels PDF 17 left/right (printed 16–17), PDF 19 left/right (printed 18–19), and PDF 21 left (printed 20); PDFs 18,20,22 are exact duplicate spreads. Correct any draft mismatch before marking verified, perform final historical-glyph checks occurrence by occurrence, and keep structured derivatives blocked until all 21 logical pages pass both gates.'
})
idxp.write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Fidelity audit: append V3 without disturbing V1/V2 history.
fa=N/'fidelity-audit.md'
s=fa.read_text(encoding='utf-8')
s=re.sub(r'^Status: \*\*IN PROGRESS — \d+/21 canonical logical pages VERIFIED\*\*\.$',
         'Status: **IN PROGRESS — 15/21 canonical logical pages VERIFIED**.',s,count=1,flags=re.M)
if '## V3 — logical printed pages 11–15' not in s:
    s=s.rstrip()+'''\n\n## V3 — logical printed pages 11–15\n\nRepresentative pixels independently re-read:\n\n- printed 11 — PDF 11 right; PDF 12 duplicate;\n- printed 12–13 — PDF 13 left/right; PDF 14 duplicate;\n- printed 14–15 — PDF 15 left/right; PDF 16 duplicate.\n\n**PASS after 5 source-supported corrections / 0 unresolved:**\n\n1. printed 11: `பழக்கொலை நீ!` → source-visible `பழக்கொடி நீ!`;\n2. printed 13: `இவன் கைது செய்த` → `இவனை கைது செய்த`;\n3. printed 15: `இவன் கைது செய்த` → `இவனை கைது செய்த`;\n4. printed 15: `அந்த சுத்தவீரன் இவனே` → `அந்த சுத்தவீரனை இவனே`;\n5. printed 15: `இந்நாட்டு மக்கள் காட்டு மிருகம்போல்` → `இந்நாட்டு மக்களை காட்டு மிருகம்போல்`.\n\nThe same independent re-read completed the final historical-glyph check for logical pages 11–15. No unresolved source reading remains in V3.\n\nNext: logical printed pages **16–20**.\n'''
fa.write_text(s,encoding='utf-8')

(N/'historical-glyph-audit.md').write_text('''# மருதநாட்டு இளவரசி — historical Tamil glyph audit

Status: **PROSPECTIVE 21/21 COMPLETE; FINAL INDEPENDENT VERIFICATION 15/21 PASS**.

Source pixels control historical glyph identity. OCR/extraction is candidate-only; no global replacements or silent modernization are allowed.

- logical pages 1–5: **FINAL GLYPH PASS**;
- logical pages 6–10: **FINAL GLYPH PASS**;
- logical pages 11–15: **FINAL GLYPH PASS**;
- logical pages 16–21: pending;
- final historical-glyph verification: **15/21**;
- open uncertainty markers: **0**.

V3 independently re-read the source-visible accusative endings and word forms that differed from the first-pass candidate, including `இவனை`, `சுத்தவீரனை`, and `மக்களை`, without grammatical normalization beyond what the source itself shows.
''',encoding='utf-8')

(T/'README.md').write_text('''# மருதநாட்டு இளவரசி — canonical Tamil transcription

Status: **T1 COMPLETE; INDEPENDENT DUAL-GATE VERIFICATION IN PROGRESS — 15/21 VERIFIED**.

All 21 logical printed pages are present. Logical pages **1–15** have passed independent visual-fidelity and final historical-glyph verification; logical pages **16–21** remain draft. Open uncertainty markers: **0**.

Corrected source geometry remains: PDF 2 is unique; exact duplicate spreads are **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22**. Canonical records use representative PDFs 2,3,5,7,9,11,13,15,17,19,21.

User/source corrections retained include logical page 1 `தங்கையின் குழந்தை தரணி ஆளவேண்டுமே` and logical page 3 `இத்தியாகம் செய்யத்தான் வேண்டும்;`. V3 pages 11–15 required five additional source-supported corrections; see `notes/fidelity-audit.md`.

**Next:** independently verify logical printed pages **16–20** using PDF 17 left/right, PDF 19 left/right and PDF 21 left. Structured derivatives remain blocked until 21/21 dual-gate closure.
''',encoding='utf-8')

(W/'README.md').write_text('''# மருதநாட்டு இளவரசி

Source-led archival workspace for the scanned **`மருதநாட்டு இளவரசி`** திரை வசனம் booklet.

## Source authority

Controlling source: `TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**. The scan is canonical authority and is not committed.

Printed credit: `வசனம் : மு. கருணாநிதி.`. No explicit edition statement or publication year was observed.

## Source geometry

PDF 2 is unique. Thereafter the PDF contains exact duplicate two-page spread pairs: **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22**. Canonical logical pages 1–21 use representative PDFs **2,3,5,7,9,11,13,15,17,19,21** exactly once.

The opening logical pages 1–3 are unnumbered; no `காட்சி 1.` is invented. Source-numbered headings are 2 through 10.

## Current gate

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- independent visual fidelity: **15/21 PASS**;
- final historical-glyph verification: **15/21 PASS**;
- remaining draft pages: **6**;
- open uncertainty markers: **0**;
- structured scene/dialogue/character/song/English layers: **BLOCKED**.

User/source corrections retained: logical page 1 `தங்கையின் குழந்தை தரணி ஆளவேண்டுமே`; logical page 3 `இத்தியாகம் செய்யத்தான் வேண்டும்;`. V3 logical pages 11–15 passed after five source-supported corrections recorded in `notes/fidelity-audit.md`.

## Exact next activity

> **Independently verify logical printed pages 16–20 using representative PDF 17 left/right, PDF 19 left/right and PDF 21 left; PDFs 18,20,22 are duplicate spreads. Correct any mismatch before verification, complete final historical-glyph checks, and keep structured derivatives blocked until 21/21 dual-gate closure.**
''',encoding='utf-8')

(W/'PROJECT_HANDOVER.md').write_text('''# மருதநாட்டு இளவரசி — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/maruthanattu-ilavarasi/`

**LIVE MAIN IS AUTHORITATIVE.**

Source: `TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**.

## Durable state

- intake / mapping: **COMPLETE / COMPLETE-VERIFIED-CORRECTED**;
- duplicate pattern: **3=4 through 21=22** in odd/even pairs; PDF 2 unique;
- canonical logical pages: **21**;
- source headings: **2–10**; logical pages 1–3 unnumbered;
- Tamil T1: **21/21 COMPLETE-DRAFT**;
- visual fidelity: **15/21 PASS**;
- final historical-glyph verification: **15/21 PASS**;
- remaining draft pages: **6**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

User/source corrections retained: logical page 1 `தங்கையின் குழந்தை தரணி ஆளவேண்டுமே`; logical page 3 `இத்தியாகம் செய்யத்தான் வேண்டும்;`. V3 logical pages 11–15 passed after five source-pixel corrections.

## Exact next activity

> **Independently verify logical printed pages 16–20 using PDF 17 left/right, PDF 19 left/right and PDF 21 left; PDFs 18,20,22 are duplicates. Correct any mismatch first, complete final historical-glyph checks, and keep derivatives blocked until 21/21 closure.**
''',encoding='utf-8')

(W/'NEXT_CHAT_PROMPT.md').write_text('''# Next Chat Prompt — மருதநாட்டு இளவரசி / verification logical pages 16–20

Continue in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/maruthanattu-ilavarasi/`. **LIVE MAIN IS AUTHORITATIVE.**

Current durable state: Tamil T1 **21/21 complete-draft**; visual fidelity **15/21 verified**; final historical-glyph verification **15/21 verified**; open uncertainties **0**; structured derivatives **BLOCKED**.

User/source corrections already applied:
- logical page 1: `தங்கையின் குழந்தை தரணி ஆளவேண்டுமே`;
- logical page 3: `இத்தியாகம் செய்யத்தான் வேண்டும்;`.

Physical source geometry: PDF 2 unique; duplicate spreads **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22**.

> **Next batch: independently re-read logical printed pages 16–20 against representative PDF 17 left/right, PDF 19 left/right and PDF 21 left. Treat PDFs 18,20,22 as provenance-only duplicate spreads. Correct any mismatch first; then mark only passing pages verified and advance both final counters to 20/21. Do not begin structured derivatives.**
''',encoding='utf-8')

# metadata.yaml counters/current action
mp=W/'metadata.yaml'; m=mp.read_text(encoding='utf-8')
for pattern,replacement in [
(r'^visual_fidelity_audit:.*$','visual_fidelity_audit: in-progress-15-of-21'),
(r'^historical_glyph_audit:.*$','historical_glyph_audit: final-in-progress-15-of-21'),
(r'^next_action:.*$','next_action: "Independently verify logical printed pages 16–20; then advance both dual-gate counters to 20/21 if PASS."'),
(r'^visual_verified_pages:.*$','visual_verified_pages: 15'),
(r'^historical_glyph_final_verified_pages:.*$','historical_glyph_final_verified_pages: 15'),
(r'^verification_current_through_logical_printed:.*$','verification_current_through_logical_printed: 15'),
]:
    m,n=re.subn(pattern,replacement,m,count=1,flags=re.M)
    if n!=1: raise SystemExit(f'metadata pattern not found: {pattern}')
mp.write_text(m,encoding='utf-8')

# data/works.json
wp=R/'data'/'works.json'
works=json.loads(wp.read_text(encoding='utf-8'))
rec=next(x for x in works if x.get('id')=='maruthanattu-ilavarasi')
rec.update({
'tamil_transcription_draft_pages':6,
'tamil_transcription_verified_pages':15,
'tamil_fidelity_audit':'in-progress-15-of-21',
'historical_glyph_audit':'final-in-progress-15-of-21',
'total_verified_pages':15,
'total_review_pages':0,
'next_action':'Independently verify logical printed pages 16–20 using representative PDF 17/19/21 sides; keep structured derivatives blocked until 21/21 dual-gate closure.'
})
wp.write_text(json.dumps(works,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Root README current work section.
rp=R/'README.md'; rt=rp.read_text(encoding='utf-8')
a=rt.index('## மருதநாட்டு இளவரசி status'); b=rt.index('## வண்டிக்காரன் மகன் status',a)
sec='''## மருதநாட்டு இளவரசி status

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- corrected physical geometry: PDF 2 unique; duplicate spreads **3=4 through 21=22**;
- visual fidelity / final glyph verification: **15/21 / 15/21 PASS**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

**Next:** logical printed pages **16–20** dual-gate verification.

'''
rp.write_text(rt[:a]+sec+rt[b:],encoding='utf-8')

# Master handover current section.
hp=R/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; ht=hp.read_text(encoding='utf-8')
marker='## 11. மருதநாட்டு இளவரசி active checkpoint'; pos=ht.rfind(marker)
if pos<0: raise SystemExit('master handover marker missing')
hp.write_text(ht[:pos]+'''## 11. மருதநாட்டு இளவரசி active checkpoint

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- duplicate-spread provenance: **3=4 through 21=22**, PDF 2 unique;
- visual fidelity / final glyph: **15/21 / 15/21 PASS**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

**Next:** independently verify logical printed pages **16–20**.
''',encoding='utf-8')

# Status consistency audit.
sp=R/'docs'/'STATUS_CONSISTENCY_AUDIT.md'; st=sp.read_text(encoding='utf-8')
row='| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி | **Tamil T1 21/21 complete-draft; visual 15/21; final glyph 15/21; 0 open** | headings **2–10**; duplicate-spread provenance corrected | not-started | not-started |'
st,n=re.subn(r'^\| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி \|.*$',row,st,count=1,flags=re.M)
if n!=1: raise SystemExit('status matrix row missing')
marker='## Maruthanattu Ilavarasi current checkpoint'; pos=st.rfind(marker)
if pos<0: raise SystemExit('status checkpoint marker missing')
sp.write_text(st[:pos]+'''## Maruthanattu Ilavarasi current checkpoint

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- source geometry: PDF 2 unique; duplicate spreads **3=4 through 21=22**;
- visual fidelity / final historical glyph: **15/21 / 15/21 PASS**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

Next: logical pages **16–20** dual-gate verification.
''',encoding='utf-8')

# Normalize touched markdown and fail-closed QA.
for fp in [fa,N/'historical-glyph-audit.md',T/'README.md',W/'README.md',W/'PROJECT_HANDOVER.md',W/'NEXT_CHAT_PROMPT.md',rp,hp,sp]:
    s=fp.read_text(encoding='utf-8')
    fp.write_text('\n'.join(line.rstrip() for line in s.splitlines()).rstrip()+'\n',encoding='utf-8')

idx2=json.loads(idxp.read_text(encoding='utf-8'))
assert idx2['visual_verified_pages']==15
assert idx2['historical_glyph_final_verified_pages']==15
assert idx2['draft_pages']==6
assert idx2['open_uncertainty_markers']==0
assert [r['status'] for r in idx2['page_records'][:15]]==['verified']*15
assert all(r['status']=='draft' for r in idx2['page_records'][15:])
assert len(applied)==5
for r in idx2['page_records'][10:15]:
    first=(T/r['path']).read_text(encoding='utf-8').splitlines()[0]
    assert 'status=verified' in first
print('Maruthanattu Ilavarasi V3 QA PASS: logical 11-15 visual+glyph verified; 5 corrections; 0 unresolved.')
