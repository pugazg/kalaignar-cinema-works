#!/usr/bin/env python3
import json,re
from pathlib import Path

R=Path(__file__).resolve().parents[3]
DATE="2026-09-08"
NEXT=("Begin Phase 5 scene-text derivatives from the fully verified canonical Tamil. "
"Create one derivative for each source-numbered காட்சி 1–45 in source order, preserve exact source headings, page provenance and cross-page/cross-part continuity, "
"and run scene-boundary ownership QA before proceeding to the dialogue index. Do not alter canonical Tamil except for later source-supported corrections.")

changed=[]
def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
    q=R/p
    old=q.read_text(encoding='utf-8') if q.exists() else ''
    if old!=s:
        q.parent.mkdir(parents=True,exist_ok=True)
        q.write_text(s,encoding='utf-8')
        changed.append(p)
def one(s,a,b,required=True):
    if a not in s:
        if required: raise SystemExit('missing expected text: '+a[:160])
        return s
    return s.replace(a,b,1)
def sub1(s,pat,repl,flags=0,required=True):
    out,n=re.subn(pat,repl,s,count=1,flags=flags)
    if n!=1 and required: raise SystemExit('regex expected once: '+pat[:160]+f' (found {n})')
    return out

def replace_tail(s,marker,new_tail):
    i=s.find(marker)
    if i<0: raise SystemExit('missing tail marker: '+marker)
    return s[:i]+new_tail.rstrip()+"\n"

# Preconditions: live state immediately before user manual closure.
ip='works/naam/transcription/index.json'
d=json.loads(rd(ip))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(64,64,67,3)

# ------------------------------------------------------------------
# 1) Canonical pages: apply the user's manual controlling-scan verdicts.
# Binding guide explicitly permits a user manual scan verdict for a reviewed
# occurrence; these are therefore source-review decisions, not context fills.
# ------------------------------------------------------------------
p='works/naam/transcription/parts/pdf-005-009.md'
s=rd(p)
s=one(s,'# நாம் — canonical Tamil first-pass batch','# நாம் — canonical Tamil verification batch')
s=one(s,'Status: **mixed verification — PDF 5 needs-review; PDF 6–9 VERIFIED** — rendered scan controls.',
      'Status: **VERIFIED — PDF 5–9 / 5 of 5 dual-gate complete** — rendered scan + recorded user manual source verdicts control.')
s=one(s,'<!-- source: pdf=5 printed=unknown status=needs-review glyph=verified-final -->',
      '<!-- source: pdf=5 printed=unknown status=verified glyph=verified-final -->')
s=sub1(s,r'⟦தெளிவில்லை — PDF 5 வரியின் இடதுபுறத் தொடக்கம் உடல் சேதத்தால் இல்லை; நேரடியாகத் தெரியும் பகுதி: `…னைத் கொலைத்துவிட சில துரோகிகள் கிளம்பினர்\.`⟧',
       'அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.')
s=replace_tail(s,'\n---\n\n## Dual-gate verification result',f'''\n---\n\n## Final dual-gate verification result\n\n- PDF 5–9: **5/5 VERIFIED**.\n- PDF 5 was initially held because assistant-side enlarged inspection could not recover the damaged beginning. On {DATE}, the user manually inspected the controlling scan and supplied the printed reading **`அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`**. Under the binding cinema-work guide's manual-scan-verdict rule, that occurrence is closed unless later direct source evidence reopens it.\n- The independent PDF 5 correction `ஒன்றியின வேண்டுகோள்படி` → **`அன்னையின் வேண்டுகோள்படி`** remains in force.\n- Historical-glyph final verification: **5/5 PASS**.\n- Open uncertainty for this batch: **0**.\n- Detailed final closure: `../../notes/canonical-closure-user-manual.md`.\n''')
wr(p,s)

p='works/naam/transcription/parts/pdf-010-014.md'
s=rd(p)
s=one(s,'Status: **mixed verification — PDF 10 needs-review; PDF 11–14 VERIFIED** — rendered scan controls.',
      'Status: **VERIFIED — PDF 10–14 / 5 of 5 dual-gate complete** — rendered scan + recorded user manual source verdicts control.')
