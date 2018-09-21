# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Create a package to accelerate Neural Networks with Project Brainwave.
"""

import json
import copy

from azureml.core.image import Image
from azureml.core.image.image import ImageConfig

from pkg_resources import resource_string

from azureml.core.model import Model
from azureml._model_management._util import _get_mms_url
from dateutil.parser import parse

realtimeai_image_payload_template = json.loads(resource_string(__name__,
                                                               'data/brainwave_image_payload_template.json')
                                               .decode('ascii'))


class BrainwaveImage(Image):
    """
    Project Brainwave image representing a package that can be deployed to have accelerated graphs.
    """
    _image_type = "FPGA"
    _expected_payload_keys = ['createdTime', 'creationState', 'description', 'id', 'properties',
                              'imageLocation', 'imageType', 'modelIds', 'name', 'kvTags', 'version']

    def _initialize(self, workspace, obj_dict):
        self._validate_get_payload(obj_dict)
        created_time = parse(obj_dict['createdTime'])

        image_build_log_uri = obj_dict['imageBuildLogUri'] if 'imageBuildLogUri' in obj_dict else None
        image_id = obj_dict['id']
        models = []
        if 'modelDetails' in obj_dict:
            models = [Model.deserialize(workspace, model_payload) for model_payload in obj_dict['modelDetails']]
        self.created_time = created_time
        self.creation_state = obj_dict['creationState']
        self.description = obj_dict['description']
        self.id = image_id
        self.image_build_log_uri = image_build_log_uri
        self.image_location = obj_dict['imageLocation']
        self.image_type = obj_dict['imageType']
        self.model_ids = obj_dict['modelIds']
        self.name = obj_dict['name']
        self.tags = obj_dict['kvTags']
        self.version = obj_dict['version']
        self.properties = obj_dict['properties']
        self.workspace = workspace
        self._mms_endpoint = _get_mms_url(workspace) + '/images/{}'.format(image_id)
        self._auth = workspace._auth
        self.models = models

    @staticmethod
    def image_configuration():
        """
        Method for creating an image configuration object
        """
        return BrainwaveImageConfiguration()

    def run(self):
        """
        Test an image locally. This does not apply to brainwave images, since they require dedicated hardware to
        accelerate neural networks.
        :raises: NotImplementedError
        """
        raise NotImplementedError("Can't run brainwave images locally.")


class BrainwaveImageConfiguration(ImageConfig):
    """
    Image configuration object for brainwave services.
    """
    _can_deploy = True

    def __init__(self, tags=None, properties=None, description=None):
        """
        Create image configuration object.
        :param tags: Dictionary of key value tags to give this image
        :type tags: dict[str, str]
        :param properties: Dictionary of key value properties to give this image. These properties cannot
            be changed after deployment, however new key value pairs can be added
        :type properties: dict[str, str]
        :param description: A description to give this image
        :type description: str
        :return: A configuration object to use when creating the image
        :rtype: azureml.contrib.brainwave.BrainwaveImageConfiguration
        :raises: azureml.exceptions.WebserviceException
        """
        self.tags = tags
        self.properties = properties
        self.description = description
        self.validate_configuration()

    def validate_configuration(self):
        """
        Checks that the specified configuration values are valid. Will raise a WebserviceException if validation
        fails.
        """
        pass

    def build_create_payload(self, workspace, name, model_ids):
        """
        Method for building the creation payload associated with this configuration object
        :param workspace: The workspace associated with the image
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the image
        :type name: str
        :param model_ids: A list of model IDs to be packaged with the image
        :type model_ids: list[str]
        :return: The creation payload to use for Image creation
        :rtype: dict
        """
        if model_ids is None:
            raise ValueError("Cannot create RealtimeAi image without model")
        json_payload = copy.deepcopy(realtimeai_image_payload_template)
        json_payload['name'] = name
        json_payload['kvTags'] = self.tags
        json_payload['properties'] = self.properties
        json_payload['description'] = self.description
        json_payload['modelIds'] = model_ids
        return json_payload
