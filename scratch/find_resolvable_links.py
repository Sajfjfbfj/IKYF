import os
import sys
import io
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = os.path.abspath("site-complete")

def get_all_local_paths():
    local_files = set()
    for root, dirs, files in os.walk(site_root):
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, site_root).replace('\\', '/')
            local_files.add(rel)
            # if index.html, also add dir path with trailing slash
            if f == "index.html":
                dir_rel = os.path.dirname(rel).replace('\\', '/')
                if dir_rel:
                    local_files.add(dir_rel + "/")
                else:
                    local_files.add("")
    return local_files

def analyze_all_links():
    local_paths = get_all_local_paths()
    print(f"Total indexed local files/endpoints: {len(local_paths)}")
    
    # Check all HTML files
    html_files = []
    for root, dirs, files in os.walk(site_root):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
                
    print(f"Total HTML files to inspect: {len(html_files)}")
    
    # Check what kyudo.jp URLs appear
    resolvable_links = {}
    external_links = {}
    
    for hf in html_files:
        rel_from_root = os.path.relpath(hf, site_root).replace('\\', '/')
        with open(hf, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        for a in soup.find_all('a'):
            href = a.get('href', '')
            if not href:
                continue
            # Check if it starts with http://127.0.0.1:5500/site-complete/
            # or https://www.kyudo.jp/
            target_path = None
            if href.startswith('http://127.0.0.1:5500/site-complete/'):
                target_path = href.replace('http://127.0.0.1:5500/site-complete/', '')
            elif href.startswith('http://localhost:5500/site-complete/'):
                target_path = href.replace('http://localhost:5500/site-complete/', '')
            elif 'kyudo.jp' in href:
                parsed = urlparse(href)
                p = parsed.path.lstrip('/')
                target_path = p
                
            if target_path is not None:
                # Check if target_path exists in local_paths
                # Try target_path, target_path + "index.html", target_path.rstrip('/') + "/index.html"
                found = None
                clean_p = target_path.split('?')[0].split('#')[0]
                candidates = [
                    clean_p,
                    clean_p.rstrip('/') + "/",
                    clean_p.rstrip('/') + "/index.html" if not clean_p.endswith('.html') else clean_p,
                    clean_p + ".html"
                ]
                for c in candidates:
                    if c in local_paths:
                        found = c
                        break
                        
                if found:
                    if rel_from_root not in resolvable_links:
                        resolvable_links[rel_from_root] = []
                    resolvable_links[rel_from_root].append((href, found, a.get_text(strip=True)[:30]))
                else:
                    if rel_from_root not in external_links:
                        external_links[rel_from_root] = []
                    external_links[rel_from_root].append((href, a.get_text(strip=True)[:30]))

    print(f"\nFiles containing resolvable URLs pointing to existing local files: {len(resolvable_links)}")
    sample_files = list(resolvable_links.keys())[:5]
    for sf in sample_files:
        print(f"\n  File: {sf}")
        for orig, local_match, txt in resolvable_links[sf][:6]:
            print(f"    {orig} -> {local_match} ({txt})")
            
    print(f"\nSample external unresolvable URLs (e.g. PDFs):")
    for sf in list(external_links.keys())[:2]:
        print(f"  File: {sf}")
        for orig, txt in external_links[sf][:4]:
            print(f"    {orig} ({txt})")

if __name__ == "__main__":
    analyze_all_links()
