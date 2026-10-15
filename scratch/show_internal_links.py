import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

detail_base = r"site-complete\taikai\detail"
dirs = sorted(os.listdir(detail_base))

internal_links = set()
for d in dirs:
    p = os.path.join(detail_base, d, "index.html")
    with open(p, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    for a in soup.find_all('a'):
        h = a.get('href', '')
        txt = a.get_text(strip=True)
        if not h.startswith('http'):
            internal_links.add((h, txt))

print(f"Internal links in detail pages: {len(internal_links)}")
for h, txt in sorted(internal_links):
    print(f"  {h} -> {txt}")
