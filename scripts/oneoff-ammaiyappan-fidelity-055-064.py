from pathlib import Path
import json, re

ROOT = Path('.')
FULL = ROOT / 'works/ammaiyappan/transcription/full-text.md'


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected exactly 1 occurrence, found {n}: {old!r}')
    return text.replace(old, new, 1)


def replace_at_least(text, old, new, label, minimum=1):
    n = text.count(old)
    if n < minimum:
        raise SystemExit(f'{label}: expected at least {minimum}, found {n}: {old!r}')
    return text.replace(old, new)


def page_span(text, pdf):
    start_pat = re.compile(rf'<!-- source: pdf={pdf} printed={pdf-2} status=(?:draft|verified|review) -->')
    m = start_pat.search(text)
    if not m:
        raise SystemExit(f'page {pdf}: source anchor not found')
    n = re.search(r'<!-- source: pdf=\d+ printed=\d+ status=(?:draft|verified|review) -->', text[m.end():])
    end = m.end() + n.start() if n else len(text)
    return m.start(), end


def patch_page(text, pdf, replacements, new_status):
    a, b = page_span(text, pdf)
    seg = text[a:b]
    old_anchor = re.search(rf'<!-- source: pdf={pdf} printed={pdf-2} status=(?:draft|verified|review) -->', seg).group(0)
    seg = seg.replace(old_anchor, f'<!-- source: pdf={pdf} printed={pdf-2} status={new_status} -->', 1)
    for old, new in replacements:
        count = seg.count(old)
        if count != 1:
            raise SystemExit(f'PDF {pdf}: expected exactly 1 occurrence, found {count}: {old!r}')
        seg = seg.replace(old, new, 1)
    return text[:a] + seg + text[b:]


text = FULL.read_text(encoding='utf-8')

