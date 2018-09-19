import requests
import json
import base64
import os
import math
import time
from PIL import Image
import ybc_config


__BASIC_URL = ybc_config.config['prefix']+ ybc_config.uri
__MERGE_URL = __BASIC_URL + "/faceMerge/base64"
__DECORATATION_URL = __BASIC_URL + "/faceDecoration/base64"


def _resize_img(filepath,max_size=512000):
    # MAX_FILE_SIZE = max_size
    filesize = os.path.getsize(filepath)
    # if filesize > MAX_FILE_SIZE :
    im = Image.open(filepath)
    src_w = im.size[0]
    src_h = im.size[1]
    dst_w = 460
    dst_h = (src_h/src_w) * 460
    dst_size = dst_w , dst_h
    im.thumbnail(dst_size)
    im.save(filepath)
    return filepath


def meizhuang(filename='', meitype='日系妆-芭比粉'):
    '''人脸美妆'''
    cosmetic_type = meizhuang_type()
    cosmetic = cosmetic_type.index(meitype) + 1
    if not filename:
        return -1
    if cosmetic < 1:
        cosmetic = 1
    if cosmetic > 23:
        cosmetic = 23
    filepath = os.path.abspath(filename)
    filepath = _resize_img(filepath)
    url = 'https://www.yuanfudao.com/tutor-ybc-course-api/faceCosmetic.php'
    b64img= base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
    data = {}
    data['b64img'] = b64img
    data['cosmetic'] = cosmetic
    r = requests.post(url, data=data)
    res = r.json()
    if res['ret'] == 0 and res['data']:
        new_file = os.path.splitext(filename)[0] +  '_' + str(int(time.time())) + '_meizhuang' + os.path.splitext(filename)[1]
        with open(new_file,'wb') as f:
            f.write(base64.b64decode(res['data']['image']))
        return new_file
    else:
        return -1


def meizhuang_type(flag=1):
    '''获取美妆类型'''
    MEIZHUANG_TYPE = {
    1:'日系妆-芭比粉',
    2:'日系妆-清透',
    3:'日系妆-烟灰',
    4:'日系妆-自然',
    5:'日系妆-樱花粉',
    6:'日系妆-原宿红',
    7:'韩妆-闪亮',
    8:'韩妆-粉紫',
    9:'韩妆-粉嫩',
    10:'韩妆-自然',
    11:'韩妆-清透',
    12:'韩妆-大地色',
    13:'韩妆-玫瑰',
    14:'裸妆-自然',
    15:'裸妆-清透',
    16:'裸妆-桃粉',
    17:'裸妆-橘粉',
    18:'裸妆-春夏',
    19:'裸妆-秋冬',
    20:'主题妆-经典复古',
    21:'主题妆-性感混血',
    22:'主题妆-炫彩明眸',
    23:'主题妆-紫色魅惑',
    }
    if flag == 1:
        return list(MEIZHUANG_TYPE.values())
    else:
        return MEIZHUANG_TYPE


def bianzhuang(filename='', biantype='灰姑娘妆'):
    """
    功能：人脸美妆。

    参数 filename 是待处理的人脸图片，
    可选参数 biantype 是妆容类型，默认是 灰姑娘妆，
    返回：美妆过的人脸图片。
    """
    decoration_type = bianzhuang_type()
    decoration = decoration_type.index(biantype) + 1

    if not filename:
        return -1
    if decoration < 1:
        decoration = 1
    if decoration > 22:
        decoration = 22

    filepath = os.path.abspath(filename)
    filepath = _resize_img(filepath)

    url = __DECORATATION_URL
    b64img= base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
    data = {}
    data['image'] = b64img
    data['decoration'] = decoration

    headers = {'content-type': "application/json"}

    for i in range(3):
        r = requests.post(url, json=data, headers=headers)
        if r.status_code == 200:
            res = r.json()
            new_file = os.path.splitext(filename)[0] + '_' + str(int(time.time())) + '_bianzhuang' + \
                       os.path.splitext(filename)[1]
            with open(new_file, 'wb') as f:
                f.write(base64.b64decode(res['data']['image']))
            return new_file
        elif i < 2:
            continue
        else:
            raise ConnectionError('人脸美妆失败', r._content)


