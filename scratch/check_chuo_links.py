import os
import re

site_root = r"site-complete"

chuo_years = [
    "category/chuoshinsa/2025chuoshinsa/index.html",
    "category/category/chuoshinsa/2024chuoshinsa/index.html",
    "category/category/category/chuoshinsa/2023chuoshinsa/index.html",
    "category/category/category/category/chuoshinsa/2022chuoshinsa/index.html",
    "category/category/category/category/category/chuoshinsa/2021chuoshinsa/index.html",
    "category/chuoshinsa/2020chuoshinsa/index.html",
    "schedule/chuoshinsa/index.html"
]

print("=== Checking chuoshinsa year files ===")
for rel in chuo_years:
    full = os.path.join(site_root, os.path.normpath(rel))
    if not os.path.exists(full):
        print(f"MISSING: {rel}")
        continue
    with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    
    # リンクを抽出して実在チェック
    links = re.findall(r'href=["\']([^"\']+)["\']', txt)
    broken = []
    for l in links:
        if l.startswith(('http:', 'https:', '#', 'mailto:', 'tel:')):
            continue
        # 相対パス解決
        file_dir = os.path.dirname(full)
        target = os.path.normpath(os.path.join(file_dir, l.split('?')[0].split('#')[0]))
        if not os.path.exists(target):
            # もしディレクトリの場合、index.htmlがあるか
            if os.path.isdir(target) and os.path.exists(os.path.join(target, 'index.html')):
                continue
            broken.append(l)
    print(f"{rel}: {len(links)} links, {len(broken)} broken")
    if broken:
        print("  Broken sample:", broken[:5])
