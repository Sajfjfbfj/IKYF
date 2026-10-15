import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"

mirror_files = []
for root, dirs, files in os.walk(mirror_root):
    for f in files:
        if f.lower().endswith(('.html', '.htm')):
            rel = os.path.relpath(os.path.join(root, f), mirror_root)
            mirror_files.append(rel)

print(f"Total HTML in mirror: {len(mirror_files)}")

# カテゴリ別に集計
by_cat = {}
for mf in mirror_files:
    parts = mf.split(os.sep)
    cat = parts[0]
    by_cat[cat] = by_cat.get(cat, 0) + 1

for cat, cnt in sorted(by_cat.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {cnt} files")
    # もしサブフォルダがあれば詳細
    sub_sample = [f for f in mirror_files if f.startswith(cat + os.sep)][:5]
    for s in sub_sample:
        print(f"    - {s}")

with open("scratch/mirror_html_list.txt", "w", encoding="utf-8") as out:
    for mf in sorted(mirror_files):
        out.write(mf + "\n")
