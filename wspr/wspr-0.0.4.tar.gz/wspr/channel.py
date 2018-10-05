# -*- coding: utf-8 -*-

from wspr.protocol.mumble_pb2 import ChannelState


class Channel:
    """"""

    def __init__(self):
        """"""
        self.channel_id = None
        self.parent = None
        self.name = None
        self.links = None
        self.description = None
        self.links_add = None
        self.links_remove = None
        self.temporary = None
        self.position = None
        self.description_hash = None
        self.max_users = None

    def update(self, data: ChannelState) -> None:
        """Update channel."""
        # Don't override existing values if the update message doesn't contain them
        for field, value in data.ListFields():
            setattr(self, field.name, value)

    def __repr__(self) -> str:
        """"""
        return 'name={}'.format(self.name)
