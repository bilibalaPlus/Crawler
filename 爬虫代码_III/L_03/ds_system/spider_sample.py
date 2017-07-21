# coding:utf-8

import sys
import traceback
import util

PARSERS = util.load_parsers('parsers')

def parse(job, config):
    driver = None
    result = {'id':job['id'],
              'source_id':job['source_id'],
              'status':config.JS_FAILED,  # job状态默认失败
              'content':'',
              'message':''}
    try:
        url = job['url']
        prefix = url.split('//')[1].split('/')[0]
        if prefix in PARSERS:
            driver = util.create_chrome_driver()
            content = PARSERS[prefix](driver, url)
            result['content'] = content
            result['status'] = config.JS_FINISHED
        else:
            raise Exception('No parser for %s.' % url)
    except Exception as e:
        result['message'] = '%s\n%s' % (e, traceback.format_exc())
    finally:
        if driver:
            driver.quit()
        return result
