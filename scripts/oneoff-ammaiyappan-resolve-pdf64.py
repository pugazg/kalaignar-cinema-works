from pathlib import Path
import json, re

ROOT = Path('.')


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def write(path, text):
    (ROOT / path).write_text(text, encoding='utf-8')


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected exactly one occurrence, found {n}: {old!r}')
    return text.replace(old, new, 1)


def replace_all_required(text, old, new, label):
    n = text.count(old)
    if n < 1:
        raise SystemExit(f'{label}: expected at least one occurrence: {old!r}')
    return text.replace(old, new)

# 1. Canonical full text: resolve marker 47 and verify PDF 64.
path = 'works/ammaiyappan/transcription/full-text.md'
text = read(path)
anchor_old = '<!-- source: pdf=64 printed=62 status=review -->'
anchor_new = '<!-- source: pdf=64 printed=62 status=verified -->'
text = replace_once(text, anchor_old, anchor_new, 'PDF64 anchor')

marker_pat = re.compile(
    r'⟦கிளியும் மெச்சிவிருப்பும் கிழவிக்கும் தன்மையும் .*?பெருநரைக் கிழவி பொறுத்தி\.\.\.⟧',
    re.S,
)
resolved47 = (
    'கிளியும் மெச்சிவிருப்பும் கிழவிக்கும் தன்மையும் துளி காட்டா மானத்தின் '
    'உறைவிடம்; மறவன் மாளிகை! இல்லத்து வாயிலிலே கிண்ணைத்துச் சோறோடு '
    'வெல்லத்தைச் சிறிதுகலந்து வயிற்றுக்குள் வழியனுப்ப பொக்கை வாய்தனைத் திறந்து '
    'பிடியன்னம் எடுத்துப் போட்டாள்; பெருநரைக் கிழவியொருத்தி...'
)
text, n = marker_pat.subn(resolved47, text, count=1)
if n != 1:
    raise SystemExit(f'marker47: expected exactly one uncertainty span, replaced {n}')
write(path, text)

# 2. Authoritative transcription index.
path = 'works/ammaiyappan/transcription/index.json'
data = json.loads(read(path))
assert data['verified_pages'] == 59 and data['draft_pages'] == 45 and data['review_pages'] == 1
assert data['open_uncertainty_markers'] == 69
fa = data['fidelity_audit']
assert fa['verified_pages'] == 59 and fa['review_pages'] == 1

