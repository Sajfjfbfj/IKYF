import os
import urllib.request
import re
from bs4 import BeautifulSoup

def main():
    detail_dir = r"site-complete\taikai\detail"
    items = os.listdir(detail_dir)
    print(f"Total items in {detail_dir}: {len(items)}")
    
    # check structure of first few items
    sample_files = []
    for item in items[:5]:
        p = os.path.join(detail_dir, item)
        if os.path.isdir(p):
            sub = os.listdir(p)
            print(f"Dir: {item} -> {sub}")
        else:
            print(f"File: {item}")
            
    # fetch schedule/taikai
    url = "https://www.kyudo.jp/schedule/taikai/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            print("\nFetched https://www.kyudo.jp/schedule/taikai/ successfully!")
            links = soup.find_all('a', href=re.compile(r'taikai/detail|schedule/taikai'))
            print(f"Found {len(links)} links matching taikai")
            unique_hrefs = set(a.get('href') for a in links)
            for h in sorted(list(unique_hrefs))[:20]:
                print("  Link:", h)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    main()
