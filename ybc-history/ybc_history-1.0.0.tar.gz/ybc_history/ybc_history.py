import json
import urllib.request
import urllib.parse
import random


APPKEY = 'ff7107aa6c5a0b300f34fe4e50d7fce0'
URL = 'http://api.juheapi.com/japi/toh'

def history_info(month, day, number = 3):
    params = {
        "key" : APPKEY,
        "v" : "1.0",
        "month" : month,
        "day" : day
    }
    params = urllib.parse.urlencode(params)
    result = urllib.request.urlopen("%s?%s" % (URL, params))

    res = json.loads(result.read())
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            length = len(res['result'])
            if number < 1:
                number = 1
            elif number > length:
                number = length
            index = set()
            while len(index) != number:
                index.add(random.randint(0,length - 1))
            info = ''
            for i in index:
                info += res['result'][i]['des'] + '\n'
            return info
        else:
            return "请求暂时失败"
    else:
        return "请求暂时失败"

def main():
    result = history_info(9,19)
    print(result)

if __name__ == '__main__':
    main()
