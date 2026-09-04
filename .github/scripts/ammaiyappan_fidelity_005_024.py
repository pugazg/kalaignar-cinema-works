import json
import re
from pathlib import Path

ROOT = Path('.')


def must_replace(text, old, new, label, count=1):
    n = text.count(old)
    if n != count:
        raise RuntimeError(f'{label}: expected {count} occurrence(s), found {n}')
    return text.replace(old, new, count)


def replace_section(text, heading, replacement, label):
    pat = re.compile(r'(?ms)^' + re.escape(heading) + r'\n.*?(?=^## |\Z)')
    out, n = pat.subn(replacement.rstrip() + '\n\n', text, count=1)
    if n != 1:
        raise RuntimeError(f'{label}: section {heading!r} expected once, found {n}')
    return out


# ---------------------------------------------------------------------------
# Canonical full text: apply only to PDF 5-24 prefix.
# ---------------------------------------------------------------------------
ft_path = ROOT / 'works/ammaiyappan/transcription/full-text.md'
ft = ft_path.read_text(encoding='utf-8')
boundary = '<!-- source: pdf=25 printed=23 status=draft -->'
if boundary not in ft:
    raise RuntimeError('PDF 25 boundary anchor not found')
prefix, suffix = ft.split(boundary, 1)

old_status = 'Status: **first pass in progress**. The rendered scan controls. `draft` means transcribed from the scan but not yet through the separate full visual fidelity audit.'
new_status = 'Status: **visual fidelity audit in progress**. PDF 5–24 / logical pp.3–22 are scan-verified; PDF 25–109 remain draft. The rendered scan controls canonical Tamil.'
prefix = must_replace(prefix, old_status, new_status, 'full-text phase status')

