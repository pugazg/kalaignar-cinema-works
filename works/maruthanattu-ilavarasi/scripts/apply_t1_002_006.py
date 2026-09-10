#!/usr/bin/env python3
from pathlib import Path
import json
import re

W = Path('works/maruthanattu-ilavarasi')
T = W / 'transcription'
P = T / 'pages'
N = W / 'notes'
P.mkdir(parents=True, exist_ok=True)
N.mkdir(parents=True, exist_ok=True)

pages = {
    2: '''<!-- source: pdf=2 printed=1-logical status=draft -->

# மருதநாட்டு இளவரசி

வசனம் : மு. கருணாநிதி.

குறிஞ்சிநாட்டுக் கொற்றவனுக்கு இரண்டு மனைவிகள். இருவரும் கர்ப்பவதிகள். இளையாளின் அண்ணன் துர்ஜயன், தன் அதிகாரம் நிலைக்க, தங்கையின் குழந்தை தான் ஆளவேண்டுமே என்று அவனுக்குத் தனி ஆசை. அதன் காரணமாக.................

கோபதிவர்மன் :- கொலைகாரி. போதும் உன் கும்மாளம். அங்கே நாசவேலை நடத்திவிட்டு அதை மறைக்க இங்கே நடனம்.

சித்ரா :- என்ன?

கோபதி:- சிங்காரியின் வாழ்வைச் சிதைக்க நீ போட்டாயே திட்டம், அது செத்துவிட்டது தெரியுமா? சண்டாளி.

சித்ரா:- திட்டமா? என்ன?

கோபதி:- ஆஹா! என்ன நடிப்பு அக்கிரமக்காரி, உன்னை அக்கினியில் தள்ளிப் பொசுக்கினாலும் போதாது.

அன்பானந்தர்:- அரசே, கோபம் நீதியை மறைத்துவிடும், நிதானமாக....

கோபதி:- நிதானம், அன்பானந்தரே! நீரே கேளும் இந்த நீலியை!

அன்பா:- மகாராணி, இளையராணி கர்ப்பமுற்றிருப்பதில் தங்களுக்குப் பொறாமை, அந்தக்குழந்தை ராஜ்யத்தில் பங்கு கேட்குமே என்ற பயம். அதன் காரணமாய் இளையராணிக்கு அனுப்பப்பட்ட மருந்தில் தாங்கள் விஷம் கலந்து விட்டீர்கள்.
''',
    3: '''<!-- source: pdf=3 printed=2 status=draft -->

# மருதநாட்டு இளவரசி

சித்ரா :- ஆ!

அன்பா :- இது இளைய மகாராணியின் குற்றச்சாட்டு

சித்ரா :- இதை நம்புகிறீர்களா?

கோபதி:- நன்றாக நம்புகிறேன், சித்ரா சிங்காரியை மட்டுமென்ன, உன் சுயநலத்திற்காக என்னையே கொலை செய்யவும் துணிவாய்!

சித்ரா:- அக்கிரமமான கட்டுக்கதை. நான் நிரபராதி! என் நெஞ்சைப் பிளக்காதீர்கள்.

கோபதி:- சீ! தொடாதே. (கீழே தள்ளிவிடுகிறான்)

அன்பா:- அரசே! பூரண கர்ப்பவதி.

கோபதி:- கர்ப்பவதி! சிங்காரியும் கர்ப்பவதிதான்.

சித்ரா:- சுவாமி, சிங்காரியை என் தங்கையாக மதிக்கிறேன்.

கோபதி:- பொய், சுத்தப்பொய்!

சித்ரா:- எனக்காக வாதாட யாருமில்லை. சிங்காரியின் பக்கம் அவள் அண்ணன்; அவள், அன்புக்குரிய மன்னர். எனக்கு சத்தியம் மாத்திரந்தான் சாட்சி!

அன்பா:- மகாராஜா! விஷய விளக்கத்திற்கு வாதி, பிரதிவாதி இருவரையும் விசாரிக்க வேண்டும்.

கோபதி:- வீண் நம்பிக்கை, இருந்தாலும் குறிஞ்சிநாட்டுக் கொற்றவன் அவசரப்பட்டான் என்ற அவச்சொல் வேண்டாம். நீதிமன்றத்திற்கு நீரே ஏற்பாடு செய்யும்.

துர்ஜயன்:- காளிங்கா, காரியம் கெட்டு விட்டது. எதிர்பார்த்தது நடக்கவில்லை. நாளை நீதிமன்றத்தில் நமது சூழ்ச்சிகள் அம்பலமாகிவிடும். இந்த துர்ஜயன் ஏகபோக அதிகாரத்திற்கு சமாதி அமைக்கப்பட்டுவிடும். இந்தத்தரணியை என் தங்கையின் மகன் ஆளவேண்டுமென்ற ஆசை அழிபட்டுப்போகும். இதிலிருந்து நாம் மீள வேண்டுமானால் மகாராணி மாளவேண்டும்.
''',
    4: '''<!-- source: pdf=4 printed=3 status=draft -->

# மருதநாட்டு இளவரசி

காளிங்கன்:- ஆமாம்!

துர்ஜயன்:- இன்றிரவே நமது திட்டம் நிறைவேறியாகவேண்டும்.

* * *

அன்பா:- இன்றிரவே நமது திட்டம் நிறைவேறியாகவேண்டும்.

சித்ரா:- அப்படியானால், நான் அரண்மனையைவிட்டு ஓடவேண்டுமா?

அன்பா:- ஆம் அம்மணி! இந்த ஆபத்திலிருந்து விடுதலை பெற வெளியேறித்தான் ஆகவேண்டும்.

சித்ரா:- வெளியேறி அரசருக்கு வருத்தத்தை அதிகமாக்குவதைவிட உயிர் விடுவது மேல்

அன்பா:- இல்லை, தங்கள் உயிர்பெரிதல்ல மகாராணி! தங்கள் வயிற்றில் தவழும் அந்த மாணிக்கம் குறிஞ்சிநாட்டு மகுடத்திற்கு ஏற்றது. அதைக் காப்பாற்ற இத்தியாகம் செய்யத்தான் வேண்டும்;

சித்ரா:- நான் எங்கே செல்வேன் அமைச்சரே!

அன்பா:- சுரங்கத்தின் மூலம் செல்லுங்கள். அது தங்களை அருகிலுள்ள கிராமத்தில் போய்ச் சேர்க்கும்.

சித்ரா:- அமைச்சரே!

அன்பா:- கவலைப்படாதீர்கள், அரண்மனையில் அநீதி வாழும்வரை, அஞ்ஞாதவாசம், பிறகு நியாயம் தங்களை நேரில் மாளிகைக்கு இழுக்கும்.

துர்ஜயன்:- ஆ! தப்பிவிட்டாள்!!......

அன்பா:- தலையணையை நன்றாகச் சோதித்துப் பார். காளிங்கா நன்றாகச் சோதித்துப்பார்............ காளிங்கா அஹ் ஹஹ்ஹா!

துர்ஜயன்:- சிரி! நன்றாகச் சிரி!.... சப்தம்போட்டுச் சிரி!... கலகலவென்று சிரி!... இதுதானே உன் கடைசிச் சிரிப்பு... காளிங்கா இந்த முட்டாளின் பிணம், யார் கண்ணுக்கும் படக்கூடாது. அரண்மனைத் தோட்டத்திலே புதைத்துவிட வேண்டும்.
''',
    5: '''<!-- source: pdf=5 printed=4 status=draft -->

# மருதநாட்டு இளவரசி

## காட்சி 2.

சேவகன்:- மகாராஜா! எங்கு தேடியும் மகாராணியைக் காணவில்லை.

கோபதி:- ஆ! காணவில்லையா?

துர்ஜயன்:- அது மட்டுமல்ல, மகாராஜா மந்திரியையும் காணவில்லை!

கோபதி:- தேடிப் போனவர் திரும்பவில்லையா?

துர்ஜயன்:- தேடிப்போனாலல்லவா திரும்ப!

கோபதி:- துர்ஜயா நீ என்ன சொல்கிறாய்?

துர்ஜயன்:- சொல்லவேண்டிய விஷயமா இது! மகாராஜா! மகாராணி என்றாலேயே, மந்திரிக்கு தனிப்பாசம்!

கோபதி:- ஆம்! அதுதான் நாம் சொல்லாமலேயே தேடப் புறப்பட்டிருக்கிறார்.

துர்ஜயன்:- அமைச்சருக்கு அரசாங்கத்தில் தனி ஆசை! அதைவிட மகாராணிமீது அபாரமான அன்பு!

கோபதி:- நான்கூடத்தான் அந்த அரக்கியிடம் அன்பு காட்டினேன்.

துர்ஜயன்:- மன்னரின் அன்பு மாற்றுக் குறைந்து, மந்திரியின் அன்பு, மகாராணியை மயக்கியது!

கோபதி:- என்ன?

துர்ஜயன்:- அரண்மனை வாழ்வையும், அமைச்சர் பதவியையும், துச்சமாக மதிக்கக்கூடியது அவருடைய அன்பு!

கோபதி:- ஆ! நினைக்க முடியாத அக்கிரமம்!

துர்ஜயன்:- ஆனாலும் நடந்திருக்கிறது.

கோபதி:- அவமானம், பெருத்த அவமானம்!

துர்ஜயன்:- அயல்நாட்டுக்குத் தெரிந்தால் அதைவிட அவமானம்!
''',
    6: '''<!-- source: pdf=6 printed=5 status=draft -->

# மருதநாட்டு இளவரசி

கோபதி:- சிங்கத்தின் குகையிலே சதி நடத்திவிட்டனர் சிறு நரிகள்! வாள் முனையிலே விளையாடிவிட்டனர் வைக்கோல் துரும்புகள், கோபதிவர்மன் யார் என்று தெரிந்தும் அவன் அரண்மனையிலே அக்கிரம அநியாயக்காரர்கள், சண்டாளர்கள். துர்ஜயா அந்த துரோகிகளைத் தேடும் வேலை திடமாக நடக்கட்டும். நாடெங்கும் பறை சாட்டுங்கள். அந்த விபசாரியை கண்டதுண்டமாக்கி என் கண் எதிரில் காட்டுங்கள். அந்த ஊதாரிகளின் ரத்தத்தால் குறிஞ்சி நாட்டிற்கு ஏற்பட்ட களங்கத்தைக் கழுவுங்கள். அந்த மாபாதகர்களை மறைத்து வைத்திருப்பவர்கள் யாராயிருந்தாலும் சரி! மரண தண்டனை! சித்ரவதை! ஊம் நடக்கட்டும்.

## காட்சி 3.

ராணி:- அப்பா!

மணிபல்லவர்: அப்பா! இதோ பார் அப்பாவுக்கு நீ தேடித் தந்த அருமையான பரிசை. நாடு, நகரம் எல்லாம் துறந்து காட்டுக்குப் போக வேண்டும் உன் அப்பா.

ராணி:- (கடிதத்தைப் பார்க்கிறாள்) மணிபல்லவ, மன்னவா! பெண் அல்லது போர்! இதற்கு உன் சம்மதம் தேவை.

கோபதிவர்மன்.

ஆஹா! என்ன வீரமான எச்சரிக்கை. அப்பா! பதில் எழுதுங்கள் போர்! போர் என்று எழுதுங்கள்.

மணி:- போதும், உன் வாயால் வந்த வினை! குஞ்சு செய்த குற்றம் கோழியின் தலையில் விடிந்தது.

ராணி:- ஏனப்பா ஏங்குகிறீர்கள். எறும்புகூட தன் பகையை எதிர்க்கிறதே!

மணி:- ராணி! காவேரியின் தண்ணீரை சிவப்பாக்க நான் விரும்பவில்லை. மருதநாட்டு வீரர்களை பிணமாக்க எனக்கு மனமில்லை, நாட்டின் அமைதிக்காக நீ ரௌத்ரனை மணந்து கொள்ளத்தான் வேண்டும்.
''',
}

