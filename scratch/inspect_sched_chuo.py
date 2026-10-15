import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

local_file = r"site-complete\schedule\chuoshinsa\index.html"
remote_url = "https://www.kyudo.jp/schedule/chuoshinsa/"

def inspect():
    # 1. Local
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding='utf-8') as f:
            local_soup = BeautifulSoup(f.read(), 'html.parser')
        print("=== Local schedule/chuoshinsa/index.html ===")
        print("Title:", local_soup.title.string if local_soup.title else '')
        local_main = local_soup.find('main')
        if local_main:
            h1 = local_main.find('h1')
            print("H1:", h1.get_text(strip=True) if h1 else '')
            table = local_main.find('table')
            if table:
                rows = table.find_all('tr')
                print(f"Table rows: {len(rows)}")
                for r in rows[:4]:
                    print("  Row:", [c.get_text(strip=True) for c in r.find_all(['th', 'td'])])
    else:
        print(f"Local file {local_file} not found!")

    # 2. Remote
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        req = urllib.request.Request(remote_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            remote_html = resp.read().decode('utf-8', errors='ignore')
        with open(r"scratch\remote_schedule_chuoshinsa.html", 'w', encoding='utf-8') as f:
            f.write(remote_html)
            
        remote_soup = BeautifulSoup(remote_html, 'html.parser')
        print("\n=== Remote https://www.kyudo.jp/schedule/chuoshinsa/ ===")
        print("Title:", remote_soup.title.string if remote_soup.title else '')
        remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.find('div', id='contents') or remote_soup.body
        h1 = remote_main.find(['h1', 'h2'])
        print("Main Heading:", h1.get_text(strip=True) if h1 else '')
        
        tables = remote_main.find_all('table')
        print(f"Tables found: {len(tables)}")
        for i, t in enumerate(tables):
            rows = t.find_all('tr')
            print(f"Table {i} rows: {len(rows)}")
            for r in rows[:6]:
                cols = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
                links = [(a.get('href'), a.get_text(strip=True)) for a in r.find_all('a')]
                print("  Row:", cols, "Links:", links)
                
    except Exception as e:
        print("Error fetching remote:", e)

if __name__ == "__main__":
    inspect()
