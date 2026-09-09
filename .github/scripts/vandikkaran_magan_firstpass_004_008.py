#!/usr/bin/env python3
"""Create and synchronize Vandikkaran Magan canonical first-pass batch PDF 4-8."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
W = ROOT / "works" / "vandikkaran-magan"
T = W / "transcription"
P = T / "pages"
N = W / "notes"

SOURCE_SHA = "03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253"
TOTAL_CANONICAL = 84  # PDF 4-87 inclusive
NEXT = (
    "Continue canonical Tamil first-pass transcription with PDF 9–13 (five source pages) in source order. "
    "Preserve exact source scene headings, speaker labels, punctuation, stage directions and page boundaries; keep every page draft during first pass; "
    "inspect the historical Tamil glyph families prospectively occurrence by occurrence from enlarged source pixels; record any uncertainty explicitly; and do not begin visual-fidelity verification or structured derivatives yet."
)

PAGES = {
4: """<!-- source: pdf=4 status=draft -->

# கலைஞரின் முன்னுரை

வணக்கம். வாழ்க தமிழ்!

எரிமலையாய்ச் சுடுதழலாய்
இயற்கைக் கூத்தாய்
எதிர்ப்புகளை நடுங்க வைக்கும் இடியொலியாய்
இன உணர்வுத் தீப்பந்தப் பேரொளியாய்
இழிவுகளைத் தீர்த்துக் கட்டும் கொடுவாளாய்
இறைவனுக்கே மறுப்புச் சொன்ன இங்கர்சாலாய்
எப்போதும் பேசுகின்ற ஏதன்சு நகர சாக்ரடீசாய்
‘ஏன்,? என்று கேட்டபடியே வைர நெஞ்ச வால்டேராய்
எம் தந்தை பெரியாரும் வாழ்ந்திட்டார்;
நம் சிந்தை அணு ஒவ்வொன்றும் நிறைந்திட்டார்.
அந்த எழுச்சி ஞாயிறுக்கு நூற்றாண்டு விழா!
எழுபதாம் ஆண்டு பிறந்தது எங்கள் அண்ணனுக்கு!

புயற்காற்று ஒரு பூந்தென்றலைப் பிள்ளையாய்ப்
பெறுவதுண்டோ?

அப்படிப் பிறந்த பிள்ளைதான் நம் அண்ணன் எனும்
மந்தமாருதம்!

சண்டமாருதங்களையும் தன் இன்முகத்தால் விரட்டுகின்ற
மந்தமாருதம்!
""",
5: """<!-- source: pdf=5 status=draft -->

பெரியாரின் வைக்கரமாய் - அறிவில்
வறியோரைச் கரையேற்றும் விசைப்படகாய்
எறியோரின் பிழை பொறுக்கும் செங்கதிராய்
வெறியோரைப் பணிய வைக்கும் வித்தகராய்—அண்ணா
நெறியோடு முறையோடு நமை வளர்த்தார்!

பொங்குகடல் நடையும், பூவையின் மென்னடையும் தன்
புதுத் தமிழ் நடையில் காட்டியவர்.
பொல்லாங்கு உரைப்போரை வாதத்தில் மாட்டியவர்.
பொடியெடுத்துப் போடும் நேரம்
புன்னகையால் எதிரிகளைப் பொடியாக்கி வாட்டியவர்.
பழுதிக் குணம் படைத்தோரை ஓட்டியவர்.
பொன்மகுடம் தமிழ்த்தாய்க்குச் சூட்டியவர்.

எழுதுகோல் வைத்திருந்தார் அண்ணா—அது
ஏமாந்த தமிழர்களின் தலையெழுத்தை மாற்றத்
தாளில் உழுத கோல்!

அந்த எழுதுகோல் படைத்ததுதான்
‘சாஞ்சி’ இதழில் நாம் கண்ட கைவண்ணம்!
சிறுகதையாய்ச் சித்தரித்தார் வண்டிக்காரன் மகனை—
திரைக்கதைக்குத் தேவையான மாற்றங்கள் செய்து,
உரையாடல் தீட்டுகின்ற வாய்ப்பினையும் நான் பெறுகிறேன்.

