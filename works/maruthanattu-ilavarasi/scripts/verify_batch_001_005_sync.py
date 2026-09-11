#!/usr/bin/env python3
from pathlib import Path
import json, re

R=Path('.'); W=R/'works'/'maruthanattu-ilavarasi'; T=W/'transcription'; N=W/'notes'
idx=json.loads((T/'index.json').read_text(encoding='utf-8'))
assert idx['visual_verified_pages']==5 and idx['historical_glyph_final_verified_pages']==5
assert idx['draft_pages']==16 and idx['open_uncertainty_markers']==0
assert idx['canonical_representative_pdf_pages']==[2,3,5,7,9,11,13,15,17,19,21]
assert len(idx['duplicate_pdf_spreads'])==10
assert [r['status'] for r in idx['page_records'][:5]]==['verified']*5
assert all(r['status']=='draft' for r in idx['page_records'][5:])

mapping='''# மருதநாட்டு இளவரசி — structural mapping

Status: **COMPLETE-VERIFIED-CORRECTED — full duplicate-spread geometry established during independent verification**.

Rendered source pixels control. The independent V1 re-read established the actual physical scan geometry:

- PDF 1 — cover.
- PDF 2 — unique scan; logical printed page 1 is on the right.
- PDF 3=4 — exact duplicate spread, printed 2–3.
- PDF 5=6 — printed 4–5.
- PDF 7=8 — printed 6–7.
- PDF 9=10 — printed 8–9.
- PDF 11=12 — printed 10–11.
- PDF 13=14 — printed 12–13.
- PDF 15=16 — printed 14–15.
- PDF 17=18 — printed 16–17.
- PDF 19=20 — printed 18–19.
- PDF 21=22 — printed 20–21.

Canonical Tamil represents logical printed pages **1–21 exactly once**, using representative PDFs **2,3,5,7,9,11,13,15,17,19,21**. The following even-numbered scan in each duplicate pair is provenance-only. Stable page-record filenames are retained; index entries and source anchors carry corrected PDF + side provenance.

## Scene-heading provenance

| Scene | Logical printed | Representative source |
|---:|---:|---|
| 2 | 4 | PDF 5 left |
| 3 | 5 | PDF 5 right |
| 4 | 7 | PDF 7 right |
| 5 | 7 | PDF 7 right |
| 6 | 8 | PDF 9 left |
| 7 | 10 | PDF 11 left |
| 8 | 12 | PDF 13 left |
| 9 | 17 | PDF 17 right |
| 10 | 18 | PDF 19 left |

Logical pages 1–3 remain an **unnumbered opening**; no source \`காட்சி 1.\` is invented. The source-visible numbered sequence is 2–10.

## Gate state

- source intake: **COMPLETE**;
- structural mapping: **COMPLETE-VERIFIED-CORRECTED**;
- Tamil T1: **21/21 COMPLETE-DRAFT**;
- independent visual fidelity: **5/21 PASS**;
- final historical-glyph verification: **5/21 PASS**;
- open uncertainty markers: **0**;
- structured derivatives: **BLOCKED**.
'''
(W/'mapping.md').write_text(mapping,encoding='utf-8')

(N/'duplicate-scan-correction.md').write_text('''# மருதநாட்டு இளவரசி — duplicate-spread correction

Independent source rendering during V1 established the complete physical pattern: PDF 2 is unique; thereafter **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22** are exact duplicate two-page spreads.

Canonical logical pages 1–21 therefore use representative PDFs **2,3,5,7,9,11,13,15,17,19,21**, split left/right where applicable. Duplicate scans contribute provenance only and never duplicate canonical text.

This supersedes the earlier one-PDF-page/one-printed-page assumption. The correction was made before structured derivatives opened.
''',encoding='utf-8')

