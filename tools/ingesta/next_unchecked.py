import sys, io
with io.open(sys.argv[1],'r',encoding='utf-8') as f:
    for line in f:
        if line.startswith('[ ] '):
            print(line.strip()[4:]); break
    else: print('COMPLETO')
