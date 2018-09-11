# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GetVpnSitesConfigurationRequest(Model):
    """List of Vpn-Sites.

    :param vpn_sites: List of resource-ids of the vpn-sites for which config
     is to be downloaded.
    :type vpn_sites: list[~azure.mgmt.network.v2018_06_01.models.SubResource]
    :param output_blob_sas_url: The sas-url to download the configurations for
     vpn-sites
    :type output_blob_sas_url: str
    """

    _attribute_map = {
        'vpn_sites': {'key': 'vpnSites', 'type': '[SubResource]'},
        'output_blob_sas_url': {'key': 'outputBlobSasUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GetVpnSitesConfigurationRequest, self).__init__(**kwargs)
        self.vpn_sites = kwargs.get('vpn_sites', None)
        self.output_blob_sas_url = kwargs.get('output_blob_sas_url', None)
