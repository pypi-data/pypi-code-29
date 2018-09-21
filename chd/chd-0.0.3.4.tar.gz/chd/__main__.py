#!/usr/bin/env python

import argparse
import sys
import os
from os import getcwd
from os.path import expanduser, join, isabs

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import chd
from .spiders.ch_spider import CHSpider


SCRAPY_SETTINGS_MODULE='chd.settings'
SCRAPY_PROJECT = 'chd'

os.environ['SCRAPY_SETTINGS_MODULE'] = SCRAPY_SETTINGS_MODULE
os.environ['SCRAPY_PROJECT'] = SCRAPY_PROJECT


def main():
    parser = argparse.ArgumentParser(prog='chd', description=chd.__doc__)
    parser.add_argument('url', help='course url', type=str)
    parser.add_argument(
        '-p',
        '--path',
        type=str,
        help='download path, default is ~/downloads/course-name'
    )
    parser.add_argument(
        '-s',
        '--start',
        type=int,
        help='the lesson number from which to start the download'
    )
    parser.add_argument(
        '-e',
        '--end',
        type=int,
        help='the lesson number at which the download will be completed'
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        help='print version information and exit',
        version=f'{parser.prog} {chd.__version__}'
        
    )

    args = parser.parse_args()

    settings = get_project_settings()
    settings.set('FILES_STORE',
                 join(expanduser('~/downloads'), args.url.split('/')[-1]))
    if args.path:
        if isabs(args.path):
            settings.set('FILES_STORE', args.path)
        else:
            settings.set('FILES_STORE', join(getcwd(), args.path))

    process = CrawlerProcess(settings)
    process.crawl(CHSpider, url=args.url, path=settings.get('FILES_STORE'),
                  start=args.start, end=args.end)
    process.start()


if __name__ == '__main__':
    main()
