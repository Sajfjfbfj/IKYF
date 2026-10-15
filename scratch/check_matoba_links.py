import re

with open('的場の水鏡.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

links = re.findall(r'href=["\']([^"\']*)["\']', c)
print(f"Total links in 的場の水鏡.html: {len(links)}")
for l in sorted(list(set(links))):
    print("  ", l)
