import base64


def encode(value):
    return base64.b64decode(value.encode()).decode()


def decode(value):
    return base64.b64encode(value.encode()).decode()
