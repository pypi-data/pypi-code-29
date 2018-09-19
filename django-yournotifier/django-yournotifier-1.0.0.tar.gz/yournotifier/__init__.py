# coding: utf-8
import json

import requests
from django.conf import settings


URL = 'https://yournotifier.com/api/v1/message/'


def send_notify(channel_name, text):
    headers = {'Authorization': 'Key {}'.format(settings.NOTIFIER_APIKEY)}
    res = requests.post(URL, headers=headers, data={'name': channel_name, 'text': text})
    return res.json()
