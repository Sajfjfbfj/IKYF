import os
import shutil
import re

# 1. Create root map/ folder
os.makedirs('map', exist_ok=True)

with open(r'site-complete\map\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# For root map/index.html:
# It is at /map/index.html (depth 1 from root)
# The logo link should go to ../index.html
# Links to notice should go to ../site-complete/notice/
# Links to info should go to ../site-complete/info/
# Links to all-pages should go to ../site-complete/all-pages.html

root_map = content
root_map = root_map.replace('href="../../index.html"', 'href="../index.html"')
root_map = root_map.replace('href="../notice/"', 'href="../site-complete/notice/"')
root_map = root_map.replace('href="../info/contact.html"', 'href="../site-complete/info/contact.html"')
root_map = root_map.replace('href="../info/english.html"', 'href="../site-complete/info/english.html"')
root_map = root_map.replace('href="../all-pages.html"', 'href="../site-complete/all-pages.html"')

with open(r'map\index.html', 'w', encoding='utf-8') as f:
    f.write(root_map)

print("Created root map/index.html")

# Also ensure site-complete/map/index.html has proper links:
# From site-complete/map/index.html, depth to root index.html is ../../index.html
# Links to notice: ../notice/
# Links to info: ../info/...
# Logo link: ../../index.html
sc_map = content
# If logo had ../../index.html, keep it
# breadcrumb HOME:
sc_map = re.sub(r'<div class="crumb"><a href="[^"]*">HOME</a>', '<div class="crumb"><a href="../../index.html">HOME</a>', sc_map)
with open(r'site-complete\map\index.html', 'w', encoding='utf-8') as f:
    f.write(sc_map)

print("Verified site-complete/map/index.html")
