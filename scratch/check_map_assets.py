with open(r'site-complete\map\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', c)
print("Assets in site-complete/map/index.html:")
for m in matches:
    if not m.startswith('http') and not m.startswith('#'):
        print(" ", m)
