import requests
import json
import base64
import os
import time
from PIL import Image
import ybc_config


__BASIC_URL = ybc_config.config['prefix']+ ybc_config.uri
__FACE_URL = __BASIC_URL + '/faceDetect'
__MERGE_URL = __BASIC_URL + "/faceMerge/base64"


__MAC_SIZE = 512000
__MODE = 1


def _resize_img(filepath, max_size = 512000):
    filesize = os.path.getsize(filepath)
    im = Image.open(filepath)
    src_w = im.size[0]
    src_h = im.size[1]
    dst_w = 500
    dst_h = (src_h/src_w) * 500
    dst_size = dst_w , dst_h
    im.thumbnail(dst_size)
    im.save(filepath)
    return filepath


def _getInfo(filename='', mode=__MODE):
    if not filename:
        return -1

    url = __FACE_URL
    filepath = os.path.abspath(filename)
    filepath = _resize_img(filepath)

    data = {
        'mode': mode
    }
    files = {
        'file': open(filepath, 'rb')
    }

    for i in range(3):
        r = requests.post(url, data=data, files=files)

        if r.status_code == 200:
            res = r.json()
            if res['code'] == 0 and res['data']:
                res = res['data']['face'][0]
                res_dict = {
                    'age':res['age'],
                    'gender':res['gender'],
                    'beauty':res['beauty'],
                    'glass':res['glass']
                }
                return res_dict

    raise ConnectionError('获取人脸信息失败', r._content)


def gender1(filename=''):
    """
    功能：识别人脸图片的性别信息。

    参数 filename 是待识别的人脸图片，

    返回：图片中人脸的性别信息[0(女性)~100(男性)]。
    """
    if not filename:
        return -1
    res = _getInfo(filename)
    if res == -1:
        return '图片中找不到人哦~'
    return res['gender']


def gender(filename=''):
    """
    功能：识别人脸图片的性别。

    参数 filename 是待识别的人脸图片，

    返回：图片中人脸的性别。
    """
    if not filename:
        return -1
    res = _getInfo(filename)
    if res == -1:
        return '图片中找不到人哦~'
    return '男' if res['gender'] > 90 else '女'


def age(filename=''):
    """
    功能：识别人脸图片的年龄信息。

    参数 filename 是待识别的人脸图片，

    返回：图片中人脸的年龄信息[0~100]。
    """
    if not filename:
        return -1
    res = _getInfo(filename)
    if res == -1:
        return '图片中找不到人哦~'
    return res['age']


def glass1(filename=''):
    """
    功能：识别人脸图片的是否戴眼镜。

    参数 filename 是待识别的人脸图片，

    返回：图片中人脸的是否戴眼镜 [true,false]。
    """
    if not filename:
        return -1
    res = _getInfo(filename)
    if res == -1:
        return '图片中找不到人哦~'
    return bool(res['glass'])


def glass(filename=''):
    """
    功能：识别人脸图片的是否戴眼镜。

    参数 filename 是待识别的人脸图片，

    返回：图片中人脸的是否戴眼镜。
    """
    if not filename:
        return -1
    res = _getInfo(filename)
    if res == -1:
        return '图片中找不到人哦~'
    return res['glass']


def beauty(filename=''):
    """
    功能：识别人脸图片的魅力值。

    参数 filename 是待识别的人脸图片，

    返回：图片中人脸的魅力值 [0~100]。
    """
    if not filename:
        return -1
    res = _getInfo(filename)
    if res == -1:
        return '图片中找不到人哦~'
    return res['beauty']


def info(filename='', mode=__MODE):
    """
    功能：识别图片中一张人脸信息。

    参数 filename 是待识别的人脸图片，

    可选参数 mode 是识别模式，1 代表最大人脸，0 代表所有人脸，默认为 1

    返回：识别出的人脸信息。
    """
    if not filename:
        return -1

    res_dict = _getInfo(filename, mode)

    gender = '男性' if res_dict['gender'] >= 50 else '女性'
    glass = '戴' if res_dict['glass'] else '不戴'
    res_str = '{gender}，{age}岁左右，{glass}眼镜，颜值打分：{beauty}分'.format(gender=gender, age=res_dict['age'], glass=glass, beauty=res_dict['beauty'])
    return res_str


def info_all(filename='', mode=0):
    '''返回图片中所有人脸信息'''

    if not filename:
        return -1
    url = 'https://www.yuanfudao.com/tutor-ybc-course-api/faceInfo.php'
    filepath = os.path.abspath(filename)
    b64img= base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
    data = {}
    data['b64img'] = b64img
    data['mode'] = mode
    r = requests.post(url, data=data)
    res = r.json()
    if res['ret'] == 0 and res['data']:
        res = res['data']['face_list']
        res_str = '图片中总共发现{face_len}张人脸：'.format(face_len=len(res))+os.linesep
        i = 1
        for val in res :
            gender =  '男性' if val['gender'] >= 50 else '女性'
            glass = '戴' if val['glass'] else '不戴'
            res_str += '第{i}个人脸信息：{gender}，{age}岁左右，{glass}眼镜，颜值打分：{beauty}分'.format(gender=gender, age=val['age'], glass=glass, beauty=val['beauty'], i=i)
            res_str += os.linesep
            i += 1
        return res_str
    else:
        return '图片中找不到人哦~'


def ps(filename='', decoration=21):
    '''变装'''

    if not filename:
        return -1
    if decoration < 1:
        decoration = 1
    if decoration > 22:
        decoration = 22
    filepath = os.path.abspath(filename)
    filepath = _resize_img(filepath)
    url = 'https://www.yuanfudao.com/tutor-ybc-course-api/faceDecoration.php'

    b64img= base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
    data = {}
    data['b64img'] = b64img
    data['decoration'] = decoration
    r = requests.post(url, data=data)
    res = r.json()
    if res['ret'] == 0 and res['data']:
        new_file = os.path.splitext(filename)[0] + '_' + str(int(time.time())) +'.'+os.path.splitext(filename)[1]
        with open(new_file,'wb') as f:
            f.write(base64.b64decode(res['data']['image']))
        return new_file
    else:
        return -1


def mofa(filename='', model=1):
    '''人脸融合'''

    if not filename:
        return -1


    filepath = os.path.abspath(filename)
    filepath = _resize_img(filepath)
    url = __MERGE_URL

    b64img = base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
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


def main():
    # pass
    # import ybc_box as box
    print(_getInfo('test.jpg'))
    print(info('test.jpg'))
    # filename = camera()
    # res = age(filename)
    # print(res)
    # res = gender(filename)
    # print(res)
    # res = glass(filename)
    # print(res)
    # res = beauty(filename)
    # print(res)
    # res = info('2.jpg')
    # print(res)
    # res = info_all('3.jpg')
    # print(res)
    # res = age('5.jpg')
    # print(res)
    # res = gender('5.jpg')
    # print(res)
    # res = glass('5.jpg')
    # print(res)
    # res = beauty('5.jpg')
    # print(res)


if __name__ == '__main__':
    main()
