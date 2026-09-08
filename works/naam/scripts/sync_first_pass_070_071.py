#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
NEXT=(
    "Begin the separate visual-fidelity and final historical-glyph verification audit with PDF 5–9. "
    "Compare every canonical token against enlarged source pixels, preserve source irregularity, and adjudicate "
    "the two carried source uncertainties only when direct scan evidence positively supports a reading. Mark a "
    "page verified only when both the visual-fidelity and occurrence-specific historical-glyph gates pass; keep "
    "any unresolved page/reason explicit. Structured derivatives and English translation remain blocked until "
    "verified Tamil."
)
changed=[]

def write(rel,text):
    p=ROOT/rel
    old=p.read_text(encoding='utf-8') if p.exists() else ''
    if old!=text:
        p.write_text(text,encoding='utf-8'); changed.append(rel)

def replace_section(text,heading,next_heading,replacement):
    i=text.find(heading)
    if i<0: raise SystemExit(f'missing section {heading}')
    j=text.find(next_heading,i+len(heading)) if next_heading else len(text)
    if j<0: raise SystemExit(f'missing next section {next_heading}')
    return text[:i]+replacement.rstrip()+"\n\n"+text[j:]

idxp=ROOT/'works/naam/transcription/index.json'
idx=json.loads(idxp.read_text(encoding='utf-8'))
for k,v in {'first_pass_pages_completed':65,'current_through_pdf':69,'historical_glyph_checked_pages':65,'verified_pages':0,'open_uncertainty_markers':2}.items():
    if idx.get(k)!=v: raise SystemExit(f'index precondition {k}: {idx.get(k)!r} != {v!r}')
if idx.get('next_batch_pdf_range') != [70,71]: raise SystemExit('expected final remainder 70-71')

batch=(ROOT/'works/naam/transcription/parts/pdf-070-071.md').read_text(encoding='utf-8')
for needle in ['<!-- source: pdf=70 printed=70 status=draft glyph=checked-first-pass -->','பரம்பரை வேதம் எழுதி வைத்திருப்பதால்!','பத்தரை மாத்துத் தங்கம்!','<!-- source: pdf=71 printed=71 status=draft glyph=checked-first-pass -->','மாக்குகிறேன்! நான் தான் சாகிறேன்.','“உலகைத்திருத்தும் உத்தமர்களுக் கெல்லாம் இது தான் முடிவா?”','# நாம்']:
    if needle not in batch: raise SystemExit(f'missing final-batch safeguard: {needle}')
notes=(ROOT/'works/naam/notes/textual-notes-pdf-070-071.md').read_text(encoding='utf-8')
if 'Canonical Tamil first-pass coverage is now **67/67 pages, PDF 5–71**.' not in notes: raise SystemExit('final notes closure statement missing')

idx.update(status='first-pass-complete-verification-pending',first_pass_complete=True,first_pass_pages_completed=67,first_pass_pdf_range_completed=[5,71],draft_pages=67,verified_pages=0,visual_fidelity_passed_pages=0,historical_glyph_checked_pages=67,historical_glyph_verified_pages=0,review_pages=67,open_uncertainty_markers=2,current_through_pdf=71,current_through_printed_page=71,next_batch_pdf_range=[],next_action=NEXT)
parts=idx.setdefault('parts',[])
if not any(x.get('path')=='parts/pdf-070-071.md' for x in parts):
    parts.append({'path':'parts/pdf-070-071.md','pdf_range':[70,71],'printed_range':[70,71],'status':'draft-needs-review','historical_glyph_status':'checked-first-pass','open_uncertainties':0})
parts.sort(key=lambda x:x['pdf_range'][0])
write('works/naam/transcription/index.json',json.dumps(idx,ensure_ascii=False,indent=2)+'\n')

