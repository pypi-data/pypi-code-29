import json
import requests


def detail(tel=''):
    '''电话号详情juhe'''
    if tel == '':
        return -1
    url='https://www.yuanfudao.com/tutor-ybc-course-api/juhe_tel.php'
    data = {}
    data['phone'] = tel
    r = requests.post(url, data=data)
    res = r.json()['result']
    if res:
        res_info = {}
        res_info['province'] = res['province']
        res_info['city'] = res['city']
        res_info['company'] = res['company']
        res_info['shouji'] = tel
        return res_info
    else:
        return -1

def __detail(tel=''):
    '''电话号详情-jisu'''
    if tel == '':
        return -1
    url='https://www.yuanfudao.com/tutor-ybc-course-api/jisu_tel.php'
    data = {}
    data['shouji'] = tel
    r = requests.post(url, data=data)
    res = r.json()['result']
    if res:
        res_info = {}
        res_info['province'] = res['province']
        res_info['city'] = res['city']
        res_info['company'] = res['company']
        res_info['phone'] = res['shouji']
        return res_info
    else:
        return -1

def main():
    print(detail('18635579617'))

if __name__ == '__main__':
    main()
