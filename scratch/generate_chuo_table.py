import re
from bs4 import BeautifulSoup

def build_table():
    with open(r"scratch\remote_schedule_chuoshinsa.html", 'r', encoding='utf-8') as f:
        remote_soup = BeautifulSoup(f.read(), 'html.parser')
        
    remote_table = remote_soup.find('table')
    remote_rows = remote_table.find_all('tr')
    
    tbody_rows = []
    
    for i, r in enumerate(remote_rows[1:], 1):
        tds = r.find_all('td')
        if len(tds) < 6:
            continue
        date_text = tds[0].get_text(strip=True)
        name_td = tds[1]
        name_text = name_td.get_text(strip=True)
        name_a = name_td.find('a')
        
        detail_href = name_a.get('href', '') if name_a else ''
        # extract slug
        m = re.search(r'chuoshinsa/detail/([^/]+)/?', detail_href)
        slug = m.group(1) if m else ''
        
        venue_text = tds[2].get_text(strip=True)
        
        # guidance
        guidance_a = tds[3].find('a')
        guidance_href = guidance_a.get('href', '') if guidance_a else ''
        if guidance_href.startswith('/'):
            guidance_href = 'https://www.kyudo.jp' + guidance_href
            
        # timetable
        timetable_a = tds[4].find('a')
        timetable_href = timetable_a.get('href', '') if timetable_a else ''
        if timetable_href.startswith('/'):
            timetable_href = 'https://www.kyudo.jp' + timetable_href
            
        # result
        result_a = tds[5].find('a')
        result_href = result_a.get('href', '') if result_a else ''
        if result_href.startswith('/'):
            result_href = 'https://www.kyudo.jp' + result_href
            
        # Build cells matching existing design
        # Date
        td_date = f'<td class="d">{date_text}</td>'
        
        # Name
        if slug:
            td_name = f'<td><a href="../../chuoshinsa/detail/{slug}/">{name_text}</a></td>'
        else:
            td_name = f'<td>{name_text}</td>'
            
        # Venue
        td_venue = f'<td>{venue_text}</td>'
        
        # Guidance
        if guidance_href:
            td_guidance = f'<td><a href="{guidance_href}">実施要項<span class="pdf">PDF</span></a></td>'
        else:
            td_guidance = '<td></td>'
            
        # Timetable
        if timetable_href:
            td_timetable = f'<td><a href="{timetable_href}">立会<span class="pdf">PDF</span></a></td>'
        else:
            td_timetable = '<td></td>'
            
        # Result
        if result_href:
            td_result = f'<td><a href="{result_href}">結果<span class="pdf">PDF</span></a></td>'
        else:
            td_result = '<td></td>'
            
        row_html = f'<tr>{td_date}{td_name}{td_venue}{td_guidance}{td_timetable}{td_result}</tr>'
        tbody_rows.append(row_html)
        
    return '\n'.join(tbody_rows)

if __name__ == '__main__':
    res = build_table()
    print("Generated rows:", len(res.splitlines()))
    print("First 3 rows:\n", '\n'.join(res.splitlines()[:3]))
    print("Last 3 rows:\n", '\n'.join(res.splitlines()[-3:]))
