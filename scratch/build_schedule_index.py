import os
import re
from bs4 import BeautifulSoup

mirror_path = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\schedule\index.html"
target_path = r"site-complete\schedule\index.html"

with open(mirror_path, 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

update_list = soup.find('ul', class_='update_list')
update_items = []
if update_list:
    for li in update_list.find_all('li')[:10]:
        date = li.find('span', class_='update_date')
        date_txt = date.get_text(strip=True) if date else ""
        cat = li.find('span', class_='category')
        cat_txt = cat.get_text(strip=True) if cat else "大会情報"
        a = li.find('a')
        title_txt = a.get_text(strip=True) if a else ""
        href = a.get('href', '') if a else ""
        # href相対化: ../taikai/detail/... -> taikai/detail/... (schedule/からの相対)
        if href.startswith('../'):
            href = href[3:]
        
        # 本文テキスト
        p = li.find('p')
        # title以降のテキスト
        full_p = p.get_text(strip=True) if p else ""
        desc = full_p.replace(cat_txt, '').replace(title_txt, '').strip()

        item_html = f'''<li style="padding:1.2em 0;border-bottom:1px solid var(--line)"><div style="display:flex;align-items:center;gap:1em;font-size:12px;color:var(--sub);margin-bottom:.4em"><time>{date_txt}</time><span style="border:1px solid var(--accent);color:var(--accent);padding:0 .5em;font-size:11px">{cat_txt}</span></div><a href="{href}" style="font-size:16px;font-weight:600;display:block;margin-bottom:.3em">{title_txt}</a><p style="margin:0;font-size:13px;color:var(--sub);line-height:1.8">{desc}</p></li>'''
        update_items.append(item_html)

updates_html = '\n'.join(update_items)

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# title & description
html = re.sub(r'<title>.*?</title>', '<title>大会・審査会情報（年間予定）｜公益財団法人 全日本弓道連盟</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="全国大会、中央審査会、連合審査会、地方審査会の年間予定・実施要項・結果および更新情報を掲載しています。">', html)

new_main = f'''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>大会・審査会情報</div><p class="eyebrow">大会・審査会情報</p><h1>大会・審査会情報(年間予定)</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div><p class="summary">全国で開催される大会や審査会の年間スケジュール、実施要項、進行表、結果発表をご案内します。</p><section class="materials"><h2>スケジュール一覧</h2><ul><li><a href="taikai/">全国大会（年間スケジュール）<span class="more" style="color:var(--sub);font-size:13px;margin-left:1em">詳しく見る</span></a></li><li><a href="chuoshinsa/">中央審査会（年間スケジュール）<span class="more" style="color:var(--sub);font-size:13px;margin-left:1em">詳しく見る</span></a></li><li><a href="association/">連合審査会（年間スケジュール）<span class="more" style="color:var(--sub);font-size:13px;margin-left:1em">詳しく見る</span></a></li><li><a href="region/">地方審査会（年間スケジュール）<span class="more" style="color:var(--sub);font-size:13px;margin-left:1em">詳しく見る</span></a></li><li><a href="../documents/">資料・申込書各種<span class="more" style="color:var(--sub);font-size:13px;margin-left:1em">詳しく見る</span></a></li><li><a href="chuoshinsa/overview.html">中央道場概要と使用日程<span class="more" style="color:var(--sub);font-size:13px;margin-left:1em">詳しく見る</span></a></li></ul></section><section class="materials"><h2>大会・審査会 最新更新情報</h2><ul style="border-top:1px solid var(--line);list-style:none;padding:0;margin:0">{updates_html}</ul></section><p class="source"><a href="https://www.kyudo.jp/schedule/">公式サイトの掲載内容を確認する</a></p></main>'''

html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated schedule/index.html successfully!")
