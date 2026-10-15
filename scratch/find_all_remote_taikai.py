import os
import sys
import io
import re
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def get_soup(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')

def main():
    base_url = "https://www.kyudo.jp/schedule/taikai/"
    soup = get_soup(base_url)
    
    # Collect year schedule category links
    cat_links = set()
    for a in soup.find_all('a'):
        h = a.get('href', '')
        if '/category/taikai/' in h:
            if not h.startswith('http'):
                h = 'https://www.kyudo.jp' + h
            cat_links.add(h)
            
    print(f"Found {len(cat_links)} category schedule links:")
    for c in sorted(cat_links):
        print(" ", c)
        
    # From each category page and schedule/taikai, collect all /taikai/detail/ links
    all_detail_links = set()
    pages_to_scan = [base_url] + list(cat_links)
    
    for p in pages_to_scan:
        try:
            s = get_soup(p)
            for a in s.find_all('a'):
                h = a.get('href', '')
                if '/taikai/detail/' in h:
                    m = re.search(r'/taikai/detail/([^/]+)/?', h)
                    if m:
                        all_detail_links.add(m.group(1))
        except Exception as e:
            print(f"Error scanning {p}: {e}")
            
    print(f"\nTotal unique taikai detail slugs found across all schedule pages: {len(all_detail_links)}")
    
    local_dirs = set(os.listdir(r"site-complete\taikai\detail"))
    print(f"Total local dirs: {len(local_dirs)}")
    
    remote_only = all_detail_links - local_dirs
    local_only = local_dirs - all_detail_links
    
    print(f"\nRemote slugs not in local: {len(remote_only)}")
    for s in sorted(remote_only):
        print("  Remote only:", s)
        
    print(f"\nLocal slugs not in remote scanned pages: {len(local_only)}")
    for s in sorted(local_only):
        print("  Local only:", s)

if __name__ == "__main__":
    main()
