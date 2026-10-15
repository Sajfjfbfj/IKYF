import os
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
mirror_root = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp"
site_root = r"c:\Users\user\Desktop\ホームページ素材\site-complete"

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

needs_update = []

for p in fixed_pages:
    sp = os.path.join(site_root, os.path.normpath(p))
    mp = os.path.join(mirror_root, os.path.normpath(p))
    
    if not os.path.exists(sp) or not os.path.exists(mp):
        continue
        
    with open(sp, 'r', encoding='utf-8', errors='ignore') as f:
        s_text = f.read()
    with open(mp, 'r', encoding='utf-8', errors='ignore') as f:
        m_text = f.read()
        
    s_soup = BeautifulSoup(s_text, 'html.parser')
    m_soup = BeautifulSoup(m_text, 'html.parser')
    
    s_main = s_soup.find('main')
    m_main = m_soup.find('div', class_='contents') or m_soup.find('main') or m_soup.body
    
    s_chars = len(s_main.get_text(strip=True)) if s_main else 0
    m_chars = len(m_main.get_text(strip=True)) if m_main else 0
    
    is_placeholder = "このページに関連する資料リンクはありません" in s_text
    
    flag = ""
    if is_placeholder:
        flag = "★ PLACEHOLDER"
        needs_update.append(p)
    elif s_chars < m_chars * 0.4 and m_chars > 300:
        flag = "★ CONTENT SHORT"
        needs_update.append(p)
    else:
        flag = "OK"
        
    print(f"{p:<35} | S:{s_chars:<5} M:{m_chars:<5} | {flag}")

print("\n--- Pages needing content update ---")
for p in needs_update:
    print(" ", p)
