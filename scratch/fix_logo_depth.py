import re

for filename in [r'site-complete\category\chuoshinsa\index.html',
                 r'site-complete\category\taikai\index.html']:
    with open(filename, encoding='utf-8') as f:
        c = f.read()
    # Fix the logo link: ../../../的場の水鏡.html → ../../的場の水鏡.html
    fixed = c.replace('../../../的場の水鏡.html', '../../的場の水鏡.html')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(fixed)
    remaining = fixed.count('../../..')
    print(f"{filename}: fixed, ../../.. remaining: {remaining}")
