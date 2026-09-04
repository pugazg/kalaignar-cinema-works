import json
import re
from pathlib import Path

ROOT = Path('.')

def rep(text, old, new, label, count=1):
    n = text.count(old)
    if n != count:
        raise RuntimeError(f'{label}: expected {count}, found {n}')
    return text.replace(old, new, count)

# Canonical full text: edit only PDF 25-34 range.
fp = ROOT / 'works/ammaiyappan/transcription/full-text.md'
text = fp.read_text(encoding='utf-8')
start = '<!-- source: pdf=25 printed=23 status=draft -->'
end = '<!-- source: pdf=35 printed=33 status=draft -->'
if start not in text or end not in text:
    raise RuntimeError('PDF 25/35 anchors missing')
pre, rest = text.split(start, 1)
seg, post = rest.split(end, 1)
seg = start + seg

corrections = [
    ('⟦மால் நன்னோரம்?⟧', 'மால் நன்னோரம்', 'marker12'),
    ('[⟦திருக்கிட்டு?⟧]', '[திருக்கிட்டு]', 'marker13'),
    ('நீ\nஎன் இங்கெல்லாம் தனியாக வருகிறாய்?', 'நீ\nஏன் இங்கெல்லாம் தனியாக வருகிறாய்?', 'pdf26 ஏன்'),
    ('⟦அகாதி?⟧', 'அகாதி', 'marker14'),
    ('⟦மரத்தில் தொத்தி?⟧', 'மரத்தில் தொத்தி', 'marker15'),
    ('உங்கள் ⟦தகாரின் வினவு?⟧ என்ன ஆகி விட்', 'உங்கள் தகராறின் விளைவு என்ன ஆகி விட்', 'marker16'),
    ('ரோமப்\nபதினொரு லோகத்திலும் மனிதர்கள் உண்டா?', 'ஈரேழு பதினறு லோகத்திலும் மனிதர்கள் உண்டா?', 'pdf30 ஈரேழு'),
    ('⟦காதல்புர...கன்றைநாடும் பசு...?⟧', 'காதல்புறு ... கன்றைநாடும் பசு ...', 'marker17'),
    ('வெளிப்படபடி துடிக்\nகிறது இருதயம்', 'வெளிப்பட்டபடி துடிக்\nகிறது இருதயம்', 'pdf32 வெளிப்பட்டபடி'),
    ('⟦கல்யாணமே வேண்டாம் என்று என்னைப் பெண்\nணை வாழ சங்கலம் கட்டிய நீங்கள் கண்ணு வாராய் என்று\nஎன்னை அழைக்கிறீர்கள்?⟧...', 'கல்யாணமே வேண்டாம் என்று கன்னிப் பெண்\nணை வாழ சங்கணம் கட்டிய நீங்கள் கண்ணு வாராய் என்று\nஎன்னை அழைக்கிறீர்கள்?...', 'marker18'),
    ('ராஜாபர்த்துரஹரி\nகதைத்தான்', 'ராஜாபர்த்துரஹரி\nகதைதான்', 'pdf33 கதைதான்'),
    ('அடங்காத\nபிய்யத்தை', 'அடங்காத\nபிரியத்தை', 'pdf33 பிரியத்தை'),
    ('வேங்கையாட்டு மன்னனிடம்', 'வேங்கைநாட்டு மன்னனிடம்', 'pdf33 வேங்கைநாட்டு'),
    ('நானும் கைநட்டி வாங்கியிருக்கிறேன்', 'நானும் கைநீட்டி வாங்கியிருக்கிறேன்', 'pdf34 கைநீட்டி'),
    ('பாளையக்காரரின் ⟦சொத்துக்கணைப் பிடிக்கும்?⟧ சூதாட்டக்\nகாரியாக;', 'பாளையக்காரின் சொத்துக்களைப் பிடிக்கும் சூதாட்டக்\nகாரியாக;', 'marker19'),
    ('இன்று; நான் நான் நீங்கள்; இப்படி வயிற்றில் அடிக்கப்', 'இன்று; நான் நாளை நீங்கள்; இப்படி வயிற்றில் அடிக்கப்', 'pdf34 இன்று நாளை'),
    ('வரையில் நாளுக்கு ஒரு அதிகாரம் ஆளுக்கு ஒரு நாட்ட', 'வரையில் நாளுக்கு ஒரு அதிகாரம் ஆளுக்கு ஒரு நாட்', 'pdf34-35 boundary'),
]
for old, new, label in corrections:
    seg = rep(seg, old, new, label)

