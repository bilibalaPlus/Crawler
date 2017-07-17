""" Sample of requests """
# coding:utf-8

import requests

def simple_get(url):
    print('simple_get')
    r = requests.get(url)
    print(dir(r))
    print('\t' + str(r.status_code))
    print('\t' + str(r.headers))
    print('\t' + str(r.encoding))
    print('\t' + r.text)

def get_with_header(url):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    r = requests.get(url, headers={'user-agent':ua})
    print(r.text)

def get_with_parameters(url):
    r = requests.get("http://httpbin.org/get", params={'key1':'你好', 'key2':'世界'})
    print(dir(r))
    print(r.url) # The url used for request
    print(r.text)

def get_json_data(url):
    r = requests.get(url)
    jdata = r.json()
    print(type(jdata))
    print(jdata)

def get_using_cookie(url):
    r = requests.get(url, cookies={'key1':'hello', 'key2':'world'})
    for k, v in r.cookies.items():
        print(k, v)

if __name__ == '__main__':
    # simple_get('http://httpbin.org/get')
    # get_with_header('http://httpbin.org/get')
    # get_with_parameters('http://httpbin.org/get')
    # get_json_data('http://apis.juhe.cn/mobile/get?phone=13429667914&key=05ff96fc7ca7ee1ff48ee772bddd0320')
    cookies = get_using_cookie('http://www.baidu.com')
