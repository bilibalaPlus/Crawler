""" Async and dynamic """

import grequests
import threadpool
from multiprocessing import Queue
from multiprocessing import cpu_count

stocks = ['sh600005',
          'sh600006',
          'sh600007',
          'sh600008',
          'sh600009',
          'sh600010']

data = []
rs = [grequests.get('http://hq.sinajs.cn/list=' + stock) for stock in stocks]
for r in grequests.map(rs):
    text = r.text[4:]
    exec(text)
    items = (eval('hq_str_' + r.url[-8:])).split(',')
    data.append({'name':items[0], 'date':items[-3], 'open':items[1]})
for d in data:
    print('name: %s, open: %s, date: %s' % (d['name'], d['open'], d['date']))