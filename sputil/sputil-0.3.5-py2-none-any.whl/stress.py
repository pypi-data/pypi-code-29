# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 20.

@author: jason96
'''
from sputil.base import SplunkBase
from threading import Lock
import requests
import threading
import time
import signal
import sys


class StressTest(SplunkBase):
    '''
    classdocs
    '''

    def __init__(self):
        super(StressTest, self).__init__()
        signal.signal(signal.SIGINT, self.signal_handler)
        self.count = 0
        self.stop = False

    def signal_handler(self, sig, frame):
        print('You pressed Ctrl+C!')
        self.stop = True

    def get_cval(self, res):
        for cookie in res.cookies:
            if cookie.name == 'cval':
                return cookie.value

    def get_csrf_token(self, res):
        for cookie in res.cookies:
            if cookie.name.startswith('splunkweb_csrf_token'):
                return cookie.value

    def login_test(self):
        lock = Lock()
        base_url = 'http://%s:8000' % (self.config['splunk_ip'],)
        for _ in range(1, 100):

            lock.acquire()
            self.count = self.count + 1
            lock.release()

            res = requests.get(base_url + '/en-US/account/login')
            cval = self.get_cval(res)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181'}
            headers['Accept-Encoding'] = 'gzip, deflate'
            headers['Cookie'] = 'cval=' + cval + ';'

            payload = {'username': self.config['splunk_id'],
                       'password': self.config['splunk_password'],
                       'set_has_logged_in': 'false', 'cval': cval}
            session = requests.Session()

            # login
            res = session.post(base_url+'/ko-KR/account/login',
                               headers=headers,
                               data=payload)
            # get_csrf_token(res)
            if self.stop is True:
                break

    def fire(self, ):

        for _ in range(100):
            t = threading.Thread(target=self.login_test, args=())
            t.start()

        while True:
            before = self.count
            time.sleep(1)
            print '%d(%d)' % (self.count - before, self.count)
            if self.count > 6000:
                break
            if self.stop is True:
                break
        sys.exit(0)


if __name__ == '__main__':

    test = StressTest()
    test.fire()