for n, text in pages.items():
    (P / f'{n:03d}.md').write_text(text, encoding='utf-8')

next_action = (
    'Canonical Tamil first-pass transcription for PDF 7–11 as the next five-source-page batch. '
    'Use the user-supplied extracted transcription only as a candidate/navigation aid; source pixels remain controlling. '
    'Preserve exact wording, punctuation, speaker labels, stage directions, page boundaries and printed scene numbering. '
    'Prospectively inspect all historical-glyph-sensitive families on every page, keep all first-pass pages draft, '
    'synchronize controls, and commit immediately after the five pages.'
)

idx = {
    'work_id': 'maruthanattu-ilavarasi',
    'source_filename': 'TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf',
    'source_sha256': '8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f',
    'transcription_scope_pdf_pages': '2-22',
    'transcription_scope_page_count': 21,
    'status': 'first-pass-in-progress',
    'first_pass_pages_completed': 5,
    'first_pass_pdf_range_completed': '2-6',
    'first_pass_current_through_pdf': 6,
    'first_pass_current_through_logical_printed': 5,
    'draft_pages': 5,
    'visual_verified_pages': 0,
    'historical_glyph_first_pass_checked_pages': 5,
    'historical_glyph_final_verified_pages': 0,
    'open_uncertainty_markers': 0,
    'page_records': [
        {'pdf_page': 2, 'printed_page': 1, 'printed_page_kind': 'logical-only', 'kind': 'unnumbered-opening', 'status': 'draft', 'path': 'pages/002.md'},
        {'pdf_page': 3, 'printed_page': 2, 'kind': 'unnumbered-opening', 'status': 'draft', 'path': 'pages/003.md'},
        {'pdf_page': 4, 'printed_page': 3, 'kind': 'unnumbered-opening', 'status': 'draft', 'path': 'pages/004.md'},
        {'pdf_page': 5, 'printed_page': 4, 'kind': 'screenplay', 'source_scene_id': '2', 'status': 'draft', 'path': 'pages/005.md'},
        {'pdf_page': 6, 'printed_page': 5, 'kind': 'screenplay', 'source_scene_ids': ['2', '3'], 'status': 'draft', 'path': 'pages/006.md'},
    ],
    'batch_size_source_pages': 5,
    'next_batch_pdf_pages': '7-11',
    'next_action': next_action,
}
(T / 'index.json').write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

