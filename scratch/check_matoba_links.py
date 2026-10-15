import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

links = re.findall(r'href=["\']([^"\']*)["\']', c)
print(f"Total links in index.html: {len(links)}")
for l in sorted(list(set(links))):
    print("  ", l)
