#!/usr/bin/env python3
import json,re
from pathlib import Path

R=Path(__file__).resolve().parents[3]

OLD_NEXT=("Perform a targeted source-obscuration hold-resolution audit for PDF 5, PDF 10 and PDF 24 using only the controlling scan at enlarged/native resolution. "
"Do not reconstruct missing or obscured text from grammar, OCR, film audio, subtitles, another edition, web text or memory. "
"Re-evaluate each hold separately; if the controlling pixels still do not expose the characters, retain the hold and document the unreadable span explicitly. "
"Do not start structured derivatives or English until the canonical Tamil gate is fully verified or a deliberate documented hold-policy decision is made.")

NEW_NEXT=("Make a deliberate documented hold-policy decision for the three irrecoverable source-obscuration lacunae on PDF 5, PDF 10 and PDF 24. "
"Do not invent or restore any missing text. Decide whether the canonical Tamil layer may be closed as source-faithful VERIFIED-WITH-LACUNAE, with the three explicit unreadable spans permanently preserved, "
"or whether the work must remain verification-in-progress until a better witness is supplied. Do not start structured derivatives or English until that policy decision is recorded and propagated.")

changed=[]
def rd(p): return (R/p).read_text(encoding='utf-8')
def wr(p,s):
    q=R/p
    old=q.read_text(encoding='utf-8') if q.exists() else ''
    if old!=s:
        q.parent.mkdir(parents=True,exist_ok=True)
        q.write_text(s,encoding='utf-8')
        changed.append(p)
def replace_once(s,a,b,required=True):
    if a not in s:
        if required: raise SystemExit("missing expected text: "+a[:120])
        return s
    return s.replace(a,b,1)

# 1) Canonical hold pages: preserve lacunae; correct one newly re-read visible word on PDF 5.
p='works/naam/transcription/parts/pdf-005-009.md'
s=rd(p)
s=replace_once(s,'ஒன்றியின வேண்டுகோள்படி அவன் வெளியூர் புறப்பட்டான்.','அன்னையின் வேண்டுகோள்படி அவன் வெளியூர் புறப்பட்டான்.')
if '## Source-obscuration re-audit — PDF 5' not in s:
    s += '''\n\n## Source-obscuration re-audit — PDF 5

- Enlarged/native controlling pixels were re-inspected after all normal-range verification closed.
- The physical loss at the left beginning of the introductory line still removes the missing leading character(s). The source directly exposes only the surviving ending before `கொலைத்துவிட சில துரோகிகள் கிளம்பினர்.`; the missing prefix is **not reconstructed**.
- A separate visible-text correction was made from direct pixels: `ஒன்றியின வேண்டுகோள்படி` → **`அன்னையின் வேண்டுகோள்படி`**.
- Result: **HOLD RETAINED** for the lost beginning only; historical-glyph final status remains PASS.
'''
wr(p,s)

p='works/naam/transcription/parts/pdf-010-014.md'
s=rd(p)
if '## Source-obscuration re-audit — PDF 10' not in s:
    s += '''\n\n## Source-obscuration re-audit — PDF 10

- Enlarged/native controlling pixels confirm physical right-edge loss in Malaiyappan's line after visible `நீ இங்கே வேலை பார்க்கிற வரைக்…`.
- The missing continuation/word ending is outside the surviving paper image and cannot be positively read from this witness.
- No grammar-, context-, OCR-, film-, subtitle-, web- or later-edition completion is inserted.
- Result: **HOLD RETAINED**; historical-glyph final status remains PASS.
'''
wr(p,s)

p='works/naam/transcription/parts/pdf-020-024.md'
s=rd(p)
if '## Source-obscuration re-audit — PDF 24' not in s:
    s += '''\n\n## Source-obscuration re-audit — PDF 24

- Enlarged/native controlling pixels confirm that a later dark ink/mark sits directly over the printed cluster immediately after visible `கெளரவம் தே` in `காட்சி 11`.
- The covered character(s) are not positively recoverable from the controlling scan. The canonical lacuna between visible `தே` and following `இருப்பது` therefore remains explicit.
- In particular, **`தேடி` is not restored** from context or the following dialogue.
- Result: **HOLD RETAINED**; historical-glyph final status remains PASS.
'''
wr(p,s)