(N/'fidelity-audit.md').write_text('''# மருதநாட்டு இளவரசி — visual-fidelity audit

Status: **IN PROGRESS — 5/21 canonical logical pages VERIFIED**.

## V1 — logical printed pages 1–5

Representative pixels independently re-read: printed 1 = PDF 2 right; printed 2–3 = PDF 3 left/right (PDF 4 duplicate); printed 4–5 = PDF 5 left/right (PDF 6 duplicate).

**PASS after 8 source-supported corrections / 0 unresolved:**

1. printed 1: \`மறைத்துவிடும்\` → \`மறைத்து விடும்\`;
2. printed 1: \`இளையராணிக்கு\` → \`இளைய ராணிக்கு\`;
3. printed 1: \`விட்டீர்கள்\` → \`விட்டார்கள்\`;
4. printed 2: \`அவள் அண்ணன்; அவள்\` → \`அவள் அண்ணன். அவள்\`;
5. printed 2: \`அவச்சொல்\` → \`அவச் சொல்\`;
6. printed 3: restored the source period after \`உயிர் விடுவது மேல்.\`;
7. printed 3: \`இத்தியாகம் செய்யத்தான் வேண்டும்;\` → \`இத்தியாகம் செய்துதான் வேண்டும்;\`;
8. printed 5: source-irregular \`மாபாதகர்கள் மறைத்து\` and \`மருதநாட்டு வீரர்கள் பிணமாக்க\` replace the normalized accusative forms.

Printed 4 required no lexical correction. The same independent re-read completed final historical-glyph checking for all five pages.

Next: logical printed pages **6–10**.
''',encoding='utf-8')

(N/'historical-glyph-audit.md').write_text('''# மருதநாட்டு இளவரசி — historical Tamil glyph audit

Status: **PROSPECTIVE 21/21 COMPLETE; FINAL INDEPENDENT VERIFICATION 5/21 PASS**.

Historical-glyph-sensitive families are read from source pixels occurrence by occurrence; OCR/extraction remains candidate-only and no global normalization is allowed.

- logical pages 1–5: **FINAL GLYPH PASS**;
- logical pages 6–21: pending;
- final historical-glyph verification: **5/21**;
- open uncertainty markers: **0**.

V1 also corrected the source provenance to the duplicate-spread geometry documented in \`mapping.md\`; that provenance correction does not promote unreviewed pages.
''',encoding='utf-8')

(T/'README.md').write_text('''# மருதநாட்டு இளவரசி — canonical Tamil transcription

Status: **T1 COMPLETE; INDEPENDENT DUAL-GATE VERIFICATION IN PROGRESS — 5/21 VERIFIED**.

All 21 logical printed pages are present. Logical pages **1–5** have passed independent visual-fidelity and final historical-glyph verification; logical pages 6–21 remain draft. Open uncertainty markers: **0**.

Corrected source geometry: PDF 2 is unique; exact duplicate spreads are **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22**. Canonical records use representative PDFs 2,3,5,7,9,11,13,15,17,19,21.

V1 records **9 source-supported corrections**; see \`notes/fidelity-audit.md\`.

**Next:** independently verify logical printed pages **6–10** using PDF 7 left/right, PDF 9 left/right, and PDF 11 left. Structured derivatives remain blocked until 21/21 dual-gate closure.
''',encoding='utf-8')

(W/'PROJECT_HANDOVER.md').write_text('''# மருதநாட்டு இளவரசி — Project Handover

Repository: \`pugazg/kalaignar-cinema-works\`  
Branch: \`main\`  
Work: \`works/maruthanattu-ilavarasi/\`

**LIVE MAIN IS AUTHORITATIVE.**

Source: \`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf\` — **22 PDF pages / 9,330,870 bytes / SHA-256 \`8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f\` / image-only**.

## Durable state

- intake / mapping: **COMPLETE / COMPLETE-VERIFIED-CORRECTED**;
- actual duplicate pattern: **3=4 through 21=22** in odd/even pairs; PDF 2 unique;
- canonical logical pages: **21**; representative scans **2,3,5,7,9,11,13,15,17,19,21**;
- source headings: **2–10**; logical pages 1–3 remain unnumbered;
- Tamil T1: **21/21 COMPLETE-DRAFT**;
- visual fidelity: **5/21 PASS**;
- final historical-glyph verification: **5/21 PASS**;
- remaining draft pages: **16**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

V1 logical pages 1–5 passed after **9 scan-supported corrections**, documented in \`notes/fidelity-audit.md\`.

## Exact next activity

> **Independently verify logical printed pages 6–10 using representative PDF 7 left/right, PDF 9 left/right and PDF 11 left; PDFs 8,10,12 are duplicates. Correct any mismatch before verification, complete final historical-glyph checks, and keep derivatives blocked until 21/21 dual-gate closure.**
''',encoding='utf-8')

