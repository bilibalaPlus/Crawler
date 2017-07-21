import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookies = {'cookie': 'bid=qD8OOq_UqUU; ll="108296"; gr_user_id=25a4f7f8-1ffc-4c28-a6ba-83de7be683ae; viewed="24703171_22993903"; _vwo_uuid_v2=C89857F2349D6C77F158F6E66E92AD1D|c8dc205a22f2ec9bc9d286f6d52caeb7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1500439696%2C%22https%3A%2F%2Fwww.google.co.jp%2F%22%5D; ps=y; __yadk_uid=CcYA3jvmrNmFkHObkXxZbYfIEN7TW7PL; ap=1; __utmt=1; dbcl2="163994952:qm6cKevpMog"; _ga=GA1.2.482272683.1493810699; _gid=GA1.2.278142237.1500440795; _gat_UA-7019765-1=1; ck=hoCg; _pk_id.100001.8cb4=d37b273bf333df1d.1500364347.2.1500442245.1500364347.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.482272683.1493810699.1500364350.1500439699.16; __utmb=30149280.15.10.1500439699; __utmc=30149280; __utmz=30149280.1500364350.15.11.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=30149280.16399'}
url = 'http://www.douban.com'
r = requests.get(url, cookies = cookies, headers = headers)
with open('douban_2.txt', 'wb+') as f:
    f.write(r.content)