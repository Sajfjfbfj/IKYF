import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

docs_dir = r"site-complete\documents"
if os.path.exists(docs_dir):
    print("Files in site-complete/documents:")
    for r, ds, fs in os.walk(docs_dir):
        print(r, fs)
else:
    print("site-complete/documents does not exist")
