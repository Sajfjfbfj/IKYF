import os

targets = [
    ('improve/02.html', r'site-complete\improve\02.html'),
    ('detail/20250221_detail/', r'site-complete\detail\20250221_detail\index.html'),
    ('news/news_202208.html', r'site-complete\news\news_202208.html'),
    ('detail/20220827_02_detail/', r'site-complete\detail\20220827_02_detail\index.html'),
    ('detail/20200628_detail/', r'site-complete\detail\20200628_detail\index.html'),
    ('detail/20190728_detail/', r'site-complete\detail\20190728_detail\index.html'),
    ('detail/20190907_detail/', r'site-complete\detail\20190907_detail\index.html'),
    ('news/news_20260302.html', r'site-complete\news\news_20260302.html'),
    ('chuoshinsa/detail/20260822_detail/', r'site-complete\chuoshinsa\detail\20260822_detail\index.html'),
    ('news/news_20260220.html', r'site-complete\news\news_20260220.html'),
    ('i/detail/20250919_detail/', r'site-complete\detail\20250919_detail\index.html'),
]

for label, p in targets:
    exists_sc = os.path.exists(p)
    # またミラー側にもあるか確認
    mirror_p = os.path.join(r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp", label.replace('/', os.sep))
    exists_mirror = os.path.exists(mirror_p) or os.path.exists(mirror_p.rstrip('\\') + '.html') or os.path.exists(os.path.join(mirror_p, 'index.html'))
    print(f"{label} -> site-complete: {exists_sc}, mirror: {exists_mirror}")
