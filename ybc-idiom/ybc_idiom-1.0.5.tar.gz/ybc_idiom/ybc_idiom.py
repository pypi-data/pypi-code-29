import json
import requests


def meaning(keyword=''):
    if keyword == '':
        return -1
    url='http://v.juhe.cn/chengyu/query'
    appkey = '1475e669bd7d988dd432bcb29d9d0399'
    data = {}
    data['word'] = keyword
    data['key'] = appkey
    data['dtype'] = 'json'
    r = requests.post(url, data=data)
    res = r.json()['result']
    if res:
        return {
            '名称':keyword,
            '读音':res['pinyin'],
            '解释':res['chengyujs'],
            '出自':res['from_'],
            '近义词':'无' if res['tongyi'] == None else ','.join(res['tongyi']),
            '反义词':'无' if res['fanyi'] == None else ','.join(res['fanyi']),
            '举例': '无' if res['example'] == None else res['example'].replace(' ','')
        }
    else:
        return -1

# def meaning1(keyword=''):
#     if keyword == '':
#         return -1
#     url='https://www.yuanfudao.com/tutor-ybc-course-api/jisu_idiom.php'
#     data = {}
#     data['keyword'] = keyword
#     data['op'] = 'meaning'
#     r = requests.post(url, data=data)
#     res = r.json()['result']
#     if res:
#         return {
#             'name':res['name'],
#             'duyin':res['pronounce'],
#             'jieshi':res['content'],
#             'chuzi':res['comefrom'],
#             'jinyici':','.join(res['thesaurus']) if len(res['thesaurus'])>1 else ''.join(res['thesaurus']),
#             'fanyici':','.join(res['antonym']) if len(res['antonym'])>1 else ''.join(res['antonym']),
#             'lizi':res['example'].replace(' ','')
#         }
#     else:
#         return 0

def search(keyword=''):
    if keyword == '':
        return -1
    url='http://api.tianapi.com/txapi/chengyu/?key=5982c93dd1e569c8eef7397a6aec86c5&mode=1&num=10&word=' + keyword
    r = requests.get(url)
    res = r.json()['newslist']
    if res:
        search_info = []
        for item in res:
            search_info.append(item['chengyu'])
        return search_info
    else:
        return -1

def main():
    # print(meaning('叶公好龙'))
    print(search('一'))


if __name__ == '__main__':
    main()
