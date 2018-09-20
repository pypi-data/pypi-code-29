import logging
import os

import scrapy
from scrapy.loader import ItemLoader

from chd import items


class CHSpider(scrapy.Spider):
    name = "ch"

    def __init__(self, url=None, path=None, start=None, end=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
        try:
            self.start = int(start) - 1 if start is not None else None
        except ValueError:
            self.logger.log(
                logging.INFO, 'The "start" is not an integer. Ignored')
            self.start = None

        try:
            self.end = int(end) if end is not None else None
        except ValueError:
            self.logger.log(
                logging.INFO, 'The "end" is not an integer. Ignored')
            self.end = None

        self.path = path

        self.info_path = os.path.join(self.path, 'info.txt')
        self.links_path = os.path.join(self.path, 'links.txt')
        self.create_download_dir()

    def parse(self, response):
        self.lessons_selector = self.get_lessons_selector(response)
        self.save_links()
        self.save_course_info(response)
        for selector in self.lessons_selector[self.start:self.end]:
            yield self.load_lesson(selector)

    def save_course_info(self, response):
        course = self.load_course(response)
        course_info = f'''
Name: {course['name'][0]}
Original name: {course['original_name'][0]}
Duration: {course['duration'][0]}
Description: {course['description'][0]}

'''

        with open(self.info_path, 'w') as f:
            f.write(course_info)
            self.save_lessons_info(f)

    def save_lessons_info(self, info_file):
        info_file.write('Lessons:\n')
        self.save_lesson_info(info_file)

    def save_lesson_info(self, info_file):
        for selector in self.lessons_selector:
            lesson = self.load_lesson(selector)
            lesson_info = f'{lesson["name"][0]} ({lesson["duration"][0]})\n'
            info_file.write(lesson_info)

    def save_links(self):
        self.lesson_urls = self.lessons_selector.xpath(
            './/link[@itemprop=$itemprop]',
            itemprop="contentUrl").css('::attr(href)').extract()
        with open(self.links_path, 'w') as f:
            for url in self.lesson_urls:
                f.write(f'{url}\n')

    def create_download_dir(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get_lessons_selector(self, response):
        return response.css('.lessons-list__li')

    def load_course(self, response):
        course_loader = ItemLoader(item=items.Course(), response=response)
        course_loader.add_css('name', 'article header.standard-block h1::text')
        course_loader.add_css(
            'original_name', 'article header div.original-name::text')
        course_loader.add_css(
            'description', 'article div.standard-block p::text')
        course_loader.add_css(
            'materials', 'article div.standard-block a.downloads::attr(href)')
        duration = response.css(
            'article div.standard-block__duration::text').extract_first().split(' ')[1]
        course_loader.add_value('duration', duration)

        return course_loader.load_item()

    def load_lesson(self, selector):
        lesson_loader = ItemLoader(items.Lesson(), selector)
        name = selector.xpath(
            './/span[@itemprop="name"]/text()').extract_first()
        url = selector.xpath(
            './/link[@itemprop="contentUrl"]/@href').extract_first()
        extention = url.split('.')[-1]
        filename = f'{name}.{extention}'
        lesson_loader.add_value('name', name)
        lesson_loader.add_value('file_urls', url)
        lesson_loader.add_value('filename', filename)
        lesson_loader.add_css('duration', 'em.lessons-list__duration::text')

        return lesson_loader.load_item()
