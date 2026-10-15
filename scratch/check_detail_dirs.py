import os

mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

for root, dirs, files in os.walk(mirror_root):
    for d in dirs:
        if any(k in d for k in ['20250221', '20220827', '20200628', '20190728', '20190907', '20250919', '20260822']):
            print("Mirror dir:", os.path.relpath(os.path.join(root, d), mirror_root))

sc_root = r"site-complete"
for root, dirs, files in os.walk(sc_root):
    for d in dirs:
        if any(k in d for k in ['20250221', '20220827', '20200628', '20190728', '20190907', '20250919', '20260822']):
            print("Site-complete dir:", os.path.relpath(os.path.join(root, d), sc_root))
