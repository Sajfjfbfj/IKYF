import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r"site-complete\schedule\chuoshinsa\index.html", 'r', encoding='utf-8') as f:
    local_soup = BeautifulSoup(f.read(), 'html.parser')

with open(r"scratch\remote_schedule_chuoshinsa.html", 'r', encoding='utf-8') as f:
    remote_soup = BeautifulSoup(f.read(), 'html.parser')

remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.find('div', id='contents') or remote_soup.body

# Compare elements
print("=== Headings ===")
print("Local H1:", [h.get_text(strip=True) for h in local_soup.find_all(['h1', 'h2', 'h3'])])
print("Remote Headings:", [h.get_text(strip=True) for h in remote_main.find_all(['h1', 'h2', 'h3'])])

# Compare Table
local_table = local_soup.find('table')
remote_table = remote_main.find('table')

local_rows = local_table.find_all('tr')
remote_rows = remote_table.find_all('tr')

print(f"\nLocal rows: {len(local_rows)}, Remote rows: {len(remote_rows)}")

row_diffs = 0
for i in range(max(len(local_rows), len(remote_rows))):
    l_cells = [c.get_text(strip=True) for c in local_rows[i].find_all(['th', 'td'])] if i < len(local_rows) else []
    r_cells = [c.get_text(strip=True) for c in remote_rows[i].find_all(['th', 'td'])] if i < len(remote_rows) else []
    l_links = [(a.get('href'), a.get_text(strip=True)) for a in local_rows[i].find_all('a')] if i < len(local_rows) else []
    r_links = [(a.get('href'), a.get_text(strip=True)) for a in remote_rows[i].find_all('a')] if i < len(remote_rows) else []
    
    # Check text diff
    if l_cells != r_cells or len(l_links) != len(r_links):
        row_diffs += 1
        print(f"\n--- Row {i} Diff ---")
        print("  Local text :", l_cells)
        print("  Remote text:", r_cells)
        print("  Local links :", l_links)
        print("  Remote links:", r_links)

print(f"\nTotal row diffs: {row_diffs}")

# Compare other sections (documents, links, archives)
print("\n=== Remote other links outside table ===")
for a in remote_main.find_all('a'):
    # if not in table
    if not a.find_parent('table'):
        print(f"  {a.get('href')} -> {a.get_text(strip=True)}")

print("\n=== Local other links outside table ===")
for a in local_soup.find('main').find_all('a'):
    if not a.find_parent('table'):
        print(f"  {a.get('href')} -> {a.get_text(strip=True)}")
