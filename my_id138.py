import requests
from bs4 import BeautifulSoup

BSLIB = 'html5lib'
BASE_URL = 'http://www.ip138.com'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
HEADERS = {'user-agent':UA}

def handle_prov(url):
    r = requests.get(url,headers=HEADERS)
    text = r.text.encode('iso-8859-1').decode('gbk')
    s = BeautifulSoup(text,'html5lib')
    items = s.select('table.t12 > tbody > tr')
    for i in range(1,len(items)):
        item = items[i].select('td')
        if(item[0].text.strip()):
            print(item[0].text,item[1].text)
            if(len(item)>3 and item[3].text.strip()):
                print(item[3].text,item[4].text)


if __name__ == '__main__':
    R = requests.get(BASE_URL+'/post/',headers=HEADERS)
    TEXT = R.text.encode('iso-8859-1').decode('gbk')
    S = BeautifulSoup(TEXT,'html5lib')
    for prov in S.select('div#newAlexa > table > tbody > tr > td > a'):
        handle_prov(BASE_URL+prov.get('href'))