(W/'NEXT_CHAT_PROMPT.md').write_text('''# Next Chat Prompt — மருதநாட்டு இளவரசி / verification logical pages 6–10

Continue in \`pugazg/kalaignar-cinema-works\`, branch \`main\`, active work \`works/maruthanattu-ilavarasi/\`. **LIVE MAIN IS AUTHORITATIVE.**

Current durable state: Tamil T1 **21/21 complete-draft**; visual fidelity **5/21 verified**; final historical-glyph verification **5/21 verified**; open uncertainties **0**; structured derivatives **BLOCKED**.

Physical source geometry: PDF 2 unique; duplicate spreads **3=4, 5=6, 7=8, 9=10, 11=12, 13=14, 15=16, 17=18, 19=20, 21=22**.

> **Next batch: independently re-read logical printed pages 6–10 against representative PDF 7 left/right, PDF 9 left/right and PDF 11 left. Treat PDFs 8,10,12 as provenance-only duplicates. Correct any mismatch first; then mark only passing pages verified and advance both final counters to 10/21. Do not begin structured derivatives.**
''',encoding='utf-8')

# metadata.yaml simple field sync
mp=W/'metadata.yaml'; m=mp.read_text(encoding='utf-8')
def repl(pattern,value):
    global m
    m,n=re.subn(pattern,value,m,count=1,flags=re.M)
    if n!=1: raise SystemExit(f'metadata pattern missing: {pattern}')
repl(r'^body_pagination_formula:.*$', 'body_pagination_formula: "PDF 2 => printed 1; representative odd PDFs 3-21 => printed 2-21; following even PDFs are exact duplicates"')
repl(r'^duplicate_pdf_spreads:.*$', 'duplicate_pdf_spreads: ["4=3", "6=5", "8=7", "10=9", "12=11", "14=13", "16=15", "18=17", "20=19", "22=21"]')
repl(r'^canonical_representative_final_spread_pdf_pages:.*$', 'canonical_representative_pdf_pages: [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]')
repl(r'^canonical_tamil_transcription:.*$', 'canonical_tamil_transcription: verification-in-progress')
repl(r'^visual_fidelity_audit:.*$', 'visual_fidelity_audit: in-progress-5-of-21')
repl(r'^historical_glyph_audit:.*$', 'historical_glyph_audit: final-in-progress-5-of-21')
repl(r'^next_action:.*$', 'next_action: "Independently verify logical printed pages 6–10; then advance both dual-gate counters to 10/21 if PASS."')
m=m.rstrip()+'\nvisual_verified_pages: 5\nhistorical_glyph_final_verified_pages: 5\nverification_current_through_logical_printed: 5\n'
mp.write_text(m,encoding='utf-8')

