import requests

CaptureMode = False
DebugBackDoor = False


def commonGet(url, headers=None, cookies=None, **kwargs):
    req = requests.get(url=url, headers=headers, cookies=cookies, **kwargs)
    return req


def commonPost(url, headers=None, cookies=None, data=None, **kwargs):
    req = requests.post(url=url, headers=headers, cookies=cookies, data=data, **kwargs)
    return req