(T / 'README.md').write_text('''# மருதநாட்டு இளவரசி — canonical Tamil transcription

Status: **FIRST PASS IN PROGRESS — PDF 2–6 / 5 of 21 body pages drafted**.

The rendered scan is canonical authority. The user-supplied extracted transcription may be used only as a candidate/navigation aid; it must never override source pixels.

Current page records are `pages/002.md` through `pages/006.md`. All remain **draft** until the later independent full visual-fidelity and historical-glyph verification gates.

Source structure is preserved: PDF 2–4 is an unnumbered opening segment, PDF 5 begins printed `காட்சி 2.`, and PDF 6 continues scene 2 before printed `காட்சி 3.`. No source `காட்சி 1.` has been invented.

Next batch: **PDF 7–11**.
''', encoding='utf-8')

(N / 'textual-notes-pdf-002-006.md').write_text('''# மருதநாட்டு இளவரசி — T1 textual notes PDF 2–6

Status: **FIRST-PASS DRAFT / COMPLETE FOR THIS BATCH**.

- Every page PDF 2–6 was read against enlarged rendered source pixels.
- The user-supplied extracted transcription was used only to accelerate navigation/candidate comparison. It was not treated as source authority.
- The extracted heading `காட்சி 1` was rejected because no such heading is printed in PDF 2–4; those pages remain the unnumbered opening source segment.
- Extraction corruptions were not copied; the draft follows the visible scan.
- Historical typeforms were decoded occurrence-by-occurrence into modern Unicode identity without modernizing source wording. Representative first-pass readings include `நன்றாகச்` on PDF 4 and the same-edition `தான்` identity in PDF 2's introductory sentence.
- PDF 4 preserves the printed `* * *` separator.
- PDF 5 preserves printed `காட்சி 2.` and PDF 6 preserves printed `காட்சி 3.`.
- No unresolved first-pass marker remains in PDF 2–6, but all five records remain `draft`; this is not visual-fidelity verification.
''', encoding='utf-8')

