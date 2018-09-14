import json
import requests

import urllib3

from cis_client.lib import base_http_client


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ContentClient(base_http_client.BaseClient):
    def __init__(self, north_host, insecure=False):
        super(ContentClient, self)
        self.north_host = north_host
        self.insecure = insecure

    def get(self, auth_token, ingest_point, content_path, **kwargs):
        endpoint = self.get_endpoint(ingest_point, content_path)
        params = self.get_auth_params(**kwargs)
        for url_param in (
                'page_size', 'offset', 'sort_by', 'sort_order',
                'filename', 'filter_case_sensitive',
                'aggregated_status'):
            if kwargs.get(url_param):
                params[url_param] = kwargs.get(url_param)
        if params.get('filter_case_sensitive'):
            params['filter_case_sensitive'] = str(params['filter_case_sensitive']).lower()
        response = requests.get(
            endpoint,
            verify=(not self.insecure),
            headers={"X-Auth-Token": auth_token},
            params=params
        )
        base_http_client.raise_for_http_response(
            response,
            'Getting of content "{content_path}" for "{ingest_point}", brand-id="{brand_id}", '
            'account-id="{account_id}", group-id="{group_id}" was failed.'.format(
                content_path=content_path,
                ingest_point=ingest_point,
                brand_id=kwargs.get('brand_id', ''),
                account_id=kwargs.get('account_id', ''),
                group_id=kwargs.get('group_id', '')
            ))
        return json.loads(response.content)

    def get_endpoint(self, ingest_point, content_path):
        endpoint = '{north_host}/ingest_points/{ingest_point}/content/{content_path}'.format(
            north_host=self.north_host,
            ingest_point=ingest_point,
            content_path=content_path
        )
        return endpoint

    def _create_modify_dir(
            self, method, error_msg,
            auth_token, ingest_point, dir_path, workflow_id, profile_ids, **kwargs):
        endpoint = self.get_endpoint(ingest_point, dir_path)
        workflow_data = {}
        if workflow_id:
            workflow_data['id'] = workflow_id
        if profile_ids:
            workflow_data['profile_ids'] = profile_ids
        data = {
            'workflow': workflow_data or None
        }
        response = method(
            endpoint,
            verify=(not self.insecure),
            headers={
                "X-Auth-Token": auth_token
            },
            params=self.get_auth_params(**kwargs),
            json=data
        )
        base_http_client.raise_for_http_response(response, error_msg)

    def create_dir(self, auth_token, ingest_point, dir_path, workflow_id, profile_ids, **kwargs):
        error_msg = (
            'Creating of directory "{dir_path}" in "{ingest_point}", brand-id="{brand_id}", '
            'account-id="{account_id}", group-id="{group_id}" was failed.').format(
                dir_path=dir_path,
                ingest_point=ingest_point,
                brand_id=kwargs.get('brand_id', ''),
                account_id=kwargs.get('account_id', ''),
                group_id=kwargs.get('group_id', '')
            )
        return self._create_modify_dir(
            requests.post, error_msg, auth_token, ingest_point, dir_path, workflow_id, profile_ids, **kwargs)

    def modify_dir(self, auth_token, ingest_point, dir_path, workflow_id, profile_ids, **kwargs):
        error_msg = (
            'Modification of directory "{dir_path}" in "{ingest_point}", brand-id="{brand_id}", '
            'account-id="{account_id}", group-id="{group_id}" was failed.').format(
                dir_path=dir_path,
                ingest_point=ingest_point,
                brand_id=kwargs.get('brand_id', ''),
                account_id=kwargs.get('account_id', ''),
                group_id=kwargs.get('group_id', '')
            )
        return self._create_modify_dir(
            requests.put, error_msg, auth_token, ingest_point, dir_path, workflow_id, profile_ids, **kwargs)

    def remove(self, auth_token, ingest_point, path, **kwargs):
        endpoint = self.get_endpoint(ingest_point, path)
        params = self.get_auth_params(**kwargs)
        if kwargs.get('recursive'):
            params['force'] = 'true'
        response = requests.delete(
            endpoint,
            verify=(not self.insecure),
            headers={
                "X-Auth-Token": auth_token
            },
            params=params,
        )
        error_msg = (
            'Remove of "{dir_path}" in "{ingest_point}", brand-id="{brand_id}", '
            'account-id="{account_id}", group-id="{group_id}" was failed.').format(
                dir_path=path,
                ingest_point=ingest_point,
                brand_id=kwargs.get('brand_id', ''),
                account_id=kwargs.get('account_id', ''),
                group_id=kwargs.get('group_id', '')
            )
        base_http_client.raise_for_http_response(response, error_msg)
        return json.loads(response.content)


