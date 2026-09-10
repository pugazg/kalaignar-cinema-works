from pathlib import Path
import json, re

root = Path('.')
W = root / 'works' / 'maruthanattu-ilavarasi'
T = W / 'transcription'
P = T / 'pages'
N = W / 'notes'
P.mkdir(parents=True, exist_ok=True)
N.mkdir(parents=True, exist_ok=True)

idxp = T / 'index.json'
idx = json.loads(idxp.read_text(encoding='utf-8'))
assert idx['first_pass_pages_completed'] == 15, idx['first_pass_pages_completed']
assert idx['first_pass_current_through_pdf'] == 16, idx['first_pass_current_through_pdf']
assert idx['open_uncertainty_markers'] == 0

pages = {
'017-left.md': '''<!-- source: pdf=17 side=left printed=16 status=draft -->

# மருதநாட்டு இளவரசி

இந்த நாட்டில், நாட்டு மக்கள் செய்த பாக்கியம் ரௌத்திரன் படுகொலை செய்யப்பட்டான்.

துர்ஜயன்:- அப்படிச் சொல்! இளவரசன் செய்தது அநீதி அதைத்தடுக்க அவனைக் கொலை செய்தாய்!

காண்:- அந்த புண்ணியம் எனக்குக்கிடைக்கவில்லை.

கோபதி:- பின் யாருக்குக்கிடைத்தது? வரட்டு வாதம் புரியும் வக்கிரபுத்திக்காரா வஞ்சகா! நெஞ்சம் பதரும் செயலைப்புரிந்துவிட்டு நீதி, ஞாயம், நேர்மை இவைகளை பேச வந்துவிட்ட கொலைகாரா! பின் யாருக்குக் கிடைத்தது?

துர்ஜயன்:- இவன் கட்டாரிக்குக் கிடைத்தது!

காண்:- கிடைக்காத எங்கள் குலச்செல்வத்தைக்கொல்லும் பாக்கியம் இவன் கட்டாரிக்கு கிடைத்தது!

(மகன் நிரபராதி இந்நாட்டு இளவரசன் என்று நிரூபிக்க மகாராணி சித்ரா கட்டாரியுடன் அங்கு காட்சி அளிக்கிறாள்)

சித்ரா:- இதோ இருக்கிறது அந்தக் கட்டாரி!

கோபதி:- எங்கே?

துர்ஜயன்:- காணாமல்போன என் கட்டாரியல்லவா இது உனக்கு எப்படிக்கிடைத்தது? மகாராஜா ஏதோ சூழ்ச்சி நடக்கிறது.

கோபதி:- நீ யார்?

சித்ரா:- என்னைத்தெரியவில்லையா? இந்த அபாக்கியவதியைத் தெரியவில்லையா சுவாமி

கோபதி:- ஆ......! (ஆச்சரியத்தால்) சித்ரா!

துர்ஜயன்:- சித்ரா!

சபையோர்:- மகாராணி! மகாராணி!! மகாராணி!!!

சித்ரா:- ஆம். மகாராணிதான்!

துர்ஜயன்:- மந்திரி அன்பானந்தரோடு புதுவாழ்வு நடத்தப்போன புனித மகாராணி!

கோபதி:- விபசாரி!

சித்ரா:- ஆ! சுவாமி, என்னைக் கொன்றுவிடுங்கள். அந்த வார்த்தையை மறுமுறையும் கூறாதீர்கள். குழந்
''',
'017-right.md': '''<!-- source: pdf=17 side=right printed=17 status=draft duplicate-scan-pdf=18 -->

# மருதநாட்டு இளவரசி

தையைக் காப்பாற்ற ஒரே இடத்திலும், கொடுமை பின் தொடர நான் பெற்ற வைரத்தை ஒரு கிழவியிடம் ஒப்பி விட்டு காளி கோயிலில் கண்ணீர் சிந்திக்கிடந்தவள் நான். இதோ குற்றவாளி கூண்டிலிருப்பவன் இந்நாட்டு இளவரசன், நம்முடைய மகன்.

காண்டி:- நான் இளவரசனா? என் தாயாரா?

(தன் கையில் வைத்திருந்த பதக்கத்தைக் காண்டிபனிடம் காட்டுகிறாள். அவன் கழுத்தை தடவிப் பார்த்துவிட்டு உண்மையிலேயே, தன் தாயார் இருப்பதைக்கண்டு)

காண்டி:- அம்மா!

சித்ரா:- கலங்காதே, கண்ணே! இனி நமக்கு நல்ல காலம் தான்.

துர்ஜய:- மகனுக்கு ஒரு நீதி, மற்றவருக்கு ஒரு நீதி என்ற மரபில் மன்னர் பிறக்கவில்லை. மந்திரி அன்பானந்தரோடு மகாராணி ஓடியதையும் அவர் மறக்கவில்லை.

கோபதி:- மகனும்! மகன்! காமத்தால் கருத்திழந்து, கள்ள நாய்களோடு ஓடிப்போனவள் காளி கோவிலில் இருந்தாளாம். கதை அளக்கிறாள் கதை! இந்த விபசாரியைப்பாதாள சிறையில் தள்ளுங்கள். இந்த வேசிக்கு உடந்தையாக இருந்த காளி கோவிலின் சட்டம் இன்றோடு ஒழியட்டும்! இவனையும் கொண்டுபோங்கள். இன்றோடு இவன் தலை பலிபீடத்தில் உருளட்டும். பட்டத்தின் இளவரசனைக் கொன்ற இந்தப் பாவியின் பச்சை ரத்தம் பலிபீடத்தை நனைக்கட்டும்.

## காட்சி 9.

(தன் மகள் மானத்தையும், தன் மகன் உயிருக்கும் எமனாக இருந்தது துர்ஜயன்தான் என்பதை தன் மகள் முத்தம்மாளின் மூலம் அறிந்த காளிங்கன் அவன் சூழ்ச்சிகளை வெளிப்படுத்த அரண்மனை செல்கிறான். கோபதிவர்மன், காண்டிபனுக்குத் தீர்ப்புக் கூறிவிட்டு அந்தப்புரத்திலிருக்கிறான்.)
''',
'019-left.md': '''<!-- source: pdf=19 side=left printed=18 status=draft duplicate-scan-pdf=20 -->

# மருதநாட்டு இளவரசி

கோபதி:- ரௌத்திரன் உம்முடைய மகனா? எவ்வளவு பெரிய அக்கிரமம்!

காளிங்:- அதைவிட அக்கிரமம் அன்பானந்தரைக் கொன்று அரண்மனைத் தோட்டத்திலே புதைத்துவிட்டு அரசியுடன் ஓடியதாக அபாண்டம் சுமத்தியது!... இதோ பாருங்கள், அன்பானந்தரின் எலும்புக்கூடு. அந்தப் புனித மூர்த்தியை நான்தான் புதைத்தேன்.

கோபதி:- எத்தனை பயங்கரச் சூழ்ச்சிகள்!

காளிங்:- அந்தப் பாவியின் செல்வாக்கைப் பலப்படுத்தத்தான்!

கோபதி:- ஆ! துர்ஜயனுடைய மோதிரம்!

காளிங்:- அவசரத்தில் அதைக்கூடக்கவனிக்கவில்லை.

(உண்மையை அறிந்த அரசன், காண்டிபனைக் காப்பாற்ற பலிபீடம் நோக்கி வருகிறான். தன்னை மானபங்கம் செய்த துர்ஜயனைப் பழிவாங்க, முத்தம்மாளும் தன்னை ஏமாற்றித் தன் மகனை இளவரசனாக்கி அவனைக் கொன்றான் என்ற கொதிப்பில் காளிங்கனும் பலிபீடம் நோக்கி வருகிறார்கள்.)

## காட்சி 10.

பலி பீடம்.

துர்ஜய:- நீ, கடைசியாகச் சொல்வது?

காண்டி:- கடைசியாகச் சொல்வது? யாரிடத்தில் சொல்வது! என் உயிரைக் குடிக்கத் துடித்து நிற்கும் சாவியிடத்தில் சொல்வதா? என் கழுத்தை நெறிக்கக் காத்திருக்கும் கத்தி இடத்தில் சொல்வதா? அல்லது வழிந்தோடும் என் ரத்தத்தைப் பார்த்து ரசிக்க வந்திருக்கும் உன்னிடத்தில் சொல்வதா? யாரிடத்தில் சொன்னாலும் சரி! யார் கேட்டாலும் சரி? கடைசி நேரத்திலாவது என் இதயத் துடிப்பு ஆவேசமாகத் துடித்து ஓயட்டும்! என் கண்களில் ஒருமுறை கனல் வீசி பிறகு அணைந்து போகட்டும்! என் ரத்தம் சூடேறிக் கொதித்துப் பிறகு ஜில்லிட்டுப் போ
''',
'019-right.md': '''<!-- source: pdf=19 side=right printed=19 status=draft duplicate-scan-pdf=20 -->

# மருதநாட்டு இளவரசி

ட்டும்! நீதியின் நிலைக்களமாய், நேர்மையின் உலைக்களமாய் வாழ்ந்த வண்டமிழ் வளநாடே! நீ, சூதகர்களின் உறைவிடமாய், சூழ்ச்சியின் இருப்பிடமாய் ஆனது ஏன்? தூய்மை, அன்பு, சத்தியம் இவைகள் மட்டும் தாங்கிய தங்கத் தாய் நாடே! நீ துரோகிகளை, துன்மார்க்கர்களை, துஷ்டர்களைத் தாங்குவது ஏன்? இந்தக் கேள்விகளுக்கெல்லாம் எனக்குக் கிடைக்கும் ஒரே பதில், பலிபீடம்! பலிபீடம்!! இந்தப் பயங்கரமான வார்த்தைதானா? ஏ! கொடுமை தாண்டவமாடும் குறிஞ்சிநாடே! நீ என்னைக் கொல்வதோடு என் ரத்தத்தை உறிஞ்சி கொழுப்பதோடு இருக்கக்கூடாதா? என் ராணியின் வாழ்வையுமா வாட்டவேண்டும்? என் ஆசைக் காதலியை என்னிடம் இருந்து பிரித்து, என்னைப் பெற்ற தாயாரைப் பாதாள சிறையில் பூட்டிவிட்டாயே! என் நெஞ்சைச் சிதள் சிதளாகப் பிரிக்கிறாயே! பச்சாத்தாபப் படுகிறாயே! புரிதாபம், ஈவு, இரக்கம் எள்ளளவும் இல்லையா உனக்கு? என்னைக் காதலித்தாள், எனக்கு வாழ்வு அளித்தாள், மாநிலம் சாய்ந்தாலும் உம்மை மறவேன் என்றாள், பூங்காட்டில் புறங்காணும் பூங்குழலாள் எங்கோ போய்விட்டாள்! சாக்காட்டின் அடிவாரத்திலும் அவளைச்சந்திக்கமுடியாத பாவியாகிவிட்டேனே! என் அறிவு வந்த பருவ முதல் என்னைப் பெற்ற அப்பா அம்மா யார் யார் என்று ஏங்கித் தவித்தேன்! மகனே என்று ஒளி வீசும் கண்களோடு அன்பு மொழி பேசிய என் அன்னையின் முகத்தைச் சரியாகக்கூடப் பார்க்கவில்லை! அவ்வளவு சீக்கிரத்தில் சாவதா? அந்த ஆனந்தத்தை அக்கிரமக்காரர்கள் ரசிப்பதா? இந்த மண்ணிலேதான் பிறந்தேன்! இந்த மண்ணிலேதான் மழலைமொழி பேசி தவழ்ந்து விளையாடினேன்! இந்த மண்ணிலேதான் சவமாகச் சாயப்போகிறேன். வந்தாரை வாழவைக்கும் இந்த மண்ணில் சொந்தநாட்டுக்காரன் அநியாயமாகச் சாவதா? குற்றமற்றவன் சாவதா? கொடுமையை நினைக்கவும் தெரியாதவன் சாவதா? என் சாவு உங்களுக்கு ஒரு பாடமாக இருக்கட்டும். இனிமேல் இந்தப் பலிபீடத்தில் நிரபராதிகள் எலும்பு நொறுங்காமல் பார்த்துக்கொள்
''',
'021-left.md': '''<!-- source: pdf=21 side=left printed=20 status=draft duplicate-scan-pdf=22 -->

# மருதநாட்டு இளவரசி

ளுங்கள். உழைக்க என்னவேண்டுமானாலும் செய்துவிடலாம் என்ற அகங்காரத்தை, ஆணவத்தை அரசாங்கச்சட்டத்தை, அதற்குத் தூபம்போடும் துரோகக்கும்பலை, துர்ஜயன் கூட்டத்தைப் பலிபீடத்தில் நிறுத்துங்கள். சூழ்ச்சியின் முதுகெலும்பைச் சுக்கு சுக்காக நொறுக்குங்கள். துரோகத்தை தூள் தூளாக நொறுக்குங்கள். அக்கிரமத்தை அணுஅணுவாக வீழ்த்..........

(ஆவேசத்தில் கால் இடறி கீழே விழுகிறான் காண்டிபன்) வீழ்ந்தது போதுமினி நாமே வாழ்வோம்! அழிந்தது போதுமினி நாமே ஆழ்வோம்!

துர்ஜயன்:- போதும் உன் ஒப்பாரி! ....நடக்கட்டும்.

[தூக்குமேடை மணி ஓசை கேட்கிறது. இரண்டுமுறை கேட்டான், மூன்றுமுறை கேட்கவில்லை. காரணம்? மூன்றுமுறை மணி ஒலித்தால் காண்டிபன் தலை கீழே உருளும் என்று நினைத்த ராணி தன் தலையை மூன்றாம் அடிக்கு நேரே பலி கொடுத்தாள். மூன்றுமுறை ஒலிக்காத காரணத்தால் எல்லோரும் திகைக்க, நிமிர்ந்து பார்க்கிறான் காண்டிபன்.]

காண்டி:- ராணி!

[தன் அரச குமாரி கீழே விழுந்ததை அறிந்த ரம்பா, ராணியை மடியில் தூக்கிவைக்கிறாள்.]

துர்ஜய:- ....உம் நிறுத்தாதே, நடக்கட்டும்.

(காண்டிபன் கழுத்தை நறுக்க கொலையாளிதயாராகிறான் மறுக்க யாதொரு வழியும் தெரியாமல் திகைக்கிறான் அழகு. அப்போது ரம்பா தும்முகிறாள். தும்மலைக் கேட்டவுடன் தன் வழக்கமான “குதி”யை ஆரம்பித்து வெட்டை நிறுத்துகிறான்.)

துர்ஜய:- டேய்! பிடியுங்கள்.

(அது சமயம், அரசன் தன் மகனைப் பார்க்க அங்கு வருகிறான். தன் மகன் உயிரோடு இருப்பதைப் பார்த்து.......)

கோபதி:- ஆ! காண்டிபா!
''',
'021-right.md': '''<!-- source: pdf=21 side=right printed=21 status=draft duplicate-scan-pdf=22 -->

# மருதநாட்டு இளவரசி

அழகு:- விடு! காண்டிபன் இளவரசனா? காண்டிபா!

(துர்ஜயன், காளிங்கன், முத்தம்மாள் இருவரையும் கண்டு கதிகலங்கி அங்கிருந்து தப்ப முயல்கிறான்.)

துர்ஜயன்:- காளிங்கன், முத்தம்மாள்!

(துர்ஜயன் கூட்டத்தில் புகுந்து ஓடுகிறான். தன்னை மானபங்கம் செய்ததற்காக பிரதி உபகாரமாக, தன் கையிலுள்ள பிச்சுவாவினால் வஞ்சம் தீர்த்துக்கொள்கிறாள் முத்தம்மாள்!)

காளிங்:- இருதய சுத்தமில்லாத அத்தனைபேர்களுக்கும் இதுதான் முடிவு!

அழகு:- ரம்பா!

காண்டி:- ராணி...!

ராணி:- சுவாமி...!

காண்டி:- இவள்தான், ராணி! மருதநாட்டு இளவரசி!

கோபதி:- இளவரசர்!

பொதுமக்கள்:- வாழ்க!

காண்டி:- வளம், வழியும் குறிஞ்சிநாட்டுப் பெருமக்களே, வணக்கம்; நான் இந்த மாநிலத்து மன்னனில்லை. மக்களின் தலைவன், மக்களின் தொண்டன். குறிஞ்சி நாட்டு முடியாட்சி முடிவுற்றது. இனி குடியாட்சிப் பூத்துக்குலுங்கும், புதுவாழ்வு மலரும், புதுக்கருத்து வளரும், எல்லோரும் ஓர் குலம்! எல்லோரும் ஓர் இனம்!! எல்லோரும் இந்நாட்டு மன்னர்!!!

நலம்!

★
'''
}