(N / 'historical-glyph-audit.md').write_text('''# மருதநாட்டு இளவரசி — historical Tamil glyph audit

Status: **FIRST-PASS IN PROGRESS — 5/21 body pages prospectively checked**.

Known families checked on every drafted page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules remain source-first: source pixels control character identity; OCR/extracted text is only a candidate; no global replacements; and glyph decoding must not modernize wording.

## Coverage

- PDF 2–6: **first-pass glyph check COMPLETE / draft only**;
- final independent historical-glyph verification: **0/21**;
- open first-pass glyph uncertainty markers in PDF 2–6: **0**.

Representative adjudications:

- PDF 4 apparent old-form `நன்றுகச்` shape → character identity `நன்றாகச்` (`றா` family), supported by enlarged source and same-edition form behaviour;
- PDF 2 introductory `தான்` was checked against the printed cluster rather than copied from the extracted candidate;
- no global lexical normalization was performed.

All pages remain `draft` until the later independent visual-fidelity and historical-glyph closure gates.
''', encoding='utf-8')

meta = (W / 'metadata.yaml').read_text(encoding='utf-8')
meta = meta.replace('canonical_tamil_transcription: not-started', 'canonical_tamil_transcription: first-pass-in-progress')
meta = meta.replace(
    'canonical_tamil_first_pass_pages_completed: 0',
    'canonical_tamil_first_pass_pages_completed: 5\n'
    'canonical_tamil_first_pass_pdf_range_completed: "2-6"\n'
    'canonical_tamil_first_pass_current_through_pdf: 6\n'
    'canonical_tamil_current_batch_path: works/maruthanattu-ilavarasi/transcription/pages/006.md'
)
meta = meta.replace('historical_glyph_audit: required-not-started', 'historical_glyph_audit: first-pass-in-progress-5-of-21')
meta = re.sub(r'next_action: ".*"', 'next_action: "' + next_action + '"', meta)
(W / 'metadata.yaml').write_text(meta, encoding='utf-8')

