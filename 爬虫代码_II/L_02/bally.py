# coding: utf-8

import sys
import util

def parse(driver, url):
    products = []
    driver.get(url)
    #driver.execute_script('window.scrollBy(0,50000)')
    #util.sleep(3)
    elements = util.find_elements_by_css_selector(driver, 'a.js-producttile_link')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return products

if __name__ == '__main__':
    # Sample: http://www.bally.cn/zh/%E9%80%89%E8%B4%AD%E7%94%B7%E5%A3%AB%E7%B3%BB%E5%88%97/%E9%9E%8B%E5%B1%A5/%E9%9D%B4%E5%AD%90/
    driver = util.create_chrome_driver()
    for product in parse(driver, sys.argv[1]):
        print(product)
    driver.quit()