கொள்கைகளைப் பரப்புவதே
என் கழப்பணியென
எல்லோரும் அறிந்திடுவீர்!
அப்பணிதான் அண்ணா வழித் திருப்பணியாம்.
திரைப்பணியால் திருந்த வேண்டும் நம் நாடு—

இல்லையேல்
குழிந்துவிடும் தீராத கேடு...

அந்த
எண்ணத்தை மனதில் வைத்து
எடுத்துள்ளார் இப்படத்தை... இனிய
இலட்சியத்தில் வெற்றி பெற இந்நாட்டுப் பெருமக்கள்!
தாய்மாரே! பெரியோரே! தங்கம் நிகர்
உடன்பிறப்புக்களே! தந்திடுவீர் ஆதரவை!

★
""",
6: """<!-- source: pdf=6 printed=5 status=draft -->

# வண்டிக்காரன் மகன்

## காட்சி—1

### ஜமீன்மாளிகை வெளிப்புறம்

(பொதுமக்கள் கூடியிருக்கிறார்கள்..... அவர்களுக்குள் “தொண தொண” என்று பேசுகிறார்கள்....

“சைலன்ஸ்” என்ற பேரொலியுடன் காலிங்கராயன் கதவைத் திறந்து கொண்டு வருதல்...)

மக்கள்:— ஏ, காலிங்கராயர் வந்துட்டாரு!.. ஜமீன்தாரய்யா வந்துடுவாரு!..

(அனைவரும் வாயிற்புறத்தையே பார்த்தல்—ஜமீன்தார் வருகிறார்.)

ஒருவன்:— ஜமீன்தார் ஜம்புலிங்க பூபதி!

மக்கள்:— வாழ்க!...

காலிங்:— என்னடா காட்டுக்கூட்டம்...வாழ்க...வாழ்க...வாள் வாழ்கன்னு!... அழகா... நல்லா நம்ப சாஸ்திரத்துக்கு சம்பிரதாயத்துக்கு எத்தப்படி... ஜமீன்தார் ஜம்புலிங்க பூபதிக்கு ஜே! ஜே!.. என்று கோஷம் போடுவீங்களா?..

ஒருவன்:— ஜமீன்தார் ஜம்புலிங்க பூபதிக்கு...

மக்கள்:— ஜே!

ஜமீன்தார்:— பெரியவர்களுக்கு நமஸ்காரம்!.. சிறியவர்களுக்கு ஆசீர்வாதம்!... காலிங்கராயா!...

காலிங்:— பிரபு!

ஜமீன்தார்:— இவர்களின் குறைகளைக் கேள்!..

காலிங்:— உத்தரவு பிரபு...
""",
7: """<!-- source: pdf=7 printed=6 status=draft -->

(ஒரு பெண் மனு ஒன்றை ஜமீன்தாரிடம் கொடுத்தல்—அவர் பரிவுடன் வாங்குதல் — அந்தப் பெண் ஜமீன்தாரின் காலில் விழுந்து கும்பிடுதல்..)

ஜமீன்தார்:— எழுந்திருங்கள்...எழுந்திருங்கள்...நீங்கள் எல்லாம் என் காலில் விழுந்து வணங்குகிறீர்களே; நான் என்ன மகானு? மஹரிஷியா? மகாத்மாவா?.. இல்லை! ஆனால் ஒன்று நீங்கள் விழுந்து வணங்குவது ஜமீன்தார் ஜம்புலிங்கத்தின் காலில் இல்லை!... தர்மத்தின் காலத்தொட்டுக் கும்பிடுகிறீர்கள்! நீதியின் காலை — நாணயத்தின் காலத்தொட்டுக் கும்பிடுகிறீர்கள்! என்ன காலிங்கராயா?...நான் சொல்வது சரிதானு?..

காலிங்:— வேற யார் சொல்ல முடியும் — நாமே சொல்லிக்க வேண்டியதுதான்!

ஜமீன்தார்:— (காலில் விழுந்த பெண்ணிடம்) உன் குறை என்னம்மா?

