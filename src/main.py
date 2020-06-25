import requests
from bs4 import BeautifulSoup

URL = "https://news.yahoo.co.jp/"
response = requests.get(URL, timeout=1)

# textでunicode, contentでstr
print(response.text)

soup = BeautifulSoup(response.text, 'lxml')

for a_tag in soup.find_all('a'):
    print(a_tag.get('href'))  # リンクを表示
