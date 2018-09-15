import json
import urllib.parse
import urllib.request
import html

def filter_keys(d, *keys):
    return {k: v for k, v in d.items() if k not in keys}


def custom_objects(d):
    if not isinstance(d, dict):
        return d

    return {k: custom_objects(v) for k, v in d if k[0] == "_" and "." not in k}


def unwrap_list(l, func=lambda x: x._asdict()):
    if l is None:
        return None

    else:
        return [func(x) for x in l]


def clean_dict(d):
    if isinstance(d, list):
        return [clean_dict(sub_d) for sub_d in d]

    elif isinstance(d, dict):
        return dict((k, clean_dict(v)) for k, v in d.items() if v is not None)

    else:
        return d


def wrap_class(class_name, item, func=None):
    if item is None:
        return item

    elif isinstance(item, class_name):
        return item

    else:
        if func is None:
            func = lambda x: class_name(**x)

        return func(item)


class Hub(object):
    def __init__(self, type, url, **customs):
        self.type = type
        self.url = url
        self.customs = custom_objects(customs.items())

    def _asdict(self):
        return clean_dict(dict(self.customs, \
                               type=self.type, \
                               url=self.url))


class Attachment(object):
    def __init__(self, url, mime_type, title=None, size_in_bytes=None,
                 duration_in_seconds=None, **customs):
        self.url = url
        self.mime_type = mime_type
        self.title = title
        self.size_in_bytes = size_in_bytes
        self.duration_in_seconds = duration_in_seconds
        self.customs = custom_objects(customs.items())

    def _asdict(self):
        return clean_dict(dict(self.customs, \
                               url=self.url, \
                               mime_type=self.mime_type, \
                               title=self.title, \
                               size_in_bytes=self.size_in_bytes, \
                               duration_in_seconds=self.duration_in_seconds))


class Author(object):
    def __init__(self, name=None, url=None, avatar=None, expired=None,
                 hubs=None, **customs):
        if name is None and url is None and avatar is None and expired is None and \
                hubs is None:
            raise ValueError("One of name, url, avatar, expired, or hubs is required")

        self.name = name
        self.url = url
        self.avatar = avatar
        self.expired = expired
        self.hubs = unwrap_list(hubs, lambda h: wrap_class(Hub, h))
        self.customs = custom_objects(customs.items())

    def _asdict(self):
        return clean_dict(dict(self.customs, \
                               name=self.name, \
                               url=self.url, \
                               avatar=self.avatar, \
                               expired=self.expired, \
                               hubs=unwrap_list(self.hubs)))


class Item(object): 
    def __init__(self, id, content_html=None, content_text=None, url=None,
                 external_url=None, title=None, summary=None, image=None,
                 banner_image=None, date_published=None, date_modified=None,
                 tags=None, attachments=None, author=None, **customs):
        self.id = str(id)
        self.content_html = html.unescape(content_html)
        self.content_text = content_text
        self.url = url
        self.external_url = external_url
        self.title = title
        self.summary = summary
        self.image = image
        self.banner_image = banner_image
        self.date_published = date_published
        self.date_modified = date_modified
        self.tags = tags
        self.author = wrap_class(Author, author)
        self.attachments = unwrap_list(attachments, func=lambda a: wrap_class(Attachment, a, lambda x: \
            Attachment(x['url'], x['mime_type'], **filter_keys(x, 'url', 'mime_type'))))
        self.customs = custom_objects(customs.items())

    def _asdict(self):
        return dict(self.customs, \
                    author=self.author._asdict() if self.author else None, \
                    id=self.id, \
                    content_html=self.content_html, \
                    content_text=self.content_text, \
                    url=self.url, \
                    external_url=self.external_url, \
                    title=self.title, \
                    summary=self.summary, \
                    image=self.image, \
                    banner_image=self.banner_image, \
                    date_published=self.date_published, \
                    date_modified=self.date_modified, \
                    tags=self.tags, \
                    attachments=unwrap_list(self.attachments))


class JSONFeed(object):
    def __init__(self, version, title, items, home_page_url=None,
                 feed_url=None, description=None, user_comment=None,
                 next_url=None, icon=None, favicon=None, author=None, expired=None,
                 hubs=None, **customs):
        self.version = version
        self.title = title
        self.items = [wrap_class(Item, i, lambda x: \
            Item(x["id"], **filter_keys(x, "id"))) for i in items]
        self.home_page_url = home_page_url
        self.feed_url = feed_url
        self.description = description
        self.user_comment = user_comment
        self.next_url = next_url
        self.icon = icon
        self.favicon = favicon
        self.author = wrap_class(Author, author)
        self.expired = expired
        self.hubs = unwrap_list(hubs, lambda h: wrap_class(Hub, h))
        self.customs = custom_objects(customs.items())

    def _asdict(self):
        return clean_dict(dict(self.customs, \
                               version=self.version, \
                               title=self.title, \
                               items=[i._asdict() for i in self.items], \
                               home_page_url=self.home_page_url, \
                               feed_url=self.feed_url, \
                               description=self.description, \
                               user_comment=self.user_comment, \
                               next_url=self.next_url, \
                               icon=self.icon, \
                               favicon=self.favicon, \
                               author=self.author._asdict(), \
                               expired=self.expired, \
                               hubs=unwrap_list(self.hubs)))


def _open_resource(url_file_stream_or_string, etag, modified, agent, referrer, handlers, request_headers):
    if hasattr(url_file_stream_or_string, 'read'):
        return url_file_stream_or_string.read().decode("utf8")

    if isinstance(url_file_stream_or_string, str) \
            and urllib.parse.urlparse(url_file_stream_or_string)[0] in ('http', 'https', 'ftp', 'file', 'feed'):
        with urllib.request.urlopen(url_file_stream_or_string) as resp:
            return resp.read().decode("utf8")

    try:
        with open(url_file_stream_or_string, encoding='utf8') as f:
            data = f.read()
    except (IOError, UnicodeEncodeError, TypeError, ValueError):
        pass
    else:
        return data

    if isinstance(url_file_stream_or_string, bytes):
        return url_file_stream_or_string.decode("utf8")

    else:
        return url_file_stream_or_string


def parse(url_file_stream_or_string, etag=None, modified=None, agent=None, referrer=None, handlers=None,
          request_headers=None, response_headers=None, resolve_relative_uris=None, sanitize_html=None):
    if isinstance(url_file_stream_or_string, dict):
        return JSONFeed(url_file_stream_or_string["version"], \
                        url_file_stream_or_string["title"], \
                        url_file_stream_or_string["items"], \
                        **filter_keys(url_file_stream_or_string, "version",
                                      "title", "items"))

    else:
        raw_data = _open_resource(url_file_stream_or_string, etag, modified, agent, referrer, handlers, request_headers)
        json_data = json.loads(raw_data)
        return JSONFeed(json_data["version"], \
                        json_data["title"], \
                        json_data["items"], \
                        **filter_keys(json_data, "version",
                                      "title", "items"))