பெண்:— என் புருஷன் சதாநேரமும் சாராயத்தைக் குடிச்சிட்டு.. குடும்பத்தைக் குட்டிச் சுவராக்கிட்டாருங்க!..

ஜமீன்தார்:— ஐயகோ! ஐயகோ! தாய்க்குலம் கண்ணீர் வடிப்பதா? அதுவும் என் எதிரிலா? தாய்க்குலத்தின் கண்ணீரை என்னால் தாங்கிக் கொள்ளவே முடியவில்லை... காலிங்கா!... இந்தப் பெண்மணியின் கணவனைக் கூப்பிட்டு... கிரமமாக உத்தரவிடு!.. (பெண்ணை நோக்கி) கவலைப்படாதே அம்மா!.. உன் புருஷனைத் திருத்துவதுதான் பொறுப்பு — காலிங்கா! அதோடு இன்னொரு கட்டளை — உடனே அமுலாக வேண்டும். நமது ஜமீன் எல்லைக்குள் மதுவின் வாடையே அடிக்கக்கூடாது.

காலிங்:— நம்ம எல்லைக்குள்தானே!... அதை அமுல்படுத்திடலாம்.

புலவர்:— மாரி பொய்த்தாலும் பாரியின் கொடை பொய்க்காது!
தலையைக் கொடுக்கவும் தயாரான குமணன்!
தான்செய்த தர்மங்களையெல்லாம் கொடையாகக்
கொடுத்தான் கர்ணன்! பாரியாய் — குமணனுய் —
கர்ணனுய்க் காட்டியளிக்கும் வள்ளலே வாழ்க!...
வாழ்க!....

ஜமீன்தார்:— காலிங்கா!: அப்பா யாரு?...

புலவர்:— ஒரு தமிழ்ப்புலவன் ஐயா!

காலிங்:— முகஸ்துதி பண்ணும் போதே தெரியுதே!..

புலவர்:— எல்லாப் புலவர்களையும் அப்படிச் சொல்லாதீர்கள்! உறுதியோடு இருக்கிற புலவர்களும் இருக்காங்க... சமயத்துக்குத் தக்கபடி தாளம் போடுகிற புலவர்களும் இருக்காங்க!..

ஜமீன்தார்:— காலிங்கா...புலவர் மனதைப் புண்படுத்தாதே! புலவரே! உங்களுக்கு என்ன வேணும்?
""",
8: """<!-- source: pdf=8 printed=7 status=draft -->

புலவர்:— இதோ... இந்தப் பெண் பூங்கொடியை விட்டுவிட்டு என் மனைவி இறந்துவிட்டாள்!... தாயில்லாக் குழந்தையை வச்சிகிட்டு நான் தவிக்கிறேன்!..

ஜமீன்தார்:— (குழந்தையைத் தூக்கி) அய்யோ பாவம்!...தங்கப் பதுமை மாதிரி இருக்கு...குழந்தை... ஏம்மா! ஜலதோஷமா உனக்கு... (மூக்கைச் சிந்தி விடுகிறார்..)

(மக்கள் வியப்பு—குழந்தையைப் புலவரிடம் கொடுத்தவாறு) புலவரே! கவலை வேண்டாம். மாதாமாதம் ஜமீனில் இருந்து இந்தக் குழந்தையை வளர்க்கவும், படிக்கவும் பணம் அனுப்பப்படும்..உமது விலாசத்தை மானேஜர் காலிங்கராயனிடம் கொடுத்துவிட்டுப் போங்கள்...

புலவர்:— நன்றி ஐயா நன்றி!....

(மனுக்கள் காலிங்கனிடம் குவிகின்றன.)

ஜமீன்தார்:— காலிங்கா! வண்டி தயாரா?.... எங்கே வண்டிக்காரன்?....

காலிங்:— டேய் சடையா!...சடையா!..

(உமாவைத் தூக்கியபடி சடையன் ஓடி வந்து)

சடையன்:— எஜமான்...வண்டி தயாருங்க!..

உமா:— அப்பா! நானும் கூட வரேம்ப்பா!

