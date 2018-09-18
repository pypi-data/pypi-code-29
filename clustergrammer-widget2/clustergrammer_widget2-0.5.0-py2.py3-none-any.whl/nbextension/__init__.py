#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Nicolas Fernandez.
# Distributed under the terms of the Modified BSD License.

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'nbextension/static',
        'dest': 'clustergrammer_widget2',
        'require': 'clustergrammer_widget2/extension'
    }]
