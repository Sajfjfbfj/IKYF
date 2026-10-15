with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
links = re.findall(r'<a[^>]+href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', c, re.DOTALL)
for href, text in links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    print(f"{clean_text} -> {href}")
