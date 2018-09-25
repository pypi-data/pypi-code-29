import json

import pytest
from requests.exceptions import HTTPError

from directory_cms_client import helpers


@pytest.mark.parametrize('response_class', [
    helpers.CMSLiveResponse,
    helpers.CMSCacheResponse,
    helpers.CMSFailureResponse,
])
def test_cms_response_interoparability(response_class):
    response = response_class(
        content=bytes(json.dumps({'key': 'value'}), 'utf8'),
        status_code=400,
    )

    assert response.status_code == 400
    assert response.json() == {'key': 'value'}

    with pytest.raises(HTTPError):
        response.raise_for_status()