s=one(s,'<!-- source: pdf=10 printed=10 status=needs-review glyph=verified-final -->',
      '<!-- source: pdf=10 printed=10 status=verified glyph=verified-final -->')
s=sub1(s,r'நீ இங்கே வேலை பார்க்கிற வரைக்⟦தெளிவில்லை — PDF 10 வலது விளிம்பு உடல் சேதம்; சொல்லின் முடிவு இல்லை⟧',
       'நீ இங்கே வேலை பார்க்கிற வரைக்கும்')
s=replace_tail(s,'\n---\n\n## Verification audit notes',f'''\n---\n\n## Final verification notes\n\n- PDF 10–14: **5/5 visual-fidelity PASS; 5/5 historical-glyph final PASS; 5/5 dual-gate VERIFIED**.\n- PDF 10 was initially held after assistant-side enlarged inspection could see only `வரைக்…`. On {DATE}, the user manually inspected the controlling scan and supplied the exact completion **`நீ இங்கே வேலை பார்க்கிற வரைக்கும்`**. The recorded manual source verdict closes the page.\n- All previously scan-backed corrections and exact source abbreviations in PDF 10–14 remain unchanged.\n- Open uncertainty for this batch: **0**.\n- Detailed final closure: `../../notes/canonical-closure-user-manual.md`.\n''')
wr(p,s)

p='works/naam/transcription/parts/pdf-020-024.md'
s=rd(p)
s=one(s,'# நாம் — canonical Tamil first-pass batch','# நாம் — canonical Tamil verification batch')
s=one(s,'Status: **mixed verification — PDF 20–23 VERIFIED; PDF 24 needs-review** — rendered scan controls.',
      'Status: **VERIFIED — PDF 20–24 / 5 of 5 dual-gate complete** — rendered scan + recorded user manual source verdicts control.')
s=one(s,'<!-- source: pdf=24 printed=24 status=needs-review glyph=verified-final -->',
      '<!-- source: pdf=24 printed=24 status=verified glyph=verified-final -->')
s=sub1(s,r'மல்லயப்ப :- மீனு\.\.\.! அண்ணனுக்கு கெளரவம் தே⟦தெளிவில்லை — PDF 24: `தே`க்கு அடுத்த அச்செழுத்து மீது மை/கறை மறைவு; மறைந்த எழுத்து ஊகித்து நிரப்பப்படவில்லை⟧ இருப்பது ரொம்பவும் அழகாக இருக்கிறது\.',
       'மல்லயப்ப :- மீனு...! அண்ணனுக்கு கெளரவம் தேடி இருப்பது ரொம்பவும் அழகாக இருக்கிறது.')
s=replace_tail(s,'\n---\n\n## Verification audit notes',f'''\n---\n\n## Final verification notes\n\n- PDF 20–24: **5/5 visual-fidelity PASS; 5/5 historical-glyph final PASS; 5/5 dual-gate VERIFIED**.\n- PDF 24 was initially held because assistant-side enlarged/channel inspection could not positively see the printed cluster after `கெளரவம் தே`. On {DATE}, the user manually inspected the controlling scan and supplied the printed form **`கெளரவம் தேடி`**. The canonical line is therefore `அண்ணனுக்கு கெளரவம் தேடி இருப்பது ரொம்பவும் அழகாக இருக்கிறது.`\n- No contextual or external-source completion is being introduced; this is a recorded manual verdict on the controlling source itself.\n- Open uncertainty for this batch: **0**.\n- Detailed final closure: `../../notes/canonical-closure-user-manual.md`.\n''')
wr(p,s)

