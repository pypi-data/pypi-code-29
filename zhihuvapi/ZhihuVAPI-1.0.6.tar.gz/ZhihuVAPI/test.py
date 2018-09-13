
from .util import zhihu
people = zhihu.json('https://api.zhihu.com/people/iCheez')
answers = zhihu.json('https://www.zhihu.com/api/v4/answers/457809435')
article = zhihu.json('https://api.zhihu.com/article/41352232')
collections = zhihu.json('https://api.zhihu.com/collections/23622858')
columns = zhihu.json(
    'https://api.zhihu.com/columns/PoliticalInaccuracy?include=%24.intro')


# def compare(o1: dict, o2: dict):
#     for k, v in o1.items():
#         if k in o2:
#             print(f'        两者都存在 {k}')


# print('比较people, columns')
# compare(people, columns)
# print('比较people, collections')
# compare(people, collections)
# print('比较collections, columns')
# compare(collections, columns)
# print('比较answers, collections')
# compare(answers, collections)
# print('比较collections, columns')
# compare(collections, columns)
# print('比较collections, answers')
# compare(collections, answers)


def compare(base, *arg):
    arr = []
    for k in base:
        for o in arg:
            if k not in o:
                break
        else:
            # print(f'        都存在 {k}')
            arr.append(k)
    print(arr)


content = ['author', 'excerpt', 'admin_closed_comment', 'id', 'voteup_count',
           'can_comment', 'url', 'comment_permission', 'comment_count', 'type', 'suggest_edit']
container = ['description', 'url', 'title', 'type', 'id']
# compare(answers, article)


def no(o1, o2):
    arr = []
    for k in o1:
        if k not in o2:
            arr.append(k)
            # print(f'self.{k}=None')
    print(arr)


# no(answers, content)
# print(answers.get('author'))
# def catch_exception(origin_func):
#     def wrapper(self, *args, **kwargs):
#         self.tt()
#         origin_func(self)
#     return wrapper


# class ClassName(object):
#     """docstring for ClassName"""

#     def __init__(self):
#         pass

#     @catch_exception
#     def aa(self):
#         print('aa')

#     def tt(self):
#         print('tt')


# ClassName().aa()
