import re, os

with open(r'c:\Users\user\Desktop\ホームページ素材\scratch\2022_trs.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Skip the first commented-out row
trs_list = lines[1:]

clean_trs = []
for line in trs_list:
    # fix row 23 venue if needed
    if '20221127_detail' in line:
        line = line.replace('<td>【学生】特別臨時中央審査会〈１１月〉</td>', '<td>ビデオ審査</td>')
    clean_trs.append(line)

trs = "".join(clean_trs)

with open(r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\chuoshinsa\2024chuoshinsa\index.html', 'r', encoding='utf-8') as f:
    tpl = f.read()

# Replace year and titles
tpl = tpl.replace('令和6年度中央審査会 年間スケジュール', '令和4年度中央審査会 年間スケジュール')
tpl = tpl.replace('2024_guideline_chuoshinsa.pdf', '2022_guideline_kansenboshi_chuoshinsa.pdf')
tpl = tpl.replace('令和６年度 中央審査会受審にあたって', '令和４年度 中央審査会受審にあたって（新型コロナウイルス感染症防止対策対応）')
tpl = tpl.replace('2024_shinsa_touan.pdf', '2022_shinsa_touan.pdf')
tpl = tpl.replace('category/chuoshinsa/2024chuoshinsa/', 'category/chuoshinsa/2022chuoshinsa/')

# Replace tbody contents
tpl = re.sub(r'<tbody>(.*?)</tbody>', f'<tbody>\n{trs}\n</tbody>', tpl, flags=re.DOTALL)

target_file = r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\chuoshinsa\2022chuoshinsa\index.html'
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(tpl)
print('Successfully written to', target_file)

quad_dir = r'c:\Users\user\Desktop\ホームページ素材\site-complete\category\category\category\category\chuoshinsa\2022chuoshinsa'
os.makedirs(quad_dir, exist_ok=True)
quad_file = os.path.join(quad_dir, 'index.html')
with open(quad_file, 'w', encoding='utf-8') as f:
    f.write(tpl)
print('Successfully written to', quad_file)