for name, body in pages.items():
    path = P / name
    if path.exists():
        raise SystemExit(f'unexpected existing final page record: {path}')
    path.write_text(body, encoding='utf-8')

# Reconcile canonical index around the newly discovered two-up/duplicate scan geometry.
new_records = [
    {"pdf_page":17,"printed_page":16,"scan_side":"left","kind":"screenplay","source_scene_id":"8","status":"draft","path":"pages/017-left.md","duplicate_scan_pdf_page":18},
    {"pdf_page":17,"printed_page":17,"scan_side":"right","kind":"screenplay","source_scene_ids":["8","9"],"status":"draft","path":"pages/017-right.md","duplicate_scan_pdf_page":18},
    {"pdf_page":19,"printed_page":18,"scan_side":"left","kind":"screenplay","source_scene_ids":["9","10"],"status":"draft","path":"pages/019-left.md","duplicate_scan_pdf_page":20},
    {"pdf_page":19,"printed_page":19,"scan_side":"right","kind":"screenplay","source_scene_id":"10","status":"draft","path":"pages/019-right.md","duplicate_scan_pdf_page":20},
    {"pdf_page":21,"printed_page":20,"scan_side":"left","kind":"screenplay","source_scene_id":"10","status":"draft","path":"pages/021-left.md","duplicate_scan_pdf_page":22},
    {"pdf_page":21,"printed_page":21,"scan_side":"right","kind":"screenplay","source_scene_id":"10","status":"draft","path":"pages/021-right.md","duplicate_scan_pdf_page":22}
]
existing_printed = {r['printed_page'] for r in idx['page_records']}
assert existing_printed == set(range(1,16)), existing_printed
idx['page_records'].extend(new_records)
idx.update({
    "status":"first-pass-complete-draft",
    "first_pass_pages_completed":21,
    "first_pass_pdf_range_completed":"2-22 (PDF 18,20,22 exact duplicate spreads excluded from canonical text)",
    "first_pass_current_through_pdf":22,
    "first_pass_current_through_logical_printed":21,
    "draft_pages":21,
    "visual_verified_pages":0,
    "historical_glyph_first_pass_checked_pages":21,
    "historical_glyph_final_verified_pages":0,
    "open_uncertainty_markers":0,
    "duplicate_pdf_spreads":[
        {"pdf_page":18,"duplicates_pdf_page":17,"printed_pages":[16,17]},
        {"pdf_page":20,"duplicates_pdf_page":19,"printed_pages":[18,19]},
        {"pdf_page":22,"duplicates_pdf_page":21,"printed_pages":[20,21]}
    ],
    "canonical_representative_pdf_pages_for_printed_16_21":[17,19,21],
    "next_batch_pdf_pages":None,
    "next_action":"Begin independent visual-fidelity plus final historical-glyph verification for logical printed pages 1–5 (source PDF 2–6) as the first five-page verification batch. Re-read the controlling pixels independently, correct any draft mismatch before marking a page verified, keep uncertainty explicit, and keep all structured derivatives blocked until all 21 canonical logical pages pass both gates."
})
assert len(idx['page_records']) == 21
assert {r['printed_page'] for r in idx['page_records']} == set(range(1,22))
assert len({r['path'] for r in idx['page_records']}) == 21
assert all((T / r['path']).exists() for r in idx['page_records'])
idxp.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')

