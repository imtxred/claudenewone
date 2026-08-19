# -*- coding: utf-8 -*-
import re, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-claudenewone/6edf4558-aa97-5f8e-8789-ca34ac607d70/BG')
from content_bg import BG

SRC = '/root/.claude/uploads/6edf4558-aa97-5f8e-8789-ca34ac607d70/88693793-RSveter.html'
DST = '/tmp/claude-0/-home-user-claudenewone/6edf4558-aa97-5f8e-8789-ca34ac607d70/BG/BG_veterinar_bg.html'

t = open(SRC, encoding='utf-8').read()

def spans(txt):
    return [(m.start(), m.end()) for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>', txt, flags=re.S | re.I)]

def walk(txt):
    sp = spans(txt); idx = 0
    for m in re.finditer(r'>([^<>]+)<', txt):
        s = m.start(1)
        if any(a <= s < b for a, b in sp): continue
        if not m.group(1).strip(): continue
        yield idx, m; idx += 1

CYR = re.compile(r'[Ѐ-ӿ]')
nodes = {i: m.group(1) for i, m in walk(t)}
missing = [i for i, v in nodes.items() if CYR.search(v) and i not in BG]
assert not missing, ('nodes with cyrillic not translated', missing, [nodes[i][:60] for i in missing])
extra = [i for i in BG if i not in nodes]
assert not extra, ('dict indices not present', extra)
kept = sorted(i for i in nodes if i not in BG)
print('kept as-is:', [(i, nodes[i].strip()[:30]) for i in kept])

out = []; last = 0; used = set()
for idx, m in walk(t):
    if idx in BG:
        orig = m.group(1)
        lead = re.match(r'\s*', orig).group(0)
        trail = re.search(r'\s*$', orig).group(0)
        out.append(t[last:m.start(1)])
        out.append(lead + BG[idx] + trail)
        last = m.end(1); used.add(idx)
out.append(t[last:])
res = ''.join(out)
assert used == set(BG), ('unused', set(BG) - used)

# attributes
attrs = [('Ваше име', 'Вашето име'), ('Ваш број телефона', 'Вашият телефонен номер'),
         ('Ваш коментар', 'Вашият коментар')]
for a, b in attrs:
    n = res.count('"%s"' % a)
    assert n >= 1, ('attr not found', a)
    res = res.replace('"%s"' % a, '"%s"' % b)

# lang
res = res.replace('<html lang="RS"', '<html lang="bg"', 1)
assert 'lang="bg"' in res

open(DST, 'w', encoding='utf-8').write(res)

# ---------- verification ----------
def stat(txt, label):
    n = len(list(walk(txt)))
    tags = len(re.findall(r'<(?:div|p|h1|h2|h3|li|ul|ol|figure|figcaption|table|tr|td|form|input|button|span|img|font|b|center|strong)\b', txt))
    print(label, 'nodes=%d tags=%d' % (n, tags))
    return n, tags

a = stat(t, 'SRC'); b = stat(res, 'DST')
assert a == b, (a, b)

# script / style blocks byte-identical
sa = re.findall(r'<(script|style)[^>]*>.*?</\1>', t, flags=re.S | re.I)
sb = re.findall(r'<(script|style)[^>]*>.*?</\1>', res, flags=re.S | re.I)
ta = [m.group(0) for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>', t, flags=re.S | re.I)]
tb = [m.group(0) for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>', res, flags=re.S | re.I)]
assert ta == tb, 'script/style changed'
print('script/style blocks identical:', len(ta))

# inline styles identical
ia = re.findall(r'style="[^"]*"', t); ib = re.findall(r'style="[^"]*"', res)
assert ia == ib, 'inline styles changed'
print('inline style attrs identical:', len(ia))

# colour tokens identical
ca = re.findall(r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)', t)
cb = re.findall(r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)', res)
assert ca == cb, 'colour tokens changed'
print('colour tokens identical:', len(ca))

# percent literals survive
for lit in ('100%', '50%'):
    print(lit, t.count(lit), '->', res.count(lit))

# leftover serbian-only letters
srb = sorted(set(re.findall(r'[ђјљњћџЂЈЉЊЋЏ]', res)))
print('serbian-only letters left:', srb)
# leftover russian-only letters
rus = sorted(set(re.findall(r'[ыэёЫЭЁ]', res)))
print('russian-only letters left:', rus)
print('product name count:', res.count('Nautubone'), 'src:', t.count('Nautubone'))
print('OK ->', DST)
