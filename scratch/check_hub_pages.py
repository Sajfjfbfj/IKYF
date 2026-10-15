import os
import sys
import io
import re
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

key_pages = [
    r"site-complete\all-pages.html",
    r"site-complete\index.html",
    r"site-complete\schedule\index.html",
    r"site-complete\category\taikai\index.html"
]

for p in key_pages:
    if not os.path.exists(p):
        print(f"File not found: {p}")
        continue
    with open(p, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(f"\n=== {p} ===")
    for a in soup.find_all('a'):
        h = a.get('href', '')
        if any(w in h for w in ['taikai', 'schedule/taikai', 'category/taikai', 'kyudo.jp']):
            print(f"  {h} -> {a.get_text(strip=True)[:40]}")
