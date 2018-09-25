#/usr/bin/env python
#coding=utf8

# import httplib
import hashlib
import urllib
import urllib.request
import random
import json
import base64

# 您的应用ID
appKey = "3e2dffe9f59171fd"
# 您的应用密钥，请勿把它和appKey泄露给他人
appSecret = "xWKO71qi6wCsBJtHYzwmyQfAgBrifBup"


httpClient = None


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of str

def pic_trans(pic='en.jpeg',_from='en',_to='zh-CHS'):

    try:

        # 参数部分
        f=open(pic,'rb') #二进制方式打开图文件
        q=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
        f.close()
        q = to_str(q)
        # 源语言
        fromLan = _from
        # 目标语言
        to = _to
        # 上传类型
        type = "1"
        # 随机数，自己随机生成，建议时间戳
        salt = random.randint(1, 65536)
        # 签名
        sign = appKey+q+str(salt)+appSecret
        m1 = hashlib.md5()
        m1.update(sign.encode("utf8"))
        sign = m1.hexdigest()
        data = {'appKey':appKey,'q':q,'from':fromLan,'to':to,'type':type,'salt':str(salt),'sign':sign}
        data = urllib.parse.urlencode(data).encode(encoding='UTF8')
        req = urllib.request.Request('http://openapi.youdao.com/ocrtransapi',data)

        #response是HTTPResponse对象
        response = urllib.request.urlopen(req)
        page = response.read()
        ddict = json.loads(page)

        # ddict = {'orientation': 'Up', 'lanFrom': 'en', 'textAngle': '2.748088', 'errorCode': '0', 'lanTo': 'zh-CHS', 'resRegions': [{'boundingBox': '160,163,250,80', 'linesCount': 2, 'lineheight': 26, 'context': 'PRODUCT: Aloe Vera DIRECTIONS:', 'linespace': 20, 'tranContent': '产品:芦荟精华素'}, {'boundingBox': '170,246,474,130', 'linesCount': 3, 'lineheight': 28, 'context': 'As a dietary suppement take as follows take one capsule, two times per day with aglass of water', 'linespace': 15, 'tranContent': '每日两次，每次一粒，每次一杯水'}, {'boundingBox': '180,376,448,107', 'linesCount': 3, 'lineheight': 28, 'context': 'Storage:store of room temperature dry place,Keep out of direct sunlight. Tightty closed keep out of reach of children.', 'linespace': 0, 'tranContent': '贮存:常温干燥处存放，避免阳光直射。紧绷着，孩子们够不着。'}, {'boundingBox': '194,482,375,42', 'linesCount': 1, 'lineheight': 28, 'context': 'Do not use if safety seal is broken', 'tranContent': '如果安全密封坏了，不要使用'}, {'boundingBox': '195,536,260,51', 'linesCount': 1, 'lineheight': 28, 'context': 'MFG Date: on the bottle', 'tranContent': '生产日期:在瓶子上'}, {'boundingBox': '200,586,120,40', 'linesCount': 1, 'lineheight': 28, 'context': 'EXP: 3years', 'tranContent': '经验:3年'}, {'boundingBox': '204,626,377,80', 'linesCount': 2, 'lineheight': 28, 'context': 'NO ARTIFICIAL FLAVORS. NO SALT NO SUGAR.NO PRESERVATIVES', 'linespace': 0, 'tranContent': '没有人工香料。没有盐就没有糖。没有防腐剂'}, {'boundingBox': '630,633,23,16', 'linesCount': 1, 'lineheight': 12, 'context': 's', 'tranContent': '年代', 'dir': 'v'}, {'boundingBox': '223,726,15,35', 'linesCount': 1, 'lineheight': 28, 'context': '、', 'tranContent': ',', 'dir': 'h'}, {'boundingBox': '306,743,217,66', 'linesCount': 4, 'lineheight': 12, 'context': 'CMA ea … e )', 'linespace': 0, 'tranContent': 'CMA ea…'}]}

        resRegions = ddict['resRegions']
        res_str = ''
        for i in range(0, len(resRegions)):
            # print (ddict['resRegions'][i]['context']+'\n'+ddict['resRegions'][i]['tranContent'])
            res_str = res_str + str(ddict['resRegions'][i]['tranContent']) + '\n'
        return res_str

    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()

def en_pic(pic,_from='en',_to='zh-CHS'):
    res_str = pic_trans(pic,_from,_to)
    return res_str

def ja_pic(pic,_from='ja',_to='zh-CHS'):
    res_str = pic_trans(pic,_from,_to)    
    return res_str

def main():
    pic_trans('ja.jpeg','ja')

if __name__ == '__main__':
    main()
