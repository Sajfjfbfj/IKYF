import subprocess
import re

out = subprocess.check_output(['git', 'grep', 'map'], cwd=r'c:\Users\user\Desktop\ホームページ素材').decode('utf-8', errors='ignore')
matches = set(re.findall(r'href=["\']([^"\']*map[^"\']*)["\']', out))
for m in sorted(list(matches)):
    print(m)
