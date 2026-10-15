import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

detail_base_dir = r"site-complete\taikai\detail"
dirs = sorted(os.listdir(detail_base_dir))

def fetch_and_compare(slug):
    local_path = os.path.join(detail_base_dir, slug, "index.html")
    if not os.path.exists(local_path):
        return slug, "Local missing", None
    
    with open(local_path, 'r', encoding='utf-8') as f:
        local_html = f.read()
    local_soup = BeautifulSoup(local_html, 'html.parser')
    
    # Remote url
    remote_url = f"https://www.kyudo.jp/taikai/detail/{slug}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        req = urllib.request.Request(remote_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            remote_html = resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return slug, f"Remote fetch error: {e}", None
        
    remote_soup = BeautifulSoup(remote_html, 'html.parser')
    
    # Compare key elements
    # 1. Title / H1 / H2
    local_h1 = local_soup.find('h1')
    local_h1_text = local_h1.get_text(strip=True) if local_h1 else ''
    
    # Remote heading: remote often has <h2 class="title"> or similar in article/main
    # Let's inspect remote headings
    remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.body
    remote_titles = [h.get_text(strip=True) for h in remote_main.find_all(['h1', 'h2'])]
    
    # 2. PDF links
    local_pdfs = [a.get('href') for a in local_soup.find_all('a') if a.get('href') and any(ext in a.get('href') for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx'])]
    remote_pdfs = [a.get('href') for a in remote_main.find_all('a') if a.get('href') and any(ext in a.get('href') for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx'])]
    
    # 3. Table row counts
    local_table = local_soup.find('table')
    local_rows = len(local_table.find_all('tr')) if local_table else 0
    remote_table = remote_main.find('table')
    remote_rows = len(remote_table.find_all('tr')) if remote_table else 0
    
    diffs = []
    if local_rows != remote_rows:
        diffs.append(f"Table rows: local={local_rows}, remote={remote_rows}")
        
    # Check if remote pdfs are in local
    missing_pdfs = [p for p in remote_pdfs if p not in local_pdfs and ('https://www.kyudo.jp' + p) not in local_pdfs]
    if missing_pdfs:
        diffs.append(f"Missing PDFs: {missing_pdfs}")
        
    return slug, "OK" if not diffs else "Diff", (local_h1_text, remote_titles, diffs)

def main():
    print(f"Comparing sample 15 directories...")
    # Test on a subset first
    sample_slugs = dirs[:5] + dirs[40:45] + dirs[-5:]
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_and_compare, sample_slugs))
        
    for slug, status, info in results:
        print(f"\n[{status}] {slug}")
        if info:
            local_h, remote_hs, diffs = info
            print(f"  Local H1: {local_h}")
            print(f"  Remote Headings: {remote_hs}")
            for d in diffs:
                print(f"  -> {d}")

if __name__ == "__main__":
    main()