corrections = [
    # PDF 5-14: scan-backed corrections already visually adjudicated in the prior batch.
    ('முத் : ஒன்றுமில்லை...', 'முத் : ஒன்றுமில்ல...', 'PDF5 ஒன்றுமில்ல'),
    ('பார்த்தது போல ஞாபகம்!...', 'பார்த்தது போலே ஞாபகம்!...', 'PDF5 போலே'),
    ('சுக : ஓஹோ! அதுவும் உன்னுடையதுதானே?', 'சுக : ஓகோ! அதுவும் உன்னுடையதுதானு?', 'PDF5 ஓகோ'),
    ('சுக : சரிதான். உலகத்திலே', 'சுக : சரிதான், உலகத்திலே', 'PDF6 punctuation'),
    ('முத் : ⟦ஊர் கூடம்?⟧.', 'முத் : ஊர் கூடம்.', 'marker1'),
    ('நண் : என்ன முத்தண்ணு ⟦சுகந்தானு?⟧?', 'நண் : என்ன முத்தண்ணு சுகந்தானு?', 'marker2'),
    ('பானையக்கார பலதேவர்', 'பாளையக்கார பலதேவர்', 'PDF6 பாளையக்கார'),
    ('⟦தோலத் தரிப்பது?⟧', 'தோலத் தரிப்பது', 'marker3'),
    ('குறும்புத் தனமாக கேள்விகளைக் கேட்காதே;', 'குறும்புத் தனமாக கேள்விகளை கேட்டாதே;', 'PDF7 கேள்விகளை கேட்டாதே'),
    ('உனக்கு என் வீட்டில் அந்த அறையை வாடகைக்குத் தர அவ்வளவு தயங்கினேன்', 'உனக்கு என் வீட்டில் அந்த அறையை வாடகைக்குத்தர அவ்வளவு தயங்கினேன்', 'PDF8 வாடகைக்குத்தர'),
    ('வேதா : இல்லை ஊதியம் வாங்குகிற இடத்தில்', 'வேதா : இல்ல ஊதியம் வாங்குகிற இடத்தில்', 'PDF8 இல்ல'),
    ('வேங்கை நாட்டானை விவாகம்', 'வேங்கை நாட்டாரை விவாகம்', 'PDF9 நாட்டாரை'),
    ('[பூங்காவனம் முத்தனுக்காக பழங்கள் எடுத்துக் கொண்டிருக்கிறாள்.]', '[பூங்காவனம் முத்தனுக்காக பழங்களை எடுத்துக் கொண்டிருக்கிறாள்.]', 'PDF9 பழங்களை'),
    ('உனக்கு அண்ணனைப் ⟦பிறந்து?⟧ விட்ட,', 'உனக்கு அண்ணனைப் பிறந்து விட்டு,', 'marker4'),
    ('பூங் : வழக்கம் தானே அண்ணா இது!...', 'பூங் : வழக்கம் தானே அண்ணு இது!...', 'PDF9 அண்ணு'),
    ('நீ அந்த வேங்கையூர்த்தாரை விவாகம்', 'நீ அந்த வேங்கைபுரத்தாரை விவாகம்', 'PDF10 வேங்கைபுரத்தாரை'),
    ('பல வருட காலமாக உன்னைத் திருமணம்', 'பல வருஷ காலமாக உன்னைத் திருமணம்', 'PDF10 வருஷ'),
    ('பிரமச்சரிய விரதம் பூண்டிருக்கிறேன்...வேங்கை', 'பிரமச்சரிய விரதம் பூண்டிருக்கிறான்....வேங்கை', 'PDF10 பூண்டிருக்கிறான்'),
    ('பூங் : அண்ணை...திருமணப் பேச்சு', 'பூங் : அண்ண...திருமணப் பேச்சு', 'PDF10 அண்ண'),
    ('பருவமோ இல்லை எனக்கு', 'பருவமோ இல்ல எனக்கு', 'PDF10 இல்ல'),
    ('## மாடம்', '## மடாலயம்', 'PDF10 heading'),
    ('கடலை வற்ற வைப்பர்; ⟦கசந்ததிலே?⟧ மிதந்திடுவர்', 'கடலை வற்ற வைப்பார்; கசந்திலே மிதந்திடுவர்', 'marker5'),
    ('மருந்துவத்தால் தீர்க்கலாம்', 'மருத்துவத்தால் தீர்க்கலாம்', 'PDF11 மருத்துவத்தால்'),
    ('அந்த புதையல் என் கண்ணிலே', 'அந்த புதையலை என் கண்ணிலே', 'PDF12 புதையலை'),
    ('பொன்னே வைரமோ அல்ல', 'பொன்னோ வைரமோ அல்ல', 'PDF12 பொன்னோ'),
    ('ஒரு அடி விழுகிறது...', 'ஒரு அடிவிழுகிறது...', 'PDF13 அடிவிழுகிறது'),
    ('⟦துப்புக்கீழே?⟧', 'துப்புகிறே', 'marker6'),
    ('⟦நன்றுயிருக்கிறது?⟧', 'நன்றுயிருக்கிறது', 'marker7'),
    ('பானையக்காரர் சொத்தை', 'பாளையக்காரர் சொத்தை', 'PDF13 பாளையக்காரர்'),
    ('கொட்டய்யா பட்டத்தை;', 'கொட்டப்பா பட்டத்தை;', 'PDF14 கொட்டப்பா'),
    ('⟦இப்ப என்னு?⟧ வாள் பயிற்சி', 'இப்ப என்னு வாள் பயிற்சி', 'marker8'),
    ('போகிறானுக்கும்......பெரிய வீராதி வீரர்...', 'போகிறாருக்கும்......பெரிய வீராதி வீரா...', 'PDF14 போகிறாருக்கும் வீரா'),
    ('எந்தக் கையிலே கத்திவசிக்கிறது', 'எந்தக்கையிலே கத்திவசிக்கிறது', 'PDF14 எந்தக்கையிலே'),
    ('முத் : ஓ...வாள் வீரனே விடலாம்.', 'முத் : ஓ...வாள் வீரனு விடலாம்.', 'PDF14 வாள் வீரனு'),
    ('பரவா இல்லை...வாள் வீரர்', 'பரவா இல்ல...வாள் வீரர்', 'PDF14 பரவா இல்ல'),

    # PDF 15-24: current rendered-scan fidelity batch.
    ('சுக : இலக்கணமே எனக்குத் தேவை இல்லை.', 'சுக : இலக்கணமே எனக்குத் தேவை இல்ல.', 'PDF15 இல்ல'),
    ('பூங் : பரவா இல்லை முத்தா, நானே கட்டி விடுகிறேன்.', 'பூங் : பரவா இல்ல முத்தா, நானே கட்டி விடுகிறேன்.', 'PDF16 பரவா இல்ல'),
    ('பூங் : ஒன்றுமில்லை முத்தா...இந்தா இதை சாப்பிடு', 'பூங் : ஒன்றுமில்ல முத்தா...இந்தா இதை சாப்பிடு', 'PDF16 ஒன்றுமில்ல'),
    ('திரிசங்கு : இல்லை தம்பி. எனக்குத்தான்.', 'திரிசங்கு : இல்ல தம்பி. எனக்குத்தான்.', 'PDF16 இல்ல 1'),
    ('திரிசங்கு : இல்லை தம்பி இல்லை. கல்யாணத்துக்குப் பெண் வேண்டுமாம்.', 'திரிசங்கு : இல்ல தம்பி இல்ல. கல்யாணத்துக்குப் பெண் வேண்டுமாம்.', 'PDF16 இல்ல 2'),
    ('வெளவாலே வா என்று அழைப்பதில்லை. சரி அதுபோல', 'வெளவாலே வா என்று அழைப்பதில்ல. சரி அதுபோல', 'PDF17 அழைப்பதில்ல'),
    ('திரிசங்கு : இல்லை தம்பி. இது காக்கை அடை காத்த குயிலின் குஞ்சு.', 'திரிசங்கு : இல்ல தம்பி. இது காக்கை அடை காத்த குயிலின் குஞ்சு.', 'PDF17 இல்ல'),
    ('திரி : எங்கம்மா போயிட்டே?', 'திரி : ஏங்கம்மா போயிட்டே?', 'PDF19 ஏங்கம்மா'),
    ('சீ...சீ...உள்ளேயாரு கூப்பிட்டது...?', 'சீ...சீ...உன்னையாரு கூப்பிட்டது...?', 'PDF19 உன்னையாரு'),
    ('நீங்கள் பரலோகக்காரர் பலதேவரின் மகன்', 'நீங்கள் பாளையக்காரர் பலதேவரின் மகன்', 'PDF19 பாளையக்காரர்'),
    ('இது வைத்தியமில் லாத வியாதி...⟦கண்ணெடு கண்ணோக் கொக்கின்?⟧', 'இது வைத்தியமில்லாத வியாதி...கண்ணொடு கண்ணோக் கொக்கின்', 'marker9'),
    ('முத் : இல்லை...இல்லை...மன்னிக்கவும்;', 'முத் : இல்ல...இல்ல...மன்னிக்கவும்;', 'PDF20 இல்ல'),
    ('⟦சிறுத்தை பூரான்?⟧ வேங்கை நகரின் மீது', 'சிறுத்தை யூரான் வேங்கை நகரின் மீது', 'marker10'),
    ('முயற்சியில் இறங்கி தடைகட்டாடென', 'முயற்சியில் இறங்கித் தடைகட்டாடென', 'PDF21 இறங்கித்'),
    ('பலதேவர் : அதெல்லாம் ஒன்றுமில்லை.', 'பலதேவர் : அதெல்லாம் ஒன்றுமில்ல.', 'PDF22 ஒன்றுமில்ல'),
    ('பேச்சிலே இனிமை இருக்கிறதாம். கையிலே என்னமோ', 'பேச்சிலே இனிமை இருக்கிறதாம்-கையிலே என்னமோ', 'PDF22 punctuation'),
    ('திரிசங்கு : இல்லை தம்பி...', 'திரிசங்கு : இல்ல தம்பி...', 'PDF22 இல்ல'),
    ('சுகதேவ் : விரலிலே மோதிரம் இருக்கு...', 'சுகதேவ் : விரல்லே மோதிரம் இருக்கு...', 'PDF22 விரல்லே'),
    ('திரிசங்கு : அது இல்லை தம்பி-போங்க நீங்க-', 'திரிசங்கு : அது இல்ல தம்பி-போங்க நீங்க-', 'PDF23 அது இல்ல'),
    ('நம்ப நாள் நிலையத்திலே கம்பராமாயணம்', 'நம்ப நூல் நிலையத்திலே கம்பராமாயணம்', 'PDF23 நூல் நிலையம்'),
    ('முதற்கால் வாசி ராமாயணமே', 'முக்கால் வாசி ராமாயணமே', 'PDF23 முக்கால் வாசி'),
    ('⟦கோமுனியுடன் வரு கொண்டல் என்றபின் தாமரைக் கண்ணினன் என்ற தன்மையால்...ஆம்...அவனே கொல் என்று ஐய நீங்கினள்...வாடமேகலையி வளர்ந்தது...?⟧', 'கோமுனியுடன் வரு கொண்டல் என்றபின் தாமரைக் கண்ணினன் என்ற தன்மையால்...ஆம்...அவனே கொல் என்று ஐய நீங்கினள்...வாமமேகலையி வளர்ந்தது...', 'marker11'),
    ('வா வா அதைக் தேடலாம்.', 'வா வா அதைத் தேடலாம்.', 'PDF23 அதைத் தேடலாம்'),
    ('இந்தப் பறக்கா உன்னை அளிக்கப் போகிறார்?', 'இந்தப் பாரிக்கா உன்னை அளிக்கப் போகிறார்?', 'PDF24 பாரிக்கா'),
    ('உன் அழகன் எல்லையை இன்னும் அறிய முடியாத என் கண்கள்.', 'உன் அழகின் எல்லையை இன்னும் அறிய முடியாத என் கண்கள்.', 'PDF24 அழகின்'),
    ('அழகுச் சோலையின் சுறறப் புறங்களிலே—', 'அழகுச் சோலையின் சுற்றப் புறங்களிலே—', 'PDF24 சுற்றப்'),
]