(W/'mapping.md').write_text('''# மருதநாட்டு இளவரசி — structural mapping

Status: **COMPLETE-VERIFIED-CORRECTED — two-up duplicate scan geometry recorded during final Tamil first pass**.

The scan is image-only. Mapping is established from rendered source pixels, not OCR or extracted text. Two corrections were required during canonical first pass: direct PDF-11 review restored the source-visible `காட்சி 7.`, and final-range review established that PDF 17–22 consists of three two-page spreads, each duplicated once.

## Pagination and content map

| PDF | Printed / logical page | Source structure |
|---:|:---:|---|
| 1 | — | Front cover: `மருதநாட்டு இளவரசி`; cover imprint `வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.`; `விலை அணா 3.`; ownership/library stamps overlay the cover. |
| 2 | logical 1 | Title/credit box with `வசனம் : மு. கருணாநிதி.`; beginning of the unnumbered opening source segment. Numeral `1` is not visibly printed. |
| 3 | 2 | Unnumbered opening segment continues. |
| 4 | 3 | Unnumbered opening segment continues; printed `* * *` separator occurs mid-page. |
| 5 | 4 | `காட்சி 2.` begins. |
| 6 | 5 | `காட்சி 2.` continues; `காட்சி 3.` begins mid-page. |
| 7 | 6 | `காட்சி 3.` continues. |
| 8 | 7 | `காட்சி 3.` closes; `காட்சி 4.` begins/closes; `காட்சி 5.` begins near page foot. |
| 9 | 8 | `காட்சி 5.` continues; `காட்சி 6.` begins near page foot. |
| 10 | 9 | `காட்சி 6.` continues. |
| 11 | 10 | `காட்சி 6.` continues; `காட்சி 7.` begins with `(ரௌத்திரன்; காண்டியன் குரலில் பேசுகிறான்)`. |
| 12 | 11 | `காட்சி 7.` continues/closes. |
| 13 | 12 | `காட்சி 8.` begins with `(ராஜ தர்பார்)`. |
| 14 | 13 | `காட்சி 8.` continues. |
| 15 | 14 | `காட்சி 8.` continues. |
| 16 | 15 | `காட்சி 8.` continues. |
| 17 | 16 left / 17 right | **Two-page spread.** Printed 16 continues `காட்சி 8.`; printed 17 closes scene 8 and begins `காட்சி 9.`. Canonical representative for both logical pages. |
| 18 | duplicate of PDF 17 | **Exact duplicate spread** of PDF 17; no new canonical text. |
| 19 | 18 left / 19 right | **Two-page spread.** Printed 18 closes `காட்சி 9.` and begins `காட்சி 10.` with `பலி பீடம்.`; printed 19 continues scene 10. Canonical representative for both logical pages. |
| 20 | duplicate of PDF 19 | **Exact duplicate spread** of PDF 19; no new canonical text. |
| 21 | 20 left / 21 right | **Two-page spread.** Printed 20 continues scene 10; printed 21 concludes it with `நலம்!` and decorative star. Canonical representative for both logical pages. |
| 22 | duplicate of PDF 21 | **Exact duplicate spread** of PDF 21; no new canonical text. |

PDF 2–16 therefore maps one scan page to one logical printed page. PDF 17/19/21 are two-up representative spreads for printed pages 16–21; PDF 18/20/22 are exact duplicates and are excluded from canonical text to prevent duplication.

## Canonical logical-page disposition for the final range

- printed 16 → PDF 17 left → `transcription/pages/017-left.md`;
- printed 17 → PDF 17 right → `transcription/pages/017-right.md`; PDF 18 duplicates the same spread;
- printed 18 → PDF 19 left → `transcription/pages/019-left.md`;
- printed 19 → PDF 19 right → `transcription/pages/019-right.md`; PDF 20 duplicates the same spread;
- printed 20 → PDF 21 left → `transcription/pages/021-left.md`;
- printed 21 → PDF 21 right → `transcription/pages/021-right.md`; PDF 22 duplicates the same spread.

## Corrected observed source-heading sequence

| Order | Representative PDF / side | Printed/logical | Exact heading / attached source marker |
|---:|:---:|:---:|---|
| 1 | 5 | 4 | `காட்சி 2.` |
| 2 | 6 | 5 | `காட்சி 3.` |
| 3 | 8 | 7 | `காட்சி 4.` |
| 4 | 8 | 7 | `காட்சி 5.` |
| 5 | 9 | 8 | `காட்சி 6.` |
| 6 | 11 | 10 | `காட்சி 7.` + `(ரௌத்திரன்; காண்டியன் குரலில் பேசுகிறான்)` |
| 7 | 13 | 12 | `காட்சி 8.` + `(ராஜ தர்பார்)` |
| 8 | 17 right | 17 | `காட்சி 9.` |
| 9 | 19 left | 18 | `காட்சி 10.` + `பலி பீடம்.` |

### Numbering disposition

- no source-visible `காட்சி 1.` heading is present in the unnumbered opening;
- source-visible numbered sequence is contiguous from 2 through 10;
- the earlier intake claim that scene 7 was absent is superseded;
- duplicate physical scans 18/20/22 do not create duplicate scene starts.

## Other structures

- recurring running header: `மருதநாட்டு இளவரசி—திரை வசனம்`;
- PDF 4 has a `* * *` structural separator;
- no clearly bounded printed song, lyric or chant block was identified during first pass;
- printed logical page 21 closes with `நலம்!` and a decorative star; the overlaid library stamp is non-source;
- older typeforms require enlarged source-pixel review.

## Gate state

- source intake: **complete, duplicate-scan geometry documented**;
- structural mapping: **complete-verified-corrected**;
- canonical Tamil first pass: **21/21 logical pages DRAFT — COMPLETE**;
- prospective historical-glyph coverage: **21/21 COMPLETE / draft only**;
- visual fidelity: **not started**;
- final historical-glyph audit: **not started**;
- scene/dialogue/character/song/English/reader layers: **blocked**.
''', encoding='utf-8')

