#!/usr/bin/env python3
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[3]
NEXT="Proceed with the separate visual-fidelity and final historical-glyph verification audit for PDF 25–29. Preserve source irregularity and mark a page verified only after both gates pass. Do not reopen already verified PDF 6–9, PDF 11–23 absent genuinely new direct-source evidence; PDF 5 and PDF 10 remain physical-source-damage holds and PDF 24 remains an ink/mark-overprint hold. Structured derivatives and English translation remain blocked until the verified Tamil gate is complete."
changed=[]
def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
 q=R/p; old=q.read_text(encoding='utf-8') if q.exists() else ''
 if old!=s: q.write_text(s,encoding='utf-8'); changed.append(p)
def one(s,a,b):
 if a not in s: raise SystemExit('missing '+a)
 return s.replace(a,b,1)
# Preconditions
ip='works/naam/transcription/index.json'; d=json.loads(rd(ip))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(13,13,15,2)
p='works/naam/transcription/parts/pdf-020-024.md'; b=rd(p)
for x in ['pdf=20 printed=20 status=draft glyph=checked-first-pass','pdf=24 printed=24 status=draft glyph=checked-first-pass','உன்னைச் சீமானுக்கும் இரகசியம்','அவன் சீமானுக்கும் இரகசியம்','அந்த உயிரில்தான்','கவலைப்படுவீர்களென்று','திங்க தின்னு','கவலை இல்லை!','பார்க்க வந்தேன்','வெளியிட்டுப் போகிறேன்','அந்த உயிரை கண்டு பிடித்து விடு','தவறு ஒன்றும் இல்லை','இன்னும் என்ன புரிந்து கொள்ளவில்லையா?','அண்ணனுக்கு கெளரவம் தேடி இருப்பது']:
 assert x in b, x
# Canonical batch status and scan-backed corrections
b=one(b,'Status: **draft / needs-review** — rendered scan controls; no page in this batch is yet verified.','Status: **mixed verification — PDF 20–23 VERIFIED; PDF 24 needs-review** — rendered scan controls.')
b=one(b,'Historical-glyph first-pass: **checked page-by-page, not final-verified**.','Historical-glyph final verification: **PASS PDF 20–24 / 5 of 5**.')
for n in range(20,24):
 b=one(b,f'pdf={n} printed={n} status=draft glyph=checked-first-pass',f'pdf={n} printed={n} status=verified glyph=verified-final')
b=one(b,'pdf=24 printed=24 status=draft glyph=checked-first-pass','pdf=24 printed=24 status=needs-review glyph=verified-final')
for a,c in [
 ('உன்னைச் சீமானுக்கும் இரகசியம்','உன்னைச் சீமானாக்கும் இரகசியம்'),
 ('அவன் சீமானுக்கும் இரகசியம்','அவன் சீமானாக்கும் இரகசியம்'),
 ('அந்த உயிரில்தான்','அந்த உயில்தான்'),
 ('கவலைப்படுவீர்களென்று','கவலைப்படுவீர்கள் என்று'),
 ('திங்க தின்னு','திங்கு தின்னு'),
 ('கவலை இல்லை!','கவலை இல்லே!'),
 ('பார்க்க வந்தேன்','பார்க்கவந்தேன்'),
 ('வெளியிட்டுப் போகிறேன்','வெளியிட்டுப்போகிறேன்'),
 ('அந்த உயிரை கண்டு பிடித்து விடு','அந்த உயிலை கண்டுபிடித்து விடு'),
 ('தவறு ஒன்றும் இல்லை','தவறு ஒன்றும் இல்லே'),
 ('இன்னும் என்ன புரிந்து கொள்ளவில்லையா?','இன்னும் என்னை புரிந்து கொள்ளவில்லையா?')]:
 b=one(b,a,c)