readme = (W / 'README.md').read_text(encoding='utf-8')
readme = readme.replace(
    'Canonical Tamil transcription has **not started**. No structured derivative layer is authorized yet.',
    'Canonical Tamil first pass is **IN PROGRESS — PDF 2–6 / 5 of 21 body pages drafted**. All five pages remain draft; visual-fidelity and final historical-glyph verification have not started. No structured derivative layer is authorized yet.'
)
readme = re.sub(r'> \*\*Begin canonical Tamil first-pass transcription from PDF 2 onward.*?\*\*', '> **' + next_action + '**', readme, flags=re.S)
(W / 'README.md').write_text(readme, encoding='utf-8')

(W / 'PROJECT_HANDOVER.md').write_text(f'''# மருதநாட்டு இளவரசி — Project Handover

Repository: `pugazg/kalaignar-cinema-works`
Branch: `main`
Work: `works/maruthanattu-ilavarasi/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**. Do not commit the source PDF.

## Durable state

- source intake: **COMPLETE**; mapping: **COMPLETE-VERIFIED**;
- body: PDF **2–22** / logical printed **1–21**;
- PDF 2–4 remains an unnumbered opening segment; no source `காட்சி 1.` is invented;
- observed source headings: **2,3,4,5,6,8,9,10**; `காட்சி 7.` not observed;
- canonical Tamil first pass: **IN PROGRESS — PDF 2–6 / 5 of 21 DRAFT**;
- prospective historical-glyph check: **5/21**; final independent glyph verification: **0/21**;
- visual-fidelity verification: **0/21**;
- open first-pass uncertainty markers through PDF 6: **0**;
- candidate extracted transcription may assist navigation only; source pixels control;
- structured/English/reader derivatives remain **BLOCKED**.

## Exact next activity

> **{next_action}**
''', encoding='utf-8')

