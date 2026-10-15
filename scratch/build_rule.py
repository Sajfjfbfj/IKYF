import os
import re
from bs4 import BeautifulSoup

def build_rule():
    mirror_path = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\aboutus\rule.html"
    target_path = r"site-complete\aboutus\rule.html"

    with open(mirror_path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    div_c = soup.find('div', class_='contents')

    # 各章ごとに section を構築
    # div_c の中には h3.title と cntbox が交互にある
    sections_html = []
    
    # 序文
    intro = div_c.find('div', class_='introduction')
    intro_text = intro.get_text(strip=True) if intro else "公益財団法人 全日本弓道連盟 定款"

    current_h3 = None
    current_items = []

    for elem in div_c.children:
        if not elem.name:
            continue
        if elem.name in ['h3', 'h2']:
            h_text = elem.get_text(strip=True)
            if h_text == "連盟規約":
                continue
            if current_h3:
                # 前のセクションを出力
                sec = f'<section class="materials"><h2>{current_h3}</h2>\n' + '\n'.join(current_items) + '\n</section>'
                sections_html.append(sec)
                current_items = []
            current_h3 = h_text
        elif elem.name in ['div', 'dl', 'table', 'p']:
            # cntbox の中の dl.rule などを整形
            dls = elem.find_all('dl', class_='rule') if elem.name == 'div' else ([elem] if elem.name == 'dl' else [])
            if dls:
                for dl in dls:
                    dts = dl.find_all('dt')
                    dds = dl.find_all('dd')
                    dl_parts = ['<dl class="rule" style="margin:1.5em 0;line-height:2">']
                    for dt, dd in zip(dts, dds):
                        dt_txt = dt.get_text(strip=True)
                        dd_html = "".join(str(c) for c in dd.contents).strip()
                        dl_parts.append(f'<dt style="font-weight:600;color:var(--accent);margin-top:1.2em">{dt_txt}</dt>')
                        dl_parts.append(f'<dd style="margin:0.4em 0 1em 1.5em;color:var(--ink)">{dd_html}</dd>')
                    dl_parts.append('</dl>')
                    current_items.append('\n'.join(dl_parts))
            else:
                txt = elem.get_text(strip=True)
                if txt and txt != intro_text:
                    current_items.append(f'<p style="margin:1em 0">{txt}</p>')

    if current_h3:
        sec = f'<section class="materials"><h2>{current_h3}</h2>\n' + '\n'.join(current_items) + '\n</section>'
        sections_html.append(sec)

    all_sections = '\n'.join(sections_html)

    with open(target_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # title
    html = re.sub(r'<title>.*?</title>', '<title>連盟規約｜公益財団法人 全日本弓道連盟</title>', html)
    # meta description
    html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="公益財団法人 全日本弓道連盟 定款・規約を掲載しています。">', html)

    # main 置換
    new_main = f'''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">全日本弓道連盟について</a><span>›</span>連盟規約</div><p class="eyebrow">連盟について</p><h1>連盟規約</h1><div class="meta"><span>公益財団法人 全日本弓道連盟 定款</span></div><p class="summary">{intro_text}</p>{all_sections}<p class="source"><a href="https://www.kyudo.jp/aboutus/rule.html">公式サイトの掲載内容を確認する</a></p></main>'''

    html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Updated {target_path} successfully!")

if __name__ == '__main__':
    build_rule()
