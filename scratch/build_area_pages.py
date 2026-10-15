"""
Build proper content for association-area and region-area index pages.
These are WordPress taxonomy pages not in the mirror, but we can create
useful pages that list links to related association/region schedule pages.
"""
import os, re

# Mapping of area name to Japanese label and related schedule dirs
association_areas = {
    'hokkaido': ('北海道地区', 'hokkaido'),
    'touhoku': ('東北地区', 'tohoku'),
    'kantou': ('関東地区', 'kanto'),
    'hokushinetsu': ('北信越地区', 'hokushinetsu'),
    'kitashinetsu': ('北信越地区', 'hokushinetsu'),
    'chubu': ('中部地区', 'chubu'),
    'kinki': ('近畿地区', 'kinki'),
    'chugoku': ('中国地区', 'chugoku'),
    'shikoku': ('四国地区', 'shikoku'),
    'kyushu': ('九州地区', 'kyushu'),
}

region_areas = {
    'hokkaido': ('北海道地区', 'hokkaido'),
    'touhoku': ('東北地区', 'tohoku'),
    'kantou': ('関東地区', 'kanto'),
    'hokushinetsu': ('北信越地区', 'hokushinetsu'),
    'kitashinetsu': ('北信越地区', 'hokushinetsu'),
    'chubu': ('中部地区', 'chubu'),
    'kinki': ('近畿地区', 'kinki'),
    'chugoku': ('中国地区', 'chugoku'),
    'shikoku': ('四国地区', 'shikoku'),
    'kyushu': ('九州地区', 'kyushu'),
}

# Read a template from the same area
def get_template(folder_path):
    with open(folder_path, encoding='utf-8') as f:
        return f.read()

def build_area_page(area_name, japanese_name, area_type, schedule_slug, template):
    """Build a simple index page for an area."""
    if area_type == 'association':
        title = f'{japanese_name} 連合審査会'
        crumb_parent = '連合審査会'
        crumb_parent_href = '../../schedule/association/'
        schedule_link = f'../../schedule/association/'
        eyebrow = '審査'
        source_url = f'https://www.kyudo.jp/association-area/{area_name}/'
    else:
        title = f'{japanese_name} 地方審査会'
        crumb_parent = '地方審査会'
        crumb_parent_href = '../../schedule/region/'
        schedule_link = f'../../schedule/region/'
        eyebrow = '審査'
        source_url = f'https://www.kyudo.jp/region-area/{area_name}/'

    main_content = f'''<main class="wrap"><div class="crumb"><a href="../../index.html">HOME</a><span>›</span><a href="{crumb_parent_href}">{crumb_parent}</a><span>›</span>{japanese_name}</div><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><div class="meta"><span>公益財団法人 全日本弓道連盟</span></div>
<p class="summary">{japanese_name}の{('連合' if area_type == 'association' else '地方')}審査会の情報を掲載しています。</p>
<section class="materials">
<h2>関連ページ</h2>
<ul>
<li><a href="{schedule_link}">{crumb_parent}スケジュール一覧<span class="more">詳しく見る</span></a></li>
</ul>
</section>
<p class="source"><a href="{source_url}">公式サイトの掲載内容を確認する</a></p></main>'''

    out = re.sub(r'<main class="wrap">.*?</main>', main_content, template, flags=re.DOTALL)
    return out

# Process association-area
assoc_dirs = [d for d in os.listdir('site-complete/association-area')
              if os.path.isdir(f'site-complete/association-area/{d}')]
print(f'association-area dirs: {assoc_dirs}')

for area in assoc_dirs:
    idx_path = f'site-complete/association-area/{area}/index.html'
    if os.path.exists(idx_path):
        template = get_template(idx_path)
        japanese_name, schedule_slug = association_areas.get(area, (area, area))
        new_content = build_area_page(area, japanese_name, 'association', schedule_slug, template)
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  Updated: {area}')

# Process region-area
region_dirs = [d for d in os.listdir('site-complete/region-area')
               if os.path.isdir(f'site-complete/region-area/{d}')]
print(f'region-area dirs: {region_dirs}')

for area in region_dirs:
    idx_path = f'site-complete/region-area/{area}/index.html'
    if os.path.exists(idx_path):
        template = get_template(idx_path)
        japanese_name, schedule_slug = region_areas.get(area, (area, area))
        new_content = build_area_page(area, japanese_name, 'region', schedule_slug, template)
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  Updated: {area}')

print('Done!')
