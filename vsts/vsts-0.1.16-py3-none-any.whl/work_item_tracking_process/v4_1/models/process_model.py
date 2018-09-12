# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ProcessModel(Model):
    """ProcessModel.

    :param description: Description of the process
    :type description: str
    :param name: Name of the process
    :type name: str
    :param projects: Projects in this process
    :type projects: list of :class:`ProjectReference <work-item-tracking.v4_1.models.ProjectReference>`
    :param properties: Properties of the process
    :type properties: :class:`ProcessProperties <work-item-tracking.v4_1.models.ProcessProperties>`
    :param reference_name: Reference name of the process
    :type reference_name: str
    :param type_id: The ID of the process
    :type type_id: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'projects': {'key': 'projects', 'type': '[ProjectReference]'},
        'properties': {'key': 'properties', 'type': 'ProcessProperties'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, description=None, name=None, projects=None, properties=None, reference_name=None, type_id=None):
        super(ProcessModel, self).__init__()
        self.description = description
        self.name = name
        self.projects = projects
        self.properties = properties
        self.reference_name = reference_name
        self.type_id = type_id