@base_http_client.with_auth
def get_content(north_host, ingest_point, content_path, **kwargs):
    """Gets content info

    :param north_host:
    :param ingest_point:
    :param content_path
    :param kwargs: can contains
        - insecure: True if SSL verification must be skipped
        - brand_id: brand ID
        - account_id: account ID
        - group_id: group ID
        - filename:
        - aggregated_status:
        - filter_case_sensitive
        - sort_by: field name to sort by
        - sort_order: can be 'asc' or 'desc'
        - offset: offset
        - page_size: size of page, -1 means all rows
        - aaa_host: AAA host, optional
        - username: username, optional
        - password: password, optional
        - token: auth token, must be specified if aaa_host,
                 username and password is not specified
    :return: content info
    """
    content_client = ContentClient(north_host, insecure=kwargs['insecure'])
    content_info = content_client.get(kwargs['token'], ingest_point, content_path, **kwargs)
    return content_info


@base_http_client.with_auth
def create_directory(north_host, ingest_point, dir_path, workflow_id, profile_ids, **kwargs):
    """Creates directory

    :param north_host:
    :param ingest_point:
    :param dir_path
    :param workflow_id: workflow id
    :param profile_ids: list of profile ids
    :param kwargs: can contains
        - insecure: True if SSL verification must be skipped
        - brand_id: brand ID
        - account_id: account ID
        - group_id: group ID
        - aaa_host: AAA host, optional
        - username: username, optional
        - password: password, optional
        - token: auth token, must be specified if aaa_host,
                 username and password is not specified
    :return:
    """
    content_client = ContentClient(north_host, insecure=kwargs['insecure'])
    return content_client.create_dir(
        kwargs['token'], ingest_point, dir_path, workflow_id, profile_ids, **kwargs)


@base_http_client.with_auth
def modify_directory(north_host, ingest_point, dir_path, workflow_id, profile_ids, **kwargs):
    """Modifies directory

    :param north_host:
    :param ingest_point:
    :param dir_path
    :param workflow_id: workflow id
    :param profile_ids: list of profile ids
    :param kwargs: can contains
        - insecure: True if SSL verification must be skipped
        - brand_id: brand ID
        - account_id: account ID
        - group_id: group ID
        - aaa_host: AAA host, optional
        - username: username, optional
        - password: password, optional
        - token: auth token, must be specified if aaa_host,
                 username and password is not specified
    :return:
    """
    content_client = ContentClient(north_host, insecure=kwargs['insecure'])
    return content_client.modify_dir(
        kwargs['token'], ingest_point, dir_path, workflow_id, profile_ids, **kwargs)


@base_http_client.with_auth
def remove(north_host, ingest_point, path, **kwargs):
    """Removes directory

    :param north_host:
    :param ingest_point:
    :param path
    :param kwargs: can contains
        - recursive: bool, remove directories and their contents recursively
        - insecure: True if SSL verification must be skipped
        - brand_id: brand ID
        - account_id: account ID
        - group_id: group ID
        - aaa_host: AAA host, optional
        - username: username, optional
        - password: password, optional
        - token: auth token, must be specified if aaa_host,
                 username and password is not specified
    :return:
    """
    content_client = ContentClient(north_host, insecure=kwargs['insecure'])
    return content_client.remove(kwargs['token'], ingest_point, path, **kwargs)
