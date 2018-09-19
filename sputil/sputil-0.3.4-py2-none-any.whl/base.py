# -*- coding: utf-8 -*-

'''
Created on 2018. 9. 12.
@author: jason96
'''
from splunklib import client
import ConfigParser
import os
from pyutil.fileutil import write_file


SPINDEX = 'sputil-test'
VERSION = '0.3.4'


class SplunkBase(object):

    def __init__(self):

        if os.path.exists('splunk.cfg') == False:
            splunk_cfg = []
            splunk_cfg.append('[splunk]')
            splunk_cfg.append('ip=127.0.0.1')
            splunk_cfg.append('port=8089')
            splunk_cfg.append('id=admin')
            splunk_cfg.append('password=changepassword')
            write_file('splunk.cfg', '\n'.join(splunk_cfg))
            print 'splunk.cfg file was created.\n'
            print 'Change the contents of the file accordingly.\n'

        cfg = ConfigParser.ConfigParser()
        cfg.read('splunk.cfg')
        self.config = {}
        self.config['splunk_ip'] = cfg.get('splunk', 'ip')
        self.config['splunk_id'] = cfg.get('splunk', 'id')
        self.config['splunk_port'] = cfg.get('splunk', 'port')
        self.config['splunk_password'] = cfg.get('splunk', 'password')

        self.service = client.connect(host=self.config['splunk_ip'],
                                      port=self.config['splunk_port'],
                                      username=self.config['splunk_id'],
                                      password=self.config['splunk_password'])


class SplunkCustom(SplunkBase):

    def __init__(self):
        super(SplunkCustom, self).__init__()
