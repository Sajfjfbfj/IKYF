import re

with open(r'site-complete\category\chuoshinsa\index.html', encoding='utf-8') as f:
    c = f.read()

# Find all ../../ occurrences
lines = c.split('\n')
with open('scratch/deep_paths.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines, 1):
        if '../../' in line:
            out.write(f"Line {i}: {line.strip()[:200]}\n")
print("saved to deep_paths.txt")
