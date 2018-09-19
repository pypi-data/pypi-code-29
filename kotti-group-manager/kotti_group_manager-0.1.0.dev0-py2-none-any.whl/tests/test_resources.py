# -*- coding: utf-8 -*-

"""
Created on 2018-09-19
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from pytest import raises


def test_model(root, db_session):
    from kotti_group_manager.resources import GroupPage

    cc = GroupPage()
    assert cc.custom_attribute is None

    cc = GroupPage(custom_attribute=u'Foo')
    assert cc.custom_attribute == u'Foo'

    root['cc'] = cc = GroupPage()
    assert cc.name == 'cc'

    with raises(TypeError):
        cc = GroupPage(doesnotexist=u'Foo')
