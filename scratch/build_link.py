import re

target_path = r"site-complete\info\link.html"

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# title & description
html = re.sub(r'<title>.*?</title>', '<title>リンク｜公益財団法人 全日本弓道連盟</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="スポーツ関連団体、武道関連団体、加盟団体等の関連リンク集です。">', html)

links_data = [
    ("文部科学省", "http://www.mext.go.jp/", "中高一貫教育の解説や生涯学習政策、学習指導要領の全文がご覧になれます。また、各種統計情報や各種審議会情報等の掲載も行っています。"),
    ("公益財団法人日本スポーツ協会（旧日本体育協会）", "https://www.japan-sports.or.jp/", "協会の概要や、国民スポーツ大会等の活動紹介の他、スポーツ指導員、アスレティックトレーナー等の資格取得情報、加盟団体の一覧等の情報がご覧になれます。"),
    ("公益財団法人日本オリンピック委員会", "https://www.joc.or.jp/", "事業概要、国際総合競技大会情報やオリンピックを目指す選手達の紹介等の掲載をしています。"),
    ("公益財団法人全国高等学校体育連盟弓道専門部", "http://www.kyudo-zenkoku.jp/", "競技規則や全国大会参加の心得、技能優秀選考規定の他、各種大会の記録、弓道部の実態調査などの資料も掲載しています。"),
    ("全日本学生弓道連盟", "http://www.pac.ne.jp/zennichi/", "全国の大学弓道部を統括する連盟の公式情報です。"),
    ("公益財団法人日本武道館", "http://www.nipponbudokan.or.jp/", "事業紹介、武道振興事業の説明、様々なイベントの日程のほか、施設の総合案内がご覧になれます。"),
    ("独立行政法人日本スポーツ振興センター", "https://www.jpnsport.go.jp/", "スポーツの振興や子どもたちの健康の増進を図るために設置されている文部科学省所管の独立行政法人です。スポーツ振興くじtotoの管理運営も行っています。"),
    ("公益財団法人スポーツ安全協会", "https://www.sportsanzen.org/", "協会の概要、スポーツ安全保険や子どもプラン補償制度についての説明を掲載しています。"),
    ("全国野鳥密猟対策連絡会", "http://www008.upp.so-net.ne.jp/mittairen/", "野鳥の違法な捕獲・飼養・販売の防止対策活動を推進し密猟問題の解決に努めている連絡会です。"),
    ("公益財団法人 日本アンチ・ドーピング機構", "https://www.playtruejapan.org/", "クリーンで公正なスポーツ環境を守るアンチ・ドーピング機関の公式サイトです。"),
    ("全日本弓道具協会", "http://kyudogu.jp/", "弓道具を通じた弓道の普及、伝統技術の継承、保存等を目的とした団体です。各地の弓具店会員情報を見ることができます。"),
]

list_items = []
for name, url, desc in links_data:
    item = f'''<li style="padding:1.4em 0;border-bottom:1px solid var(--line)"><div style="display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px;margin-bottom:.4em"><a href="{url}" target="_blank" rel="noopener" style="font-size:16px;font-weight:600;color:var(--ink)">{name} ↗</a><span style="font-size:12px;color:var(--accent);font-family:Arial,sans-serif">{url}</span></div><p style="margin:0;font-size:13px;color:var(--sub);line-height:1.8">{desc}</p></li>'''
    list_items.append(item)

links_html = '\n'.join(list_items)

new_main = f'''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>リンク</div><p class="eyebrow">ご案内</p><h1>リンク集</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div><p class="summary">スポーツ関連機関、武道団体、学生弓道連盟など、関連する組織・団体のリンク集です。</p><section class="materials"><h2>関連団体・機関リンク</h2><ul style="border-top:1px solid var(--line);list-style:none;padding:0;margin:0">{links_html}</ul></section><p class="source"><a href="https://www.kyudo.jp/info/link.html">公式サイトの掲載内容を確認する</a></p></main>'''

html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated info/link.html successfully!")
