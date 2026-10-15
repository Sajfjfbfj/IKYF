import os
import re

site_root = r"site-complete"

fixed_pages = [
    "aboutus/index.html",
    "aboutus/overview.html",
    "aboutus/plan.html",
    "aboutus/org.html",
    "aboutus/recruit.html",
    "aboutus/book.html",
    "aboutus/latestissue.html",
    "aboutus/officialgoods.html",
    "aboutus/rule.html",
    "begin/index.html",
    "begin/tool.html",
    "begin/faq.html",
    "howto/index.html",
    "howto/history.html",
    "howto/syaho.html",
    "howto/terminology.html",
    "improve/index.html",
    "info/contact.html",
    "info/english.html",
    "info/guidelines.html",
    "info/link.html",
    "info/personalinfo.html",
    "info/usearrow.html",
    "documents/index.html",
    "map/index.html",
    "movie/index.html",
    "schedule/index.html",
    "schedule/taikai/index.html",
    "schedule/chuoshinsa/index.html",
    "schedule/chuoshinsa/overview.html",
    "schedule/association/index.html",
    "schedule/region/index.html",
    "notice/index.html",
]

total_checked = 0
broken_links = []

for rel in fixed_pages:
    full = os.path.join(site_root, os.path.normpath(rel))
    if not os.path.exists(full):
        continue
    with open(full, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    links = re.findall(r'href=["\']([^"\']+)["\']', txt)
    for l in links:
        if l.startswith(('http:', 'https:', '#', 'mailto:', 'tel:', 'javascript:')):
            continue
        total_checked += 1
        file_dir = os.path.dirname(full)
        target = os.path.normpath(os.path.join(file_dir, l.split('?')[0].split('#')[0]))
        if not os.path.exists(target):
            if os.path.isdir(target) and os.path.exists(os.path.join(target, 'index.html')):
                continue
            broken_links.append((rel, l))

print(f"Fixed pages checked: {len(fixed_pages)}")
print(f"Total internal links: {total_checked}, Broken: {len(broken_links)}")
if broken_links:
    for b in broken_links[:10]:
        print("  Broken:", b)
