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


def replace_page(text, pdf, status, body):
    printed = pdf - 2
    pat = re.compile(
        rf'<!-- source: pdf={pdf} printed={printed} status=(?:draft|verified|review) -->.*?(?=<!-- source: pdf={pdf+1} printed={printed+1} status=(?:draft|verified|review) -->)',
        re.S,
    )
    m = pat.search(text)
    if not m:
        raise SystemExit(f'page span {pdf} not found')
    repl = f'<!-- source: pdf={pdf} printed={printed} status={status} -->\n\n{body.strip()}\n\n'
    return text[:m.start()] + repl + text[m.end():]


def replace_last_page(text, pdf, status, body):
    printed = pdf - 2
    # not used here, retained for completeness
    pat = re.compile(rf'<!-- source: pdf={pdf} printed={printed} status=(?:draft|verified|review) -->.*?$', re.S)
    m = pat.search(text)
    if not m:
        raise SystemExit(f'last page span {pdf} not found')
    repl = f'<!-- source: pdf={pdf} printed={printed} status={status} -->\n\n{body.strip()}\n'
    return text[:m.start()] + repl


page65 = r'''
⟦PDF 64–65 quoted poetic continuation: the long old-type poetic passage remains marker 49 and requires a separate glyph-level adjudication from the rendered scan; no outside literary text may fill it.⟧

வீரர்கள் : தச்...தச்...தச்...

முத் : இப்போது சொல்லுங்கள்...மானமும், வீரமும் எவ்வளவு மதிப்பு வாய்ந்தவை...அவைகளை மாற்றானின் காலடியில் மிதிக்க விடலாமா?

வீரர்கள் : கூடாது!...கூடாது!

முத் : அப்படியானால் பழுதாரை விடுவிக்க என் தலைமையில் ஒன்று சேருங்கள்.
'''

page66 = r'''
வீரன் : அண்ணே! உன் தலைமையில் பணி புரிய இந்தத் தம்பி எப்போதும் தயார்...

வீரர்கள் : தயார்.

நான் தயார்.

நானும் தயார்.

நானும் தயார்....

(வேலழகன் சிரித்தபடி வருகிறான்)

வேல : எல்லோரும் தயார்...ஆனால் நான் தான் தயார் இல்ல...விடுதலை வீரர்களாகிய உங்களை வெளியில் விட்டா!...ஏ? அடிமைகளே! மலைப்பாம்பின் வாயில் இருந்து கொண்டு விடுதலை மகுடியா ஊதுகிறாய்?...அதன் வயிற்றுக்குள்ளேயே உன்னைப் போட்டு விடுகிறேன்...பார்...இதோ தெரிகிறதாடா உனக்குச் சித்திரவதை செய்யப் போகும் சிறைச்சாலை...

முத் : சிறைச்சாலை!...புரட்சிக் கவிதை புரியாதே உமக்கு!...அறிவீர்...மாங்குயில் கூவிடும் பூஞ்சோலை...எமை மாட்ட நினைக்கும் சிறைச்சாலை...

வேல : எதிர்த்துப் பேசாதே...மூடு வாயை!......

[இழுத்து உள்ளே தள்ளுகிறான்.]

பழுதார் வாழும் பூச்சிகளே! புழுக்களே!...புலியை இடறுகிறீர்கள்—ஜாக்கிரதை;...'இம்' என்றால் சிறைவாசம்; 'ஏன்' என்றால் வனவாசம்!

[வேகமாகப் போகிறான்.]

## கண்ணகி மாளிகை

(வேதாளம் சுகதேவ்)

சுகதேவ் : வேதாளம்! நீர் சொன்னபடி எல்லா ஏற்பாடுகளையும் செய்து முடித்து விட்டேன். இரண்டாயிரம் பொன் செலவழித்து...ஆபரணம்...ஆடை அது...இது....எல்லாம் வாங்கி விட்டேன்...என் முத்தாயி வந்து விடுவாளா?...வேதாளம்...என் கண்ணுடிக்காக இந்த கண்ணகி மாளிகை காத்துக் கிடக்கிறதே...வருவாளா அந்த ஆணங்கு?...
'''

page67 = r'''
வேதாளம் : (விலக்கிக் காட்டி) நிச்சயமாக தம்பி!...இரண்டிலே ஒன்று தொடங்கு! (தொடுகிறான்)

வேதா : ஆ!...கட்டாயம் வருவாள் தம்பி...

சுக : வருவாளா?...

வேதா : சரி!...ஒரு பூ சொல்லுங்க தம்பி!...

சுக : பூ!...இதுதானு? புளியம்பூ...

வேதா : ஏன் இந்த வம்பு!...நானே போய் முத்தாயியை அழைத்துக் கொண்டு வருகிறேன்...நீங்கள் இங்கேயே இருங்கள்...இப்போதே வருகிறேன்.

## வேங்கையூர் பாசறைச் சிறை

[முத்தன் சிறையில் இருக்கிறான்...அவனது தோழர்கள் பதுங்கிப் பதுங்கி வந்து அவனை விடுவிக்கிறார்கள்...அவன் அவர்கள் காதில் ரகசியம் கூறி செல்கிறான் முத்தன் விடுவிப்பதை மறைந்து இருந்து கவனித்த வேங்கையூர் வீரர்கள்...பாய்ந்து வந்து அவனை பிடித்து விடுகின்றனர். உடனே வேலழகனிடம் இழுத்துக் கொண்டு போகிறார்கள்]

## தனபதி மாளிகை

வேலழகன் : என்ன?...

குறும்பன் : வேதாளம் வந்திருக்கிறான்...

வேல : வேதாளமா?...வாச் சொல் வாச் சொல்...

வேல : வாரும் வேதாளம்...வெற்றியோடுதான் வந்திருப்பீர் என எண்ணுகிறேன்...

வேதா : வெற்றியின் ஆரம்பந்தான் பிரபு!—நமது புது புதிய வேடனிடம் சிக்கி இருக்கிறது!

வேல : என்ன?...என்ன?...

வேதா : சொல்கிறேன்...சுகதேவனுக்கும் முத்தாயிக்கும்—ஆனந்தபுரம் கண்ணகி மாளிகையிலே திருமணம்...

வேல : ஆ!...
'''

