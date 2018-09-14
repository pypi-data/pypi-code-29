import json
import requests
import urllib3

from cis_client.lib.aaa import auth_client
from cis_client.lib import base_http_client

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class JobsClient(base_http_client.BaseClient):
    jobs_endpoint = 'jobs'

    def __init__(self, north_host, token, insecure=False):
        super(JobsClient, self).__init__()
        self.jobs_endpoint_url = "{}/{}".format(north_host, self.jobs_endpoint)
        self.token = token
        self.insecure = insecure

    def get_auth_header(self):
        return {auth_client.AuthClient.auth_header: self.token}

    def list(self, **kwargs):
        query_params = self.compose_query_jobs_url_params(**kwargs)
        get_jobs_response = requests.get(
            self.jobs_endpoint_url,
            verify=(not self.insecure),
            params=query_params,
            headers=self.get_auth_header())
        base_http_client.raise_for_http_response(
            get_jobs_response,
            'Listing of jobs was failed. Query parameters: {query_params}.',
            query_params=query_params
        )
        return json.loads(get_jobs_response.content)

    def compose_query_jobs_url_params(self, **kwargs):
        join_values = lambda list_values: ','.join(list_values)
        query_params = {}
        if kwargs.get('job_type') is not None:
            query_params['type'] = join_values(kwargs['job_type'])
        if kwargs.get('path') is not None:
            query_params['filename'] = join_values(kwargs['path'])
        if kwargs.get('file_basename') is not None:
            query_params['filter_by'] = 'file_basename'
            query_params['filter_value'] = kwargs['file_basename']
        if kwargs.get('case_sensitive_file_basename') is not None:
            query_params['filter_case_sensitive'] = 'true' if kwargs['filter_case_sensitive'] else 'false'
        if kwargs.get('state') is not None:
            query_params['state'] = join_values(kwargs['state'])
        if kwargs.get('state_simple') is not None:
            query_params['state_simple'] = join_values(kwargs['state_simple'])
        if kwargs.get('aggregated_status') is not None:
            query_params['aggregated_status'] = kwargs['aggregated_status']
        if kwargs.get('fields') is not None:
            query_params['fields'] = join_values(kwargs['fields'])
        if kwargs.get('with_children') is not None:
            query_params['with_children'] = 'true' if kwargs['with_children'] else 'false'
        if kwargs.get('ingest_point') is not None:
            query_params['ingest_point'] = kwargs['ingest_point']
        if kwargs.get('root_only') is not None:
            query_params['root_only'] = 'true' if kwargs.get('root_only') else 'false'
        if kwargs.get('sort_by') is not None:
            query_params['sort_by'] = kwargs['sort_by']
        if kwargs.get('sort_order') is not None:
            query_params['sort_order'] = kwargs['sort_order']
        if kwargs.get('offset') is not None:
            query_params['offset'] = str(kwargs['offset'])
        if kwargs.get('page_size') is not None:
            query_params['page_size'] = str(kwargs['page_size'])
        if kwargs.get('brand_id') is not None:
            query_params['brand_id'] = str(kwargs['brand_id'])
        if kwargs.get('account_id') is not None:
            query_params['account_id'] = str(kwargs['account_id'])
        if kwargs.get('group_id') is not None:
            query_params['group_id'] = str(kwargs['group_id'])
        if kwargs.get('latest') is not None and kwargs['latest']:
            query_params['latest'] = str(kwargs['latest'])
        return query_params


@base_http_client.with_auth
def get_jobs(north_host, **kwargs):
    """Gets jobs

    :param north_host:
    :param kwargs: can contains
        - brand_id: Brand ID
        - account_id: account ID
        - group_id: group ID
        - job_type: list of job types like ['abr'] or ['http-push'] or ['abr', 'http-push'] or other
        - path: list of exact paths like ['root_dir/sub_dir/vid.mp4']
        - file_basename: partial match of filename.
            Filtering by filename allows to specify the beginning of filename only.
        - case_sensitive_file_basename: True if filtering is case sensitive.
        - state: list of allowed states. Allowed states are:
            pending
            running
            cancelling
            paused
            completed
            failed
        - aggregated_status: aggregated status. Allowed states are:
            uploading
            processing
            local_done
            global_done
            failed
        - fields: list of fields in response like ['id', 'filename'].
        - with_children: if True will return whole job tree which contains information
            about children and children of children
        - ingest_point: ingest point id
        - root_only: returns root jobs only
        - sort_by: field name to sort by
        - sort_order: can be 'asc' or 'desc'
        - offset: offset
        - page_size: size of page, -1 means all rows
        - insecure: True if SSL verification must be skipped
        - aaa_host: AAA host, optional
        - username: username, optional
        - password: password, optional
        - token: auth token, must be specified if aaa_host,
                 username and password is not specified
    :return: list of jobs
    """
    jobs_client = JobsClient(north_host, kwargs['token'], insecure=kwargs['insecure'])
    return jobs_client.list(**kwargs)
