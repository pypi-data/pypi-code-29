import base64


def base64_decode(value):
    return base64.b64decode(value.encode()).decode()


def base64_encode(value):
    return base64.b64encode(value.encode()).decode()
