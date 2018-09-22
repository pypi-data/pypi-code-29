import re
from datetime import datetime
from typing import Optional

from bs4 import BeautifulSoup

from rtv.extractors.common import (
    Extractor, GenericDescriptionMixin, GenericTitleMixin
)
from rtv.utils import get_ext


class Rmf24(GenericTitleMixin, GenericDescriptionMixin, Extractor):
    SITE_NAME = 'rmf24.pl'
    _VALID_URL = r'https?://(?:www\.)?rmf24\.pl/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_html()
        self.soup = BeautifulSoup(self.html, 'lxml')
        # TODO: use decorators to mark the need to use bs4?
        # TODO: make_soup(html=Optional) or/and load_html(url=Optional)

    def get_date(self) -> Optional[datetime]:
        meta_tag = self.soup.select_one('meta[itemprop=datePublished]')
        if meta_tag:
            date_published_str = meta_tag.get('content')
            return datetime.strptime(date_published_str, '%Y-%m-%dT%H:%M:%S')
        return None

    def _get_audio_source_url(self) -> Optional[str]:
        pattern = re.compile(r'audio.src\s*=\s*[\'\"](?P<url>.*)[\'\"]')
        match = pattern.search(self.html)
        if match:
            return match.group('url')
        return None

    # def _get_video_entries(self) -> list:
    #     # .embed-video video > source
    #     entries = [video['src'] for video in self.soup.select('video > source')]
    #     return entries

    def extract(self):
        audio_url = self._get_audio_source_url()
        extension = get_ext(audio_url)

        entries = [{
            'title': self.get_title(),
            'description': self.get_description(),
            'date': self.get_date(),
            'url': audio_url,
            'ext': extension
        }]

        return entries
