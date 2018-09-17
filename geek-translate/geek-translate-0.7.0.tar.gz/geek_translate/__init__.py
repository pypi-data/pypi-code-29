import json
import string

import requests
import pinyin
import html


def sogou_translate(text, target='en', from_target='zh-CHS'):
    if type(text) is list:
        text = [sogou_translate(i).strip(string.punctuation) for i in text]
        return text
    sogou_api_url = "http://snapshot.sogoucdn.com/engtranslate"
    data = {'from_lang': from_target, 'to_lang': target,
            'trans_frag': [{'text': text}]}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url=sogou_api_url, headers=headers, data=json.dumps(data))
    json_response = response.json()
    if json_response.get('status', 0) < 0:
        raise Exception(json_response.get('error_string'))
    text = html.unescape(json_response['trans_result'][0]['trans_text'])
    return text.strip(string.punctuation)


def translate_company(texts):
    if isinstance(texts, str):
        if texts == 'None':
            return ""
        else:
            text_list = [string.capwords(pinyin.get(text,
                         format='strip', delimiter='')) for text in texts]
            return ''.join(text_list)
    else:
        return '类型不对'


if __name__ == '__main__':
    pass
