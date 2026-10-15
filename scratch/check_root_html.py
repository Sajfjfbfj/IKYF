import os
import re

for fname in os.listdir('.'):
    if fname.endswith('.html') and not fname.startswith('.'):
        with open(fname, 'r', encoding='utf-8', errors='ignore') as fp:
            txt = fp.read()
        links = re.findall(r'href=["\'](https?://(?:www\.)?kyudo\.jp/[^"\']*)["\']', txt)
        print(f"{repr(fname)}: {len(links)} external kyudo.jp links")
        for l in links[:5]:
            print("  ", l)
