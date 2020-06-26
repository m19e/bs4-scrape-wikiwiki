import requests
from bs4 import BeautifulSoup

URL = "https://wikiwiki.jp/shinycolors/%E5%B0%8F%E5%AE%AE%E6%9E%9C%E7%A9%82"
response = requests.get(URL, timeout=1)

# textでunicode, contentでstr
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')

cards = list(map(lambda h4: {'name': h4.a.text, 'detail': h4.a.get("href"), 'image': soup.select_one("a[href='{0}']>img".format(h4.a.get("href"))).get("src")}, filter(lambda h4: h4.a != None, soup.select("h4[id^='h4_content_']"))))

print(type(cards))
