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

URL = 'https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2017-07-25&searchArrivalTime=2017-07-28&nextNDays=0&startSearch=true&fromCode=BJS&toCode=SHA&from=qunarindex&lowestPrice=null'

def parse(driver,url):
    driver.get(url)
    
    sleep(3)
    nextpage = find_element_by_css_selector(driver,'a.page-link')
    driver.execute_script('arguments[0].click();', nextpage)
    sleep(3)

    items = find_elements_by_css_selector(driver,'div.air')
    for item in items:
        driver.execute_script('arguments[0].click();', item)
        sleep(1)
    
    flys = []
    elements = find_elements_by_css_selector(driver,'div.e-airfly > div.col-price > div.vim > span')
    prices = find_elements_by_css_selector(driver,'div.prc > span')
    for element in elements:
        flys.append(element.get_attribute('data-reactid').strip())
        flys.append(element.text)
    for price in prices:
        flys.append(price.text)

    return flys

if __name__ == '__main__':
    driver = create_chrome_driver()

    for fly in parse(driver,URL):
        print(fly)

    driver.quit()

