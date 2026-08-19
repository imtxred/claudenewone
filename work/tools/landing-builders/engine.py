import re
SRC='/root/.claude/uploads/6edf4558-aa97-5f8e-8789-ca34ac607d70/eb4d5c81-RStrav.html'

def spans(t):
    return [(m.start(),m.end()) for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>',t,flags=re.S|re.I)]

def walk(t):
    """yield (idx, match) for every text node outside script/style"""
    sp=spans(t); idx=0
    for m in re.finditer(r'>([^<>]+)<', t):
        s=m.start(1)
        if any(a<=s<b for a,b in sp): continue
        if not m.group(1).strip(): continue
        yield idx,m; idx+=1

def apply(t, repl):
    out=[]; last=0; used=set()
    for idx,m in walk(t):
        if idx in repl:
            out.append(t[last:m.start(1)]); out.append(repl[idx])
            last=m.end(1); used.add(idx)
    out.append(t[last:])
    missing=set(repl)-used
    assert not missing, ('unused indices', sorted(missing))
    return ''.join(out)
