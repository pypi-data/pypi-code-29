import zlib
import base64


def compress(data):
    return base64.b64encode(zlib.compress(data.encode('utf-8'))).decode()


def decompress(data):
    return zlib.decompress(base64.b64decode(data.encode())).decode('utf-8')
