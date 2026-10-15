import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r"scratch\remote_latestissue.html", 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main') or soup.find('article') or soup.find('div', id='contents') or soup.body
print("Remote page title:", soup.title.string if soup.title else '')

# Find the content elements
# Let's see all sections or divs inside contents
print("\n--- Elements under main/contents ---")
for child in main.children:
    if child.name:
        print(f"<{child.name} class='{child.get('class')}' id='{child.get('id')}'>")
        # print inner headings or text preview
        for h in child.find_all(['h1', 'h2', 'h3', 'h4', 'p'])[:6]:
            print(f"   <{h.name}> {h.get_text(strip=True)[:60]}")