data['verified_pages'] = 60
data['draft_pages'] = 45
data['review_pages'] = 0
data['open_uncertainty_markers'] = 68
fa['audited_pages'] = 60
fa['verified_pages'] = 60
fa['review_pages'] = 0
fa['unresolved_source_readings'] = 68
fa['verified_pdf_range'] = [5, 64]
fa['verified_logical_printed_range'] = [3, 62]
fa.pop('review_pdf_pages', None)
fa.pop('review_logical_printed_pages', None)
data['next_pdf_page'] = 65
data['next_printed_page'] = 63
data['next_action'] = (
    'Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63. '
    'Resolve remaining first-pass uncertainties occurrence-by-occurrence; structured derivatives '
    'remain blocked until all 105 canonical pages are verified.'
)
write(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

# 3. Fidelity ledger.
path = 'works/ammaiyappan/notes/fidelity-audit.md'
text = read(path)
text = replace_once(text,
    '| PDF 55–63 / logical pp.53–61 | 9 | 0 | 0 | verified |\n| PDF 64 / logical p.62 | 0 | 1 | 0 | review — marker 47 unresolved |',
    '| PDF 55–64 / logical pp.53–62 | 10 | 0 | 0 | verified |',
    'fidelity progress rows')
text = replace_once(text,
    '| **Total** | **59** | **1** | **45** | **in progress** |',
    '| **Total** | **60** | **0** | **45** | **in progress** |',
    'fidelity total')
text = replace_once(text,
    'Open first-pass uncertainty markers after this audit checkpoint: **69** (markers **1–46 and 48 resolved**; marker **47** plus markers **49–116** remain unresolved).',
    'Open first-pass uncertainty markers after this audit checkpoint: **68** (markers **1–48 resolved**; markers **49–116** remain unresolved).',
    'fidelity open count')
text = replace_once(text,
    '## PDF 55–64 / logical pp.53–62 — 9 verified + 1 review',
    '## PDF 55–64 / logical pp.53–62 — verified',
    'fidelity section heading')
text = replace_once(text,
    'PDF 55–63 were compared page-by-page against the rendered controlling scan and are source-clean after scan-backed correction. PDF 64 was also compared in full, but remains `review` because first-pass marker 47 contains an old-type sequence that is not secure enough to normalize from the scan. The historical bounded `parts/pdf-055-064.md` remains first-pass provenance and was not rewritten.',
    'PDF 55–64 were compared page-by-page against the rendered controlling scan and are source-clean after scan-backed correction. Marker 47 was resolved only after enlarged glyph-level review of PDF 64; no outside poem text was used. The historical bounded `parts/pdf-055-064.md` remains first-pass provenance and was not rewritten.',
    'fidelity section intro')
text = replace_once(text,
    '46. PDF 64: `குடிசைகாண்! ஒருபுறத்தில் கூரிய வேல், வாள் வரிசையாய் அமைத்திருக்கும். வையத்தை பிடிப்பதற்கும் வெம்பகை முடிப்பதற்கும் வடித்து வைத்த படைக்கலம் போல் மின்னும் மிளிரும்...புலியின் குகையினிலே அழகில்லை......புதுமையல்ல!`\n48. PDF 64:',
    '46. PDF 64: `குடிசைகாண்! ஒருபுறத்தில் கூரிய வேல், வாள் வரிசையாய் அமைத்திருக்கும். வையத்தை பிடிப்பதற்கும் வெம்பகை முடிப்பதற்கும் வடித்து வைத்த படைக்கலம் போல் மின்னும் மிளிரும்...புலியின் குகையினிலே அழகில்லை......புதுமையல்ல!`\n47. PDF 64: `கிளியும் மெச்சிவிருப்பும் கிழவிக்கும் தன்மையும் துளி காட்டா மானத்தின் உறைவிடம்; மறவன் மாளிகை! இல்லத்து வாயிலிலே கிண்ணைத்துச் சோறோடு வெல்லத்தைச் சிறிதுகலந்து வயிற்றுக்குள் வழியனுப்ப பொக்கை வாய்தனைத் திறந்து பிடியன்னம் எடுத்துப் போட்டாள்; பெருநரைக் கிழவியொருத்தி...`\n48. PDF 64:',
    'fidelity marker47 insertion')
text = replace_once(text,
    'Marker **47** remains explicitly unresolved on PDF 64. No external poem text, OCR, film dialogue, or semantic reconstruction was used to fill it.',
    'Marker **47** is resolved from the enlarged PDF 64 scan. The decisive source-visible forms include `துளி காட்டா`, `உறைவிடம்; மறவன் மாளிகை!`, `கிண்ணைத்துச் சோறோடு`, `எடுத்துப் போட்டாள்`, and `பெருநரைக் கிழவியொருத்தி`. No external poem text, OCR, film dialogue, or semantic reconstruction was used.',
    'fidelity marker47 disposition')
text = re.sub(
    r'## Exact next activity\n\nReopen \*\*PDF 64 / logical printed p\.62\*\*.*$',
    '## Exact next activity\n\nContinue the rendered-scan fidelity audit at **PDF 65 / logical printed p.63**, in source order. Resolve markers **49 onward** occurrence-by-occurrence and keep structured derivatives blocked until all 105 canonical pages are verified.',
    text,
    flags=re.S,
)
write(path, text)

# 4. Work-local README.
path = 'works/ammaiyappan/README.md'
text = read(path)
text = replace_once(text, '- verified pages: **59**;', '- verified pages: **60**;', 'work README verified')
text = replace_once(text, '- open first-pass uncertainty markers: **69**;', '- open first-pass uncertainty markers: **68**;', 'work README markers')
text = replace_once(text,
    '- visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 / logical p.62 review**.',
    '- visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified (60/105)**.',
    'work README audit')
text = replace_once(text,
    '| Visual fidelity audit | **in-progress — 59/105 verified + PDF 64 review** |',
    '| Visual fidelity audit | **in-progress — 60/105 verified** |',
    'work README table audit')
text = replace_once(text,
    '| Verified Tamil pages | **59/105; 1 review** |',
    '| Verified Tamil pages | **60/105; 0 review** |',
    'work README table verified')
text = re.sub(
    r'## Exact next activity\n\n\*\*Reopen PDF 64 / logical printed p\.62.*$',
    '## Exact next activity\n\n**Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63.** Resolve the remaining **68** explicit first-pass readings occurrence-by-occurrence, upgrade pages only after full-page direct scan comparison, and keep all structured derivatives blocked until the complete 105-page canonical range is verified.\n',
    text,
    flags=re.S,
)
write(path, text)

# 5. Metadata YAML.
path = 'works/ammaiyappan/metadata.yaml'
text = read(path)
for old, new, label in [
    ('  verified_pages: 59\n  draft_pages: 45\n  review_pages: 1\n  open_first_pass_uncertainty_markers: 69',
     '  verified_pages: 60\n  draft_pages: 45\n  review_pages: 0\n  open_first_pass_uncertainty_markers: 68', 'metadata progress counts'),
    ('  next_pdf_page: 64\n  next_logical_printed_page: 62', '  next_pdf_page: 65\n  next_logical_printed_page: 63', 'metadata next page'),
    ('  next_action: "Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan; PDF 5-63 are verified, PDF 64 is review, and structured derivatives remain blocked until all 105 pages are verified."',
     '  next_action: "Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63; 60/105 pages are verified and 68 explicit first-pass readings remain unresolved."', 'metadata next action'),
    ('  audited_pages: 60\n  verified_pages: 59\n  review_pages: 1\n  unresolved_source_readings: 69\n  verified_pdf_pages: "5-63"\n  verified_logical_printed_pages: "3-61"\n  review_pdf_pages: "64"\n  review_logical_printed_pages: "62"',
     '  audited_pages: 60\n  verified_pages: 60\n  review_pages: 0\n  unresolved_source_readings: 68\n  verified_pdf_pages: "5-64"\n  verified_logical_printed_pages: "3-62"', 'metadata fidelity block'),
    ('  visual_fidelity_audit: in-progress-59-of-105-plus-1-review', '  visual_fidelity_audit: in-progress-60-of-105', 'metadata status'),
    ('next_action: "Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan; do not advance to PDF 65 until PDF 64 is verified."',
     'next_action: "Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63; resolve the remaining 68 explicit first-pass readings before structured derivatives."', 'metadata final next')
]:
    text = replace_once(text, old, new, label)
write(path, text)

# 6. Transcription README.
path = 'works/ammaiyappan/transcription/README.md'
text = read(path)
text = replace_once(text, '- verified pages: **59**;', '- verified pages: **60**;', 'transcription README verified')
text = replace_once(text, '- review pages: **1**;', '- review pages: **0**;', 'transcription README review')
text = replace_once(text, '- open first-pass uncertain readings: **69**;', '- open first-pass uncertain readings: **68**;', 'transcription README markers')
text = replace_once(text,
    '- full rendered-scan visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 review**.',
    '- full rendered-scan visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified (60/105)**.',
    'transcription README audit')
text = re.sub(
    r'## Exact next activity\n\nReopen \*\*PDF 64 / logical printed p\.62\*\*.*$',
    '## Exact next activity\n\nContinue the **rendered-scan visual fidelity audit at PDF 65 / logical printed p.63**. Compare the entire page directly against the controlling scan, adjudicate remaining first-pass uncertainties occurrence-by-occurrence, and keep structured derivatives blocked until all 105 canonical pages are verified.',
    text,
    flags=re.S,
)
write(path, text)

# 7. Work handover.
path = 'works/ammaiyappan/PROJECT_HANDOVER.md'
text = read(path)
text = replace_once(text,
    '- state: **draft-complete**, verified pages **59**, review pages **1**;',
    '- state: **draft-complete**, verified pages **60**, review pages **0**;',
    'handover state')
text = replace_once(text, '- open uncertainty markers: **69**;', '- open uncertainty markers: **68**;', 'handover markers')
text = replace_once(text,
    '- visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 / logical p.62 review**.',
    '- visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified (60/105)**.',
    'handover audit')
text = replace_once(text,
    '- visual fidelity audit: **in-progress — 59/105 verified; PDF 64 / logical p.62 review**;',
    '- visual fidelity audit: **in-progress — 60/105 verified; next PDF 65 / logical p.63**;',
    'handover phase gate')
text = re.sub(
    r'## Exact next activity\n\n> \*\*Reopen PDF 64 / logical printed p\.62.*$',
    '## Exact next activity\n\n> **Continue the separate rendered-scan visual fidelity audit at PDF 65 / logical printed p.63 and proceed in source order through PDF 109. Compare each full page directly with the controlling scan, adjudicate the remaining 68 explicit first-pass uncertainty markers occurrence-by-occurrence, preserve locked source verdicts, and upgrade pages only after direct page-level visual comparison. Do not start scene/dialogue/character derivatives until all 105 canonical pages pass the audit.**',
    text,
    flags=re.S,
)
write(path, text)

# 8. Root README.
path = 'README.md'
text = read(path)
text = replace_once(text,
    '- visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified; PDF 64 review**;',
    '- visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified**;',
    'root audit')
text = replace_once(text,
    '- verified / draft / review pages: **59 / 45 / 1**;',
    '- verified / draft / review pages: **60 / 45 / 0**;',
    'root counts')
text = replace_once(text,
    '- open first-pass uncertainty markers: **69**;',
    '- open first-pass uncertainty markers: **68**;',
    'root markers')
text = replace_once(text,
    '**Next:** reopen **PDF 64 / logical printed p.62** and resolve marker **47** from the scan. Do not advance to PDF 65 while PDF 64 remains review. Do not start scene/dialogue/character derivatives until all 105 canonical pages are verified.',
    '**Next:** continue the rendered-scan visual fidelity audit at **PDF 65 / logical printed p.63** and adjudicate the remaining **68** explicit first-pass uncertainty markers. Do not start scene/dialogue/character derivatives until all 105 canonical pages are verified.',
    'root next')
write(path, text)

# 9. Machine-readable registry; repair both current and older duplicate mirror fields.
path = 'data/works.json'
arr = json.loads(read(path))
w = next(x for x in arr if x.get('id') == 'ammaiyappan')
w['canonical_tamil_draft_pages'] = 45
w['canonical_tamil_verified_pages'] = 60
w['canonical_tamil_review_pages'] = 0
w['canonical_tamil_open_uncertainty_markers'] = 68
w['tamil_fidelity_audit'] = 'in-progress-60-of-105'
w['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63. Resolve the remaining 68 explicit first-pass readings before structured derivatives.'
w['tamil_transcription_draft_pages'] = 45
w['tamil_transcription_verified_pages'] = 60
w['tamil_transcription_review_pages'] = 0
w['total_verified_pages'] = 60
w['total_review_pages'] = 0
w['open_first_pass_uncertainty_markers'] = 68
w['fidelity_audit_verified_pdf_pages'] = '5-64'
w['fidelity_audit_verified_logical_printed_pages'] = '3-62'
w['fidelity_audit_next_pdf_page'] = 65
write(path, json.dumps(arr, ensure_ascii=False, indent=2) + '\n')

# 10. Master handover: update the two active Ammayappan checkpoint blocks.
path = 'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
text = read(path)
text = replace_once(text,
    '**PDF 5–63 verified (59/105), PDF 64 / logical p.62 in review, 45 draft pages, and 69 unresolved first-pass readings**',
    '**PDF 5–64 verified (60/105), 45 draft pages, and 68 unresolved first-pass readings**',
    'master summary first')
text = replace_once(text,
    '**Ammayappan fidelity checkpoint: first pass 105/105 assembled, PDF 5–63 verified (59/105), PDF 64 / logical p.62 review, 45 draft pages, and 69 unresolved first-pass readings**. The next gate is PDF 64 / logical p.62.',
    '**Ammayappan fidelity checkpoint: first pass 105/105 assembled, PDF 5–64 verified (60/105), 45 draft pages, and 68 unresolved first-pass readings**. The next source page is PDF 65 / logical p.63.',
    'master synchronized summary')
text = replace_once(text,
    '- fidelity audit: **PDF 5–63 / logical pp.3–61 verified — 59/105**;\n- review: **PDF 64 / logical p.62 — marker 47 unresolved**;\n- remaining draft pages: **45 — PDF 65–109**;\n- open first-pass uncertainty markers: **69**;',
    '- fidelity audit: **PDF 5–64 / logical pp.3–62 verified — 60/105**;\n- review: **none**;\n- remaining draft pages: **45 — PDF 65–109**;\n- open first-pass uncertainty markers: **68**;',
    'master section16')
write(path, text)

# 11. Status consistency audit.
path = 'docs/STATUS_CONSISTENCY_AUDIT.md'
text = read(path)
text = replace_once(text,
    '**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–63 visually verified (59/105), PDF 64 review, 45 draft pages, 1 review page, and 69 open first-pass readings; next gate PDF 64 / logical p.62.**',
    '**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–64 visually verified (60/105), 45 draft pages, 0 review pages, and 68 open first-pass readings; next PDF 65 / logical p.63.**',
    'status result')
text = replace_once(text,
    '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–63 fidelity-verified (59/105); PDF 64 review; 45 draft; 69 open markers** |',
    '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–64 fidelity-verified (60/105); 45 draft; 68 open markers** |',
    'status matrix')
text = replace_once(text,
    '- rendered-scan fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified; PDF 64 / logical p.62 review**;',
    '- rendered-scan fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified**;',
    'status audit line')
text = replace_once(text,
    '- verified / draft / review pages: **59 / 45 / 1**;',
    '- verified / draft / review pages: **60 / 45 / 0**;',
    'status counts')
text = replace_once(text,
    '- open first-pass uncertainty markers: **69**;',
    '- open first-pass uncertainty markers: **68**;',
    'status markers')
text = replace_once(text,
    'Exact next activity: **reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan**. Do not advance to PDF 65 while PDF 64 remains review.',
    'Exact next activity: **continue at PDF 65 / logical printed p.63 and adjudicate the remaining 68 uncertainty markers in source order**.',
    'status next')
write(path, text)

# 12. Assertions across active surfaces.
full = read('works/ammaiyappan/transcription/full-text.md')
assert '<!-- source: pdf=64 printed=62 status=verified -->' in full
assert '⟦கிளியும் மெச்சிவிருப்பும்' not in full
assert resolved47 in full
idx = json.loads(read('works/ammaiyappan/transcription/index.json'))
assert (idx['verified_pages'], idx['draft_pages'], idx['review_pages'], idx['open_uncertainty_markers']) == (60, 45, 0, 68)
assert idx['next_pdf_page'] == 65 and idx['next_printed_page'] == 63
reg = next(x for x in json.loads(read('data/works.json')) if x.get('id') == 'ammaiyappan')
assert reg['canonical_tamil_verified_pages'] == 60
assert reg['total_verified_pages'] == 60
assert reg['open_first_pass_uncertainty_markers'] == 68
assert reg['fidelity_audit_verified_pdf_pages'] == '5-64'
assert reg['fidelity_audit_next_pdf_page'] == 65

print('PASS: Ammayappan PDF 64 marker 47 resolved; 60/105 verified, 45 draft, 0 review, 68 open; next PDF 65.')
