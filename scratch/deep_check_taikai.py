import os
import sys
import io
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

detail_base_dir = r"site-complete\taikai\detail"
dirs = sorted(os.listdir(detail_base_dir))

def clean_text(text):
    return "".join(text.split()).replace('\u3000', '').replace('&nbsp;', '')

def check_content_detail(slug):
    local_path = os.path.join(detail_base_dir, slug, "index.html")
    with open(local_path, 'r', encoding='utf-8') as f:
        local_soup = BeautifulSoup(f.read(), 'html.parser')
        
    remote_url = f"https://www.kyudo.jp/taikai/detail/{slug}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        req = urllib.request.Request(remote_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            remote_soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
    except Exception as e:
        return slug, "error", f"{e}"
        
    remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.body
    
    # 1. Title / H1 check
    local_h1 = local_soup.find('h1')
    local_title = local_h1.get_text(strip=True) if local_h1 else ''
    
    # Remote page title or h2
    remote_h = remote_main.find(['h1', 'h2', 'h3'])
    
    # 2. Table comparison - check each (th, td) pair
    local_table = local_soup.find('table')
    remote_table = remote_main.find('table')
    
    table_diffs = []
    if local_table and remote_table:
        l_trs = local_table.find_all('tr')
        r_trs = remote_table.find_all('tr')
        l_dict = {tr.find('th').get_text(strip=True): tr.find('td').get_text(strip=True) for tr in l_trs if tr.find('th') and tr.find('td')}
        r_dict = {tr.find('th').get_text(strip=True): tr.find('td').get_text(strip=True) for tr in r_trs if tr.find('th') and tr.find('td')}
        
        for k, v in r_dict.items():
            if k not in l_dict:
                table_diffs.append(f"Missing key in local: {k}")
            elif clean_text(l_dict[k]) != clean_text(v):
                table_diffs.append(f"Value mismatch for [{k}]:\n    Local: {l_dict[k][:60]}...\n    Remote: {v[:60]}...")
        for k in l_dict.keys():
            if k not in r_dict:
                table_diffs.append(f"Extra key in local: {k}")
    elif remote_table and not local_table:
        table_diffs.append("Remote has table but local does not")
        
    # 3. PDF/file links
    def get_file_links(soup):
        res = {}
        for a in soup.find_all('a'):
            h = a.get('href', '')
            if any(ext in h.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']):
                # normalize
                fname = h.split('/')[-1]
                res[fname] = a.get_text(strip=True)
        return res
        
    l_files = get_file_links(local_soup)
    r_files = get_file_links(remote_main)
    
    link_diffs = []
    for fn, txt in r_files.items():
        if fn not in l_files:
            link_diffs.append(f"Missing file link: {fn} ({txt})")
            
    if table_diffs or link_diffs:
        return slug, "diff", {"table": table_diffs, "links": link_diffs}
    return slug, "ok", None

def main():
    print("Deeply checking all 97 taikai detail files...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(check_content_detail, dirs))
        
    diffs = [r for r in results if r[1] == "diff"]
    errors = [r for r in results if r[1] == "error"]
    oks = [r for r in results if r[1] == "ok"]
    
    print(f"\nResult: OK={len(oks)}, Diff={len(diffs)}, Errors={len(errors)}")
    for slug, status, data in diffs:
        print(f"\n=== {slug} ===")
        if data.get('table'):
            print("  Table diffs:")
            for td in data['table']:
                print("   ", td)
        if data.get('links'):
            print("  Link diffs:")
            for ld in data['links']:
                print("   ", ld)

if __name__ == "__main__":
    main()
