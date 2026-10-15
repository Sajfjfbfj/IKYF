import os
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

chuo_detail_base = r"site-complete\chuoshinsa\detail"

slugs = [
    "20260504_detail",
    "20260506_detail",
    "20260523_detail",
    "20260530_detail",
    "20260620_detail",
    "20260621_detail",
    "20260627_detail",
    "20260703_detail",
    "20260705_detail",
    "20260812_detail",
    "20260822_detail",
    "20260905_detail",
    "20260906_detail",
    "20260926_detail",
    "20261003_detail",
    "20261017_detail",
    "20261029_detail",
    "20261031_detail",
    "20261114_detail",
    "20261121_detail",
    "20261127_detail",
    "20261128_detail",
    "20261219_detail",
    "20270129_detail",
    "20270220_detail",
    "20270221_detail",
    "20270322_detail",
    "20270326_detail"
]

missing = []
for s in slugs:
    p = os.path.join(chuo_detail_base, s, "index.html")
    if not os.path.exists(p):
        missing.append(s)

print(f"Total checked: {len(slugs)}")
print(f"Missing in local chuoshinsa/detail: {len(missing)}")
if missing:
    for m in missing:
        print("  Missing:", m)
else:
    print("All 28 slugs exist locally in site-complete/chuoshinsa/detail/!")
