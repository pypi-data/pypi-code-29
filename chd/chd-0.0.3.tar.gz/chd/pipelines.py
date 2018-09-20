import os

from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

from .items import Course, Lesson
from . import settings


class CleanFileNamesPipeline(object):
    def process_item(self, item, spider):
        if 'filename' in item.keys():
            item['filename'][0] = item['filename'][0].replace('!', '')
        return item


class CustomNamingFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return request.meta.get('filename', '')

    def get_media_requests(self, item, info):
        filename = item.get('filename', None)
        meta = {'filename': filename[0]} if filename else {}
        return [Request(x, meta=meta) for x in item.get(self.files_urls_field, [])]
