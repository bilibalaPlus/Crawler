""" Get ZipCodes """
# coding:utf-8

import requests
from bs4 import BeautifulSoup

BSLIB = 'html5lib'
BASE_URL = 'http://www.ip138.com'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
HEADERS = {'user-agent':UA}

def handle_zip_code(province, url):
    r = requests.get(url, headers=HEADERS)
    s = BeautifulSoup(r.text.encode("iso-8859-1").decode("gbk"), BSLIB)
    print(province)
    rows = s.select('table.t12 > tbody > tr')
    for i in range(1, len(rows)):
        items = rows[i].select('td')
        a_1 = items[0].text.strip()
        if a_1:
            print('\t%s, %s' % (a_1, items[1].text.strip()))
        if len(items) >= 4:
            a_2 = items[3].text.strip()
            if a_2:
                print('\t%s, %s' % (a_2, items[4].text.strip()))

if __name__ == '__main__':
    R = requests.get(BASE_URL + '/post/', headers=HEADERS)
    TEXT = R.text.encode('iso-8859-1').decode('gbk')
    S = BeautifulSoup(TEXT, BSLIB)
    for item in S.select('div#newAlexa > table > tbody > tr > td > a'):
        print(item.text)
        #handle_zip_code(item.text, BASE_URL + item.get('href'))
