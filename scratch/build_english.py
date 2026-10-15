import re

target_path = r"site-complete\info\english.html"

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# title & description
html = re.sub(r'<title>.*?</title>', '<title>English Guide｜All Nippon Kyudo Federation</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="General information and outline of the All Nippon Kyudo Federation (ANKF) in English.">', html)

new_main = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>English</div><p class="eyebrow">Information</p><h1>All Nippon Kyudo Federation</h1><div class="meta"><span>公益財団法人 全日本弓道連盟 (ANKF)</span></div><div class="summary" style="line-height:2.1"><p>Kyudo is a traditional discipline that uses the Japanese bow for both recreation and sport as well as the training of body and mind.<br>The All Nippon Kyudo Federation (ANKF) is the governing body for kyudo in Japan and under the auspice of the International Kyudo Federation (IKYF) is responsible for the promotion and development of kyudo worldwide.</p></div><section class="materials"><h2>The outline of ALL NIPPON KYUDO FEDERATION</h2><p style="margin-bottom:1em">All Nippon Kyudo Federation responsibilities:</p><ol style="line-height:2;padding-left:1.5em;margin-bottom:2em"><li>1. Establishment of general policies in terms of the dissemination and promotion of kyudo.</li><li>2. Organization of national and international competition and events.</li><li>3. Assessment of instructors (shogo title holders) and examination for the kyudo and dan grade levels.</li><li>4. Implementation of research and studies, and the organization of workshops.</li><li>5. Publication of journals and information.</li><li>6. Other projects necessary to accomplish its purposes.</li></ol><p style="line-height:2">The birthplace of kyudo is Japan and as such the All Nippon Kyudo Federation is responsible for the development of kyudo and keeping standards of practice to the many national organizations that are found throughout the world.</p></section><section class="materials"><h2>Address and Contacts</h2><div style="background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:6px;padding:24px 28px;margin:1.5em 0;line-height:2"><p style="font-size:17px;font-weight:600;margin:0 0 .5em">All Nippon Kyudo Federation</p><p style="margin:.3em 0">JAPAN SPORT OLYMPIC SQUARE<br>4-2, KASUMIGAOKA-MACHI, SHINJUKU-KU, TOKYO<br>160-0013 JAPAN</p><p style="margin:.5em 0">FAX: +81-3-3481-2398</p><p style="margin:.5em 0"><a href="contact.html" style="color:var(--accent);border-bottom:1px solid var(--accent);padding-bottom:2px">Contact Us (Online Form)</a></p></div></section><p class="source"><a href="https://www.kyudo.jp/info/english.html">View original page on official website</a></p></main>'''

html = re.sub(r'<main class="wrap">.*?</main>', new_main, html, flags=re.DOTALL)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated info/english.html successfully!")
