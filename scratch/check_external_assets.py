import os
import re

site_root = r"site-complete"
external_count = 0
files_with_external = []

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
            m = re.findall(r'https?://(?:www\.)?kyudo\.jp/(pdf|img)/[^\s"\'<>]+', txt)
            if m:
                external_count += len(m)
                files_with_external.append((os.path.relpath(full, site_root), len(m)))

print(f"Total external pdf/img links found: {external_count}")
print(f"Files affected: {len(files_with_external)}")
print("Sample 20 files:")
for f, cnt in files_with_external[:20]:
    print(f"  {f}: {cnt} links")
