# coding: utf-8

from selenium import webdriver
import importlib
import os
import time

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