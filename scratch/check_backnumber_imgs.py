import re, os

with open(r'site-complete\aboutus\backnumber.html', encoding='utf-8') as f:
    c = f.read()

imgs = re.findall(r'src="(\.\./img/aboutus/monthlykyudo_[^"]+)"', c)
missing = []
for img in imgs:
    path = img.replace('../', 'site-complete/')
    if not os.path.exists(path):
        missing.append(img)

print(f'Total magazine imgs: {len(imgs)}')
print(f'Missing: {len(missing)}')
for m in missing[:20]:
    print(' ', m)
