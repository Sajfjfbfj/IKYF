"""
Build site-complete/news/ pages:
- index.html
- news_20260302.html
- news_20260220.html
- news_202208.html
- news_202208_01.html
using site-complete design and typography.
"""
import os
import re

os.makedirs(r'site-complete\news', exist_ok=True)

# Read base template from site-complete/info/guidelines.html
with open(r'site-complete\info\guidelines.html', encoding='utf-8') as f:
    template = f.read()

def create_page(title, crumb_label, main_html, dest_path):
    # Replace main in template
    out = re.sub(r'<main class="wrap">.*?</main>', main_html, template, flags=re.DOTALL)
    # Fix page title
    out = re.sub(r'<title>[^<]*</title>', f'<title>{title}｜連盟からのお知らせ｜公益財団法人 全日本弓道連盟</title>', out)
    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as fp:
        fp.write(out)
    print(f"Created: {dest_path}")

# 1. news_20260302.html
main_20260302 = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">連盟からのお知らせ</a><span>›</span>第５回世界弓道大会（2028）東京開催決定</div>
<p class="eyebrow">連盟からのお知らせ</p>
<h1>IKYF総会にて「第５回世界弓道大会（2028）」の日本（東京）開催が決定いたしました。</h1>
<div class="meta"><span>2026年3月2日</span><span>公益財団法人 全日本弓道連盟</span></div>

<div class="lead" style="display:flex;gap:28px;align-items:flex-start;flex-wrap:wrap;margin:28px 0">
<figure style="margin:0;max-width:400px;flex:1 1 300px">
  <img src="../img/news/02/sekaitaikai_2028_01.jpg" alt="第５回世界弓道大会" style="width:100%;height:auto;border-radius:6px;border:1px solid var(--line)" loading="lazy">
</figure>
<div style="flex:2 1 320px;font-size:1.05rem;line-height:2">
  <p>2026年2月12日（木）に開かれた国際弓道連盟（IKYF）の総会にて、「第５回世界弓道大会」が2028年11月に日本・東京で開催されることが決定いたしました。</p>
  <p style="margin-top:16px;color:var(--sub)">大会の詳細、日程、要項等につきましては決定次第、公式サイトおよび月刊「弓道」にて順次お知らせいたします。</p>
</div>
</div>

<section class="materials">
<h2>関連リンク</h2>
<ul>
<li><a href="../schedule/taikai/">大会・行事スケジュール一覧<span class="more">詳しく見る</span></a></li>
<li><a href="../schedule/chuoshinsa/">中央審査会スケジュール一覧<span class="more">詳しく見る</span></a></li>
<li><a href="index.html">連盟からのお知らせ一覧へ戻る<span class="more">詳しく見る</span></a></li>
</ul>
</section>
<p class="source"><a href="https://www.kyudo.jp/news/news_20260302.html">公式サイトの掲載内容を確認する</a></p></main>'''

create_page(
    "「第５回世界弓道大会（2028）」日本（東京）開催決定",
    "第５回世界弓道大会（2028）東京開催決定",
    main_20260302,
    r'site-complete\news\news_20260302.html'
)

# 2. news_20260220.html
main_20260220 = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">連盟からのお知らせ</a><span>›</span>小越智就錬士六段 インタビュー記事掲載</div>
<p class="eyebrow">連盟からのお知らせ</p>
<h1>NEXT STORIESに小越智就錬士六段のインタビュー記事が掲載されました。</h1>
<div class="meta"><span>2026年2月20日</span><span>公益財団法人 全日本弓道連盟</span></div>

<div class="lead" style="display:flex;gap:28px;align-items:flex-start;flex-wrap:wrap;margin:28px 0">
<figure style="margin:0;max-width:400px;flex:1 1 300px">
  <a href="https://nextstories.jp/tomonari_okoshi" target="_blank" rel="noopener"><img src="../img/news/02/okoshi_tomonari_01.jpg" alt="小越智就錬士六段" style="width:100%;height:auto;border-radius:6px;border:1px solid var(--line)" loading="lazy"></a>
</figure>
<div style="flex:2 1 320px;font-size:1.05rem;line-height:2">
  <p>小越智就錬士六段（東京）がスポーツWebメディア NEXT STORIESに取材されました。<br>ぜひ記事をご覧ください。</p>
  <div style="margin:20px 0;padding:16px 20px;background:rgba(255,255,255,0.04);border-radius:6px;border:1px solid var(--line)">
    <p style="font-weight:700;margin-bottom:8px">■ 28歳、天皇盃最年少優勝。小越智就が証明した弓道の可能性</p>
    <a href="https://nextstories.jp/tomonari_okoshi" target="_blank" rel="noopener" style="color:var(--accent);word-break:break-all">https://nextstories.jp/tomonari_okoshi</a>
  </div>
  <p style="font-size:0.88rem;color:var(--sub)">※この企画は、夢へのチャレンジを応援する「海外FXのSong」の協賛により制作されました。</p>
</div>
</div>

<section class="materials">
<h2>関連リンク</h2>
<ul>
<li><a href="../aboutus/book.html">月刊「弓道」刊行物情報<span class="more">詳しく見る</span></a></li>
<li><a href="index.html">連盟からのお知らせ一覧へ戻る<span class="more">詳しく見る</span></a></li>
</ul>
</section>
<p class="source"><a href="https://www.kyudo.jp/news/news_20260220.html">公式サイトの掲載内容を確認する</a></p></main>'''

