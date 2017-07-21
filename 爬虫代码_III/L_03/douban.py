# coding: utf-8

import time
from selenium import webdriver

if __name__ == '__main__':
    DRIVER = webdriver.Chrome() # DRIVER大写是为了满足Pylint静态代码检查规范
    try:    
        DRIVER.get('https://www.douban.com/')
        EMAIL = DRIVER.find_element_by_css_selector('input#form_email') # 用户名输入框
        PASSWORD = DRIVER.find_element_by_css_selector('input#form_password') # 密码输入框
        LOGIN = DRIVER.find_element_by_css_selector('input.bn-submit')
        EMAIL.send_keys('regdzz.lin@gmail.com')
        PASSWORD.send_keys('Julyedu123!')
        LOGIN.click() # 提交
        time.sleep(15)
        DRIVER.save_screenshot('douban.jpg')
    except Exception as e:
        pass
    finally:
        if DRIVER:
            DRIVER.quit()