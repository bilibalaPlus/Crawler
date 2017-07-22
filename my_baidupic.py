import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import importlib
import os
import time
import wget
import sys

def sleep(seconds = 1):
    time.sleep(seconds)

def create_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options = options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver

def find_element_by_css_selector(item, selector):
    try:
        return item.find_element_by_css_selector(selector)
    except:
        return None
        
def find_elements_by_css_selector(item, selector):
    try:
        return item.find_elements_by_css_selector(selector)
    except:
        return []

def get_url(tex,p):
    url = ''
    for i in range(p+11,len(tex)):
        if tex[i] != '"':
            url += tex[i]
        else:
            break
    #filename = wget.download(url)
    #os.rename(filename,filename+'.jpg')

if __name__ == '__main__':
    driver = create_chrome_driver()
    driver.get('http://pic.sogou.com/pics?query=%C8%CB%C1%B3&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1500732916&sc=index&sut=2277&sst0=1500732916053')
    driver.execute_script('window.scrollBy(0,5000)')
    sleep(3)

    pics = find_elements_by_css_selector(driver,'head > script')
    
    """
    r = requests.get('http://pic.sogou.com/pics?query=%C8%CB%C1%B3&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1500732916&sc=index&sut=2277&sst0=1500732916053')
    TEXT = r.text
    bs = BeautifulSoup(TEXT,'html5lib')
    pic = bs.select('script[type="text/javascript"]')
    """
    for pic in pics:
        print(pic.tag_name)
        print(pic.text
    """
    pos = pic[0].text.find('thumbUrl',0)

    cnt = 0
    while pos>0:
        cnt += 1
        #get_url(pic[0].text,pos)
        pos = pic.text.find('thumbUrl',pos+8)

    print(cnt)
    """

    driver.quit()