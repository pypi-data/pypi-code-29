from datetime import datetime

DATE_TIME_STR_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class News:
    def __init__(self, title, published_at: datetime = None,
                 body: str = None, url: str = None,
                 tags=None, source=None):
        if tags is None:
            tags = []
        self.title = title
        self.published_at = published_at if published_at else datetime.now()
        self.body = body
        self.url = url
        self.tags = tags
        self.source = source

    def contains_any_keywords(self, keywords):
        for keyword in keywords:
            if self.has_any_keyword(keyword):
                return True
        return False

    def has_any_keyword(self, keyword: str) -> bool:
        upper_case_keyword = keyword.upper()
        return (self.title and upper_case_keyword in self.title.upper()) or \
               (self.tags and upper_case_keyword in
                [tag.upper() for tag in self.tags]) or \
               (self.body and upper_case_keyword in self.body.upper())

    def to_dict(self):
        return {
            'title': self.title,
            'published_at': datetime.strftime(self.published_at,
                                              DATE_TIME_STR_FORMAT),
            'body': self.body,
            'url': self.url,
            'tags': self.tags,
            'source': self.source,
        }
