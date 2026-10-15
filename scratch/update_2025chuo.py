import os
import re
from bs4 import BeautifulSoup

def update_2025():
    mirror_path = r"c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\category\chuoshinsa\2025chuoshinsa\index.html"
    target_path = r"site-complete\category\chuoshinsa\2025chuoshinsa\index.html"

    with open(mirror_path, 'r', encoding='utf-8') as f:
        mirror_soup = BeautifulSoup(f.read(), 'html.parser')

    mirror_table = mirror_soup.find('table')
    mirror_rows = mirror_table.find_all('tr')

    tbody_rows = []

    for r in mirror_rows[1:]:
        tds = r.find_all('td')
        if len(tds) < 6:
            continue
        date_text = tds[0].get_text(strip=True)
        name_td = tds[1]
        name_text = name_td.get_text(strip=True)
        name_a = name_td.find('a')

        detail_href = name_a.get('href', '') if name_a else ''
        m = re.search(r'chuoshinsa/detail/([^/]+)/?', detail_href)
        slug = m.group(1) if m else ''

        venue_text = tds[2].get_text(strip=True)

        guidance_a = tds[3].find('a')
        guidance_href = guidance_a.get('href', '') if guidance_a else ''
        if guidance_href:
            # 相対パスまたは絶対URLの処理
            # 例: ../../../pdf/schedule/chuoshinsa/20250504_0505_guidance.pdf -> ../../../pdf/...
            if guidance_href.startswith('/'):
                guidance_href = '../../..' + guidance_href
            elif not guidance_href.startswith(('http', '../', './')):
                guidance_href = '../../../' + guidance_href

        timetable_a = tds[4].find('a')
        timetable_href = timetable_a.get('href', '') if timetable_a else ''
        if timetable_href:
            if timetable_href.startswith('/'):
                timetable_href = '../../..' + timetable_href
            elif not timetable_href.startswith(('http', '../', './')):
                timetable_href = '../../../' + timetable_href

        result_a = tds[5].find('a')
        result_href = result_a.get('href', '') if result_a else ''
        if result_href:
            if result_href.startswith('/'):
                result_href = '../../..' + result_href
            elif not result_href.startswith(('http', '../', './')):
                result_href = '../../../' + result_href

        td_date = f'<td class="d">{date_text}</td>'

        if slug:
            td_name = f'<td><a href="../../../chuoshinsa/detail/{slug}/">{name_text}</a></td>'
        else:
            td_name = f'<td>{name_text}</td>'

        td_venue = f'<td>{venue_text}</td>'

        # PDFのリンクがある場合のみ表示。テキストが空でもリンクがあれば表示。
        # mirrorではリンクタグがあるがテキストが空の場合がある。実ファイルがあるか、またはhrefがあれば「実施要項PDF」を表示するか？
        # mirrorの元の表示をチェック
        if guidance_href and ('guidance' in guidance_href or guidance_a.get_text(strip=True)):
            # mirrorの実体リンク
            td_guidance = f'<td><a href="{guidance_href}">実施要項<span class="pdf">PDF</span></a></td>'
        else:
            td_guidance = '<td></td>'

        if timetable_href and ('timetable' in timetable_href or timetable_a.get_text(strip=True)):
            td_timetable = f'<td><a href="{timetable_href}">立会<span class="pdf">PDF</span></a></td>'
        else:
            td_timetable = '<td></td>'

        if result_href and ('result' in result_href or result_a.get_text(strip=True)):
            td_result = f'<td><a href="{result_href}">結果<span class="pdf">PDF</span></a></td>'
        else:
            td_result = '<td></td>'

        row_html = f'<tr>{td_date}{td_name}{td_venue}{td_guidance}{td_timetable}{td_result}</tr>'
        tbody_rows.append(row_html)

    table_tbody_content = '\n'.join(tbody_rows)

    # 既存のHTMLテンプレートを読み込み
    with open(target_path, 'r', encoding='utf-8') as f:
        orig_html = f.read()

    # tbodyの内容を置換
    new_html = re.sub(r'<tbody>.*?</tbody>', f'<tbody>\n{table_tbody_content}\n</tbody>', orig_html, flags=re.DOTALL)

    # 上部の受審にあたってのリンクや答案用紙のリンクも確認
    # mirror: /pdf/schedule/chuoshinsa/2025_guideline_chuoshinsa.pdf
    # mirror: /pdf/schedule/chuoshinsa/2024_shinsa_touan.pdf
    # target: ../../../schedule/chuoshinsa/ -> ../../../pdf/schedule/chuoshinsa/2025_guideline_chuoshinsa.pdf
    new_html = new_html.replace(
        '<li><a href="../../../schedule/chuoshinsa/">令和７年度 中央審査会受審にあたって</a></li>',
        '<li><a href="../../../pdf/schedule/chuoshinsa/2025_guideline_chuoshinsa.pdf">令和７年度 中央審査会受審にあたって<span class="pdf">PDF</span></a></li>'
    )
    new_html = new_html.replace(
        '<li><a href="../../../schedule/chuoshinsa/">中央審査会 学科試験答案用紙</a></li>',
        '<li><a href="../../../pdf/schedule/chuoshinsa/2024_shinsa_touan.pdf">中央審査会 学科試験答案用紙<span class="pdf">PDF</span></a></li>'
    )

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"Updated {target_path} successfully!")

if __name__ == '__main__':
    update_2025()
