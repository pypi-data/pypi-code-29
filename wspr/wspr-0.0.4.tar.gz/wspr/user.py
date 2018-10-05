# -*- coding: utf-8 -*-

from wspr.protocol.mumble_pb2 import UserState


class User:
    """"""

    def __init__(self):
        """"""
        self.session = None
        self.actor = None
        self.name = None
        self.user_id = None
        self.channel_id = None
        self.mute = None
        self.deaf = None
        self.suppress = None
        self.self_mute = None
        self.self_deaf = None
        self.texture = None
        self.plugin_context = None
        self.plugin_identity = None
        self.comment = None
        self.texture_hash = None
        self.priority_speaker = None
        self.recording = None

    def update(self, data: UserState) -> None:
        """Update user state."""
        # Don't override existing values if the update message doesn't contain them
        for field, value in data.ListFields():
            setattr(self, field.name, value)

    def __repr__(self) -> str:
        """"""
        return 'name={}'.format(self.name)
