import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

for path in ['aboutus/index.html', 'info/contact.html', 'aboutus/rule.html']:
    full = os.path.join(mirror_root, os.path.normpath(path))
    with open(full, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    main = soup.find('main') or soup.find('div', id='contents') or soup.find('article') or soup.body
    print(f'=== Mirror {path} ===')
    if main:
        print(main.get_text(strip=True)[:400])
