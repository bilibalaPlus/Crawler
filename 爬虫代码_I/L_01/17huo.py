""" 获取杭州男装衬衫数据 """
# coding:utf-8

import requests
from bs4 import BeautifulSoup

BSLIB = 'html5lib'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
HEADERS = {'user-agent':UA}

def get_products_info(url):
    r = requests.get(url, headers=HEADERS)
    s = BeautifulSoup(r.text, BSLIB)
    pages = s.select('div.pagem.product_list_pager > a')
    next_page = pages[-2].get('href')
    for item in s.select('ul.item > li > a'):
        url = item.get('href').strip()
        if '/shop/' in url:
            continue
        name = item.select('p.item_title')[0].text.strip()
        code = item.select('p.item_info > span')[0].text.strip()
        price = item.select('div.item_info > span')[0].text.strip()
        print(url)
        print('\t' + name)
        print('\t' + code)
        print('\t' + price)
    return next_page if next_page != url else None

if __name__ == '__main__':
    NEXT_PAGE = 'http://www.17huo.com/list-man-0-50011123-0--2m0.html'
    pages = 0
    while NEXT_PAGE:
        NEXT_PAGE = get_products_info(NEXT_PAGE)
        pages += 1
        if pages == 3:
            break