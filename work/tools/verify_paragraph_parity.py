import re, sys

def load(p):
    t = open(p, encoding='utf-8').read()
    paras = [x.strip() for x in t.split('\n') if x.strip()]
    return t, paras

ru_t, ru = load('storytale_hitna_RU.txt')
sr_t, sr = load('storytale_hitna_RS_sr.txt')

print("=== PARAGRAPH PARITY ===")
print(f"RU: {len(ru)}   SR: {len(sr)}   {'OK' if len(ru)==len(sr) else 'MISMATCH'}")

def words(s): return len(re.findall(r'[^\W\d_]+', s, re.UNICODE))
rw, sw = words(ru_t), words(sr_t)
print(f"\n=== WORDS ===\nRU: {rw}  chars {len(ru_t)}\nSR: {sw}  chars {len(sr_t)}\nratio {sw/rw:.3f}")

print("\n=== RATIO OUTLIERS (<0.6 or >1.9) ===")
bad=0
if len(ru)==len(sr):
    for i,(a,b) in enumerate(zip(ru,sr)):
        wa, wb = words(a), words(b)
        if wa==0: continue
        r = wb/wa
        if r<0.6 or r>1.9:
            bad+=1
            print(f"[{i}] {r:.2f}  RU({wa}): {a[:70]}\n         SR({wb}): {b[:70]}")
print("none" if bad==0 else f"{bad} outliers")

print("\n=== CHARSET ===")
# Russian-only letters that must NOT appear in Serbian Cyrillic
ru_only = set('ёйщыэюяъЁЙЩЫЭЮЯЪ')
sr_only = set('ђјљњћџѕЂЈЉЊЋЏЅ')
bg_only = set('щъьюяЩЪЬЮЯ')
hits = sorted({c for c in sr_t if c in ru_only})
print(f"Russian-only letters in SR: {hits if hits else 'none — OK'}")
lat = sorted({c for c in sr_t if re.match(r'[A-Za-z]', c)})
print(f"Latin letters in SR: {lat if lat else 'none — OK'}")
print(f"Serbian-specific letters present: {sorted({c for c in sr_t if c in sr_only})}")

print("\n=== PRODUCT NAME ===")
for name in ['Nautubone','Наутубон','НАУТУБОН','наутубон']:
    print(f"  {name}: RU={ru_t.count(name)}  SR={sr_t.count(name)}")

print("\n=== HOOK (first 125 chars) ===")
print("RU:", repr(ru_t[:125]))
print("SR:", repr(sr_t[:125]))
