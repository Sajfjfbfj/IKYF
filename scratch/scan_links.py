import os
import sys
import io
import re
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = r"site-complete"

def scan_all_html_links():
    all_html_files = []
    for root, dirs, files in os.walk(site_root):
        for f in files:
            if f.endswith('.html'):
                all_html_files.append(os.path.join(root, f))
                
    print(f"Total HTML files in {site_root}: {len(all_html_files)}")
    
    # Check links in taikai/detail files specifically
    detail_files = [p for p in all_html_files if r"taikai\detail" in p]
    print(f"Total detail files: {len(detail_files)}")
    
    # Analyze links inside taikai/detail
    internal_like_remote_urls = set()
    for p in detail_files:
        with open(p, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        for a in soup.find_all('a'):
            h = a.get('href', '')
            if 'kyudo.jp' in h and not any(ext in h.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']):
                internal_like_remote_urls.add(h)
                
    print(f"\nNon-file kyudo.jp URLs found in taikai/detail index.html files ({len(internal_like_remote_urls)}):")
    for u in sorted(internal_like_remote_urls):
        print(" ", u)
        
    # Analyze links inside schedule/taikai
    sched_files = [p for p in all_html_files if r"schedule\taikai" in p]
    sched_remote_urls = set()
    for p in sched_files:
        with open(p, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        for a in soup.find_all('a'):
            h = a.get('href', '')
            if 'kyudo.jp' in h and not any(ext in h.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']):
                sched_remote_urls.add(h)
                
    print(f"\nNon-file kyudo.jp URLs found in schedule/taikai files ({len(sched_remote_urls)}):")
    for u in sorted(sched_remote_urls):
        print(" ", u)

if __name__ == "__main__":
    scan_all_html_links()