rel='works/naam/metadata.yaml'; t=(ROOT/rel).read_text(encoding='utf-8')
for old,new in [('  status: partial-first-pass\n  pages_expected: 67','  status: first-pass-complete-verification-pending\n  pages_expected: 67'),('first_pass_pages_completed: 65','first_pass_pages_completed: 67'),('first_pass_pdf_range_completed: "5-69"','first_pass_pdf_range_completed: "5-71"'),('first_pass_current_through_pdf: 69','first_pass_current_through_pdf: 71'),('first_pass_current_through_printed_page: 69','first_pass_current_through_printed_page: 71'),('draft_pages: 65','draft_pages: 67'),('review_pages: 65','review_pages: 67'),('current_batch_path: "transcription/parts/pdf-065-069.md"','current_batch_path: "transcription/parts/pdf-070-071.md"'),('current_textual_notes_path: "notes/textual-notes-pdf-065-069.md"','current_textual_notes_path: "notes/textual-notes-pdf-070-071.md"'),('  status: partial-first-pass\n  main_text_pages_expected: 67','  status: first-pass-complete-final-verification-pending\n  main_text_pages_expected: 67'),('pages_checked: 65','pages_checked: 67'),('canonical_tamil_transcription: partial-first-pass-through-pdf-069','canonical_tamil_transcription: first-pass-complete-through-pdf-071'),('historical_glyph_audit: partial-first-pass-through-pdf-069','historical_glyph_audit: first-pass-complete-through-pdf-071')]: t=t.replace(old,new)
anchor='    - "transcription/parts/pdf-065-069.md"\n'
if '    - "transcription/parts/pdf-070-071.md"' not in t:
    if anchor not in t: raise SystemExit('metadata final completed-batch anchor missing')
    t=t.replace(anchor,anchor+'    - "transcription/parts/pdf-070-071.md"\n',1)
if 'batch_070_071_consequential_decodings:' not in t:
    marker='mapped_source_visible_performance_structures:\n'
    extra='''  batch_070_071_consequential_decodings:\n    - pdf_page: 70\n      source_supported_unicode: "சிறைச்சாலை / மலையப்பன்"\n      family: "லை"\n    - pdf_page: 70\n      source_supported_unicode: "குமரனால்"\n      family: "னா"\n    - pdf_page: 70\n      source_supported_unicode: "என்னை"\n      family: "னை"\n    - pdf_page: 70\n      source_supported_unicode: "வருகிறாள்"\n      family: "றா"\n    - pdf_page: 71\n      source_supported_unicode: "உங்களை"\n      family: "ளை"\n\n'''
    if marker not in t: raise SystemExit('metadata performance marker missing')
    t=t.replace(marker,extra+marker,1)
if 'pdf_70_71_new_performance_structures' not in t: t=t.replace('  pdf_65_69_new_performance_structures: 0\n','  pdf_65_69_new_performance_structures: 0\n  pdf_70_71_new_performance_structures: 0\n',1)
t=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',t,count=1,flags=re.S); write(rel,t)

rel='works/naam/README.md'; t=(ROOT/rel).read_text(encoding='utf-8')
for old,new in [('canonical Tamil transcription: **partial first pass — PDF 5–69 / 65 of 67 pages**','canonical Tamil transcription: **first pass complete — PDF 5–71 / 67 of 67 pages; verification pending**'),('historical-Tamil-glyph audit: **partial first pass — 65 pages checked / 0 final-verified**','historical-Tamil-glyph audit: **first pass complete — 67/67 checked / 0 final-verified**'),('Current textual notes: `notes/textual-notes-pdf-065-069.md`','Current textual notes: `notes/textual-notes-pdf-070-071.md`'),('PDF **5–69** has now been transcribed as source-order draft material in thirteen five-page batches. The newest batch contains `காட்சி 40–45` and ends mid-dialogue in `காட்சி-45` on PDF 69; PDF 70 continues the same Kumaran utterance.','PDF **5–71 / 67 of 67 pages** has now been transcribed in source order. The first-pass gate is complete; all pages remain draft/needs-review until the separate visual-fidelity and final historical-glyph verification gates close.'),('PDF 10–69 adds **0** new uncertainty markers','PDF 10–71 adds **0** new uncertainty markers'),('**0** of the sixty-five first-pass pages are called verified yet.','**0** of the sixty-seven canonical pages are called verified yet.')]: t=t.replace(old,new)
if '`transcription/parts/pdf-070-071.md`' not in t:
    marker='`transcription/parts/pdf-065-069.md`  '
    if marker not in t: raise SystemExit('README completed batch marker missing')
    t=t.replace(marker,'`transcription/parts/pdf-065-069.md`, `transcription/parts/pdf-070-071.md`  ',1)
