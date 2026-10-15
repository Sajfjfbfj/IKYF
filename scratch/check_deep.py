import re

for filename in [r'site-complete\category\chuoshinsa\index.html',
                 r'site-complete\category\taikai\index.html']:
    with open(filename, encoding='utf-8') as f:
        c = f.read()
    lines = c.split('\n')
    print(f"\n=== {filename} ===")
    for i, line in enumerate(lines, 1):
        if '../../..' in line:
            print(f"  Line {i}: {line.strip()[:200]}")
