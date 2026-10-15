import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def analyze():
    # 1. Check local schedule/taikai
    sched_taikai = r"site-complete\schedule\taikai\index.html"
    if os.path.exists(sched_taikai):
        with open(sched_taikai, 'r', encoding='utf-8') as f:
            sched_content = f.read()
        soup_sched = BeautifulSoup(sched_content, 'html.parser')
        print(f"Local schedule/taikai title: {soup_sched.title.string if soup_sched.title else ''}")
        table = soup_sched.find('table')
        if table:
            rows = table.find_all('tr')
            print(f"Local schedule/taikai table rows: {len(rows)}")
            for r in rows[:5]:
                print("  Sched row:", [c.get_text(strip=True) for c in r.find_all(['th', 'td'])])

    # 2. Check local detail file
    sample_detail = r"site-complete\taikai\detail\20170502_detail\index.html"
    with open(sample_detail, 'r', encoding='utf-8') as f:
        soup_det = BeautifulSoup(f.read(), 'html.parser')
    print("\nLocal detail title:", soup_det.title.string if soup_det.title else '')
    main = soup_det.find('main')
    if main:
        h1 = main.find(['h1', 'h2'])
        print("Local detail heading:", h1.get_text(strip=True) if h1 else 'None')
        tables = main.find_all('table')
        print("Local detail tables:", len(tables))
        for t in tables:
            for r in t.find_all('tr'):
                print("   Det row:", [c.get_text(strip=True) for c in r.find_all(['th', 'td'])])
        for a in main.find_all('a'):
            print("   Det link:", a.get('href'), "->", a.get_text(strip=True))

    # 3. Check remote https://www.kyudo.jp/schedule/taikai/
    url = "https://www.kyudo.jp/schedule/taikai/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    soup_rem = BeautifulSoup(html, 'html.parser')
    print("\nRemote schedule title:", soup_rem.title.string if soup_rem.title else '')
    rem_table = soup_rem.find('table')
    if rem_table:
        rows = rem_table.find_all('tr')
        print(f"Remote schedule rows: {len(rows)}")
        for r in rows[:8]:
            cols = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
            links = [a.get('href') for a in r.find_all('a')]
            print("  Remote row:", cols, "Links:", links)

    # 4. Check if remote has detail pages or what links exist on kyudo.jp
    print("\nChecking any detail links in remote schedule:")
    for a in soup_rem.find_all('a'):
        href = a.get('href', '')
        if 'detail' in href or 'taikai' in href:
            print("  a href:", href, "text:", a.get_text(strip=True))

if __name__ == "__main__":
    analyze()
