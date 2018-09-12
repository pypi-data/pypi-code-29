# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pprint
import warnings

from .helpers import use_appropriate_encoding


class Channel:
    CHANNEL_ATTRIBUTES = ("name", "description", "created", "modified",
                          "iden", "tag", "image_url", "website_url")

    def __init__(self, account, channel_info):
        self._account = account
        self.channel_info = channel_info
        self.channel_tag = channel_info.get("tag")

        # for attr in ("name", "description", "created", "modified",
        #              "iden", "tag", "image_url", "website_url"):
        #     setattr(self, attr, channel_info.get(attr))
        for attr in self.CHANNEL_ATTRIBUTES:
            setattr(self, attr, channel_info.get(attr))

    def push_note(self, title, body):
        data = {"type": "note", "title": title, "body": body}
        return self._push(data)

    def push_address(self, name, address):
        warnings.warn("Address push type is removed. This push will be sent as note.")
        return self.push_note(name, address)

    def push_list(self, title, items):
        warnings.warn("List push type is removed. This push will be sent as note.")
        return self.push_note(title, ",".join(items))

    def push_link(self, title, url, body=None):
        data = {"type": "link", "title": title, "url": url, "body": body}
        return self._push(data)

    def push_file(self, file_name, file_url, file_type, body=None, title=None):
        return self._account.push_file(file_name, file_url, file_type, body=body, title=title, channel=self)

    def _push(self, data):
        data["channel_tag"] = self.channel_tag
        return self._account._push(data)

    @use_appropriate_encoding
    def __str__(self):
        _str = "Channel('{}', tag: '{}')".format(self.name or "nameless (iden: {})"
                                               .format(self.iden), self.channel_tag)
        return _str

    def __repr__(self):
        attr_map = {k: self.__getattribute__(k) for k in self.CHANNEL_ATTRIBUTES}
        attr_str = pprint.pformat(attr_map)

        _str = "Channel('{}', tag: '{}'".format(self.name or "nameless (iden: {})"
                                               .format(self.iden), self.channel_tag)

        _str  += ",\n{})".format(attr_str)
        return _str

    # @property
    # def name(self):
    #     return getattr(self, "name")
    #
    # @property
    # def description(self):
    #     return getattr(self, "description")
    #
    # @property
    # def created(self):
    #     return getattr(self, "created")
    #
    # @property
    # def modified(self):
    #     return getattr(self, "modified")
