import os

mirror_news = r'c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\news'

for f in ['index.html', 'news_202208.html', 'news_202208_01.html', 'news_20260220.html', 'news_20260302.html']:
    fp = os.path.join(mirror_news, f)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8', errors='ignore') as fp_in:
            c = fp_in.read()
        start = c.find('<main')
        end = c.find('</main>')
        main = c[start:end+7] if start != -1 and end != -1 else "No main"
        with open(f'scratch/news_{f}.txt', 'w', encoding='utf-8') as out:
            out.write(main)
        print(f"Saved news_{f}.txt, main len: {len(main)}")
