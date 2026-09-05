from pathlib import Path
import json
import re

ROOT = Path('.')


def replace_exact(text, old, new, label, count=1):
    n = text.count(old)
    if n != count:
        raise RuntimeError(f'{label}: expected {count}, found {n}')
    return text.replace(old, new)


def replace_all_expected(text, old, new, label, counts=(1,)):
    n = text.count(old)
    if n not in counts:
        raise RuntimeError(f'{label}: expected one of {counts}, found {n}')
    return text.replace(old, new)


# 1) Canonical full text: correct only PDF 45-54. Bounded part remains historical provenance.
fp = ROOT / 'works/ammaiyappan/transcription/full-text.md'
text = fp.read_text(encoding='utf-8')
start_token = '<!-- source: pdf=45 printed=43 status=draft -->'
end_token = '<!-- source: pdf=55 printed=53 status=draft -->'
if text.count(start_token) != 1 or text.count(end_token) != 1:
    raise RuntimeError('PDF 45-54 boundary tokens not unique')
pre, rest = text.split(start_token, 1)
body, post = rest.split(end_token, 1)
body = start_token + body

corrections = [
    ('இப்போதுவந்து ⟦வர்ணிப்பார் பார்?⟧...அப்போது', 'இப்போ வந்து வர்ணிப்பார் பார்...அப்போ', 'marker 25 + colloquial forms'),
    ('எனக்கொன்றும் கோபமில்லை.', 'எனக்கொன்றும் கோபமில்ல.', 'PDF45 கோபமில்ல'),
    ('புருவத்துக்குருகே', 'புருவத்துக்கருகே', 'PDF45 புருவத்துக்கருகே'),
    ('எனக்கு மறந்து விடுகிறது.', 'எனக்கு மறைந்து விடுகிறது.', 'PDF45 மறைந்து'),
    ('⟦மாகமே?⟧', 'மாகமே', 'marker 26'),
    ('உன் முத்தனில்லை...முத்தன் பேசவில்லை;', 'உன் முத்தனில்ல...முத்தன் பேசவில்ல;', 'PDF46 colloquial இல்ல'),
    ('⟦வீரனுக?⟧', 'வீரனாக', 'marker 27'),
    ('எழை முத்தனைக்', 'ஏழை முத்தனைக்', 'PDF46 ஏழை 1'),
    ('⟦காகரத்துக் குருவிலே, கம்பிய தொளியிலே?⟧', 'காகரத்த குரலிலே, கம்பிய தொனியிலே', 'marker 28'),
    ('எழை முத்தன் கட்டளை', 'ஏழை முத்தன் கட்டளை', 'PDF46 ஏழை 2'),
    ('உன் தங்கைக்கு அளித்த', 'உன் தந்தைக்கு அளித்த', 'PDF46 தந்தைக்கு'),
    ('⟦கலத்து எழும் சித்திரமா?⟧', 'கீற்று எழுதும் சித்திரமா?', 'marker 29'),
    ('⟦அதைக் காட்டியாகிக் காட்டுகிறேன் அதோ, அந்த ஆடும் மாக்களவில்?⟧', 'அதைக் காட்சியாக்கிக் காட்டுகிறேன் அதோ, அந்த ஆடும் மரக் கிளையில்', 'marker 30'),
    ('செய்து விட்டேன்...என்ன செய்வது?', 'செய்து விட்டேனே...என்ன செய்வது?', 'PDF47 விட்டேனே'),
    ('அவன் கை ⟦பொய்ப்பிடும்போது?⟧', 'அவன் கையொப்பமிடும்போது', 'marker 31'),
    ('அப்படி ஒரு தப்பால் இருப்பது உண்மை.', 'அப்படி ஒரு தப்பல் இருப்பது உண்மை.', 'PDF48 தப்பல்'),
    ('⟦தலைவனுக்கிவிட்டேன்?⟧', 'தலைவனாக்கிவிட்டேன்', 'marker 32'),
    ('சந்தர்ப்பம் சரியில்லை,', 'சந்தர்ப்பம் சரியில்ல,', 'PDF49 சரியில்ல'),
    ('⟦ஆளப்பார் மில்போல் இருக்கிறான்?⟧', 'ஆளைப்பார் மல்லேபோல் இருக்கிறான்', 'marker 33 old-typeface'),
    ('சேருவதற்குக் கட்டாயமில்லை ஆனால் சேர்ந்துவிலகுவது உன் இஷ்டமில்லை.', 'சேருவதற்குக் கட்டாயமில்ல ஆனால் சேர்ந்துவிலகுவது உன் இஷ்டமில்ல.', 'PDF49 colloquial கட்டாயமில்ல'),
    ('இந்த சேதத்தை வளர்த்து', 'இந்த தேகத்தை வளர்த்து', 'PDF49 தேகத்தை'),
    ('என்ன சொன்னாய். ராஜதுரோகி?', 'என்ன சொன்னாய், ராஜதுரோகி?', 'PDF50 punctuation'),
    ('நான் துரோகி இல்லை!', 'நான் துரோகி இல்ல!', 'PDF50 துரோகி இல்ல'),
    ('வெளியில் உலவுகிறான்', 'வெளியிலே உலவுகிறான்', 'PDF50 வெளியிலே'),
    ('பயலே விடாதீர்கள்.', 'பயல விடாதீர்கள்.', 'PDF50 பயல'),
    ('இங்கு இடமேயில்லை.', 'இங்கு இடமேயில்ல.', 'PDF51 இடமேயில்ல'),
    ('தங்களுக்கு தரவேண்டிய', 'தங்களுக்குத் தரவேண்டிய', 'PDF51 தங்களுக்குத்'),
    ('அய்யோ! பெருமைக்குரிய', 'அய்யா! பெருமைக்குரிய', 'PDF51 அய்யா'),
    ('⟦வேலழகன் உத்தா விடுகிறேன்?⟧', 'வேலழகன் உத்தரவு விடுகிறேன்', 'marker 34'),
    ('இந்த குறும்பன்.', 'இந்தக் குறும்பன்.', 'PDF51 இந்தக்'),
    ('⟦முடிகுடிய மண்ணையும் விட்டது?⟧', 'முடி சூடிய மன்னனையும் விடாது', 'marker 35'),
    ('⟦அவிர்த யோகமா?⟧', 'அமிர்த யோகமா?', 'marker 36'),
    ('என் கண்ணார் படையிலிருந்து', 'என் கண்ணாளர் படையிலிருந்து', 'PDF52 கண்ணாளர்'),
    ('பாலையக்காரிடம்', 'பாளையக்காரிடம்', 'PDF52 பாளையக்காரிடம்'),
    ('⟦ஏழையின் குரல் எழுக்கு மாளிகையில் எப்படிக் கேட்கும்?⟧', 'ஏழையின் குரல் ஏழடுக்கு மாளிகையில் எப்படிக் கேட்கும்?', 'marker 37'),
    ('⟦என்ன மிலக்கிறீர்?⟧', 'என்ன மிலக்கிறீர்?', 'marker 38'),
    ('வேலழு :', 'வேலழ :', 'PDF53 source speaker abbreviation'),
    ('இனி பயமில்லை.', 'இனி பயமில்ல.', 'PDF54 பயமில்ல'),
    ('⟦பொன் வாட்டும்?⟧', 'பொன் வரட்டும்', 'marker 39'),
]
for old, new, label in corrections:
    expected = 2 if label == 'PDF53 source speaker abbreviation' else 1
    body = replace_exact(body, old, new, label, expected)

