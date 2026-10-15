"""
Replace remaining external kyudo.jp links with local relative links.
"""

replacements = [
    (r'site-complete\documents\favicon.html', [
        ('http://www.kyudo.jp/', '../index.html'),
    ]),
    (r'site-complete\notice\page\12\index.html', [
        ('https://www.kyudo.jp/detail/20250221_detail/', '../../../chuoshinsa/detail/20250221_detail/index.html'),
    ]),
    (r'site-complete\notice\page\28\index.html', [
        ('https://www.kyudo.jp/news/news_202208.html', '../../../news/news_202208.html'),
    ]),
    (r'site-complete\notice\page\29\index.html', [
        ('https://www.kyudo.jp/detail/20220827_02_detail/', '../../../chuoshinsa/detail/20220827_02_detail/index.html'),
    ]),
    (r'site-complete\notice\page\43\index.html', [
        ('https://www.kyudo.jp/detail/20200628_detail/', '../../../chuoshinsa/detail/20200628_detail/index.html'),
    ]),
    (r'site-complete\notice\page\45\index.html', [
        ('https://www.kyudo.jp/detail/20190728_detail/', '../../../chuoshinsa/detail/20190728_detail/index.html'),
        ('https://www.kyudo.jp/detail/20190907_detail/', '../../../chuoshinsa/detail/20190907_detail/index.html'),
    ]),
    (r'site-complete\notice\page\5\index.html', [
        ('https://www.kyudo.jp/news/news_20260302.html', '../../../news/news_20260302.html'),
        ('https://www.kyudo.jp/news/news_20260220.html', '../../../news/news_20260220.html'),
        ('https://www.kyudo.jp/p/chuoshinsa/detail/20260822_detail/', '../../../chuoshinsa/detail/20260822_detail/index.html'),
    ]),
    (r'site-complete\notice\page\8\index.html', [
        ('https://www.kyudo.jp/i/detail/20250919_detail/', '../../../taikai/detail/20250919_detail/index.html'),
    ]),
]

for file_path, pairs in replacements:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old_url, new_url in pairs:
        if old_url in content:
            content = content.replace(old_url, new_url)
            modified = True
            print(f"Replaced {old_url} -> {new_url} in {file_path}")
        else:
            print(f"Warning: {old_url} not found in {file_path}")
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Replacement complete.")
