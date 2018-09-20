#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Flask engine
------------

Engine for web server with Flask and swagger.

"""

from functools import lru_cache

from flask import Flask
from flasgger import Swagger


class FlaskEngine:
    """
    Handle flask app with swagger.
    Load all view from views dictionary with key 'cls'.
    You can define REST method in they 'method' key.

    :param dict views: Web views data.
    :param dict swagger_config: swagger configuration.
    """
    def __init__(self, views, swagger_config):
        self.app = Flask(__name__)
        self.swagger = Swagger(self.app, **swagger_config)
        for url, view in views.items():
            self.app.add_url_rule(
                url, view_func=self._get_view(view['cls']),
                methods=view.get('methods')
            )

    @staticmethod
    @lru_cache()
    def _get_view(view):
        """
        Get a view and put it in cache for view used by multiple methods.

        :param cls view: Flask View class.
        :return: view as view.
        """
        return view.as_view(view.__name__)

    def run(self):
        """
        Run the flask app with debug.
        """
        self.app.run(debug=True)
