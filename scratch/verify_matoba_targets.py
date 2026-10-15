import os
import re

with open('的場の水鏡.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

links = re.findall(r'href=["\']([^"\']*)["\']', c)
for l in sorted(list(set(links))):
    if l.startswith('./site-complete/'):
        clean = l[2:]  # site-complete/...
        if clean.endswith('/'):
            target = os.path.join(clean, 'index.html')
        else:
            target = clean
        exists = os.path.exists(target)
        print(f"{target}: {exists}")
