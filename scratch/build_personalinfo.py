import re

target_path = r"site-complete\info\personalinfo.html"

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# title & description
html = re.sub(r'<title>.*?</title>', '<title>個人情報保護方針｜公益財団法人 全日本弓道連盟</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="全弓連公式ウェブサイトにおける個人情報保護方針（プライバシーポリシー）をご案内します。">', html)

new_main = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>個人情報保護方針</div><p class="eyebrow">ご案内</p><h1>個人情報保護方針</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div><p class="summary">全弓連公式ウェブサイトでは、個人情報を保護すべき重要なものと認識し、その取り扱いに関して次の方針（プライバシーポリシー）を定めて運営・管理しております。<br>当ウェブサイトは、これらの内容をご理解のうえご利用ください。</p><section class="materials"><h2>方針の概要</h2><div style="line-height:2.1"><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 .5em">【個人情報とは】</h3><p style="margin:0 0 1.5em">この方針における個人情報とは、当ウェブサイトが運営・管理するサービスのために、ユーザからご提供頂く、ユーザの会員ＩＤ、氏名、性別、郵便番号、住所、電話番号、E-mailアドレスなどで、このうち１つまたは複数を組み合わせることでユーザ個人を特定できる情報を意味するものとします。</p><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 .5em">【個人情報の取り扱いについて】</h3><p style="margin:0 0 .8em">当ウェブサイトでは、ユーザに無断で個人情報を集めることはありません。個人情報を集める場合には、利用の目的を明らかにして、その目的以外の用途には利用しません。<br>ユーザからご提供いただいた個人情報は、次の場合を除いて第三者に開示することはありません。</p><ul style="margin:0 0 1.5em 1.5em;list-style:disc"><li>ユーザの同意がある場合。</li><li>商品等の発送にあたり、業務を運送業者などに委託する場合。</li><li>法令などにより個人情報の提供を求められた場合。</li></ul><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 .5em">【個人情報の利用目的】</h3><p style="margin:0 0 .8em">ユーザに個人情報をご提供いただく場合には、あらかじめその利用目的を当ウェブサイトに明示して、その利用目的の範囲内で利用します。事前に明示した利用目的の範囲外で利用する必要が生じた際には、利用する前にユーザにその利用目的をお知らせいたします。<br>新たな利用目的にご同意いただけない場合には、ユーザご自身の判断で拒否することができます。ただし、サービスの提供にあたり、個人情報の利用が不可欠な場合には、そのサービスを提供できないことがありますのでご了承ください。<br>ユーザからご提供いただいた個人情報は、次のような目的のために利用します。ユーザが利用を停止したい場合は、その旨を要求することができます。</p><ul style="margin:0 0 1.5em 1.5em;list-style:disc"><li>各種行事（競技会／審査会／講習会等）における参加者や入賞者等の氏名、所属、成績、称号段位、画像などの公開。</li><li>公益財団法人全日本弓道連盟、及び加盟の各都道府県連盟の活動内容の公開。</li><li>お問い合わせに対するご返信。</li><li>ご注文になられた商品等のお届け。</li><li>その他、必要に応じてユーザとご連絡を取るため。</li></ul><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 .5em">【著作権について】</h3><p style="margin:0 0 1.5em">当ウェブサイトに掲載されている情報は、著作権法により保護されています。<br>著作権者の許諾無く、私的使用など一定の範囲以外の目的で使用（複製、転載、頒布、販売、出版等を含む）することは違法行為となりますのでご注意ください。</p><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 .5em">【リンクについて】</h3><p style="margin:0 0 1.5em">当ウェブサイトにリンクを希望される際には、その旨を<a href="contact.html">お問い合わせフォーム</a>よりご連絡ください。<br>なお、サイトを確認いたしますので、お問い合わせの際には、必ずURLを記入してください。<br>ご連絡いただいたホームページが全日本弓道連盟の趣旨にそぐわない場合には、リンクをお断りすることもありますのでご了承ください。また、リンク許可後も、全日本弓道連盟からリンク解除の連絡があった場合には直ちに解除の処理を行ってください。</p><h3 style="color:var(--accent);font-size:16px;margin:1.5em 0 .5em">【お問い合わせ】</h3><p style="margin:0 0 1.5em">当ウェブサイトに関するお問い合わせは、<a href="contact.html">お問い合わせフォーム</a>よりご連絡ください。</p></div></section><p class="source"><a href="https://www.kyudo.jp/info/personalinfo.html">公式サイトの掲載内容を確認する</a></p></main>'''

html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated info/personalinfo.html successfully!")
