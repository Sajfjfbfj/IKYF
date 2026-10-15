import re, os

with open(r'c:\Users\user\Desktop\ホームページ素材\scratch\2021_trs.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Skip the first commented-out row
clean_trs = lines[1:]
trs = "".join(clean_trs)

with open(r'c:\Users\user\Desktop\ホームページ素材\scratch\2021_top_docs.html', 'r', encoding='utf-8') as f:
    top_docs = f.read().strip()

with open(r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\chuoshinsa\2024chuoshinsa\index.html', 'r', encoding='utf-8') as f:
    tpl = f.read()

# Replace year and titles
tpl = tpl.replace('令和6年度中央審査会 年間スケジュール', '令和3年度中央審査会 年間スケジュール')
tpl = tpl.replace('category/chuoshinsa/2024chuoshinsa/', 'category/chuoshinsa/2021chuoshinsa/')

# Replace the top documents list
tpl = re.sub(r'<section class="materials"><h2>令和3年度中央審査会 年間スケジュール</h2><ul>.*?</ul>', 
             f'<section class="materials"><h2>令和3年度中央審査会 年間スケジュール</h2><ul>{top_docs}</ul>', 
             tpl, flags=re.DOTALL)

# Replace tbody contents
tpl = re.sub(r'<tbody>(.*?)</tbody>', f'<tbody>\n{trs}\n</tbody>', tpl, flags=re.DOTALL)

target_file = r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\chuoshinsa\2021chuoshinsa\index.html'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(tpl)
print('Successfully written to', target_file)

pent_dir = r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\category\category\category\category\chuoshinsa\2021chuoshinsa'
os.makedirs(pent_dir, exist_ok=True)
pent_file = os.path.join(pent_dir, 'index.html')
with open(pent_file, 'w', encoding='utf-8') as f:
    f.write(tpl)
print('Successfully written to', pent_file)
