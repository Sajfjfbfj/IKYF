"""
1. Rename/Replace all references to 的場の水鏡.html with index.html across all html/js/css files.
2. Ensure index.html is the sole root top page.
"""
import os
import re

workspace = r"c:\Users\user\Desktop\ホームページ素材"
modified_count = 0
total_replacements = 0

# Match variations of 的場の水鏡.html (including possible encoding corruption ending in 水鏡.html)
# e.g., '的場の水鏡.html', '皁Eの水鏡.html', 'I̐.html', etc.
pattern = re.compile(r'([a-zA-Z0-9_\-\./]*)(?:[\w\u3000-\u9fff\ufffd]*水鏡\.html|的場の水鏡\.html|I̐\.html)')

for root, dirs, files in os.walk(workspace):
    if '.git' in root or 'scratch' in root or '.user_uploaded' in root:
        continue
    for f in files:
        if f.endswith('.html') or f.endswith('.js') or f.endswith('.css'):
            full_path = os.path.join(root, f)
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            # Check if any target exists
            if '水鏡.html' in content or '的場の水鏡' in content or 'I̐.html' in content:
                # Replace in hrefs and src
                # e.g., href="../../的場の水鏡.html" -> href="../../index.html"
                # href="的場の水鏡.html" -> href="index.html"
                def replace_func(m):
                    prefix = m.group(1)
                    return prefix + 'index.html'
                
                new_content = pattern.sub(replace_func, content)
                # Also replace plain comments "的場の水鏡.html" -> "index.html"
                new_content = new_content.replace('的場の水鏡.html', 'index.html')
                new_content = new_content.replace('的場の水鏡', 'index')
                
                if new_content != content:
                    with open(full_path, 'w', encoding='utf-8') as fp:
                        fp.write(new_content)
                    modified_count += 1
                    total_replacements += content.count('水鏡.html') + content.count('的場の水鏡')
                    print(f"Updated: {os.path.relpath(full_path, workspace)}")

print(f"\nDone! Modified {modified_count} files.")
