#!/usr/bin/env python3
import hashlib, json, re
from pathlib import Path

R = Path(__file__).resolve().parents[3]
W = R / 'works' / 'naam'
PARTS = W / 'transcription' / 'parts'
SCENES = W / 'scenes'

EXPECTED_STARTS = {
    1:5, 2:7, 3:8, 4:11, 5:13, 6:14, 7:16, 8:17, 9:19, 10:21,
    11:24, 12:25, 13:25, 14:29, 15:31, 16:31, 17:32, 18:33, 19:34, 20:34,
    21:35, 22:36, 23:38, 24:38, 25:42, 26:42, 27:43, 28:45, 29:45, 30:47,
    31:49, 32:52, 33:54, 34:56, 35:58, 36:58, 37:60, 38:60, 39:62, 40:65,
    41:65, 42:67, 43:67, 44:68, 45:68,
}
SOURCE_RE = re.compile(r'<!--\s*source:\s*pdf=(\d+)(?:\s+printed=([^\s>]+))?[^>]*-->')
SCENE_RE = re.compile(r'^##\s+காட்சி\s*-?\s*(\d+)[\.,]?\s*$', re.M)
PART_RE = re.compile(r'^pdf-(\d{3})-(\d{3})\.md$')
PHASE5 = ('Begin Phase 5 scene-text derivatives from the fully verified canonical Tamil. '
          'Create one derivative for each source-numbered காட்சி 1–45 in source order, preserve exact source headings, page provenance and cross-page/cross-part continuity, '
          'and run scene-boundary ownership QA before proceeding to the dialogue index. Do not alter canonical Tamil except for later source-supported corrections.')
NEXT = ('Begin Phase 6 dialogue indexing from the 45/45 complete-verified scene derivatives. Inventory every explicit source speaker label exactly as printed, '
        'create immutable dialogue records in scene/source order with PDF provenance, keep cross-page labelled utterances as one logical record, leave source-unlabelled speech unlabelled, '
        'and run whole-work dialogue coverage QA before starting the character/entity index. Do not alter canonical Tamil or scene text except for later source-supported corrections.')

changed = []
def rd(path):
    return (R / path).read_text(encoding='utf-8')
def wr(path, text):
    p = R / path
    old = p.read_text(encoding='utf-8') if p.exists() else None
    if old != text:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
        changed.append(path)
def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
def canonical_part_text(p):
    s = p.read_text(encoding='utf-8')
    m = re.search(r'\n---\s*\n', s)
    if m:
        s = s[:m.start()]
    first = s.find('<!-- source:')
    if first < 0:
        raise SystemExit(f'No source anchor in {p}')
    return s[first:].rstrip() + '\n'

idx = json.loads(rd('works/naam/transcription/index.json'))
assert idx['status'] == 'complete-verified', idx['status']
assert idx['verified_pages'] == 67 and idx['open_uncertainty_markers'] == 0

part_files = []
for p in PARTS.iterdir():
    m = PART_RE.match(p.name)
    if m:
        part_files.append((int(m.group(1)), p))
part_files.sort()
assert len(part_files) == 14, len(part_files)
corpus = '\n'.join(canonical_part_text(p) for _, p in part_files)

matches = list(SCENE_RE.finditer(corpus))
nums = [int(m.group(1)) for m in matches]
assert nums == list(range(1, 46)), nums
first_scene_pos = matches[0].start()
canonical_scene_region = corpus[first_scene_pos:]

