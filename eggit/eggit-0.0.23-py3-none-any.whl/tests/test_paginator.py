from eggit.paginator import Paginator


def test_paginator():
    page = Paginator(1, 1, None, 0, 5)
    json = page.get_dict()
    assert json['page'] == 1
    assert json['pages'] == 1
    assert json['items'] is None
    assert json['total'] == 0
    assert json['per_page'] == 5
