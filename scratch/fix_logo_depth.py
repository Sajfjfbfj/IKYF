import re

for filename in [r'site-complete\category\chuoshinsa\index.html',
                 r'site-complete\category\taikai\index.html']:
    with open(filename, encoding='utf-8') as f:
        c = f.read()
    # Fix the logo link: ../../../index.html → ../../index.html
    fixed = c.replace('../../../index.html', '../../index.html')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(fixed)
    remaining = fixed.count('../../..')
    print(f"{filename}: fixed, ../../.. remaining: {remaining}")