create_page(
    "NEXT STORIESに小越智就錬士六段のインタビュー記事掲載",
    "小越智就錬士六段 インタビュー記事掲載",
    main_20260220,
    r'site-complete\news\news_20260220.html'
)

# 3. news_202208.html
main_202208 = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">連盟からのお知らせ</a><span>›</span>「劇場版ツルネ」公開のお知らせ</div>
<p class="eyebrow">連盟からのお知らせ</p>
<h1>弓道をテーマにしたアニメ映画「劇場版ツルネ ーはじまりの一射ー」公開</h1>
<div class="meta"><span>2022年8月</span><span>公益財団法人 全日本弓道連盟</span></div>

<p class="summary">弓道をテーマにしたアニメ映画「劇場版ツルネ ーはじまりの一射ー」が8月19日から公開になります。弓道を志すすべての人におすすめの映画です。</p>

<div style="margin:28px 0;text-align:center">
  <a href="news_202208_01.html">
    <img src="../img/news/01/gK_01.jpg" alt="劇場版ツルネ はじまりの一射" style="max-width:100%;height:auto;border-radius:6px;border:1px solid var(--line)" loading="lazy">
  </a>
  <div style="margin-top:16px">
    <a href="news_202208_01.html" style="display:inline-block;padding:10px 24px;background:var(--accent);color:#14121c;border-radius:6px;font-weight:700">作品紹介・あらすじ・キャラクター紹介を見る</a>
  </div>
</div>

