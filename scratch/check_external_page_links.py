import os
import re

site_root = r"site-complete"
external_pages = []

for root, dirs, files in os.walk(site_root):
    rel_root = os.path.relpath(root, site_root)
    top = rel_root.split(os.sep)[0]
    if top in ['pdf', 'img']:
        continue
    for f in files:
        if f.endswith('.html'):
            full = os.path.join(root, f)
            with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
            # source クラス以外のリンクを検出
            # <p class="source"><a href="https://www.kyudo.jp/..."> は公式サイト確認用リンクなので除外して集計
            # それ以外の普通のリンク
            matches = re.findall(r'href=["\'](https?://(?:www\.)?kyudo\.jp/[^"\']*)["\']', txt)
            non_source = []
            for m in matches:
                # sourceリンクかチェック
                idx = txt.find(m)
                surrounding = txt[max(0, idx-50):min(len(txt), idx+len(m)+50)]
                if 'class="source"' not in surrounding and "公式サイトの掲載内容を確認する" not in surrounding:
                    non_source.append(m)
            if non_source:
                external_pages.append((os.path.relpath(full, site_root), len(non_source), non_source[:3]))

print(f"Files with internal links pointing to external kyudo.jp: {len(external_pages)}")
for f, cnt, samples in external_pages[:20]:
    print(f"  {f} ({cnt} links): {samples}")