(N/'duplicate-scan-correction.md').write_text('''# மருதநாட்டு இளவரசி — final-range duplicate scan correction

Direct source rendering during the final Tamil first-pass range established a non-obvious scan geometry that supersedes the initial one-PDF-page/one-printed-page assumption after PDF 16.

- PDF 17 and PDF 18 are identical two-page spreads containing printed pages **16–17**.
- PDF 19 and PDF 20 are identical two-page spreads containing printed pages **18–19**.
- PDF 21 and PDF 22 are identical two-page spreads containing printed pages **20–21**.

Canonical text therefore uses representative spreads PDF **17, 19, 21** only, split into left/right logical-page records. Duplicate physical scans **18, 20, 22** are retained in provenance but contribute no second copy of text.

This correction also relocates source-heading provenance without changing the printed sequence: `காட்சி 9.` is on printed page 17 / PDF 17 right, and `காட்சி 10.` + `பலி பீடம்.` is on printed page 18 / PDF 19 left.

No source text was inferred from the duplicate relationship; the rendered pixels remain controlling.
''', encoding='utf-8')

(N/'T1_FINAL_BATCH_017_022.md').write_text('''# மருதநாட்டு இளவரசி — Tamil T1 final range

Status: **PASS / FIRST-PASS COMPLETE-DRAFT**.

Final source review covered physical PDF 17–22 and established that this range contains **6 logical printed pages across 3 unique two-up spreads**, with each spread duplicated once.

Canonical logical pages added:

- printed 16 — PDF 17 left;
- printed 17 — PDF 17 right;
- printed 18 — PDF 19 left;
- printed 19 — PDF 19 right;
- printed 20 — PDF 21 left;
- printed 21 — PDF 21 right.

Duplicate physical scans excluded from canonical text: **PDF 18 = PDF 17, PDF 20 = PDF 19, PDF 22 = PDF 21**.

Result: **21/21 canonical logical pages DRAFT**, prospective historical-glyph inspection **21/21**, first-pass uncertainty markers **0**. Independent visual-fidelity and final historical-glyph verification remain **0/21**, so no structured derivative layer is opened yet.
''', encoding='utf-8')