for pdf, printed in zip(range(25,35), range(23,33)):
    old = f'<!-- source: pdf={pdf} printed={printed} status=draft -->'
    new = f'<!-- source: pdf={pdf} printed={printed} status=verified -->'
    seg = rep(seg, old, new, f'anchor {pdf}')

text = pre + seg + end + post
text = rep(text,
    'Status: **visual fidelity audit in progress**. PDF 5–24 / logical pp.3–22 are scan-verified; PDF 25–109 remain draft. The rendered scan controls canonical Tamil.',
    'Status: **visual fidelity audit in progress**. PDF 5–34 / logical pp.3–32 are scan-verified; PDF 35–109 remain draft. The rendered scan controls canonical Tamil.',
    'full-text status')
fp.write_text(text, encoding='utf-8')

# Authoritative index.
ip = ROOT / 'works/ammaiyappan/transcription/index.json'
idx = json.loads(ip.read_text(encoding='utf-8'))
idx['draft_pages'] = 75
idx['verified_pages'] = 30
idx['review_pages'] = 0
idx['open_uncertainty_markers'] = 97
fa = idx['fidelity_audit']
fa['audited_pages'] = 30
fa['verified_pages'] = 30
fa['unresolved_source_readings'] = 97
fa['review_pages'] = 0
fa['verified_pdf_range'] = [5,34]
fa['verified_logical_printed_range'] = [3,32]
idx['next_pdf_page'] = 35
idx['next_printed_page'] = 33
idx['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 35 / logical printed p.33. Resolve remaining first-pass uncertainties occurrence-by-occurrence and keep structured derivatives blocked until all 105 canonical pages are verified.'
ip.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Fidelity audit ledger.
ap = ROOT / 'works/ammaiyappan/notes/fidelity-audit.md'
a = ap.read_text(encoding='utf-8')
a = rep(a, '| PDF 25–109 / logical pp.23–107 | 0 | 0 | 85 | pending |', '| PDF 25–34 / logical pp.23–32 | 10 | 0 | 0 | verified |\n| PDF 35–109 / logical pp.33–107 | 0 | 0 | 75 | pending |', 'audit table range')
a = rep(a, '| **Total** | **20** | **0** | **85** | **in progress** |', '| **Total** | **30** | **0** | **75** | **in progress** |', 'audit table total')
a = rep(a, 'Open first-pass uncertainty markers after this audit checkpoint: **105** (markers **1–11 resolved**; markers **12–116 remain for later source-order review**).', 'Open first-pass uncertainty markers after this audit checkpoint: **97** (markers **1–19 resolved**; markers **20–116 remain for later source-order review**).', 'audit marker count')
section = '''\n## PDF 25–34 / logical pp.23–32 — verified\n\nAll ten pages were compared directly against the rendered scan. Markers 12–19 were resolved from the printed glyphs and the canonical assembled text was corrected without rewriting the retained historical first-pass part file.\n\nResolved marker readings:\n\n12. PDF 25: `மால் நன்னோரம்`\n13. PDF 25: `[திருக்கிட்டு]`\n14. PDF 26: `அகாதி`\n15. PDF 27: `மரத்தில் தொத்தி`\n16. PDF 30: `தகராறின் விளைவு`\n17. PDF 31: `காதல்புறு ... கன்றைநாடும் பசு ...`\n18. PDF 32: `கல்யாணமே வேண்டாம் என்று கன்னிப் பெண்ணை வாழ சங்கணம் கட்டிய நீங்கள் கண்ணு வாராய் என்று என்னை அழைக்கிறீர்கள்?...`\n19. PDF 34: `பாளையக்காரின் சொத்துக்களைப் பிடிக்கும்`\n\nOther scan-backed restorations include `நீ ஏன் இங்கெல்லாம்`, `ஈரேழு பதினறு லோகத்திலும்`, `வெளிப்பட்டபடி`, `கதைதான்`, `பிரியத்தை`, `வேங்கைநாட்டு`, `கைநீட்டி`, and `இன்று; நான் நாளை நீங்கள்`. The PDF 34→35 boundary was corrected from draft `நாட்ட` + `டாண்மை` to the source split `நாட்` + `டாண்மை`, preserving `நாட்டாண்மை` exactly across the page break.\n\nNo unresolved scan reading remains in PDF 25–34.\n'''
a = rep(a, '\n## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 25 / logical printed p.23**, in source order. Adjudicate markers **12 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.\n', section + '\n## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 35 / logical printed p.33**, in source order. Adjudicate markers **20 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.\n', 'audit next section')
ap.write_text(a, encoding='utf-8')

# Work-local markdown/status mirrors.
replacements = {
'works/ammaiyappan/README.md': [
('verified pages: **20**;', 'verified pages: **30**;'),
('open first-pass uncertainty markers: **105**;', 'open first-pass uncertainty markers: **97**;'),
('in-progress — PDF 5–24 / logical pp.3–22 verified (20/105)', 'in-progress — PDF 5–34 / logical pp.3–32 verified (30/105)'),
('in-progress — 20/105 verified', 'in-progress — 30/105 verified'),
('at PDF 25 / logical printed p.23', 'at PDF 35 / logical printed p.33'),
('remaining **105** explicit first-pass readings', 'remaining **97** explicit first-pass readings'),
],
'works/ammaiyappan/transcription/README.md': [
('verified pages: **20**;', 'verified pages: **30**;'),
('open first-pass uncertain readings: **105**;', 'open first-pass uncertain readings: **97**;'),
('in-progress — PDF 5–24 / logical pp.3–22 verified (20/105)', 'in-progress — PDF 5–34 / logical pp.3–32 verified (30/105)'),
('at PDF 25 / logical printed p.23', 'at PDF 35 / logical printed p.33'),
],
'works/ammaiyappan/PROJECT_HANDOVER.md': [
('verified pages **20**;', 'verified pages **30**;'),
('open uncertainty markers: **105**;', 'open uncertainty markers: **97**;'),
('in-progress — PDF 5–24 / logical pp.3–22 verified (20/105)', 'in-progress — PDF 5–34 / logical pp.3–32 verified (30/105)'),
('in-progress — 20/105 verified; next PDF 25 / logical p.23', 'in-progress — 30/105 verified; next PDF 35 / logical p.33'),
('at PDF 25 / logical printed p.23', 'at PDF 35 / logical printed p.33'),
('remaining 105 explicit first-pass uncertainty markers', 'remaining 97 explicit first-pass uncertainty markers'),
],
}
for path, pairs in replacements.items():
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    for old, new in pairs:
        if old in s:
            s = s.replace(old, new)
    p.write_text(s, encoding='utf-8')

# metadata.yaml exact current checkpoint values.
mp = ROOT / 'works/ammaiyappan/metadata.yaml'
m = mp.read_text(encoding='utf-8')
for old,new in [
('  verified_pages: 20\n  draft_pages: 85\n  review_pages: 0\n  open_first_pass_uncertainty_markers: 105\n  next_pdf_page: 25\n  next_logical_printed_page: 23', '  verified_pages: 30\n  draft_pages: 75\n  review_pages: 0\n  open_first_pass_uncertainty_markers: 97\n  next_pdf_page: 35\n  next_logical_printed_page: 33'),
('  audited_pages: 20\n  verified_pages: 20\n  review_pages: 0\n  unresolved_source_readings: 105\n  verified_pdf_pages: "5-24"\n  verified_logical_printed_pages: "3-22"', '  audited_pages: 30\n  verified_pages: 30\n  review_pages: 0\n  unresolved_source_readings: 97\n  verified_pdf_pages: "5-34"\n  verified_logical_printed_pages: "3-32"'),
('  visual_fidelity_audit: in-progress-20-of-105', '  visual_fidelity_audit: in-progress-30-of-105'),
('PDF 25 / logical printed p.23; 20/105 pages are verified and 105 explicit first-pass readings remain unresolved.', 'PDF 35 / logical printed p.33; 30/105 pages are verified and 97 explicit first-pass readings remain unresolved.'),
('PDF 25 / logical printed p.23; resolve the remaining 105 explicit first-pass readings', 'PDF 35 / logical printed p.33; resolve the remaining 97 explicit first-pass readings'),
]:
    if old in m:
        m = m.replace(old,new)
mp.write_text(m, encoding='utf-8')

# data/works.json machine-readable mirror.
dp = ROOT / 'data/works.json'
data = json.loads(dp.read_text(encoding='utf-8'))
rec = next(x for x in data if x.get('id') == 'ammaiyappan')
rec['canonical_tamil_draft_pages'] = 75
rec['canonical_tamil_verified_pages'] = 30
rec['canonical_tamil_review_pages'] = 0
rec['canonical_tamil_open_uncertainty_markers'] = 97
rec['tamil_fidelity_audit'] = 'in-progress-30-of-105'
rec['tamil_transcription_draft_pages'] = 75
rec['tamil_transcription_verified_pages'] = 30
rec['tamil_transcription_review_pages'] = 0
rec['total_verified_pages'] = 30
rec['total_review_pages'] = 0
rec['open_first_pass_uncertainty_markers'] = 97
rec['fidelity_audit_verified_pdf_pages'] = '5-34'
rec['fidelity_audit_verified_logical_printed_pages'] = '3-32'
rec['fidelity_audit_next_pdf_page'] = 35
rec['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 35 / logical printed p.33. Resolve the remaining 97 explicit first-pass readings before structured derivatives.'
dp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Shared prose mirrors: mechanical checkpoint-only substitutions.
shared = [ROOT/'README.md', ROOT/'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md', ROOT/'docs/STATUS_CONSISTENCY_AUDIT.md']
for p in shared:
    s = p.read_text(encoding='utf-8')
    pairs = [
        ('PDF 5–24 / logical pp.3–22', 'PDF 5–34 / logical pp.3–32'),
        ('20/105 verified', '30/105 verified'),
        ('20 / 85 / 0', '30 / 75 / 0'),
        ('20 / 85 / 0', '30 / 75 / 0'),
        ('20/105), 85 draft pages, 0 review pages, and 105', '30/105), 75 draft pages, 0 review pages, and 97'),
        ('20/105), 85 draft; 105 open markers', '30/105), 75 draft; 97 open markers'),
        ('**105** explicit unresolved first-pass readings', '**97** explicit unresolved first-pass readings'),
        ('**105** explicit first-pass uncertainty markers', '**97** explicit first-pass uncertainty markers'),
        ('remaining **105** explicit first-pass uncertainty markers', 'remaining **97** explicit first-pass uncertainty markers'),
        ('next PDF 25 / logical p.23', 'next PDF 35 / logical p.33'),
        ('PDF 25 / logical printed p.23', 'PDF 35 / logical printed p.33'),
        ('105 open first-pass readings; next PDF 25 / logical p.23', '97 open first-pass readings; next PDF 35 / logical p.33'),
    ]
    for old,new in pairs:
        s = s.replace(old,new)
    p.write_text(s, encoding='utf-8')

# Assertions.
check = json.loads(ip.read_text(encoding='utf-8'))
assert check['verified_pages'] == 30 and check['draft_pages'] == 75
assert check['open_uncertainty_markers'] == 97 and check['next_pdf_page'] == 35
ft = fp.read_text(encoding='utf-8')
for n in range(25,35):
    assert f'pdf={n} printed={n-2} status=verified' in ft
assert '⟦மால் நன்னோரம்?⟧' not in ft
assert '⟦சொத்துக்கணைப் பிடிக்கும்?⟧' not in ft
assert 'வரையில் நாளுக்கு ஒரு அதிகாரம் ஆளுக்கு ஒரு நாட்\n\n<!-- source: pdf=35 printed=33 status=draft -->\n\nடாண்மை' in ft
print('Ammayappan fidelity checkpoint prepared: 30/105 verified; next PDF 35')
