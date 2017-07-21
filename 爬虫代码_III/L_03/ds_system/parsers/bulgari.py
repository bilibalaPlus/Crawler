# coding: utf-8

import sys
import time
sys.path.append('../')
import util

PREFIX = 'www.bulgari.com'

def parse(driver, url):
    products = []
    driver.get(url)
    i = 0
    while True:
        elements = util.find_elements_by_css_selector(driver, 'a.bul-btn-more')
        cont = False
        for element in elements:
            if element.is_displayed():
                cont = True
                driver.execute_script('arguments[0].click();', element)
                i += 1 # 超过20次就放弃，页面本身有bug
                print('i = %d' % i)
                if i >= 20:
                    cont = False
                    break
                time.sleep(1)
        print(cont)
        if not cont:
            break
    elements = util.find_elements_by_css_selector(driver, 'a.product-link')
    for element in elements:
        products.append(element.get_attribute('href').strip())
    return products
    
if __name__ == '__main__':
    # Sample: https://www.bulgari.com/zh-cn/products.html?root_level=317&sign=594
    driver = util.create_chrome_driver()
    for product in parse(driver, sys.argv[1]):
        print(product)
    driver.quit()