<section class="materials">
<h2>関連リンク</h2>
<ul>
<li><a href="news_202208_01.html">「劇場版ツルネ」作品紹介・あらすじ・登場人物<span class="more">詳しく見る</span></a></li>
<li><a href="../begin/index.html">見学・入門 弓道を始めたい方へ<span class="more">詳しく見る</span></a></li>
<li><a href="index.html">連盟からのお知らせ一覧へ戻る<span class="more">詳しく見る</span></a></li>
</ul>
</section>
<p class="source"><a href="https://www.kyudo.jp/news/news_202208.html">公式サイトの掲載内容を確認する</a></p></main>'''

create_page(
    "「劇場版ツルネ ーはじまりの一射ー」公開のお知らせ",
    "「劇場版ツルネ」公開のお知らせ",
    main_202208,
    r'site-complete\news\news_202208.html'
)

# 4. news_202208_01.html
main_202208_01 = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">連盟からのお知らせ</a><span>›</span><a href="news_202208.html">劇場版ツルネ</a><span>›</span>作品紹介</div>
<p class="eyebrow">連盟からのお知らせ</p>
<h1>「劇場版ツルネ ーはじまりの一射ー」作品紹介</h1>
<div class="meta"><span>2022年8月</span><span>公益財団法人 全日本弓道連盟</span></div>

<p class="summary">弓道をテーマにしたアニメ映画「劇場版ツルネ ーはじまりの一射ー」が8月19日から公開になります。綾野ことこの同名小説。弓道を志すすべての人におすすめの映画です。</p>

<section class="materials">
<h2>作品紹介</h2>
<div style="display:flex;gap:24px;align-items:flex-start;flex-wrap:wrap;margin:16px 0">
  <figure style="margin:0;max-width:320px;flex:1 1 240px">
    <a href="http://tsurune.com/" target="_blank" rel="noopener"><img src="../img/news/01/tsurune_01.jpg" alt="ツルネ ポスター" style="width:100%;height:auto;border-radius:6px;border:1px solid var(--line)" loading="lazy"></a>
  </figure>
  <div style="flex:2 1 300px;font-size:0.95rem;line-height:2">
    <p><strong>「弦音」＝ツルネ</strong><br>矢を放ったときに鳴る弦の音。射手にとって美しい弦音を響かせることは喜びであり、その美しい音は人の心をとらえて離さない。</p>
    <p>同一人物が同じ道具を使ったとしても同じ弦音を発することはできず、まさに一期一会。一射一射が、一生に一度の〈出会い〉と〈別れ〉である。</p>
    <p>果てのない弓の道を歩み始める高校生たちの青春〝弓道〟アニメーション！</p>
    <p style="font-size:0.88rem;color:var(--sub);margin-top:12px">アニメーション制作：京都アニメーション／配給：松竹／製作：ツルネ製作委員会</p>
  </div>
</div>
</section>

<section class="materials">
<h2>あらすじ</h2>
<div style="line-height:2;font-size:0.95rem">
  <p>鳴宮湊は、弓引きの病とも言われる「早気」にかかり、弓道から身を引くことにした。</p>
  <p>高校に進学後、親友の竹早静弥が弓道部に入ると言っても、湊の気持ちは変わらない。</p>
  <p>だが、滝川雅貴と運命的な出会いを果たし、湊は傷つきながらも再び弓を手に取る。「弓道部に戻って、いろいろなものが見えてきた気がするんだ」</p>
  <p>雅貴は湊を指導する一方で、自分の師匠に深い復讐心を抱いていた。「俺は、あいつみたいな師匠にはならない」</p>
  <p>ともに歩み始めた雅貴と湊。これまで湊を支えてきた静弥は、自分はもう必要のない存在だと思い始める。「僕は、滝川さん。あなたが嫌いです」</p>
  <p>弓への苦しみにもがき続ける湊、師への愛憎にさいなまれる雅貴、友への想いに追い詰められる静弥。彼らが、たどりつく先は―――。</p>
</div>
</section>

<section class="materials">
<h2>キャラクター紹介</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:20px;margin-top:16px">
  <div style="background:rgba(255,255,255,0.04);border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center">
    <img src="../img/news/01/characterPicture1.png" alt="鳴宮 湊" style="max-width:140px;height:auto;margin-bottom:8px" loading="lazy">
    <h3 style="margin:4px 0;font-size:1.1rem">鳴宮 湊</h3>
    <p style="color:var(--accent);font-size:0.85rem;margin:0 0 8px">CV. 上村祐翔</p>
    <p style="font-size:0.82rem;line-height:1.7;text-align:left;color:var(--sub)">「美しい弦音を響かせたい」という想いで弓道を始める。早気が原因で弓道を辞めていたが、雅貴の射に出会い、再び弦音を取り戻そうと風舞高校弓道部へ入部する。</p>
  </div>
  <div style="background:rgba(255,255,255,0.04);border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center">
    <img src="../img/news/01/characterPicture2.png" alt="滝川雅貴" style="max-width:140px;height:auto;margin-bottom:8px" loading="lazy">
    <h3 style="margin:4px 0;font-size:1.1rem">滝川雅貴</h3>
    <p style="color:var(--accent);font-size:0.85rem;margin:0 0 8px">CV. 浅沼晋太郎</p>
    <p style="font-size:0.82rem;line-height:1.7;text-align:left;color:var(--sub)">弓の師匠であった祖父に憧れ、弓道を続けてきた。夜多神社の神主を務めるかたわら、風舞高校弓道部のコーチとして湊たちを導く。</p>
  </div>
  <div style="background:rgba(255,255,255,0.04);border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center">
    <img src="../img/news/01/characterPicture3.png" alt="竹早静弥" style="max-width:140px;height:auto;margin-bottom:8px" loading="lazy">
    <h3 style="margin:4px 0;font-size:1.1rem">竹早静弥</h3>
    <p style="color:var(--accent);font-size:0.85rem;margin:0 0 8px">CV. 市川 蒼</p>
    <p style="font-size:0.82rem;line-height:1.7;text-align:left;color:var(--sub)">湊の幼馴染。風舞高校では弓道部の部長を務め、冷静沈着に部員たちを支える。</p>
  </div>
  <div style="background:rgba(255,255,255,0.04);border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center">
    <img src="../img/news/01/characterPicture4.png" alt="山之内遼平" style="max-width:140px;height:auto;margin-bottom:8px" loading="lazy">
    <h3 style="margin:4px 0;font-size:1.1rem">山之内遼平</h3>
    <p style="color:var(--accent);font-size:0.85rem;margin:0 0 8px">CV. 鈴木崚汰</p>
    <p style="font-size:0.82rem;line-height:1.7;text-align:left;color:var(--sub)">風舞高校弓道部1年。高校から本格的に弓道を始めた初心者。争いを好まず真心で接する。</p>
  </div>
  <div style="background:rgba(255,255,255,0.04);border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center">
    <img src="../img/news/01/characterPicture5.png" alt="如月七緒" style="max-width:140px;height:auto;margin-bottom:8px" loading="lazy">
    <h3 style="margin:4px 0;font-size:1.1rem">如月七緒</h3>
    <p style="color:var(--accent);font-size:0.85rem;margin:0 0 8px">CV. 矢野奨吾</p>
    <p style="font-size:0.82rem;line-height:1.7;text-align:left;color:var(--sub)">風舞高校弓道部1年。人目を引くルックスと朗らかな人柄。海斗の従兄弟。</p>
  </div>
  <div style="background:rgba(255,255,255,0.04);border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center">
    <img src="../img/news/01/characterPicture6.png" alt="小野木海斗" style="max-width:140px;height:auto;margin-bottom:8px" loading="lazy">
    <h3 style="margin:4px 0;font-size:1.1rem">小野木海斗</h3>
    <p style="color:var(--accent);font-size:0.85rem;margin:0 0 8px">CV. 石川界人</p>
    <p style="font-size:0.82rem;line-height:1.7;text-align:left;color:var(--sub)">風舞高校弓道部1年・副部長。人一倍真面目に弓道と向き合い、情に厚い一面も持つ。</p>
  </div>
</div>
</section>

<section class="materials">
<h2>関連リンク</h2>
<ul>
<li><a href="news_202208.html">「劇場版ツルネ」公開のお知らせへ戻る<span class="more">詳しく見る</span></a></li>
<li><a href="index.html">連盟からのお知らせ一覧へ戻る<span class="more">詳しく見る</span></a></li>
</ul>
</section>
<p class="source"><a href="https://www.kyudo.jp/news/news_202208_01.html">公式サイトの掲載内容を確認する</a></p></main>'''

