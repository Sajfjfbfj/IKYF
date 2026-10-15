import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r"site-complete\category\chuoshinsa\2025chuoshinsa\index.html", 'r', encoding='utf-8') as f:
    local_soup = BeautifulSoup(f.read(), 'html.parser')

with open(r"scratch\remote_2025chuoshinsa.html", 'r', encoding='utf-8') as f:
    remote_soup = BeautifulSoup(f.read(), 'html.parser')

remote_main = remote_soup.find('main') or remote_soup.find('article') or remote_soup.find('div', id='contents') or remote_soup.body

print("=== Headings ===")
print("Local H1:", [h.get_text(strip=True) for h in local_soup.find_all(['h1', 'h2', 'h3'])])
print("Remote Headings:", [h.get_text(strip=True) for h in remote_main.find_all(['h1', 'h2', 'h3'])])

local_table = local_soup.find('table')
remote_table = remote_main.find('table')

local_rows = local_table.find_all('tr') if local_table else []
remote_rows = remote_table.find_all('tr') if remote_table else []

print(f"\nLocal rows: {len(local_rows)}, Remote rows: {len(remote_rows)}")

row_diffs = 0
for i in range(max(len(local_rows), len(remote_rows))):
    l_cells = [c.get_text(strip=True) for c in local_rows[i].find_all(['th', 'td'])] if i < len(local_rows) else []
    r_cells = [c.get_text(strip=True) for c in remote_rows[i].find_all(['th', 'td'])] if i < len(remote_rows) else []
    l_links = [(a.get('href'), a.get_text(strip=True)) for a in local_rows[i].find_all('a')] if i < len(local_rows) else []
    r_links = [(a.get('href'), a.get_text(strip=True)) for a in remote_rows[i].find_all('a')] if i < len(remote_rows) else []
    
    if l_cells != r_cells or len(l_links) != len(r_links):
        row_diffs += 1
        print(f"\n--- Row {i} Diff ---")
        print("  Local text :", l_cells)
        print("  Remote text:", r_cells)
        print("  Local links :", l_links)
        print("  Remote links:", r_links)

print(f"\nTotal row diffs: {row_diffs}")

print("\n=== Remote other links outside table ===")
for a in remote_main.find_all('a'):
    if not a.find_parent('table'):
        print(f"  {a.get('href')} -> {a.get_text(strip=True)}")

print("\n=== Local other links outside table ===")
for a in local_soup.find('main').find_all('a'):
    if not a.find_parent('table'):
        print(f"  {a.get('href')} -> {a.get_text(strip=True)}")
