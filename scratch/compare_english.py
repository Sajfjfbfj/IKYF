with open(r'c:\Users\user\Desktop\全日本弓道連盟\kyudo\www.kyudo.jp\info\english.html', encoding='utf-8', errors='ignore') as f:
    mirror_eng = f.read()

with open(r'site-complete\info\english.html', encoding='utf-8') as f:
    sc_eng = f.read()

m_start = mirror_eng.find('<main')
m_end = mirror_eng.find('</main>')
sc_start = sc_eng.find('<main')
sc_end = sc_eng.find('</main>')

with open('scratch/eng_comparison.txt', 'w', encoding='utf-8') as out:
    out.write("=== MIRROR MAIN ===\n")
    out.write(mirror_eng[m_start:m_end+7])
    out.write("\n\n=== SITE-COMPLETE MAIN ===\n")
    out.write(sc_eng[sc_start:sc_end+7])

print("Saved eng_comparison.txt")
