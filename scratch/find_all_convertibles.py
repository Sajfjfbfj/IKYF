import os
import sys
import io
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

site_root = os.path.abspath("site-complete")

def build_local_file_index():
    # Maps normalized path (without leading slash, using forward slashes) to relative path from site_root
    index = {}
    for root, dirs, files in os.walk(site_root):
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, site_root).replace('\\', '/')
            index[rel.lower()] = rel
            if f == "index.html":
                dir_rel = os.path.dirname(rel).replace('\\', '/')
                if dir_rel:
                    index[dir_rel.lower() + "/"] = dir_rel + "/"
                    index[dir_rel.lower()] = dir_rel + "/"
                else:
                    index[""] = ""
                    index["/"] = ""
    return index

def find_convertible_links():
    local_index = build_local_file_index()
    print(f"Total entries in local index: {len(local_index)}")
    
    html_files = []
    for root, dirs, files in os.walk(site_root):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
                
    results = {}
    for hf in html_files:
        rel_src = os.path.relpath(hf, site_root).replace('\\', '/')
        src_dir = os.path.dirname(hf)
        
        with open(hf, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        file_matches = []
        for a in soup.find_all('a'):
            href = a.get('href', '')
            txt = a.get_text(strip=True)
            if not href:
                continue
            # Skip explicit official reference link if desired, or examine it
            is_official_note = "公式サイトの掲載内容を確認する" in txt
            
            target_norm = None
            if href.startswith('http://127.0.0.1:5500/site-complete/'):
                target_norm = href.replace('http://127.0.0.1:5500/site-complete/', '')
            elif href.startswith('http://localhost:5500/site-complete/'):
                target_norm = href.replace('http://localhost:5500/site-complete/', '')
            elif 'kyudo.jp' in href:
                # parsed
                parsed = urlparse(href)
                p = parsed.path.lstrip('/')
                # check if p matches something local
                target_norm = p
                
            if target_norm is not None:
                # Strip query and anchor
                clean = target_norm.split('?')[0].split('#')[0].lower()
                # Check variants
                matched_target = None
                for candidate in [clean, clean.rstrip('/') + '/', clean.rstrip('/') + '/index.html', clean + '.html']:
                    if candidate in local_index:
                        matched_target = local_index[candidate]
                        break
                        
                if matched_target:
                    # Calculate relative path from src_dir to matched_target
                    dest_full = os.path.join(site_root, matched_target)
                    rel_calc = os.path.relpath(dest_full, src_dir).replace('\\', '/')
                    # If target was a directory with index.html, format cleanly
                    if matched_target.endswith('/'):
                        if not rel_calc.endswith('/'):
                            rel_calc += '/'
                    file_matches.append({
                        'orig_href': href,
                        'matched_target': matched_target,
                        'suggested_rel': rel_calc,
                        'text': txt,
                        'is_official_note': is_official_note
                    })
                    
        if file_matches:
            results[rel_src] = file_matches

    print(f"\nFiles with convertible links: {len(results)}")
    
    # Let's inspect non-official-note convertible links
    content_links_count = 0
    official_links_count = 0
    for rel_src, matches in sorted(results.items()):
        non_officials = [m for m in matches if not m['is_official_note']]
        officials = [m for m in matches if m['is_official_note']]
        content_links_count += len(non_officials)
        official_links_count += len(officials)
        if non_officials:
            print(f"\n{rel_src} (Content links: {len(non_officials)}):")
            for m in non_officials[:5]:
                print(f"  {m['orig_href']} -> {m['suggested_rel']} ({m['text'][:30]})")
                
    print(f"\nTotal content links to convert: {content_links_count}")
    print(f"Total 'official note' links pointing to same page: {official_links_count}")

if __name__ == "__main__":
    find_convertible_links()
