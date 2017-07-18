""" Fix coding issue """
# coding:utf-8

import requests

R = requests.get('http://www.ip138.com/post/')
# print(R.text)
# print(R.encoding)
# print(R.text.encode('ISO-8859-1').decode('gbk'))
