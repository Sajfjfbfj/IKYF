import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r"scratch\remote_schedule_chuoshinsa.html", 'r', encoding='utf-8') as f:
    remote_soup = BeautifulSoup(f.read(), 'html.parser')

remote_table = remote_soup.find('table')
remote_rows = remote_table.find_all('tr')

for i, r in enumerate(remote_rows):
    cells = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
    # collect all a tags in each td
    tds = r.find_all('td')
    if not tds:
        print(f"Row {i} (Header): {cells}")
        continue
    date = cells[0]
    name = cells[1]
    venue = cells[2]
    
    # check detail link
    name_a = tds[1].find('a')
    detail_url = name_a.get('href') if name_a else None
    
    # guidance, timetable, result
    guidance_a = tds[3].find('a')
    guidance_url = guidance_a.get('href') if guidance_a else None
    
    timetable_a = tds[4].find('a')
    timetable_url = timetable_a.get('href') if timetable_a else None
    
    result_a = tds[5].find('a')
    result_url = result_a.get('href') if result_a else None
    
    print(f"Row {i:2d} | {date} | {name} | Detail: {detail_url}")
    print(f"       Guidance: {guidance_url} | Timetable: {timetable_url} | Result: {result_url}")
