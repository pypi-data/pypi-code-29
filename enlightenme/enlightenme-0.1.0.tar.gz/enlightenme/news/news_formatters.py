import csv
import io
import json
from abc import ABCMeta, abstractmethod
from copy import deepcopy
from typing import List, Any

from enlightenme.news.news import News, DATE_TIME_STR_FORMAT
from enlightenme.utils import camel_case


class NewsFormatter:
    __metaclass__ = ABCMeta

    DEFAULT_FORMAT = "list"
    FORMAT_OPTIONS = ['list', 'csv', 'json']

    def __init__(self, news_list: List[News]):
        self._news_list = news_list

    @property
    def news_list(self):
        return self._news_list

    @news_list.setter
    def news_list(self, value: List[News]):
        self._news_list = value

    @abstractmethod
    def format(self) -> Any:
        raise NotImplementedError

    @classmethod
    def formatter_for_format(cls, format_type: str):
        return eval("%sNewsFormatter" % camel_case(format_type))


class ListNewsFormatter(NewsFormatter):
    def format(self) -> str:
        output = "\n"
        for index, news in enumerate(self.news_list):
            output += "\t%d. Title: %s\n" % (index + 1, news.title)
            published_at = news.published_at.strftime(DATE_TIME_STR_FORMAT)
            output += "\t    Published At: %s\n" % published_at

            if news.url:
                output += "\t    URL: %s\n" % news.url
            if news.tags:
                output += "\t    Tags: %s\n" % ", ".join(news.tags)
            if news.source:
                output += "\t    Source: %s\n" % news.source
        return output


class CsvNewsFormatter(NewsFormatter):
    def format(self) -> str:
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
        for index, news in enumerate(self.news_list):
            if index == 0:
                writer.writerow(news.to_dict().keys())
            news_dict = deepcopy(news.to_dict())
            writer.writerow(news_dict.values())
        return output.getvalue()


class JsonNewsFormatter(NewsFormatter):
    def format(self) -> str:
        return json.dumps([news.to_dict() for news in self.news_list])
