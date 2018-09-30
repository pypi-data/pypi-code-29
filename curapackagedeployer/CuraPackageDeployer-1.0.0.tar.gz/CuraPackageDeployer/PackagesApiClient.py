# Copyright (c) 2018 Ultimaker B.V.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import json
import logging
from datetime import timedelta
from typing import Dict, Union, List, Optional

from bravado.client import SwaggerClient
from bravado.exception import HTTPError
from bravado.requests_client import RequestsClient
from bravado_core.model import Model

from CuraPackageDeployer.ApiAuthenticator import ApiAuthenticator


class PackagesApiClient:
    """
    API client for calling the packages API.
    """
    
    _root_url = "https://api-staging.ultimaker.com/cura-packages/v1"
    
    def __init__(self) -> None:
        self._http_client = RequestsClient()
        self._http_client.authenticator = ApiAuthenticator()
        self._api: SwaggerClient = SwaggerClient.from_spec(
            self._loadSpec(),
            origin_url = self._root_url,
            http_client = self._http_client
        )
        self._api.swagger_spec.api_url = self._root_url
        
    def setBearerToken(self, token: str) -> None:
        """
        Set the bearer token used for authenticating to the API.
        :param token: The bearer token.
        """
        self._http_client.authenticator.bearer_tokens[self._root_url] = token
        
    def getPackageReleases(self, package_id: str) -> Optional[Union[Model, List[Model]]]:
        """
        Get all existing releases for a package.
        :param package_id: The ID of the package.
        :return: A list of models with the releases data.
        """
        try:
            request = self._api.developer.getDeveloperPackageReleases(package_id = package_id).result()
            return self._loadModel("PackageReleaseResponse", request, is_list = True)
        except HTTPError as e:
            logging.error("Could not get package releases: {}".format(e))
            return None
        
    def uploadPackageSources(self, package_id: str, package_sources: bytes) -> Optional[Model]:
        """
        Upload the sources for a package.
        :param package_id:
        :param package_sources:
        :return:
        """
        b64_encoded = base64.b64encode(package_sources)
        data_uri_string = "data:application/zip;base64,{}".format(b64_encoded.decode("utf-8"))

        logging.info("Uploading sources to Ultimaker...")
        try:
            data = {"package_sources": data_uri_string}
            result = self._api.developer.uploadPackageSources(package_id = package_id,
                                                              request_body = dict(data = data)).result()
            return self._loadModel("PackageUploadResponse", result)
        except HTTPError as e:
            logging.error("Could not upload package sources: {}".format(e))
            return None
        
    def createOrUpdatePackageRelease(self, package_id: str, metadata: Dict[str, any], object_name: str,
                                     icon_source: Optional[bytes] = None) -> Optional[Model]:
        """
        Create a new or update an existing package release with the new data.
        :param package_id: The ID of the package
        :param metadata: Package metadata, includes package version.
        :param object_name: Name of the uploaded sources.
        :param icon_source: Icon data.
        :return: The package release if success, None otherwise.
        """
        package_releases = self.getPackageReleases(package_id)
        print("package_releases", package_releases)
        if not package_releases:
            logging.error("Could not fetch existing releases for package {}".format(package_id))
            return None
        
        release_id = None
        for release in package_releases:
            if release["package_version"] == metadata["package_version"]:
                if release["status"] in ["published", "unpublished"]:
                    logging.error("A release of this package with version {} already exists but was already published."
                                  .format(release["package_version"]))
                    return None
                release_id = release["package_release_id"]

        metadata["status"] = "concept"
        metadata["package_sources_object_name"] = object_name
        if icon_source:
            metadata["icon"] = "data:image/png;base64,{}".format(base64.b64encode(icon_source).decode("utf-8"))
                
        if release_id:
            # A release of this package and version number already exists, so we'll update it.
            logging.info("Updating existing release of version {}...".format(metadata["package_version"]))
            del metadata["package_version"]
            result = self._api.developer.updateDeveloperPackageRelease(
                package_id = package_id,
                package_release_id = release_id,
                request_body = dict(data = metadata)
            ).result()
            return self._loadModel("PackageReleaseResponse", result)
        else:
            logging.info("Creating new release with version {}...".format(metadata["package_version"]))
            result = self._api.developer.createDeveloperPackageRelease(
                package_id = package_id,
                request_body = dict(data = metadata)
            ).result()
            return self._loadModel("PackageReleaseResponse", result)
    
    def requestReview(self, package_id: str, package_release_id: str) -> Optional[Model]:
        """
        Request a review for a package release.
        :param package_id: The ID of the package.
        :param package_release_id: The ID of the release.
        :return: The package release if success, None otherwise.
        """
        request_data = {
            "status": "review",
            "description": "This review was requested automatically via CuraPackageDeployer."
        }
        result = self._api.developer.developerPackageReleaseStatusChange(
            package_id = package_id,
            package_release_id = package_release_id,
            request_body = dict(data = request_data)
        ).result()
        return self._loadModel("PackageReleaseResponse", result)

    def _loadSpec(self) -> Dict[str, any]:
        """
        Load the API spec from the live API.
        :return: The API spec dict.
        """
        request_params = {'method': 'GET', 'url': "{}/spec".format(self._root_url)}
        timeout_sec = timedelta(seconds=10).total_seconds()
        
        response = self._http_client.request(request_params).result(timeout_sec)
        spec_json = response.text
        spec_dict = json.loads(spec_json)
        spec_dict = self._updatePatterns(spec_dict)

        # Remove /spec endpoints to prevent recursive issues.
        for path in list(spec_dict['paths']):
            if path.endswith("/spec") or not path.strip("/"):
                del spec_dict["paths"][path]
                
        return spec_dict

    def _updatePatterns(self, spec: Dict[str, any]) -> Dict[str, any]:
        """
        Patterns starting or ending with slashes are not supported by Bravado.
        This method recursively removes them.
        :param spec: The spec to update.
        :return: The updated spec.
        """
        for key, value in spec.items():
            if isinstance(value, dict):
                self._updatePatterns(value)
            elif key == "pattern" and value[0] == '/' and value[-1] == '/':
                spec[key] = value[1:-1]
        return spec
    
    def _loadModel(self, model_name: str, response: str, is_list: bool = False) -> Union[Model, List[Model]]:
        """
        Converts an API response string to a model.
        :param model_name: Name to give to the model.
        :param response: Response string to convert.
        :param is_list: Whether the response is a list of models or not.
        :return: The model or list of models.
        """
        logging.info("model %s: %s", model_name, response[:1000])
        data_dict = json.loads(response)
        if "data" not in data_dict:
            raise AssertionError("Unexpected response for model {}: {}".format(model_name, data_dict))
        model_class = self._api.get_model(model_name)
        if is_list:
            return [model_class(**item) for item in data_dict["data"]]
        return model_class(**data_dict["data"])