# data/works.json
wp=R/'data'/'works.json'; works=json.loads(wp.read_text(encoding='utf-8'))
rec=next(x for x in works if x.get('id')=='maruthanattu-ilavarasi')
rec.update({
'body_pagination_formula':'PDF 2 => printed 1; representative odd PDFs 3-21 => printed 2-21; following even PDFs are exact duplicates',
'duplicate_pdf_spreads':['4=3','6=5','8=7','10=9','12=11','14=13','16=15','18=17','20=19','22=21'],
'canonical_representative_pdf_pages':[2,3,5,7,9,11,13,15,17,19,21],
'canonical_tamil_transcription':'verification-in-progress','historical_glyph_audit':'final-in-progress-5-of-21',
'tamil_transcription':'verification-in-progress','tamil_first_pass_complete':True,
'tamil_transcription_draft_pages':16,'tamil_transcription_verified_pages':5,
'tamil_fidelity_audit':'in-progress-5-of-21','total_verified_pages':5,'total_review_pages':0,
'next_action':'Independently verify logical printed pages 6–10; keep derivatives blocked until 21/21 dual-gate closure.'
})
wp.write_text(json.dumps(works,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Current root status section only.
rp=R/'README.md'; rt=rp.read_text(encoding='utf-8')
a=rt.index('## மருதநாட்டு இளவரசி status'); b=rt.index('## வண்டிக்காரன் மகன் status',a)
sec='''## மருதநாட்டு இளவரசி status

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- corrected physical geometry: PDF 2 unique; duplicate spreads **3=4 through 21=22**;
- visual fidelity / final glyph verification: **5/21 / 5/21 PASS**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

**Next:** logical printed pages **6–10** dual-gate verification.

'''
rp.write_text(rt[:a]+sec+rt[b:],encoding='utf-8')

# Current repository mirrors.
hp=R/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; ht=hp.read_text(encoding='utf-8')
mark='## 11. மருதநாட்டு இளவரசி active checkpoint'; pos=ht.rfind(mark)
if pos<0: raise SystemExit('handover marker missing')
hp.write_text(ht[:pos]+'''## 11. மருதநாட்டு இளவரசி active checkpoint

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- corrected duplicate-spread provenance: **3=4 through 21=22**, PDF 2 unique;
- visual fidelity / final glyph: **5/21 / 5/21 PASS**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

**Next:** independently verify logical printed pages **6–10**.
''',encoding='utf-8')

sp=R/'docs'/'STATUS_CONSISTENCY_AUDIT.md'; st=sp.read_text(encoding='utf-8')
row='| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி | **Tamil T1 21/21 complete-draft; visual 5/21; final glyph 5/21; 0 open** | headings **2–10**; duplicate-spread provenance corrected | not-started | not-started |'
st,n=re.subn(r'^\| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி \|.*$',row,st,count=1,flags=re.M)
if n!=1: raise SystemExit('status matrix row missing')
mark='## Maruthanattu Ilavarasi current checkpoint'; pos=st.rfind(mark)
if pos<0: raise SystemExit('status marker missing')
sp.write_text(st[:pos]+'''## Maruthanattu Ilavarasi current checkpoint

- Tamil T1: **21/21 COMPLETE-DRAFT**;
- source geometry: PDF 2 unique; duplicate spreads **3=4 through 21=22**;
- visual fidelity / final historical glyph: **5/21 / 5/21 PASS**;
- open uncertainties: **0**;
- derivatives: **BLOCKED**.

Next: logical pages **6–10** dual-gate verification.
''',encoding='utf-8')

# Normalize Markdown and final QA.
for fp in [W/'mapping.md',N/'duplicate-scan-correction.md',N/'fidelity-audit.md',N/'historical-glyph-audit.md',T/'README.md',W/'PROJECT_HANDOVER.md',W/'NEXT_CHAT_PROMPT.md',rp,hp,sp]:
    s=fp.read_text(encoding='utf-8')
    fp.write_text('\n'.join(x.rstrip() for x in s.splitlines()).rstrip()+'\n',encoding='utf-8')
idx2=json.loads((T/'index.json').read_text(encoding='utf-8'))
assert idx2['visual_verified_pages']==5 and idx2['historical_glyph_final_verified_pages']==5
assert idx2['open_uncertainty_markers']==0
assert len(idx2['duplicate_pdf_spreads'])==10
assert idx2['canonical_representative_pdf_pages']==[2,3,5,7,9,11,13,15,17,19,21]
for r in idx2['page_records']:
    first=(T/r['path']).read_text(encoding='utf-8').splitlines()[0]
    assert f"pdf={r['pdf_page']}" in first and f"status={r['status']}" in first
print('V1 sync QA PASS: 5/21 visual + glyph verified; 9 source corrections; 0 unresolved.')
