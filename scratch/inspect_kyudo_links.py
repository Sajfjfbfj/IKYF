import os
import re

files = [
    r'site-complete\documents\favicon.html',
    r'site-complete\improve\index.html',
    r'site-complete\notice\page\12\index.html',
    r'site-complete\notice\page\28\index.html',
    r'site-complete\notice\page\29\index.html',
    r'site-complete\notice\page\43\index.html',
    r'site-complete\notice\page\45\index.html',
    r'site-complete\notice\page\5\index.html',
    r'site-complete\notice\page\8\index.html',
    r'index.html'
]

for fp in files:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        matches = re.findall(r'href=["\'](https?://(?:www\.)?kyudo\.jp/[^"\']*)["\']', c)
        print(f"=== {fp} ({len(matches)} links) ===")
        for m in sorted(list(set(matches))):
            idx = c.find(m)
            surr = c[max(0, idx-60):min(len(c), idx+len(m)+60)].replace('\n', ' ')
            print(f"   {m}\n      context: {surr}")