(W / 'NEXT_CHAT_PROMPT.md').write_text(f'''# Next Chat Prompt — மருதநாட்டு இளவரசி / canonical Tamil PDF 7–11

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/maruthanattu-ilavarasi/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**. Do not commit it.

## Durable state

- intake/mapping: **COMPLETE / COMPLETE-VERIFIED**;
- canonical Tamil first pass: **5/21 DRAFT — PDF 2–6**;
- PDF 2–4 is the unnumbered opening segment; do not invent scene 1;
- PDF 5 begins `காட்சி 2.`; PDF 6 begins `காட்சி 3.` after scene-2 continuation;
- historical-glyph prospective coverage: **5/21**; final verification: **0/21**;
- visual-fidelity verification: **0/21**;
- later derivatives: **BLOCKED**.

## Next batch

> **{next_action}**
''', encoding='utf-8')

# Registry synchronization.
dp = Path('data/works.json')
data = json.loads(dp.read_text(encoding='utf-8'))
rec = next(x for x in data if x.get('id') == 'maruthanattu-ilavarasi')
rec['canonical_tamil_transcription'] = 'first-pass-in-progress'
rec['canonical_tamil_first_pass_pages_completed'] = 5
rec['canonical_tamil_first_pass_pdf_range_completed'] = '2-6'
rec['canonical_tamil_first_pass_current_through_pdf'] = 6
rec['canonical_tamil_current_batch_path'] = 'works/maruthanattu-ilavarasi/transcription/pages/006.md'
rec['historical_glyph_audit'] = 'first-pass-in-progress-5-of-21'
rec['next_action'] = next_action
dp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Root README current status block.
rp = Path('README.md')
root = rp.read_text(encoding='utf-8')
block = f'''## மருதநாட்டு இளவரசி status

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — source intake and structural mapping are complete-verified; canonical Tamil first pass is now **5/21 DRAFT through PDF 6**.

- body: **PDF 2–22 / logical printed 1–21**;
- PDF 2–4: unnumbered opening segment; no synthetic `காட்சி 1.`;
- printed headings observed: **2,3,4,5,6,8,9,10**; `காட்சி 7.` not observed;
- canonical Tamil first pass: **PDF 2–6 / 5 of 21 DRAFT**;
- historical-glyph prospective check: **5/21**; final visual/glyph verification: **0/21 / 0/21**;
- open first-pass uncertainty markers through PDF 6: **0**;
- later derivatives: **BLOCKED**.

**Next:** {next_action}

'''
root = re.sub(r'## மருதநாட்டு இளவரசி status\n.*?(?=## )', block, root, flags=re.S)
rp.write_text(root, encoding='utf-8')

ap = Path('docs/STATUS_CONSISTENCY_AUDIT.md')
audit = ap.read_text(encoding='utf-8')
audit = re.sub(
    r'\| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி \|[^\n]*',
    '| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி | **Tamil T1 5/21 DRAFT through PDF 6; glyph-first-pass 5/21; final visual/glyph 0/21** | headings **2,3,4,5,6,8,9,10**; opening unnumbered; scene 7 absent | not-started | not-started |',
    audit,
)
ap.write_text(audit, encoding='utf-8')

# Fail-closed batch invariants.
assert idx['first_pass_pages_completed'] == 5
assert idx['open_uncertainty_markers'] == 0
joined = '\n'.join(pages.values())
assert '## காட்சி 1.' not in joined and '\nகாட்சி 1.' not in joined
assert '## காட்சி 2.' in pages[5]
assert '## காட்சி 3.' in pages[6]
assert '* * *' in pages[4]
assert 'status=draft' in pages[2] and 'status=draft' in pages[6]
print('PASS: Maruthanattu Ilavarasi Tamil T1 PDF 2-6')
