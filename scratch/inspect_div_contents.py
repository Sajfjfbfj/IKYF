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
    
    div_c = soup.find('div', class_='contents')
    print(f"\n=================== {p} ===================")
    if div_c:
        print(div_c.prettify()[:1000])