(N/'historical-glyph-audit.md').write_text('''# மருதநாட்டு இளவரசி — historical Tamil glyph audit

Status: **FIRST-PASS PROSPECTIVE COVERAGE COMPLETE — 21/21 canonical logical pages checked; final independent verification not started**.

Known families checked prospectively on every drafted logical page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules remain source-first: source pixels control character identity; OCR/extracted text is only a candidate; no global replacements; glyph decoding must not modernize wording.

## Coverage

- canonical logical printed pages 1–21: **first-pass glyph check COMPLETE / draft only**;
- representative final-range scans: PDF 17, 19, 21 split left/right;
- duplicate scans PDF 18, 20, 22: provenance-only duplicates, not separate canonical text;
- final independent historical-glyph verification: **0/21**;
- open first-pass glyph uncertainty markers: **0**.

Representative first-pass adjudications include the restored source-visible `காட்சி 7.`, source-irregular forms retained in PDF 12–16, and final-range two-up page geometry. None of these prospective readings is promoted to final verification by this file.

All canonical pages remain `draft` until the independent visual-fidelity + final historical-glyph closure campaign.
''', encoding='utf-8')

(T/'README.md').write_text('''# மருதநாட்டு இளவரசி — canonical Tamil transcription

Status: **FIRST PASS COMPLETE — 21/21 canonical logical pages DRAFT**.

The rendered scan is canonical authority. The user-supplied extracted transcription was used only as a candidate/navigation aid and never overrides source pixels.

Canonical records cover printed logical pages **1–21**. PDF 2–16 maps one scan page to printed pages 1–15. The final six printed pages are stored as left/right logical-page records from representative two-up spreads:

- PDF 17 → printed 16–17; PDF 18 is an exact duplicate;
- PDF 19 → printed 18–19; PDF 20 is an exact duplicate;
- PDF 21 → printed 20–21; PDF 22 is an exact duplicate.

All 21 logical pages remain **draft**. Prospective historical-glyph coverage is **21/21**; independent visual-fidelity and final historical-glyph verification are **0/21**. Open first-pass uncertainty markers: **0**.

Source structure remains unchanged: PDF 2–4 is an unnumbered opening; numbered scene headings are 2 through 10; scene 9 begins on printed 17 / PDF 17 right; scene 10 begins on printed 18 / PDF 19 left; printed 21 closes with `நலம்!` and a decorative star.

## Next gate

Begin independent visual-fidelity plus final historical-glyph verification for **logical printed pages 1–5 (source PDF 2–6)**. Re-read source pixels independently, correct any draft mismatch before marking verified, keep uncertainty explicit, and do not start structured derivatives until all 21 logical pages pass both verification gates.
''', encoding='utf-8')