for old, new, label in corrections:
    prefix = must_replace(prefix, old, new, label)

# Mark every source anchor PDF 5-24 verified.
def verify_anchor(match):
    pdf = int(match.group(1))
    body = match.group(2)
    if 5 <= pdf <= 24:
        return f'<!-- source: pdf={pdf}{body}status=verified -->'
    return match.group(0)

prefix = re.sub(r'<!-- source: pdf=(\d+)(.*?)status=draft -->', verify_anchor, prefix)
verified_anchors = re.findall(r'<!-- source: pdf=(\d+).*?status=verified -->', prefix)
verified_anchors = [int(x) for x in verified_anchors if 5 <= int(x) <= 24]
if verified_anchors != list(range(5, 25)):
    raise RuntimeError(f'verified anchor sequence mismatch: {verified_anchors}')
if '⟦' in prefix or '⟧' in prefix:
    raise RuntimeError('unresolved uncertainty marker remains in PDF 5-24 prefix')

ft_path.write_text(prefix + boundary + suffix, encoding='utf-8')

# ---------------------------------------------------------------------------
# Fidelity audit ledger.
# ---------------------------------------------------------------------------
audit_path = ROOT / 'works/ammaiyappan/notes/fidelity-audit.md'
audit_path.write_text('''# அம்மையப்பன் — canonical Tamil visual fidelity audit

Status: **in progress**.

Controlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`  
Canonical range: **PDF 5–109 / logical printed pp.3–107 — 105 pages**

## Audit rules

- The rendered scan is controlling evidence.
- OCR, film audio, subtitles, web text, semantic expectation and later editions do not repair canonical Tamil.
- Preserve source-visible spelling, colloquial forms, speaker labels, headings, punctuation and stage directions.
- A page becomes `verified` only after the entire visible page has been compared against the scan and every source-supported correction has been applied.
- If a reading cannot be supported confidently from the scan, retain it explicitly as unresolved and do not mark that page verified.
- Structured derivatives remain blocked until all 105 canonical pages are verified.

## Progress

| Range | Verified pages | Review pages | Remaining draft pages | Status |
|---|---:|---:|---:|---|
| PDF 5–14 / logical pp.3–12 | 10 | 0 | 0 | verified |
| PDF 15–24 / logical pp.13–22 | 10 | 0 | 0 | verified |
| PDF 25–109 / logical pp.23–107 | 0 | 0 | 85 | pending |
| **Total** | **20** | **0** | **85** | **in progress** |

Open first-pass uncertainty markers after this audit checkpoint: **105** (markers **1–11 resolved**; markers **12–116 remain for later source-order review**).

## PDF 5–14 / logical pp.3–12 — verified

All ten pages were compared directly against the rendered scan. The eight explicit first-pass uncertainties in this range were adjudicated from the scan and their markers removed.

Resolved marker readings:

1. PDF 6: `ஊர் கூடம்`
2. PDF 6: `சுகந்தானு`
3. PDF 6: `தோலத் தரிப்பது`
4. PDF 9: `பிறந்து விட்டு`
5. PDF 10: `கசந்திலே`
6. PDF 13: `துப்புகிறே`
7. PDF 13: `நன்றுயிருக்கிறது`
8. PDF 14: `இப்ப என்னு`

Additional scan-backed corrections include `மடாலயம்`, `பாளையக்கார`, `வேங்கைபுரத்தாரை`, `மருத்துவத்தால்`, `பொன்னோ வைரமோ`, and source-colloquial `இல்ல` forms. These are source restorations, not modernization.

## PDF 15–24 / logical pp.13–22 — verified

All ten pages were compared directly against the rendered scan. Markers 9–11 were resolved from the printed glyphs, and several non-marker first-pass drifts were corrected.

Resolved marker readings:

9. PDF 19: `கண்ணொடு கண்ணோக் கொக்கின்`
10. PDF 21: `சிறுத்தை யூரான்`
11. PDF 23: `கோமுனியுடன் வரு கொண்டல் என்றபின் தாமரைக் கண்ணினன் என்ற தன்மையால்...ஆம்...அவனே கொல் என்று ஐய நீங்கினள்...வாமமேகலையி வளர்ந்தது...`

Other source-backed restorations in this batch include:

- PDF 15: source `இலக்கணமே எனக்குத் தேவை இல்ல.`;
- PDF 16–17: retained repeated source-colloquial `இல்ல` forms rather than normalized `இல்லை`;
- PDF 19: `ஏங்கம்மா`, `உன்னையாரு`, and `பாளையக்காரர் பலதேவரின் மகன்`;
- PDF 21: source sandhi `இறங்கித் தடைகட்டாடென`;
- PDF 22: `விரல்லே மோதிரம் இருக்கு...`;
- PDF 23: `நூல் நிலையத்திலே`, `முக்கால் வாசி ராமாயணமே`, and `அதைத் தேடலாம்`;
- PDF 24: `பாரிக்கா`, `உன் அழகின் எல்லையை`, and `சுற்றப் புறங்களிலே`.

No unresolved scan reading remains in PDF 5–24.

## Exact next activity

Continue the rendered-scan fidelity audit at **PDF 25 / logical printed p.23**, in source order. Adjudicate markers **12 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.
''', encoding='utf-8')

