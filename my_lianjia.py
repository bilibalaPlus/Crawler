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

def parse(driver,url):
    driver.get(url)
    elements = find_elements_by_css_selector(driver,'div.bigImgList > div.item')
    houses=[]
    for element in elements:
        titles = element.find_element_by_css_selector('a.title')
        prices = element.find_element_by_css_selector('div.price > span')
        title = titles.text
        price = prices.text
        houses.append([title,price])

    return houses

URL = 'https://bj.lianjia.com/ershoufang/?utm_source=baidu&utm_medium=ppc&utm_term=%E9%93%BE%E5%AE%B6&utm_content=%E5%93%81%E7%89%8C_%E5%93%81%E7%89%8C&utm_campaign=%E5%93%81%E7%89%8C%E8%AF%8D_%E7%B2%BE%E7%A1%AE&ljref=pc_sem_baidu_sstg_ppc'

if __name__ == '__main__':
    driver = create_chrome_driver()

    for house in parse(driver,URL):
        print(house)

    driver.quit()