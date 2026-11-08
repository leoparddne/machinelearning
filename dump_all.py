# -*- coding: utf-8 -*-
import json, glob, os, sys

files = []
for base in [r'c:\Users\ives\Desktop\temp\ml\homework\week2', r'c:\Users\ives\Desktop\temp\ml\homework\week3']:
    for p in glob.glob(os.path.join(base, '**', '*.ipynb'), recursive=True):
        if 'checkpoint' in p.lower() or 'archive' in p.lower():
            continue
        files.append(p)

out = sys.argv[1] if len(sys.argv) > 1 else 'dump_all.txt'
with open(out, 'w', encoding='utf-8') as w:
    for p in files:
        nb = json.load(open(p, encoding='utf-8'))
        w.write('\n\n########## FILE: %s ##########\n' % p)
        for i, c in enumerate(nb['cells']):
            if c['cell_type'] == 'markdown':
                w.write('\n--- MD CELL %d ---\n' % i)
                w.write(''.join(c['source']))
            elif c['cell_type'] == 'code':
                src = ''.join(c['source'])
                w.write('\n--- CODE CELL %d ---\n' % i)
                w.write(src)
print('files:', len(files))
for f in files: print(f)
