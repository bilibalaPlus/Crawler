''' Parse XML using DOM '''
# coding:utf-8

import xml.dom.minidom
from xml.dom.minidom import parse

DT = xml.dom.minidom.parse('sample.xml')
COLLECTION = DT.documentElement
if COLLECTION.hasAttribute('shelf'):
   print('Root element : %s' % COLLECTION.getAttribute('shelf'))
# Get all films and print detail information
MOVIES = COLLECTION.getElementsByTagName('movie')
# 打印每部电影的详细信息
for movie in MOVIES:
    type_ = movie.getElementsByTagName('type')[0]
    format_ = movie.getElementsByTagName('format')[0]
    rating = movie.getElementsByTagName('rating')[0]
    description = movie.getElementsByTagName('description')[0]
    print('*****Movie*****')
    print('\tTitle: %s' % movie.getAttribute('title'))
    print('\tType: %s' % type_.childNodes[0].data)
    print('\tFormat: %s' % format_.childNodes[0].data)
    print('\tRating: %s' % rating.childNodes[0].data)
    print('\tDescription: %s' % description.childNodes[0].data)
