import re

target_path = r"site-complete\info\usearrow.html"

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# title & description
html = re.sub(r'<title>.*?</title>', '<title>矢羽の使用に関する準則ならびに関係資料｜公益財団法人 全日本弓道連盟</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="矢羽の使用に関する準則ならびに関係資料、トレーサビリティ証明書の様式・記入要領をご案内します。">', html)

new_main = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>矢羽の使用に関する準則ならびに関係資料</div><p class="eyebrow">ご案内</p><h1>矢羽の使用に関する準則<br>ならびに関係資料</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div><div class="summary" style="line-height:2.1"><p>近時、ワシタカ類の羽根を用いた矢羽に関して、関連法令等に違反する取引がなされていた可能性があり、この問題につき昨年３月に調査委員会を設置して調査を行っていたことは、既にホームページでご案内したとおりです。</p><p style="margin-top:1em">当連盟では、同調査委員会の報告を受けて、矢羽の使用に関するルール（準則）を検討してまいりましたが、この度「矢羽の使用に関する準則」を制定しました。また４月２８日には本準則の運用に関する説明会を開催して、各加盟団体に周知を図るようご依頼したところです。</p><p style="margin-top:1em">各位におかれましては準則ならびに運用マニュアル等関係資料をご覧いただき、トレーサビリティ証明書の作成・携行など、適正な矢羽の使用についてご理解ご協力を賜りますようお願い申し上げます。</p></div><section class="materials"><h2>関係資料一覧・ダウンロード</h2><ul><li><a href="../pdf/info/usearrow_1.pdf">1. 【会員の皆様へ】矢羽の使用に関する準則制定のお知らせ<span class="pdf">PDF</span></a></li><li><a href="../pdf/info/usearrow_2.pdf">2. 矢羽の使用に関する準則<span class="pdf">PDF</span></a></li><li><a href="../pdf/info/usearrow_3.pdf">3. 羽根の使用等に関する早見表<span class="pdf">PDF</span></a></li><li><a href="../pdf/info/usearrow_4-1.docx">4-1. トレーサビリティ証明書<span class="pdf" style="border-color:#5c9cd8;color:#5c9cd8">Word</span></a></li><li><a href="../pdf/info/usearrow_4-2.pdf">4-2. トレーサビリティ証明書 記入説明書<span class="pdf">PDF</span></a></li><li><a href="../pdf/info/usearrow_5.pdf">5. 【矢羽の使用に関する準則】の運用マニュアル(4月30日版)<span class="pdf">PDF</span></a></li><li><a href="../pdf/info/usearrow_6.pdf">6. 矢羽の取引の問題について(経緯報告)<span class="pdf">PDF</span></a></li></ul><p class="note" style="margin-top:1.5em">※トレーサビリティ証明書を作成の際には上記データをダウンロードしてご使用ください。</p></section><p class="source"><a href="https://www.kyudo.jp/info/usearrow.html">公式サイトの掲載内容を確認する</a></p></main>'''

html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated info/usearrow.html successfully!")
