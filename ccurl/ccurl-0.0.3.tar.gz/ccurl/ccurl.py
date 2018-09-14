from __future__ import print_function
import os
import sys
import time
import subprocess
import argparse


class colors:
    BLUE = '\033[94m'
    CYAN   = '\033[36m'
    YELLOW = '\033[93m'
    RED = '\033[31m'
    ENDCOLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--repeat', dest='repeat_times', default=1,
                        help='The number of times to repeat the request')
    parser.add_argument('--delay', dest='delay_seconds', default=1,
                        help='The number of seconds to delay between requests')
    parser.add_argument('--name', dest='display_name', required=False,
                        help='An optional label to display rather than the first characters of the URL')
    args = parser.parse_args()
    return args


def ccurl(
    url,
    repeat_times,
    delay_seconds,
    display_name):
    # format of command without python string interpolation making it weird
    # curl -k url.com --write-out %{http_code} --silent --output /dev/null
    cmd = "curl -k {} --write-out %{{http_code}} --silent --output /dev/null".format(url)
    print(cmd)

    ok_count = 0
    total_count = 0
    response_codes = {}
    for idx in range(int(repeat_times)):
        try:
            status_code = int(subprocess.check_output(cmd, shell=True))

            if not status_code in response_codes:
                response_codes[status_code] = 1
            else:
                response_codes[status_code] += 1
            if status_code >= 300 and status_code <= 499:
                color = colors.YELLOW
            elif status_code >= 500 and status_code <= 599:
                color = colors.RED
            else:
                color = colors.ENDCOLOR

            if not display_name:
                display_name = "{}{}".format(
                    url[0:20],
                    '...' if len(url) > 20 else '')

            print("{}{} (try {}) Status: {}, Accum: {}".format(
                color,
                display_name,
                idx,
                status_code,
                response_codes))
            time.sleep(int(delay_seconds))
        except KeyboardInterrupt:
            sys.exit(1)
            break


def main():
    here = os.path.abspath(os.path.dirname(__file__))
    about = {}
    with open(os.path.join(here, 'version.py'), 'r') as f:
        exec(f.read(), about)

    print('Continuous Curl version {}'.format(about['__version__']))

    args = parse_args()
    ccurl(
        args.url,
        args.repeat_times,
        args.delay_seconds,
        args.display_name)


if __name__ == '__main__':
    main()
