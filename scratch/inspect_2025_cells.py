import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

mirror_path = r'c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\category\chuoshinsa\2025chuoshinsa\index.html'
with open(mirror_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

table = soup.find('table')
for i, r in enumerate(table.find_all('tr')[1:11], 1):
    tds = r.find_all('td')
    row_info = []
    for td in tds:
        a = td.find('a')
        if a:
            row_info.append(f'[{td.get_text(strip=True)}] (href={a.get("href")})')
        else:
            row_info.append(f'[{td.get_text(strip=True)}]')
    print(f'Row {i}: ' + ' | '.join(row_info))
