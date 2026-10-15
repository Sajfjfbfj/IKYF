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
    
    remote_url = f"https://www.kyudo.jp/taikai/detail/{slug}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        req = urllib.request.Request(remote_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            remote_html = resp.read().decode('utf-8', errors='ignore')
    except urllib.error.HTTPError as e:
        return slug, f"HTTP Error {e.code}", None
    except Exception as e:
        return slug, f"Fetch Error {e}", None
        
    remote_soup = BeautifulSoup(remote_html, 'html.parser')
    remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.body
    
    local_h1 = local_soup.find('h1')
    local_h1_text = local_h1.get_text(strip=True) if local_h1 else ''
    
    # Extract links
    local_links = set(a.get('href') for a in local_soup.find_all('a') if a.get('href'))
    remote_links = set(a.get('href') for a in remote_main.find_all('a') if a.get('href'))
    
    # Normalize kyudo.jp links
    def norm(link):
        if link.startswith('/'):
            return 'https://www.kyudo.jp' + link
        return link

    remote_pdf_links = set(norm(l) for l in remote_links if any(ext in l.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']))
    local_pdf_links = set(norm(l) for l in local_links if any(ext in l.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']))
    
    missing_pdfs = remote_pdf_links - local_pdf_links
    
    # Table rows
    local_tables = local_soup.find_all('table')
    local_rows = sum(len(t.find_all('tr')) for t in local_tables)
    remote_tables = remote_main.find_all('table')
    remote_rows = sum(len(t.find_all('tr')) for t in remote_tables)
    
    # Table text diff check
    local_table_text = " ".join(t.get_text(strip=True) for t in local_tables)
    remote_table_text = " ".join(t.get_text(strip=True) for t in remote_tables)
    
    diffs = []
    if missing_pdfs:
        diffs.append(f"Missing PDFs: {missing_pdfs}")
    if local_rows != remote_rows:
        diffs.append(f"Row count diff: local={local_rows}, remote={remote_rows}")
    elif len(local_table_text) != len(remote_table_text):
        # Allow minor whitespace difference
        l_clean = "".join(local_table_text.split())
        r_clean = "".join(remote_table_text.split())
        if l_clean != r_clean:
            diffs.append(f"Table content diff (len {len(l_clean)} vs {len(r_clean)})")

    return slug, "Diff" if diffs else "OK", diffs

def main():
    print(f"Comparing all {len(dirs)} directories...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(fetch_and_compare, dirs))
        
    diff_count = 0
    err_count = 0
    ok_count = 0
    for slug, status, diffs in results:
        if status == "OK":
            ok_count += 1
        elif "Error" in status:
            err_count += 1
            print(f"[{status}] {slug}")
        else:
            diff_count += 1
            print(f"[Diff] {slug}: {diffs}")
            
    print(f"\nSummary: Total={len(dirs)}, OK={ok_count}, Diff={diff_count}, Error={err_count}")

if __name__ == "__main__":
    main()
