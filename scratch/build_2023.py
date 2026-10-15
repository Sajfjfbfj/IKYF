import os

with open(r'c:\Users\user\Desktop\ホームページ素材\scratch\2023_trs_clean.html', 'r', encoding='utf-8') as f:
    trs = f.read()

with open(r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\chuoshinsa\2024chuoshinsa\index.html', 'r', encoding='utf-8') as f:
    tpl = f.read()

# Replace year and titles
tpl = tpl.replace('令和6年度中央審査会 年間スケジュール', '令和5年度中央審査会 年間スケジュール')
tpl = tpl.replace('2024_guideline_chuoshinsa.pdf', '2023_guideline_chuoshinsa.pdf')
tpl = tpl.replace('令和６年度 中央審査会受審にあたって', '令和５年度 中央審査会受審にあたって')
tpl = tpl.replace('2024_shinsa_touan.pdf', '2023_shinsa_touan.pdf')
tpl = tpl.replace('category/chuoshinsa/2024chuoshinsa/', 'category/chuoshinsa/2023chuoshinsa/')

# Replace tbody contents
import re
tpl = re.sub(r'<tbody>(.*?)</tbody>', f'<tbody>\n{trs}\n</tbody>', tpl, flags=re.DOTALL)

target_file = r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\chuoshinsa\2023chuoshinsa\index.html'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(tpl)
print('Successfully written to', target_file)

triple_dir = r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\category\category\chuoshinsa\2023chuoshinsa'
os.makedirs(triple_dir, exist_ok=True)
triple_file = os.path.join(triple_dir, 'index.html')
with open(triple_file, 'w', encoding='utf-8') as f:
    f.write(tpl)
print('Successfully written to', triple_file)
