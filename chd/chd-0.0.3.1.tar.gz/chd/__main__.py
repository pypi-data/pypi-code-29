#!/usr/bin/env python

import argparse
from os import getcwd
from os.path import expanduser, join, isabs

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .spiders.ch_spider import CHSpider


def main():
    parser = argparse.ArgumentParser()
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
