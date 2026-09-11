#!/usr/bin/env python3
from pathlib import Path
import json, re

root=Path('.')
W=root/'works'/'maruthanattu-ilavarasi'; T=W/'transcription'; P=T/'pages'; N=W/'notes'
idxp=T/'index.json'; idx=json.loads(idxp.read_text(encoding='utf-8'))
assert idx['first_pass_pages_completed']==21
assert idx['visual_verified_pages']==0
assert idx['historical_glyph_final_verified_pages']==0
assert idx['open_uncertainty_markers']==0
assert {r['printed_page'] for r in idx['page_records']}==set(range(1,22))

corrections={
'pages/002.md':[
('தங்கையின் குழந்தை தான் ஆளவேண்டுமே','தங்கையின் குழந்தை தரணி ஆளவேண்டுமே'),
('கோபம் நீதியை மறைத்துவிடும், நிதானமாக....','கோபம் நீதியை மறைத்து விடும், நிதானமாக....'),
('அதன் காரணமாய் இளையராணிக்கு அனுப்பப்பட்ட மருந்தில் தாங்கள் விஷம் கலந்து விட்டீர்கள்.','அதன் காரணமாய் இளைய ராணிக்கு அனுப்பப்பட்ட மருந்தில் தாங்கள் விஷம் கலந்து விட்டார்கள்.')],
'pages/003.md':[
('சிங்காரியின் பக்கம் அவள் அண்ணன்; அவள், அன்புக்குரிய மன்னர்.','சிங்காரியின் பக்கம் அவள் அண்ணன். அவள், அன்புக்குரிய மன்னர்.'),
('என்ற அவச்சொல் வேண்டாம்.','என்ற அவச் சொல் வேண்டாம்.')],
'pages/004.md':[
('வெளியேறி அரசருக்கு வருத்தத்தை அதிகமாக்குவதைவிட உயிர் விடுவது மேல்\n','வெளியேறி அரசருக்கு வருத்தத்தை அதிகமாக்குவதைவிட உயிர் விடுவது மேல்.\n'),
('அதைக் காப்பாற்ற இத்தியாகம் செய்யத்தான் வேண்டும்;','அதைக் காப்பாற்ற இத்தியாகம் செய்துதான் வேண்டும்;')],
'pages/006.md':[
('அந்த மாபாதகர்களை மறைத்து வைத்திருப்பவர்கள் யாராயிருந்தாலும் சரி!','அந்த மாபாதகர்கள் மறைத்து வைத்திருப்பவர்கள் யாராயிருந்தாலும் சரி!'),
('மருதநாட்டு வீரர்களை பிணமாக்க எனக்கு மனமில்லை, நாட்டின் அமைதிக்காக','மருதநாட்டு வீரர்கள் பிணமாக்க எனக்கு மனமில்லை, நாட்டின் அமைதிக்காக')]
}
applied=[]
for rel,reps in corrections.items():
    fp=T/rel; s=fp.read_text(encoding='utf-8')
    for old,new in reps:
        if old not in s: raise SystemExit(f'missing expected source in {rel}: {old}')
        s=s.replace(old,new,1); applied.append((rel,old,new))
    fp.write_text(s,encoding='utf-8')

# Correct full PDF geometry discovered during independent source review.
dups=[]; reps=[2]
for rep in range(3,22,2):
    dups.append({'pdf_page':rep+1,'duplicates_pdf_page':rep,'printed_pages':[rep-1,rep]}); reps.append(rep)
for rec in idx['page_records']:
    p=rec['printed_page']
    if p==1:
        rec['pdf_page']=2; rec['scan_side']='right'; rec.pop('duplicate_scan_pdf_page',None)
    else:
        rep=3+2*((p-2)//2); rec['pdf_page']=rep; rec['scan_side']='left' if p%2==0 else 'right'; rec['duplicate_scan_pdf_page']=rep+1
    rec['status']='verified' if p<=5 else 'draft'
    fp=T/rec['path']; s=fp.read_text(encoding='utf-8'); lines=s.splitlines()
    if not lines or not lines[0].startswith('<!-- source:'): raise SystemExit(f'bad anchor {fp}')
    pt='1-logical' if p==1 else str(p)
    anchor=f"<!-- source: pdf={rec['pdf_page']} side={rec['scan_side']} printed={pt}"
    if 'duplicate_scan_pdf_page' in rec: anchor+=f" duplicate-scan-pdf={rec['duplicate_scan_pdf_page']}"
    anchor+=f" status={rec['status']} -->"
    lines[0]=anchor; fp.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')

idx.update({
'status':'verification-in-progress','draft_pages':16,'visual_verified_pages':5,
'historical_glyph_first_pass_checked_pages':21,'historical_glyph_final_verified_pages':5,
'verification_current_through_logical_printed':5,'verification_batches_completed':1,
'duplicate_pdf_spreads':dups,'canonical_representative_pdf_pages':reps,
'canonical_representative_pdf_pages_for_printed_16_21':[17,19,21],
'first_pass_pdf_range_completed':'PDF 2–22 source coverage; canonical logical pages 1–21 use representative scans 2,3,5,7,9,11,13,15,17,19,21; exact duplicate scans 4,6,8,10,12,14,16,18,20,22 excluded','open_uncertainty_markers':0,
'next_action':'Independently verify logical printed pages 6–10 as the next five-page dual-gate batch. Use representative source pixels PDF 7 left/right, PDF 9 left/right, and PDF 11 left; PDFs 8,10,12 are exact duplicate spreads. Correct any draft mismatch before marking verified, perform final historical-glyph identity checks occurrence by occurrence, and keep structured derivatives blocked until all 21 logical pages pass both gates.'})
idxp.write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