(W/'README.md').write_text('''# மருதநாட்டு இளவரசி

Source-led archival workspace for the scanned **`மருதநாட்டு இளவரசி`** திரை வசனம் booklet.

## Source authority

Controlling source: `TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**. The scan remains canonical authority and is not committed.

Visible source evidence includes title `மருதநாட்டு இளவரசி`, recurring body header `மருதநாட்டு இளவரசி—திரை வசனம்`, printed credit `வசனம் : மு. கருணாநிதி.`, cover imprint `வியந்தமிழ்ப் பாசறை, கோவில்பட்டி.`, and cover price `விலை அணா 3.`. No explicit edition statement or publication year was observed.

## Corrected source geometry

Source intake and structural mapping are **COMPLETE-VERIFIED-CORRECTED**.

- PDF 1: cover.
- PDF 2–16: one logical printed page per scan, representing printed/logical pages 1–15.
- PDF 17: two-page spread containing printed 16–17; PDF 18 is its exact duplicate.
- PDF 19: spread 18–19; PDF 20 is its exact duplicate.
- PDF 21: spread 20–21; PDF 22 is its exact duplicate.
- Canonical text uses each printed page exactly once; duplicate physical scans 18/20/22 are provenance-only.
- PDF 2–4 remains an unnumbered opening; no `காட்சி 1.` is invented.
- Source-numbered headings are **2,3,4,5,6,7,8,9,10**.
- `காட்சி 9.` is on printed 17 / PDF 17 right.
- `காட்சி 10.` + `பலி பீடம்.` is on printed 18 / PDF 19 left.
- printed 21 closes with `நலம்!` and decorative star.

## Current gate

Canonical Tamil first pass: **COMPLETE — 21/21 logical pages DRAFT**. Prospective historical-glyph coverage: **21/21**. Open first-pass uncertainty markers: **0**. Independent visual-fidelity verification: **0/21**. Final historical-glyph verification: **0/21**. Structured scene/dialogue/character/song/English layers remain **BLOCKED**.

## Exact next activity

> **Begin independent visual-fidelity plus final historical-glyph verification for logical printed pages 1–5 (source PDF 2–6) as the first five-page verification batch. Re-read the controlling pixels independently, correct any draft mismatch before marking a page verified, keep uncertainty explicit, and keep structured derivatives blocked until all 21 canonical logical pages pass both gates.**
''', encoding='utf-8')

(W/'metadata.yaml').write_text('''id: maruthanattu-ilavarasi
title_ta: "மருதநாட்டு இளவரசி"
work_type: film
source_type: printed_screenplay_dialogue_booklet
source_identifier: TVA_BOK_0065774
source_filename: "TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf"
source_pdf_pages: 22
source_byte_size: 9330870
source_sha256: 8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f
source_embedded_text: false
source_image_only: true
credit_as_printed: "வசனம் : மு. கருணாநிதி."
recurring_header_as_printed: "மருதநாட்டு இளவரசி—திரை வசனம்"
cover_imprint_as_printed: "வியந்தமிழ்ப் பாசறை, கோவில்பட்டி."
cover_price_as_printed: "விலை அணா 3."
publication_year_as_printed: null
edition_statement_as_printed: null
cover_pdf_pages: "1"
main_text_pdf_pages: "2-22"
main_text_logical_printed_pages: "1-21"
visible_printed_page_numbers: "2-21"
body_pagination_formula: "PDF 2-16 => printed 1-15; PDF 17/19/21 are two-page representative spreads => printed 16-21; PDF 18/20/22 duplicate the preceding spread"
duplicate_pdf_spreads: ["18=17", "20=19", "22=21"]
canonical_representative_final_spread_pdf_pages: [17, 19, 21]
source_intake: complete
structural_mapping: complete-verified-corrected
mapping_path: works/maruthanattu-ilavarasi/mapping.md
source_numbered_scene_headings: true
scene_headings_observed: 9
scene_ids_observed: ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
scene_number_gaps_observed: []
source_scene_1_heading_observed: false
opening_unnumbered_segment_pdf_pages: "2-4"
opening_unnumbered_segment_logical_printed_pages: "1-3"
historical_glyph_policy: required
historical_glyph_guide_path: docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md
historical_glyph_audit_path: works/maruthanattu-ilavarasi/notes/historical-glyph-audit.md
canonical_tamil_transcription: first-pass-complete-draft
canonical_tamil_first_pass_pages_completed: 21
canonical_tamil_first_pass_pdf_range_completed: "2-22 (18,20,22 exact duplicate spreads excluded from canonical text)"
canonical_tamil_first_pass_current_through_pdf: 22
canonical_tamil_current_batch_path: works/maruthanattu-ilavarasi/transcription/pages/021-right.md
canonical_tamil_total_body_pages: 21
visual_fidelity_audit: not-started
historical_glyph_audit: first-pass-complete-21-of-21
structured_derivatives: blocked
next_action: "Begin independent visual-fidelity plus final historical-glyph verification for logical printed pages 1–5 (source PDF 2–6) as the first five-page verification batch. Re-read the controlling pixels independently, correct any draft mismatch before marking a page verified, keep uncertainty explicit, and keep all structured derivatives blocked until all 21 canonical logical pages pass both gates."
''', encoding='utf-8')

