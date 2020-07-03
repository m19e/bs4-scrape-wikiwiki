import requests
import urllib.parse
from bs4 import BeautifulSoup


def print_list(list):
    [print(item) for item in list]


def insert_head(l, head):
    r = list(l)
    for _ in range(head - len(r)):
        r = [0] + r
    return r


def a_exists(l):
    for i in list(reversed(list(l))):
        if i.a != None:
            return True
    return False


def filter_by_thead(tables, target):
    return list(filter(lambda x: x.tr.select_one("td") is not None and x.tr.select_one("td").text == target, tables))


def filter_by_onerous(gasha, target):
    for tr in gasha:
        if target in tr.text:
            return tr.a != None
    return True


def get_current_gasha(table):
    head = list(map(lambda x: x.text, table[0].thead.tr.select("th")))
    body = table[0].tbody.select("tr")

    # fil = list(filter(lambda x: a_exists(x), body))
    # texts = [[t.text for t in tr] for tr in fil]
    # f = [insert_head(i, len(head)) for i in texts]
    result = [dict(zip(head, t)) for t in [insert_head(i, len(head)) for i in [
        [t.text for t in tr] for tr in list(filter(lambda x: a_exists(x), body))]]]
    fix = []
    for i, g in enumerate(result):
        cp = dict(g)
        if cp['期間'] == 0:
            cp['期間'] = result[i-1]['期間']
        fix.append(cp)

    return fix


def get_pass_gashas(tables):
    result = []
    for table in tables:
        head = [td.text for td in table.thead.tr.select('td')]
        body = [[td.text for td in tr.select('td')] for tr in [
            trs for trs in list(filter(lambda x: a_exists(x) and filter_by_onerous(x, '有償限定'), table.tbody.select('tr')))]]
        zipped = [dict(zip(head, g))
                  for g in [insert_head(i, len(head)) for i in body]]
        result.append(zipped)
    return result


def get_gasha_table():
    # URL = "https://wikiwiki.jp/shinycolors/%E3%82%AC%E3%82%B7%E3%83%A3"
    # response = requests.get(URL, timeout=5)
    # soup = BeautifulSoup(response.text, 'lxml')
    soup = BeautifulSoup(load_html_file('gashapage.html'), 'lxml')

    table = soup.select("table")
    cur = get_current_gasha(table)

    fed = filter_by_thead(table, '期間')

    result = get_pass_gashas(fed)

    # print_list(sum(result, []))
    save_list_file(sum(result, []), 'gashalist.txt')


def main():
    URL = "https://wikiwiki.jp/shinycolors/%E5%B0%8F%E5%AE%AE%E6%9E%9C%E7%A9%82"
    response = requests.get(URL, timeout=1)
    soup = BeautifulSoup(response.text, 'lxml')

    cards = list(map(lambda h4: {'name': h4.a.text, 'detail': urllib.parse.urljoin("https://wikiwiki.jp/", h4.a.get("href")), 'image': soup.select_one(
        "a[href='{0}']>img".format(h4.a.get("href"))).get("src")}, filter(lambda h4: h4.a != None, soup.select("h4[id^='h4_content_']"))))

    print_list(cards)


def save_html_file(html, filename):
    with open(filename, 'w') as file:
        file.write(html)


def save_list_file(l, filename):
    with open(filename, 'w') as file:
        file.writelines('\n'.join(map(str, l)))


def load_html_file(filename):
    return open(filename)


if __name__ == "__main__":
    # main()
    get_gasha_table()