# Mark all ten page anchors verified only after the completed page-level comparison.
for pdf in range(45, 55):
    printed = pdf - 2
    old = f'<!-- source: pdf={pdf} printed={printed} status=draft -->'
    new = f'<!-- source: pdf={pdf} printed={printed} status=verified -->'
    body = replace_exact(body, old, new, f'anchor PDF {pdf}')

if '⟦' in body or '⟧' in body:
    raise RuntimeError('unresolved marker remains in PDF 45-54 canonical segment')
fp.write_text(pre + body + end_token + post, encoding='utf-8')

# 2) Fidelity ledger.
ap = ROOT / 'works/ammaiyappan/notes/fidelity-audit.md'
a = ap.read_text(encoding='utf-8')
a = replace_exact(a, '| PDF 45–109 / logical pp.43–107 | 0 | 0 | 65 | pending |', '| PDF 45–54 / logical pp.43–52 | 10 | 0 | 0 | verified |\n| PDF 55–109 / logical pp.53–107 | 0 | 0 | 55 | pending |', 'audit progress range')
a = replace_exact(a, '| **Total** | **40** | **0** | **65** | **in progress** |', '| **Total** | **50** | **0** | **55** | **in progress** |', 'audit total')
a = replace_exact(a, 'Open first-pass uncertainty markers after this audit checkpoint: **92** (markers **1–24 resolved**; markers **25–116 remain for later source-order review**).', 'Open first-pass uncertainty markers after this audit checkpoint: **77** (markers **1–39 resolved**; markers **40–116 remain for later source-order review**).', 'audit markers')
section = '''\n## PDF 45–54 / logical pp.43–52 — verified\n\nAll ten pages were compared directly against the rendered scan. Markers 25–39 were resolved from the printed glyphs, including old-typeface forms that could not safely be inferred from modern visual expectation. The retained bounded `parts/pdf-045-054.md` remains historical first-pass provenance and was not rewritten.\n\nResolved marker readings:\n\n25. PDF 45: `வர்ணிப்பார் பார்`\n26. PDF 46: `மாகமே`\n27. PDF 46: `வீரனாக`\n28. PDF 46: `காகரத்த குரலிலே, கம்பிய தொனியிலே`\n29. PDF 46: `கீற்று எழுதும் சித்திரமா?`\n30. PDF 47: `அதைக் காட்சியாக்கிக் காட்டுகிறேன் அதோ, அந்த ஆடும் மரக் கிளையில்`\n31. PDF 48: `கையொப்பமிடும்போது`\n32. PDF 48: `தலைவனாக்கிவிட்டேன்`\n33. PDF 49: `ஆளைப்பார் மல்லேபோல் இருக்கிறான்`\n34. PDF 51: `வேலழகன் உத்தரவு விடுகிறேன்`\n35. PDF 51: `முடி சூடிய மன்னனையும் விடாது`\n36. PDF 52: `அமிர்த யோகமா?`\n37. PDF 53: `ஏழையின் குரல் ஏழடுக்கு மாளிகையில் எப்படிக் கேட்கும்?`\n38. PDF 53: source-visible `என்ன மிலக்கிறீர்?`\n39. PDF 54: `பொன் வரட்டும்`\n\nOther scan-backed restorations include PDF 45 `இப்போ வந்து` / `அப்போ`, `கோபமில்ல`, `புருவத்துக்கருகே`, and `மறைந்து விடுகிறது`; PDF 46 source-colloquial `முத்தனில்ல` / `பேசவில்ல`, `ஏழை`, and `உன் தந்தைக்கு`; PDF 47 `விட்டேனே`; PDF 48 `தப்பல்`; PDF 49 `சரியில்ல`, `கட்டாயமில்ல`, `இஷ்டமில்ல`, and `தேகத்தை`; PDF 50 `துரோகி இல்ல`, `வெளியிலே`, and `பயல`; PDF 51 `இடமேயில்ல`, `தங்களுக்குத்`, `அய்யா`, and `இந்தக் குறும்பன்`; PDF 52 `கண்ணாளர்` and `பாளையக்காரிடம்`; PDF 53 the printed speaker abbreviation `வேலழ`; and PDF 54 `பயமில்ல`.\n\nNo unresolved scan reading remains in PDF 45–54.\n'''
needle = '\n## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 45 / logical printed p.43**, in source order. Adjudicate markers **25 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.'
replacement = section + '\n## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 55 / logical printed p.53**, in source order. Adjudicate markers **40 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.'
a = replace_exact(a, needle, replacement, 'audit next section')
ap.write_text(a, encoding='utf-8')

