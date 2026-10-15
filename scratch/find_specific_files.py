import os

mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

for root, dirs, files in os.walk(mirror_root):
    for f in files:
        if f in ['02.html', 'news_202208.html', 'news_20260302.html', 'news_20260220.html'] or '20250221' in f or '20220827_02' in f or '20200628' in f or '20190728' in f or '20190907' in f or '20250919' in f:
            print("Found in mirror:", os.path.relpath(os.path.join(root, f), mirror_root))

sc_root = r"site-complete"
for root, dirs, files in os.walk(sc_root):
    for f in files:
        if f in ['02.html', 'news_202208.html', 'news_20260302.html', 'news_20260220.html'] or '20250221' in f or '20220827_02' in f or '20200628' in f or '20190728' in f or '20190907' in f or '20250919' in f:
            print("Found in site-complete:", os.path.relpath(os.path.join(root, f), sc_root))
