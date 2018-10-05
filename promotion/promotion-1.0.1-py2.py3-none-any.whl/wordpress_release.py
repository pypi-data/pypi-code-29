#-*- coding:utf-8 -*-

"""
http://xiaohost.com/1802.html
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts, taxonomies
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

__author__ = "TANG BIN <bintang.hit@gmail.com>"
__date__ = "24 Sep 2018"


__all__ = [
    'release_post',
]


def release_post(host, user, passwd, title, content,
                 post_tag=[], category=[], status='publish'):
    """ 发布WordPress文章

    Args:
        host: wordpress站点域名
        user: wordpress站点管理员用户名
        passwd: wordpress站点管理员密码
        title: 文章标题
        content: 文章正文
        post_tag: 文章所属标签，没有则自动创建
        category: 文章所属分类，没有则自动创建
        status: 文章状态，不写默认是草稿，private表示私密，draft表示草稿，publish表示发布

    Returns:
        文章id
    """
    client = Client('https://%s/xmlrpc.php' % host, user, passwd)

    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = status

    post.terms_names = {
        'post_tag': post_tag,
        'category': category
    }

    """post.custom_fields = []   #自定义字段列表
    post.custom_fields.append({  #添加一个自定义字段
        'key': 'price',
        'value': 3
    })
    post.custom_fields.append({ #添加第二个自定义字段
        'key': 'ok',
        'value': '天涯海角'
    })"""
    post.id = client.call(posts.NewPost(post))

    return post.id


if __name__ == '__main__':
    host = 'www.cmxdk.com'
    user = 'cmxdk'
    passwd = 'wm-1809'
    title = 'test'
    content = 'test'
    post_tag = ['sunglasses']
    category = ['fashion']
    release_post(host, user, passwd, title, content, post_tag, category)
