import requests
import json


def chat(question=''):
    if question == '':
        return -1
    key = 'df9ce298374045beab51bbd3d3e03601'
    url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + question
    r = requests.get(url)
    res = r.json()
    if res['text']:
        res_dict = {'content':res['text']}
        return res_dict
    else:
        return -1

def main() :
    print(chat('你好呀,你叫什么名字'))

if __name__ == '__main__':
    main()