page68 = r'''
வேதா : நான்தான் ஏற்பாடு செய்தேன்...

வேல : (கோபமாக) என்ன?...

வேதா : வாருங்கள்......முத்தாயியை உங்களிடம் சேர்ப்பதற்காகவே இந்த சூழ்ச்சியை ஆரம்பித்திருக்கிறேன்...

வேல : புரியும்படி சொல்லும்...

வேதா : நான் சொல்கிறபடி நீங்கள் செய்ய வேண்டும்...சுகதேவனுக்கும் முத்தாயிக்கும் திருமணம் நடக்கப் போகிறது...தாங்கள் முத்தனை உடனே அங்கு அனுப்ப வேண்டும்...முத்தன் போனால் முத்தாயி அவனுடன் ஓடி வருவாள்...இருவரும் தப்பி வரும்போது நாம் முத்தனை துரத்தி விட்டு முத்தாயியை மட்டும் அபகரித்துவிட வேண்டும்...

வேல : நல்ல யோசனை...முத்தன் நம் சூழ்ச்சியைப் புரிந்து கொண்டால்?...

வேதா : உம்...காதல் மயக்கத்தில் எதையும் யோசிக்க மாட்டான்...ஒருவன் குதிரை வீரன் (வருகிறான்.)

வீரன் : பிரபு! முத்தன் சிறையிலிருந்து தப்பியோடினான்...பிடித்து வந்திருக்கிறோம்...

வேல : எங்கே?...கொண்டு வாருங்கள்...வேதாளம்; நீர் சற்று மறைந்திரும்...

[முத்தன் இழுத்துவரப்படுகிறான்.]

வேல : சரி! நீங்கள் போகலாம்...ஹி...ஹி...ஹி...முத்தா!...நீ சிறையிலிருந்து தப்பி ஓடாவிட்டாலும் நானே உன்னை விடுவித்து அனுப்புவதாக யோசித்துக் கொண்டிருந்தேன்...நல்ல வாலிபனே!...உன்னை நான் மிகவும் கஷ்டப்படுத்திவிட்டேன்...வருந்துகிறேன், அதற்காக....

முத் : அய்யா! திடமென்று மாறிவிட்டீர்களே...நான் திக்கற்றவன் என்பதை எப்படி உணர்ந்தீர்கள்?......தெய்வமும் வந்து சொல்லி இருக்க முடியாதே!

வேல : மனிதனுக்கு மனச்சாட்சி என்று ஒன்று இருக்கிறது. மனிதன் மிருகமாக மாறும் போது அந்த
'''

page69 = r'''
மனச்சாட்சி புழுவாக மாறி அடங்கிக் கிடக்கும். மிருகத் தன்மை தோல்வி அடையும் நேரத்தில் புழுவாகிப்போன மனச்சாட்சி புள்ளி மயிலாக எழுந்து நடனமாடும்...அந்த ஆட்டத்திலேதான் உண்மையின் அழகு ஒளிவிட ஆரம்பிக்கிறது.

முத் : ஆகா! சிறப்பான கருத்து இந்த இடத்திலேயும் முளைக்கிறது, சேற்றிலே செந்தாமரை முளைப்பதைப் போல...

வேல : முத்தா! என் கண்ணைத் திறந்துவிட்ட செய்தி எது தெரியுமா?...உன் அன்புக் காதலி முத்தாயியை அந்த சுகதேவன் பலவந்தமாக மணம் புரியப் போகிறான்...

முத் : உண்மையாகவா?...

வேல : ஆமாம்! ஆனந்தபுரம் கண்ணகி மாளிகையிலே திருமணம்...அவள் ஆவி பிரிவதற்கு முன்னாள் நீ ஓடு...முத்தா! எனக்கேனு இப்போது இவ்வளவு அக்கறை என்று கருதுவாய்...லைலாமஜ்னு கதை படித்திருப்பாயே நீ...லைலாவின் கணவன் அவளின் அவன் காதலன் கயசிடம் திருப்பி அனுப்பிய நிகழ்ச்சிக்கும் இதற்கும் அதிக வேறுபாடில்லை...முத்தா! ஒன்று சொல்கிறேன்...நீயும் முத்தாயியும் என் பாதுகாப்பிலேயே குடும்பம் நடத்தலாம்...அதற்கென்ன இப்போது, அவசரம்!......உடனே போ...உன் உயிரிணையாளைக் காப்பாற்று...[உள்ளேபோய் சிறந்த ஆடைகள் எடுத்து வந்து] இஞ்ஞுனே! இப்போதே ஓடு...இழந்த காதலைப் பெற்றிடு...இந்தா அழகான உடைகள். அணிந்து கொள்...ஆனந்தமாக திருமணத்தை முடித்துக் கொண்டுவா!...

முத் : மிகவும் நன்றி உடையவனய்யா நான்...

[வேகமாகப் போகிறான். அதற்குள் சிரிப்பொலி கேட்கிறது. மறைந்து கவனிக்கிறான்.]

வேதாளம் : சபாஷ் பிரபுவே! மிகவும் நன்றாக நடித்துவிட்டார்கள்.
'''

