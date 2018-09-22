from datetime import datetime
from typing import List, Optional

import requests

from enlightenme.news.news import News
from enlightenme.sources import Source


class HackerNewsSource(Source):
    URL = "https://hacker-news.firebaseio.com/"

    NUMBER_OF_STORIES = 10
    MAX_STORIES_TO_LOOP = 100

    HELP = "Source: hacker-news (https://news.ycombinator.com/)"

    @classmethod
    def name(cls):
        return "hacker-news"

    def __init__(self) -> None:
        super(HackerNewsSource, self).__init__()
        self._story_ids = []

    def fetch(self, keywords: List = None) -> List[News]:
        self._story_ids = self._fetch_new_stories()[0:self.MAX_STORIES_TO_LOOP]
        if keywords:
            return self._fetch_latest_stories_with_keywords(keywords)
        else:
            return self._fetch_latest_stories(number=self.NUMBER_OF_STORIES)

    def _fetch_new_stories(self):
        response = requests.get(self.URL + "v0/newstories.json")
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def _fetch_latest_stories(self, number=20) -> List[News]:
        latest_news = []
        for story_id in self._story_ids[0:number]:
            news = HackerNewsStory(story_id).fetch()
            if news is not None:
                latest_news.append(news)
        return latest_news

    def _fetch_latest_stories_with_keywords(self, keywords: List) \
            -> List[News]:
        interesting_news = []
        for index, story_id in enumerate(self._story_ids):
            news = HackerNewsStory(story_id).fetch()
            if news:
                if news.contains_any_keywords(keywords):
                    interesting_news.append(news)
                if len(interesting_news) == self.NUMBER_OF_STORIES:
                    break
        return interesting_news


class HackerNewsStory:
    def __init__(self, story_id: int, story_details: dict = None):
        self._story_id = story_id
        self._story_details = story_details

    def fetch(self) -> Optional[News]:
        response = requests.get(HackerNewsSource.URL +
                                "v0/item/%s.json" % str(self._story_id))
        if response.status_code == 200:
            self._story_details = response.json()
            if self._story_details is not None:
                return self._create_new_from_story_details()
            return None
        response.raise_for_status()

    def _create_new_from_story_details(self) -> News:
        published_at = datetime.fromtimestamp(self._story_details.get("time"))
        return News(self._story_details.get("title"),
                    published_at,
                    self._story_details.get("text"),
                    self._story_details.get("url"),
                    [],
                    HackerNewsSource.name())
