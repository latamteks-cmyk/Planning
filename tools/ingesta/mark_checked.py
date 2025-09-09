import sys, io
path, target = sys.argv[1], sys.argv[2]
out, ok = [], False
with io.open(path,'r',encoding='utf-8') as f:
  for l in f:
    if not ok and l.startswith('[ ] ') and l.strip()[4:]==target:
      out.append('[x] '+target+'\n'); ok=True
    else: out.append(l)
with io.open(path,'w',encoding='utf-8') as f: f.writelines(out)
if not ok: raise SystemExit('No match')
