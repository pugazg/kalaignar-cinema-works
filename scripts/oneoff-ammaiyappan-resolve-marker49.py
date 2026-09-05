from pathlib import Path
import json, re

ROOT = Path('.')
FULL = ROOT / 'works/ammaiyappan/transcription/full-text.md'
INDEX = ROOT / 'works/ammaiyappan/transcription/index.json'
AUDIT = ROOT / 'works/ammaiyappan/notes/fidelity-audit.md'
NOTES = ROOT / 'works/ammaiyappan/notes/textual-notes-pdf-065-074.md'
TREADME = ROOT / 'works/ammaiyappan/transcription/README.md'
META = ROOT / 'works/ammaiyappan/metadata.yaml'
WREADME = ROOT / 'works/ammaiyappan/README.md'
HANDOVER = ROOT / 'works/ammaiyappan/PROJECT_HANDOVER.md'
ROOTREADME = ROOT / 'README.md'
WORKS = ROOT / 'data/works.json'
MASTER = ROOT / 'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
STATUS = ROOT / 'docs/STATUS_CONSISTENCY_AUDIT.md'


def read(p): return p.read_text(encoding='utf-8')
def write(p, s): p.write_text(s, encoding='utf-8')
def sub1(text, pat, repl, label, flags=0):
    out, n = re.subn(pat, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 replacement, got {n}')
    return out

page65 = '''
மார்பிலா முதுகிலா என்றாள்! முதுகிலென்றான்...கிழவி துடித்தனள்; இதயம் வெடித்தனள்; வாளை எடுத்தனள் முழவு ஒலித்த திக்கை நோக்கி முடுக்கினள் வேகம்...கோழைக்குப் பால் கொடுத்தேன்—குப்புற வீழ்ந்து கிடக்கும் மோழைக்குப் பெயர் போர் வீரனே!....அன்றொரு நாள்...பாய்ந்து வந்த ஈட்டிக்கு பதில் சொல்ல மார்பைக் காட்டி சாய்ந்து கிடந்தார் என் சாகாத கண்ணுளர் அவருக்குப் பிறந்தானா?...அடடா மானம் எங்கே?....குடிச் சுவருக்கும் கீழாக வீழ்ந்துபட்டான்...இமயவரம்பினிலே வீரம் சிரிக்கும் இங்கு வீண நரம்பினிலே இசை துடிக்கும்...அதுவும் மானம் மானம் என்றே முழக்கும்—மதுவும் சுருவும் உண்டு வாழும் மானமற்ற வம்சமா நீ...எடா, மறத்தமிழ் குடியிலே மாசு தூவிவிட்டாய்...தின்று கொழுத்தாய்?—திமிர்பாய்ந்த தோள்கள் எங்கே?...திணவெடுக்க வில்லையோ—அங்கேதோ என்று அலறினள். எண்பதை நெருங்கிய ஏழைக்கிழவி—சென்றங்கு செறுமுனையில் சிதறிக் கிடந்த செந்தமிழ்க் காளையைப் புறட்டிப் பார்த்தாள்...ஆங்கு நந்தமிழ் நாட்டைக் காக்க ஓடிட்டு ரத்தவெள்ளம்! பிணக்குவியலிலே பெருமூச்சு வாங்க நடந்தாள்...மணப்பந்தலிலும் அந்த மகிழ்ச்சி இல்ல...மகன் பிறந்தபோதும் மகிழ்ச்சிக்கு எல்லையுண்டு அவன் இறந்து கிடந்தான் ஈட்டிக்கு மார்புகாட்டி! அறுத்தெறிய இருந்தேன் அவன் குடித்த மார்பை—அடடா கருத்தரியப் பொய் சொன்ன கயவனெங்கே?...வாளிங்கே...அவன் நாக்கெங்கே?

வீரர்கள் : தச்...தச்...தச்...

முத் : இப்போது சொல்லுங்கள்...மானமும், வீரமும் எவ்வளவு மதிப்பு வாய்ந்தவை...அவைகளை மாற்றானின் காலடியில் மிதிக்க விடலாமா?

வீரர்கள் : கூடாது!...கூடாது!

முத் : அப்படியானால் பழுதாரை விடுவிக்க என் தலைமையில் ஒன்று சேருங்கள்.
'''.strip()

# Canonical page 65: replace the review placeholder with the scan-supported full page.
text = read(FULL)
pat = re.compile(r'<!-- source: pdf=65 printed=63 status=review -->.*?(?=<!-- source: pdf=66 printed=64 status=verified -->)', re.S)
m = pat.search(text)
if not m:
    raise SystemExit('full-text: PDF 65 review span not found')
replacement = '<!-- source: pdf=65 printed=63 status=verified -->\n\n' + page65 + '\n\n'
text = text[:m.start()] + replacement + text[m.end():]
if '⟦' in replacement:
    raise SystemExit('PDF 65 replacement still contains uncertainty marker')
if text.count('⟦') != 29:
    raise SystemExit(f'full-text uncertainty count expected 29, got {text.count("⟦")}')
for required in ['மோழைக்குப் பெயர் போர் வீரனே', 'என் சாகாத கண்ணுளர்', 'மதுவும் சுருவும் உண்டு வாழும்', 'அடடா கருத்தரியப் பொய் சொன்ன கயவனெங்கே', 'வீரர்கள் : தச்...தச்...தச்...']:
    if required not in replacement:
        raise SystemExit('PDF 65 required source reading missing: ' + required)
write(FULL, text)

# Machine-readable transcription authority.
data = json.loads(read(INDEX))
data['draft_pages'] = 35
data['verified_pages'] = 70
data['review_pages'] = 0
data['open_uncertainty_markers'] = 29
fa = data['fidelity_audit']
fa['audited_pages'] = 70
fa['verified_pages'] = 70
fa['unresolved_source_readings'] = 29
fa['review_pages'] = 0
fa['verified_pdf_range'] = [5, 74]
fa['verified_logical_printed_range'] = [3, 72]
fa.pop('additional_verified_pdf_ranges', None)
fa.pop('additional_verified_logical_printed_ranges', None)
fa.pop('review_pdf_pages', None)
fa.pop('review_logical_printed_pages', None)
data['next_pdf_page'] = 75
data['next_printed_page'] = 73
data['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 75 / logical printed p.73. PDF 5-74 are verified; 29 first-pass uncertainty markers remain on PDF 75-109. Structured derivatives remain blocked until all 105 canonical pages are verified.'
write(INDEX, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

# Fidelity ledger: current progress and PDF 65-74 disposition.
a = read(AUDIT)
progress = '''## Progress

| Range | Verified pages | Review pages | Remaining draft pages | Status |
|---|---:|---:|---:|---|
| PDF 5–14 / logical pp.3–12 | 10 | 0 | 0 | verified |
| PDF 15–24 / logical pp.13–22 | 10 | 0 | 0 | verified |
| PDF 25–34 / logical pp.23–32 | 10 | 0 | 0 | verified |
| PDF 35–44 / logical pp.33–42 | 10 | 0 | 0 | verified |
| PDF 45–54 / logical pp.43–52 | 10 | 0 | 0 | verified |
| PDF 55–64 / logical pp.53–62 | 10 | 0 | 0 | verified |
| PDF 65–74 / logical pp.63–72 | 10 | 0 | 0 | verified |
| PDF 75–109 / logical pp.73–107 | 0 | 0 | 35 | pending |
| **Total** | **70** | **0** | **35** | **in progress** |

Open first-pass uncertainty markers after this audit checkpoint: **29** (markers **1–87 resolved**; markers **88–116** remain unresolved).'''
a = sub1(a, r'## Progress\n\n.*?(?=\n\n## PDF 5–14)', progress, 'audit progress', re.S)
section = '''## PDF 65–74 / logical pp.63–72 — verified

All ten pages were compared directly against the rendered controlling scan and are now source-clean. PDF 65 marker 49 was resolved only after enlarged glyph-level review; no external literary witness, OCR, film dialogue, subtitles, web text, or semantic reconstruction was used. The retained bounded `parts/pdf-065-074.md` remains historical first-pass provenance and was not rewritten.

Marker **49 — PDF 65** is resolved from the printed page as the full continuation beginning `மார்பிலா முதுகிலா என்றாள்! முதுகிலென்றான்...` and ending `வாளிங்கே...அவன் நாக்கெங்கே?`. Decisive source-visible forms retained exactly include `மோழைக்குப்`, `கண்ணுளர்`, `இமயவரம்பினிலே`, `மதுவும் சுருவும்`, `செறுமுனையில்`, and `கருத்தரியப்`.

Markers **50–51** remain resolved as `வீரர்கள் : தச்...தச்...தச்...` and Muthan's question ending `அவைகளை மாற்றானின் காலடியில் மிதிக்க விடலாமா?`. Markers **52–87** remain resolved by the earlier full-page direct scan transcription of PDF 66–74.

Boundary disposition remains unchanged: PDF 73→74 preserves the source split `வைத்` + `திருந்த`; PDF 74 closes locally with `ஆபத்து காத்திருக்கிறது!`, and PDF 75 begins a new bracketed action.

No unresolved scan reading remains on PDF 65–74.'''
a = sub1(a, r'## PDF 65–74 / logical pp\.63–72 — 9 verified \+ 1 review.*?(?=\n## Exact next activity)', section + '\n', 'audit 65-74 section', re.S)
a = sub1(a, r'## Exact next activity\n\n.*$', '## Exact next activity\n\nContinue the rendered-scan visual fidelity audit at **PDF 75 / logical printed p.73**. PDF 5–74 are verified; markers **88–116** remain unresolved on PDF 75–109. Structured derivatives remain blocked until all 105 canonical pages are verified.\n', 'audit next action', re.S)
write(AUDIT, a)

# Historical uncertainty ledger gets a superseding fidelity disposition only.
n = read(NOTES)
fidelity = '''## Fidelity disposition — PDF 65–74

A later rendered-scan fidelity pass supersedes the first-pass uncertainty disposition without rewriting this historical ledger.

- markers **49–87** are now resolved directly from the rendered scan;
- marker **49** was cleared only after enlarged glyph-level review of PDF 65; decisive retained source forms include `மோழைக்குப்`, `கண்ணுளர்`, `மதுவும் சுருவும்`, and `கருத்தரியப்`;
- PDF **65–74** are verified after full-page direct scan transcription;
- the old marker-87 note claiming a PDF 74→75 continuation is superseded: PDF 74 closes locally with `ஆபத்து காத்திருக்கிறது!`, and PDF 75 begins a new bracketed action;
- the PDF 73→74 split `வைத்` + `திருந்த` is source-visible and retained.
'''
n = sub1(n, r'## Fidelity disposition — PDF 65–74.*$', fidelity, 'textual notes fidelity disposition', re.S)
write(NOTES, n)

# Work-local prose mirrors.
t = read(TREADME)
t = t.replace('- verified pages: **69**;', '- verified pages: **70**;')
t = t.replace('- review pages: **1**;', '- review pages: **0**;')
t = t.replace('- open first-pass uncertain readings: **30**;', '- open first-pass uncertain readings: **29**;')
t = t.replace('- full rendered-scan visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified (69/105); PDF 65 / logical p.63 review**.', '- full rendered-scan visual fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 verified (70/105)**.')
t = sub1(t, r'## Exact next activity\n\n.*$', '## Exact next activity\n\nContinue the **rendered-scan visual fidelity audit at PDF 75 / logical printed p.73**. PDF 5–74 are verified; markers **88–116** remain unresolved on PDF 75–109. Structured derivatives stay blocked until all 105 pages are verified.\n', 'transcription README next', re.S)
write(TREADME, t)

m = read(META)
m = re.sub(r'  verified_pages: 69\n  draft_pages: 35\n  review_pages: 1\n  open_first_pass_uncertainty_markers: 30\n  next_pdf_page: 65\n  next_logical_printed_page: 63\n  next_action: ".*?"', '  verified_pages: 70\n  draft_pages: 35\n  review_pages: 0\n  open_first_pass_uncertainty_markers: 29\n  next_pdf_page: 75\n  next_logical_printed_page: 73\n  next_action: "Continue the rendered-scan visual fidelity audit at PDF 75 / logical printed p.73; PDF 5-74 are verified and 29 first-pass uncertainty markers remain on PDF 75-109."', m, count=1)
m = re.sub(r'fidelity_audit:\n  status: in-progress\n  canonical_range_audit_complete: false\n  audited_pages: 70\n  verified_pages: 69\n  review_pages: 1\n  unresolved_source_readings: 30\n  verified_pdf_pages: "5-64,66-74"\n  verified_logical_printed_pages: "3-62,64-72"\n  review_pdf_pages: "65"\n  review_logical_printed_pages: "63"', 'fidelity_audit:\n  status: in-progress\n  canonical_range_audit_complete: false\n  audited_pages: 70\n  verified_pages: 70\n  review_pages: 0\n  unresolved_source_readings: 29\n  verified_pdf_pages: "5-74"\n  verified_logical_printed_pages: "3-72"', m, count=1)
m = m.replace('  visual_fidelity_audit: in-progress-69-of-105-plus-1-review', '  visual_fidelity_audit: in-progress-70-of-105')
m = re.sub(r'next_action: "Reopen PDF 65.*?"\n$', 'next_action: "Continue the rendered-scan visual fidelity audit at PDF 75 / logical printed p.73; PDF 5-74 are verified and structured derivatives remain blocked until all 105 pages are verified."\n', m, count=1, flags=re.S)
write(META, m)

w = read(WREADME)
w = w.replace('- verified pages: **69**;', '- verified pages: **70**;')
w = w.replace('- open first-pass uncertainty markers: **30**;', '- open first-pass uncertainty markers: **29**;')
w = w.replace('- visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified (69/105); PDF 65 / logical p.63 review**.', '- visual fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 verified (70/105)**.')
w = w.replace('| Visual fidelity audit | **in-progress — 69/105 verified + PDF 65 review** |', '| Visual fidelity audit | **in-progress — 70/105 verified** |')
w = w.replace('| Verified Tamil pages | **69/105; 1 review** |', '| Verified Tamil pages | **70/105; 0 review** |')
w = sub1(w, r'## Exact next activity\n\n.*$', '## Exact next activity\n\n**Continue the rendered-scan visual fidelity audit at PDF 75 / logical printed p.73.** PDF 5–74 are verified; 29 first-pass uncertainty markers remain on PDF 75–109. Do not start structured derivatives until all 105 canonical pages are verified.\n', 'work README next', re.S)
write(WREADME, w)

h = read(HANDOVER)
h = h.replace('state: **draft-complete**, verified pages **69**, review pages **1**;', 'state: **draft-complete**, verified pages **70**, review pages **0**;')
h = h.replace('- open uncertainty markers: **30**;', '- open uncertainty markers: **29**;')
h = h.replace('- visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified (69/105); PDF 65 / logical p.63 review**.', '- visual fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 verified (70/105)**.')
h = h.replace('- visual fidelity audit: **in-progress — 69/105 verified + PDF 65 review**;', '- visual fidelity audit: **in-progress — 70/105 verified; next PDF 75 / logical p.73**;')
h = sub1(h, r'## Exact next activity\n\n> .*$', '## Exact next activity\n\n> **Continue the separate rendered-scan visual fidelity audit at PDF 75 / logical printed p.73 and proceed in source order. PDF 5–74 are verified; adjudicate markers 88–116 occurrence-by-occurrence. Do not start scene/dialogue/character derivatives until all 105 canonical pages pass.**\n', 'handover next', re.S)
write(HANDOVER, h)

# Root README Ammayappan section.
r = read(ROOTREADME)
sec_pat = re.compile(r'## அம்மையப்பன் status\n.*?(?=\n## கலைஞர் திரை இசைப் பாடல்கள் status)', re.S)
sec = '''## அம்மையப்பன் status

`TVA_BOK_0064230_அம்மையப்பன்.pdf` is an active **111-page image-only screenplay/dialogue booklet** whose canonical Tamil first pass is complete and whose separate rendered-scan fidelity audit is now in progress.

- printed title: **`அம்மையப்பன்`**;
- printed credit: **`கதை வசனம்` / `மு. கருணாநிதி`**;
- source SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107 — 105 pages**;
- structural mapping: **verified intake map**;
- source-numbered scenes: **none**;
- locked PDF 56 / printed p.54 heading: **`பழுதார் வீதி`**;
- locked PDF 107 / printed p.105 heading: **`தூக்குமேடை`**; rejected `தாக்குமேடை` absent;
- canonical Tamil first pass: **draft-complete — 105/105 pages**;
- continuous `full-text.md`: **assembled through PDF 109**;
- first-pass assembly QA: **PASS — 105 anchors, exact PDF 5→109 order, 0 missing, 0 duplicate**;
- visual fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 verified (70/105)**;
- verified / draft / review pages: **70 / 35 / 0**;
- open first-pass uncertainty markers: **29**;
- structured derivatives / English / reader: **blocked pending complete verified Tamil**.

**Next:** audit **PDF 75 / logical printed p.73** and continue in source order; markers 88–116 remain unresolved. Do not start scene/dialogue/character derivatives until all 105 canonical pages are verified.
'''
if not sec_pat.search(r): raise SystemExit('root README Ammayappan section not found')
r = sec_pat.sub(sec.rstrip() + '\n', r, count=1)
write(ROOTREADME, r)

# Registry authority.
arr = json.loads(read(WORKS))
work = next((x for x in arr if x.get('id') == 'ammaiyappan'), None)
if not work: raise SystemExit('data/works.json: ammaiyappan not found')
for k,v in {
    'tamil_transcription_draft_pages':35,
    'tamil_transcription_verified_pages':70,
    'tamil_transcription_review_pages':0,
    'total_verified_pages':70,
    'total_review_pages':0,
    'open_first_pass_uncertainty_markers':29,
    'canonical_tamil_draft_pages':35,
    'canonical_tamil_verified_pages':70,
    'canonical_tamil_review_pages':0,
    'canonical_tamil_open_uncertainty_markers':29,
}.items(): work[k] = v
work['tamil_fidelity_audit'] = 'in-progress-70-of-105'
work['fidelity_audit_verified_pdf_pages'] = '5-74'
work['fidelity_audit_verified_logical_printed_pages'] = '3-72'
work['fidelity_audit_next_pdf_page'] = 75
work.pop('fidelity_audit_review_pdf_pages', None)
work.pop('fidelity_audit_review_logical_printed_pages', None)
work['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 75 / logical printed p.73; PDF 5-74 are verified and 29 first-pass uncertainty markers remain on PDF 75-109.'
write(WORKS, json.dumps(arr, ensure_ascii=False, indent=2) + '\n')

# Master handover: replace active Ammayappan checkpoint and synchronization sentence.
master = read(MASTER)
master = master.replace('rendered-scan fidelity audit has **PDF 5–64 and PDF 66–74 verified (69/105), PDF 65 / logical p.63 in review, 35 draft pages, and 30 unresolved first-pass readings**', 'rendered-scan fidelity audit has **PDF 5–74 verified (70/105), 35 draft pages, 0 review pages, and 29 unresolved first-pass readings**')
master = re.sub(r'`data/works\.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT\.md` are synchronized to the active \*\*Ammayappan fidelity checkpoint:.*?\*\*\. The next source page is PDF .*?\.', '`data/works.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` are synchronized to the active **Ammayappan fidelity checkpoint: first pass 105/105 assembled, PDF 5–74 verified (70/105), 35 draft pages, 0 review pages, and 29 unresolved first-pass readings**. The next source page is PDF 75 / logical p.73.', master, count=1)
master = sub1(master, r'## 16\. Ammayappan active checkpoint\n.*$', '''## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- source intake / whole-scan map: **complete**;
- canonical first pass: **105/105 draft-complete**, continuous `full-text.md` through PDF 109;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- fidelity audit verified range: **PDF 5–74 / logical pp.3–72 — 70/105 verified**;
- review pages: **0**;
- remaining draft pages: **35 — PDF 75–109**;
- open first-pass uncertainty markers: **29 — markers 88–116**;
- PDF 65 marker 49 is scan-resolved; retained unusual forms include `மோழைக்குப்`, `கண்ணுளர்`, `மதுவும் சுருவும்`, and `கருத்தரியப்`;
- PDF 73→74 source split `வைத்` + `திருந்த` is preserved; PDF 74 closes locally and does not continue into PDF 75;
- locked source headings remain `பழுதார் வீதி` (PDF 56) and `தூக்குமேடை` (PDF 107; reject `தாக்குமேடை`);
- structured derivatives / English / reader: **blocked pending 105/105 verified Tamil**.

**Exact next activity:** audit **PDF 75 / logical printed p.73** and continue in source order through PDF 109; resolve markers 88–116 only from the rendered scan.
''', 'master section16', re.S)
write(MASTER, master)

# Repository-wide consistency audit: current result, matrix row, Ammayappan detail.
s = read(STATUS)
s = re.sub(r'\*\*PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint:.*?\*\*', '**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–74 visually verified (70/105), 35 draft pages, 0 review pages, and 29 open first-pass readings; next gate PDF 75 / logical p.73.**', s, count=1)
s = re.sub(r'\| Ammayappan \|.*?\| scene/dialogue/character blocked pending complete verified Tamil \| blocked \| blocked \|', '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–74 fidelity-verified (70/105); 35 draft; 29 open markers** | scene/dialogue/character blocked pending complete verified Tamil | blocked | blocked |', s, count=1)
s = s.replace('- rendered-scan fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified; PDF 65 / logical p.63 review**;', '- rendered-scan fidelity audit: **in-progress — PDF 5–74 / logical pp.3–72 verified**;')
s = s.replace('- verified / draft / review pages: **69 / 35 / 1**;', '- verified / draft / review pages: **70 / 35 / 0**;')
s = s.replace('- open first-pass uncertainty markers: **30**;', '- open first-pass uncertainty markers: **29**;')
s = re.sub(r'The canonical Tamil first-pass transcription and assembly gate remains closed\. The separate source-fidelity gate is active\. Exact next activity: \*\*reopen PDF 65.*?\*\*\. Do not continue to PDF 75 while PDF 65 remains review\.', 'The canonical Tamil first-pass transcription and assembly gate remains closed. The separate source-fidelity gate is active. Exact next activity: **audit PDF 75 / logical printed p.73 and continue in source order**.', s, count=1)
write(STATUS, s)

# Final invariants across active authorities.
if json.loads(read(INDEX))['verified_pages'] != 70: raise SystemExit('index verified mismatch')
if json.loads(read(INDEX))['review_pages'] != 0: raise SystemExit('index review mismatch')
if json.loads(read(INDEX))['open_uncertainty_markers'] != 29: raise SystemExit('index marker mismatch')
if '<!-- source: pdf=65 printed=63 status=verified -->' not in read(FULL): raise SystemExit('PDF65 not verified')
if 'PDF 65 remains review' in read(AUDIT): raise SystemExit('stale audit review text')
if 'PDF 65 review' in read(ROOTREADME): raise SystemExit('stale root review text')
if '69/105' in read(WREADME): raise SystemExit('stale work README count')
print('Ammayappan marker 49 resolution prepared: 70 verified, 35 draft, 0 review, 29 open, next PDF 75')