# ------------------------------------------------------------------
# 2) Final canonical-closure audit and audit lineage.
# ------------------------------------------------------------------
closure=f'''# நாம் — canonical Tamil closure — user manual controlling-scan verdicts\n\nSource: `TVA_BOK_0064201_நாம்.pdf`  \nDate: **{DATE}**  \nFinal result: **canonical Tamil COMPLETE-VERIFIED — 67/67 visual-fidelity PASS; 67/67 historical-glyph final PASS; 67/67 dual-gate VERIFIED; 0 unresolved source markers**.\n\n## Authority basis\n\nThe controlling printed scan remains the textual authority. Earlier assistant-side enlarged/native inspections left three obscuration holds because the surviving pixels were not confidently recoverable from that inspection path. The user then manually inspected the same controlling scan and explicitly supplied the printed forms. `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` states that when the user manually inspects the controlling scan and explicitly supplies the printed form, that reviewed verdict is preserved for the occurrence unless later direct source evidence reopens it.\n\nThese readings are therefore recorded as **user manual controlling-scan verdicts**, not grammar-, OCR-, film-, subtitle-, web-, later-edition- or memory-based reconstruction.\n\n## Final resolved readings\n\n| PDF | Earlier repository hold | Final user-reviewed source reading | Disposition |\n|---:|---|---|---|\n| 5 | damaged beginning of introductory line | `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.` | **RESOLVED / VERIFIED** |\n| 10 | right-edge ending after `வரைக்…` | `நீ இங்கே வேலை பார்க்கிற வரைக்கும்` | **RESOLVED / VERIFIED** |\n| 24 | covered cluster after `கெளரவம் தே` | `கெளரவம் தேடி` | **RESOLVED / VERIFIED** |\n\nPDF 5 also retains the earlier direct visible-text correction `ஒன்றியின வேண்டுகோள்படி` → `அன்னையின் வேண்டுகோள்படி`.\n\n## Final gate state\n\n- first pass: **67/67 COMPLETE**;\n- visual fidelity: **67/67 PASS / COMPLETE**;\n- historical Tamil glyph final: **67/67 PASS / COMPLETE**;\n- dual-gate canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- draft / review pages: **0 / 0**;\n- open source uncertainty markers: **0**;\n- structured derivatives: **now unblocked**;\n- English translation: still waits for the normal structured-derivative gates.\n\nNo scene/dialogue/character/song/translation/reader derivative existed when these three readings were closed, so downstream reconciliation is not required.\n\n## Next activity\n\n{NEXT}\n'''
wr('works/naam/notes/canonical-closure-user-manual.md',closure)

p='works/naam/notes/source-obscuration-hold-resolution.md'
s=rd(p)
if '## Final superseding disposition — user manual controlling-scan verdicts' not in s:
    s += f'''\n\n## Final superseding disposition — user manual controlling-scan verdicts\n\nThe `0 resolved / 3 retained` result above records the earlier assistant-side enlarged-source reinspection only. It is **superseded for current canonical status** by the user's manual inspection of the controlling scan on {DATE}. The user supplied: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, and PDF 24 `கெளரவம் தேடி`.\n\nPer `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`, these explicit manual controlling-scan verdicts are accepted for the reviewed occurrences. All three holds are now **RESOLVED**. See `canonical-closure-user-manual.md`.\n'''
wr(p,s)

# Verification-audit lineage: preserve initial audit history but clearly supersede hold dispositions.
for p,old_result,old_heading,pg,reading in [
('works/naam/notes/verification-audit-pdf-005-009.md','Result: **PDF 6–9 PASS / VERIFIED; PDF 5 HOLD; 4/5 dual-gate verified**.','## PDF 5 — HOLD',5,'`அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`'),
('works/naam/notes/verification-audit-pdf-010-014.md','Result: **PDF 11–14 PASS / VERIFIED; PDF 10 HOLD; 4/5 dual-gate verified**.','## PDF 10 — HOLD',10,'`நீ இங்கே வேலை பார்க்கிற வரைக்கும்`'),
('works/naam/notes/verification-audit-pdf-020-024.md','Result: **PDF 20–23 PASS / VERIFIED; PDF 24 HOLD; 4/5 dual-gate verified**.','## PDF 24 — HOLD',24,'`கெளரவம் தேடி`')]:
    s=rd(p)
    s=one(s,old_result,old_result+'  \n**Final amendment:** the held page was subsequently resolved by the user\'s manual controlling-scan verdict; final batch status is **5/5 VERIFIED**.')
    s=one(s,old_heading,old_heading+' — INITIAL HOLD, SUPERSEDED')
    if '## Final user-manual source closure amendment' not in s:
        s += f'''\n\n## Final user-manual source closure amendment\n\nOn {DATE}, the user manually inspected the controlling scan and supplied the exact reviewed reading for PDF {pg}: **{reading}**. Under the binding cinema-work processing guide, this manual source verdict supersedes the earlier assistant-side inability to recover the obscured characters. PDF {pg} is now **VERIFIED**, this batch is **5/5 dual-gate VERIFIED**, and the current whole-work status is recorded in `canonical-closure-user-manual.md`.\n'''
    wr(p,s)

