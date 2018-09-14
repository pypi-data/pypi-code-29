#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

Test flask engine
-----------------

Test suite for flask_engine.

"""

from unittest import TestCase, mock

from flask import Flask
from flask.views import MethodView
from flasgger import Swagger

from dataf import FlaskEngine


class TestFlaskEngine(TestCase):
    """
    Test suite for FlaskEngine class.
    """
    @classmethod
    def setUpClass(cls):
        cls.flask_engine = FlaskEngine({}, {})

    def tearDown(self):
        self.flask_engine._get_view.cache_clear()

    def test_init_attr(self):
        """
        Test __init__ method attribute.
        """
        self.assertIsInstance(self.flask_engine, FlaskEngine)
        self.assertIsInstance(self.flask_engine.app, Flask)
        self.assertIsInstance(self.flask_engine.swagger, Swagger)

    @mock.patch('dataf.flask_engine.Flask.add_url_rule')
    def test_init_url(self, mock):
        """
        Test __init__ method correctly set url.
        """
        flask_engine = FlaskEngine({'/test': {'cls': MethodView}}, {})
        mock.assert_called_with(
            '/test', view_func=flask_engine._get_view(MethodView), methods=None
        )

    @mock.patch('dataf.tests.test_flask_engine.MethodView.as_view')
    def test_get_view(self, mock):
        """
        Test _get_view method call MethodView.as_view.
        """
        self.flask_engine._get_view(MethodView)
        mock.assert_called_with(MethodView.__name__)

    def test_get_view_return(self):
        """
        Test return value of _get_view method.
        """
        view = self.flask_engine._get_view(MethodView)
        self.assertTrue(callable(view))
        self.assertEqual(view.view_class, MethodView.as_view(MethodView.__name__).view_class)

    @mock.patch('dataf.flask_engine.Flask.run')
    def test_run(self, mock):
        """
        Test run method.
        """
        self.flask_engine.run()
        mock.assert_called_with(debug=True)
