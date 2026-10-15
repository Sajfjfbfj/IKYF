import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

cat_chuo_dirs = [
    r"site-complete\category\chuoshinsa\2025chuoshinsa\index.html",
    r"site-complete\category\category\chuoshinsa\2024chuoshinsa\index.html",
    r"site-complete\category\category\category\chuoshinsa\2023chuoshinsa\index.html",
    r"site-complete\category\category\category\category\chuoshinsa\2022chuoshinsa\index.html",
    r"site-complete\category\category\category\category\category\chuoshinsa\2021chuoshinsa\index.html",
    r"site-complete\category\chuoshinsa\2020chuoshinsa\index.html"
]

broken = []
for p in cat_chuo_dirs:
    if not os.path.exists(p):
        print("Missing:", p)
        continue
    dir_path = os.path.dirname(os.path.abspath(p))
    with open(p, 'r', encoding='utf-8') as fl:
        soup = BeautifulSoup(fl.read(), 'html.parser')
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if not href or href.startswith('http') or href.startswith('#') or href.startswith('javascript:'):
            continue
        clean = href.split('?')[0].split('#')[0]
        target = os.path.normpath(os.path.join(dir_path, clean))
        if not os.path.exists(target) and not os.path.exists(os.path.join(target, "index.html")):
            broken.append((p, href, target, a.get_text(strip=True)[:30]))

print(f"Total checked files: {len(cat_chuo_dirs)}")
print(f"Broken links in category chuoshinsa pages: {len(broken)}")
for b in broken:
    print("  Broken:", b)