# Post-fidelity/correction history.
p='works/naam/notes/post-fidelity-corrections.md'
s=rd(p)
if '## 2026-09-08 — final user-manual source closure' not in s:
    s += f'''\n\n## 2026-09-08 — final user-manual source closure\n\nAfter the assistant-side source-obscuration audit retained PDF 5, PDF 10 and PDF 24 as holds, the user manually inspected the controlling scan and supplied exact printed readings. The binding processing guide explicitly permits this occurrence-specific manual source verdict.\n\n| PDF | Earlier canonical state | Final reviewed reading |\n|---:|---|---|\n| 5 | explicit damaged-line lacuna | `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.` |\n| 10 | `வரைக்` + explicit right-edge lacuna | `நீ இங்கே வேலை பார்க்கிற வரைக்கும்` |\n| 24 | `கெளரவம் தே` + explicit ink/mark lacuna | `கெளரவம் தேடி` |\n\nNo downstream structured derivative, English translation or reader existed, so no derivative reconciliation is required. After these three manual source verdicts, canonical Tamil is **67/67 dual-gate COMPLETE-VERIFIED with 0 unresolved source markers**.\n'''
wr(p,s)

# ------------------------------------------------------------------
# 3) Canonical index and metadata.
# ------------------------------------------------------------------
d.update(status='complete-verified',draft_pages=0,verified_pages=67,visual_fidelity_passed_pages=67,
         historical_glyph_checked_pages=67,historical_glyph_verified_pages=67,review_pages=0,
         open_uncertainty_markers=0,next_batch_pdf_range=[],next_action=NEXT,
         hold_resolution_status='resolved-3-by-user-manual-scan-verdict',
         canonical_closure_audit='../notes/canonical-closure-user-manual.md')
for x in d['parts']:
    if x['path'] in {'parts/pdf-005-009.md','parts/pdf-010-014.md','parts/pdf-020-024.md'}:
        x['status']='verified'; x['historical_glyph_status']='verified-final'; x['open_uncertainties']=0