records = []
raw_spans = []
page_union = set()
for i, m in enumerate(matches):
    n = int(m.group(1))
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(corpus)
    raw = corpus[start:end]
    raw_spans.append(raw)

    prior_anchors = list(SOURCE_RE.finditer(corpus, 0, start))
    if not prior_anchors:
        raise SystemExit(f'No preceding source anchor for scene {n}')
    a0 = prior_anchors[-1]
    start_pdf = int(a0.group(1))
    printed_token = a0.group(2)
    start_printed = int(printed_token) if printed_token and printed_token.isdigit() else None
    if start_pdf != EXPECTED_STARTS[n]:
        raise SystemExit(f'Scene {n} start mismatch: {start_pdf} != {EXPECTED_STARTS[n]}')

    inside = list(SOURCE_RE.finditer(raw))
    anchor_pages = [start_pdf] + [int(a.group(1)) for a in inside]
    end_pdf = max(anchor_pages)
    pdf_pages = list(range(start_pdf, end_pdf + 1))
    page_union.update(pdf_pages)
    end_printed = None if end_pdf == 5 else end_pdf

    scene_id = f'naam-s{n:03d}'
    filename = f'scene-{n:03d}.md'
    span_hash = sha(raw)
    heading_exact = m.group(0).removeprefix('##').strip()
    next_scene = f'naam-s{n+1:03d}' if n < 45 else None
    provenance = (
        f'<!-- derivative provenance: work=naam scene_id={scene_id} ordinal={n} source_scene_number={n} '
        f'start_pdf={start_pdf} start_printed={start_printed if start_printed is not None else "none"} end_pdf={end_pdf} '
        f'end_before={next_scene if next_scene else "end-of-screenplay"} -->\n'
        f'<!-- derivative span_sha256={span_hash} -->\n'
        '<!-- derivative rule: source-numbered scene copied from complete-verified canonical Tamil; source wording and heading are not normalized. -->\n'
    )
    scene_text = provenance + a0.group(0) + '\n\n' + raw.lstrip('\n')
    wr(f'works/naam/scenes/{filename}', scene_text)
    records.append({
        'scene_id': scene_id,
        'ordinal': n,
        'source_scene_number': n,
        'heading': heading_exact,
        'start_pdf': start_pdf,
        'start_printed': start_printed,
        'end_pdf': end_pdf,
        'end_printed': end_printed,
        'pdf_pages': pdf_pages,
        'end_before_scene_id': next_scene,
        'span_sha256': span_hash,
        'file': filename,
        'status': 'verified-derivative',
    })

joined = ''.join(raw_spans)
assert joined == canonical_scene_region
assert page_union == set(range(5,72)), sorted(set(range(5,72))-page_union)
body_hash = sha(canonical_scene_region)
assert body_hash == sha(joined)
cross_page = sum(1 for r in records if r['end_pdf'] > r['start_pdf'])
same_page_multi_start = len(records) - len(set(r['start_pdf'] for r in records))

index = {
    'work_id': 'naam',
    'status': 'complete-verified',
    'source_numbered_scenes': True,
    'source_scene_count': 45,
    'source_scene_number_range': [1,45],
    'canonical_tamil_gate': '67/67-dual-gate-complete-verified',
    'boundary_ownership_qa': '../notes/scene-boundary-ownership-qa.md',
    'canonical_scene_region_sha256': body_hash,
    'joined_scene_spans_sha256': sha(joined),
    'unique_pdf_pages_represented': len(page_union),
    'cross_page_scene_count': cross_page,
    'same_page_additional_scene_starts': same_page_multi_start,
    'scene_records': records,
    'next_action': NEXT,
}
wr('works/naam/scenes/index.json', json.dumps(index, ensure_ascii=False, indent=2) + '\n')

readme = f'''# நாம் — Scene-text derivatives

Status: **COMPLETE-VERIFIED — 45/45 source-numbered scenes**  
Canonical authority: `../transcription/` — **67/67 complete-verified**  
Boundary ownership QA: `../notes/scene-boundary-ownership-qa.md` — **PASS**

These files are derivatives of the verified canonical Tamil, not independent textual authorities. The source prints **காட்சி 1–45** sequentially, so derivative ordinals and source scene numbers are identical. Exact source heading forms such as `காட்சி-10.` and `காட்சி 30,` remain unchanged inside the scene files.

## Integrity

- scene files: **45/45** (`scene-001.md` … `scene-045.md`);
- source-number sequence: **1–45, no gaps/repeats**;
- canonical PDF pages represented: **67/67 — PDF 5–71**;
- scenes spanning more than one PDF page: **{cross_page}**;
- additional scene starts sharing a PDF page with another scene: **{same_page_multi_start}**;
- canonical scene-region SHA-256: `{body_hash}`;
- joined scene-span SHA-256: `{sha(joined)}` — exact match;
- gaps / overlaps in canonical scene-span ownership: **0 / 0**.

Each scene file prepends derivative provenance and the applicable source-page anchor, then preserves the canonical scene span without wording, punctuation, speaker-label, heading or performance-text normalization.

## Next activity

{NEXT}
'''
wr('works/naam/scenes/README.md', readme)

