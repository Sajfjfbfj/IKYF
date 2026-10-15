"""
Build category index pages:
- site-complete/category/chuoshinsa/index.html
- site-complete/category/taikai/index.html
"""
import os, re

# Read a template (2025chuoshinsa) to get the design
with open(r'site-complete\category\chuoshinsa\2025chuoshinsa\index.html', encoding='utf-8') as f:
    template = f.read()

def fix_depth(html, from_levels, to_levels):
    """
    Adjust relative path depth.
    from_levels: how many '../' in the original template root path
    to_levels: how many '../' needed in the target file's root path
    """
    from_root = '../' * from_levels
    to_root = '../' * to_levels
    # Replace occurrences carefully
    # Replace longer sequences first to avoid partial matches
    # We handle the JS variable separately
    html = html.replace(f'var K="{("../" * from_levels).rstrip("/")}";',
                        f'var K="{("../" * to_levels).rstrip("/")}";')
    # Replace all href/src occurrences
    html = re.sub(
        r'(href|src)="(\.\./){' + str(from_levels) + r'}',
        lambda m: m.group(1) + '="' + from_root.replace('../' * from_levels, to_root),
        html
    )
    return html

# ---- CHUOSHINSA INDEX ----
chuoshinsa_years = [
    ('2026chuoshinsa', '令和8年度'),
    ('2025chuoshinsa', '令和7年度'),
    ('2024chuoshinsa', '令和6年度'),
    ('2023chuoshinsa', '令和5年度'),
    ('2022chuoshinsa', '令和4年度'),
    ('2021chuoshinsa', '令和3年度'),
    ('2020chuoshinsa', '令和2年度'),
]

chuo_items = '\n'.join(
    f'<li><a href="{folder}/index.html">{reiwa}中央審査会<span class="more">詳しく見る</span></a></li>'
    for folder, reiwa in chuoshinsa_years
)

chuo_main = f'''<main class="wrap"><div class="crumb"><a href="../../index.html">HOME</a><span>›</span><a href="../../schedule/chuoshinsa/index.html">中央審査会</a><span>›</span>年度別一覧</div><p class="eyebrow">審査</p><h1>中央審査会 年度別一覧</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div>
<section class="materials">
<h2>年度別 中央審査会</h2>
<p class="lead">各年度の中央審査会の日程・要項・結果をご覧いただけます。</p>
<ul>
{chuo_items}
</ul>
</section>
<section class="materials"><h2>大会・審査関連コンテンツ</h2><ul><li><a href="../../schedule/taikai/">全国大会<span class="more">詳しく見る</span></a></li><li><a href="../../schedule/chuoshinsa/">中央審査会<span class="more">詳しく見る</span></a></li><li><a href="../../schedule/region/">地方審査会<span class="more">詳しく見る</span></a></li><li><a href="../../schedule/association/">連合審査会<span class="more">詳しく見る</span></a></li></ul></section>
<p class="source"><a href="https://www.kyudo.jp/category/chuoshinsa/">公式サイトの掲載内容を確認する</a></p></main>'''

# Build from template: replace main content
chuo_out = re.sub(r'<main class="wrap">.*?</main>', chuo_main, template, flags=re.DOTALL)

# Fix paths: template is at depth 3 (category/chuoshinsa/2025chuoshinsa/)
# Target is at depth 2 (category/chuoshinsa/)
# Replace ../../.. with ../..
chuo_out = chuo_out.replace('../../..', '../..')
# Replace var K="../../.." with var K="../.."  (already done by above line)
# Fix title
chuo_out = re.sub(r'<title>[^<]*</title>',
                  '<title>中央審査会 年度別一覧｜全日本弓道連盟について｜公益財団法人 全日本弓道連盟</title>',
                  chuo_out)

os.makedirs(r'site-complete\category\chuoshinsa', exist_ok=True)
with open(r'site-complete\category\chuoshinsa\index.html', 'w', encoding='utf-8') as f:
    f.write(chuo_out)
print('chuoshinsa index.html created')

# Verify
with open(r'site-complete\category\chuoshinsa\index.html', encoding='utf-8') as f:
    verify = f.read()
deep_count = verify.count('../../..')
print(f'  ../../.. remaining: {deep_count}')

# ---- TAIKAI INDEX ----
taikai_years = [
    ('r8taikai', '令和8年度'),
    ('r7taikai', '令和7年度'),
    ('r6taikai', '令和6年度'),
    ('r5taikai', '令和5年度'),
    ('r4taikai', '令和4年度'),
    ('r3taikai', '令和3年度'),
    ('r2taikai', '令和2年度'),
]

taikai_items = '\n'.join(
    f'<li><a href="{folder}/index.html">{reiwa}大会・行事<span class="more">詳しく見る</span></a></li>'
    for folder, reiwa in taikai_years
)

taikai_main = f'''<main class="wrap"><div class="crumb"><a href="../../index.html">HOME</a><span>›</span><a href="../../schedule/taikai/index.html">大会・行事</a><span>›</span>年度別一覧</div><p class="eyebrow">大会・行事</p><h1>大会・行事 年度別一覧</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div>
<section class="materials">
<h2>年度別 大会・行事</h2>
<p class="lead">各年度の大会・行事の日程・要項・結果をご覧いただけます。</p>
<ul>
{taikai_items}
</ul>
</section>
<section class="materials"><h2>大会・審査関連コンテンツ</h2><ul><li><a href="../../schedule/taikai/">全国大会<span class="more">詳しく見る</span></a></li><li><a href="../../schedule/chuoshinsa/">中央審査会<span class="more">詳しく見る</span></a></li><li><a href="../../schedule/region/">地方審査会<span class="more">詳しく見る</span></a></li><li><a href="../../schedule/association/">連合審査会<span class="more">詳しく見る</span></a></li></ul></section>
<p class="source"><a href="https://www.kyudo.jp/category/taikai/">公式サイトの掲載内容を確認する</a></p></main>'''

taikai_out = re.sub(r'<main class="wrap">.*?</main>', taikai_main, template, flags=re.DOTALL)
taikai_out = taikai_out.replace('../../..', '../..')
taikai_out = re.sub(r'<title>[^<]*</title>',
                    '<title>大会・行事 年度別一覧｜全日本弓道連盟について｜公益財団法人 全日本弓道連盟</title>',
                    taikai_out)

os.makedirs(r'site-complete\category\taikai', exist_ok=True)
with open(r'site-complete\category\taikai\index.html', 'w', encoding='utf-8') as f:
    f.write(taikai_out)
print('taikai index.html created')

# Verify
with open(r'site-complete\category\taikai\index.html', encoding='utf-8') as f:
    verify2 = f.read()
deep_count2 = verify2.count('../../..')
print(f'  ../../.. remaining: {deep_count2}')
