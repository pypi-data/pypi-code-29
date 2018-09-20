#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:             record.py
# author:           Harold Bradley III
# email:            harold@bradleystudio.net
# created on:       09/15/2018
#

"""
clouddns.record
~~~~~~~~~~~~~~~

This module contains API wrapper functions for DNS listing, creating, updating,
and deleting records.

There are also a functions for activating/deactivating a record, importing
records, copying existing records

For SOA records, see soa.py
"""

from .api import api, get_auth_params, RECORD_TYPES, ValidationError
from requests import get, post


def list(domain_name, host = '', record_type = ''):
    """Lists DNS records for a particular domain.

    :param domain_name: string, the domain name for which to retrieve the
        records
    :param host: (optional) string, a host to limit results by. Use '@' for
        domain as host.
    :param record_type: (optional) string, the record type to retrieve (ie,
        'a', 'cname', etc..., See RECORD_TYPES)
    """

    url = 'https://api.cloudns.net/dns/records.json'

    params = get_auth_params()

    params['domain-name'] = domain_name
    if host:
        params['host'] = host
    if record_type:
        params['type'] = record_type

    return get(url, params=params)


def create(domain_name, record_type, host, record, ttl, priority = None,
            weight = None, port = None, frame = None, frame_title = '',
            frame_keywords = '', frame_description = '', save_path = None,
            redirect_type = None, mail = None, txt = None, algorithm = None,
            fptype = None, status = 1, geodns_location = None,
            caa_flag = None, caa_type = '', caa_value = ''):
    """Creates a DNS record.

    :param domain_name: string, the domain name for which to retrieve the
        records
    :param record_type: string, the record type to retrieve (ie,
        'a', 'cname', etc..., See RECORD_TYPES)
    :param host: string, the host for this record. Use '@' for domain as host.
    :param record: string, the record to be added
    :param ttl: int, the time-to-live for this record
    :param priority: (optional) int, used for MX or SRV records
    :param weight: (optional) int, weight for SRV record
    :param port: (optional) int, port for SRV record
    :param frame: (optional) int, 0 or 1 for Web redirects to disable or enable
        frame
    :param frame_title: (optional) string, title if frame is enabled in Web
        redirects
    :param frame_keywords: (optional) string, keywords if frame is enabled in
        Web redirects
    :param frame_description: (optional) string, description if frame is
        enabled in Web redirects
    :param save_path: (optional) int, 0 or 1 for Web redirects
    :param redirect_type: (optional) int, 301 or 302 for Web redirects if frame
        is disabled
    :param mail: (optional) int?, e-mail address for RP records
    :param txt: (optional) int?, domain name for TXT record used in RP records
    :param algorithm: (required only for SSHFP) int, algorithm used to create
        the SSHFP fingerprint. Required for SSHFP records only.
    :param fptype: (required only for SSHFP) int, type of the SSHFP algorithm.
        Required for SSHFP records only.
    :param status: (optional) int, set to 1 to create the record active or to 0
        to create it inactive. If omitted the record will be created active.
    :param geodns_location: (optional) int, ID of a GeoDNS location for A, AAAA
        or CNAME record. The GeoDNS locations can be obtained with List GeoDNS
        locations
    :param caa_flag: (optional) int, 0 - Non critical or 128 - Critical
    :param caa_type: (optional) string, type of CAA record. The available flags
        are issue, issuewild, iodef.
    :param caa_value: (optional) string, if caa_type is issue, caa_value can be
        hostname or ";". If caa_type is issuewild, it can be hostname or ";".
        If caa_type is iodef, it can be "mailto:someemail@address.tld,
        http://example.tld or http://example.tld.
    """

    url = 'https://api.cloudns.net/dns/add-record.json'

    if record_type.upper() not in RECORD_TYPES:
        # TODO: error handling
        raise Exception('Not a valid record type.')

    if record_type.upper() is 'SSHFP':
        if algorithm is None or fptype is None:
            # TODO do the same error as required var missing
            raise Exception('Not a valid record type.')
        # TODO: make sure they are the right numbers/ strings.
        # allow strings for convenience

    if frame not in [None, 0, 1]:
        # TODO do the same error as required var missing
        raise Exception('Not a valid record type.')

    if save_path not in [None, 0, 1]:
        # TODO do the same error as required var missing
        raise Exception('Not a valid record type.')

    if redirect_type not in [None, 301, 302]:
        # TODO do the same error as required var missing
        raise Exception('Not a valid record type.')

    if redirect_type not in [None, 301, 302]:
        # TODO do the same error as required var missing
        raise Exception('Not a valid record type.')

    if status not in [0, 1]:
        # TODO do the same error as required var missing
        raise Exception('Not a valid record type.')

    if caa_flag not in [0, 128]:
        # TODO do the same error as required var missing
        raise Exception('Not a valid record type.')

    params['domain-name'] = domain_name
    params['record-type'] = record_type
    params['host'] = host
    params['record'] = record
    params['ttl'] = ttl

    if priority:
        params['priority'] = priority

    if weight:
        params['weight'] = weight

    if port:
        params['port'] = port

    if not frame is None:
        params['frame'] = frame

    if frame_title:
        params['frame-title'] = frame_title

    if frame_keywords:
        params['frame-keywords'] = frame_keywords

    if frame_description:
        params['frame-description'] = frame_description

    if not save_path is None:
        params['save-path'] = save_path

    if not redirect_type is None:
        params['redirect-type'] = redirect_type

    if not mail is None:
        params['mail'] = mail

    if txt:
        params['txt'] = txt

    if not algorithm is None:
        params['algorithm'] = algorithm

    if fptype:
        params['fptype'] = fptype

    if not status is None:
        params['status'] = status

    if not geodns_location is None:
        params['geodns-location'] = geodns_location

    if not caa_flag is None:
        params['caa_flag'] = caa_flag

    if caa_type:
        params['caa_type'] = caa_type

    if caa_value:
        params['caa_value'] = caa_value

    return get(url, params=params)


