import re

with open(r'site-complete\category\chuoshinsa\2025chuoshinsa\index.html', encoding='utf-8') as f:
    c = f.read()

lines = c.split('\n')
with open('scratch/template_paths.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines, 1):
        if '水鏡' in line or '../../' in line or 'notice' in line:
            out.write(f"Line {i}: {line.strip()[:300]}\n")
print("saved")
