# -*- coding: utf-8 -*-

"""
Created on 2018-09-19
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from pytest import fixture


@fixture
def dummy_content(root):

    from kotti_group_manager.resources import GroupPage

    root['cc'] = cc = GroupPage(
        title=u'My content',
        description=u'My very custom content is custom',
        custom_attribute='Lorem ipsum'
    )

    return cc


def test_view(dummy_content, dummy_request):

    from kotti_group_manager.views.view import GroupPageViews

    views = GroupPageViews(dummy_content, dummy_request)

    default = views.default_view()
    assert 'foo' in default

    alternative = views.alternative_view()
    assert alternative['foo'] == u'bar'
