import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def inspect_20170609():
    slug = "20170609_detail"
    local_path = os.path.join(r"site-complete\taikai\detail", slug, "index.html")
    with open(local_path, 'r', encoding='utf-8') as f:
        local_soup = BeautifulSoup(f.read(), 'html.parser')
        
    remote_url = f"https://www.kyudo.jp/taikai/detail/{slug}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(remote_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        remote_soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
        
    local_trs = local_soup.find('table').find_all('tr')
    remote_trs = remote_soup.find('table').find_all('tr')
    
    print("Local tr count:", len(local_trs))
    print("Remote tr count:", len(remote_trs))
    
    local_headers = [tr.find('th').get_text(strip=True) if tr.find('th') else '' for tr in local_trs]
    remote_headers = [tr.find('th').get_text(strip=True) if tr.find('th') else '' for tr in remote_trs]
    
    print("Local headers:", local_headers)
    print("Remote headers:", remote_headers)
    
    for tr in remote_trs:
        th = tr.find('th').get_text(strip=True) if tr.find('th') else ''
        td = tr.find('td').get_text(strip=True) if tr.find('td') else ''
        if th not in local_headers:
            print(f"Missing in local: [{th}] -> {td[:50]}")

if __name__ == "__main__":
    inspect_20170609()