page70 = r'''
வேல : சரியானபடி ஏமாந்து விட்டான் பயல்...

வேதாளம்!...அடுத்த ஏற்பாடு என்ன?...

வேதா : அடுத்த ஏற்பாடு!...ஐந்தாறு குதிரை வீரர்களே அடியேனுடைய தலைமையில் அனுப்புங்கள். அந்த அழகியுடன் வந்து சேருகிறேன்.

வேல : ஆயிரம் பொன் தருவேன்...அவளுடன் வந்தால்...

முத்தன் : [தனியாக] சதி செய்கிறார்கள்....அந்தச் சதியை எனக்குச் சாதகமாக்கிக் கொள்கிறேன்.

## பாசறை சமையல் கூடம்

முத்தன் : தோழர்களே! முத்தாயியை அபகரிப்பதற்காக என்னை கருவியாக உபயோகிக்கிறான் தனபதி. நான் இந்த சந்தர்ப்பத்தை பயன்படுத்திக் கொண்டு மறைந்து விடுகிறேன்.

வீரன் : அப்படியானால் நாங்கள் என்ன ஆவது அண்ணே?

முத் : நீங்களும் எப்படியாவது இங்கிருந்து தப்பி என்னிடம் வந்து விடுங்கள். பிறகு எல்லோரும் சேர்ந்து பழுதார் விடுதலைக்கு பாடுபடுவோம். வாட்டமா நான்?

வீரன் : ஜாக்கிரதையாகப் போங்கள் அண்ணே! நாங்கள் எப்படியும் வந்து சேருகிறோம்.—தந்திரமாக வெளியேற வேண்டும்.

## கண்ணகி மாளிகை

முத்தாயி : என்னப்பா யாருமே காணவில்ல? எங்கேயப்பா அவர்?...

திரிசங்கு : அடடடா! அதற்குள் அவசரமா? இலை போட்ட பிறகு சோறு போடாமலா இருந்து விடுவார்கள்? வாம்மா வா......

முத் : ஆமாம் ...திருமணத்திற்கான ஏற்பாடுகள் எல்லாம்...
'''

page71 = r'''
திரி : மேளதாள மில்லையே; பந்தல் இல்லையே; பந்தி இல்லையே; என்று பார்க்கிறாயா?...இது பெண் வீடுதான். முகூர்த்தம் நடைபெறுகிற இடம் வேறிடம். அதுவுமில்லாமல்...இந்தத் திருமணம் சுகதேவுக்குத் தெரியாமல் நடைபெற வேண்டுமே...

முத் : ஆமாம்....ஆமாம்...அந்த சுகதேவ...

[சுகதேவ் வருவதைக் கண்ட திரிசங்கு]

மிகவும் அழகானவர்—உனக்குப் பிடித்தமானவர் என்று கூறுகிறாய்......

முத் : அப்பா...என்ன உளறுகிறீர்கள்...!

[திரும்புகிறாள். சுகதேவை கண்டுவிடுகிறாள். மயங்கி விழுகிறாள்.]

சுக : என்ன?...என்ன?...

திரி : ஒன்றுமில்ல ...ஒன்றுமில்ல ...உங்களைப் பார்த்த அதிர்ச்சியில் மயக்கம் வந்துவிட்டது...சந்தோஷத்தால் இருதயம் படபடக்குமல்லவா...தம்பி...?

சுக : ஆமாம்!...ஆமாம்! எனக்குக்கூட இப்போது அப்படித்தான் அடித்துக்கொள்கிறது...

திரி : சரி; நீங்கள் மேலே போங்கள். நான் பிறகு வருகிறேன்.

[சுகதேவ் போகிறான். முத்தாயி மயக்கம் தெளிந்து எழுகிறாள். திரிசங்கு விலையுயர்ந்த நகைகளையும் உடைகளையும் எடுத்துக் காட்டுகிறான்.]

திரி : முத்தாயி! இவைகளேப் பார்...முத்தும், பவளமும், ரத்தினமும், வைரமும் பதித்திட்ட ஆபரணங்கள்! பளபளக்கும் பட்டாடை!...ஜொலிக்கும் வைரம்! மதிப்பு வாய்ந்த ரத்தினம்! ஆஹா...ஹா...இவைகள் எல்லாம்....

முத் : உங்கள் மனத்திற்கு தாப்படும் விலை! உங்கள் மகள் மீது வீசப்படும் வலை!...

திரி : சொல்வதைக் கேள்...

திரி : எதுவும் சொல்லவேண்டாம். எல்லாம் விளங்கி விட்டது. சிப்பியே முத்தைக் கொண்டு வந்து சேற்றில்
'''