corrections = {
    55: [
        ('அபாரதத் தொகையை', 'அபராதத் தொகையை'),
        ('அபாரதப் பணம்—அரைக்காசுக்கு வழியற்ற உன்னிடம் எது அபாரதப் பணம்?', 'அபராதப் பணம்—அரைக்காசுக்கு வழியற்ற உன்னிடம் எது அபராதப் பணம்?'),
        ('உங்கள் அபாரதத்தை?', 'உங்கள் அபராதத்தை?'),
        ('அபாரதப் பணம் விரைவில் வந்துவிடலாம்', 'அபராதப் பணம் விரைவில் வந்துவிடலாம்'),
        ('⟦தங்கள் திலகின் செந்தாமரை மொட்டுகளாக?⟧', 'தங்கள் தலைகளே செந்தாமரை மொட்டுகளாக'),
    ],
    56: [
        ('புத்தி சுவாதீனம் மற்றவனும்', 'புத்தி சுவாதீனம் அற்றவனும்'),
    ],
    57: [
        ('அலங்கோலக் காட்சி அல்ல', 'அலங்கோலக் காட்சியல்ல'),
        ('கத்தி முனைகளையும்', 'கத்திமுனைகளையும்'),
    ],
    58: [
        ('⟦கண்ணமற்றவனே?⟧', 'கண்ணியமற்றவனே'),
    ],
    59: [
        ('சாவாலும் பிரிக்க முடியாத எங்களிரத்து', 'சாவாலும் பிரிக்க முடியாத எங்களன்பிற்கு'),
        ('பொன்னுக்கு ஆசைப்பட்டேனா? நானு?', 'பொன்னுக்கு ஆசைப்பட்டேனு? நானு?'),
        ('முத்தாயி! சொல்லைக் கேள்', 'முத்தாயி! சொல்வதைக் கேள்'),
    ],
    60: [
        ('பேசியும் பலனில்லை.', 'பேசியும் பலனில்ல.'),
        ('எப்போது ஆவது உணராமல் இருக்கப் போகிறாய்?', 'எப்போதாவது உணராமலா இருக்கப் போகிறாய்?'),
        ('இரத்தின் ஒட்டியானம்', 'இரத்தின ஒட்டியானம்'),
        ('வாடும் இசைந்தாள்', 'வரவும் இசைந்தாள்'),
        ('⟦அர்ச்சுனன் பாம்பரணை அல்லியை மணக்க?⟧', 'அர்ச்சுனன் பாம்பரணை அல்லியை மணக்க'),
        ('⟦வேலன் கிழவனணை வள்ளியை மணக்க?⟧', 'வேலன் கிழவனை வள்ளியை மணக்க'),
    ],
    61: [
        ('⟦வந்தி ரப்பா நாதர் போல?⟧', 'வந்தி ரப்பா நாதர் போல'),
        ('பாவா இல்லை—பரவாயில்லை', 'பாவா இல்ல—பரவாயில்ல'),
        ('ஒரு முக்கியமான வழி சொல்லும்.', 'ஒரு முதல் தரமான வழி சொல்லும்.'),
        ('சிக்கிரம் எடுங்கள் யுவராஜ்', 'சீக்கிரம் எடுங்கள் யுவராஜ்'),
    ],
    62: [
        ('விட்டு பிறகு மற்ற ஏற்பாடு நடத்தட்டும்; ஆமாம்!', 'விட்டு பிறகு மற்ற ஏற்பாடு நடக்கட்டும்; ஆமாம்!'),
        ('⟦மல்விகைக் கொடியின்?⟧', 'மல்லிகைக் கொடியின்'),
        ('நான் செய்த தவறுகூட மறந்துவிடு.', 'நான் செய்த தவறுகளை மறந்துவிடு.'),
    ],
    63: [
        ('உன்னைத் தூக்கிப் போய்', 'உன்னைத் தூக்கிப்போய்'),
        ('ஆனந்தபுரம் என்று ஊருக்குச்', 'ஆனந்தபுரம் என்ற ஊருக்குச்'),
        ('நான் எதாவது வேகத்தில்', 'நான் ஏதாவது வேகத்தில்'),
    ],
    64: [
        ('⟦குடிசைகான்! ஒருபுறத்தில் கூரிய வேல், வாள் வரிசையாய் அமைத்திருக்கும்; வயத்தைப் பிடிப்பதற்கும் வெம்பகை முடிப்பதற்கும் வடித்து வைத்த படைக்கலம் போல் மின்னும் மிளிரும்...புலியின் குகையினிலே அழகில்லை......புதுமையல்ல!⟧',
         'குடிசைகாண்! ஒருபுறத்தில் கூரிய வேல், வாள் வரிசையாய் அமைத்திருக்கும். வையத்தை பிடிப்பதற்கும் வெம்பகை முடிப்பதற்கும் வடித்து வைத்த படைக்கலம் போல் மின்னும் மிளிரும்...புலியின் குகையினிலே அழகில்லை......புதுமையல்ல!'),
        ('⟦துயரம் ஆடுகையில் காய்களை வெட்டுவதுண்டு...களமும் அதுதான்...காயம்⟧',
         'துயரம் ஆடுகையில் காய்கள் வெட்டுவதுண்டு...களமும் அதுதான்...காயம்'),
    ],
}

for p in range(55, 64):
    text = patch_page(text, p, corrections[p], 'verified')
text = patch_page(text, 64, corrections[64], 'review')

# Marker 47 must remain visible on the review page.
a, b = page_span(text, 64)
seg64 = text[a:b]
if '⟦கிளியும் மெச்சிவிருப்பும்' not in seg64:
    raise SystemExit('PDF 64: marker 47 is no longer visible')
if seg64.count('⟦') != 1 or seg64.count('⟧') != 1:
    raise SystemExit(f'PDF 64: expected exactly one unresolved span after reconciliation, found {seg64.count("⟦")}')

FULL.write_text(text, encoding='utf-8')