if '- PDF 70–71 completes `காட்சி-45`' not in t:
    marker='- PDF 65–69 adds no new distinct song/lyric/performance structure and introduces **0 new explicit uncertainty markers**;\n'
    add=('- PDF 70–71 completes `காட்சி-45`; PDF 70 continues the PDF 69 utterance without a repeated speaker label and PDF 70→71 preserves the physical `சொந்த` / `மாக்குகிறேன்!` cross-page continuation;\n- PDF 70 preserves source-visible `பத்தரை மாத்துத் தங்கம்!`; PDF 71 closes with `(குமரன் உயிரை இழக்கிறான்)`, `“உலகைத்திருத்தும் உத்தமர்களுக் கெல்லாம் இது தான் முடிவா?”`, `இதை மாற்றி அமைப்பது யார்?`, and final `நாம்`;\n- PDF 70–71 adds **0** new uncertainty markers and no new distinct song/lyric/performance structure; historical-glyph first-pass coverage is now **67/67**;\n')
    if marker in t: t=t.replace(marker,marker+add,1)
t=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S); write(rel,t)

rel='works/naam/transcription/README.md'; t=(ROOT/rel).read_text(encoding='utf-8')
for old,new in [('first-pass completed: **PDF 5–69 / 65 pages**','first-pass completed: **PDF 5–71 / 67 pages — COMPLETE**'),('current first-pass status: **partial-first-pass**','current first-pass status: **complete / verification pending**'),('historical-glyph pages checked during first pass: **65/67**','historical-glyph pages checked during first pass: **67/67**'),('current batch: `parts/pdf-065-069.md`','current/final batch: `parts/pdf-070-071.md`'),('PDF 6–69: visible printed numerals 6–69','PDF 6–71: visible printed numerals 6–71'),('PDF 10–69 introduced **0 new explicit uncertainty markers**.','PDF 10–71 introduced **0 new explicit uncertainty markers**.')]: t=t.replace(old,new)
if '## PDF 70–71 source decisions' not in t:
    section='''\n## PDF 70–71 source decisions\n\nThe final remainder completes source `காட்சி-45` and closes the screenplay.\n\n- PDF 70 directly continues PDF 69's Kumaran utterance at `பரம்பரை வேதம் எழுதி வைத்திருப்பதால்!`; no duplicate label or invented boundary is introduced.\n- PDF 70 preserves `பத்தரை மாத்துத் தங்கம்!` as printed and retains the fight / final-address sequence.\n- PDF 70→71 remains one logical Kumaran utterance across `என் சொத்துக்களை மக்களுக்கு சொந்த` / `மாக்குகிறேன்!`.\n- PDF 71 preserves `வாழ்க சுயமரியாதை, வெல்க பகுத்தறிவு.`, Kumaran's death, the unlabeled closing question, `இதை மாற்றி அமைப்பது யார்?`, and final `நாம்`.\n- Historical-family representatives include PDF 70 `சிறைச்சாலை` / `மலையப்பன்` (`லை`), `குமரனால்` (`னா`), `என்னை` (`னை`), `வருகிறாள்` (`றா`), and PDF 71 `உங்களை` (`ளை`).\n- PDF 70–71 introduces **0 new explicit uncertainty markers** and no newly distinct song/lyric/performance structure.\n- First-pass coverage is **67/67 pages**; verified coverage remains **0/67** pending the separate dual-gate audit.\n\nSee `../notes/textual-notes-pdf-070-071.md` for the final-batch decision log.\n'''
    marker='\n## Performance / lyric evidence encountered so far\n'; t=t.replace(marker,section+marker,1) if marker in t else t+section
