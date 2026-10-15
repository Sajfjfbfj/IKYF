import os
import re

site_root = r"site-complete"

def get_rel_prefix(file_rel_path):
    # 例: "aboutus/overview.html" -> depth 1 -> ".."
    # 例: "category/chuoshinsa/2025chuoshinsa/index.html" -> depth 3 -> "../../.."
    # 例: "index.html" -> depth 0 -> "."
    parts = os.path.normpath(file_rel_path).split(os.sep)
    depth = len(parts) - 1
    if depth == 0:
        return "."
    return "/".join([".."] * depth)

def test_conversion():
    sample_files = [
        "index.html",
        "aboutus/overview.html",
        "schedule/chuoshinsa/index.html",
        "category/chuoshinsa/2025chuoshinsa/index.html",
        "category/category/chuoshinsa/2024chuoshinsa/index.html"
    ]
    for s in sample_files:
        p = get_rel_prefix(s)
        print(f"{s} -> prefix: '{p}', sample link: '{p}/pdf/documents/probation_rules.pdf'")

if __name__ == '__main__':
    test_conversion()