def update(page = 1, rows_per_page = 30, search = ''):
    """Creates a new zone.

    :param page: (optional) int, current page
    :param rows_per_page: (optional) int, number of results on each page
    :param search: (optional) string used to search domain names, reverse zone
        name, or other keyword to search for in the zone names
    """

    params = get_auth_params()

    params['page'] = page
    params['rows-per-page'] = rows_per_page
    if search:
        params['search'] = search

    return get(URL_CREATE_ZONES, params=params)


def delete(page = 1, rows_per_page = 30, search = ''):
    """Deletes a DNS record

    :param page: (optional) int, current page
    :param rows_per_page: (optional) int, number of results on each page
    :param search: (optional) string used to search domain names, reverse zone
        name, or other keyword to search for in the zone names
    """

    params['page'] = page


@api
def transfer(domain_name, record_id):
    """Toggles active/inactive status on a particular record of a domain name.

    :param domain_name: string, the domain name on which to work
    :param record_id: int, record id (the id returned when listing records)
    """
    params['domain_name'] = domain_name
    params['record_id'] = record_id

    return post(url, params=params)




@api
def toggle_activation(domain_name, record_id):
    """Toggles active/inactive status on a particular record of a domain name.

    :param domain_name: string, the domain name on which to work
    :param record_id: int, record id (the id returned when listing records)
    """
    params['domain_name'] = domain_name
    params['record_id'] = record_id

    return post(url, params=params)


@api
def activate(domain_name, record_id):
    """Makes a particular record on a domain name active

    :param domain_name: string, the domain name on which to work
    :param record_id: int, record id (the id returned when listing records)
    """
    params['domain_name'] = domain_name
    params['record_id'] = record_id
    params['status'] = 1

    return post(url, params=params)


@api
def deactivate(domain_name, record_id):
    """Makes a particular record on a domain name inactive

    :param domain_name: string, the domain name on which to work
    :param record_id: int, record id (the id returned when listing records)
    """

    url = 'https://api.cloudns.net/dns/change-record-status.json'

    params['domain_name'] = domain_name
    params['record_id'] = record_id
    params['status'] = 2

    return post(url, params=params)
