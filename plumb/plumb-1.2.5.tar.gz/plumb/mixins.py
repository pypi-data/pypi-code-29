import base64
import json
import zlib


class CompressionMixin:
    """Mixin to provide compression/decompression capablities."""

    DEFAULT_ENCODING = 'utf-8'

    def compress(self, message):
        return self._b64compress(message)

    def decompress(self, message):
        try:
            # There may be uncompressed messages in the queue
            json.loads(message)
            return message
        except json.decoder.JSONDecodeError:
            return self._b64decompress(message)

    def _b64compress(self, message):
        ''' Returns a base64-encoded string after compression.
            We always return a string, since SNS does not accept bytes. '''
        return base64.b64encode(zlib.compress(bytes(message, self.DEFAULT_ENCODING))).decode(
            self.DEFAULT_ENCODING)

    def _b64decompress(self, message):
        return zlib.decompress(base64.b64decode(message)).decode(self.DEFAULT_ENCODING)


