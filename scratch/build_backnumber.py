"""
Build site-complete/aboutus/backnumber.html
from the mirror's backnumber.html content,
using the site-complete design (same as latestissue.html / book.html).
"""
import re

# ---- Read template (latestissue.html) ----
with open(r'site-complete\aboutus\latestissue.html', encoding='utf-8') as f:
    template = f.read()

# ---- Read mirror backnumber data ----
with open(r'scratch\backnumber_full.html', encoding='utf-8') as f:
    mirror = f.read()

# Extract all cntbox entries from mirror
# Each entry is between <!-- ▼ YYYY年M月号 ... START ▼ --> and <!-- ▲ ... END ▲ -->
entries_raw = re.findall(
    r'<!-- ▼ (.+?) -->\s*<div class="cntbox">(.*?)</div><!-- cntbox end -->',
    mirror,
    re.DOTALL
)

def build_entry_html(label, body):
    """Convert a mirror cntbox entry into our card style."""
    # Extract figure/img
    img_m = re.search(r'<figure>(.*?)</figure>', body, re.DOTALL)
    img_block = img_m.group(1).strip() if img_m else ''
    
    # Fix img src: ../img/... → ../img/...  (already relative in mirror)
    # In site-complete, img is one level deeper: site-complete/aboutus/ → ../img/
    # Mirror src="../img/..." which is already correct for our structure
    
    # Extract shop link (first <a href> in figure or infobox)
    shop_m = re.search(r'href="(https://www\.kyudo-shop\.com/[^"]*)"', body)
    shop_url = shop_m.group(1) if shop_m else 'https://www.kyudo-shop.com/'
    
    # Extract title
    title_m = re.search(r'<p class="title">(.*?)</p>', body)
    title = title_m.group(1).strip() if title_m else ''
    
    # Extract text content
    text_m = re.search(r'<div class="text">(.*?)</div>\s*</div>\s*</div><!-- monthlykyudo end -->', body, re.DOTALL)
    text_content = text_m.group(1).strip() if text_m else ''
    
    # Build img src
    img_src_m = re.search(r'src="([^"]*)"', img_block)
    img_src = img_src_m.group(1) if img_src_m else ''
    
    return f'''<div class="magazine-card">
<figure><a href="{shop_url}" target="_blank" rel="noopener"><img src="{img_src}" alt="{title} 表紙" loading="lazy"></a></figure>
<div class="magazine-info">
<p class="title">{title}</p>
<a class="shop-link" href="{shop_url}" target="_blank" rel="noopener">ご購入はこちらから</a>
<div class="text">{text_content}</div>
</div>
</div><!-- magazine-card end -->'''

# Build all entries
cards_html = '\n'.join(build_entry_html(lbl, body) for lbl, body in entries_raw)

# ---- Build main content ----
main_content = f'''<main class="wrap"><div class="crumb"><a href="../index.html">HOME</a><span>›</span><a href="index.html">全日本弓道連盟について</a><span>›</span><a href="book.html">ブック（刊行物）</a><span>›</span>月刊「弓道」 バックナンバー</div><p class="eyebrow">全日本弓道連盟について</p><h1>月刊「弓道」 バックナンバー</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div>
<section class="materials">
<h2>バックナンバー一覧</h2>
<p class="lead">月刊「弓道」のバックナンバーはオンラインショップからご購入いただけます。<br><a href="https://www.kyudo-shop.com/" target="_blank" rel="noopener">オンラインショップはこちらから</a></p>
<div class="magazine-grid">
{cards_html}
</div>
</section>
<section class="materials"><h2>ご注文についてのご案内</h2><p class="lead">全弓連の機関誌のお求めは、オンラインショップ・お電話・FAX・E-mailでもご購入いただけます。</p><table class="info-tbl"><tbody><tr><th>バックナンバーのご注文</th><td>月刊『弓道』のバックナンバーはオンラインショップからご購入いただけます。<br><a href="https://www.kyudo-shop.com/" target="_blank" rel="noopener">オンラインショップはこちらから</a></td></tr><tr><th>新規定期ご購読お申込み／<br>ご購読状況確認</th><td>月刊『弓道』購読者管理システムサポート<p class="tel">TEL: 03-3259-6269</p><span class="quiet">（月～金 10:00～17:30　※12:00～13:00除く）</span><br><a href="mailto:kikanshi-support@kyudo.jp">メールでのお問い合わせはこちら（kikanshi-support@kyudo.jp）</a></td></tr><tr><th>お問い合わせ先</th><td>公益財団法人全日本弓道連盟<br><a href="../info/contact.html">メールでのお問い合わせはこちら</a></td></tr></tbody></table></section>
<section class="materials"><h2>全日本弓道連盟について コンテンツ</h2><ul><li><a href="overview.html">概要<span class="more">詳しく見る</span></a></li><li><a href="plan.html">中期計画<span class="more">詳しく見る</span></a></li><li><a href="rule.html">連盟規約<span class="more">詳しく見る</span></a></li><li><a href="recruit.html">職員採用案内<span class="more">詳しく見る</span></a></li><li><a href="book.html">ブック（刊行物）<span class="more">詳しく見る</span></a></li><li><a href="officialgoods.html">公式グッズ<span class="more">詳しく見る</span></a></li><li><a href="org.html">加盟団体<span class="more">詳しく見る</span></a></li></ul><a class="banner" href="../map/index.html"><img src="../img/common/bn_dojomap.jpg" alt="全国弓道場マップ" loading="lazy"></a></section>
<p class="source"><a href="https://www.kyudo.jp/aboutus/backnumber.html">公式サイトの掲載内容を確認する</a></p></main>'''

# ---- Replace main in template ----
out = re.sub(r'<main class="wrap">.*?</main>', main_content, template, flags=re.DOTALL)

# Fix title
out = out.replace(
    '月刊「弓道」 最新号｜',
    '月刊「弓道」 バックナンバー｜'
)

with open(r'site-complete\aboutus\backnumber.html', 'w', encoding='utf-8') as f:
    f.write(out)

print("Done! Entries processed:", len(entries_raw))