# 2) Durable audit.
audit='''# நாம் — targeted source-obscuration hold-resolution audit — PDF 5 / 10 / 24

Source: `TVA_BOK_0064201_நாம்.pdf`  
Mode: **controlling-scan-only, enlarged/native-resolution reinspection**  
Result: **3/3 holds re-inspected; 0 resolved; 3 retained**.

No OCR, grammar, semantic expectation, film audio, subtitles, another edition, web text or memory is textual authority for the missing/covered characters.

## PDF 5 — RETAINED HOLD

Physical damage removes the left beginning of the introductory line under `காட்சி 1`. The surviving scan does not expose enough pixels to restore the missing leading character(s), so the canonical explicit lacuna remains. The visible continuation through `கொலைத்துவிட சில துரோகிகள் கிளம்பினர்.` is retained exactly as directly readable.

The same enlarged reinspection produced one independent **visible-text correction** on the next line:

- first-pass `ஒன்றியின வேண்டுகோள்படி` → source-visible **`அன்னையின் வேண்டுகோள்படி`**.

This correction does not resolve the physical lacuna.

## PDF 10 — RETAINED HOLD

The page's physical right edge is missing in Malaiyappan's speech. The surviving scan directly reaches `நீ இங்கே வேலை பார்க்கிற வரைக்…`; the missing continuation/word ending is not present in the surviving paper image. It is therefore left unresolved rather than completed from syntax or context.

## PDF 24 — RETAINED HOLD

A later dark ink/mark overlays the printed cluster immediately after visible `கெளரவம் தே` in `காட்சி 11`. Enlarged inspection does not expose a complete recoverable printed character under the mark. The following visible text `இருப்பது` remains separate. No contextual restoration such as `தேடி` is accepted without a better source witness.

## Gate result

| PDF | Source-visible text | Historical glyph final | Obscuration status | Canonical page status |
|---:|---|---|---|---|
| 5 | PASS after visible correction | PASS | physical loss unresolved | HOLD / needs-review |
| 10 | PASS for surviving text | PASS | right-edge loss unresolved | HOLD / needs-review |
| 24 | PASS for surviving text | PASS | ink/mark coverage unresolved | HOLD / needs-review |

Repository checkpoint remains:

- first pass: **67/67 COMPLETE**;
- historical-glyph final: **67/67 COMPLETE**;
- visual-fidelity / dual-gate fully verified pages: **64/67**;
- unresolved source-obscuration holds: **3** — PDF 5, PDF 10, PDF 24;
- structured derivatives / English: **blocked**.

## Next activity

'''+NEW_NEXT+'\n'
wr('works/naam/notes/source-obscuration-hold-resolution.md',audit)

