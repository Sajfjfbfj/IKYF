import os
import re

site_root = r"site-complete"

def get_rel_prefix(file_rel_path):
    parts = os.path.normpath(file_rel_path).split(os.sep)
    depth = len(parts) - 1
    if depth == 0:
        return "."
    return "/".join([".."] * depth)

def run():
    modified = 0
    for root, dirs, files in os.walk(site_root):
        rel_root = os.path.relpath(root, site_root)
        top = rel_root.split(os.sep)[0]
        if top in ['pdf', 'img']:
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, site_root)
            prefix = get_rel_prefix(rel_path)

            with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()

            orig = content

            # movie/index.html 特有の誤ったリンク
            if 'movie' in rel_path:
                content = content.replace('https://www.kyudo.jp/movie/overview.html', '../aboutus/overview.html')
                content = content.replace('https://www.kyudo.jp/movie/plan.html', '../aboutus/plan.html')
                content = content.replace('https://www.kyudo.jp/movie/rule.html', '../aboutus/rule.html')
                content = content.replace('https://www.kyudo.jp/movie/recruit.html', '../aboutus/recruit.html')
                content = content.replace('https://www.kyudo.jp/movie/book.html', '../aboutus/book.html')
                content = content.replace('https://www.kyudo.jp/movie/officialgoods.html', '../aboutus/officialgoods.html')
                content = content.replace('https://www.kyudo.jp/movie/org.html', '../aboutus/org.html')

            # 一般的な kyudo.jp 内部リンクの置換（source 以外）
            patterns = [
                (r'https?://(?:www\.)?kyudo\.jp/taikai/detail/([^\s"\'<>]+)', f'{prefix}/taikai/detail/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/chuoshinsa/detail/([^\s"\'<>]+)', f'{prefix}/chuoshinsa/detail/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/notice/([^"\'<>\s]*)', f'{prefix}/notice/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/info/([^\s"\'<>]+)', f'{prefix}/info/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/aboutus/([^\s"\'<>]+)', f'{prefix}/aboutus/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/schedule/([^\s"\'<>]+)', f'{prefix}/schedule/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/howto/([^\s"\'<>]+)', f'{prefix}/howto/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/begin/([^\s"\'<>]+)', f'{prefix}/begin/\\1'),
                (r'https?://(?:www\.)?kyudo\.jp/map/([^\s"\'<>]+)', f'{prefix}/map/\\1'),
            ]

            # source 行は置換しないようにする
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                if 'class="source"' in line or '公式サイトの掲載内容を確認する' in line:
                    new_lines.append(line)
                    continue
                l = line
                for pat, rep in patterns:
                    l = re.sub(pat, rep, l)
                new_lines.append(l)

            content = '\n'.join(new_lines)

            if content != orig:
                with open(full_path, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                modified += 1

    print(f"Remaining links localized in {modified} files.")

if __name__ == '__main__':
    run()