qa_lines = [
    '# நாம் — Scene boundary ownership QA', '', 'Result: **PASS**', '',
    'The 45 source-numbered scene spans were generated only from the complete-verified canonical Tamil. Scene boundaries are the exact `## காட்சி...` headings already preserved in canonical transcription; no film audio, subtitle, OCR, web text or semantic reconstruction was used.', '',
    '## Whole-work checks', '',
    '- source scene numbers: **1–45 exactly; 0 gaps / 0 repeats / 0 out-of-order**;',
    '- mapping start-PDF check: **45/45 PASS** against `mapping.md`;',
    '- canonical page representation: **PDF 5–71 / 67 unique pages**;',
    f'- cross-page scenes: **{cross_page}**;',
    f'- additional same-page scene starts: **{same_page_multi_start}**;',
    f'- canonical scene-region SHA-256: `{body_hash}`;',
    f'- joined scene-span SHA-256: `{sha(joined)}`;',
    '- joined-span equality: **PASS — exact byte-for-byte equality for the canonical region from `காட்சி 1` through the final screenplay text**;',
    '- source text gaps / overlaps: **0 / 0**;',
    '- canonical Tamil modified by this derivative phase: **0**.', '',
    '## Scene ranges', '', '| Scene | Start PDF | End PDF | File | Status |', '|---:|---:|---:|---|---|'
]
for r in records:
    qa_lines.append(f"| {r['source_scene_number']} | {r['start_pdf']} | {r['end_pdf']} | `{r['file']}` | PASS |")
qa_lines += ['', '## Gate result', '', '**Scene-text derivative phase CLOSED / COMPLETE-VERIFIED.** Dialogue indexing may now begin from these derivatives while canonical Tamil remains the upstream authority.', '', '## Next activity', '', NEXT, '']
wr('works/naam/notes/scene-boundary-ownership-qa.md', '\n'.join(qa_lines))

p='works/naam/metadata.yaml'; s=rd(p)
s=s.replace('  scene_derivatives: not-started-ready', '  scene_derivatives: complete-verified-45-of-45')
s=s.replace('  dialogue_index: blocked-pending-scene-derivatives', '  dialogue_index: ready-next')
s=s.replace('  song_authorship_gate: blocked-pending-scene-dialogue-character-layers', '  song_authorship_gate: blocked-pending-dialogue-character-layers')
if '\nstructured_derivatives:\n' not in s:
    block = f'''\nstructured_derivatives:\n  scene_index_path: "scenes/index.json"\n  scene_text_derivatives: complete-verified\n  source_numbered_scene_count: 45\n  scene_text_files_completed: 45\n  boundary_ownership_qa_path: "notes/scene-boundary-ownership-qa.md"\n  boundary_ownership_qa: PASS\n  canonical_scene_region_sha256: "{body_hash}"\n  joined_scene_spans_sha256: "{sha(joined)}"\n  dialogue_index: not-started\n\n'''
    s=s.replace('\nstatus:\n', block+'status:\n',1)
