with open(r'c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\improve\02.html', encoding='utf-8', errors='ignore') as f:
    c = f.read()

start = c.find('<main')
end = c.find('</main>') + 7

with open('scratch/mirror_improve_02.txt', 'w', encoding='utf-8') as out:
    out.write(c[start:end])

print("Saved mirror_improve_02.txt, len:", end - start)
