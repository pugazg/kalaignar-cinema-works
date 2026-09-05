import json
import re
from pathlib import Path

ROOT = Path('.')

def rep(text, old, new, label, count=1):
    n = text.count(old)
    if n != count:
        raise RuntimeError(f'{label}: expected {count}, found {n}')
    return text.replace(old, new, count)

# ---------------------------------------------------------------------------
# Canonical full text: edit only PDF 35-44 range.
# ---------------------------------------------------------------------------
fp = ROOT / 'works/ammaiyappan/transcription/full-text.md'
text = fp.read_text(encoding='utf-8')
start = '<!-- source: pdf=35 printed=33 status=draft -->'
end = '<!-- source: pdf=45 printed=43 status=draft -->'
if start not in text or end not in text:
    raise RuntimeError('PDF 35/45 anchors missing')
pre, rest = text.split(start, 1)
seg, post = rest.split(end, 1)
seg = start + seg

# Source-backed corrections from direct rendered-scan review.
corrections = [
    ('⟦கோபுர மேற்கலாம்?⟧', 'கோபுர மேதைகளாம்', 'marker20'),
    ('ஆள் தடகாத்திரமாய் இருக்கிறாய்', 'ஆள் திடகாத்திரமாய் இருக்கிறாய்', 'pdf36 திடகாத்திரமாய்'),
    ('வேங்கையூர்த்தாரின் படையில்', 'வேங்கைபுரத்தாரின் படையில்', 'pdf36 வேங்கைபுரத்தாரின்'),
    ('⟦புகழ் வாய்ந்த வேல்...போர் வீரன் வேல்...?⟧', 'புகழ் வாய்ந்த வேல்...போர் வீரன் வேல்...', 'marker21'),
    ('ஆதிக்கக்காரரின் சேனையிலே நான்', 'ஆதிக்கக்காரரின் சேணையிலே நான்', 'pdf36 சேணையிலே'),
    ('⟦வெறிநெறெல்லாம்?⟧', 'வெறிநெறெல்லாம்', 'marker22'),
    ('அதற்காகக் கைகளிலே வேலேந்துங்கள். தெய்\nவமே துணையென தின் தோள்', 'அதற்காகக் கைகளில் வாளேந்துங்கள். தெய்\nவமே துணையென திண் தோள்', 'pdf37 வாளேந்துங்கள் திண்'),
    ('⟦ஹி...ஹி...ஹி...வாலையும், வேலையும்\nதொடாதே—வைகுந்தவாசனை தொழு...கையிலே கேட\nயம் வந்தாதே—கைலாச நாதனின் திருநீறு எங்கு...அது\nஎங்கே இப்போது? வளைந்து போன தோள்களிலே வாகை\nமால் ஏந்துங்கள்...அதற்காகக் கைகளிலே வேலேந்துங்\nகள்...இது எங்கே? எல்லாம் மாயை...மாயாஜாலம்...இல்\nலையா சாமியாரே?⟧', 'ஹி...ஹி...ஹி...வாளையும், வேலையும்\nதொடாதே—வைகுந்தவாசனை தொழு...கையிலே கேட\nயம் ஏந்தாதே—கைலாச நாதனின் திருநீறு ஏந்து...அது\nஎங்கே இப்போது? வளைந்து போன தோள்களிலே வாகை\nமாலை ஏந்துங்கள்...அதற்காகக் கைகளிலே வேலேந்துங்\nகள்...இது எங்கே? எல்லாம் மாயை...மாயாஜாலம்...இல்\nலையா சாமியாரே?', 'marker23'),
    ('உன்னே எது எதிர்கொள்ளாதான்\nபயன் படுத்துகிறார்கள்.', 'உன்னை எது எதற்கெல்லாந்தான்\nபயன்படுத்துகிறார்கள்.', 'pdf38 உன்னை எது எதற்கெல்லாந்தான்'),
    ('அவதரித்து அர்ச்சுனனே போர் புரியச்', 'அவதரித்து அர்ச்சுனனை போர் புரியச்', 'pdf38 அர்ச்சுனனை'),
    ('உண்மை\nதிவென்று வெடித்துவிடும்', 'உண்மை\nதிடீரென்று வெடித்துவிடும்', 'pdf39 திடீரென்று'),
    ('[பூபதி போகிறார். சாமியார் பெருமூச்சு\nவிட்டு பீடத்தில் உட்காருகிறார்.]', '[பூபதி போகிறார். சாமியார் பெருமூச்சு\nவிட்டு பீடத்தில் உட்காரப் போகிறார்.]', 'pdf39 உட்காரப் போகிறார்'),
    ('அஞ்ச\nலோடி ஏதோ பைக்கைத் தூக்கிக் கொண்டு', 'அஞ்ச\nலோடி ஏதோ பைகளைக் தூக்கிக் கொண்டு', 'pdf39 பைகளைக்'),
    ('புதிய ஆணை பிறந்திருக்கும.', 'புதிய ஆணை பிறந்திருக்கும்.', 'pdf39 பிறந்திருக்கும்'),
    ('தொடர்பே இல்லை...முத்தா, இங்கு யாருமில்லை', 'தொடர்பே இல்ல...முத்தா, இங்கு யாருமில்ல', 'pdf39 இல்ல'),
    ('முத்தன்: இல்லை...என்ன விஷயம்?', 'முத்தன்: இல்ல...என்ன விஷயம்?', 'pdf39 முத்தன் இல்ல'),
    ('நான் வீசவும் இல்லை. அவள் விழவும்\nஇல்லை...நாங்கள் இருவருமே காதல் வலையில் சிக்கி விட்ட\nபறவைகள்!', 'நான் வீசவும் இல்ல. அவள் விழவும்\nஇல்ல...நாங்கள் இருவருமே காதல் வலையில் சிக்கி விட்ட\nபுறாக்கள்!', 'pdf39 புறாக்கள்'),
    ('⟦மாடனூர் வீட்டை?⟧', 'மாமனார் வீட்டை', 'marker24'),
    ('அஞ்சல் மனக்கு குதிரை தேய்த்து', 'அஞ்சல் மனைக்கு குதிரை தேய்த்து', 'pdf40 அஞ்சல் மனைக்கு'),
    ('சேனையில் ஒரு சரியான\nஇடம் காத்திருக்கிறது.', 'சைன்யத்தில் ஒரு சரியான\nஇடம் காத்திருக்கிறது.', 'pdf43 சைன்யத்தில்'),
    ('பயப்பட்டாமல் போடு.', 'பயப்படாமல் போடு.', 'pdf44 பயப்படாமல்'),
]
for old, new, label in corrections:
    seg = rep(seg, old, new, label)

