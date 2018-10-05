# -*- coding: utf-8 -*-
"""
Module swagger.py
---------------------
  Swagger documentation endpoints
"""
import json
import flask
import os


class Swagger(object):
    """
    Swagger ui endpoints.
    """
    def __init__(self, specification, api_title):
        self.spec = specification
        self.index_path = "index.html"
        self.api_title = api_title

    def swagger_json(self):
        """
        endpoint that returns the swagger.json specification.
        """
        return json.dumps(self.spec)

    def index(self):
        """
        returns the swagger index.html page.
        """
        spec_name = "{}.swagger_json".format(self.api_title)
        temp = flask.render_template(self.index_path, spec=spec_name, api_title=self.api_title)
        return temp
