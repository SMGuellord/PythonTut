import requests
from bs4 import BeautifulSoup


"""def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org/trade/search.php?pages='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)

        for link in soup.findAll('a', {'class' : 'item-name'}):
            href= "https://buckysroom.org"+link.get('href')
            print(href)
        page += 1"""


def get_single_item_date(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class ': 'i-name'}):
        print(item_name.string)

    for link in soup.findAll('a'):
        href = str(item_url) + link.get('href')
        print(href)


#trade_spider(1)

get_single_item_date("http://dmoz-odp.org/")