import os
import sys
import io
from bs4 import BeautifulSoup
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = os.path.abspath("site-complete")

def check_taikai_links():
    targets = []
    for root, dirs, files in os.walk(site_root):
        for f in files:
            if f.endswith('.html'):
                p = os.path.join(root, f)
                rel = os.path.relpath(p, site_root).replace('\\', '/')
                if any(x in rel for x in ['taikai', 'schedule/taikai', 'category/taikai']):
                    targets.append((p, rel))
                    
    print(f"Target taikai-related HTML files: {len(targets)}")
    
    internal_nav_externals = []
    
    for full_path, rel in targets:
        with open(full_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        for a in soup.find_all('a'):
            href = a.get('href', '')
            txt = a.get_text(strip=True)
            # Skip if it's explicitly "公式サイトの掲載内容を確認する"
            if "公式サイトの掲載内容を確認する" in txt:
                continue
            if "kyudo.jp" in href and not any(ext in href.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']):
                internal_nav_externals.append((rel, href, txt))
            elif href.startswith('http://127.0.0.1') or href.startswith('http://localhost'):
                internal_nav_externals.append((rel, href, txt))
                
    print(f"\nFound {len(internal_nav_externals)} navigation/content links pointing externally/to localhost in taikai files:")
    by_file = {}
    for rel, href, txt in internal_nav_externals:
        by_file.setdefault(rel, []).append((href, txt))
        
    for rel, links in list(by_file.items())[:15]:
        print(f"\nFile: {rel} ({len(links)} links)")
        for h, t in links[:6]:
            print(f"   {h} -> {t[:40]}")

if __name__ == "__main__":
    check_taikai_links()
