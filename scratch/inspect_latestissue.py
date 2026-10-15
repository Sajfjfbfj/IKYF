import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

local_file = r"site-complete\aboutus\latestissue.html"

def check_both():
    # 1. Local
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding='utf-8') as f:
            local_html = f.read()
        local_soup = BeautifulSoup(local_html, 'html.parser')
        print("=== Local latestissue.html ===")
        print("Title:", local_soup.title.string if local_soup.title else '')
        local_main = local_soup.find('main')
        if local_main:
            print("Main text (first 500 chars):")
            print(local_main.get_text()[:500].strip())
            print("\nMain images:")
            for img in local_main.find_all('img'):
                print("  img:", img.get('src'), img.get('alt'))
            print("\nMain links:")
            for a in local_main.find_all('a'):
                print("  a:", a.get('href'), a.get_text(strip=True)[:40])
    else:
        print(f"Local file {local_file} not found!")

    # 2. Remote
    url = "https://www.kyudo.jp/aboutus/latestissue.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            remote_html = resp.read().decode('utf-8', errors='ignore')
        remote_soup = BeautifulSoup(remote_html, 'html.parser')
        print("\n=== Remote https://www.kyudo.jp/aboutus/latestissue.html ===")
        print("Title:", remote_soup.title.string if remote_soup.title else '')
        remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.find('div', id='contents') or remote_soup.body
        print("Main text:")
        print(remote_main.get_text()[:800].strip())
        print("\nRemote images:")
        for img in remote_main.find_all('img'):
            print("  img:", img.get('src'), img.get('alt'))
        print("\nRemote links:")
        for a in remote_main.find_all('a'):
            print("  a:", a.get('href'), a.get_text(strip=True)[:40])
            
        with open(r"scratch\remote_latestissue.html", 'w', encoding='utf-8') as f:
            f.write(remote_html)
    except Exception as e:
        print("Remote fetch error:", e)

if __name__ == "__main__":
    check_both()
