"""
Build site-complete/improve/02.html
matching the exact design and dark theme of site-complete/improve/index.html
"""
import re

# Read template from improve/index.html
with open(r'site-complete\improve\index.html', encoding='utf-8') as f:
    template = f.read()

# Build main content for vol.02
main_content = '''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">上達への道。</a><span>›</span>vol.02</div>
<div class="lead"><div class="lead-text"><p class="eyebrow">上達への道。</p><h1><span class="pre">上達への道。vol.02　効果的な“素引き練習”で基礎を習得する</span>素引き練習法</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span><span>月刊「弓道」連載</span></div><p class="summary">月刊「弓道」の連載「上達への道。」の第2回。実際に弓を持ち、手の内のつくり方や弓の張り方を覚えながら、射法八節に沿って正しいバランス感覚を身につける素引き練習法を、写真つきで紹介しています。</p></div><figure class="cover"><img src="../img/improve/book201809.png" alt="月刊弓道" loading="lazy"><figcaption>月刊「弓道」</figcaption></figure></div>

<section class="about"><h2>素引き練習とは</h2><div class="about-body"><p class="body">実際に弓を持ち、矢を番えずに射法八節の動作を行う練習法です。前回のゴム弓練習で身につけた形を、実際の弓の重みや張力の中で確かめます。</p><p class="body">はじめに覚えるのは「手の内のつくり方（左手で弓を正しく握ること）」と「バランス感覚」です。何度も素引き練習を重ねることで、余計な力みが抜け、安定した射形が身につきます。</p></div><figure class="tool"><img src="../img/improve/yumi.png" alt="弓" loading="lazy"></figure></section>

<section class="about"><h2>弓の張り方を覚えよう！</h2><div class="about-body"><p class="body">弓を押さえる人が末弭（弓の上部先端）を右手の手のひらでしっかり押さえ、張る人は左手で握りの下あたりをつかみ、右手で弦輪を持ちます。</p><p class="body">張る人が腰をかがめ、左足の太ももに弓を乗せ、弦輪がピンと張るように左手で握りの下を押しながら、本弭（弓の下部）に弦輪をかけます。<br><small class="quiet">※弓張り板が設置されている場所では、指導に従って的確に張りましょう。</small></p></div><div class="ph-row" style="display:flex;gap:16px;flex-wrap:wrap;margin-top:16px"><figure class="ph" style="flex:1;min-width:140px"><img src="../img/improve/improve02HARI01.jpg" alt="弓の張り方1" loading="lazy"></figure><figure class="ph" style="flex:1;min-width:140px"><img src="../img/improve/improve02HARI02.jpg" alt="弓の張り方2" loading="lazy"></figure><figure class="ph" style="flex:1;min-width:140px"><img src="../img/improve/improve02HARI03.jpg" alt="弓の張り方3" loading="lazy"></figure></div></section>

<section class="about"><h2>手の内のつくり方</h2><p class="lead">射を決めるのが手の内です。正しい基礎を覚え、確実に調えられるように学びましょう。</p><div class="ph-row" style="display:flex;gap:20px;flex-wrap:wrap;margin-top:16px"><div style="flex:1;min-width:200px"><img src="../img/improve/improve02hand01.jpg" alt="手の内のつくり方1" loading="lazy"><h4 style="margin:8px 0 4px">1. 左手の「天紋筋」に弓を当てる</h4><p style="font-size:0.88rem;color:var(--sub)">天紋筋に弓と手のひらが直角になるように、弓の外竹の左角を当てます。親指以外の指は伸ばします。</p></div><div style="flex:1;min-width:200px"><img src="../img/improve/improve02hand02.jpg" alt="手の内のつくり方2" loading="lazy"><h4 style="margin:8px 0 4px">2. 親指で弓をつかむ</h4><p style="font-size:0.88rem;color:var(--sub)">親指と人さし指の間の「虎口」の皮を、弓にあてがうようにして巻き込みます。親指以外の指は伸ばしたままにします。</p></div><div style="flex:1;min-width:200px"><img src="../img/improve/improve02hand03.jpg" alt="手の内のつくり方3" loading="lazy"><h4 style="margin:8px 0 4px">3. 包むような感覚で握る</h4><p style="font-size:0.88rem;color:var(--sub)">人さし指以外を弓を包むように内側に曲げ、中指の先と親指のはらを合わせます。素引き練習では右手も弦をしっかり握ります。</p></div></div></section>

<section class="flow"><h2>射法八節に沿った素引き練習の流れ</h2><p class="flow-lead">正しい姿勢とバランス感覚を保ちながら、各動作を確かめます。</p><ol class="steps">
<li class="step"><div class="tag"><span class="no">一</span><ruby class="nm">足踏み<rt>あしぶみ</rt></ruby></div><figure class="ph"><img src="../img/improve/improve02_01.jpg" alt="素引き 足踏み" loading="lazy"></figure><p>左手に弓を持ち、右手は腰に当て、足を左右に踏み開きます。幅は身長の約半分、角度は約60度が基本です。</p></li>
<li class="step"><div class="tag"><span class="no">二</span><ruby class="nm">胴造り<rt>どうづくり</rt></ruby></div><figure class="ph"><img src="../img/improve/improve02_02.jpg" alt="素引き 胴造り" loading="lazy"></figure><p>足踏みで調えた姿勢を保ちながら、両足の上に上体を正しく置きます。腰をすえ、左右の肩を沈め、心気を丹田におさめます。</p></li>
<li class="step"><div class="tag"><span class="no">三</span><ruby class="nm">弓構え<rt>ゆがまえ</rt></ruby></div><figure class="ph"><img src="../img/improve/improve02_03.jpg" alt="素引き 弓構え" loading="lazy"></figure><p>弓を起こして身体の中心にもち、右手で弦をしっかり握ります。両こぶしの高さをそろえ、左手は調えた手の内をつくります。</p></li>
<li class="step"><div class="tag"><span class="no">四</span><ruby class="nm">打起し<rt>うちおこし</rt></ruby></div><figure class="ph"><img src="../img/improve/improve02_04.jpg" alt="素引き 打起し" loading="lazy"></figure><p>呼吸に合わせて両腕をしなやかにすくい上げます。両こぶしは頭よりやや上にし、肩に余計な力を入れないようにします。</p></li>
<li class="step"><div class="tag"><span class="no">五</span><ruby class="nm">引分け<rt>ひきわけ</rt></ruby></div><figure class="ph"><img src="../img/improve/improve02_05.jpg" alt="素引き 引分け" loading="lazy"></figure><p>両こぶしの高さをそろえながら、左手を開き、右ひじを折り曲げて引きます。左右の肩とこぶしが平行になることが重要です。</p></li>
<li class="step"><div class="tag"><span class="no">六</span><ruby class="nm">会<rt>かい</rt></ruby></div><figure class="ph"><img src="../img/improve/improve02_06.jpg" alt="素引き 会" loading="lazy"></figure><p>引分けの状態から、身体全体を使って両腕を左右均等に張り合います。背骨をまっすぐ伸ばし、五重十文字の働きを意識します。</p></li>
</ol></section>

<section class="credit"><h2>監修・指導・スタッフ</h2><dl><div><dt>監修</dt><dd>影山 一（全日本弓道連盟理事）</dd></div><div><dt>指導</dt><dd>山田 紀之（埼玉県立川越総合高等学校弓道部顧問）</dd></div><div><dt>演武協力</dt><dd>埼玉大学弓道部</dd></div><div><dt>撮影</dt><dd>杉田 賢治</dd></div><div><dt>参考資料</dt><dd>『弓道教本第1巻』『弓道講座全4巻（DVD）』（いずれも全日本弓道連盟発行）</dd></div></dl></section>

<nav class="pager" aria-label="関連ページ"><a href="index.html"><small>前の回</small>上達への道。 vol.01（ゴム弓練習法）</a><a href="02.html"><small>第2回</small>上達への道。 vol.02（素引き練習法）</a></nav></main>'''

# Replace main block in template
html_02 = re.sub(r'<main class="wrap">.*?</main>', main_content, template, flags=re.DOTALL)
# Update title
html_02 = html_02.replace('上達への道。vol.01', '上達への道。vol.02')

with open(r'site-complete\improve\02.html', 'w', encoding='utf-8') as f:
    f.write(html_02)
print("Created site-complete/improve/02.html")

# Update improve/index.html pager
with open(r'site-complete\improve\index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

new_pager = '<nav class="pager" aria-label="関連ページ"><a href="index.html"><small>第1回</small>ゴム弓練習法</a><a href="02.html"><small>次の回</small>上達への道。 vol.02（素引き練習法）</a></nav>'
idx_content_fixed = re.sub(r'<nav class="pager"[^>]*>.*?</nav>', new_pager, idx_content, flags=re.DOTALL)

with open(r'site-complete\improve\index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content_fixed)
print("Updated site-complete/improve/index.html pager")
