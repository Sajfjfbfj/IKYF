import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sched_dir = r"site-complete\schedule\taikai"
files = [
    "index.html",
    "r2taikai.html",
    "r3taikai.html",
    "r4taikai.html",
    "r5taikai.html",
    "r6taikai.html",
    "r7taikai.html"
]

broken = []
for f in files:
    p = os.path.join(sched_dir, f)
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
            broken.append((f, href, target, a.get_text(strip=True)[:30]))

print(f"Broken relative links in schedule/taikai files: {len(broken)}")
for b in broken:
    print("  Broken:", b)
