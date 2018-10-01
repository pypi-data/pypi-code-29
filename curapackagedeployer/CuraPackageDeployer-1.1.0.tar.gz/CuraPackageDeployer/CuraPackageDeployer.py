# Copyright (c) 2018 Ultimaker B.V.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from pathlib import Path
from typing import Optional, Dict
from zipfile import ZipFile, ZIP_DEFLATED

from CuraPackageDeployer import Config
from CuraPackageDeployer.PackagesApiClient import PackagesApiClient


class CuraPackageDeployer:
    """
    Class responsible for executing all the deployer business logic.
    """
    
    # Required fields needed for uploading.
    plugin_json_required_fields = ["name", "description", "version", "api"]
    
    def __init__(self, config: Config) -> None:
        """
        Create a new deployer instance.
        :param config: The deployer configuration.
        """
        self._plugin_json_data: Optional[Dict[str, any]] = None
        self._icon_data: Optional[bytes] = None
        self._plugin_archive: Optional[ZipFile] = None
        self._package_release_id: Optional[str] = None
        self._build_success: bool = False

        self._config: Config = config
        self._api_client = PackagesApiClient()
        
        self._initialize()
        
    def _initialize(self):
        self._api_client.setBearerToken(self._config.access_token)
    
    def loadPluginSources(self):
        """
        Load the source files needed to build and deploy the plugin.
        """
        logging.info("Finding and validating plugin source files...")
        
        # Validate the plugin sources exist.
        plugin_root_path = Path(self._config.package_sources_dir)
        if not plugin_root_path.exists() or not plugin_root_path.is_dir():
            raise NotADirectoryError("No directory found at {}".format(plugin_root_path))
        
        # Find the plugin.json file and load it.
        plugin_json_path = Path(self._config.package_sources_dir + "/plugin.json")
        if not plugin_json_path.exists():
            raise FileNotFoundError("No plugin.json file found at {}".format(plugin_json_path))
        
        # Get the plugin.json data and validate it.
        self._plugin_json_data = json.loads(plugin_json_path.open().read())
        for field in self.plugin_json_required_fields:
            if field not in self._plugin_json_data:
                raise KeyError("Required field {} not found in plugin.json".format(field))
            
        # Find an optional icon.png to upload.
        icon_path = Path(self._config.package_sources_dir + "/icon.png")
        if icon_path.exists():
            logging.info("Found an icon to upload with the release")
            self._icon_data = icon_path.open("rb").read()
    
    def buildPlugin(self) -> None:
        """
        Make a ZIP archive from the plugin sources.
        """
        logging.info("Creating ZIP archive from plugin source files...")
        plugin_root_path = Path(self._config.package_sources_dir).expanduser().resolve(strict = True)
        with ZipFile("{}.zip".format(self._config.package_id), "w", ZIP_DEFLATED) as zip_file:
            for file in plugin_root_path.rglob('*'):
                zip_file.write(file, file.relative_to(plugin_root_path.parent))
            zip_file.close()
            self._plugin_archive = zip_file
    
    def deploy(self):
        """
        Deploy the release via the API.
        """
        object_name = self._uploadPluginSources()
        metadata = {
            "display_name": self._plugin_json_data["name"],
            "package_version": self._plugin_json_data["version"],
            "description": self._plugin_json_data["description"],
            "website": self._config.website,
            "tags": self._config.tags,
            "sdk_versions": [self._plugin_json_data["api"]],
            "release_notes": self._config.release_notes
        }
        package_release = self._api_client.createOrUpdatePackageRelease(
                self._config.package_id, metadata, object_name, self._icon_data)
        if not package_release:
            raise Exception("Could not create package release")
        self._package_release_id = package_release.package_release_id

    def checkBuildStatus(self, throw_exception_on_failed: bool = True) -> None:
        """
        Check the build status for the release to ensure the build succeeds.
        :param throw_exception_on_failed: Throw an exception if the build failed. Handy for CI status.
        """
        package_release = self._api_client.getPackageRelease(self._config.package_id, self._package_release_id)
        if not package_release:
            raise Exception("Could not fetch releases to check build status")
        package_build = package_release.package_builds[0]
        self._build_success = package_build["build_status"] == "finished"
        if not self._build_success and throw_exception_on_failed:
            raise Exception("The remote build failed: {}".format(package_build["build_error"]))
        
    def requestReview(self) -> None:
        """
        Request a review from Ultimaker for the release.
        """
        logging.info("Requesting review from Ultimaker...")
        self._api_client.requestReview(self._config.package_id, self._package_release_id)

    def _uploadPluginSources(self) -> str:
        """
        Upload the sources of the plugin to the API.
        :return: The object name of the sources, needed for the next API call.
        """
        plugin_data = open("{}.zip".format(self._config.package_id), "rb").read()
        object_name = self._api_client.uploadPackageSources(
                self._config.package_id, plugin_data).package_sources_object_name
        if not object_name:
            raise Exception("Could not upload package sources")
        return object_name
