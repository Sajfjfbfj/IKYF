import re
with open(r'site-complete\category\chuoshinsa\index.html', encoding='utf-8') as f:
    c = f.read()

count_deep = c.count('../../')
count_one = c.count('../')
with open('scratch/cat_check.txt', 'w', encoding='utf-8') as out:
    out.write(f"../../ count: {count_deep}\n")
    out.write(f"../ count: {count_one}\n")
    main_start = c.find('<main')
    main_end = c.find('</main>') + 7
    out.write('\nMain content:\n')
    out.write(c[main_start:main_end])

print(f"../../ count: {count_deep}, ../ count: {count_one}")