page72 = r'''
போடுகிறது!...செந்தாமரைக் கொடியே இதழ்களின் உதிர்த்து எருமைக்குத் தருகிறது! அப்பா உங்கள் மகளிடமா இப்படி சூழ்ச்சி செய்வது!...

திரி : மகள்!...மகளா இருந்தால் ஒரு தகப்பனுடைய மனதை இப்படி எரியவிடுவாளா? நீ மகளா இருந்தால்—ஒரு வயதான தகப்பன்—வாஞ்சையுள்ள தகப்பன்—வறுமையிலே பலநாள் கஷ்டப்பட்டவன்—இப்போது வாழ்ந்து பார்க்கலாம் என நினைக்கிறேனே, அதற்கு துணைபுரிவோமென்று எண்ணமாட்டாயா?...நான் வாழ்வதற்காக உன்னையென்ன தீயிலா குதிக்கச் சொல்கிறேன்? பெரிய தியாகமா பண்ணச் சொல்கிறேன்?....தேடக் கிடக்காத இடம்...அந்த இடத்து தெய்வமாக வைத்துப் போற்றுகிறேன் என்கிறான்...நீ தேம்புகிறாய்; விம்முகிறாய்; புலம்புகிறாய்; புத்தியற்றவளே! எத்தனையோ ஆசைகள் உனக்கு நான் நிறைவேற்றித் தந்திருக்கிறேன், நீ எனது முதலும் கடைசியுமான இந்த ஆசையை பூர்த்தி செய்யக் கூடாதா?....

முத் : பல முறை உனக்கு நான் இளநீர் வழங்கி இருக்கிறேன்; ஒரு முறை உன் தலையில் விழுகிறேன் என்று தென்னைமரம் சொல்வதற்கும், நீங்கள் சொல்வதற்கும் என்னப்பா வித்தியாசம்?...

திரி : சீ, அதிகப்பிரசங்கி! அடங்கிக்கிட! காலையிலே உனக்கும் இளவரசருக்கும் திருமணம்!...தயாராகிக் கொள் அதற்கு...

[வேகமாகப் போகிறான். வெளியில் வரும்போது வேதாளத்தை காண்கிறான்.]

திரி : வாருங்கள்...நல்ல சமயத்தில் வந்தீர்கள்...

வேதா : என்ன திரிசங்கு? எப்படி எனது ஏற்பாடுகள் எல்லாம்......

திரி : ஏற்பாடுகள் எல்லாம் சரி! ஒரே ஒரு குறை தான்

வேதா : என்ன அது?

திரி : சுகதேவை மணந்திட முத்தாயி மறுக்கிறாள்...
'''

page73 = r'''
வேதா : சரிதான் போ! சாப்பாடு தயார்; சோறு தான் இல்ல என்பது போல் இருக்கிறதே! என்னப்பா...இருவருமே ஒன்றுபட்ட காதலர்கள் என்றீர்களே முன்பு...

திரி : முத்தாயி ஒரு முட்டுப்பெண். அவள் பிடிவாதத்தை என்னால் மாற்ற முடியவில்லை...நீங்கள் தான் எப்படியாவது...

வேதா : உம்...முயற்சிக்கிறேன்...இப்போது அவள் எங்கே இருக்கிறாள்?

திரி : உள்ளேதான் இருக்கிறாள்.

வேதா : சரி நீங்கள் யாரும் வாருங்கள்; நான் அவளோடு சரி செய்கிறேன்!...

[வேதாளம் உள்ளே போகிறான். முத்தாயியைப் பார்த்து]

வேதா : முட்டாள் பெண்ணே! எழுந்திரு! ஏன் இப்படி உட்கார்ந்திருக்கிறாய்?...பேசமாட்டாயா?...ம்...தகப்பன் இது தான் நேரம் போவிருக்கிறது...கடல் குமுறிக் கொண்டிருக்கிறது...நீ என்னமோ கட்டுமரத்தில் இருந்து ஒப்பாரி பாடிக்கொண்டிருக்கிறாய்!...ஆ! வேண்டியதைப் பார், அன்புள்ள சிறுமியே! அழுவதால் ஆபத்தை தடுத்து விட முடியாது......ஏன் அழுகிறாய்?

முத் : ஊர் சிரிக்கிறது; நான் அழுகிறேன்...

வேதா : உண்மை தான். ஆனாலும் கொழுந்து மனம் படைத்த கோதையே! கொந்தளிப்பிலிருந்து மீள்வதற்கு இன்னும் வாய்ப்பு இருக்கிற தென்பதை உணருவாய்...

முத் : மீள்வதற்கு வாய்ப்பா!...

வேதா : ஆமாம்...வாய்ப்புத்தான்...உன் விடுதலை தான்...வேதனை விலகுகிறது என்ற அறிகுறிதான், வேதாளத்தின் வடிவத்திலே வந்திருக்கிறது...

முத் : என்ன சொல்கிறீர்கள்?....

வேதா : முத்தனும் நானும் எவ்வளவு நேசமுடன் பழகினோம் என்பது உனக்குத் தெரியாது...நீ கொடுத்த பொண்ணு சுமதி வாயில் போட்டுக் கொண்டு விட்டாள்...முத்தன் பாசறைச் சிறையில் அடைக்கப்பட்டு விட்டான்...நான் வெகு நாளாக அரும்பாடுபட்டு சேமித்து வைத்
'''

