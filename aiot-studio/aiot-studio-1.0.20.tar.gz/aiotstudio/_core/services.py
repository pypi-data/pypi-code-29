from __future__ import absolute_import

from .errors import FeatureUnavailableError, RestitutionTimeoutError, RestitutionResultError
from requests.exceptions import Timeout


def restitution_search(client, query):
    if 'limit' in query.keys():
        if query['limit'] > 100000:
            if 'offset' in query.keys() and (query['limit'] - query['offset']) > 100000:
                query.pop('offset', None)
                query['limit'] = 100000
            else:
                query['limit'] = 100000

    try:
        response = client.post("/api/v3/search/all", query)
        if response.ok:
            return response.json()
        else:
            raise RestitutionResultError(response.text)
    except Timeout as e:
        raise RestitutionTimeoutError("Call to restitution timed out (max: {} seconds).".format(client.DEFAULT_TIMEOUT_SECONDS), {"query": query, "error": e})


def blob_store_fetch(client, bucket, object):
    raise FeatureUnavailableError("Use of the blob store is not yet available from outside mnubo's infrastructure.")


def blob_store_bucket_names(client):
    raise FeatureUnavailableError("Use of the blob store is not yet available from outside mnubo's infrastructure.")