# Authoritative machine-readable index.
idx_path = ROOT / 'works/ammaiyappan/transcription/index.json'
idx = json.loads(idx_path.read_text(encoding='utf-8'))
idx['status'] = 'fidelity-audit-in-progress'
idx['draft_pages'] = 45
idx['verified_pages'] = 59
idx['review_pages'] = 1
idx['open_uncertainty_markers'] = 69
fa = idx.setdefault('fidelity_audit', {})
fa['status'] = 'in-progress'
fa['canonical_range_audit_complete'] = False
fa['audited_pages'] = 60
fa['verified_pages'] = 59
fa['unresolved_source_readings'] = 69
fa['review_pages'] = 1
fa['verified_pdf_range'] = [5, 63]
fa['verified_logical_printed_range'] = [3, 61]
fa['review_pdf_pages'] = [64]
fa['review_logical_printed_pages'] = [62]
idx['next_pdf_page'] = 64
idx['next_printed_page'] = 62
idx['next_action'] = 'Reopen PDF 64 / logical printed p.62 and resolve first-pass marker 47 from the rendered scan. Do not advance to PDF 65 until PDF 64 is source-clean and verified; structured derivatives remain blocked until all 105 canonical pages are verified.'
idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Fidelity audit ledger.
audit_path = ROOT / 'works/ammaiyappan/notes/fidelity-audit.md'
audit = audit_path.read_text(encoding='utf-8')
old_table = '''| PDF 45–54 / logical pp.43–52 | 10 | 0 | 0 | verified |
| PDF 55–109 / logical pp.53–107 | 0 | 0 | 55 | pending |
| **Total** | **50** | **0** | **55** | **in progress** |'''
new_table = '''| PDF 45–54 / logical pp.43–52 | 10 | 0 | 0 | verified |
| PDF 55–63 / logical pp.53–61 | 9 | 0 | 0 | verified |
| PDF 64 / logical p.62 | 0 | 1 | 0 | review — marker 47 unresolved |
| PDF 65–109 / logical pp.63–107 | 0 | 0 | 45 | pending |
| **Total** | **59** | **1** | **45** | **in progress** |'''
audit = replace_once(audit, old_table, new_table, 'fidelity progress table')
audit = replace_once(audit,
    'Open first-pass uncertainty markers after this audit checkpoint: **77** (markers **1–39 resolved**; markers **40–116 remain for later source-order review**).',
    'Open first-pass uncertainty markers after this audit checkpoint: **69** (markers **1–46 and 48 resolved**; marker **47** plus markers **49–116** remain unresolved).',
    'fidelity marker summary')