t=re.sub(r'## Next activity\n\n\*\*.*?\*\*\s*$',f'## Next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S); write(rel,t)

rel='works/naam/notes/historical-glyph-audit.md'; t=(ROOT/rel).read_text(encoding='utf-8')
t=t.replace('Status: **partial-first-pass**','Status: **first-pass-complete / final-verification-pending**',1)
old='| PDF 65–69 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 70–71 | 2 | 0 | 0 | 0 | not-started |\n| **Total** | **67** | **65** | **0** | **65** | **partial-first-pass** |'; new='| PDF 65–69 | 5 | 5 | 0 | 5 | partial-first-pass |\n| PDF 70–71 | 2 | 2 | 0 | 2 | first-pass-complete |\n| **Total** | **67** | **67** | **0** | **67** | **first-pass-complete / final-verification-pending** |'
if old not in t: raise SystemExit('glyph coverage final precondition missing')
t=t.replace(old,new,1)
if '| 71 | 71 | historical `ளை` cluster | `உங்களை`' not in t:
    rows='''| 70 | 70 | historical `லை` clusters | `சிறைச்சாலை` / `மலையப்பன்` | `லை` | enlarged source pixels | draft-supported |\n| 70 | 70 | historical `னா` cluster | `குமரனால்` | `னா` | enlarged source pixels | draft-supported |\n| 70 | 70 | historical `னை` cluster | `என்னை` | `னை` | enlarged source pixels | draft-supported |\n| 70 | 70 | historical `றா` cluster | `வருகிறாள்` | `றா` | enlarged source pixels | draft-supported |\n| 71 | 71 | historical `ளை` cluster | `உங்களை` | `ளை` | enlarged source pixels | draft-supported |\n'''; marker='\nThese findings decode character identity only.'
    if marker not in t: raise SystemExit('glyph findings marker missing')
    t=t.replace(marker,'\n'+rows+marker,1)
if '## First-pass closure' not in t: t+='''\n## First-pass closure\n\nAll **67/67 canonical pages (PDF 5–71)** have completed occurrence-specific historical-glyph first-pass inspection. This is not final glyph verification: all pages remain review-pending until paired visual-fidelity comparison closes the dual gate. The two source uncertainties remain explicit at PDF 5 and PDF 9.\n'''
write(rel,t)

rel='works/naam/mapping.md'; t=(ROOT/rel).read_text(encoding='utf-8')
t=t.replace('Status: **verified structural mapping; canonical Tamil not-started**','Status: **verified structural mapping; canonical Tamil first-pass complete / verification pending**',1)
t=t.replace('- canonical Tamil: **not-started**;','- canonical Tamil first pass: **complete — PDF 5–71 / 67 of 67; verification pending**;',1)
t=re.sub(r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',t,count=1,flags=re.S); write(rel,t)

rel='works/naam/PROJECT_HANDOVER.md'; t=(ROOT/rel).read_text(encoding='utf-8')
for old,new in [('canonical Tamil: **partial first pass — PDF 5–69 / 65 of 67 pages**','canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages; verification pending**'),('historical-glyph first-pass checked: **65/67**','historical-glyph first-pass checked: **67/67**')]: t=t.replace(old,new)
ls=t.find('Current canonical files:\n'); hd=t.find('\n## Source identity',ls)
if ls>=0 and hd>ls:
    batches=['005-009','010-014','015-019','020-024','025-029','030-034','035-039','040-044','045-049','050-054','055-059','060-064','065-069','070-071']; lines=['Current canonical files:','', '- `transcription/index.json`;','- `transcription/README.md`;']+[f'- `transcription/parts/pdf-{b}.md`;' for b in batches]+[f'- `notes/textual-notes-pdf-{b}.md`;' for b in batches]+['- `notes/historical-glyph-audit.md`.','']; t=t[:ls]+'\n'.join(lines)+t[hd:]
if '### PDF 70–71' not in t:
    marker='\n## Historical-glyph gate'; sec='''\n### PDF 70–71\n\n- final first-pass remainder; completes `காட்சி-45` and closes the screenplay;\n- PDF 70 directly continues the PDF 69 Kumaran utterance and preserves source `பத்தரை மாத்துத் தங்கம்!`;\n- PDF 70→71 preserves the cross-page `சொந்த` / `மாக்குகிறேன்!` continuation as one logical utterance;\n- PDF 71 closes with `(குமரன் உயிரை இழக்கிறான்)`, `“உலகைத்திருத்தும் உத்தமர்களுக் கெல்லாம் இது தான் முடிவா?”`, `இதை மாற்றி அமைப்பது யார்?`, and final `நாம்`;\n- PDF 70–71 introduces **0** new uncertainty markers and no new distinct performance structure;\n- canonical Tamil first pass and historical-glyph first-pass coverage are now **67/67**, but verified pages remain **0/67**.\n'''; t=t.replace(marker,sec+marker,1) if marker in t else t+sec
t=re.sub(r'## Exact next activity\n\n> \*\*.*?\*\*\s*$',f'## Exact next activity\n\n> **{NEXT}**\n',t,count=1,flags=re.S); write(rel,t)

write('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`.\n\n## LIVE MAIN IS AUTHORITATIVE\n\nFetch live `main` first and preserve newer durable work.\n\nCurrent durable checkpoint:\n\n- source intake / mapping: **complete / verified**;\n- canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages**;\n- verified pages: **0/67**;\n- visual-fidelity audit: **not-started**;\n- historical-glyph first-pass checked: **67/67**;\n- historical-glyph final verified: **0/67**;\n- open uncertainty markers: **2** — PDF 5 damaged introductory span and PDF 9 unclear montage word;\n- structured derivatives / English: **blocked pending verified Tamil**.\n\n## Controlling source\n\nResolve `TVA_BOK_0064201_நாம்.pdf` before source-level visual work. Recorded identity: **72 PDF pages**, **115,948,588 bytes**, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`, image-only; canonical screenplay PDF **5–71**.\n\n## Frozen first-pass layer\n\nPDF 5–71 is now complete as a source-order first-pass draft. Do not retranscribe or silently modernize it. PDF 70–71 closes `காட்சி-45`; PDF 70 continues the PDF 69 utterance and PDF 70→71 preserves the `சொந்த` / `மாக்குகிறேன்!` cross-page continuation.\n\nThe first-pass layer is **not verified**. English translation remains blocked until both visual-fidelity and final occurrence-specific historical-glyph verification close.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

rel='data/works.json'; d=json.loads((ROOT/rel).read_text(encoding='utf-8')); n=next(x for x in d if x.get('id')=='naam')
n.update(canonical_tamil_transcription='first-pass-complete-through-pdf-071-verification-pending',historical_glyph_audit='first-pass-complete-through-pdf-071-final-verification-pending',next_action=NEXT,canonical_tamil_first_pass_pages_completed=67,canonical_tamil_first_pass_pdf_range_completed='5-71',canonical_tamil_first_pass_current_through_pdf=71,canonical_tamil_first_pass_complete=True,canonical_tamil_draft_pages=67,canonical_tamil_verified_pages=0,canonical_tamil_review_pages=67,canonical_tamil_open_uncertainty_markers=2,canonical_tamil_current_batch_path='works/naam/transcription/parts/pdf-070-071.md',canonical_tamil_current_textual_notes_path='works/naam/notes/textual-notes-pdf-070-071.md',historical_glyph_pages_checked=67,historical_glyph_pages_verified=0,visual_fidelity_audit='not-started'); write(rel,json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')

rel='README.md'; t=(ROOT/rel).read_text(encoding='utf-8'); block=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` is the **active cinema source**. Intake and the 45-scene structural map are complete; canonical Tamil first-pass transcription is now **complete**.\n\n- canonical Tamil first pass: **PDF 5–71 / 67 of 67 pages — COMPLETE**;\n- verified pages: **0/67**; visual-fidelity audit: **not-started**;\n- historical-glyph first-pass checked: **67/67**; final glyph-verified: **0/67**;\n- open source uncertainty markers: **2**, both carried from PDF 5/9; PDF 10–71 adds none;\n- final batch: `works/naam/transcription/parts/pdf-070-071.md`;\n- first-pass source layer is frozen pending verification; downstream derivatives and English remain blocked.\n\n**Next:** {NEXT}\n'''; t=replace_section(t,'## நாம் status','## ராஜா ராணி status',block); write(rel,t)

rel='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; t=(ROOT/rel).read_text(encoding='utf-8')
t=re.sub(r'- \*\*Naam / நாம்\*\* — active work;.*?Source SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`\.', '- **Naam / நாம்** — active work; intake/map complete; canonical Tamil first pass **COMPLETE — PDF 5–71 / 67 of 67**; glyph first-pass **67/67**; verified **0/67**; 2 carried source uncertainties; visual-fidelity/final-glyph verification next. Source SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.',t,count=1,flags=re.S)
block=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / whole-scan map: **complete / verified**;\n- canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages**;\n- canonical verified pages: **0/67**;\n- visual-fidelity audit: **not-started**;\n- historical-glyph first-pass checked / final verified: **67/67 / 0/67**;\n- open source uncertainties: **2**, both inherited from PDF 5/9;\n- final batch: `works/naam/transcription/parts/pdf-070-071.md`;\n- final source notes: `works/naam/notes/textual-notes-pdf-070-071.md`;\n- PDF 70–71 completes scene 45 and the screenplay; no new uncertainty or distinct performance structure was added;\n- structured derivatives / English / reader remain blocked pending verified Tamil.\n\n**Exact next activity:** {NEXT}\n'''; t=replace_section(t,'## 8. Naam active checkpoint','## 9. Ammayappan closed checkpoint',block); write(rel,t)

rel='docs/STATUS_CONSISTENCY_AUDIT.md'; t=(ROOT/rel).read_text(encoding='utf-8').replace('Audit date: 2026-09-06','Audit date: 2026-09-08')
t=t.replace('| Naam / நாம் | intake/map complete; first pass **PDF 5–69 / 65 of 67**, 0 verified','| Naam / நாம் | intake/map complete; first pass **PDF 5–71 / 67 of 67 COMPLETE**, 0 verified')
block=f'''## Naam current checkpoint\n\n- work: `works/naam/`;\n- source intake / structural mapping: **complete / verified**;\n- canonical Tamil first pass: **COMPLETE — PDF 5–71 / 67 of 67 pages**;\n- verified pages / visual-fidelity passed: **0 / 0**;\n- historical-glyph first-pass checked / final verified: **67 / 0**;\n- open uncertainty markers: **2**, both carried from PDF 5/9;\n- final draft: `works/naam/transcription/parts/pdf-070-071.md`;\n- final source notes: `works/naam/notes/textual-notes-pdf-070-071.md`;\n- PDF 70–71 introduces no new explicit uncertainty and no new distinct song/lyric/performance structure;\n- downstream scene/dialogue/character/song/English layers remain blocked until verified Tamil.\n\n**Next production phase:** {NEXT}\n'''; t=replace_section(t,'## Naam current checkpoint','## Ammayappan current checkpoint',block)
t=re.sub(r'\*\*Naam / நாம்\*\* is the active production work with intake/map complete and canonical Tamil first pass at \*\*PDF 5–69 / 65 of 67 pages\*\*, \*\*0 verified pages\*\*, historical-glyph first-pass \*\*65/67\*\*, and \*\*2 carried source uncertainties\*\*\. The final first-pass remainder is PDF 70–71\.', '**Naam / நாம்** is the active production work with intake/map complete and canonical Tamil first pass **COMPLETE at PDF 5–71 / 67 of 67 pages**, **0 verified pages**, historical-glyph first-pass **67/67**, and **2 carried source uncertainties**. The next phase is visual-fidelity plus final historical-glyph verification.',t,count=1); write(rel,t)

print('Closed Naam Tamil first-pass gate through PDF 71')
for x in changed: print('-',x)
