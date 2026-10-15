import os
import re

workspace = r"c:\Users\user\Desktop\ホームページ素材"
found_files = []

for root, dirs, files in os.walk(workspace):
    if '.git' in root or 'scratch' in root or '.user_uploaded' in root:
        continue
    for f in files:
        if f.endswith('.html') or f.endswith('.js') or f.endswith('.css'):
            full_path = os.path.join(root, f)
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            # Check for '的場の水鏡.html' or anything ending with '水鏡.html'
            matches = re.findall(r'[^"\'<>\s]*水鏡\.html', content)
            if matches:
                found_files.append((os.path.relpath(full_path, workspace), list(set(matches))))

print(f"Total files referencing 水鏡.html: {len(found_files)}")
for path, matches in found_files:
    print(f"  {path}: {matches}")
