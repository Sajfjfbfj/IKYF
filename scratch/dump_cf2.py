import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r"scratch\remote_latestissue.html", 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cf = soup.find('div', class_='contents-full')
if cf:
    print(cf.prettify()[2800:6000])
