import re, os

with open(r'C:\Users\user\.gemini\antigravity\brain\7388d7b5-c5ed-4e7f-a797-48c4c820d209\.system_generated\steps\439\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract top guideline links
top_docs = []
msg_body = re.search(r'<div class="message-body">(.*?)</div>', html, re.DOTALL)
if msg_body:
    for m in re.finditer(r'<a href="([^"]+)"[^>]*>(.*?)</a>', msg_body.group(1)):
        href = m.group(1)
        if not href.startswith('http'):
            href = 'https://www.kyudo.jp' + href
        title = m.group(2).strip()
        top_docs.append(f'<li><a href="{href}">{title}</a></li>')

print(f'Top docs found: {len(top_docs)}')

tbody = re.search(r'<tbody>(.*?)</tbody>', html, re.DOTALL)
if tbody:
    rows = re.findall(r'<tr>(.*?)</tr>', tbody.group(1), re.DOTALL)
    print(f'Total rows in remote table: {len(rows)}')
    out_trs = []
    for i, r in enumerate(rows):
        d = re.search(r'<td class="date">(.*?)</td>', r, re.DOTALL)
        date = d.group(1).strip() if d else ''
        
        name_m = re.search(r'<td class="name">.*?<a href="([^"]+)"[^>]*>(?:<u>)?(.*?)(?:</u>)?</a>', r, re.DOTALL)
        name_url = ''
        name_text = ''
        if name_m:
            name_url = name_m.group(1)
            name_text = name_m.group(2).strip()
            slug_m = re.search(r'/detail/([^/]+)/', name_url)
            slug = slug_m.group(1) if slug_m else ''
            name_link = f'<a href="../../chuoshinsa/detail/{slug}/">{name_text}</a>'
        else:
            name_m2 = re.search(r'<td class="name">(.*?)</td>', r, re.DOTALL)
            name_text = re.sub(r'<[^>]+>', ' ', name_m2.group(1)).strip() if name_m2 else ''
            name_link = name_text

        venue_m = re.search(r'<td class="venue">(.*?)</td>', r, re.DOTALL)
        venue = re.sub(r'<!--.*?-->', '', venue_m.group(1)).strip() if venue_m else ''

        guidance_m = re.search(r'<td class="guidance">.*?<a href="([^"]+)".*?</td>', r, re.DOTALL)
        guidance = f'<a href="https://www.kyudo.jp{guidance_m.group(1)}">実施要項<span class="pdf">PDF</span></a>' if guidance_m else ''

        tachiai_m = re.search(r'<td class="tachiai[^"]*">.*?<a href="([^"]+)".*?</td>', r, re.DOTALL)
        tachiai = f'<a href="https://www.kyudo.jp{tachiai_m.group(1)}">立会<span class="pdf">PDF</span></a>' if tachiai_m else ''

        result_m = re.search(r'<td class="result">.*?<a href="([^"]+)".*?</td>', r, re.DOTALL)
        result = f'<a href="https://www.kyudo.jp{result_m.group(1)}">結果<span class="pdf">PDF</span></a>' if result_m else ''

        tr_html = f'<tr><td class="d">{date}</td><td>{name_link}</td><td>{venue}</td><td>{guidance}</td><td>{tachiai}</td><td>{result}</td></tr>'
        out_trs.append(tr_html)

    # Save to scratch
    with open(r'c:\Users\user\Desktop\ホームページ素材\scratch\2021_trs.html', 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(out_trs))

    with open(r'c:\Users\user\Desktop\ホームページ素材\scratch\2021_top_docs.html', 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(top_docs))
