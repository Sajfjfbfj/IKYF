import subprocess
import re
import os

cwd = r"c:\Users\user\Desktop\ホームページ素材"

# 1. Get all files tracked by git that contain "水鏡"
output = subprocess.check_output(['git', 'grep', '-l', '水鏡'], cwd=cwd).decode('utf-8', errors='ignore')
files = [line.strip() for line in output.splitlines() if line.strip()]

# Also check index.html if it's untracked
if 'index.html' not in files and os.path.exists(os.path.join(cwd, 'index.html')):
    files.append('index.html')

print(f"Target files found: {len(files)}")

# Regex to match any ../../... followed by non-quotes ending in 水鏡.html
# e.g., href="../../...水鏡.html" -> href="../../...index.html"
link_pattern = re.compile(r'((?:\.\./)+)[^"\'<>\s]*水鏡\.html')
plain_pattern = re.compile(r'[^"\'<>\s/]*水鏡\.html')

updated_count = 0
for rel_path in files:
    full_path = os.path.join(cwd, rel_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace relative links: (../../)something水鏡.html -> \1index.html
    new_content = link_pattern.sub(r'\1index.html', content)
    # Replace root links: something水鏡.html -> index.html
    new_content = plain_pattern.sub(r'index.html', new_content)
    # Replace any plain text mentions
    new_content = new_content.replace('的場の水鏡', 'index')

    if new_content != content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1

print(f"Successfully updated {updated_count} files!")
