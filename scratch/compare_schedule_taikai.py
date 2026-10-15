import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def compare_schedule():
    local_path = r"site-complete\schedule\taikai\index.html"
    with open(local_path, 'r', encoding='utf-8') as f:
        local_soup = BeautifulSoup(f.read(), 'html.parser')
        
    url = "https://www.kyudo.jp/schedule/taikai/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        remote_soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
        
    local_main = local_soup.find('main') or local_soup.body
    remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.body
    
    local_table = local_main.find('table')
    remote_table = remote_main.find('table')
    
    print("Local schedule table rows:", len(local_table.find_all('tr')) if local_table else 0)
    print("Remote schedule table rows:", len(remote_table.find_all('tr')) if remote_table else 0)
    
    if local_table and remote_table:
        l_rows = local_table.find_all('tr')
        r_rows = remote_table.find_all('tr')
        for i in range(max(len(l_rows), len(r_rows))):
            l_text = [c.get_text(strip=True) for c in l_rows[i].find_all(['th', 'td'])] if i < len(l_rows) else ["MISSING"]
            r_text = [c.get_text(strip=True) for c in r_rows[i].find_all(['th', 'td'])] if i < len(r_rows) else ["MISSING"]
            l_links = [a.get('href') for a in l_rows[i].find_all('a')] if i < len(l_rows) else []
            r_links = [a.get('href') for a in r_rows[i].find_all('a')] if i < len(r_rows) else []
            print(f"\nRow {i}:")
            print(f"  Local : {l_text} | Links: {l_links}")
            print(f"  Remote: {r_text} | Links: {r_links}")

if __name__ == "__main__":
    compare_schedule()