ஜமீன்தார்:— உமா! வேண்டாம்மா...நீ போயி விளையாடு... அப்பா கோயிலுக்குப் போயிட்டு வரேன்!

காலிங்:— குழந்தைங்க கோயிலுக்குப் போகக்கூடாது!...வாம்மா வா...என்கூட வா!

(ஜமீன்தார் வந்து வண்டியில் ஏறி அமர்தல். சடையனும் வண்டியில் ஏறி ஓட்ட — வண்டி புறப்படுகின்றது.)

★

## காட்சி—2

(ஜமீன்தார் வண்டியில் வர, வண்டிக்கார சடையன் வண்டியை ஓட்டி வருகிறான்.)

★
""",
}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def write(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")

def load_json(p: Path):
    return json.loads(read(p))

def dump_json(p: Path, obj) -> None:
    write(p, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

def upsert_marker(path: Path, marker: str, block: str) -> None:
    s=read(path)
    pat=re.escape(marker)+r".*?(?=\n<!-- |\Z)"
    rep=marker+"\n"+block.rstrip()+"\n"
    if marker in s:
        s,n=re.subn(pat,rep,s,count=1,flags=re.S)
        if not n: s += "\n\n"+rep
    else:
        s += "\n\n"+rep
    write(path,s)


def main() -> None:
    P.mkdir(parents=True, exist_ok=True)
    N.mkdir(parents=True, exist_ok=True)
    for n,text in PAGES.items():
        write(P / f"{n:03d}.md", text.rstrip()+"\n")

    index={
        "work_id":"vandikkaran-magan",
        "source_filename":"TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf",
        "source_sha256":SOURCE_SHA,
        "canonical_scope_pdf_pages":"4-87",
        "canonical_scope_page_count":TOTAL_CANONICAL,
        "front_matter_pdf_pages":"4-5",
        "screenplay_pdf_pages":"6-87",
        "screenplay_printed_pages":"5-86",
        "status":"in-progress-draft",
        "first_pass_pages_completed":5,
        "first_pass_pdf_range_completed":"4-8",
        "first_pass_current_through_pdf":8,
        "first_pass_current_through_printed":7,
        "draft_pages":5,
        "verified_pages":0,
        "review_pages":0,
        "open_uncertainty_markers":0,
        "historical_glyph_first_pass_checked_pages":5,
        "historical_glyph_final_verified_pages":0,
        "page_records":[
            {"pdf_page":4,"printed_page":None,"kind":"foreword","status":"draft","path":"pages/004.md"},
            {"pdf_page":5,"printed_page":None,"kind":"foreword","status":"draft","path":"pages/005.md"},
            {"pdf_page":6,"printed_page":5,"kind":"screenplay","status":"draft","path":"pages/006.md"},
            {"pdf_page":7,"printed_page":6,"kind":"screenplay","status":"draft","path":"pages/007.md"},
            {"pdf_page":8,"printed_page":7,"kind":"screenplay","status":"draft","path":"pages/008.md"},
        ],
        "batch_size_source_pages":5,
        "next_batch_pdf_pages":"9-13",
        "next_action":NEXT,
    }
    dump_json(T / "index.json", index)

    write(T / "README.md", f"""# வண்டிக்காரன் மகன் — canonical Tamil transcription

The rendered scan is the controlling source. These files are **first-pass draft transcription**, not visually verified text.

## Current checkpoint

- canonical scope: **PDF 4–87 / 84 pages**;
- first pass complete: **PDF 4–8 / 5 of 84**;
- front matter: **PDF 4–5 / 2 of 2 drafted**;
- screenplay: **PDF 6–8 / 3 of 82 drafted**;
- verified pages: **0**;
- open first-pass uncertainty markers: **0**;
- historical-glyph prospective check: **5/5 drafted pages checked**, final glyph verification **0/84**;
- batch size: **5 source pages per iteration**.

Every page remains `draft` until the later separate full visual-fidelity and historical-glyph verification gates.

## Next

{NEXT}
""")

    write(N / "canonical-first-pass-batch-001.md", f"""# வண்டிக்காரன் மகன் — canonical first pass batch 001