old_next = '''## Exact next activity

Continue the rendered-scan fidelity audit at **PDF 55 / logical printed p.53**, in source order. Adjudicate markers **40 onward** occurrence-by-occurrence and mark a page verified only after full-page visual comparison. Do not begin scene/dialogue/character derivatives yet.'''
section = '''## PDF 55–64 / logical pp.53–62 — 9 verified + 1 review

PDF 55–63 were compared page-by-page against the rendered controlling scan and are source-clean after scan-backed correction. PDF 64 was also compared in full, but remains `review` because first-pass marker 47 contains an old-type sequence that is not secure enough to normalize from the scan. The historical bounded `parts/pdf-055-064.md` remains first-pass provenance and was not rewritten.

Resolved marker readings:

40. PDF 55: `தங்கள் தலைகளே செந்தாமரை மொட்டுகளாக`
41. PDF 58: `கண்ணியமற்றவனே`
42. PDF 60: `அர்ச்சுனன் பாம்பரணை அல்லியை மணக்க`
43. PDF 60: `வேலன் கிழவனை வள்ளியை மணக்க`
44. PDF 61: source-visible `வந்தி ரப்பா நாதர் போல`
45. PDF 62: `மல்லிகைக் கொடியின்`
46. PDF 64: `குடிசைகாண்! ஒருபுறத்தில் கூரிய வேல், வாள் வரிசையாய் அமைத்திருக்கும். வையத்தை பிடிப்பதற்கும் வெம்பகை முடிப்பதற்கும் வடித்து வைத்த படைக்கலம் போல் மின்னும் மிளிரும்...புலியின் குகையினிலே அழகில்லை......புதுமையல்ல!`
48. PDF 64: `துயரம் ஆடுகையில் காய்கள் வெட்டுவதுண்டு...களமும் அதுதான்...காயம்`

Marker **47** remains explicitly unresolved on PDF 64. No external poem text, OCR, film dialogue, or semantic reconstruction was used to fill it.

Other source-backed restorations in PDF 55–63 include `அபராதத்/அபராதப்`, `புத்தி சுவாதீனம் அற்றவனும்`, `அலங்கோலக் காட்சியல்ல`, `கத்திமுனைகளையும்`, `எங்களன்பிற்கு`, `ஆசைப்பட்டேனு`, `சொல்வதைக் கேள்`, `பலனில்ல`, `எப்போதாவது உணராமலா`, `இரத்தின ஒட்டியானம்`, `வரவும் இசைந்தாள்`, `பாவா இல்ல—பரவாயில்ல`, `முதல் தரமான வழி`, `சீக்கிரம்`, `நடக்கட்டும்`, `தவறுகளை மறந்துவிடு`, `ஆனந்தபுரம் என்ற ஊருக்குச்`, and `ஏதாவது`.

## Exact next activity

Reopen **PDF 64 / logical printed p.62** and adjudicate marker **47** from the rendered scan. Do **not** advance the fidelity frontier to PDF 65 until PDF 64 is source-clean and verified. Do not begin scene/dialogue/character derivatives yet.'''
audit = replace_once(audit, old_next, section, 'fidelity exact next activity')
audit_path.write_text(audit, encoding='utf-8')

# Work-local README.
work_readme = ROOT / 'works/ammaiyappan/README.md'
s = work_readme.read_text(encoding='utf-8')
s = s.replace('- verified pages: **50**;', '- verified pages: **59**;')
s = s.replace('- open first-pass uncertainty markers: **77**;', '- open first-pass uncertainty markers: **69**;')
s = s.replace('visual fidelity audit: **in-progress — PDF 5–54 / logical pp.3–52 verified (50/105)**.', 'visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 / logical p.62 review**.')
s = s.replace('| Visual fidelity audit | **in-progress — 50/105 verified** |', '| Visual fidelity audit | **in-progress — 59/105 verified + PDF 64 review** |')
s = s.replace('| Verified Tamil pages | **50/105** |', '| Verified Tamil pages | **59/105; 1 review** |')
s = re.sub(r'\*\*Continue the rendered-scan visual fidelity audit at PDF 55 / logical printed p\.53\.\*\* Resolve the remaining \*\*77\*\* explicit first-pass readings occurrence-by-occurrence, upgrade pages only after full-page direct scan comparison, and keep all structured derivatives blocked until the complete 105-page canonical range is verified\.',
           '**Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan.** PDF 5–63 are verified; PDF 64 remains review. Do not advance to PDF 65 or start structured derivatives until PDF 64 is source-clean and ultimately all 105 canonical pages are verified.', s)
work_readme.write_text(s, encoding='utf-8')

