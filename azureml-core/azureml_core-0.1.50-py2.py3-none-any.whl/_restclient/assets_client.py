# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Access AssetsClient"""

import datetime
import re
import os
import requests

from .workspace_client import WorkspaceClient


class AssetsClient(WorkspaceClient):
    """Asset client class"""
    def __init__(self, host, auth, subscription_id, resource_group,
                 workspace_name, **kwargs):
        """Constructor of the class."""

        self._subscription_id = subscription_id
        self._resource_group = resource_group
        self._workspace_name = workspace_name
        host = host if host else self._get_host_url(auth)
        host = AssetsClient._convert_exp_to_mms(host)
        super(AssetsClient, self).__init__(host, auth, subscription_id,
                                           resource_group, workspace_name,
                                           **kwargs)

    def create_asset(self, model_name, artifact_values, metadata_dict,
                     project_id=None, run_id=None, tags=None, properties=None):
        """
        :param run:
        :param model_name:
        :param artifact_map:
        artifact_path to artifact map
        :param tags:
        :type tags: dict[str, str]
        :param properties:
        :type properties: dict[str, str]
        :return:
        """
        create_asset_host = self._get_host_url()
        create_asset_url = "{}/api/{}/assets?api-version=2018-03-01-preview".format(
            create_asset_host,
            self.get_workspace_uri_path().strip("/"))

        created_time = str(datetime.datetime.utcnow())
        payload = {"name": model_name,
                   "description": "{} saved during run {} in project {}".format(model_name,
                                                                                run_id,
                                                                                project_id),
                   "artifacts": artifact_values,
                   "kvTags": tags,
                   "properties": properties,
                   "runid": run_id,
                   "projectid": project_id,
                   "meta": metadata_dict,
                   "CreatedTime": created_time}
        headers = self._client._client.creds.get_authentication_header()
        self._logger.debug("Create Asset url: {}\nPayload: {}".format(
            create_asset_url, str(payload)))
        result = requests.post(create_asset_url, json=payload, headers=headers)
        if result.status_code != 200:
            message = "Create asset request error. Code: {}\n: {}".format(result.status_code,
                                                                          result.text)
            self._logger.error(message)
            raise Exception(message)
        return result

    def get_asset_id(self, run_id, name):
        """Get asset identification"""
        asset_dict = self._execute_with_workspace_arguments(self._client.asset.list_query,
                                                            run_id=run_id,
                                                            name=name)
        asset = asset_dict.value[0]
        return asset.id

    def _get_host_url(self, auth=None):
        auth = auth if auth else self._client.config.credentials
        base_url = self.get_cluster_url(auth)
        return AssetsClient._convert_exp_to_mms(base_url)

    @staticmethod
    def _convert_exp_to_mms(url):
        # TODO use service discovery here
        if "master." in url or "mms." in url or os.environ.get('AZUREML_EXPERIMENTATION_HOST'):
            mms_host = "https://mms.azureml-test.net"  # test
            # TODO Below used due to 502 in Test per Anubhav
            # mms_host = "https://eastus2euap.modelmanagement.azureml.net"  # canary
        else:
            region = re.compile("//(.*?)\.").search(url).group(1)
            mms_host = "https://{}.modelmanagement.azureml.net".format(region)
        return mms_host

    def get_asset_by_id(self, asset_id):
        """
        Get events of a run by its run_id
        :rtype: ~_restclient.models.Asset or ~msrest.pipeline.ClientRawResponse
        """
        return self._execute_with_workspace_arguments(self._client.asset.query_by_id,
                                                      id=asset_id)

    def list_assets(self):
        """
        Get events of a run by its run_id
        :rtype: ~_restclient.models.Asset or ~msrest.pipeline.ClientRawResponse
        """
        return self._execute_with_workspace_arguments(self._client.asset.list_query)