(W/'PROJECT_HANDOVER.md').write_text('''# மருதநாட்டு இளவரசி — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/maruthanattu-ilavarasi/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**. Do not commit the PDF.

## Durable state

- source intake: **COMPLETE**;
- structural mapping: **COMPLETE-VERIFIED-CORRECTED**;
- canonical logical printed pages: **1–21**;
- PDF 2–16 represents printed 1–15 one-to-one;
- PDF 17/19/21 are representative two-up spreads for printed 16–21;
- PDF 18/20/22 are exact duplicate spreads and add no canonical text;
- opening printed 1–3 remains unnumbered; do not invent `காட்சி 1.`;
- observed numbered headings: **2,3,4,5,6,7,8,9,10**;
- scene 9 provenance: printed 17 / PDF 17 right;
- scene 10 provenance: printed 18 / PDF 19 left;
- canonical Tamil first pass: **21/21 DRAFT — COMPLETE**;
- prospective historical-glyph coverage: **21/21 COMPLETE**;
- first-pass uncertainty markers: **0**;
- independent visual-fidelity verification: **0/21**;
- final historical-glyph verification: **0/21**;
- later structured/English/reader derivatives: **BLOCKED**.

## Exact next activity

> **Begin independent visual-fidelity plus final historical-glyph verification for logical printed pages 1–5 (source PDF 2–6) as the first five-page verification batch. Re-read the controlling pixels independently, correct any draft mismatch before marking a page verified, keep uncertainty explicit, and keep structured derivatives blocked until all 21 canonical logical pages pass both gates.**
''', encoding='utf-8')

(W/'NEXT_CHAT_PROMPT.md').write_text('''# Next Chat Prompt — மருதநாட்டு இளவரசி / verification logical pages 1–5

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/maruthanattu-ilavarasi/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / 9,330,870 bytes / SHA-256 `8191b345c8b82faa25b95d574287cb1510230daea63e32490284dd4482e05d2f` / image-only**.

## Durable state

- intake/mapping: **COMPLETE / COMPLETE-VERIFIED-CORRECTED**;
- final-range geometry: PDF 17=18 spread printed 16–17; PDF 19=20 spread printed 18–19; PDF 21=22 spread printed 20–21;
- duplicate scans 18/20/22 are provenance-only and must not duplicate canonical text;
- canonical Tamil first pass: **21/21 logical pages DRAFT — COMPLETE**;
- prospective historical-glyph coverage: **21/21**;
- open first-pass uncertainty markers: **0**;
- visual-fidelity verified: **0/21**;
- final historical-glyph verified: **0/21**;
- derivatives: **BLOCKED**.

## Next batch

> **Independently re-read logical printed pages 1–5 against the controlling pixels (source PDF 2–6). Correct any source mismatch first, then mark only passing pages verified. Complete both visual-fidelity and final historical-glyph checks for the same five logical pages. Do not use the user-supplied extracted transcription as authority, do not normalize the source, and do not begin structured derivatives until all 21 logical pages close both gates.**
''', encoding='utf-8')

# Synchronize data/works.json current record.
works_path = root/'data'/'works.json'
works = json.loads(works_path.read_text(encoding='utf-8'))
rec = next(x for x in works if x.get('id') == 'maruthanattu-ilavarasi')
rec.update({
    "body_pagination_formula":"PDF 2-16 => printed 1-15; PDF 17/19/21 are two-page representative spreads => printed 16-21; PDF 18/20/22 duplicate the preceding spread",
    "duplicate_pdf_spreads":["18=17","20=19","22=21"],
    "structural_mapping":"verified-corrected",
    "canonical_tamil_transcription":"first-pass-complete-draft",
    "canonical_tamil_first_pass_pages_completed":21,
    "canonical_tamil_first_pass_pdf_range_completed":"2-22 (18,20,22 exact duplicate spreads excluded from canonical text)",
    "canonical_tamil_first_pass_current_through_pdf":22,
    "canonical_tamil_current_batch_path":"works/maruthanattu-ilavarasi/transcription/pages/021-right.md",
    "historical_glyph_audit":"first-pass-complete-21-of-21",
    "tamil_transcription":"first-pass-complete-draft",
    "tamil_first_pass_complete":True,
    "tamil_transcription_through_pdf_page":22,
    "tamil_transcription_through_logical_printed_page":21,
    "tamil_transcription_draft_pages":21,
    "tamil_transcription_verified_pages":0,
    "tamil_transcription_review_pages":0,
    "tamil_fidelity_audit":"not-started",
    "canonical_range_fidelity_audit_complete":False,
    "total_canonical_pages":21,
    "total_verified_pages":0,
    "total_review_pages":0,
    "next_action":"Begin independent visual-fidelity plus final historical-glyph verification for logical printed pages 1–5 (source PDF 2–6) as the first five-page verification batch. Re-read the controlling pixels independently, correct any draft mismatch before marking a page verified, keep uncertainty explicit, and keep structured derivatives blocked until all 21 canonical logical pages pass both gates."
})
works_path.write_text(json.dumps(works, ensure_ascii=False, indent=2)+"\n", encoding='utf-8')