# Transcription README (also fixes a stale 92-marker count left by an older sync).
tr_readme = ROOT / 'works/ammaiyappan/transcription/README.md'
s = tr_readme.read_text(encoding='utf-8')
s = re.sub(r'- verified pages: \*\*\d+\*\*;', '- verified pages: **59**;', s)
s = re.sub(r'- review pages: \*\*\d+\*\*;', '- review pages: **1**;', s)
s = re.sub(r'- open first-pass uncertain readings: \*\*\d+\*\*;', '- open first-pass uncertain readings: **69**;', s)
s = re.sub(r'- full rendered-scan visual fidelity audit: \*\*in-progress — PDF 5–\d+ / logical pp\.3–\d+ verified \(\d+/105\)\*\*\.', '- full rendered-scan visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 review**.', s)
s = re.sub(r'## Exact next activity\n\n.*', '## Exact next activity\n\nReopen **PDF 64 / logical printed p.62** and resolve marker **47** from the rendered scan. Do not advance to PDF 65 while PDF 64 remains review; structured derivatives stay blocked until all 105 pages are verified.', s, flags=re.S)
tr_readme.write_text(s, encoding='utf-8')

# Metadata YAML via anchored field replacements.
meta_path = ROOT / 'works/ammaiyappan/metadata.yaml'
s = meta_path.read_text(encoding='utf-8')
subs = {
    r'(?m)^  verified_pages: \d+$': '  verified_pages: 59',
    r'(?m)^  draft_pages: \d+$': '  draft_pages: 45',
    r'(?m)^  review_pages: \d+$': '  review_pages: 1',
    r'(?m)^  open_first_pass_uncertainty_markers: \d+$': '  open_first_pass_uncertainty_markers: 69',
    r'(?m)^  next_pdf_page: \d+$': '  next_pdf_page: 64',
    r'(?m)^  next_logical_printed_page: \d+$': '  next_logical_printed_page: 62',
    r'(?m)^  next_action: ".*"$': '  next_action: "Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan; PDF 5-63 are verified, PDF 64 is review, and structured derivatives remain blocked until all 105 pages are verified."',
    r'(?m)^  audited_pages: \d+$': '  audited_pages: 60',
    r'(?m)^  unresolved_source_readings: \d+$': '  unresolved_source_readings: 69',
    r'(?m)^  verified_pdf_pages: ".*"$': '  verified_pdf_pages: "5-63"',
    r'(?m)^  verified_logical_printed_pages: ".*"$': '  verified_logical_printed_pages: "3-61"',
    r'(?m)^  visual_fidelity_audit: in-progress-\d+-of-105$': '  visual_fidelity_audit: in-progress-59-of-105-plus-1-review',
}
for pat, repl in subs.items():
    s, n = re.subn(pat, repl, s)
    if n == 0 and 'visual_fidelity_audit' not in pat:
        raise SystemExit(f'metadata replacement missed: {pat}')
# fidelity_audit block has a second verified_pages/review_pages occurrence; global regex above updates both where applicable.
# Add explicit review page fields if absent.
if '  review_pdf_pages:' not in s:
    s = s.replace('  verified_logical_printed_pages: "3-61"\n', '  verified_logical_printed_pages: "3-61"\n  review_pdf_pages: "64"\n  review_logical_printed_pages: "62"\n')
s = re.sub(r'(?m)^next_action: ".*"$', 'next_action: "Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan; do not advance to PDF 65 until PDF 64 is verified."', s)
meta_path.write_text(s, encoding='utf-8')

# Work-specific handover: current-state replacements, including its stale 92-marker next instruction.
hand_path = ROOT / 'works/ammaiyappan/PROJECT_HANDOVER.md'
s = hand_path.read_text(encoding='utf-8')
s = s.replace('- state: **draft-complete**, verified pages **50**;', '- state: **draft-complete**, verified pages **59**, review pages **1**;')
s = s.replace('- open uncertainty markers: **77**;', '- open uncertainty markers: **69**;')
s = s.replace('- visual fidelity audit: **in-progress — PDF 5–54 / logical pp.3–52 verified (50/105)**.', '- visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified (59/105); PDF 64 / logical p.62 review**.')
s = re.sub(r'- visual fidelity audit: \*\*in-progress — \d+/105 verified; next PDF \d+ / logical p\.\d+\*\*;', '- visual fidelity audit: **in-progress — 59/105 verified; PDF 64 / logical p.62 review**;', s)
s = re.sub(r'> \*\*Continue the separate rendered-scan visual fidelity audit at PDF 55 / logical printed p\.53.*?\*\*$', '> **Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan. PDF 5–63 are verified; PDF 64 remains review. Do not advance to PDF 65 or start scene/dialogue/character derivatives until PDF 64 is source-clean and ultimately all 105 canonical pages pass.**', s, flags=re.M)
hand_path.write_text(s, encoding='utf-8')

