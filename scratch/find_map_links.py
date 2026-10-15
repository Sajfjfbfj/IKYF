with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<a[^>]+href=["\'][^"\']*map[^"\']*["\'][^>]*>', c)
print(f"Map links in index.html ({len(matches)}):")
for m in matches:
    print(" ", m)