page74 = r'''
திருந்த திரவியத்தை கொடுத்து இப்போது அவனை மீட்டு விட்டேன்.

முத் : ஆ!...என் முத்தன் விடுதலை யடைந்து விட்டாரா?

வேதா : அய்யோ! பரிதாபத்துக்குரிய பாவையே!...இன்னும்கேள் இன்பச் சேதியை. உன் தகப்பன் கொடியவன்; உன்னை ஏமாற்றி இந்தத் திருமணத்தை ஏற்பாடு செய்தான் என்பது எனக்குத் தெரிந்து...உடனே ஓடிவந்தேன், உன்னைக் காப்பாற்ற!...கலியாண விருந்தினன்போல் வந்து என் நண்பனின் காதலியை விடுவிக்க நான் முயலுகிறேன்.

முத் : அய்யா! நீங்கள் பல்லாண்டு வாழ்க!

வேதா : இந்த அக்கிரம உலகத்தில் என்னம்மா ஆயுள் நீடிக்க வேண்டும்? அது கிடக்கட்டும்...இதைக் கேள், இளஞ் சிட்டே!...இன்றிரவே முத்தன் இங்கு வருவான்; நீ அவனுடன் புறப்பட்டு வந்துவிடு.

முத் : அவர் வருவாரா?...

வேதா : வராமல் இருப்பானு?...ஜாக்கிரதை, நீங்கள் இருவரும்!

[வேதாளம் போகிறான். அறைக்குள்ளே கிழவன் வேஷத்தில் முத்தன் நுழைகிறான்]

முத்தாயி : அத்தான்! நீங்கள் வருவீர்கள் என்று வேதாளம் சொன்னார்.

முத் : வேதாளம்! விஷப்பாம்பு அவன்! முத்தாயி, எப்படியாவது சுகதேவனை நீ இங்கே வரும்படி செய்ய வேண்டும்.

முத் : சுகதேவனா? ஏன்?

முத் : ஏன் தெரியுமா? நாம் இப்போது வெளியேறுவது என்பதென்றால் சாதாரணமல்ல, நம்மைச்சுற்றி ஆபத்து காத்திருக்கிறது!
'''

text = FULL.read_text(encoding='utf-8')
for p, status, body in [
    (65, 'review', page65),
    (66, 'verified', page66),
    (67, 'verified', page67),
    (68, 'verified', page68),
    (69, 'verified', page69),
    (70, 'verified', page70),
    (71, 'verified', page71),
    (72, 'verified', page72),
    (73, 'verified', page73),
    (74, 'verified', page74),
]:
    text = replace_page(text, p, status, body)
FULL.write_text(text, encoding='utf-8')

# Index is the machine-readable authority.
idx = json.loads(INDEX.read_text(encoding='utf-8'))
idx['draft_pages'] = 35
idx['verified_pages'] = 69
idx['review_pages'] = 1
idx['open_uncertainty_markers'] = 30
fa = idx['fidelity_audit']
fa['status'] = 'in-progress'
fa['canonical_range_audit_complete'] = False
fa['audited_pages'] = 70
fa['verified_pages'] = 69
fa['unresolved_source_readings'] = 30
fa['review_pages'] = 1
fa['verified_pdf_range'] = [5, 64]
fa['verified_logical_printed_range'] = [3, 62]
fa['additional_verified_pdf_ranges'] = [[66, 74]]
fa['additional_verified_logical_printed_ranges'] = [[64, 72]]
fa['review_pdf_pages'] = [65]
fa['review_logical_printed_pages'] = [63]
idx['next_pdf_page'] = 65
idx['next_printed_page'] = 63
idx['next_action'] = 'Reopen PDF 65 / logical printed p.63 and adjudicate the remaining long old-type poetic marker 49 from the rendered scan. PDF 5-64 and PDF 66-74 are verified; PDF 65 remains review. Do not continue to PDF 75 until marker 49 is source-clean; structured derivatives remain blocked until all 105 canonical pages are verified.'
INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Fidelity ledger: update current progress and append the batch disposition.
audit = AUDIT.read_text(encoding='utf-8')
old_table = '''| PDF 55–64 / logical pp.53–62 | 10 | 0 | 0 | verified |\n| PDF 65–109 / logical pp.63–107 | 0 | 0 | 45 | pending |\n| **Total** | **60** | **0** | **45** | **in progress** |'''
new_table = '''| PDF 55–64 / logical pp.53–62 | 10 | 0 | 0 | verified |\n| PDF 65 / logical p.63 | 0 | 1 | 0 | review — marker 49 unresolved |\n| PDF 66–74 / logical pp.64–72 | 9 | 0 | 0 | verified |\n| PDF 75–109 / logical pp.73–107 | 0 | 0 | 35 | pending |\n| **Total** | **69** | **1** | **35** | **in progress** |'''
if old_table not in audit:
    raise SystemExit('fidelity progress table target missing')
audit = audit.replace(old_table, new_table, 1)
audit = audit.replace(
    'Open first-pass uncertainty markers after this audit checkpoint: **68** (markers **1–48 resolved**; markers **49–116** remain unresolved).',
    'Open first-pass uncertainty markers after this audit checkpoint: **30** (markers **1–48 and 50–87 resolved**; marker **49** plus markers **88–116** remain unresolved).',
    1,
)
section = r'''

## PDF 65–74 / logical pp.63–72 — 9 verified + 1 review

All ten pages were compared directly against the rendered controlling scan. PDF 65 remains `review` because marker 49 is the long old-type poetic continuation and is still not secure enough for a source-faithful transcription. The other two PDF 65 uncertainties and every uncertainty on PDF 66–74 were resolved from the printed pages.

- **marker 49 — PDF 65:** remains unresolved; no external literary witness, OCR, film dialogue or semantic reconstruction may fill it.
- **markers 50–51 — PDF 65:** resolved as the warriors' printed `தச்...தச்...தச்...` response and Muthan's question ending `அவைகளை மாற்றானின் காலடியில் மிதிக்க விடலாமா?`.
- **markers 52–87 — PDF 66–74:** resolved by full-page direct scan transcription. The canonical page blocks were rebuilt from the rendered pages rather than from the first-pass summaries.

Important boundary corrections:

- PDF 73→74 preserves the source split `வைத்` + `திருந்த`.
- The first-pass note that marker 87 continues from PDF 74 into PDF 75 was incorrect. PDF 74 closes with `ஆபத்து காத்திருக்கிறது!`; PDF 75 begins a new bracketed action and is a fresh source unit.

No unresolved scan reading remains on PDF 66–74. PDF 65 remains the only review page in this audited range.
'''
if '## PDF 65–74 / logical pp.63–72 — 9 verified + 1 review' not in audit:
    # Insert before exact next activity if present; otherwise append.
    marker = '\n## Exact next activity\n'
    if marker in audit:
        audit = audit.replace(marker, section + marker, 1)
    else:
        audit += section
