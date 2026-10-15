import os
import re

site_root = r"site-complete"

def get_rel_prefix(file_rel_path):
    parts = os.path.normpath(file_rel_path).split(os.sep)
    depth = len(parts) - 1
    if depth == 0:
        return "."
    return "/".join([".."] * depth)

def run_localization():
    total_files_modified = 0
    total_replacements = 0

    for root, dirs, files in os.walk(site_root):
        rel_root = os.path.relpath(root, site_root)
        top = rel_root.split(os.sep)[0]
        # pdfやimg内のhtmlはスキップ
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

            orig_content = content
            file_replaces = 0

            # 1. https?://(www.)?kyudo.jp/pdf/xxx -> prefix/pdf/xxx
            def replace_url_pdf(m):
                nonlocal file_replaces
                file_replaces += 1
                return f"{prefix}/pdf/{m.group(1)}"

            content = re.sub(r'https?://(?:www\.)?kyudo\.jp/pdf/([^\s"\'<>]+)', replace_url_pdf, content)

            # 2. https?://(www.)?kyudo.jp/img/xxx -> prefix/img/xxx
            def replace_url_img(m):
                nonlocal file_replaces
                file_replaces += 1
                return f"{prefix}/img/{m.group(1)}"

            content = re.sub(r'https?://(?:www\.)?kyudo\.jp/img/([^\s"\'<>]+)', replace_url_img, content)

            # 3. href="/pdf/xxx" または src="/img/xxx"
            def replace_root_pdf(m):
                nonlocal file_replaces
                file_replaces += 1
                quote = m.group(1)
                subpath = m.group(2)
                return f'href={quote}{prefix}/pdf/{subpath}{quote}'

            content = re.sub(r'href=(["\'])/pdf/([^\s"\'<>]+)\1', replace_root_pdf, content)

            def replace_root_img(m):
                nonlocal file_replaces
                file_replaces += 1
                quote = m.group(1)
                subpath = m.group(2)
                return f'src={quote}{prefix}/img/{subpath}{quote}'

            content = re.sub(r'src=(["\'])/img/([^\s"\'<>]+)\1', replace_root_img, content)

            if content != orig_content:
                with open(full_path, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                total_files_modified += 1
                total_replacements += file_replaces

    print(f"Localization complete!")
    print(f"Files modified: {total_files_modified}")
    print(f"Total replacements: {total_replacements}")

if __name__ == '__main__':
    run_localization()
