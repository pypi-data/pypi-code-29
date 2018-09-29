from Reserver.utils import package, unpackage
import requests
import json

class CallbackToLogin:
    def __init__(self, url, file_path):
        self._path = file_path
        self._url = url

    def __call__(self):
        pass


def send_ding_img(token, content,img='', title='no title', *at_mobiles):
    msg = {
        "msgtype": "markdown",
        "markdown": {
            "title":'login !',
            "text":"#%s\n>%s\n![screenshot](data:image/png;base64,%s) " % (title, content,img),
        },
        "at": {
            "atMobiles": list(at_mobiles), 
            "isAtAll": False
        }
    }
    res = requests.post("https://oapi.dingtalk.com/robot/send?access_token=%s" % token,
        headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps(msg))

    if res.status_code == 200:
        return True, res.json()
    return False, None