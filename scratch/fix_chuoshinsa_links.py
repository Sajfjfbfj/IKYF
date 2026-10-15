import os
import re
from bs4 import BeautifulSoup

site_root = os.path.abspath("site-complete")

# Define paths
year_files = {
    "2025": r"site-complete\category\chuoshinsa\2025chuoshinsa\index.html",
    "2024": r"site-complete\category\category\chuoshinsa\2024chuoshinsa\index.html",
    "2023": r"site-complete\category\category\category\chuoshinsa\2023chuoshinsa\index.html",
    "2022": r"site-complete\category\category\category\category\chuoshinsa\2022chuoshinsa\index.html",
    "2021": r"site-complete\category\category\category\category\category\chuoshinsa\2021chuoshinsa\index.html",
    "2020": r"site-complete\category\chuoshinsa\2020chuoshinsa\index.html"
}

# The target paths relative to site-complete for year archives
year_destinations = {
    "2026": "schedule/chuoshinsa/",
    "2025": "category/chuoshinsa/2025chuoshinsa/",
    "2024": "category/category/chuoshinsa/2024chuoshinsa/",
    "2023": "category/category/category/chuoshinsa/2023chuoshinsa/",
    "2022": "category/category/category/category/chuoshinsa/2022chuoshinsa/",
    "2021": "category/category/category/category/category/chuoshinsa/2021chuoshinsa/",
    "2020": "category/chuoshinsa/2020chuoshinsa/"
}

def fix_chuoshinsa_files():
    for year, file_path in year_files.items():
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        file_dir = os.path.dirname(os.path.abspath(file_path))
        root_rel = os.path.relpath(site_root, file_dir).replace('\\', '/') + '/'
        matoba_rel = root_rel + "../的場の水鏡.html"
        
        print(f"Processing {year} ({file_path}): root_rel = {root_rel}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Update logo link to 的場の水鏡.html
        mark_a = soup.find('a', class_='mark')
        if mark_a:
            mark_a['href'] = matoba_rel
            
        # 2. Update util links inside #cur
        util_div = soup.find('div', class_='util')
        if util_div:
            for a in util_div.find_all('a'):
                h = a.get('href', '')
                if 'notice' in h:
                    a['href'] = root_rel + "notice/"
                elif 'contact' in h:
                    a['href'] = root_rel + "info/contact.html"
                elif 'english' in h:
                    a['href'] = root_rel + "info/english.html"
                    
        # 3. Breadcrumbs
        crumb = soup.find('div', class_='crumb')
        if crumb:
            home_a = crumb.find('a')
            if home_a:
                home_a['href'] = root_rel + "index.html"
                
        # 4. Detail links in table
        tbl = soup.find('table')
        if tbl:
            for a in tbl.find_all('a'):
                h = a.get('href', '')
                m = re.search(r'chuoshinsa/detail/([^/]+)/?', h)
                if m:
                    slug = m.group(1)
                    local_detail = os.path.join(site_root, "chuoshinsa", "detail", slug)
                    if os.path.exists(local_detail):
                        dest = root_rel + f"chuoshinsa/detail/{slug}/"
                        a['href'] = dest
                    else:
                        print(f"  Warning: chuoshinsa detail {slug} not found locally!")

        # 5. General links
        for a in soup.find_all('a'):
            h = a.get('href', '')
            txt = a.get_text(strip=True)
            if '中央道場概要と使用日程' in txt or 'overview.html' in h:
                a['href'] = root_rel + "schedule/chuoshinsa/overview.html"
            elif '全ページ一覧' in txt or 'all-pages.html' in h:
                a['href'] = root_rel + "all-pages.html"
            elif '全国大会' in txt and 'schedule/taikai' in h:
                a['href'] = root_rel + "schedule/taikai/"
            elif '中央審査会' in txt and 'schedule/chuoshinsa' in h:
                a['href'] = root_rel + "schedule/chuoshinsa/"
            elif '地方審査会' in txt and 'schedule/region' in h:
                a['href'] = root_rel + "schedule/region/"
            elif '連合審査会' in txt and 'schedule/association' in h:
                a['href'] = root_rel + "schedule/association/"
            elif '全国弓道場マップ' in txt and 'map' in h:
                a['href'] = root_rel + "map/"

        # 6. Year schedule links in "年度別スケジュール" section
        for yr, dest_rel in year_destinations.items():
            pattern = re.compile(rf'{yr}chuoshinsa')
            for a in soup.find_all('a', href=pattern):
                a['href'] = root_rel + dest_rel

        # 7. In <script>, update var K="../../.."; to correct root_rel
        new_html = str(soup)
        clean_k = root_rel.rstrip('/')
        new_html = re.sub(r'var\s+K\s*=\s*"[^"]*"', f'var K="{clean_k}"', new_html)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        print(f"  Successfully updated {file_path}")

if __name__ == "__main__":
    fix_chuoshinsa_files()
