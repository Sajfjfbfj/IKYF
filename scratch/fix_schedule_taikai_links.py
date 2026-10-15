import os
import re
from bs4 import BeautifulSoup

sched_dir = r"site-complete\schedule\taikai"
detail_base = r"site-complete\taikai\detail"

files = [
    "index.html",
    "r2taikai.html",
    "r3taikai.html",
    "r4taikai.html",
    "r5taikai.html",
    "r6taikai.html",
    "r7taikai.html"
]

def fix_sched_links():
    for f in files:
        p = os.path.join(sched_dir, f)
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as fl:
            content = fl.read()
            
        def repl(match):
            slug = match.group(1)
            # handle slug typo
            if slug == "20230717_detail":
                slug = "20230717_detail-2"
            
            # verify local dir exists
            local_target = os.path.join(detail_base, slug)
            if os.path.exists(local_target):
                # Return relative path from schedule/taikai to taikai/detail/<slug>/
                return f'href="../../taikai/detail/{slug}/"'
            else:
                print(f"Warning: local {local_target} not found!")
                return match.group(0)

        # Regex for href="https://www.kyudo.jp/taikai/detail/<slug>/"
        new_content, count = re.subn(r'href="https://www\.kyudo\.jp/taikai/detail/([^/"]+)/?"', repl, content)
        
        # Also, remove target="_blank" and rel="noopener" from these local links if present
        # e.g.: <a href="../../taikai/detail/.../" target="_blank" rel="noopener"> -> <a href="../../taikai/detail/.../">
        # Let's clean up using BeautifulSoup or regex
        soup = BeautifulSoup(new_content, 'html.parser')
        modified = 0
        for a in soup.find_all('a'):
            h = a.get('href', '')
            if h.startswith('../../taikai/detail/'):
                if a.get('target') == '_blank':
                    del a['target']
                    modified += 1
                if a.get('rel') == ['noopener'] or a.get('rel') == 'noopener':
                    del a['rel']
                    modified += 1
                    
        with open(p, 'w', encoding='utf-8') as fl:
            fl.write(str(soup))
            
        print(f"Updated {f}: converted {count} taikai detail links to local relative paths")

if __name__ == "__main__":
    fix_sched_links()
