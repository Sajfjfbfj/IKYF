with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<a[^>]+href=["\'][^"\']*["\'][^>]*>.*?</a>', c, re.DOTALL)
print(f"Total links in index.html: {len(matches)}")
for m in matches:
    if '道場' in m or 'map' in m.lower():
        print(" ", m.strip())
