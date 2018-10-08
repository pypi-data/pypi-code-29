import sys

from gevent.pywsgi import WSGIServer
import getopt

import fserver
from fserver.fserver_app import app as application
from fserver import util

help_str_short = 'usage: fserver [-h] [-d] [--ip ADDRESS] [port]'
help_str = '''usage: fserver [-h] [-d] [--ip ADDRESS] [port]

  positional arguments:
    port                  Specify alternate port [default: 2000]

  optional arguments:
    -h, --help            show this help message and exit
    -d, --debug           use debug mode of fserver
    -i ADDRESS, --ip ADDRESS,
                          Specify alternate bind address [default: all interfaces]

  arguments of url:
    m                     get_arg to set the mode of processing method of file
                          Such as http://localhost:port?m=dv to download the file specified by url
                          value 'p' to play file with Dplayer
                          value 'v' to show the file specified by url
                          value 'dv' to download the file specified by url
 '''


def run_fserver():
    try:
        options, args = getopt.getopt(sys.argv[1:], 'hdvi:', ['help', 'debug', 'version', 'ip='])
    except getopt.GetoptError as e:
        print(help_str_short)
        print('error:', e.msg)
        sys.exit()

    # init conf
    ip = '0.0.0.0'
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
        if name in ['-i', '--ip']:
            ip = value
        if name in ['-v', '--version']:
            print('fserver', fserver._VERSION)

    print('fserver is available at following address:')
    if ip == '0.0.0.0':
        ips = util.get_ip_v4()
        for _ip in ips:
            print('  %s:%s' % (_ip, port))
        print('  127.0.0.1:%s' % port)
    else:
        print('  %s:%s' % (ip, port))

    http_server = WSGIServer((ip, int(port)), application)
    http_server.serve_forever()


if __name__ == '__main__':
    run_fserver()
