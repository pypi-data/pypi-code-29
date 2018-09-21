#-*- coding:utf-8 -*-
"""
Test the get rpc method
"""
#pylint:disable=wildcard-import,unused-wildcard-import,redefined-outer-name
import json
from .fixtures import *

def test_detail_default(buildb1):
    """
    Test the detail method : must succeed.
    """
    entries = cuisson.service.Cuisson().detail('buildb1owner', buildb1)
    assert len(entries['results']) == 8

def test_detail_no_uid(buildb1):
    """
    Test with a wrong uid : return an empty list.
    """
    entries = cuisson.service.Cuisson().detail('buildb1owner', 'toto')
    assert len(entries['results']) == 0

def test_detail_no_owner(buildb1):
    """
    Test with a wrong owner : return an empty list.
    """
    entries = cuisson.service.Cuisson().detail('toto', buildb1)
    assert len(entries['results']) == 0
