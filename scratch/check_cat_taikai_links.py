import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

cat_taikai = r"site-complete\category\taikai"
for root, dirs, files in os.walk(cat_taikai):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fl:
                soup = BeautifulSoup(fl.read(), 'html.parser')
            detail_links = []
            for a in soup.find_all('a'):
                h = a.get('href', '')
                if 'detail' in h or 'taikai' in h:
                    detail_links.append((h, a.get_text(strip=True)[:30]))
            print(f"\n{p} (detail/taikai links: {len(detail_links)})")
            for h, txt in detail_links[:5]:
                print(f"  {h} -> {txt}")
