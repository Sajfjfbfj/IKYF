import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r"site-complete\schedule\chuoshinsa\index.html", 'r', encoding='utf-8') as f:
    local_soup = BeautifulSoup(f.read(), 'html.parser')

with open(r"scratch\remote_schedule_chuoshinsa.html", 'r', encoding='utf-8') as f:
    remote_soup = BeautifulSoup(f.read(), 'html.parser')

remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.find('div', id='contents') or remote_soup.body

local_table = local_soup.find('table')
remote_table = remote_main.find('table')

local_rows = local_table.find_all('tr')
remote_rows = remote_table.find_all('tr')

for i in range(1, 10):
    l_r = local_rows[i]
    r_r = remote_rows[i]
    
    print(f"\n--- Row {i} ---")
    print("Local TD HTML:")
    for td in l_r.find_all('td'):
        print("  ", td)
    print("Remote TD HTML:")
    for td in r_r.find_all('td'):
        print("  ", td)