**Batch:** PDF **4–8**  
**Status:** **DRAFT FIRST PASS — 5/84 canonical-scope pages**

## Source disposition

- PDF 4–5: `கலைஞரின் முன்னுரை`;
- PDF 6 / printed 5: title + `காட்சி—1` / `ஜமீன்மாளிகை வெளிப்புறம்`;
- PDF 7 / printed 6: continuation of scene 1;
- PDF 8 / printed 7: scene 1 close and source-visible `காட்சி—2` start.

## Fidelity safeguards used during first pass

- transcription was read from enlarged rendered source pixels, not OCR authority;
- exact source speaker labels and punctuation were retained, including `:—`, colloquial forms and repeated ellipses;
- source-visible star separators remain `★` and were not converted into prose;
- source-irregular lexical forms such as `வைக்கரமாய்`, `கழப்பணியென`, `மகானு`, `குமணனுய்`, and `கர்ணனுய்க்` were not silently modernized;
- the historical `ணா` identity in `அண்ணா` and `நாணயத்தின்`, and the `னா` family in `என்னால்`, were decoded occurrence by occurrence from the source pixels;
- no global historical-glyph replacement was used;
- no page is called verified in this pass.

## First-pass result

- page records created: **5**;
- open uncertainty markers: **0**;
- verified pages claimed: **0**;
- structured derivatives: **still blocked**.

## Next batch

{NEXT}
""")

    write(N / "historical-glyph-audit.md", """# வண்டிக்காரன் மகன் — historical Tamil glyph audit

Guide: `docs/HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

Known mandatory families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

## Prospective first-pass coverage

| PDF | Printed | First-pass glyph check | Representative direct-scan evidence | Final glyph verification |
|---:|:---:|---|---|---|
| 4 | — | PASS for first-pass drafting | complete page inspected; no global substitution | not-started |
| 5 | — | PASS for first-pass drafting | `அண்ணா` → historical `ணா` identity decoded in Unicode | not-started |
| 6 | 5 | PASS for first-pass drafting | complete page inspected; source labels/punctuation retained | not-started |
| 7 | 6 | PASS for first-pass drafting | `நாணயத்தின்` (`ணா`), `என்னால்` (`னா`) inspected from enlarged pixels | not-started |
| 8 | 7 | PASS for first-pass drafting | complete page inspected; no global substitution | not-started |

This is **prospective first-pass glyph checking only**. It does not make a page `verified`; a separate final historical-glyph gate remains mandatory after the complete first pass and visual-fidelity audit.
""")

    # Work metadata.
    mp=W/"metadata.yaml"; s=read(mp)
    s=s.replace("  canonical_tamil_first_pass: not-started","  canonical_tamil_first_pass: in-progress-draft-5-of-84")
    s=s.replace("  visual_fidelity_audit: not-started","  visual_fidelity_audit: not-started")
    insert="""  canonical_tamil_first_pass_pages_completed: 5
  canonical_tamil_first_pass_pdf_range_completed: 4-8
  canonical_tamil_first_pass_current_through_pdf: 8
  canonical_tamil_first_pass_current_through_printed: 7
  canonical_tamil_total_pages: 84
  canonical_tamil_draft_pages: 5
  canonical_tamil_verified_pages: 0
  canonical_tamil_review_pages: 0
  canonical_tamil_open_uncertainty_markers: 0
  canonical_tamil_index_path: works/vandikkaran-magan/transcription/index.json
  canonical_tamil_batch_size_source_pages: 5
  historical_glyph_first_pass_checked_pages: 5
  historical_glyph_final_verified_pages: 0
  historical_glyph_audit_path: works/vandikkaran-magan/notes/historical-glyph-audit.md
"""
    anchor="  canonical_tamil_first_pass: in-progress-draft-5-of-84\n"
    if "canonical_tamil_first_pass_pages_completed" not in s:
        s=s.replace(anchor,anchor+insert,1)
    s=re.sub(r'(?m)^next_action:.*$',"next_action: "+json.dumps(NEXT,ensure_ascii=False),s,count=1)
    write(mp,s)

    # Work README.
    rp=W/"README.md"; s=read(rp)
    s=s.replace("- canonical Tamil: **NOT-STARTED**;","- canonical Tamil first pass: **IN PROGRESS — PDF 4–8 / 5 of 84 DRAFT**;")
    s=s.replace("- historical-glyph full-work audit: **NOT-STARTED**;","- historical-glyph prospective first-pass check: **5/5 drafted pages PASS; final full-work audit NOT-STARTED**;")
    s=re.sub(r"## Exact next activity\n\n> \*\*.*?\*\*\n?", "## Exact next activity\n\n> **"+NEXT+"**\n", s, count=1, flags=re.S)
    if "## Canonical first-pass checkpoint — PDF 4–8" not in s:
        s += f"""\n## Canonical first-pass checkpoint — PDF 4–8

- first-pass canonical pages: **5/84**;
- PDF range: **4–8**;
- screenplay drafted through: **PDF 8 / printed 7**;
- page states: **5 draft / 0 verified / 0 review**;
- open uncertainty markers: **0**;
- prospective historical-glyph check: **5/5**;
- structured derivatives remain **blocked**.

**Next:** {NEXT}
"""
    write(rp,s)

    # Work handover and next-chat prompt.
    hp=W/"PROJECT_HANDOVER.md"; s=read(hp)
    marker="<!-- canonical first pass 004-008 -->"
    block=f"""## Canonical Tamil first-pass checkpoint

- canonical scope: **PDF 4–87 / 84 pages**;
- drafted: **PDF 4–8 / 5 pages**;
- screenplay drafted through **PDF 8 / printed 7**;
- page states: **5 draft / 0 verified / 0 review**;
- first-pass uncertainty markers: **0**;
- historical-glyph prospective check: **PASS 5/5**, final verification **0/84**;
- derivatives: **blocked**.

**Exact next activity:** {NEXT}
"""
    upsert_marker(hp,marker,block)

    write(W/"NEXT_CHAT_PROMPT.md",f"""# Next Chat Prompt — வண்டிக்காரன் மகன்

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **Live `main` is authoritative.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf`