# 3) Index.
p='works/naam/transcription/index.json'
d=json.loads(rd(p))
assert (d['verified_pages'],d['visual_fidelity_passed_pages'],d['historical_glyph_verified_pages'],d['open_uncertainty_markers'])==(64,64,67,3)
d['hold_resolution_audit']='../notes/source-obscuration-hold-resolution.md'
d['hold_resolution_status']='completed-3-retained'
d['next_action']=NEW_NEXT
wr(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# 4) Metadata.
p='works/naam/metadata.yaml'
s=rd(p)
s=replace_once(s,'  current_audit_path: "notes/verification-audit-pdf-070-071.md"','  current_audit_path: "notes/source-obscuration-hold-resolution.md"\n  hold_resolution_audit_path: "notes/source-obscuration-hold-resolution.md"\n  hold_resolution_status: completed-3-retained')
s=replace_once(s,'  next_pdf_range: "5,10,24"','  next_pdf_range: null')
s=re.sub(r'next_action: ".*?"\s*$',f'next_action: "{NEW_NEXT}"',s,count=1,flags=re.S)
wr(p,s)

# 5) Historical glyph audit.
p='works/naam/notes/historical-glyph-audit.md'
s=rd(p)
if '## Source-obscuration hold-resolution audit' not in s:
    s += '''\n\n## Source-obscuration hold-resolution audit

The targeted re-audit of PDF 5, PDF 10 and PDF 24 leaves all three source-obscuration holds unresolved. These are **not historical-glyph failures**: the historical-glyph gate remains **67/67 COMPLETE / final-verified**. The remaining block is source visibility / physical witness completeness only. See `source-obscuration-hold-resolution.md`.
'''
wr(p,s)

# 6) Work README.
p='works/naam/README.md'
s=rd(p)
s=replace_once(s,'**Next:** targeted hold-resolution for PDF 5, PDF 10 and PDF 24.',
'''## Source-obscuration hold-resolution audit — PDF 5 / 10 / 24

- **3/3 re-inspected; 0 resolved; 3 retained**;
- PDF 5 remains a physical-loss hold; direct source reinspection corrected `ஒன்றியின வேண்டுகோள்படி` → `அன்னையின் வேண்டுகோள்படி`;
- PDF 10 remains a physical right-edge-loss hold after visible `வரைக்…`;
- PDF 24 remains an ink/mark-obscuration hold after visible `கெளரவம் தே`;
- detailed audit: `notes/source-obscuration-hold-resolution.md`;
- counters remain visual/dual **64/67**, glyph-final **67/67 COMPLETE**, open holds **3**.

**Next:** deliberate documented hold-policy decision for these three irrecoverable lacunae.''')
s=replace_once(s,OLD_NEXT,NEW_NEXT)
wr(p,s)

# 7) Transcription README.
p='works/naam/transcription/README.md'
s=rd(p)
s=s.replace('- current first-pass status: **complete / verification pending**;','- current first-pass status: **complete; normal-range verification complete; source-lacuna policy pending**;',1)
s=s.replace('- separate visual-fidelity audit: **in progress — 64/67 passed; 3 source holds remain**;','- separate visual-fidelity audit: **64/67 passed; 3 source holds retained after targeted enlarged-source re-audit**;',1)
if '## Targeted source-obscuration hold-resolution audit' not in s:
    s += '''\n\n## Targeted source-obscuration hold-resolution audit

PDF 5, PDF 10 and PDF 24 were separately re-inspected at enlarged/native resolution using only the controlling scan. **0/3 holds resolved; 3/3 retained.** PDF 5 also received one source-visible correction: `ஒன்றியின வேண்டுகோள்படி` → `அன்னையின் வேண்டுகோள்படி`. PDF 10's right-edge continuation and PDF 24's post-`தே` covered cluster remain unreadable and are not reconstructed. See `../notes/source-obscuration-hold-resolution.md`.

**Next:** '''+NEW_NEXT+'\n'
else:
    s=s.replace(OLD_NEXT,NEW_NEXT)
wr(p,s)

# 8) Project handover.
p='works/naam/PROJECT_HANDOVER.md'
s=rd(p)
if 'source-obscuration-hold-resolution.md' not in s:
    s += '''\n\n## Source-obscuration hold-resolution checkpoint

- targeted re-audit: **COMPLETE — 3/3 reinspected, 0 resolved, 3 retained**;
- retained holds: PDF 5 physical left-start loss; PDF 10 physical right-edge loss; PDF 24 dark ink/mark over the post-`தே` printed cluster;
- PDF 5 visible correction: `ஒன்றியின வேண்டுகோள்படி` → `அன்னையின் வேண்டுகோள்படி`;
- audit: `notes/source-obscuration-hold-resolution.md`;
- counters unchanged: visual/dual **64/67**; glyph-final **67/67 COMPLETE**; open holds **3**;
- derivatives / English remain blocked.

## Exact next activity

> **'''+NEW_NEXT+'''**
'''
else:
    s=s.replace(OLD_NEXT,NEW_NEXT)
wr(p,s)

# 9) Next-chat prompt.
wr('works/naam/NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.

Current durable checkpoint: first pass **67/67 COMPLETE**; visual-fidelity **64/67**; historical-glyph final **67/67 COMPLETE**; dual-gate verified **64/67** (PDF 6–9, PDF 11–23, PDF 25–71). The targeted enlarged/native source-obscuration re-audit is **COMPLETE: 3/3 reinspected, 0 resolved, 3 retained** — PDF 5 physical left-start loss, PDF 10 physical right-edge loss, PDF 24 post-`தே` ink/mark coverage.

PDF 5 additionally has a direct visible-text correction: `ஒன்றியின வேண்டுகோள்படி` → **`அன்னையின் வேண்டுகோள்படி`**. Do not restore the missing PDF 5 prefix, the PDF 10 continuation after visible `வரைக்…`, or PDF 24 as `தேடி` without a better witness.

Controlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.

Latest audit: `works/naam/notes/source-obscuration-hold-resolution.md`.

Structured derivatives and English remain blocked.

## Exact next activity

> **{NEW_NEXT}**
''')

# 10) data/works.json.
p='data/works.json'
x=json.loads(rd(p))
n=next(q for q in x if q.get('id')=='naam')
n['canonical_tamil_current_verification_path']='works/naam/notes/source-obscuration-hold-resolution.md'
n['canonical_tamil_hold_resolution']='completed-3-retained'
n['next_action']=NEW_NEXT
wr(p,json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')

# 11) Repo-wide mirrors.
for p in ['README.md','docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md','docs/STATUS_CONSISTENCY_AUDIT.md']:
    s=rd(p)
    s=s.replace(OLD_NEXT,NEW_NEXT)
    if p=='README.md' and 'source-obscuration-hold-resolution.md' not in s:
        anchor='- structured derivatives / English remain blocked pending verified Tamil.'
        if anchor in s:
            s=s.replace(anchor,anchor+'\n- targeted source-obscuration re-audit: **3/3 retained**; audit `works/naam/notes/source-obscuration-hold-resolution.md`.',1)
    if p=='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md' and 'source-obscuration-hold-resolution.md' not in s:
        anchor='- structured derivatives / English / reader remain blocked.'
        if anchor in s:
            s=s.replace(anchor,anchor+'\n- targeted source-obscuration re-audit: **3/3 retained**; audit `works/naam/notes/source-obscuration-hold-resolution.md`.',1)
    if p=='docs/STATUS_CONSISTENCY_AUDIT.md' and 'source-obscuration-hold-resolution.md' not in s:
        anchor='- downstream layers remain blocked.'
        if anchor in s:
            s=s.replace(anchor,anchor+'\n- targeted source-obscuration re-audit: **3/3 retained**; audit `works/naam/notes/source-obscuration-hold-resolution.md`.',1)
    wr(p,s)

print('\n'.join(changed))
