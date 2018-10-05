# -*- coding: utf-8 -*-

import logging
import struct

from wspr.protocol.mumble_pb2 import RequestBlob
from wspr.protocol.packet_type import PacketType


class Blob:
    """A binary large object, also known as blob. Keeps data."""

    def __init__(self):
        """"""
        self._logger = logging.getLogger('whisper')

    def request(self, item_hash, connection):
        """Request the user's comment."""
        # We already have this information
        # if comment_hash in self.blobs:
        #     return
        request_packet = RequestBlob()
        request_packet.session_comment.extend(struct.unpack("!5I", item_hash))
        connection.send_message(PacketType.REQUESTBLOB, request_packet)
