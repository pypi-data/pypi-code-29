#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             zone.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       09/15/2018
#

"""
clouddns.zone
~~~~~~~~~~~~~

This module contains API wrapper functions for listing, creating, updating,
and deleting zones.
"""

from __future__ import absolute_import

from .api import api, get_auth_params, ValidationError
from requests import get, post


def list(page = 1, rows_per_page = 30, search = ''):
    """Returns a paginated list of zones

    :param page: (optional) int, current page
    :param rows_per_page: (optional) int, number of results on each page
    :param search: (optional) string used to search domain names, reverse zone
        name, or other keyword to search for in the zone names
    """
    url = 'https://api.cloudns.net/dns/list-zones.json'

    params = get_auth_params()

    params['page'] = page
    params['rows-per-page'] = rows_per_page
    if search:
        params['search'] = search

    return get(url, params=params)


# TODO: Think about combining this with listing. When do you not want to know
# the count? or is that a waste of calls?
def get_page_count(rows_per_page = 30, search = ''):
    """Returns the number of pages for the full listing or search listing

    :param rows_per_page: int, number of results on each page
    :param search: (optional) string used to search domain names, reverse zone
        name, or other keyword to search for in the zone names
    """
    url = 'https://api.cloudns.net/dns/get-pages-count.json'

    params = get_auth_params()

    params['rows-per-page'] = rows_per_page
    if search:
        params['search'] = search

    return get(url, params=params)


def create():
    """Creates a new zone.

    :param page: (optional) int, current page
    :param rows_per_page: (optional) int, number of results on each page
    :param search: (optional) string used to search domain names, reverse zone
        name, or other keyword to search for in the zone names
    """
    url = 'https://api.cloudns.net/dns/register.json'

    params = get_auth_params()

    params['page'] = page
    params['rows-per-page'] = rows_per_page
    if search:
        params['search'] = search

    return get(url, params=params)
