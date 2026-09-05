#!/usr/bin/env python3
from __future__ import annotations
import difflib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'works'/'ammaiyappan'
MANIFEST=WORK/'notes'/'dual-gate-sync-pdf-095-104.json'
REPORT=WORK/'notes'/'dual-gate-sync-report-pdf-095-104.json'
CANON=WORK/'transcription'/'full-text.md'
PROV=WORK/'transcription'/'parts'/'pdf-095-104.md'
NOTES=WORK/'notes'/'textual-notes-pdf-095-104.md'
ANCHOR=re.compile(r'<!--\s*source:\s*pdf=(\d+)\b[^>]*-->')

def logical(s): return ''.join(c for c in s if not c.isspace())
def imap(s): return [i for i,c in enumerate(s) if not c.isspace()]
def span(text,pdf):
    a=list(ANCHOR.finditer(text))
    for i,m in enumerate(a):
        if int(m.group(1))==pdf:
            return m.start(), a[i+1].start() if i+1<len(a) else len(text)
    raise SystemExit(f'missing PDF {pdf} anchor')
def block(text,pdf):
    a,b=span(text,pdf); return text[a:b]
def matches(raw,needle):
    x,y=logical(raw),logical(needle); mp=imap(raw); out=[]; p=0
    while y:
        q=x.find(y,p)
        if q<0: break
        e=q+len(y); out.append((q,e,mp[q],mp[e-1]+1)); p=e
    return out

def standalone(oldm,newm):
    return [o for o in oldm if not any(n[0]<=o[0] and o[1]<=n[1] for n in newm)]
def mapper(old,new):
    ops=difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes()
    def f(pos):
        if pos<=0:return 0
        if pos>=len(old):return len(new)
        for tag,i1,i2,j1,j2 in ops:
            if i1<=pos<=i2:
                if tag=='equal': return j1+(pos-i1)
                if pos==i1:return j1
                if pos==i2:return j2
                return j1+round((pos-i1)*(j2-j1)/(i2-i1 or 1))
        return len(new)
    return f
def replace_ws(raw,old,new):
    ol,nl=logical(old),logical(new)
    if logical(raw)!=ol: raise SystemExit('logical match failure')
    f=mapper(ol,nl); runs=[]; lc=0; i=0
    while i<len(raw):
        if raw[i].isspace():
            j=i
            while j<len(raw) and raw[j].isspace(): j+=1
            runs.append((lc,raw[i:j])); i=j
        else: lc+=1; i+=1
    out=[]; last=0
    for pos,ws in runs:
        k=max(last,min(f(pos),len(nl))); out += [nl[last:k],ws]; last=k
    out.append(nl[last:]); return ''.join(out)
def replace_page(text,pdf,old,new,count,surface):
    a,b=span(text,pdf); pg=text[a:b]
    om=standalone(matches(pg,old),matches(pg,new)); nm=matches(pg,new)
    if not om and len(nm)>=count:
        return text,0,'already-synchronized'
    if len(om)!=count:
        raise SystemExit(f'PDF {pdf} {surface}: {old!r} expected {count}, found {len(om)} standalone old; new={len(nm)}')
    for m in reversed(om):
        raw=pg[m[2]:m[3]]; rep=replace_ws(raw,old,new); pg=pg[:m[2]]+rep+pg[m[3]:]
    if standalone(matches(pg,old),matches(pg,new)):
        raise SystemExit(f'PDF {pdf} {surface}: old remains after sync: {old!r}')
    return text[:a]+pg+text[b:],count,'synchronized'
def verify_anchor(text,pdf):
    a,b=span(text,pdf); pg=text[a:b]; m=ANCHOR.search(pg)
    s=m.group(0)
    if 'status=verified' in s:return text
    if 'status=draft' not in s: raise SystemExit(f'PDF {pdf}: unexpected anchor {s}')
    pg=pg[:m.start()]+s.replace('status=draft','status=verified',1)+pg[m.end():]
    return text[:a]+pg+text[b:]
def comparable(text,pdf):
    pg=block(text,pdf); m=ANCHOR.search(pg); return logical(pg[m.end():])

def main():
    mf=json.loads(MANIFEST.read_text(encoding='utf-8'))
    if mf.get('pdf_range')!=[95,104]: raise SystemExit('wrong manifest range')
    orig={CANON:CANON.read_text(encoding='utf-8'), PROV:PROV.read_text(encoding='utf-8')}
    work=dict(orig); report_pages=[]; total=0
    for p in mf['pages']:
        pdf=int(p['pdf']); pr={'pdf':pdf,'printed':p['printed'],'replacements':[]}
        for r in p['replacements']:
            cnt=int(r.get('occurrences',1)); rr={'from':r['from'],'to':r['to'],'basis':r['basis'],'occurrences':cnt,'targets':[]}
            for path,surf in ((CANON,'canonical'),(PROV,'provenance')):
                work[path],ap,st=replace_page(work[path],pdf,r['from'],r['to'],cnt,surf)
                total+=ap; rr['targets'].append({'surface':surf,'status':st,'applied':ap})
            pr['replacements'].append(rr)
        report_pages.append(pr)
    for pdf in range(95,105):
        work[CANON]=verify_anchor(work[CANON],pdf); work[PROV]=verify_anchor(work[PROV],pdf)
        for path,surf in ((CANON,'canonical'),(PROV,'provenance')):
            pg=block(work[path],pdf)
            if '⟦' in pg or '⟧' in pg: raise SystemExit(f'PDF {pdf} {surf}: unresolved marker remains')
        if comparable(work[CANON],pdf)!=comparable(work[PROV],pdf): raise SystemExit(f'PDF {pdf}: canonical/provenance mismatch')
    changed=[]
    for path,val in work.items():
        if val!=orig[path]: path.write_text(val,encoding='utf-8'); changed.append(str(path.relative_to(ROOT)))
    resolved='\n'.join(f"- **{k}:** `{v}`" for k,v in mf['resolved_markers'].items())
    NOTES.write_text(f'''# அம்மையப்பன் — resolved uncertainty supplement — PDF 95–104\n\nControlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`\n\nStatus: **CLOSED / dual-gate verified**. Markers **108–114** were adjudicated from enlarged rendered-scan evidence during the combined visual-fidelity + historical-Tamil-glyph pass.\n\nResolved readings:\n\n{resolved}\n\nNo `⟦…⟧` uncertainty marker remains in PDF 95–104. PDF 104 ends inside Muthan's speech and the continuation on PDF 105 remains a provenance boundary, not a paragraph close.\n''',encoding='utf-8')
    changed.append(str(NOTES.relative_to(ROOT)))
    rep={'work_id':'ammaiyappan','source':mf['source'],'status':'complete-pass','pdf_range':[95,104],'printed_range':[93,102],'pages_verified':10,'page_scoped':True,'global_replacement_used':False,'source_whitespace_preserved_around_replacements':True,'uncertainty_markers_remaining_in_range':0,'canonical_provenance_page_match':'PASS','logical_replacements_applied_across_surfaces':total,'changed_files':changed,'resolved_markers':mf['resolved_markers'],'pages':report_pages,'next_pdf_page':105,'next_printed_page':103,'next_action':'Continue at PDF 105 / printed p.103 with visual source-fidelity and historical-Tamil-glyph verification together; preserve the PDF 104→105 speech continuation.'}
    REPORT.write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'complete-pass','pages_verified':10,'applied':total,'changed_files':changed},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