b=one(b,'மல்லயப்ப :- மீனு...! அண்ணனுக்கு கெளரவம் தேடி இருப்பது ரொம்பவும் அழகாக இருக்கிறது.','மல்லயப்ப :- மீனு...! அண்ணனுக்கு கெளரவம் தே⟦தெளிவில்லை — PDF 24: `தே`க்கு அடுத்த அச்செழுத்து மீது மை/கறை மறைவு; மறைந்த எழுத்து ஊகித்து நிரப்பப்படவில்லை⟧ இருப்பது ரொம்பவும் அழகாக இருக்கிறது.')
i=b.find('## First-pass audit notes')
if i<0: raise SystemExit('missing batch footer')
b=b[:i]+'''## Verification audit notes\n\n- PDF **20–23** pass both direct visual-fidelity and final historical-glyph gates and are **VERIFIED**.\n- PDF **24** passes final historical-glyph review but remains `needs-review`: in scene 11 the source is directly readable only as `அண்ணனுக்கு கெளரவம் தே… இருப்பது`; a later dark ink/mark covers the printed character(s) after visible `தே`. Native, enlarged and channel-separated inspection did not positively recover the hidden glyph, so the earlier `தேடி` completion is not retained as canonical authority.\n- Scan-backed corrections applied in this audit include PDF 20 `சீமானாக்கும்` (2 occurrences), `உயில்தான்`, `கவலைப்படுவீர்கள் என்று`; PDF 21 `திங்கு தின்னு`, `கவலை இல்லே`; PDF 22 `பார்க்கவந்தேன்`; PDF 23 `வெளியிட்டுப்போகிறேன்`, `உயிலை கண்டுபிடித்து`; PDF 24 `இல்லே`, `என்னை`.\n- Historical `னா` in PDF 21 `நீதானா...?` is **final-verified** occurrence-specifically; no global glyph replacement was used.\n- PDF 20–23 add no uncertainty. PDF 24 adds **1** source-obscuration hold. Repository-wide open uncertainties become **3**: PDF 5, PDF 10, PDF 24. PDF 9 remains resolved as `குறுக்கொடிய`.\n- No OCR, film audio, subtitles, web text, later edition or semantic completion was used as textual authority.\n'''
wr(p,b)
# Audit log
audit='''# நாம் — visual-fidelity + final historical-glyph verification audit — PDF 20–24\n\nSource: `TVA_BOK_0064201_நாம்.pdf`  \nRange: **PDF 20–24**  \nAudit mode: **dual gate — rendered-pixel lexical fidelity + occurrence-specific historical-glyph verification**  \nResult: **PDF 20–23 PASS / VERIFIED; PDF 24 HOLD; 4/5 dual-gate verified**.\n\nThe rendered scan is controlling. No OCR, film audio, subtitles, later edition, web text or semantic reconstruction is textual authority.\n\n## PDF 20 — PASS / VERIFIED\n\nDirect source comparison corrects: `சீமானுக்கும்` → **`சீமானாக்கும்`** in both occurrences; `அந்த உயிரில்தான்` → **`அந்த உயில்தான்`**; `கவலைப்படுவீர்களென்று` → **`கவலைப்படுவீர்கள் என்று`**. Source-period forms including `போறு ஞானம்!` and `பாய்சன்!` remain unchanged. Historical-glyph final review: **PASS**.\n\n## PDF 21 — PASS / VERIFIED\n\nCorrections: `திங்க தின்னு` → **`திங்கு தின்னு`**; `கவலை இல்லை!` → **`கவலை இல்லே!`**. The historical old-form cluster in `நீதானா...?` is final-verified as **`னா`**, not the modern-lookalike `னு`. Historical-glyph final review: **PASS**.\n\n## PDF 22 — PASS / VERIFIED\n\nDirect source comparison establishes source-joined **`பார்க்கவந்தேன்`** rather than `பார்க்க வந்தேன்`. The unlabeled `எங்கம்மா?` remains unlabeled, and source `பாலிலா` remains unmodernized. Historical-glyph final review: **PASS**.\n\n## PDF 23 — PASS / VERIFIED\n\nCorrections: `வெளியிட்டுப் போகிறேன்` → **`வெளியிட்டுப்போகிறேன்`**; `அந்த உயிரை கண்டு பிடித்து விடு` → **`அந்த உயிலை கண்டுபிடித்து விடு`**. Source irregular forms `தூர பந்து`, `மட்டாக`, `காலராவா? ஜன்னியா?` remain unchanged. Historical-glyph final review: **PASS**.\n\n## PDF 24 — HOLD\n\nDirect comparison corrects `தவறு ஒன்றும் இல்லை` → **`தவறு ஒன்றும் இல்லே`** and `இன்னும் என்ன புரிந்து கொள்ளவில்லையா?` → **`இன்னும் என்னை புரிந்து கொள்ளவில்லையா?`**.\n\nScene 11 contains a physical/ink-overprint obstruction. The scan positively supports only:\n\n`அண்ணனுக்கு கெளரவம் தே… இருப்பது ரொம்பவும் அழகாக இருக்கிறது.`\n\nThe printed character(s) immediately after `தே` are covered by a dark later mark. Native-resolution, enlarged and channel-separated inspection does not positively expose the hidden glyph. The earlier first-pass completion `தேடி` is therefore **not** treated as verified source text and is replaced by an explicit uncertainty marker.\n\nHistorical-glyph final review of all surviving visible clusters: **PASS**. The hold is lexical source obscuration, not an unresolved historical-glyph identity.\n\n## Batch result\n\n| PDF | Visual fidelity | Historical glyph final | Dual-gate status | Open uncertainty |\n|---:|---|---|---|---:|\n| 20 | PASS after correction | PASS | VERIFIED | 0 |\n| 21 | PASS after correction | PASS | VERIFIED | 0 |\n| 22 | PASS after correction | PASS | VERIFIED | 0 |\n| 23 | PASS after correction | PASS | VERIFIED | 0 |\n| 24 | HOLD — ink/mark obscures post-`தே` glyph | PASS | needs-review | 1 |\n| **Total** | **4 PASS + 1 HOLD** | **5 PASS** | **4 VERIFIED** | **1** |\n\nRepository-wide checkpoint after synchronization: first pass **67/67 COMPLETE**; visual-fidelity **17/67**; historical-glyph final **20/67**; dual-gate verified **17/67**; review **50/67**; open source uncertainties **3** — PDF 5, PDF 10, PDF 24.\n\n## Next activity\n\nProceed with dual-gate verification for **PDF 25–29**. Do not reopen verified PDF 6–9 or PDF 11–23 absent new direct-source evidence. Keep PDF 5, PDF 10 and PDF 24 as explicit source-obscuration holds. Structured derivatives and English remain blocked until verified Tamil closes.\n'''
wr('works/naam/notes/verification-audit-pdf-020-024.md',audit)
# Index
d.update(draft_pages=50,verified_pages=17,visual_fidelity_passed_pages=17,historical_glyph_verified_pages=20,review_pages=50,open_uncertainty_markers=3,next_action=NEXT)
for x in d['parts']:
 if x['path']=='parts/pdf-020-024.md': x.update(status='mixed-pdf20-23-verified-pdf24-needs-review',historical_glyph_status='verified-final',open_uncertainties=1)
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Metadata
p='works/naam/metadata.yaml'; s=rd(p)
for a,c in [('  draft_pages: 54','  draft_pages: 50'),('  verified_pages: 13','  verified_pages: 17'),('  review_pages: 54','  review_pages: 50'),('  open_uncertainty_markers: 2','  open_uncertainty_markers: 3'),('  pages_verified: 15','  pages_verified: 20'),('  visual_fidelity_audit: in-progress-through-pdf-019-13-of-67-pass','  visual_fidelity_audit: in-progress-through-pdf-024-17-of-67-pass'),('  historical_glyph_audit: final-verification-in-progress-15-of-67','  historical_glyph_audit: final-verification-in-progress-20-of-67')]: s=one(s,a,c)
v='''verification_progress:\n  current_audit_path: "notes/verification-audit-pdf-020-024.md"\n  visual_fidelity_passed_pages: 17\n  historical_glyph_final_verified_pages: 20\n  dual_gate_verified_pages: 17\n  held_pages:\n    - pdf_page: 5\n      reason: "physically damaged left beginning of introductory line"\n    - pdf_page: 10\n      reason: "physically damaged right-edge ending in Malaiyappan speech"\n    - pdf_page: 24\n      reason: "later dark ink/mark obscures the printed character immediately after visible தே in scene 11"\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n  next_pdf_range: "25-29"\n'''
s=re.sub(r'verification_progress:\n.*?\nhistorical_glyph:\n',v+'\nhistorical_glyph:\n',s,count=1,flags=re.S)
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',s,count=1,flags=re.S); wr(p,s)
# Glyph audit
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
s=one(s,'| PDF 20–24 | 5 | 5 | 0 | 5 | partial-first-pass |','| PDF 20–24 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF24 hold |')
s=one(s,'| **Total** | **67** | **67** | **13** | **54** | **final-verification-in-progress** |','| **Total** | **67** | **67** | **17** | **50** | **final-verification-in-progress** |')
s=one(s,'| 21 | 21 | modern-lookalike `நீதானு...?` | `நீதானா...?` | `னா` | enlarged source pixels + binding guide\'s same-family precedent (`மட்டுந்தானு?` → `மட்டுந்தானா?`) | draft-supported |','| 21 | 21 | modern-lookalike `நீதானு...?` | `நீதானா...?` | `னா` | enlarged source pixels + binding guide\'s same-family precedent (`மட்டுந்தானு?` → `மட்டுந்தானா?`) | **final-verified** |')
if '## PDF 20–24 final dual-gate audit' not in s:
 s+='''\n## PDF 20–24 final dual-gate audit\n\n- historical-glyph final: **5/5 PASS**;\n- visual-fidelity: **PDF 20–23 PASS / PDF 24 HOLD**;\n- PDF 21 `நீதானா...?` is final-verified historical `னா`;\n- PDF 24 hold is caused by a later dark mark obscuring the printed glyph after visible `தே`, not by historical-glyph ambiguity;\n- details: `verification-audit-pdf-020-024.md`.\n\nNext final audit range: **PDF 25–29**.\n'''
wr(p,s)
# data/works.json
p='data/works.json'; x=json.loads(rd(p)); n=next(q for q in x if q.get('id')=='naam')
n.update(canonical_tamil_transcription='verification-in-progress',visual_fidelity_audit='in-progress-through-pdf-024-17-of-67',historical_glyph_audit='final-verification-in-progress-20-of-67',canonical_tamil_draft_pages=50,canonical_tamil_verified_pages=17,canonical_tamil_review_pages=50,canonical_tamil_open_uncertainty_markers=3,historical_glyph_pages_verified=20,visual_fidelity_passed_pages=17,canonical_tamil_current_verification_path='works/naam/notes/verification-audit-pdf-020-024.md',next_action=NEXT)
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
print('\n'.join(changed))