# Rewrite next activity text generically.
audit = re.sub(
    r'## Exact next activity\n.*?$',
    '## Exact next activity\n\nReopen **PDF 65 / logical printed p.63** and adjudicate **marker 49** from the rendered scan. PDF 5–64 and PDF 66–74 are verified; PDF 65 remains review. Do **not** continue to PDF 75 or begin structured derivatives until PDF 65 is source-clean.',
    audit,
    flags=re.S,
)
AUDIT.write_text(audit, encoding='utf-8')

notes = NOTES.read_text(encoding='utf-8')
if '## Fidelity disposition — PDF 65–74' not in notes:
    notes += r'''

## Fidelity disposition — PDF 65–74

A later rendered-scan fidelity pass supersedes the first-pass uncertainty disposition without rewriting this historical ledger.

- marker **49** remains unresolved on PDF 65 and keeps that page in `review`;
- markers **50–87** are resolved directly from the rendered scan;
- PDF **66–74** are verified after full-page transcription against the scan;
- the old marker-87 note claiming a PDF 74→75 continuation is superseded: PDF 74 closes locally with `ஆபத்து காத்திருக்கிறது!`, and PDF 75 begins a new bracketed action;
- the PDF 73→74 split `வைத்` + `திருந்த` is source-visible and retained.
'''
NOTES.write_text(notes, encoding='utf-8')

# Work-local prose mirrors: targeted replacements from the durable 60/105 checkpoint.
def sub_file(path, replacements, regexes=()):
    s = path.read_text(encoding='utf-8')
    for old, new in replacements:
        if old not in s:
            raise SystemExit(f'{path}: missing target {old!r}')
        s = s.replace(old, new)
    for pat, repl in regexes:
        s, n = re.subn(pat, repl, s, flags=re.S)
        if n == 0:
            raise SystemExit(f'{path}: regex target missing {pat!r}')
    path.write_text(s, encoding='utf-8')

sub_file(TREADME, [
    ('- verified pages: **60**;', '- verified pages: **69**;'),
    ('- review pages: **0**;', '- review pages: **1**;'),
    ('- open first-pass uncertain readings: **68**;', '- open first-pass uncertain readings: **30**;'),
    ('- full rendered-scan visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified (60/105)**.', '- full rendered-scan visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified (69/105); PDF 65 / logical p.63 review**.'),
], regexes=[
    (r'## Exact next activity\n.*?$', '## Exact next activity\n\nReopen **PDF 65 / logical printed p.63** and adjudicate marker **49** from the rendered scan. PDF 5–64 and PDF 66–74 are verified; PDF 65 remains review. Do not continue to PDF 75 while marker 49 remains unresolved; structured derivatives stay blocked until all 105 pages are verified.'),
])

sub_file(WREADME, [
    ('- verified pages: **60**;', '- verified pages: **69**;'),
    ('- open first-pass uncertainty markers: **68**;', '- open first-pass uncertainty markers: **30**;'),
    ('- visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified (60/105)**.', '- visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified (69/105); PDF 65 / logical p.63 review**.'),
    ('| Visual fidelity audit | **in-progress — 60/105 verified** |', '| Visual fidelity audit | **in-progress — 69/105 verified + PDF 65 review** |'),
    ('| Verified Tamil pages | **60/105; 0 review** |', '| Verified Tamil pages | **69/105; 1 review** |'),
], regexes=[
    (r'## Exact next activity\n.*?$', '## Exact next activity\n\n**Reopen PDF 65 / logical printed p.63 and adjudicate marker 49 from the rendered scan.** PDF 5–64 and PDF 66–74 are verified; PDF 65 remains review. Do not continue to PDF 75 or start structured derivatives until PDF 65 is source-clean and ultimately all 105 canonical pages are verified.'),
])

# YAML-like metadata: line-level current values are unique inside this work file.
meta = META.read_text(encoding='utf-8')
repls = {
    '  verified_pages: 60\n': '  verified_pages: 69\n',
    '  draft_pages: 45\n': '  draft_pages: 35\n',
    '  review_pages: 0\n': '  review_pages: 1\n',
    '  open_first_pass_uncertainty_markers: 68\n': '  open_first_pass_uncertainty_markers: 30\n',
    '  next_action: "Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63; 60/105 pages are verified and 68 explicit first-pass readings remain unresolved."\n': '  next_action: "Reopen PDF 65 / logical printed p.63 and adjudicate marker 49 from the rendered scan; PDF 5-64 and PDF 66-74 are verified, PDF 65 is review, and structured derivatives remain blocked until all 105 pages are verified."\n',
    '  audited_pages: 60\n': '  audited_pages: 70\n',
    '  unresolved_source_readings: 68\n': '  unresolved_source_readings: 30\n',
    '  verified_pdf_pages: "5-64"\n': '  verified_pdf_pages: "5-64,66-74"\n',
    '  verified_logical_printed_pages: "3-62"\n': '  verified_logical_printed_pages: "3-62,64-72"\n',
    '  visual_fidelity_audit: in-progress-60-of-105\n': '  visual_fidelity_audit: in-progress-69-of-105-plus-1-review\n',
    'next_action: "Continue the rendered-scan visual fidelity audit at PDF 65 / logical printed p.63; resolve the remaining 68 explicit first-pass readings before structured derivatives."\n': 'next_action: "Reopen PDF 65 / logical printed p.63 and adjudicate marker 49 from the rendered scan; do not continue to PDF 75 until PDF 65 is verified."\n',
}
for old, new in repls.items():
    if old not in meta:
        raise SystemExit(f'metadata missing target {old!r}')
    meta = meta.replace(old, new, 1)
