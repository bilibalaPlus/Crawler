#---json---
import json

d = {'name':'lin',
    'tile':'Teather'}

t = json.dumps(d)
print(type(t))
print(t)

d = json.loads(t)
print(type(d))
print(d)

#---XML---
#---request---
import requests

r = requests.get('http://www.ip138.com/post')
text = r.text
print(text)