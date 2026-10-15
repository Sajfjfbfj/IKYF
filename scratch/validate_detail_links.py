import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

detail_base = r"site-complete\taikai\detail"
site_root = os.path.abspath("site-complete")
dirs = sorted(os.listdir(detail_base))

broken_relative_links = []
unusual_links = []

for d in dirs:
    p = os.path.join(detail_base, d, "index.html")
    if not os.path.exists(p):
        continue
    dir_path = os.path.dirname(os.path.abspath(p))
    with open(p, 'r', encoding='utf-8') as fl:
        soup = BeautifulSoup(fl.read(), 'html.parser')
        
    for a in soup.find_all('a'):
        href = a.get('href', '')
        txt = a.get_text(strip=True)
        if not href or href.startswith('#') or href.startswith('javascript:'):
            continue
            
        if href.startswith('http://') or href.startswith('https://'):
            # External link
            # Check if it points to localhost or 127.0.0.1
            if '127.0.0.1' in href or 'localhost' in href:
                unusual_links.append((d, href, txt, "Points to localhost"))
        else:
            # Relative link
            # Resolve against dir_path
            clean_href = href.split('?')[0].split('#')[0]
            target_path = os.path.normpath(os.path.join(dir_path, clean_href))
            if not os.path.exists(target_path):
                # If target ends with slash, check target/index.html
                if os.path.exists(os.path.join(target_path, "index.html")):
                    pass
                else:
                    broken_relative_links.append((d, href, target_path, txt))

print(f"Total checked detail files: {len(dirs)}")
print(f"Broken relative links: {len(broken_relative_links)}")
for item in broken_relative_links[:10]:
    print("  Broken:", item)
    
print(f"Unusual links (e.g. localhost): {len(unusual_links)}")
for item in unusual_links[:10]:
    print("  Unusual:", item)