- 90 PDF pages;
- 26,391,039 bytes;
- SHA-256 `{SOURCE_SHA}`;
- image-only scan;
- first edition 1978;
- canonical first-pass scope: **PDF 4–87 / 84 pages**;
- screenplay: PDF 6–87 / printed pp.5–86.

## Durable state

- source intake: **COMPLETE**;
- structural mapping / scene-heading audit: **COMPLETE-VERIFIED / 70 observed headings**;
- canonical Tamil first pass: **IN PROGRESS — PDF 4–8 / 5 of 84 DRAFT**;
- screenplay drafted through **PDF 8 / printed 7**;
- first-pass page states: **5 draft / 0 verified / 0 review**;
- open first-pass uncertainty markers: **0**;
- prospective historical-glyph check: **PASS PDF 4–8 / 5 pages**;
- final visual-fidelity and historical-glyph verification: **NOT-STARTED**;
- structured derivatives: **BLOCKED**.

Preserve source irregularities exactly. Use enlarged source pixels for historical Tamil glyph identity; never global-replace. First-pass pages remain draft.

## Exact next activity

> **{NEXT}**
""")

    # data/works.json entry.
    dp=ROOT/"data"/"works.json"; data=load_json(dp)
    x=next(i for i in data if i.get("id")=="vandikkaran-magan")
    x.update({
        "canonical_tamil_first_pass":"in-progress-draft-5-of-84",
        "canonical_tamil_scope_pdf_pages":"4-87",
        "canonical_tamil_total_pages":84,
        "canonical_tamil_first_pass_pages_completed":5,
        "canonical_tamil_first_pass_pdf_range_completed":"4-8",
        "canonical_tamil_first_pass_current_through_pdf":8,
        "canonical_tamil_first_pass_current_through_printed":7,
        "canonical_tamil_draft_pages":5,
        "canonical_tamil_verified_pages":0,
        "canonical_tamil_review_pages":0,
        "canonical_tamil_open_uncertainty_markers":0,
        "canonical_tamil_index_path":"works/vandikkaran-magan/transcription/index.json",
        "canonical_tamil_batch_size_source_pages":5,
        "historical_glyph_first_pass_checked_pages":5,
        "historical_glyph_final_verified_pages":0,
        "historical_glyph_audit_path":"works/vandikkaran-magan/notes/historical-glyph-audit.md",
        "visual_fidelity_audit":"not-started",
        "historical_glyph_audit":"prospective-first-pass-5-pages-final-not-started",
        "next_action":NEXT,
    })
    dump_json(dp,data)

    # Root README current section.
    root=ROOT/"README.md"; s=read(root)
    s=re.sub(r"- canonical Tamil / fidelity / structured derivatives: \*\*NOT-STARTED / NOT-STARTED / BLOCKED\*\*;", "- canonical Tamil first pass / fidelity / structured derivatives: **PDF 4–8 / 5 of 84 DRAFT / NOT-STARTED / BLOCKED**;", s, count=1)
    s=re.sub(r"- historical-glyph workflow: \*\*mandatory prospectively from first pass\*\*\.", "- historical-glyph workflow: **prospective PASS for PDF 4–8 / 5 drafted pages; final verification not-started**.", s, count=1)
    # replace only active Vandikkaran Next within its section
    pat=r"(## வண்டிக்காரன் மகன் status.*?\n\*\*Next:\*\*) .*?(?=\n\n## |\Z)"
    s=re.sub(pat,lambda m:m.group(1)+" "+NEXT,s,count=1,flags=re.S)
    write(root,s)
    upsert_marker(root,"<!-- Vandikkaran Magan first pass current -->",f"**வண்டிக்காரன் மகன் current:** canonical Tamil first pass **PDF 4–8 / 5 of 84 DRAFT**, screenplay through PDF 8 / printed 7; open uncertainty markers **0**; prospective historical-glyph check **5/5 PASS**; verified pages **0**; derivatives **blocked**. **Next:** {NEXT}\n")

    # Master handover/status audit current markers.
    hand=ROOT/"docs"/"HANDOVER_KALAIGNAR_CINEMA_WORKS.md"
    upsert_marker(hand,"<!-- Vandikkaran Magan first pass current -->",f"""## வண்டிக்காரன் மகன் active first-pass checkpoint

