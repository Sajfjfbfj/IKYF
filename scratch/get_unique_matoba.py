import subprocess
import re

out = subprocess.check_output(['git', 'grep', '水鏡'], cwd=r'c:\Users\user\Desktop\ホームページ素材').decode('utf-8', errors='ignore')
matches = set(re.findall(r'[^"\'<>\s]*水鏡[^\s"\'<>]*', out))
for m in sorted(list(matches)):
    print(m)