# Root README current Ammayappan status.
root_readme = ROOT / 'README.md'
s = root_readme.read_text(encoding='utf-8')
s = s.replace('- visual fidelity audit: **in-progress — PDF 5–54 / logical pp.3–52 verified**;', '- visual fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified; PDF 64 review**;')
s = s.replace('- verified / draft / review pages: **50 / 55 / 0**;', '- verified / draft / review pages: **59 / 45 / 1**;')
s = s.replace('- open first-pass uncertainty markers: **77**;', '- open first-pass uncertainty markers: **69**;')
s = re.sub(r'\*\*Next:\*\* continue the rendered-scan visual fidelity audit at \*\*PDF 55 / logical printed p\.53\*\* and adjudicate the remaining \*\*77\*\* explicit first-pass uncertainty markers\.', '**Next:** reopen **PDF 64 / logical printed p.62** and resolve marker **47** from the scan. Do not advance to PDF 65 while PDF 64 remains review.', s)
root_readme.write_text(s, encoding='utf-8')

# Machine-readable work registry, including stale total_verified_pages left by an older checkpoint.
works_path = ROOT / 'data/works.json'
works = json.loads(works_path.read_text(encoding='utf-8'))
w = next(x for x in works if x.get('id') == 'ammaiyappan')
updates = {
    'canonical_tamil_draft_pages': 45,
    'canonical_tamil_verified_pages': 59,
    'canonical_tamil_review_pages': 1,
    'canonical_tamil_open_uncertainty_markers': 69,
    'tamil_transcription_draft_pages': 45,
    'tamil_transcription_verified_pages': 59,
    'tamil_transcription_review_pages': 1,
    'total_verified_pages': 59,
    'total_review_pages': 1,
    'canonical_range_fidelity_audit_complete': False,
}
for k, v in updates.items():
    w[k] = v