- intake / structural map: **COMPLETE / COMPLETE-VERIFIED**;
- canonical Tamil first pass: **PDF 4–8 / 5 of 84 DRAFT**;
- screenplay drafted through **PDF 8 / printed 7**;
- historical-glyph prospective check: **5/5 PASS**, final verification **0/84**;
- visual fidelity: **not-started**;
- derivatives: **blocked**.

**Exact next activity:** {NEXT}
""")
    audit=ROOT/"docs"/"STATUS_CONSISTENCY_AUDIT.md"
    s=read(audit)
    s=s.replace("| Vandikkaran Magan / வண்டிக்காரன் மகன் | intake + structural map **complete-verified**; canonical Tamil not started | 70 observed source scene headings mapped; derivatives blocked | not-started | not-started |", "| Vandikkaran Magan / வண்டிக்காரன் மகன் | intake + map complete-verified; canonical first pass **5/84 draft** | 70 observed scene headings; derivatives blocked | not-started | not-started |")
    write(audit,s)
    upsert_marker(audit,"<!-- Vandikkaran Magan first pass current -->",f"**Current active work:** **வண்டிக்காரன் மகன்** — canonical Tamil first pass now **PDF 4–8 / 5 of 84 DRAFT**, screenplay through PDF 8 / printed 7, **0** uncertainty markers, historical-glyph prospective check **5/5 PASS**, verified pages **0**, derivatives blocked. **Next:** {NEXT}\n")

    print(json.dumps({
        "status":"PASS",
        "batch":"PDF 4-8",
        "canonical_pages_completed":5,
        "canonical_pages_total":84,
        "through_pdf":8,
        "through_printed":7,
        "open_uncertainty_markers":0,
        "verified_pages":0,
        "next_batch":"PDF 9-13",
    },ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