# 3) Machine-readable transcription index.
ip = ROOT / 'works/ammaiyappan/transcription/index.json'
idx = json.loads(ip.read_text(encoding='utf-8'))
assert idx['verified_pages'] == 40 and idx['draft_pages'] == 65 and idx['open_uncertainty_markers'] == 92
idx['verified_pages'] = 50
idx['draft_pages'] = 55
idx['review_pages'] = 0
idx['open_uncertainty_markers'] = 77
fa = idx['fidelity_audit']
fa['audited_pages'] = 50
fa['verified_pages'] = 50
fa['review_pages'] = 0
fa['unresolved_source_readings'] = 77
fa['verified_pdf_range'] = [5, 54]
fa['verified_logical_printed_range'] = [3, 52]
idx['next_pdf_page'] = 55
idx['next_printed_page'] = 53
idx['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 55 / logical printed p.53. Resolve remaining first-pass uncertainties occurrence-by-occurrence and keep structured derivatives blocked until all 105 canonical pages are verified.'
ip.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Helpers for dedicated Ammayappan markdown/status files.
def advance_dedicated(path):
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    pairs = [
        ('PDF 5–44 / logical pp.3–42', 'PDF 5–54 / logical pp.3–52'),
        ('PDF 5–44 / logical p.42', 'PDF 5–54 / logical p.52'),
        ('40/105', '50/105'),
        ('40 / 105', '50 / 105'),
        ('verified pages **40**', 'verified pages **50**'),
        ('verified pages: **40**', 'verified pages: **50**'),
        ('open first-pass uncertainty markers: **92**', 'open first-pass uncertainty markers: **77**'),
        ('open uncertainty markers: **92**', 'open uncertainty markers: **77**'),
        ('remaining **92** explicit first-pass readings', 'remaining **77** explicit first-pass readings'),
        ('remaining 92 explicit first-pass readings', 'remaining 77 explicit first-pass readings'),
        ('PDF 45 / logical printed p.43', 'PDF 55 / logical printed p.53'),
        ('PDF 45 / logical p.43', 'PDF 55 / logical p.53'),
        ('markers **25 onward**', 'markers **40 onward**'),
    ]
    for old, new in pairs:
        s = s.replace(old, new)
    # Common numeric status fields in prose.
    s = s.replace('verified / draft / review pages: **40 / 65 / 0**', 'verified / draft / review pages: **50 / 55 / 0**')
    s = s.replace('65 draft pages', '55 draft pages')
    s = s.replace('92 unresolved', '77 unresolved')
    p.write_text(s, encoding='utf-8')

for path in [
    'works/ammaiyappan/transcription/README.md',
    'works/ammaiyappan/README.md',
    'works/ammaiyappan/PROJECT_HANDOVER.md',
]:
    advance_dedicated(path)

# metadata.yaml: update both transcription_progress and fidelity_audit blocks.
mp = ROOT / 'works/ammaiyappan/metadata.yaml'
m = mp.read_text(encoding='utf-8')
m = replace_all_expected(m, 'verified_pages: 40', 'verified_pages: 50', 'metadata verified pages', (2,))
m = replace_exact(m, 'draft_pages: 65', 'draft_pages: 55', 'metadata draft pages')
m = replace_exact(m, 'open_first_pass_uncertainty_markers: 92', 'open_first_pass_uncertainty_markers: 77', 'metadata markers')
m = replace_exact(m, 'next_pdf_page: 45', 'next_pdf_page: 55', 'metadata next pdf')
m = replace_exact(m, 'next_logical_printed_page: 43', 'next_logical_printed_page: 53', 'metadata next printed')
m = replace_exact(m, 'audited_pages: 40', 'audited_pages: 50', 'metadata audited pages')
m = replace_exact(m, 'unresolved_source_readings: 92', 'unresolved_source_readings: 77', 'metadata unresolved')
m = replace_exact(m, 'verified_pdf_pages: "5-44"', 'verified_pdf_pages: "5-54"', 'metadata PDF range')
m = replace_exact(m, 'verified_logical_printed_pages: "3-42"', 'verified_logical_printed_pages: "3-52"', 'metadata logical range')
m = m.replace('in-progress-40-of-105', 'in-progress-50-of-105')
m = m.replace('PDF 35 / logical printed p.33; 30/105 pages are verified and 97 explicit first-pass readings remain unresolved.', 'PDF 55 / logical printed p.53; 50/105 pages are verified and 77 explicit first-pass readings remain unresolved.')
m = m.replace('PDF 45 / logical printed p.43; 40/105 pages are verified and 92 explicit first-pass readings remain unresolved.', 'PDF 55 / logical printed p.53; 50/105 pages are verified and 77 explicit first-pass readings remain unresolved.')
m = m.replace('PDF 45 / logical printed p.43; resolve the remaining 92 explicit first-pass readings', 'PDF 55 / logical printed p.53; resolve the remaining 77 explicit first-pass readings')
mp.write_text(m, encoding='utf-8')

# data/works.json machine-readable shared registry.
dp = ROOT / 'data/works.json'
data = json.loads(dp.read_text(encoding='utf-8'))
rec = next(x for x in data if x.get('id') == 'ammaiyappan' or x.get('work_id') == 'ammaiyappan')
for key, value in {
    'canonical_tamil_draft_pages': 55,
    'canonical_tamil_verified_pages': 50,
    'canonical_tamil_review_pages': 0,
    'canonical_tamil_open_uncertainty_markers': 77,
    'tamil_transcription_draft_pages': 55,
    'tamil_transcription_verified_pages': 50,
    'tamil_transcription_review_pages': 0,
}.items():
    if key in rec:
        rec[key] = value
if 'tamil_fidelity_audit' in rec:
    rec['tamil_fidelity_audit'] = 'in-progress-50-of-105'
rec['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 55 / logical printed p.53. Resolve the remaining 77 explicit first-pass readings before structured derivatives.'
dp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# 4) Repository-wide mirrors: update only their Ammayappan current-status language.
for path in ['README.md', 'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md', 'docs/STATUS_CONSISTENCY_AUDIT.md']:
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    s = s.replace('PDF 5–44 / logical pp.3–42 verified', 'PDF 5–54 / logical pp.3–52 verified')
    s = s.replace('PDF 5–44 / logical p.42 — 40/105 verified', 'PDF 5–54 / logical p.52 — 50/105 verified')
    s = s.replace('PDF 5–44 fidelity-verified (40/105); 65 draft; 92 open markers', 'PDF 5–54 fidelity-verified (50/105); 55 draft; 77 open markers')
    s = s.replace('PDF 5–44 visually verified (40/105), 65 draft pages, 0 review pages, and 92 unresolved first-pass readings', 'PDF 5–54 visually verified (50/105), 55 draft pages, 0 review pages, and 77 unresolved first-pass readings')
    s = s.replace('PDF 5–44 visually verified (40/105), 65 draft pages, 0 review pages, and 92 open first-pass readings; next PDF 45 / logical p.43', 'PDF 5–54 visually verified (50/105), 55 draft pages, 0 review pages, and 77 open first-pass readings; next PDF 55 / logical p.53')
    s = s.replace('verified / draft / review pages: **40 / 65 / 0**', 'verified / draft / review pages: **50 / 55 / 0**')
    s = s.replace('open first-pass uncertainty markers: **92**', 'open first-pass uncertainty markers: **77**')
    s = s.replace('**92** explicit unresolved first-pass readings remain', '**77** explicit unresolved first-pass readings remain')
    s = s.replace('remaining **92** explicit first-pass uncertainty markers', 'remaining **77** explicit first-pass uncertainty markers')
    s = s.replace('next PDF 45 / logical p.43', 'next PDF 55 / logical p.53')
    s = s.replace('at **PDF 45 / logical printed p.43**', 'at **PDF 55 / logical printed p.53**')
    s = s.replace('at PDF 45 / logical printed p.43', 'at PDF 55 / logical printed p.53')
    s = s.replace('40 / 65 / 0', '50 / 55 / 0')
    p.write_text(s, encoding='utf-8')

# Targeted cleanup for status audit variants.
sp = ROOT / 'docs/STATUS_CONSISTENCY_AUDIT.md'
s = sp.read_text(encoding='utf-8')
s = s.replace('PDF 5–44 visually verified (40/105), 65 draft pages, 0 review pages, and 92 open first-pass readings; next PDF 45 / logical p.43.', 'PDF 5–54 visually verified (50/105), 55 draft pages, 0 review pages, and 77 open first-pass readings; next PDF 55 / logical p.53.')
s = s.replace('PDF 5–44 / logical pp.3–42 verified', 'PDF 5–54 / logical pp.3–52 verified')
s = s.replace('PDF 5–34 / logical pp.3–32 verified', 'PDF 5–54 / logical pp.3–52 verified')
s = s.replace('verified / draft / review pages: **30 / 75 / 0**', 'verified / draft / review pages: **50 / 55 / 0**')
s = s.replace('open first-pass uncertainty markers: **92**', 'open first-pass uncertainty markers: **77**')
sp.write_text(s, encoding='utf-8')

# Final invariants across active authority surfaces.
idx2 = json.loads(ip.read_text(encoding='utf-8'))
assert idx2['verified_pages'] == 50 and idx2['draft_pages'] == 55 and idx2['open_uncertainty_markers'] == 77
assert idx2['next_pdf_page'] == 55 and idx2['next_printed_page'] == 53
canon = fp.read_text(encoding='utf-8')
for pdf in range(45, 55):
    assert f'<!-- source: pdf={pdf} printed={pdf-2} status=verified -->' in canon
assert '⟦' not in canon.split('<!-- source: pdf=45 printed=43 status=verified -->',1)[1].split('<!-- source: pdf=55 printed=53 status=draft -->',1)[0]

print('Ammayappan PDF 45-54 fidelity update prepared: 50/105 verified, 77 markers remain, next PDF 55.')