def bianzhuang_type(flag=1):
    '''获取美妆类型'''
    BIANZHUANG_TYPE = {
    1:'埃及妆',
    2:'巴西土著妆',
    3:'灰姑娘妆',
    4:'恶魔妆',
    5:'武媚娘妆',
    6:'星光薰衣草',
    7:'花千骨',
    8:'僵尸妆',
    9:'爱国妆',
    10:'小胡子妆',
    11:'美羊羊妆',
    12:'火影鸣人妆',
    13:'刀马旦妆',
    14:'泡泡妆',
    15:'桃花妆',
    16:'女皇妆',
    17:'权志龙',
    18:'撩妹妆',
    19:'印第安妆',
    20:'印度妆',
    21:'萌兔妆',
    22:'大圣妆'
    }
    if flag == 1:
        return list(BIANZHUANG_TYPE.values())
    else:
        return BIANZHUANG_TYPE


def ronghe(filename='', rongtype='篮球队长'):
    """
    功能：人脸融合。

    参数 filename 是待处理的人脸图片，
    可选参数 rongtype 是融合类型，默认是 篮球队长，
    返回：融合过的人脸图片。
    """
    if not filename:
        return -1

    model_type = ronghe_type()
    model = model_type.index(rongtype) + 1

    if model < 1:
        model = 1
    if model > 10:
        model = 10

    filepath = os.path.abspath(filename)
    filepath = _resize_img(filepath)
    url = __MERGE_URL

    b64img= base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
    data = {}
    data['image'] = b64img
    data['model'] = model

    headers = {'content-type': "application/json"}

    for i in range(3):
        r = requests.post(url, json=data, headers=headers)
        if r.status_code == 200:
            res = r.json()
            if res['ret'] == '0' and res['img_base64']:
                new_file = os.path.splitext(filename)[0] + '_' + str(int(time.time())) + '_ronghe' + '.png'
                with open(new_file, 'wb') as f:
                    f.write(base64.b64decode(res['img_base64']))
                return _resize_img(new_file)

    raise ConnectionError('人脸融合失败', r._content)


def ronghe_type(flag=1):
    RONGHE_TYPE = {
	1: '篮球队长',
	2: '不羁少年',
	3: '可人儿',
	4: '轻舞飞扬',
	5: '元气女孩',
	6: '优雅公主',
	7: '女神马尾',
	8: '帅气学霸',
	9: '飘逸长发',
	10: '阳光少年'
    }
    if flag == 1:
        return list(RONGHE_TYPE.values())
    else:
        return RONGHE_TYPE


def datoutie(filename='', sticker='NewDay'):
    '''制作大头贴'''
    if not filename:
        return -1
    sticker_type = datoutie_type()
    sticker = sticker_type.index(sticker) + 1
    if sticker < 1:
        sticker = 1
    if sticker > 31:
        sticker = 31
    url = 'https://www.yuanfudao.com/tutor-ybc-course-api/faceSticker.php'
    filepath = os.path.abspath(filename)
    b64img= base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
    data = {}
    data['b64img'] = b64img
    data['sticker'] = sticker
    r = requests.post(url, data=data)
    res = r.json()
    if res['ret'] == 0 and res['data']:
        new_file = os.path.splitext(filename)[0] + '_' + str(int(time.time())) + '_datoutie'+os.path.splitext(filename)[1]
        with open(new_file,'wb') as f:
            f.write(base64.b64decode(res['data']['image']))
        return new_file
    else:
        return -1


def datoutie_type(flag=1):
    '''返回大头贴背景类型'''
    STICKER_TYPE = {
    1:	'NewDay',
    2:	'欢乐球吃球1:',
    3:	'Bonvoyage',
    4:	'Enjoy',
    5:	'ChickenSpring',
    6:	'ChristmasShow',
    7:	'ChristmasSnow',
    8:	'CircleCat',
    9:	'CircleMouse',
    10:	'CirclePig',
    11:	'Comicmn',
    12:	'CuteBaby',
    13:	'Envolope',
    14:	'Fairytale',
    15:	'GoodNight',
    16:	'HalloweenNight',
    17:	'LovelyDay',
    18:	'Newyear2017',
    19:	'PinkSunny',
    20:	'KIRAKIRA',
    21:	'欢乐球吃球2:',
    22:	'SnowWhite',
    23:	'SuperStar',
    24:	'WonderfulWork',
    25:	'Cold',
    26:	'狼人杀守卫',
    27:	'狼人杀猎人',
    28:	'狼人杀预言家',
    29:	'狼人杀村民',
    30:	'狼人杀女巫',
    31:	'狼人杀狼人'
    }
    if flag == 1:
        return list(STICKER_TYPE.values())
    else:
        return STICKER_TYPE


def main():
    # res = meizhuang('1.jpg','日系妆-烟灰')
    # print(res)
    # res = bianzhuang('1.jpg')
    # print(res)
    # res = ronghe('1.jpg')
    # print(res)
    # bianzhuang('test.jpg')
    ronghe('test.jpg')


if __name__ == '__main__':
    main()