# ---------------------------------------------------------------------------
# Authoritative transcription index.
# ---------------------------------------------------------------------------
idx_path = ROOT / 'works/ammaiyappan/transcription/index.json'
idx = json.loads(idx_path.read_text(encoding='utf-8'))
idx['status'] = 'fidelity-audit-in-progress'
idx['draft_pages'] = 85
idx['verified_pages'] = 20
idx['review_pages'] = 0
idx['open_uncertainty_markers'] = 105
fa = idx.setdefault('fidelity_audit', {})
fa['status'] = 'in-progress'
fa['canonical_range_audit_complete'] = False
fa['audited_pages'] = 20
fa['verified_pages'] = 20
fa['review_pages'] = 0
fa['unresolved_source_readings'] = 105
fa['verified_pdf_range'] = [5, 24]
fa['verified_logical_printed_range'] = [3, 22]
idx['next_pdf_page'] = 25
idx['next_printed_page'] = 23
idx['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 25 / logical printed p.23. Resolve remaining first-pass uncertainties occurrence-by-occurrence and keep structured derivatives blocked until all 105 canonical pages are verified.'
idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------------------------------------------------------------------------
# Work-local prose/status mirrors.
# ---------------------------------------------------------------------------
tr_path = ROOT / 'works/ammaiyappan/transcription/README.md'
tr = tr_path.read_text(encoding='utf-8')
tr = must_replace(tr, '- verified pages: **0**;', '- verified pages: **20**;', 'transcription README verified')
tr = must_replace(tr, '- open first-pass uncertain readings: **116**;', '- open first-pass uncertain readings: **105**;', 'transcription README markers')
tr = must_replace(tr, '- full rendered-scan visual fidelity audit: **not-started**.', '- full rendered-scan visual fidelity audit: **in-progress — PDF 5–24 / logical pp.3–22 verified (20/105)**.', 'transcription README audit')
tr = re.sub(r'(?ms)^## Exact next activity\n\n.*\Z', '## Exact next activity\n\nContinue the **rendered-scan visual fidelity audit at PDF 25 / logical printed p.23**. Compare the entire page directly against the controlling scan, adjudicate remaining first-pass uncertainties occurrence-by-occurrence, and keep structured derivatives blocked until all 105 canonical pages are verified.\n', tr)
tr_path.write_text(tr, encoding='utf-8')

wr_path = ROOT / 'works/ammaiyappan/README.md'
wr = wr_path.read_text(encoding='utf-8')
wr = must_replace(wr, '- verified pages: **0**;', '- verified pages: **20**;', 'work README verified')
wr = must_replace(wr, '- open first-pass uncertainty markers: **116**;', '- open first-pass uncertainty markers: **105**;', 'work README markers')
wr = must_replace(wr, '- visual fidelity audit: **not-started**.', '- visual fidelity audit: **in-progress — PDF 5–24 / logical pp.3–22 verified (20/105)**.', 'work README audit')
wr = must_replace(wr, '| Visual fidelity audit | **not-started** |', '| Visual fidelity audit | **in-progress — 20/105 verified** |', 'work README table audit')
wr = must_replace(wr, '| Verified Tamil pages | **0/105** |', '| Verified Tamil pages | **20/105** |', 'work README table verified')
wr = re.sub(r'(?ms)^## Exact next activity\n\n.*\Z', '## Exact next activity\n\n**Continue the rendered-scan visual fidelity audit at PDF 25 / logical printed p.23.** Resolve the remaining **105** explicit first-pass readings occurrence-by-occurrence, upgrade pages only after full-page direct scan comparison, and keep all structured derivatives blocked until the complete 105-page canonical range is verified.\n', wr)
wr_path.write_text(wr, encoding='utf-8')

# metadata.yaml
meta_path = ROOT / 'works/ammaiyappan/metadata.yaml'
meta = meta_path.read_text(encoding='utf-8')
meta = must_replace(meta, '  status: draft-complete-awaiting-fidelity-audit\n', '  status: fidelity-audit-in-progress\n', 'metadata transcription status')
old_progress = '''  verified_pages: 0\n  draft_pages: 105\n  review_pages: 0\n  open_first_pass_uncertainty_markers: 116\n  next_pdf_page: 5\n  next_logical_printed_page: 3\n  next_action: "Begin the separate rendered-scan visual fidelity audit at PDF 5 / logical printed p.3 and continue through PDF 109. Adjudicate all 116 explicit uncertainty markers occurrence-by-occurrence before any structured derivatives."'''
new_progress = '''  verified_pages: 20\n  draft_pages: 85\n  review_pages: 0\n  open_first_pass_uncertainty_markers: 105\n  next_pdf_page: 25\n  next_logical_printed_page: 23\n  next_action: "Continue the rendered-scan visual fidelity audit at PDF 25 / logical printed p.23; 20/105 pages are verified and 105 explicit first-pass readings remain unresolved."'''
meta = must_replace(meta, old_progress, new_progress, 'metadata progress block')
old_fidelity = '''fidelity_audit:\n  status: not-started\n  canonical_range_audit_complete: false\n  audited_pages: 0\n  verified_pages: 0\n  unresolved_source_readings: 116'''
new_fidelity = '''fidelity_audit:\n  status: in-progress\n  canonical_range_audit_complete: false\n  audited_pages: 20\n  verified_pages: 20\n  review_pages: 0\n  unresolved_source_readings: 105\n  verified_pdf_pages: "5-24"\n  verified_logical_printed_pages: "3-22"'''
meta = must_replace(meta, old_fidelity, new_fidelity, 'metadata fidelity block')
meta = must_replace(meta, '  visual_fidelity_audit: not-started\n', '  visual_fidelity_audit: in-progress-20-of-105\n', 'metadata status audit')
meta = re.sub(r'(?m)^next_action: ".*"$', 'next_action: "Continue the rendered-scan visual fidelity audit at PDF 25 / logical printed p.23; resolve the remaining 105 explicit first-pass readings and verify all 105 canonical pages before starting structured derivatives."', meta, count=1)
meta_path.write_text(meta, encoding='utf-8')

# project handover
ph_path = ROOT / 'works/ammaiyappan/PROJECT_HANDOVER.md'
ph = ph_path.read_text(encoding='utf-8')
ph = must_replace(ph, '- state: **draft-complete**, verified pages **0**;', '- state: **draft-complete**, verified pages **20**;', 'handover verified')
ph = must_replace(ph, '- open uncertainty markers: **116**;', '- open uncertainty markers: **105**;', 'handover markers')
ph = must_replace(ph, '- visual fidelity audit: **not-started**.', '- visual fidelity audit: **in-progress — PDF 5–24 / logical pp.3–22 verified (20/105)**.', 'handover audit')
ph = must_replace(ph, '- visual fidelity audit: **not-started — 0/105 verified**;', '- visual fidelity audit: **in-progress — 20/105 verified; next PDF 25 / logical p.23**;', 'handover phase gate')
ph = re.sub(r'(?ms)^## Exact next activity\n\n> .*\Z', '## Exact next activity\n\n> **Continue the separate rendered-scan visual fidelity audit at PDF 25 / logical printed p.23 and proceed in source order through PDF 109. Compare each full page directly with the controlling scan, adjudicate the remaining 105 explicit first-pass uncertainty markers occurrence-by-occurrence, preserve locked source verdicts, and upgrade pages only after direct page-level visual comparison. Do not start scene/dialogue/character derivatives until all 105 canonical pages pass the audit.**\n', ph)
ph_path.write_text(ph, encoding='utf-8')

# ---------------------------------------------------------------------------
# Structured repository registry.
# ---------------------------------------------------------------------------
works_path = ROOT / 'data/works.json'
works = json.loads(works_path.read_text(encoding='utf-8'))
rec = next(x for x in works if x.get('id') == 'ammaiyappan')
rec['canonical_tamil_transcription'] = 'fidelity-audit-in-progress'
rec['canonical_tamil_draft_pages'] = 85
rec['canonical_tamil_verified_pages'] = 20
rec['canonical_tamil_review_pages'] = 0
rec['canonical_tamil_open_uncertainty_markers'] = 105
rec['tamil_fidelity_audit'] = 'in-progress-20-of-105'
rec['next_action'] = 'Continue the rendered-scan visual fidelity audit at PDF 25 / logical printed p.23. Resolve the remaining 105 explicit first-pass readings before structured derivatives.'
rec['tamil_transcription'] = 'fidelity-audit-in-progress'
rec['tamil_transcription_draft_pages'] = 85
rec['tamil_transcription_verified_pages'] = 20
rec['tamil_transcription_review_pages'] = 0
rec['total_verified_pages'] = 20
rec['total_review_pages'] = 0
rec['open_first_pass_uncertainty_markers'] = 105
rec['fidelity_audit_verified_pdf_pages'] = '5-24'
rec['fidelity_audit_verified_logical_printed_pages'] = '3-22'
rec['fidelity_audit_next_pdf_page'] = 25
works_path.write_text(json.dumps(works, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------------------------------------------------------------------------
# Root README: replace only Ammayappan status section.
# ---------------------------------------------------------------------------
root_readme = ROOT / 'README.md'
rr = root_readme.read_text(encoding='utf-8')
amma_section = '''## அம்மையப்பன் status

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
- visual fidelity audit: **in-progress — PDF 5–24 / logical pp.3–22 verified**;
- verified / draft / review pages: **20 / 85 / 0**;
- open first-pass uncertainty markers: **105**;
- structured derivatives / English / reader: **blocked pending complete verified Tamil**.

**Next:** continue the rendered-scan visual fidelity audit at **PDF 25 / logical printed p.23** and adjudicate the remaining **105** explicit first-pass uncertainty markers. Do not start scene/dialogue/character derivatives until all 105 canonical pages are verified.
'''
rr = replace_section(rr, '## அம்மையப்பன் status', amma_section, 'root README Ammayappan')
root_readme.write_text(rr, encoding='utf-8')

# ---------------------------------------------------------------------------
# Master handover: high-level bullet + synchronization paragraph + Section 16.
# ---------------------------------------------------------------------------
mh_path = ROOT / 'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
mh = mh_path.read_text(encoding='utf-8')
old_bullet = '- **Ammayappan** — 111-page image-only screenplay/dialogue source; source intake and whole-scan mapping complete; canonical Tamil first pass **draft-complete 105/105 across PDF 5–109 / logical pp.3–107**; continuous `full-text.md` assembled through PDF 109; assembly QA **PASS — 105 exact source anchors, 0 missing, 0 duplicate**; **116** explicit unresolved first-pass readings; verified Tamil **0/105**; separate rendered-scan visual fidelity audit is the exact next gate; structured derivatives remain blocked.'
new_bullet = '- **Ammayappan** — 111-page image-only screenplay/dialogue source; source intake and whole-scan mapping complete; canonical Tamil first pass **draft-complete 105/105 across PDF 5–109 / logical pp.3–107**; continuous `full-text.md` assembled through PDF 109; assembly QA **PASS — 105 exact source anchors, 0 missing, 0 duplicate**; rendered-scan fidelity audit **in progress through PDF 24 / logical p.22 — 20/105 verified**; **105** explicit unresolved first-pass readings remain; structured derivatives remain blocked.'
mh = must_replace(mh, old_bullet, new_bullet, 'master high-level bullet')
old_sync = '`data/works.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` are synchronized to the active **Ammayappan first-pass closure checkpoint: 105/105 draft pages, continuous `full-text.md` through PDF 109, assembly QA PASS, 116 unresolved first-pass readings, and 0/105 verified pages**. The separate rendered-scan visual fidelity audit is now the required next gate.'
new_sync = '`data/works.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` are synchronized to the active **Ammayappan fidelity checkpoint: first pass 105/105 assembled, PDF 5–24 visually verified (20/105), 85 draft pages, 0 review pages, and 105 unresolved first-pass readings**. The next source page is PDF 25 / logical p.23.'
mh = must_replace(mh, old_sync, new_sync, 'master sync paragraph')
section16 = '''## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- source intake: **complete**;
- whole-scan inspection: **111/111 complete**;
- structural intake mapping: **verified — 58 heading/transition occurrences / 37 distinct forms**;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107 — 105 pages**;
- source-numbered scenes: **none**;
- locked scan reading: PDF 56 / p.54 = **`பழுதார் வீதி`**;
- user scan verdict: PDF 107 / p.105 = **`தூக்குமேடை`**, not `தாக்குமேடை`;
- canonical Tamil first pass: **draft-complete — 105/105 pages**;
- continuous assembled transcription: `works/ammaiyappan/transcription/full-text.md` through **PDF 109**;
- first-pass assembly QA: **PASS — 105 exact source anchors / 0 missing / 0 duplicate**;
- rendered-scan visual fidelity audit: **in-progress — PDF 5–24 / logical pp.3–22 verified**;
- verified / draft / review pages: **20 / 85 / 0**;
- open first-pass uncertainty markers: **105**;
- scene/dialogue/character derivatives: **blocked pending verified Tamil**;
- English / reader / Reading Room integration: **blocked**.

Exact next activity: **continue the rendered-scan visual fidelity audit at PDF 25 / logical printed p.23 and proceed in source order. Resolve the remaining 105 explicit uncertainty markers occurrence-by-occurrence and mark pages verified only after complete direct scan comparison. Structured derivatives remain blocked until all 105 canonical pages are verified.**
'''
mh = replace_section(mh, '## 16. Ammayappan active checkpoint', section16, 'master Section 16')
mh_path.write_text(mh, encoding='utf-8')

# ---------------------------------------------------------------------------
# Repository status consistency audit.
# ---------------------------------------------------------------------------
sa_path = ROOT / 'docs/STATUS_CONSISTENCY_AUDIT.md'
sa = sa_path.read_text(encoding='utf-8')
sa = must_replace(sa,
    '**PASS — current status mirrors synchronized across all seven works at the Ammayappan canonical-Tamil first-pass closure: 105/105 draft pages assembled through PDF 109, assembly QA PASS, 116 open first-pass readings, visual fidelity audit next.**',
    '**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–24 visually verified (20/105), 85 draft pages, 0 review pages, and 105 open first-pass readings; next PDF 25 / logical p.23.**',
    'status audit result')
sa = must_replace(sa,
    '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete across PDF 5–109; assembly QA PASS; 116 open markers; 0 verified pages** | scene/dialogue/character blocked pending verified Tamil | blocked | blocked |',
    '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–24 fidelity-verified (20/105); 85 draft; 105 open markers** | scene/dialogue/character blocked pending complete verified Tamil | blocked | blocked |',
    'status audit matrix')
checkpoint = '''## Ammayappan canonical-Tamil first-pass closure checkpoint

- source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`;
- PDF pages: **111**;
- source SHA-256: `eda6468a57022b418f44851a0013b090469bc6f4be44a682487800658771720d`;
- main screenplay/dialogue: **PDF 5–109 / logical printed pp.3–107 — 105 pages**;
- PDF 110–111: advertisement/back matter, excluded from canonical screenplay;
- structural intake map: **verified — 58 heading/transition occurrences / 37 distinct forms**;
- source-numbered scenes: **none**;
- locked PDF 56 / printed p.54: **`பழுதார் வீதி`**;
- locked PDF 107 / printed p.105: **`தூக்குமேடை`**; rejected `தாக்குமேடை` absent;
- canonical Tamil first pass: **draft-complete — 105/105 pages**;
- continuous assembled transcription: `works/ammaiyappan/transcription/full-text.md` through **PDF 109**;
- assembly QA: `works/ammaiyappan/transcription/ASSEMBLY_QA.md` — **PASS**;
- source anchors: **105 / exact PDF 5→109 order / 0 missing / 0 duplicate**;
- rendered-scan fidelity audit: **in-progress — PDF 5–24 / logical pp.3–22 verified**;
- verified / draft / review pages: **20 / 85 / 0**;
- open first-pass uncertainty markers: **105**;
- scene / dialogue / character derivatives: **blocked pending complete verified Tamil**;
- song/performance authorship gate: **not-started**;
- English translation / reader / Reading Room integration: **blocked**.

The canonical Tamil first-pass transcription and assembly gate remains closed. The separate source-fidelity gate is now active. Exact next activity: **continue at PDF 25 / logical printed p.23**, compare the entire page directly against the controlling scan, and adjudicate remaining uncertainty markers in source order. Structured derivatives remain blocked until all 105 pages pass.
'''
sa = replace_section(sa, '## Ammayappan canonical-Tamil first-pass closure checkpoint', checkpoint, 'status audit checkpoint')
sa_path.write_text(sa, encoding='utf-8')

# Final consistency assertions.
ft_check = ft_path.read_text(encoding='utf-8')
prefix_check = ft_check.split(boundary, 1)[0]
assert len(re.findall(r'status=verified -->', prefix_check)) == 20
assert '⟦' not in prefix_check and '⟧' not in prefix_check
idx_check = json.loads(idx_path.read_text(encoding='utf-8'))
assert idx_check['verified_pages'] == 20
assert idx_check['draft_pages'] == 85
assert idx_check['open_uncertainty_markers'] == 105
assert idx_check['next_pdf_page'] == 25

print('Ammayappan fidelity synchronization prepared: 20/105 verified; next PDF 25')
