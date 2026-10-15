import os
import re

site_root = r"site-complete"

# schedule/taikai files
taikai_sched_files = [
    "schedule/taikai/index.html",
    "schedule/taikai/r2taikai.html",
    "schedule/taikai/r3taikai.html",
    "schedule/taikai/r4taikai.html",
    "schedule/taikai/r5taikai.html",
    "schedule/taikai/r6taikai.html",
    "schedule/taikai/r7taikai.html",
]

total_checked = 0
broken_links = []

for rel in taikai_sched_files:
    full = os.path.join(site_root, os.path.normpath(rel))
    if not os.path.exists(full):
        continue
    with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    links = re.findall(r'href=["\']([^"\']+)["\']', txt)
    for l in links:
        if l.startswith(('http:', 'https:', '#', 'mailto:', 'tel:')):
            continue
        total_checked += 1
        file_dir = os.path.dirname(full)
        target = os.path.normpath(os.path.join(file_dir, l.split('?')[0].split('#')[0]))
        if not os.path.exists(target):
            if os.path.isdir(target) and os.path.exists(os.path.join(target, 'index.html')):
                continue
            broken_links.append((rel, l))

print(f"Schedule taikai files checked: {len(taikai_sched_files)}")
print(f"Total internal links: {total_checked}, Broken: {len(broken_links)}")
if broken_links:
    for b in broken_links[:10]:
        print("  Broken:", b)