s=re.sub(r'next_action:\s*".*"\s*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False), s, count=1, flags=re.M)
wr(p,s)

p='works/naam/README.md'; s=rd(p)
s=s.replace('- scene derivatives: **not-started / ready**;', '- scene derivatives: **45/45 COMPLETE-VERIFIED; boundary ownership QA PASS**;')
s=s.replace('**Next:** '+PHASE5, '**Next:** '+NEXT)
if '## Scene-text derivative checkpoint' not in s:
    insert=f'''\n## Scene-text derivative checkpoint\n\n- source-numbered scenes: **45/45 COMPLETE-VERIFIED**;\n- exact sequence: **காட்சி 1–45**;\n- canonical PDF representation: **67/67 pages, PDF 5–71**;\n- boundary ownership QA: **PASS — 0 gaps / 0 overlaps**;\n- scene index: `scenes/index.json`;\n- QA: `notes/scene-boundary-ownership-qa.md`;\n- canonical scene-region / joined scene-span SHA-256: `{body_hash}` / `{sha(joined)}` — **MATCH**;\n- canonical Tamil changed by derivative generation: **0**.\n\n**Next:** {NEXT}\n\n'''
    s=s.replace('## Source-visible publication / credit evidence\n', insert+'## Source-visible publication / credit evidence\n',1)
wr(p,s)

p='works/naam/transcription/README.md'; s=rd(p)
s=s.replace(PHASE5,NEXT)
if '## Downstream scene derivative closure' not in s:
    s+=f'''\n\n## Downstream scene derivative closure\n\nScene-text derivatives are now **45/45 COMPLETE-VERIFIED** with boundary ownership QA PASS. Canonical Tamil remains unchanged and authoritative. See `../scenes/index.json` and `../notes/scene-boundary-ownership-qa.md`.\n\n**Next:** {NEXT}\n'''
wr(p,s)

p='works/naam/mapping.md'; s=rd(p)
s=s.replace('Status: **verified structural mapping; canonical Tamil first-pass complete / verification pending**', 'Status: **verified structural mapping; canonical Tamil complete-verified; scene derivatives 45/45 complete-verified**')
s=s.replace('**Begin the separate visual-fidelity and final historical-glyph verification audit with PDF 5–9. Compare every canonical token against enlarged source pixels, preserve source irregularity, and adjudicate the two carried source uncertainties only when direct scan evidence positively supports a reading. Mark a page verified only when both the visual-fidelity and occurrence-specific historical-glyph gates pass; keep any unresolved page/reason explicit. Structured derivatives and English translation remain blocked until verified Tamil.**', '**'+NEXT+'**')
wr(p,s)

p='works/naam/PROJECT_HANDOVER.md'; s=rd(p)
s=s.replace(PHASE5,NEXT)
if '## Scene-text derivative closure checkpoint' not in s:
    s+=f'''\n\n## Scene-text derivative closure checkpoint\n\n- scene derivatives: **45/45 COMPLETE-VERIFIED**;\n- source numbering: **காட்சி 1–45 exact**;\n- page representation: **PDF 5–71 / 67 unique pages**;\n- boundary ownership QA: **PASS — 0 gaps / 0 overlaps**;\n- scene index: `scenes/index.json`;\n- QA: `notes/scene-boundary-ownership-qa.md`;\n- canonical scene-region / joined scene-span SHA-256: `{body_hash}` / `{sha(joined)}` — MATCH;\n- canonical Tamil modifications in this phase: **0**.\n\n## Exact next activity\n\n> **{NEXT}**\n'''
wr(p,s)
wr('works/naam/NEXT_CHAT_PROMPT.md', f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. Live `main` is authoritative.\n\nCanonical Tamil is **COMPLETE-VERIFIED: 67/67 dual-gate, 0 open uncertainties**. Scene-text derivatives are now **45/45 COMPLETE-VERIFIED** for source-numbered **காட்சி 1–45**, with `works/naam/notes/scene-boundary-ownership-qa.md` = **PASS — 0 gaps / 0 overlaps / PDF 5–71 represented**. Canonical Tamil was not changed by scene generation.\n\nScene index: `works/naam/scenes/index.json`.\n\nControlling source: `TVA_BOK_0064201_நாம்.pdf`, 72 pages, SHA-256 `0f7a54882eb6a5a8f83b29060c771ef18dee2b9e108c8797184de2b97c30b7ad`.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

p='data/works.json'; data=json.loads(rd(p)); naam=next(x for x in data if x.get('id')=='naam')
naam['tamil_transcription']='complete-verified'; naam['tamil_first_pass_complete']=True
naam['tamil_transcription_draft_pages']=0; naam['tamil_transcription_verified_pages']=67; naam['tamil_transcription_review_pages']=0
naam['tamil_fidelity_audit']='complete'; naam['canonical_range_fidelity_audit_complete']=True
naam['total_canonical_pages']=67; naam['total_verified_pages']=67; naam['total_review_pages']=0
sd=naam.setdefault('structured_derivatives',{})
sd.update({'scene_index':'complete-verified','scene_index_path':'works/naam/scenes/index.json','source_numbered_scene_records':45,'scene_text_derivatives':'complete-verified','scene_text_files_completed':45,'scene_boundary_ownership_qa':'PASS','scene_boundary_ownership_qa_path':'works/naam/notes/scene-boundary-ownership-qa.md','scene_canonical_region_sha256':body_hash,'scene_joined_spans_sha256':sha(joined),'dialogue_index':'not-started','next_structured_derivative':'dialogue-index'})
naam['next_action']=NEXT
wr(p,json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')

p='README.md'; s=rd(p)
s=s.replace('- scene derivatives: **not-started / ready**;', '- scene derivatives: **45/45 COMPLETE-VERIFIED; boundary ownership QA PASS**;')
s=s.replace('**Next:** '+PHASE5, '**Next:** '+NEXT)
wr(p,s)

p='docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'; s=rd(p)
s=s.replace('- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; visual / glyph-final / dual-gate **67/67 / 67/67 / 67/67**; open source uncertainties **0**; scene derivatives next.', '- **Naam / நாம்** — canonical Tamil **67/67 COMPLETE-VERIFIED**; scene derivatives **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS**; dialogue index next.')
s=s.replace('- scene derivatives: **not-started / ready**; English remains downstream.', '- scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; dialogue index next; English remains downstream.')
s=s.replace('**Exact next activity:** '+PHASE5, '**Exact next activity:** '+NEXT)
wr(p,s)

p='docs/STATUS_CONSISTENCY_AUDIT.md'; s=rd(p)
s=s.replace('| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | 45 scenes mapped; scene derivatives ready/not-started | not-started | not-started |', '| Naam / நாம் | canonical Tamil 67/67 complete-verified; 0 unresolved | **45/45 scene derivatives complete-verified; boundary QA PASS** | dialogue index next | not-started |')
s=s.replace('- structured scene derivatives: **not-started / ready**.', '- structured scene derivatives: **45/45 COMPLETE-VERIFIED**; boundary ownership QA **PASS — 0 gaps / 0 overlaps**; canonical PDF pages represented **67/67**.')
s=s.replace('**Next production phase:** '+PHASE5, '**Next production phase:** '+NEXT)
s=s.replace('**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** now has canonical Tamil **67/67 COMPLETE-VERIFIED**, visual-fidelity **67/67 PASS**, historical-glyph final **67/67 COMPLETE**, dual-gate **67/67**, and **0 open source uncertainties** after three user manual controlling-scan verdicts.', '**PASS for the current repository-wide checkpoint.** Ammayappan remains complete-verified. **Naam / நாம்** has canonical Tamil **67/67 COMPLETE-VERIFIED** and scene-text derivatives **45/45 COMPLETE-VERIFIED** with boundary ownership QA **PASS — 0 gaps / 0 overlaps**. Dialogue indexing is the next gate.')
wr(p,s)

assert len(list(SCENES.glob('scene-*.md'))) == 45
assert json.loads(rd('works/naam/scenes/index.json'))['source_scene_count'] == 45
print(json.dumps({'changed':changed,'scene_count':45,'cross_page_scenes':cross_page,'same_page_additional_starts':same_page_multi_start,'body_sha256':body_hash},ensure_ascii=False,indent=2))
