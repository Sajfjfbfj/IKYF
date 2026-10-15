import os
import sys
import io
import re
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sched_dir = r"site-complete\schedule\taikai"
detail_base = r"site-complete\taikai\detail"

html_files = [f for f in os.listdir(sched_dir) if f.endswith('.html')]

for hf in sorted(html_files):
    p = os.path.join(sched_dir, hf)
    with open(p, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    taikai_links = []
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if 'kyudo.jp/taikai/detail/' in href:
            m = re.search(r'/taikai/detail/([^/]+)/?', href)
            if m:
                slug = m.group(1)
                # check if local detail exists
                local_detail_path = os.path.join(detail_base, slug, "index.html")
                exists = os.path.exists(local_detail_path)
                taikai_links.append((slug, href, exists, a.get_text(strip=True)[:30]))
                
    print(f"\n{hf} -> {len(taikai_links)} taikai detail links:")
    all_exist = all(t[2] for t in taikai_links)
    print(f"  All exist in local taikai/detail: {all_exist}")
    if not all_exist:
        for slug, href, exists, txt in taikai_links:
            if not exists:
                print(f"    Missing: {slug} ({txt})")

