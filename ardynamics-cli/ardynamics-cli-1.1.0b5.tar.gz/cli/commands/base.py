# cli/commands/base.py

import sys
import boto3
from os.path import expanduser, join, abspath
from json import dumps


class Base(object):
    bucket = None

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        session = boto3.Session(region_name='eu-central-1')
        s3 = session.resource('s3')
        self.bucket = s3.Bucket('ardynamics')
        if self.options['--test'] or self.options['--debug']:
            print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    @staticmethod
    def is_virtual():
        return getattr(sys, 'base_prefix', sys.prefix) != sys.prefix or hasattr(sys, 'real_prefix')

    def get_location(self, script_file):
        if self.is_virtual():
            return abspath(join('.', 'test', script_file))
        folder = expanduser("~")
        return abspath(join(folder, script_file))