# PDF 41 had a substantive first-pass omission. Replace that page body from scan.
p41 = '<!-- source: pdf=41 printed=39 status=draft -->'
p42 = '<!-- source: pdf=42 printed=40 status=draft -->'
if p41 not in seg or p42 not in seg:
    raise RuntimeError('PDF 41/42 anchors missing in segment')
left, rest41 = seg.split(p41, 1)
old41, right = rest41.split(p42, 1)
new41 = '''<!-- source: pdf=41 printed=39 status=draft -->

அரண்மனை உத்தரவு தடுக்கிறது. இனி வீட்டு நிழல்கள்;
மாட்டின் நிழல்கள் இவைதான் உனக்கு வாசஸ்தலம்!
முத்தா! உன் வறுமையைப் பரிசீக்கிறேன் என்று கவலைப்
படாதே, கவலையோடு கவலையாக இன்னும் ஒன்றைச்
சொல்லிவிடுகிறேன். நீ உணர்ந்து பார்ப்பதற்காக. உனக்கு
வயதாகி இருந்து; உலகத்தோடு ஒட்டி ஒழுகும் பழக்க
மிருந்து; உனக்கும் ஒரு மகள் இருப்பதாக வைத்துக்கொள்
அந்தமகளை தகப்பன் பெயர் தெரியாத ஒரு மணமகனுக்கு
மணம் செய்து கொடுப்பாயா? நீ செய்வாயோ என்னமோ.
என்னால் முடியுமா? என் வைதீக மனம் இடம் கொடுக்
குமா? யோசித்துப்பார்! உன் அம்மா காவேரி என்று
தெரியுமே தவிர, அவள் உன்னை யாருக்குப் பெற்றாள்
என்பது......

முத்தன்: போதும்! போதுமய்யா போதும்!

திரிசங்கு: காதைப் பொத்திக் கொண்டு பயனில்லை.
கண்ணை அகலமாகத் திறந்தும் பயனில்லை. கருத்துக் கத
வைத் திற... கொஞ்சமாகத் திற, போதும். சீரும், சிறப்பும்
சிங்கார மாளிகையும் அழைக்கிறது என் மகளே. நீ அதை
மறக்கிறாயா? மறக்கிறாயா முத்தா? நீ மறுத்தால், அது
அவள் மேல் உனக்குள்ள காதலுக்கு அடையாளமல்ல
அவளை சீரழிக்க வேண்டும் என்ற உன் கொடிய எண்ணத்
துக்குத்தான் அடையாளம். முத்தா! உன்னைக் கெஞ்சிக்
கேட்கிறேன். உன் காலில் வேண்டுமானாலும் விழுகிறேன்.
அவளை மறந்து விடு...அவளை மறந்து விடு.

முத்தன்: [அழுதபடி] ஆ! அய்யோ! மறக்கமுடியாத
மாணிக்கம், இழக்க முடியாத செல்வம்....அதையா மறந்து
விடுவது?

திரிசங்கு: நீ மறக்கா விட்டால் முத்தாயி தன்
தகப்பனை மறந்துவிட வேண்டும். அப்படி மறந்து விட்டால்
மரக்கிளையிலே அனாதையாக அந்தரத்திலே தொங்கும்
இந்த திரிசங்குவின் பிணம் உன்னை சபிக்கும்...பிணம்
உன்னை சபிக்கும்!

முத்தன்: அய்யா! என் உயிரை மறக்கச் சொல்கிறீர்.
மறந்து விடுகிறேன்.

'''
seg = left + new41 + p42 + right

