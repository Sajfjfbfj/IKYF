import os, re

for cat in ['notice1', 'notice2', 'notice3']:
    path = f'site-complete/notice-cat/{cat}/index.html'
    with open(path, encoding='utf-8') as f:
        c = f.read()
    with open(f'scratch/notice_{cat}.txt', 'w', encoding='utf-8') as out:
        m_start = c.find('<main')
        m_end = c.find('</main>') + 7
        out.write(c[m_start:m_end])
    print(f'{cat}: saved')
