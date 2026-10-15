import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"
site_root = r"c:\Users\user\Desktop\ホームページ素材\site-complete"

# 主要カテゴリの固定ページ（detail以外）をピックアップ
fixed_pages = [
    # aboutus
    "aboutus/index.html",
    "aboutus/overview.html",
    "aboutus/plan.html",
    "aboutus/org.html",
    "aboutus/recruit.html",
    "aboutus/book.html",
    "aboutus/latestissue.html",
    "aboutus/officialgoods.html",
    "aboutus/rule.html",
    # begin
    "begin/index.html",
    "begin/tool.html",
    "begin/faq.html",
    # howto
    "howto/index.html",
    "howto/history.html",
    "howto/syaho.html",
    "howto/terminology.html",
    # improve
    "improve/index.html",
    # info
    "info/contact.html",
    "info/english.html",
    "info/guidelines.html",
    "info/link.html",
    "info/personalinfo.html",
    "info/usearrow.html",
    # documents
    "documents/index.html",
    # map
    "map/index.html",
    # movie
    "movie/index.html",
    # schedule
    "schedule/index.html",
    "schedule/taikai/index.html",
    "schedule/chuoshinsa/index.html",
    "schedule/chuoshinsa/overview.html",
    "schedule/association/index.html",
    "schedule/region/index.html",
    # notice
    "notice/index.html",
]

print(f"{'Page':<35} | {'Mirror':<8} | {'Site':<8} | Status")
print("-" * 65)

for p in fixed_pages:
    mp = os.path.join(mirror_root, os.path.normpath(p))
    sp = os.path.join(site_root, os.path.normpath(p))
    
    m_exists = os.path.exists(mp)
    s_exists = os.path.exists(sp)
    
    status = "OK"
    if not m_exists and not s_exists:
        status = "Both Missing"
    elif not m_exists:
        status = "Mirror Missing"
    elif not s_exists:
        status = "Site Missing"
    else:
        # Check size or difference
        msize = os.path.getsize(mp)
        ssize = os.path.getsize(sp)
        status = f"M:{msize} S:{ssize}"
        
    print(f"{p:<35} | {str(m_exists):<8} | {str(s_exists):<8} | {status}")
