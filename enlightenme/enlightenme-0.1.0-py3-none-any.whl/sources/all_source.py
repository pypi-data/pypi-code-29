from typing import List

import click

from enlightenme.news.news import News
from enlightenme.sources import Source


class AllSource(Source):
    HELP = "Pulls news from all the available sources"

    def __init__(self, **kwargs):
        print(kwargs)
        self.sources = []
        for source in Source.get_all_source_sub_classes():
            if source is not AllSource:
                source_name = source.name()
                source_kwargs = self._extract_source_args(kwargs, source_name)
                self.sources.append(source(**source_kwargs))

    def fetch(self, keywords: List = None) -> List[News]:
        return sum([source.fetch() for source in self.sources], [])

    @classmethod
    def name(cls):
        return "all"

    @classmethod
    def params(cls) -> List[click.Option]:
        return sum([cls._get_prefixed_source_params(source)
                    for source in Source.get_all_source_sub_classes()
                    if source is not AllSource],
                   [])

    @classmethod
    def _get_prefixed_source_params(cls, source):
        source_params = []

        def prefix_opts(opts, prefix):
            return ["--%s-%s" % (prefix, opt[2:])
                    for opt in opts
                    if opt[:2] == "--"]

        for param in source.params():
            prefix = source.name()
            param.name = '%s_%s' % (prefix, param.name)
            param.opts = prefix_opts(param.opts, prefix)
            param.secondary_opts = prefix_opts(param.secondary_opts, prefix)
            source_params.append(param)
        return source_params

    def _extract_source_args(self, kwargs, source_name):
        source_kwargs = {k.replace("%s_" % source_name, ''): v
                         for k, v in kwargs.items() if
                         k.startswith(source_name)}
        return source_kwargs
