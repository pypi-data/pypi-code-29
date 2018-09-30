# Copyright (c) 2018 Ultimaker B.V.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Config:
    
    # The ID of the plugin to build and deploy.
    package_id: str
    
    # The path to the sources of the plugin.
    # CuraPackageDeployer will use the package.json file in this directory for most of the metadata.
    # It will also try to find a file called `icon.png` in this directory to upload with the package.
    package_sources_dir: str
    
    # List of tags to add to the package.
    tags: List[str]
    
    # The public support website for this package.
    website: str
    
    # Release notes for this release of the package.
    release_notes: str
    
    # Access token to use on the API.
    access_token: str