d['manual_source_verdicts']=[
    {'pdf_page':5,'reading':'அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.','basis':'user-manual-controlling-scan-verdict'},
    {'pdf_page':10,'reading':'நீ இங்கே வேலை பார்க்கிற வரைக்கும்','basis':'user-manual-controlling-scan-verdict'},
    {'pdf_page':24,'reading':'கெளரவம் தேடி','basis':'user-manual-controlling-scan-verdict'},
]
wr(ip,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

p='works/naam/metadata.yaml'; s=rd(p)
s=one(s,'  status: verification-in-progress','  status: complete-verified')
s=one(s,'  draft_pages: 3','  draft_pages: 0')
s=one(s,'  verified_pages: 64','  verified_pages: 67')
s=one(s,'  review_pages: 3','  review_pages: 0')
s=one(s,'  open_uncertainty_markers: 3','  open_uncertainty_markers: 0')
vp=f'''verification_progress:\n  current_audit_path: "notes/canonical-closure-user-manual.md"\n  hold_resolution_audit_path: "notes/source-obscuration-hold-resolution.md"\n  canonical_closure_audit_path: "notes/canonical-closure-user-manual.md"\n  hold_resolution_status: resolved-3-by-user-manual-scan-verdict\n  visual_fidelity_passed_pages: 67\n  historical_glyph_final_verified_pages: 67\n  dual_gate_verified_pages: 67\n  held_pages: []\n  resolved_uncertainties:\n    - pdf_page: 9\n      reading: "குறுக்கொடிய"\n      basis: direct-source-final-audit\n    - pdf_page: 5\n      reading: "அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்."\n      basis: user-manual-controlling-scan-verdict\n    - pdf_page: 10\n      reading: "நீ இங்கே வேலை பார்க்கிற வரைக்கும்"\n      basis: user-manual-controlling-scan-verdict\n    - pdf_page: 24\n      reading: "கெளரவம் தேடி"\n      basis: user-manual-controlling-scan-verdict\n  next_pdf_range: null\n'''
s=sub1(s,r'verification_progress:\n.*?\nhistorical_glyph:\n',vp+'\nhistorical_glyph:\n',flags=re.S)
s=one(s,'  status: intake-plus-first-pass-candidates','  status: verified-canonical-candidates-awaiting-song-gate')
status=f'''status:\n  duplicate_work_check: complete-no-existing-work\n  source_intake: complete\n  whole_scan_inspection: complete\n  structural_mapping: verified\n  canonical_tamil_transcription: complete-verified-67-of-67\n  visual_fidelity_audit: complete-67-of-67-pass\n  historical_glyph_audit: complete-final-verified-67-of-67\n  scene_derivatives: not-started-ready\n  dialogue_index: blocked-pending-scene-derivatives\n  character_entity_index: blocked-pending-dialogue-layer\n  song_authorship_gate: blocked-pending-scene-dialogue-character-layers\n  english_translation: blocked-pending-structured-derivatives-and-song-gate\n  reader_export: not-started\n  reading_room_integration: not-started\n'''
s=sub1(s,r'status:\n  duplicate_work_check:.*?\n\nuser_supplied_context:',status+'\nuser_supplied_context:',flags=re.S)
s=sub1(s,r'next_action: ".*?"\s*$',f'next_action: "{NEXT}"',flags=re.S)
wr(p,s)

# Historical glyph dual-gate coverage is now also 67/67.
p='works/naam/notes/historical-glyph-audit.md'; s=rd(p)
for a,b in [
('| PDF 5–9 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF5 hold |','| PDF 5–9 | 5 | 5 | 5 | 0 | final-audit: 5 verified |'),
('| PDF 10–14 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF10 hold |','| PDF 10–14 | 5 | 5 | 5 | 0 | final-audit: 5 verified |'),
('| PDF 20–24 | 5 | 5 | 4 | 1 | final-audit: 4 verified / PDF24 hold |','| PDF 20–24 | 5 | 5 | 5 | 0 | final-audit: 5 verified |'),
('| **Total** | **67** | **67** | **64** | **3** | **historical-glyph-final-complete / visual-holds-remain** |','| **Total** | **67** | **67** | **67** | **0** | **dual-gate-complete-verified** |')]: s=one(s,a,b)
if '## Final canonical closure by manual source verdict' not in s:
    s += f'''\n\n## Final canonical closure by manual source verdict\n\nHistorical-glyph final verification was already **67/67 COMPLETE**. The remaining visual/source holds on PDF 5, PDF 10 and PDF 24 were resolved on {DATE} by the user's explicit manual inspection of the controlling scan. Final whole-work dual-gate status is therefore **67/67 COMPLETE-VERIFIED / 0 needs-review**. See `canonical-closure-user-manual.md`.\n'''
wr(p,s)

# ------------------------------------------------------------------
# 4) Work-local current mirrors.
# ------------------------------------------------------------------
p='works/naam/README.md'; s=rd(p)
current='''## Current checkpoint\n\n- source intake: **complete**;\n- structural mapping: **verified**;\n- canonical Tamil transcription: **67/67 COMPLETE-VERIFIED**;\n- canonical Tamil verified pages: **67/67**;\n- visual fidelity audit: **67/67 PASS / COMPLETE**;\n- historical-Tamil-glyph audit: **67/67 final-verified / COMPLETE**;\n- open source uncertainty markers: **0**;\n- scene derivatives: **not-started / ready**;\n- dialogue / character / song derivatives: **blocked by normal gate order after scenes**;\n- English translation / reader / Reading Room: **not-started**.\n\n'''
s=sub1(s,r'## Current checkpoint\n\n.*?(?=Current transcription index:)',current,flags=re.S)
s=sub1(s,r'PDF \*\*5–71 / 67 of 67 pages\*\* has now been transcribed in source order\. The first-pass gate is complete and the dual-gate verification pass is in progress: \*\*64/67\*\* pages are now verified; PDF 5, PDF 10 and PDF 24 remain explicit source-obscuration holds\.',
       'PDF **5–71 / 67 of 67 pages** is transcribed and **67/67 dual-gate COMPLETE-VERIFIED**. The three former source-obscuration holds on PDF 5, PDF 10 and PDF 24 were closed by recorded user manual controlling-scan verdicts; open source uncertainty is now **0**.')
s=sub1(s,r'- three source uncertainties remain explicit rather than guessed:.*?\n- \*\*64/67\*\* canonical pages are dual-gate VERIFIED: PDF 6–9, PDF 11–23 and PDF 25–71\.',
       '- the three former holds are now resolved by user manual controlling-scan verdicts: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;\n- **67/67** canonical pages are dual-gate VERIFIED.',flags=re.S)
closure_sec=f'''## Canonical Tamil closure — user manual source verdicts\n\n- PDF 5: **`அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`**;\n- PDF 10: **`நீ இங்கே வேலை பார்க்கிற வரைக்கும்`**;\n- PDF 24: **`கெளரவம் தேடி`**;\n- authority basis: explicit user manual inspection of the controlling scan, permitted by the binding cinema-work processing guide;\n- canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- visual / historical-glyph / dual-gate: **67/67 / 67/67 / 67/67**;\n- open source uncertainties: **0**;\n- final audit: `notes/canonical-closure-user-manual.md`;\n- no downstream derivative reconciliation required because derivatives had not yet started.\n\n**Next:** {NEXT}\n\n'''
s=sub1(s,r'## Verification audit — through PDF 71\n.*?(?=## Song / verse / performance structures mapped or confirmed so far)',closure_sec,flags=re.S)
s=sub1(s,r'## Exact next activity\n\n\*\*.*?\*\*\s*$',f'## Exact next activity\n\n**{NEXT}**\n',flags=re.S)
wr(p,s)

p='works/naam/transcription/README.md'; s=rd(p)
current='''## Current checkpoint\n\n- canonical range expected: **PDF 5–71 / 67 pages**;\n- first-pass completed: **PDF 5–71 / 67 pages — COMPLETE**;\n- canonical Tamil status: **COMPLETE-VERIFIED**;\n- verified pages: **67/67**;\n- visual-fidelity audit: **67/67 PASS / COMPLETE**;\n- historical-glyph pages checked / final verified: **67/67 / 67/67 COMPLETE**;\n- open source uncertainty markers: **0**;\n- canonical closure audit: `../notes/canonical-closure-user-manual.md`;\n- index: `index.json`.\n\n'''
s=sub1(s,r'## Current checkpoint\n\n.*?(?=The first pass is deliberately not the verification gate\.)',current,flags=re.S)
final_tail=f'''## Final canonical closure — user manual controlling-scan verdicts\n\nThe three former source-obscuration holds are resolved: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, and PDF 24 `கெளரவம் தேடி`. These are recorded occurrence-specific user manual verdicts on the controlling scan, not inferred completions.\n\nFinal status: **67/67 visual PASS; 67/67 historical-glyph final PASS; 67/67 dual-gate COMPLETE-VERIFIED; 0 open uncertainty markers**. See `../notes/canonical-closure-user-manual.md`.\n\n## Next activity\n\n**{NEXT}**\n'''
if '## Targeted source-obscuration hold-resolution audit' in s:
    s=sub1(s,r'## Targeted source-obscuration hold-resolution audit\n.*$',final_tail,flags=re.S)
else:
    s += '\n\n'+final_tail
wr(p,s)

p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
current='''## Current checkpoint\n\n- source intake: **complete**;\n- whole scan inspected: **72/72 PDF pages**;\n- structural mapping: **verified**;\n- source-numbered scenes: **45 / காட்சி 1–45**, sequential with no observed gaps/repeats/out-of-order numbers;\n- canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- visual fidelity: **67/67 PASS / COMPLETE**;\n- historical-glyph final: **67/67 COMPLETE**;\n- open source uncertainty markers: **0**;\n- scene derivatives: **not-started / ready**;\n- dialogue / character / song / English / reader layers: **not-started, subject to normal gate order**.\n\n'''
s=sub1(s,r'## Current checkpoint\n\n.*?(?=Current canonical files:)',current,flags=re.S)
final=f'''## Final canonical closure — {DATE}\n\nThe user's manual controlling-scan review resolves all three former source-obscuration holds:\n\n- PDF 5 — `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`;\n- PDF 10 — `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`;\n- PDF 24 — `கெளரவம் தேடி`.\n\nThe cinema-work processing guide explicitly preserves a user's manual controlling-scan verdict for a reviewed occurrence unless later direct source evidence reopens it. Final canonical Tamil is **67/67 COMPLETE-VERIFIED**, visual **67/67**, glyph-final **67/67**, dual-gate **67/67**, open source uncertainties **0**. Final audit: `notes/canonical-closure-user-manual.md`.\n\nNo downstream derivative existed at closure, so reconciliation is not required.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
s=sub1(s,r'## Verification checkpoint through PDF 71\n.*$',final,flags=re.S)
wr(p,s)

wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is now **COMPLETE-VERIFIED: 67/67 visual-fidelity PASS; 67/67 historical-glyph final PASS; 67/67 dual-gate VERIFIED; 0 open source uncertainties**.\n\nThe three former holds were closed by the user's manual inspection of the controlling scan on {DATE}:\n\n- PDF 5: `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`\n- PDF 10: `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`\n- PDF 24: `கெளரவம் தேடி`\n\nPDF 5 also retains the earlier correction `அன்னையின் வேண்டுகோள்படி`. These are occurrence-specific manual controlling-scan verdicts under `docs/CINEMA_WORKS_PROCESSING_GUIDE.md`; do not reopen them absent genuinely new direct source evidence.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\nFinal canonical audit: `works/naam/notes/canonical-closure-user-manual.md`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# ------------------------------------------------------------------
# 5) Repository-wide current mirrors.
# ------------------------------------------------------------------
p='README.md'; s=rd(p)
sec=f'''## நாம் status\n\n`TVA_BOK_0064201_நாம்.pdf` now has **complete-verified canonical Tamil**. The user's manual controlling-scan review resolved the three former source-obscuration holds.\n\n- canonical Tamil / visual / glyph-final / dual-gate: **67/67 / 67/67 / 67/67 / 67/67 COMPLETE**;\n- open source uncertainties: **0**;\n- final manual-source readings: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;\n- final canonical audit: `works/naam/notes/canonical-closure-user-manual.md`;\n- scene derivatives: **not-started / ready**;\n- English remains downstream of scene/dialogue/character/song gates.\n\n**Next:** {NEXT}\n\n'''
s=sub1(s,r'## நாம் status\n.*?(?=## ராஜா ராணி status)',sec,flags=re.S)
wr(p,s)

p='data/works.json'; arr=json.loads(rd(p)); item=next(x for x in arr if x.get('id')=='naam')
item.update(tamil_transcription='complete-verified',tamil_first_pass_complete=True,tamil_transcription_draft_pages=0,
            tamil_transcription_verified_pages=67,tamil_transcription_review_pages=0,tamil_fidelity_audit='complete',
            canonical_range_fidelity_audit_complete=True,total_canonical_pages=67,total_verified_pages=67,total_review_pages=0,
            historical_glyph_checked_pages=67,historical_glyph_final_verified_pages=67,open_source_uncertainties=0,
            canonical_closure_audit='works/naam/notes/canonical-closure-user-manual.md',next_action=NEXT)
item['manual_source_verdicts']=[
    {'pdf_page':5,'reading':'அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.'},
    {'pdf_page':10,'reading':'நீ இங்கே வேலை பார்க்கிற வரைக்கும்'},
    {'pdf_page':24,'reading':'கெளரவம் தேடி'}]
sd=item.setdefault('structured_derivatives',{})
sd.update(scene_index='not-started',scene_records=0,scene_text_derivatives='not-started',scene_text_files_completed=0,next_structured_derivative='scene-text-derivatives')
wr(p,json.dumps(arr,ensure_ascii=False,separators=(',',':'))+'\n')

p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=one(s,'- **Naam / நாம்** — active work; first pass **67/67 COMPLETE**; dual-gate **64/67**; visual **64/67**; glyph-final **67/67 COMPLETE**; source holds PDF 5 / PDF 10 / PDF 24; downstream blocked.',
      '- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; visual / glyph-final / dual-gate **67/67 / 67/67 / 67/67**; open source uncertainties **0**; scene derivatives next.')
sec=f'''## 8. Naam active checkpoint\n\nWork: `works/naam/`  \nSource: `TVA_BOK_0064201_நாம்.pdf`\n\n- intake / map / first pass: **complete / verified / 67/67 COMPLETE**;\n- canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- visual-fidelity / historical-glyph final / dual-gate: **67/67 / 67/67 / 67/67**;\n- open source uncertainties: **0**;\n- user manual source verdicts: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;\n- final audit: `works/naam/notes/canonical-closure-user-manual.md`;\n- scene derivatives: **not-started / ready**; English remains downstream.\n\n**Exact next activity:** {NEXT}\n\n'''
s=sub1(s,r'## 8\. Naam active checkpoint\n.*?(?=## 9\. Ammayappan closed checkpoint)',sec,flags=re.S)
wr(p,s)

p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
s=sub1(s,r'\*\*PASS for the current repository-wide checkpoint\.\*\* Ammayappan remains complete-verified\. \*\*Naam / நாம்\*\* has first pass \*\*67/67 COMPLETE\*\*, dual-gate verification \*\*64/67\*\*, visual-fidelity \*\*64/67\*\*, historical-glyph final \*\*67/67 COMPLETE\*\*, and \*\*3 source-obscuration holds\*\* \(PDF 5, PDF 10, PDF 24\)\. PDF 70–71 is fully verified and adds no uncertainty\.',
       '**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** now has canonical Tamil **67/67 COMPLETE-VERIFIED**, visual-fidelity **67/67 PASS**, historical-glyph final **67/67 COMPLETE**, dual-gate **67/67**, and **0 open source uncertainties** after three user manual controlling-scan verdicts.')
s=sub1(s,r'\| Naam / நாம் \| first pass 67/67 COMPLETE; dual-gate 64/67; 3 source holds \| 45 scenes mapped; derivatives blocked \| not-started \| not-started \|',
       '| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | 45 scenes mapped; scene derivatives ready/not-started | not-started | not-started |')
sec=f'''## Naam current checkpoint\n\n- canonical Tamil: **67/67 COMPLETE-VERIFIED**;\n- visual-fidelity / historical-glyph final / dual-gate: **67/67 / 67/67 / 67/67**;\n- open source uncertainties: **0**;\n- manual controlling-scan verdicts: PDF 5 `அவனை தொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`, PDF 10 `நீ இங்கே வேலை பார்க்கிற வரைக்கும்`, PDF 24 `கெளரவம் தேடி`;\n- final audit: `works/naam/notes/canonical-closure-user-manual.md`;\n- structured scene derivatives: **not-started / ready**.\n\n**Next production phase:** {NEXT}\n\n'''
s=sub1(s,r'## Naam current checkpoint\n.*?(?=## Ammayappan current checkpoint)',sec,flags=re.S)
s=sub1(s,r'## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS\. \*\*Naam / நாம்\*\* is active with first pass \*\*67/67 COMPLETE\*\*, dual-gate \*\*64/67\*\*, visual \*\*64/67\*\*, glyph-final \*\*67/67 COMPLETE\*\*, and source holds on PDF 5, PDF 10 and PDF 24\. Next activity: targeted hold resolution for those three pages\.',
       '## Conclusion\n\nAmmayappan remains closed through Reading Room payload QA PASS. **Naam / நாம்** now has canonical Tamil **67/67 COMPLETE-VERIFIED with 0 open source uncertainties**. The next production phase is scene-text derivative construction for source-numbered காட்சி 1–45 with boundary-ownership QA.')
wr(p,s)

print('CHANGED')
for x in changed: print(x)