w['next_action'] = 'Reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan. PDF 5-63 are verified; PDF 64 is review. Do not advance to PDF 65 until it is verified.'
works_path.write_text(json.dumps(works, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Master handover: replace current high-level bullet and Section 16 with one coherent active checkpoint.
master_path = ROOT / 'docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
s = master_path.read_text(encoding='utf-8')
s = re.sub(r'- \*\*Ammayappan\*\* — 111-page image-only screenplay/dialogue source;.*?structured derivatives remain blocked\.',
           '- **Ammayappan** — 111-page image-only screenplay/dialogue source; first pass **105/105** assembled with QA PASS; rendered-scan fidelity audit now has **PDF 5–63 verified (59/105), PDF 64 / logical p.62 in review, 45 draft pages, and 69 unresolved first-pass readings**; structured derivatives remain blocked.', s)
s = re.sub(r'`data/works\.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT\.md` are synchronized to the active \*\*Ammayappan fidelity checkpoint:.*?\*\*\. The next source page is PDF \d+ / logical p\.\d+\.',
           '`data/works.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` are synchronized to the active **Ammayappan fidelity checkpoint: first pass 105/105 assembled, PDF 5–63 verified (59/105), PDF 64 / logical p.62 review, 45 draft pages, and 69 unresolved first-pass readings**. The next gate is PDF 64 / logical p.62.', s)
sec16 = '''## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- source intake / whole-scan map: **complete**;
- canonical first pass: **105/105 draft-complete**, continuous `full-text.md` through PDF 109;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- fidelity audit: **PDF 5–63 / logical pp.3–61 verified — 59/105**;
- review: **PDF 64 / logical p.62 — marker 47 unresolved**;
- remaining draft pages: **45 — PDF 65–109**;
- open first-pass uncertainty markers: **69**;
- locked source headings remain `பழுதார் வீதி` (PDF 56) and `தூக்குமேடை` (PDF 107; reject `தாக்குமேடை`);
- structured derivatives / English / reader: **blocked pending 105/105 verified Tamil**.

**Exact next activity:** reopen PDF 64 / logical p.62 and adjudicate marker 47 from the rendered scan. Do not move the fidelity frontier to PDF 65 until PDF 64 is source-clean and verified.
'''
s = re.sub(r'## 16\. Ammayappan active checkpoint.*?(?=\n---\n|\Z)', sec16.rstrip(), s, flags=re.S)
master_path.write_text(s, encoding='utf-8')

# Status consistency audit: reconcile all current Ammayappan counts.
status_path = ROOT / 'docs/STATUS_CONSISTENCY_AUDIT.md'
s = status_path.read_text(encoding='utf-8')
s = re.sub(r'\*\*PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint:.*?\*\*',
           '**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–63 visually verified (59/105), PDF 64 review, 45 draft pages, 1 review page, and 69 open first-pass readings; next gate PDF 64 / logical p.62.**', s)
s = re.sub(r'\| Ammayappan \|.*?\| blocked \| blocked \|',
           '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–63 fidelity-verified (59/105); PDF 64 review; 45 draft; 69 open markers** | scene/dialogue/character blocked pending complete verified Tamil | blocked | blocked |', s)
s = s.replace('- rendered-scan fidelity audit: **in-progress — PDF 5–54 / logical pp.3–52 verified**;', '- rendered-scan fidelity audit: **in-progress — PDF 5–63 / logical pp.3–61 verified; PDF 64 / logical p.62 review**;')
s = s.replace('- verified / draft / review pages: **50 / 55 / 0**;', '- verified / draft / review pages: **59 / 45 / 1**;')
s = s.replace('- open first-pass uncertainty markers: **77**;', '- open first-pass uncertainty markers: **69**;')
s = re.sub(r'Exact next activity: \*\*continue at PDF 55 / logical printed p\.53\*\*.*?Structured derivatives remain blocked until all 105 pages pass\.',
           'Exact next activity: **reopen PDF 64 / logical printed p.62 and resolve marker 47 from the rendered scan**. Do not advance to PDF 65 while PDF 64 remains review. Structured derivatives remain blocked until all 105 pages pass.', s)
status_path.write_text(s, encoding='utf-8')

# Final invariant sweep on active work-local authority.
full = FULL.read_text(encoding='utf-8')
for p in range(55, 64):
    if f'<!-- source: pdf={p} printed={p-2} status=verified -->' not in full:
        raise SystemExit(f'final invariant: PDF {p} not verified')
if '<!-- source: pdf=64 printed=62 status=review -->' not in full:
    raise SystemExit('final invariant: PDF 64 not review')
if '⟦கிளியும் மெச்சிவிருப்பும்' not in full:
    raise SystemExit('final invariant: marker 47 missing')
for resolved in ['⟦தங்கள் திலகின்', '⟦கண்ணமற்றவனே', '⟦அர்ச்சுனன் பாம்பரணை', '⟦வேலன் கிழவனணை', '⟦வந்தி ரப்பா நாதர் போல?', '⟦மல்விகைக்', '⟦குடிசைகான்!', '⟦துயரம் ஆடுகையில்']:
    if resolved in full:
        raise SystemExit(f'final invariant: resolved marker text still present: {resolved}')

print('Ammayappan PDF 55-64 reconciliation prepared: 59 verified / 45 draft / 1 review / 69 open; next PDF 64 marker 47.')
