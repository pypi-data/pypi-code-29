from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import os
import requests


LYREBIRD_API_HOST = os.getenv('LYREBIRD_URL', 'https://avatar.lyrebird.ai')


class LyrebirdError(Exception):
    pass


def req(logger, access_token, meth, path, params, **kwargs):
    full_url = LYREBIRD_API_HOST + '/api/v0' + path
    logger.debug('%s %s %s', meth, full_url, params)
    headers = {
        'authorization': 'Bearer ' + access_token,
        'Content-Type': "application/json",
        'accept': "application/json"
    }
    headers.update(kwargs.pop('headers', {}))
    data = json.dumps(kwargs.pop('data', {}))
    if meth == 'POST':
        rsp = requests.request(
            meth,
            full_url,
            headers=headers,
            params=params,
            data=data,
            **kwargs
        )
    else:
        rsp = requests.request(
            meth,
            full_url,
            headers=headers,
            params=params,
            **kwargs
        )

    if rsp.status_code > 200:
        raise LyrebirdError('Lyrebird Vocal Avatar API responded with status: ' +
                            str(rsp.status_code) + ' (' + rsp.reason + ')')

    logger.debug('%s %s %s', meth, full_url, rsp.status_code)
    return rsp


class Lyrebird(object):
    access_token = None

    def __init__(self, access_token, logger=None):
        self.access_token = access_token
        self.logger = logger or logging.getLogger(__name__)

    def generated(self, offset=0, limit=10):
        """ Return the list of generated utterances.

        :param offset: The offset of the first returned paginated utterances from the beginning of the result set. You can read more at http://docs.lyrebird.ai/reference-avatar/api.html#section/Pagination
        :param limit: Limit the number of utterances returned
        :return:
        """
        params = {}
        if offset is not None:
            params['offset'] = offset
        if limit is not None:
            params['limit'] = limit
        resp = req(self.logger, self.access_token, 'GET', '/generated', params)
        return resp

    def generate(self, text):
        """ Synthethize the text using the client vocal avatar.

        :param text: the text to synthethize
        :return:
        """
        params = {}
        headers = {}
        resp = req(
            self.logger,
            self.access_token,
            'POST',
            '/generate',
            params,
            data={
                'text': text},
            headers={})
        return resp
