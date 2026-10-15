paths = [
    'site-complete/category/category/category/category/category/chuoshinsa/2021chuoshinsa/index.html',
    'site-complete/category/chuoshinsa/2021chuoshinsa/index.html'
]
for path in paths:
    with open(path, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    txt = txt.replace('20210704_02_result"', '20210704_02_result.pdf"')
    txt = txt.replace("20210704_02_result'", "20210704_02_result.pdf'")
    txt = txt.replace('20211009_02_guidance"', '20211009_02_guidance.pdf"')
    txt = txt.replace("20211009_02_guidance'", "20211009_02_guidance.pdf'")
    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(txt)
print('Fixed missing .pdf in 2021chuoshinsa!')
