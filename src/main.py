import requests
from bs4 import BeautifulSoup

URL = "https://wikiwiki.jp/shinycolors/%E5%B0%8F%E5%AE%AE%E6%9E%9C%E7%A9%82"
response = requests.get(URL, timeout=1)

# textでunicode, contentでstr
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')

for h4_tag in soup.select("h4[id^='h4_content_']"):
    print(h4_tag.text)