# fidelity block has its own verified/review counts; replace the next remaining occurrences.
meta = meta.replace('  verified_pages: 60\n', '  verified_pages: 69\n', 1)
meta = meta.replace('  review_pages: 0\n', '  review_pages: 1\n', 1)
insert_after = '  verified_logical_printed_pages: "3-62,64-72"\n'
if '  review_pdf_pages: "65"\n' not in meta:
    meta = meta.replace(insert_after, insert_after + '  review_pdf_pages: "65"\n  review_logical_printed_pages: "63"\n', 1)
META.write_text(meta, encoding='utf-8')

sub_file(HANDOVER, [
    ('- state: **draft-complete**, verified pages **60**, review pages **0**;', '- state: **draft-complete**, verified pages **69**, review pages **1**;'),
    ('- open uncertainty markers: **68**;', '- open uncertainty markers: **30**;'),
    ('- visual fidelity audit: **in-progress — PDF 5–64 / logical pp.3–62 verified (60/105)**.', '- visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified (69/105); PDF 65 / logical p.63 review**.'),
    ('- visual fidelity audit: **in-progress — 60/105 verified**;', '- visual fidelity audit: **in-progress — 69/105 verified + PDF 65 review**;'),
], regexes=[
    (r'## Exact next activity\n.*?$', '## Exact next activity\n\n> **Reopen PDF 65 / logical printed p.63 and adjudicate marker 49 from the rendered scan. PDF 5–64 and PDF 66–74 are verified; PDF 65 remains review. Do not continue to PDF 75 or start scene/dialogue/character derivatives until PDF 65 is source-clean and ultimately all 105 canonical pages pass.**'),
])

# Machine registry: update the Ammayappan object robustly.
data = json.loads(WORKS.read_text(encoding='utf-8'))
obj = next(x for x in data if x.get('id') == 'ammaiyappan')
obj['canonical_tamil_draft_pages'] = 35
obj['canonical_tamil_verified_pages'] = 69
obj['canonical_tamil_review_pages'] = 1
obj['canonical_tamil_open_uncertainty_markers'] = 30
obj['tamil_fidelity_audit'] = 'in-progress-69-of-105-plus-1-review'
obj['next_action'] = 'Reopen PDF 65 / logical printed p.63 and adjudicate marker 49 from the rendered scan. PDF 5-64 and PDF 66-74 are verified; PDF 65 is review. Do not continue to PDF 75 until it is verified.'
obj['tamil_transcription_draft_pages'] = 35
obj['tamil_transcription_verified_pages'] = 69
obj['tamil_transcription_review_pages'] = 1
obj['canonical_range_fidelity_audit_complete'] = False
obj['total_verified_pages'] = 69
obj['total_review_pages'] = 1
obj['open_first_pass_uncertainty_markers'] = 30
obj['fidelity_audit_verified_pdf_pages'] = '5-64,66-74'
obj['fidelity_audit_verified_logical_printed_pages'] = '3-62,64-72'
obj['fidelity_audit_review_pdf_pages'] = '65'
obj['fidelity_audit_review_logical_printed_pages'] = '63'
obj['fidelity_audit_next_pdf_page'] = 65
WORKS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Root README: replace only the Ammayappan status section.
root = ROOTREADME.read_text(encoding='utf-8')
root_section = r'''## அம்மையப்பன் status

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
- visual fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified; PDF 65 review**;
- verified / draft / review pages: **69 / 35 / 1**;
- open first-pass uncertainty markers: **30**;
- structured derivatives / English / reader: **blocked pending complete verified Tamil**.

**Next:** reopen **PDF 65 / logical printed p.63** and adjudicate marker **49** from the scan. Do not continue to PDF 75 while PDF 65 remains review. Do not start scene/dialogue/character derivatives until all 105 canonical pages are verified.
'''
pat = re.compile(r'## அம்மையப்பன் status\n.*?(?=\n## கலைஞர் திரை இசைப் பாடல்கள் status)', re.S)
root, n = pat.subn(root_section.rstrip(), root)
if n != 1:
    raise SystemExit(f'root README Ammayappan section replacements={n}')
ROOTREADME.write_text(root, encoding='utf-8')

