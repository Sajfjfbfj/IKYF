import sys
import io
import urllib.request
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

urls = [
    "https://www.kyudo.jp/taikai/detail/20260502_detail/",
    "https://www.kyudo.jp/taikai/detail/20240921_1.html",  # check if .html or _detail/
    "https://www.kyudo.jp/taikai/detail/20170502_detail/"
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in urls:
    print(f"\n================ Fetching {url} ================")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            print("Title:", soup.title.string if soup.title else '')
            main = soup.find('main') or soup.find('article') or soup.find('div', class_='contents') or soup.find('div', id='contents')
            if not main:
                main = soup.body
            print("Found main-like container:", main.name, main.get('class'), main.get('id'))
            
            # headings
            headings = [h.get_text(strip=True) for h in main.find_all(['h1', 'h2', 'h3'])[:5]]
            print("Headings:", headings)
            
            # tables
            tables = main.find_all('table')
            print(f"Tables: {len(tables)}")
            for t in tables[:2]:
                for r in t.find_all('tr'):
                    print("  Row:", [c.get_text(strip=True) for c in r.find_all(['th', 'td'])])
                    
            # links
            print("PDF / file links:")
            for a in main.find_all('a'):
                h = a.get('href', '')
                if any(ext in h.lower() for ext in ['.pdf', '.doc', '.docx', '.xls', '.xlsx']):
                    print("  File link:", h, "->", a.get_text(strip=True))
    except Exception as e:
        print("Error:", e)
