import glob
import re

matches = set()
for html in glob.glob('site-complete/**/*.html', recursive=True):
    with open(html, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    icons = re.findall(r'<link[^>]+rel=["\'](?:shortcut )?icon["\'][^>]*>', c)
    for ic in icons:
        matches.add(ic)

print("Favicon tags found in site-complete:")
for m in sorted(list(matches))[:20]:
    print(" ", m)

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()
icons = re.findall(r'<link[^>]+rel=["\'](?:shortcut )?icon["\'][^>]*>', c)
print("Favicon tags in index.html:", icons)
