import pycurl
import re
import json
from io import BytesIO

class CurlLib(object):
    REF_HEADER = 'http://www.joox.com'
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'

    def __init__(self, conn_timeout=60, timeout=60, logger=None):
        self.conn_timeout = conn_timeout
        self.timeout = timeout
        self.logger = logger

    def set_refer_header(self, refer_header):
        self.REF_HEADER = refer_header

    def set_ua(self, user_agent):
        self.USER_AGENT = user_agent

    def error_log(self, error_msg):
        if(self.logger == None):
            print(error_msg) #self.mysql_error_log in std.out
        else:
            self.logger.debug(error_msg)

    def get(self, url, retry_max=0):
        success_flag = True
        retry_count = 0
        while True:
            buf = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.FOLLOWLOCATION, 1)
            c.setopt(c.CONNECTTIMEOUT, self.conn_timeout)
            c.setopt(c.TIMEOUT, self.timeout)
            c.setopt(c.USERAGENT, self.USER_AGENT)
            c.setopt(c.REFERER, self.REF_HEADER)
            c.setopt(c.WRITEDATA, buf)
            try:
                c.perform()
            except pycurl.error as error:
                self.error_log('curl error:[{0}]'.format(json.dumps(error)))
                success_flag = False
            
            if success_flag is True:
                response = buf.getvalue().decode('utf-8')
                buf.close()
                return response
            
            if retry_count > retry_max:
                break
            
            retry_count = retry_count + 1
        return False