# Mark all ten audited pages verified.
for pdf, printed in zip(range(35,45), range(33,43)):
    old = f'<!-- source: pdf={pdf} printed={printed} status=draft -->'
    new = f'<!-- source: pdf={pdf} printed={printed} status=verified -->'
    seg = rep(seg, old, new, f'anchor {pdf}')

text = pre + seg + end + post
text = rep(text,
    'Status: **visual fidelity audit in progress**. PDF 5–34 / logical pp.3–32 are scan-verified; PDF 35–109 remain draft. The rendered scan controls canonical Tamil.',
    'Status: **visual fidelity audit in progress**. PDF 5–44 / logical pp.3–42 are scan-verified; PDF 45–109 remain draft. The rendered scan controls canonical Tamil.',
    'full-text status')
fp.write_text(text, encoding='utf-8')

# ---------------------------------------------------------------------------
# Authoritative index.
# ---------------------------------------------------------------------------
ip = ROOT / 'works/ammaiyappan/transcription/index.json'
idx = json.loads(ip.read_text(encoding='utf-8'))
idx['draft_pages'] = 65
idx['verified_pages'] = 40
idx['review_pages'] = 0
idx['open_uncertainty_markers'] = 92
fa = idx['fidelity_audit']
fa['audited_pages'] = 40
fa['verified_pages'] = 40
fa['unresolved_source_readings'] = 92
fa['review_pages'] = 0
fa['verified_pdf_range'] = [5,44]
fa['verified_logical_printed_range'] = [3,42]
idx['next_pdf_page'] = 45
idx['next_printed_page'] = 43
idx['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 45 / logical printed p.43. Resolve remaining first-pass uncertainties occurrence-by-occurrence and keep structured derivatives blocked until all 105 canonical pages are verified.'
ip.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------------------------------------------------------------------------
# Fidelity audit ledger.
# ---------------------------------------------------------------------------
ap = ROOT / 'works/ammaiyappan/notes/fidelity-audit.md'
a = ap.read_text(encoding='utf-8')
a = rep(a, '| PDF 35–109 / logical pp.33–107 | 0 | 0 | 75 | pending |', '| PDF 35–44 / logical pp.33–42 | 10 | 0 | 0 | verified |\n| PDF 45–109 / logical pp.43–107 | 0 | 0 | 65 | pending |', 'audit table range')
a = rep(a, '| **Total** | **30** | **0** | **75** | **in progress** |', '| **Total** | **40** | **0** | **65** | **in progress** |', 'audit table total')
a = rep(a, 'Open first-pass uncertainty markers after this audit checkpoint: **97** (markers **1–19 resolved**; markers **20–116 remain for later source-order review**).', 'Open first-pass uncertainty markers after this audit checkpoint: **92** (markers **1–24 resolved**; markers **25–116 remain for later source-order review**).', 'audit marker count')
section = '''\n## PDF 35–44 / logical pp.33–42 — verified\n\nAll ten pages were compared directly against the rendered scan. Markers 20–24 were resolved from the printed glyphs. PDF 41 also required restoration of a substantive first-pass omission; the missing printed lines were restored only from the scan. The retained bounded `parts/pdf-035-044.md` remains historical first-pass provenance and was not rewritten.\n\nResolved marker readings:\n\n20. PDF 35: `கோபுர மேதைகளாம்`\n21. PDF 36: `புகழ் வாய்ந்த வேல்...போர் வீரன் வேல்...`\n22. PDF 37: `வெறிநெறெல்லாம்`\n23. PDF 38: `ஹி...ஹி...ஹி...வாளையும், வேலையும் தொடாதே—வைகுந்தவாசனை தொழு...கையிலே கேடயம் ஏந்தாதே—கைலாச நாதனின் திருநீறு ஏந்து...அது எங்கே இப்போது? வளைந்து போன தோள்களிலே வாகைமாலை ஏந்துங்கள்...அதற்காகக் கைகளிலே வேலேந்துங்கள்...இது எங்கே? எல்லாம் மாயை...மாயாஜாலம்...இல்லையா சாமியாரே?`\n24. PDF 40: `மாமனார் வீட்டை`\n\nOther scan-backed restorations include `திடகாத்திரமாய்`, `வேங்கைபுரத்தாரின்`, source `சேணையிலே`, PDF 37 `கைகளில் வாளேந்துங்கள்` / `திண் தோள்`, PDF 38 `உன்னை எது எதற்கெல்லாந்தான் பயன்படுத்துகிறார்கள்` / `அர்ச்சுனனை`, PDF 39 `திடீரென்று`, `பைகளைக்`, source-colloquial `இல்ல`, and `புறாக்கள்`, PDF 40 `அஞ்சல் மனைக்கு`, PDF 43 `சைன்யத்தில்`, and PDF 44 `பயப்படாமல்`.\n\nPDF 41 was restored to include the printed passage from `அந்தமகளை தகப்பன் பெயர் தெரியாத ஒரு மணமகனுக்கு...` through the subsequent discussion of `வைதீக மனம்`, `காவேரி`, `சீரும், சிறப்பும் சிங்கார மாளிகையும்`, and Thirisangu's final plea; those lines had been absent from the first-pass canonical assembly.\n\nNo unresolved scan reading remains in PDF 35–44.\n'''
a = rep(a, '\n## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 35 / logical printed p.33**, in source order. Adjudicate markers **20 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.\n', section + '\n## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 45 / logical printed p.43**, in source order. Adjudicate markers **25 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.\n', 'audit next section')
ap.write_text(a, encoding='utf-8')

# ---------------------------------------------------------------------------
# Work-local prose/status mirrors.
# ---------------------------------------------------------------------------
files_repls = {
    'works/ammaiyappan/README.md': [
        ('verified pages: **30**;', 'verified pages: **40**;'),
        ('open first-pass uncertainty markers: **97**;', 'open first-pass uncertainty markers: **92**;'),
        ('in-progress — PDF 5–34 / logical pp.3–32 verified (30/105)', 'in-progress — PDF 5–44 / logical pp.3–42 verified (40/105)'),
        ('| Visual fidelity audit | **in-progress — 30/105 verified** |', '| Visual fidelity audit | **in-progress — 40/105 verified** |'),
        ('| Verified Tamil pages | **20/105** |', '| Verified Tamil pages | **40/105** |'),
        ('**Continue the rendered-scan visual fidelity audit at PDF 35 / logical printed p.33.** Resolve the remaining **97** explicit first-pass readings', '**Continue the rendered-scan visual fidelity audit at PDF 45 / logical printed p.43.** Resolve the remaining **92** explicit first-pass readings'),
    ],
    'works/ammaiyappan/transcription/README.md': [
        ('verified pages: **30**;', 'verified pages: **40**;'),
        ('open first-pass uncertain readings: **97**;', 'open first-pass uncertain readings: **92**;'),
        ('in-progress — PDF 5–34 / logical pp.3–32 verified (30/105)', 'in-progress — PDF 5–44 / logical pp.3–42 verified (40/105)'),
        ('at PDF 35 / logical printed p.33', 'at PDF 45 / logical printed p.43'),
    ],
    'works/ammaiyappan/PROJECT_HANDOVER.md': [
        ('verified pages **30**;', 'verified pages **40**;'),
        ('open uncertainty markers: **97**;', 'open uncertainty markers: **92**;'),
        ('in-progress — PDF 5–34 / logical pp.3–32 verified (30/105)', 'in-progress — PDF 5–44 / logical pp.3–42 verified (40/105)'),
        ('in-progress — 30/105 verified; next PDF 35 / logical p.33', 'in-progress — 40/105 verified; next PDF 45 / logical p.43'),
        ('at PDF 35 / logical printed p.33', 'at PDF 45 / logical printed p.43'),
        ('remaining 97 explicit', 'remaining 92 explicit'),
    ],
}
for path, repls in files_repls.items():
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    for old, new in repls:
        s = rep(s, old, new, f'{path}: {old[:30]}')
    p.write_text(s, encoding='utf-8')

# metadata.yaml
mp = ROOT / 'works/ammaiyappan/metadata.yaml'
m = mp.read_text(encoding='utf-8')
for old, new, label in [
    ('verified_pages: 30', 'verified_pages: 40', 'metadata verified'),
    ('draft_pages: 75', 'draft_pages: 65', 'metadata draft'),
    ('open_first_pass_uncertainty_markers: 97', 'open_first_pass_uncertainty_markers: 92', 'metadata markers'),
    ('next_pdf_page: 35', 'next_pdf_page: 45', 'metadata next pdf'),
    ('next_logical_printed_page: 33', 'next_logical_printed_page: 43', 'metadata next printed'),
    ('audited_pages: 30', 'audited_pages: 40', 'metadata audited'),
    ('unresolved_source_readings: 97', 'unresolved_source_readings: 92', 'metadata unresolved'),
    ('verified_pdf_pages: "5-34"', 'verified_pdf_pages: "5-44"', 'metadata range'),
    ('verified_logical_printed_pages: "3-32"', 'verified_logical_printed_pages: "3-42"', 'metadata logical range'),
    ('visual_fidelity_audit: in-progress-30-of-105', 'visual_fidelity_audit: in-progress-40-of-105', 'metadata status'),
    ('at PDF 35 / logical printed p.33; 30/105 pages are verified and 97 explicit first-pass readings remain unresolved.', 'at PDF 45 / logical printed p.43; 40/105 pages are verified and 92 explicit first-pass readings remain unresolved.', 'metadata next action'),
    ('at PDF 35 / logical printed p.33; resolve the remaining 97 explicit first-pass readings', 'at PDF 45 / logical printed p.43; resolve the remaining 92 explicit first-pass readings', 'metadata status next'),
]:
    m = rep(m, old, new, label)
mp.write_text(m, encoding='utf-8')

# data/works.json — machine-readable shared registry.
dp = ROOT / 'data/works.json'
data = json.loads(dp.read_text(encoding='utf-8'))
rec = next(x for x in data if x.get('id') == 'ammaiyappan' or x.get('work_id') == 'ammaiyappan')
rec['canonical_tamil_draft_pages'] = 65
rec['canonical_tamil_verified_pages'] = 40
rec['canonical_tamil_review_pages'] = 0
rec['canonical_tamil_open_uncertainty_markers'] = 92
rec['tamil_fidelity_audit'] = 'in-progress-40-of-105'
rec['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 45 / logical printed p.43. Resolve the remaining 92 explicit first-pass readings before structured derivatives.'
rec['tamil_transcription_draft_pages'] = 65
rec['tamil_transcription_verified_pages'] = 40
rec['tamil_transcription_review_pages'] = 0
rec['total_verified_pages'] = 40
rec['total_review_pages'] = 0
rec['open_first_pass_uncertainty_markers'] = 92
rec['fidelity_audit_verified_pdf_pages'] = '5-44'
rec['fidelity_audit_verified_logical_printed_pages'] = '3-42'
rec['fidelity_audit_next_pdf_page'] = 45
dp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Root README.
rp = ROOT / 'README.md'
r = rp.read_text(encoding='utf-8')
for old, new, label in [
    ('PDF 5–34 / logical pp.3–32 verified', 'PDF 5–44 / logical pp.3–42 verified', 'root range'),
    ('verified / draft / review pages: **30 / 75 / 0**;', 'verified / draft / review pages: **40 / 65 / 0**;', 'root counts'),
    ('open first-pass uncertainty markers: **97**;', 'open first-pass uncertainty markers: **92**;', 'root markers'),
    ('at **PDF 35 / logical printed p.33** and adjudicate the remaining **97**', 'at **PDF 45 / logical printed p.43** and adjudicate the remaining **92**', 'root next'),
]:
    r = rep(r, old, new, label)
rp.write_text(r, encoding='utf-8')

# Master handover.
hp = ROOT / 'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
h = hp.read_text(encoding='utf-8')
for old, new, label in [
    ('through PDF 34 / logical p.32 — 30/105 verified', 'through PDF 44 / logical p.42 — 40/105 verified', 'handover range'),
    ('**97** explicit unresolved first-pass readings remain', '**92** explicit unresolved first-pass readings remain', 'handover markers'),
    ('PDF 5–34 visually verified (30/105), 75 draft pages, 0 review pages, and 97 unresolved first-pass readings', 'PDF 5–44 visually verified (40/105), 65 draft pages, 0 review pages, and 92 unresolved first-pass readings', 'handover checkpoint'),
    ('next source page is PDF 35 / logical p.33', 'next source page is PDF 45 / logical p.43', 'handover next'),
]:
    h = rep(h, old, new, label)
hp.write_text(h, encoding='utf-8')

# Status consistency audit.
sp = ROOT / 'docs/STATUS_CONSISTENCY_AUDIT.md'
s = sp.read_text(encoding='utf-8')
for old, new, label in [
    ('PDF 5–34 visually verified (30/105), 75 draft pages, 0 review pages, and 97 open first-pass readings; next PDF 35 / logical p.33.', 'PDF 5–44 visually verified (40/105), 65 draft pages, 0 review pages, and 92 open first-pass readings; next PDF 45 / logical p.43.', 'status result'),
    ('PDF 5–34 fidelity-verified (30/105); 75 draft; 97 open markers', 'PDF 5–44 fidelity-verified (40/105); 65 draft; 92 open markers', 'status matrix'),
]:
    s = rep(s, old, new, label)
sp.write_text(s, encoding='utf-8')

# Assertions.
check = json.loads(ip.read_text(encoding='utf-8'))
assert check['verified_pages'] == 40 and check['draft_pages'] == 65
assert check['open_uncertainty_markers'] == 92 and check['next_pdf_page'] == 45
ft = fp.read_text(encoding='utf-8')
for n in range(35,45):
    assert f'pdf={n} printed={n-2} status=verified' in ft
for bad in ['⟦கோபுர மேற்கலாம்?⟧','⟦புகழ் வாய்ந்த வேல்...போர் வீரன் வேல்...?⟧','⟦வெறிநெறெல்லாம்?⟧','⟦மாடனூர் வீட்டை?⟧']:
    assert bad not in ft
assert 'அந்தமகளை தகப்பன் பெயர் தெரியாத ஒரு மணமகனுக்கு' in ft
assert 'சைன்யத்தில் ஒரு சரியான' in ft
print('Ammayappan fidelity checkpoint prepared: 40/105 verified; next PDF 45')