create_page(
    "「劇場版ツルネ」作品紹介・登場人物",
    "「劇場版ツルネ」作品紹介",
    main_202208_01,
    r'site-complete\news\news_202208_01.html'
)

# 5. index.html
main_index = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span>連盟からのお知らせ（特集・ニュース）</div>
<p class="eyebrow">ニュース</p>
<h1>連盟からのお知らせ（特集・ニュース）</h1>
<div class="meta"><span>公益財団法人 全日本弓道連盟</span></div>

<section class="materials">
<h2>最新のニュース・特集</h2>
<p class="lead">全日本弓道連盟の最新情報、メディア掲載、特集記事一覧です。</p>
<ul>
<li><a href="news_20260302.html">IKYF総会にて「第５回世界弓道大会（2028）」の日本（東京）開催が決定いたしました。<span class="more">2026.03.02</span></a></li>
<li><a href="news_20260220.html">NEXT STORIESに小越智就錬士六段のインタビュー記事が掲載されました。<span class="more">2026.02.20</span></a></li>
<li><a href="news_202208.html">アニメ映画「劇場版ツルネ ーはじまりの一射ー」公開のお知らせ<span class="more">2022.08.19</span></a></li>
<li><a href="news_202208_01.html">「劇場版ツルネ ーはじまりの一射ー」作品紹介・あらすじ・キャラクター紹介<span class="more">詳しく見る</span></a></li>
</ul>
</section>

<section class="materials">
<h2>関連コンテンツ</h2>
<ul>
<li><a href="../notice/index.html">連盟からのお知らせ（告知板・審査結果）<span class="more">詳しく見る</span></a></li>
<li><a href="../schedule/index.html">大会・審査会スケジュール<span class="more">詳しく見る</span></a></li>
<li><a href="../aboutus/book.html">月刊「弓道」刊行物情報<span class="more">詳しく見る</span></a></li>
</ul>
</section>
<p class="source"><a href="https://www.kyudo.jp/news/">公式サイトの掲載内容を確認する</a></p></main>'''

create_page(
    "連盟からのお知らせ（特集・ニュース）一覧",
    "連盟からのお知らせ（特集・ニュース）",
    main_index,
    r'site-complete\news\index.html'
)

print("All news pages successfully created!")
