import os
import sys
import io
import re
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = r"site-complete"

def analyze_links():
    # Check detail files first
    detail_dir = os.path.join(site_root, "taikai", "detail")
    dirs = os.listdir(detail_dir)
    print(f"Detail dirs: {len(dirs)}")
    
    external_links_in_detail = {}
    for d in dirs:
        p = os.path.join(detail_dir, d, "index.html")
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        for a in soup.find_all('a'):
            h = a.get('href', '')
            if 'kyudo.jp' in h or 'http://' in h or 'https://' in h:
                # categorize
                if d not in external_links_in_detail:
                    external_links_in_detail[d] = []
                external_links_in_detail[d].append((h, a.get_text(strip=True)))
                
    # Sample output of external links in detail files
    sample_slug = dirs[0]
    print(f"\nSample external links in {sample_slug}:")
    for h, txt in external_links_in_detail.get(sample_slug, []):
        print(f"  {h} -> {txt}")
        
    # Check schedule/taikai/index.html
    sched_taikai = os.path.join(site_root, "schedule", "taikai", "index.html")
    if os.path.exists(sched_taikai):
        with open(sched_taikai, 'r', encoding='utf-8') as f:
            s_soup = BeautifulSoup(f.read(), 'html.parser')
        print(f"\nExternal links in {sched_taikai}:")
        for a in s_soup.find_all('a'):
            h = a.get('href', '')
            if 'kyudo.jp' in h:
                print(f"  {h} -> {a.get_text(strip=True)[:40]}")

if __name__ == "__main__":
    analyze_links()
