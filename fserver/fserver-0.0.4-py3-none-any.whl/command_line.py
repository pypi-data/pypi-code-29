import sys

from gevent.pywsgi import WSGIServer
import getopt

import fserver
from fserver.fserver_app import app as application
from fserver import util

help_str = '''usage: fserver [-h] [-d] [port]

  positional arguments:
    port                  Specify alternate port [default: 2000]

  optional arguments:
    -h, --help            show this help message and exit
    -d, --debug           use debug mode of fserver

  arguments of url:
    m                     get_arg to set the mode of processing method of file
                          Such as http://localhost:port?m=dv to download the file specified by url
                          value 'p' to play file with Dplayer
                          value 'v' to show the file specified by url
                          value 'dv' to download the file specified by url
 '''


def run_fserver():
    try:
        options, args = getopt.getopt(sys.argv[1:], 'hdv', ['help', 'debug', 'version'])
    except getopt.GetoptError as e:
        print('error:', e.msg)
        print(help_str)
        sys.exit()

    # init conf
    port = 2000
    util.DEBUG = False

    if len(args) > 0:
        port = args[0]
        if not port.isdigit():
            print('error: port must be int, input:', port)
            sys.exit()

    for name, value in options:
        if name in ['-h', '--help']:
            print(help_str)
            sys.exit()
        if name in ['-d', '--debug']:
            util.DEBUG = True
        if name in ['-v', '--version']:
            print('fserver', fserver._VERSION)

    ips = util.get_ip_v4()
    print('fserver is available at following address:')
    for ip in ips:
        print(' ', ip + ':' + str(port))
    print(' ', '127.0.0.1:' + str(port))

    http_server = WSGIServer(('0.0.0.0', port), application)
    http_server.serve_forever()


if __name__ == '__main__':
    run_fserver()
