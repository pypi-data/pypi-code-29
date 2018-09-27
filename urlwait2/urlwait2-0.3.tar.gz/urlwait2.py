#!/usr/bin/env python3
import time

import click
from requests import get


@click.command()
@click.argument('url')
def main(url):
    if not url.startswith('http'):
        url = 'http://' + url
    print('urlwait2: waiting for {0}'.format(url))

    attempt = 1
    while True:
        try:
            get(url, allow_redirects=True).raise_for_status()
        except Exception as e:
            print('{0} Attempt {1} failed, retrying in 2 seconds'.format(e, attempt))
            attempt += 1
            time.sleep(2)
        else:
            print('urlwait2: successfully connected to {0}'.format(url))
            break


if __name__ == '__main__':
    main()
