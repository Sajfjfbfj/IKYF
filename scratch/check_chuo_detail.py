import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

chuo_detail = r"site-complete\chuoshinsa\detail"
if os.path.exists(chuo_detail):
    dirs = os.listdir(chuo_detail)
    print(f"Total dirs in chuoshinsa/detail: {len(dirs)}")
    print("Sample dirs:", dirs[:10])
else:
    print("chuoshinsa/detail not found")
