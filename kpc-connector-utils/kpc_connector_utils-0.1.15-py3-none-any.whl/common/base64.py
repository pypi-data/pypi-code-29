import base64


def decode(value):
    return base64.b64decode(value.encode()).decode()


def encode(value):
    return base64.b64encode(value.encode()).decode()
