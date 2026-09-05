#!/usr/bin/env python3
from __future__ import annotations
import difflib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; WORK=ROOT/'works'/'ammaiyappan'
MAN=WORK/'notes'/'dual-gate-sync-pdf-105-109.json'; REP=WORK/'notes'/'dual-gate-sync-report-pdf-105-109.json'
CAN=WORK/'transcription'/'full-text.md'; PROV=WORK/'transcription'/'parts'/'pdf-105-109.md'; NOTES=WORK/'notes'/'textual-notes-pdf-105-109.md'
A=re.compile(r'<!--\s*source:\s*pdf=(\d+)\b[^>]*-->')
def logical(s): return ''.join(c for c in s if not c.isspace())
def imap(s): return [i for i,c in enumerate(s) if not c.isspace()]
def span(t,p):
    aa=list(A.finditer(t))
    for i,m in enumerate(aa):
        if int(m.group(1))==p:return m.start(), aa[i+1].start() if i+1<len(aa) else len(t)
    raise SystemExit(f'missing PDF {p}')
def block(t,p): a,b=span(t,p); return t[a:b]
def ms(raw,needle):
    x,y=logical(raw),logical(needle); mp=imap(raw); out=[]; s=0
    while y:
        q=x.find(y,s)
        if q<0:break
        e=q+len(y); out.append((q,e,mp[q],mp[e-1]+1)); s=e
    return out
def standalone(o,n): return [x for x in o if not any(y[0]<=x[0] and x[1]<=y[1] for y in n)]
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
def replws(raw,old,new):
    ol,nl=logical(old),logical(new)
    if logical(raw)!=ol: raise SystemExit('logical mismatch')
    f=mapper(ol,nl); runs=[]; lc=0; i=0
    while i<len(raw):
        if raw[i].isspace():
            j=i
            while j<len(raw) and raw[j].isspace():j+=1
            runs.append((lc,raw[i:j])); i=j
        else:lc+=1;i+=1
    out=[];last=0
    for pos,ws in runs:
        k=max(last,min(f(pos),len(nl))); out += [nl[last:k],ws]; last=k
    out.append(nl[last:]); return ''.join(out)
def replace_page(t,p,old,new,count,surf):
    a,b=span(t,p); pg=t[a:b]; om=standalone(ms(pg,old),ms(pg,new)); nm=ms(pg,new)
    if not om and len(nm)>=count:return t,0,'already-synchronized'
    if len(om)!=count: raise SystemExit(f'PDF {p} {surf}: expected {count} {old!r}, found {len(om)}; new={len(nm)}')
    for m in reversed(om): pg=pg[:m[2]]+replws(pg[m[2]:m[3]],old,new)+pg[m[3]:]
    if standalone(ms(pg,old),ms(pg,new)): raise SystemExit(f'PDF {p} {surf}: old remains')
    return t[:a]+pg+t[b:],count,'synchronized'
def mark(t,p):
    a,b=span(t,p); pg=t[a:b]; m=A.search(pg); s=m.group(0)
    if 'status=verified' in s:return t
    if 'status=draft' not in s: raise SystemExit(f'PDF {p}: unexpected anchor')
    pg=pg[:m.start()]+s.replace('status=draft','status=verified',1)+pg[m.end():]
    return t[:a]+pg+t[b:]
def comp(t,p):
    pg=block(t,p); m=A.search(pg); return logical(pg[m.end():])
def main():
    mf=json.loads(MAN.read_text(encoding='utf-8'))
    if mf.get('pdf_range')!=[105,109]:raise SystemExit('wrong manifest')
    orig={CAN:CAN.read_text(encoding='utf-8'),PROV:PROV.read_text(encoding='utf-8')}; work=dict(orig); pages=[]; total=0
    for p in mf['pages']:
        rr={'pdf':p['pdf'],'printed':p['printed'],'replacements':[]}
        for r in p['replacements']:
            cnt=int(r.get('occurrences',1)); entry={'from':r['from'],'to':r['to'],'basis':r['basis'],'occurrences':cnt,'targets':[]}
            for path,surf in ((CAN,'canonical'),(PROV,'provenance')):
                work[path],ap,st=replace_page(work[path],p['pdf'],r['from'],r['to'],cnt,surf); total+=ap
                entry['targets'].append({'surface':surf,'status':st,'applied':ap})
            rr['replacements'].append(entry)
        pages.append(rr)
    for p in range(105,110):
        work[CAN]=mark(work[CAN],p); work[PROV]=mark(work[PROV],p)
        for path,surf in ((CAN,'canonical'),(PROV,'provenance')):
            pg=block(work[path],p)
            if '⟦' in pg or '⟧' in pg:raise SystemExit(f'PDF {p} {surf}: unresolved marker')
        if comp(work[CAN],p)!=comp(work[PROV],p):raise SystemExit(f'PDF {p}: canonical/provenance mismatch')
    changed=[]
    for path,val in work.items():
        if val!=orig[path]:path.write_text(val,encoding='utf-8');changed.append(str(path.relative_to(ROOT)))
    resolved='\n'.join(f"- **{k}:** `{v}`" for k,v in mf['resolved_markers'].items())
    NOTES.write_text(f'''# அம்மையப்பன் — resolved uncertainty supplement — PDF 105–109\n\nControlling source: `TVA_BOK_0064230_அம்மையப்பன்.pdf`\n\nStatus: **CLOSED / dual-gate verified**. Markers **115–116** were adjudicated from enlarged rendered-scan evidence. The user-reviewed PDF 107 heading remains `தூக்குமேடை`; rejected `தாக்குமேடை` remains absent.\n\nResolved readings:\n\n{resolved}\n\nNo `⟦…⟧` uncertainty marker remains in PDF 105–109. PDF 109 / printed p.107 closes the canonical screenplay/dialogue range.\n''',encoding='utf-8');changed.append(str(NOTES.relative_to(ROOT)))
    rep={'work_id':'ammaiyappan','source':mf['source'],'status':'complete-pass','pdf_range':[105,109],'printed_range':[103,107],'pages_verified':5,'page_scoped':True,'global_replacement_used':False,'source_whitespace_preserved_around_replacements':True,'uncertainty_markers_remaining_in_range':0,'canonical_provenance_page_match':'PASS','logical_replacements_applied_across_surfaces':total,'changed_files':changed,'resolved_markers':mf['resolved_markers'],'pages':pages,'canonical_tamil_dual_gate_complete':True,'next_pdf_page':None,'next_printed_page':None,'next_action':'Synchronize all repository status mirrors to 105/105 dual-gate verified, then begin the next unblocked structured-derivative phase per project workflow.'}
    REP.write_text(json.dumps(rep,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'complete-pass','pages_verified':5,'applied':total,'canonical_tamil_dual_gate_complete':True},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
