import os

mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

for path in [r'improve\02.html', r'news\news_202208.html', r'news\news_20260220.html', r'news\news_20260302.html']:
    full = os.path.join(mirror_root, path)
    if os.path.exists(full):
        with open(full, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [f.readline() for _ in range(30)]
        print(f"=== {path} ===")
        print("".join(lines[:15]))
