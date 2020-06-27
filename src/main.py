import requests
import urllib.parse
from bs4 import BeautifulSoup


def print_list(list):
    [print(item) for item in list]


def insert_head(l, head):
    if len(l) < head:
        return [0] + l
    return l


def get_gasha_table():
    URL = "https://wikiwiki.jp/shinycolors/%E3%82%AC%E3%82%B7%E3%83%A3"
    response = requests.get(URL, timeout=1)
    soup = BeautifulSoup(response.text, 'lxml')

    table = soup.select("table")
    head = list(map(lambda x: x.text, table[0].thead.tr.select("th")))
    body = table[0].tbody.select("tr")

    texts = [[t.text for t in tr] for tr in body]
    f = [insert_head(i, len(head)) for i in texts]
    result = [dict(zip(head, t)) for t in f]
    print_list(result)


def main():
    URL = "https://wikiwiki.jp/shinycolors/%E5%B0%8F%E5%AE%AE%E6%9E%9C%E7%A9%82"
    response = requests.get(URL, timeout=1)
    soup = BeautifulSoup(response.text, 'lxml')

    cards = list(map(lambda h4: {'name': h4.a.text, 'detail': urllib.parse.urljoin("https://wikiwiki.jp/", h4.a.get("href")), 'image': soup.select_one(
        "a[href='{0}']>img".format(h4.a.get("href"))).get("src")}, filter(lambda h4: h4.a != None, soup.select("h4[id^='h4_content_']"))))

    print_list(cards)


if __name__ == "__main__":
    # main()
    get_gasha_table()
