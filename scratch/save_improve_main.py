with open(r'site-complete\improve\index.html', encoding='utf-8') as f:
    c = f.read()

start = c.find('<main')
end = c.find('</main>') + 7

with open('scratch/improve_main.txt', 'w', encoding='utf-8') as out:
    out.write(c[start:end])

print("Saved improve_main.txt, len:", end - start)
