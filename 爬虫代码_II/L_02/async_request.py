import grequests

urls = ['http://news.sina.com.cn',
        'http://www.baidu.com',
        'http://www.so.com',
        'http://www.csdn.com']

rs = [grequests.get(url) for url in urls]
for r in grequests.map(rs):
    print(r.status_code, r.encoding)

# https://github.com/kennethreitz/grequests/blob/master/grequests.py
    