# Master handover: high-level line/sync paragraph + active Section 16.
master = MASTER.read_text(encoding='utf-8')
master = re.sub(
    r'- \*\*Ammayappan\*\* — 111-page image-only screenplay/dialogue source;.*?structured derivatives remain blocked\.',
    '- **Ammayappan** — 111-page image-only screenplay/dialogue source; first pass **105/105** assembled with QA PASS; rendered-scan fidelity audit has **PDF 5–64 and PDF 66–74 verified (69/105), PDF 65 / logical p.63 in review, 35 draft pages, and 30 unresolved first-pass readings**; structured derivatives remain blocked.',
    master,
    count=1,
)
master = re.sub(
    r'`data/works\.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT\.md` are synchronized to the active \*\*Ammayappan fidelity checkpoint:.*?\*\*\. The next gate is .*?\.',
    '`data/works.json`, root README, work metadata/README/transcription index/handover, this master handover and `docs/STATUS_CONSISTENCY_AUDIT.md` are synchronized to the active **Ammayappan fidelity checkpoint: first pass 105/105 assembled, PDF 5–64 and PDF 66–74 verified (69/105), PDF 65 / logical p.63 review, 35 draft pages, and 30 unresolved first-pass readings**. The next gate is PDF 65 / logical p.63 / marker 49.',
    master,
    count=1,
    flags=re.S,
)
section16 = r'''## 16. Ammayappan active checkpoint

Work path: `works/ammaiyappan/`  
Source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`

- source intake / whole-scan map: **complete**;
- canonical first pass: **105/105 draft-complete**, continuous `full-text.md` through PDF 109;
- assembly QA: **PASS — 105 anchors / 0 missing / 0 duplicate**;
- fidelity audit verified ranges: **PDF 5–64 / logical pp.3–62 and PDF 66–74 / logical pp.64–72 — 69/105 verified**;
- review: **PDF 65 / logical p.63 — marker 49 unresolved**;
- remaining draft pages: **35 — PDF 75–109**;
- open first-pass uncertainty markers: **30**;
- PDF 73→74 source split `வைத்` + `திருந்த` is preserved; PDF 74 closes locally and does not continue into PDF 75;
- locked source headings remain `பழுதார் வீதி` (PDF 56) and `தூக்குமேடை` (PDF 107; reject `தாக்குமேடை`);
- structured derivatives / English / reader: **blocked pending 105/105 verified Tamil**.

Exact next activity: **reopen PDF 65 / logical p.63 and adjudicate marker 49 from the rendered scan. Do not continue to PDF 75 until PDF 65 is source-clean.**
'''
master, n = re.subn(r'## 16\. Ammayappan active checkpoint\n.*?$', section16.rstrip(), master, flags=re.S)
if n != 1:
    raise SystemExit(f'master Section 16 replacements={n}')
MASTER.write_text(master, encoding='utf-8')

# Status consistency audit: result, matrix row, Ammayappan detail section.
status = STATUS.read_text(encoding='utf-8')
status = re.sub(
    r'\*\*PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint:.*?\*\*',
    '**PASS — current status mirrors synchronized across all seven works at the Ammayappan visual-fidelity checkpoint: first pass 105/105 assembled through PDF 109, PDF 5–64 and PDF 66–74 visually verified (69/105), PDF 65 review, 35 draft pages, 1 review page, and 30 open first-pass readings; next gate PDF 65 / logical p.63 / marker 49.**',
    status,
    count=1,
)
status = re.sub(
    r'\| Ammayappan \| source intake 111/111;.*?\| blocked \| blocked \| blocked \|',
    '| Ammayappan | source intake 111/111; structural map verified; Tamil first pass **105/105 draft-complete; PDF 5–64 and 66–74 fidelity-verified (69/105); PDF 65 review; 35 draft; 30 open markers** | scene/dialogue/character blocked pending complete verified Tamil | blocked | blocked |',
    status,
    count=1,
)
checkpoint = r'''## Ammayappan canonical-Tamil first-pass closure checkpoint

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
- rendered-scan fidelity audit: **in-progress — PDF 5–64 and PDF 66–74 verified; PDF 65 / logical p.63 review**;
- verified / draft / review pages: **69 / 35 / 1**;
- open first-pass uncertainty markers: **30**;
- scene / dialogue / character derivatives: **blocked pending complete verified Tamil**;
- song/performance authorship gate: **not-started**;
- English translation / reader / Reading Room integration: **blocked**.

The canonical Tamil first-pass transcription and assembly gate remains closed. The separate source-fidelity gate is active. Exact next activity: **reopen PDF 65 / logical printed p.63 and adjudicate marker 49 from the rendered scan**. Do not continue to PDF 75 while PDF 65 remains review. Structured derivatives remain blocked until all 105 pages pass.
'''
status, n = re.subn(r'## Ammayappan canonical-Tamil first-pass closure checkpoint\n.*?(?=\n## Manthiri Kumari reconciliation checkpoint)', checkpoint.rstrip(), status, flags=re.S)
if n != 1:
    raise SystemExit(f'status Ammayappan section replacements={n}')
STATUS.write_text(status, encoding='utf-8')

# Final invariants.
full = FULL.read_text(encoding='utf-8')
for p in range(66, 75):
    anchor = f'<!-- source: pdf={p} printed={p-2} status=verified -->'
    if full.count(anchor) != 1:
        raise SystemExit(f'verified anchor invariant failed PDF {p}')
if full.count('<!-- source: pdf=65 printed=63 status=review -->') != 1:
    raise SystemExit('PDF 65 review anchor invariant failed')
if full.count('⟦') != 30 or full.count('⟧') != 30:
    raise SystemExit(f'expected 30 visible uncertainty spans, found {full.count("⟦")}/{full.count("⟧")}')
if 'வைத்\n\n<!-- source: pdf=74 printed=72 status=verified -->\n\nதிருந்த' not in full:
    raise SystemExit('PDF 73→74 வைத்/திருந்த boundary invariant failed')
if 'ஆபத்து காத்திருக்கிறது!' not in full:
    raise SystemExit('PDF 74 closing line missing')
print('PASS: Ammayappan PDF 65-74 fidelity reconciliation prepared — 69 verified / 1 review / 35 draft / 30 open')
