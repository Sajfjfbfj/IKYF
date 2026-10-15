import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

for p in ['aboutus/index.html', 'aboutus/rule.html', 'info/contact.html', 'documents/index.html']:
    full = os.path.join(mirror_root, os.path.normpath(p))
    with open(full, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # kyudo.jp のメインコンテンツ領域を探す
    main = soup.find('div', id='contents') or soup.find('main') or soup.find('article')
    print(f"=== {p} ===")
    if main:
        # idやクラス
        print(f"Tag: {main.name}, id={main.get('id')}, class={main.get('class')}")
        children = [f"{c.name}.{c.get('class')}" for c in main.find_all(recursive=False)]
        print("Direct children:", children[:10])
    else:
        print("No main content container found!")
