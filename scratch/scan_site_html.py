import os
import sys
from bs4 import BeautifulSoup

site_root = r"c:\Users\user\Desktop\ホームページ素材\site-complete"
mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

# site-complete 内の全HTMLファイルをスキャン
site_files = []
for root, dirs, files in os.walk(site_root):
    for f in files:
        if f.lower().endswith(('.html', '.htm')):
            rel = os.path.relpath(os.path.join(root, f), site_root)
            site_files.append(rel)

print(f"Total HTML in site-complete: {len(site_files)}")

# カテゴリ別に分類してカウント
categories = {}
for sf in site_files:
    top = sf.split(os.sep)[0]
    categories[top] = categories.get(top, 0) + 1

for cat, cnt in sorted(categories.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {cnt} files")