# Root README current-status section.
rp = root/'README.md'
rt = rp.read_text(encoding='utf-8')
start = rt.index('## மருதநாட்டு இளவரசி status')
end = rt.index('## வண்டிக்காரன் மகன் status', start)
section = '''## மருதநாட்டு இளவரசி status

`TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` is a **22-PDF-page image-only திரை வசனம் source** with corrected structural mapping.

- printed credit: **`வசனம் : மு. கருணாநிதி.`**;
- canonical logical body: **printed pages 1–21**;
- PDF 2–16 map one-to-one to printed 1–15;
- PDF 17/19/21 are two-up representative spreads for printed 16–21; PDF **18/20/22 are exact duplicate spreads**;
- opening printed 1–3 is unnumbered; no source `காட்சி 1.` is invented;
- numbered headings: **2,3,4,5,6,7,8,9,10**;
- canonical Tamil first pass: **21/21 DRAFT — COMPLETE**;
- prospective historical-glyph coverage: **21/21**;
- independent visual/glyph verification: **0/21**;
- first-pass uncertainty markers: **0**;
- later derivatives: **BLOCKED**.

**Next:** Independently verify logical printed pages **1–5 / source PDF 2–6** for both visual fidelity and final historical-glyph identity.

'''
rp.write_text(rt[:start]+section+rt[end:], encoding='utf-8')

# Master handover: replace the latest active Maruthanattu section if present.
hp = root/'docs'/'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
ht = hp.read_text(encoding='utf-8')
marker = '## 11. மருதநாட்டு இளவரசி active checkpoint'
pos = ht.rfind(marker)
if pos < 0:
    raise SystemExit('master handover marker missing')
current = '''## 11. மருதநாட்டு இளவரசி active checkpoint

Work: `works/maruthanattu-ilavarasi/`  
Source: `TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf`

- intake: **COMPLETE**;
- mapping: **COMPLETE-VERIFIED-CORRECTED**;
- canonical logical pages: **21**;
- duplicate scan geometry: **PDF 18=17, 20=19, 22=21**; representative spreads 17/19/21 contain printed 16–21;
- source headings: **2,3,4,5,6,7,8,9,10**; opening remains unnumbered;
- canonical Tamil first pass: **21/21 DRAFT — COMPLETE**;
- prospective historical-glyph coverage: **21/21**;
- visual-fidelity / final glyph verification: **0/21 / 0/21**;
- first-pass uncertainty markers: **0**;
- structured derivatives: **BLOCKED**.

**Exact next activity:** Independent visual-fidelity + final historical-glyph verification for logical printed pages **1–5 (source PDF 2–6)**. Correct draft mismatches before marking verified; no downstream derivative work until all 21 logical pages pass both gates.
'''
hp.write_text(ht[:pos]+current+'\n', encoding='utf-8')

# Status audit matrix + latest current checkpoint.
sp = root/'docs'/'STATUS_CONSISTENCY_AUDIT.md'
st = sp.read_text(encoding='utf-8')
row = '| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி | **Tamil T1 21/21 DRAFT COMPLETE; glyph-first-pass 21/21; final visual/glyph 0/21; duplicate scans 18=17, 20=19, 22=21** | headings **2,3,4,5,6,7,8,9,10**; opening unnumbered | not-started | not-started |'
st, n = re.subn(r'^\| Maruthanattu Ilavarasi / மருதநாட்டு இளவரசி \|.*$', row, st, count=1, flags=re.M)
if n != 1:
    raise SystemExit(f'status matrix row replacement count={n}')
marker2 = '## Maruthanattu Ilavarasi current checkpoint'
pos2 = st.rfind(marker2)
if pos2 < 0:
    raise SystemExit('status current marker missing')
curr2 = '''## Maruthanattu Ilavarasi current checkpoint

- source: `TVA_BOK_0065774_மருதநாட்டு_இளவரசி.pdf` — **22 PDF pages / image-only**;
- source intake / structural mapping: **COMPLETE / COMPLETE-VERIFIED-CORRECTED**;
- canonical logical printed pages: **1–21**;
- PDF 17/19/21 are representative two-page spreads; PDF **18/20/22 are exact duplicate physical scans**;
- opening logical pages 1–3 remain unnumbered; no synthetic scene 1;
- observed numbered scene headings: **2–10 contiguous**;
- canonical Tamil first pass: **21/21 DRAFT — COMPLETE**;
- prospective historical-glyph coverage: **21/21**;
- open first-pass uncertainty markers: **0**;
- independent visual-fidelity / final historical-glyph verification: **0/21 / 0/21**;
- later derivatives: **BLOCKED**.

**Next production phase:** Independently verify logical printed pages **1–5 (source PDF 2–6)** for visual fidelity and final historical-glyph identity. Correct any draft mismatch first; structured derivatives remain blocked until the full 21/21 dual gate passes.
'''
sp.write_text(st[:pos2]+curr2+'\n', encoding='utf-8')

# Normalize touched prose controls for git diff --check.
for _p in [hp, sp]:
    _s = _p.read_text(encoding='utf-8')
    _s = "\n".join(line.rstrip() for line in _s.splitlines()).rstrip() + "\n"
    _p.write_text(_s, encoding='utf-8')

# Integrity checks before commit.
idx2 = json.loads(idxp.read_text(encoding='utf-8'))
assert idx2['status'] == 'first-pass-complete-draft'
assert idx2['first_pass_pages_completed'] == 21
assert idx2['historical_glyph_first_pass_checked_pages'] == 21
assert idx2['visual_verified_pages'] == 0
assert idx2['historical_glyph_final_verified_pages'] == 0
assert idx2['open_uncertainty_markers'] == 0
assert {r['printed_page'] for r in idx2['page_records']} == set(range(1,22))
assert [x['pdf_page'] for x in idx2['duplicate_pdf_spreads']] == [18,20,22]
assert not (P/'018.md').exists()
assert not (P/'020.md').exists()
assert not (P/'022.md').exists()
print('Maruthanattu Ilavarasi T1 closure QA PASS: 21/21 logical draft pages; 3 duplicate spreads excluded; 0 first-pass uncertainties.')
