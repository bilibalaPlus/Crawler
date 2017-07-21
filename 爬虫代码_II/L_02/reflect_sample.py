""" Load modules dynamically """
# coding:utf-8

import importlib
import os
import traceback
import util

def load_modulers(folder, name=''):
    if folder.endswith('/'):
        folder = folder[:-1]
    modules = {}
    for f in os.listdir(folder):
        if not os.path.isfile(folder + '/' + f):
            continue
        if name and (f != (name + '.py')):
            continue
        if f.endswith('.py'):
            module = importlib.import_module(folder + '.' + f[:-3])
            modules[module.PREFIX] = module
            print("Module for '%s' loaded" % module.PREFIX)
    return modules

if __name__ == '__main__':
    modules = load_modulers('mod')
    urls = ['http://www.bally.cn/zh/%E9%80%89%E8%B4%AD%E7%94%B7%E5%A3%AB%E7%B3%BB%E5%88%97/%E9%9E%8B%E5%B1%A5/%E9%9D%B4%E5%AD%90/',
             'https://www.bulgari.com/zh-cn/products.html?root_level=317&sign=594',
             'http://www.baidu.com']
    for url in urls:
        driver = None
        try:
            prefix = url.split('//')[1].split('/')[0]
            if prefix in modules:
                print(url)
                driver = util.create_chrome_driver()
                products = modules[prefix].parse(driver, url)
                for product in products:
                    print('\t' + product)
            else:
                raise Exception("Can't parse %s" % prefix)
        except Exception as e:
            print('%s\n%s' % (e, traceback.format_exc()))
        finally:
            if driver:
                driver.quit()