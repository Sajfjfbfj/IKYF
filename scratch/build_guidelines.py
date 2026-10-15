import re

target_path = r"site-complete\info\guidelines.html"

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# title & description
html = re.sub(r'<title>.*?</title>', '<title>倫理に関するガイドラインと相談窓口｜公益財団法人 全日本弓道連盟</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="本連盟は、弓道関係者によるセクハラ・パワハラ・暴力行為等を根絶するため、「倫理に関するガイドライン」を制定し、相談窓口を設置しました。">', html)

new_main = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>倫理に関するガイドラインと相談窓口</div><p class="eyebrow">ご案内</p><h1>倫理に関するガイドラインと相談窓口</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div><p class="summary">本連盟は、弓道関係者によるセクハラ・パワハラ・暴力行為等を根絶するため、「倫理に関するガイドライン」を制定し、相談窓口を設置しました。<br>相談窓口は、本連盟の活動に関係してなされた上記行為についての通報を受けつける窓口です。</p><section class="materials"><h2>相談窓口について</h2><div style="background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:6px;padding:24px 28px;margin:1.5em 0;line-height:2"><h3 style="color:var(--accent);font-size:16px;margin:0 0 1em">１．相談・通報できる方</h3><p style="margin:0 0 1.5em">(1) 弓道関係者（本連盟および加盟団体の登録会員・役員・職員等）<br>(2) 過去に弓道関係者であった者</p><h3 style="color:var(--accent);font-size:16px;margin:0 0 1em">２．相手方</h3><p style="margin:0 0 1.5em">弓道関係者（過去に弓道関係者であった者は対象外）</p><h3 style="color:var(--accent);font-size:16px;margin:0 0 1em">３．取扱事案</h3><p style="margin:0 0 1.5em">本連盟の活動に関して行われた<br>(1) セクハラ・パワハラ・暴力行為等<br>(2) 競技の結果に影響を及ぼす不正行為<br>(3) 反社会的勢力との関わり</p><h3 style="color:var(--accent);font-size:16px;margin:0 0 1em">４．通報方法</h3><div class="tbl" style="margin-bottom:1.5em"><table><tbody><tr><th style="width:120px">メール</th><td><a href="contact.html">お問い合わせフォームはこちら</a></td></tr><tr><th>郵送</th><td>〒160-0013 東京都新宿区霞ヶ丘町4番2号 JAPAN SPORT OLYMPIC SQUARE<br>(公財) 全日本弓道連盟 相談窓口 係</td></tr><tr><th>FAX</th><td>03-6447-2981</td></tr></tbody></table></div><p style="font-size:13px;color:var(--sub);margin:.5em 0">※通報者と相手方の登録情報の確認及び調査の確実性を期すため、通報には原則氏名を明記するようお願いします。<br>※匿名による通報の場合には、「相談内容の真実性について相当な根拠を示す情報や資料」が必要となりますので、問題行為に関する写真・録音・動画や目撃者情報等をご提供ください。</p><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 1em">５．通報からの流れ</h3><div style="background:rgba(255,255,255,.03);padding:16px 20px;border-left:3px solid var(--accent);line-height:2;font-size:14px">通 報<br>↓<br>弓道関係者および取扱事案に該当するか等の確認<br>↓<br>通報者による調査等申立書の作成・提出<br>↓<br>相談窓口による事実調査<br>↓<br>（事案により）倫理委員会による審理<br>↓<br>（事案により）理事会による対象者の処分</div></div></section><section class="materials"><h2>関連資料（ガイドライン・宣言）</h2><ul><li><a href="../pdf/info/guidelines_1.pdf">公益財団法人全日本弓道連盟 倫理に関するガイドライン<span class="pdf">PDF</span></a></li><li><a href="../pdf/info/guidelines_2.pdf">スポーツ界における暴力行為根絶宣言<span class="pdf">PDF</span></a></li></ul></section><p class="source"><a href="https://www.kyudo.jp/info/guidelines.html">公式サイトの掲載内容を確認する</a></p></main>'''

html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated info/guidelines.html successfully!")
