import os
import sys
import io
import re
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = os.path.abspath("site-complete")

def scan_all_files():
    matches = []
    for root, dirs, files in os.walk(site_root):
        for f in files:
            if not f.endswith('.html'):
                continue
            full_path = os.path.join(root, f)
            rel = os.path.relpath(full_path, site_root).replace('\\', '/')
            
            with open(full_path, 'r', encoding='utf-8') as fl:
                content = fl.read()
                
            # Quick check if file contains any interesting URLs
            if 'kyudo.jp' in content or '127.0.0.1' in content or 'localhost' in content:
                soup = BeautifulSoup(content, 'html.parser')
                for a in soup.find_all('a'):
                    h = a.get('href', '')
                    txt = a.get_text(strip=True)
                    # Check if href is pointing to taikai or schedule or category
                    if any(frag in h for frag in ['taikai/detail', 'schedule/taikai', 'category/taikai', '127.0.0.1', 'localhost']):
                        matches.append((rel, h, txt))
                        
    print(f"Total matching links found across entire site-complete: {len(matches)}")
    by_file = {}
    for rel, h, txt in matches:
        by_file.setdefault(rel, []).append((h, txt))
        
    for rel, links in sorted(by_file.items()):
        print(f"\n{rel} ({len(links)} links):")
        for h, txt in links[:8]:
            print(f"  {h} -> {txt[:40]}")
        if len(links) > 8:
            print(f"  ... and {len(links)-8} more")

if __name__ == "__main__":
    scan_all_files()
