import os
import sys
import io
import re
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_all_local():
    detail_dir = r"site-complete\taikai\detail"
    dirs = sorted(os.listdir(detail_dir))
    print(f"Total dirs in {detail_dir}: {len(dirs)}")
    
    # Check each dir
    official_urls = {}
    titles = {}
    for d in dirs:
        p = os.path.join(detail_dir, d, "index.html")
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            # Look for official url link if present
            official_link = None
            for a in soup.find_all('a'):
                h = a.get('href', '')
                if 'kyudo.jp/taikai/detail/' in h:
                    official_link = h
                    break
            # Title
            t = soup.find('h1') or soup.find('h2')
            title_text = t.get_text(strip=True) if t else (soup.title.string if soup.title else '')
            official_urls[d] = official_link
            titles[d] = title_text
        else:
            print(f"Missing index.html in {d}")
            
    print("\nSample local mappings (first 10):")
    for d in dirs[:10]:
        print(f"  {d} -> URL: {official_urls.get(d)} | Title: {titles.get(d)[:30]}")

    print("\nSample local mappings (last 10):")
    for d in dirs[-10:]:
        print(f"  {d} -> URL: {official_urls.get(d)} | Title: {titles.get(d)[:30]}")

    no_url = [d for d, u in official_urls.items() if not u]
    print(f"\nDirs without explicit official kyudo.jp/taikai/detail URL: {len(no_url)}")
    if no_url:
        print("  examples:", no_url[:5])

if __name__ == "__main__":
    check_all_local()
