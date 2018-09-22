from typing import List, Dict

from enlightenme.news import news_formatters
from enlightenme.news.news_formatters import NewsFormatter
from enlightenme.sources import Source


class NewsManager:
    def __init__(self, source_name: str,
                 source_params: Dict = None,
                 keywords: List = None,
                 format_type=NewsFormatter.DEFAULT_FORMAT):
        self._source_name = source_name
        self._source_params = source_params if source_params else {}
        self._format_type = format_type
        self._keywords = keywords
        self._news_list = []

    def fetch_and_format(self) -> str:
        self._fetch()
        return self._format()

    def _fetch(self):
        source_class = Source.get_source(self._source_name)
        __import__(source_class.__module__, fromlist=[source_class.__name__])
        source_object = source_class(**self._source_params)
        self._news_list = source_object.fetch(keywords=self._keywords)

    def _format(self) -> str:
        kls = news_formatters.NewsFormatter.formatter_for_format(
            self._format_type)
        formatter = kls(self._news_list)
        return formatter.format()
