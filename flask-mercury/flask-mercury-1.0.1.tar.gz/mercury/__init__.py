# -*- coding: utf-8 -*-
"""
Flask-Mercury
-----------------
Flask-Mercury is a simple lightweight framework to build flask restful apis 
and swagger documentation.
It is empowered by simple_mappers to delivers auto-mapping capabilities.
"""
from .resource import Resource
from .api_model import ApiModel
from flask import Flask
from .swagger import Swagger


def load(app:Flask, api_title, schemes, api_package="."):
    """ Flask-Mercury loader function.
    An autodiscover function used to load the framework on the current project.
    It will scan the current project looking for mercury Resources and Models
    :param app: The flask app reference.
    :param api_title: the api title.
    :param schemes: a list containing two possible values [http, https].
    :param api_package: a dotted path to the api root package.
    """
    # some imports needed to load the module
    # we are importing them here because it is required only on the first run
    import inspect
    import importlib
    import pkgutil
    from . import utils
    from simple_mappers import JsonObject

    # swagger specification object initialization
    swagger_spec = dict(
        definitions=dict(),
        # initialize the paths part
        paths=dict(),
        tags=list(),
        swagger="2.0",
        info=JsonObject(),
        basePath='/' + api_title,
        schemes=schemes
    )
    swagger_spec = JsonObject(**swagger_spec)

    # builds api info part of the specification
    api_module = importlib.import_module(api_package)
    api_doc = api_module.__doc__
    doc = utils.parse_docstring(api_doc)

    swagger_spec.info.description = doc.summary
    swagger_spec.info.version = doc.version
    swagger_spec.info.title = api_title
    # TODO
    # swagger_spec.info.termsOfService = ""
    # swagger_spec.info.contact = {"email":""}
    # swagger_spec.info.license = {"name": doc.license, "url":""}

    def selector(member):
        """Filters members that are either an ApiModel implementation or a Resource implementation"""
        if inspect.isclass(member):
            if issubclass(member, ApiModel) and member is not ApiModel:
                return True
            elif issubclass(member, Resource) and member is not Resource:
                return True
        return False

    # searches for 'mercury.Resource' implementation recursively on the API_ROOT package
    for finder, name, is_pack in pkgutil.walk_packages(api_module.__path__, api_module.__name__+"."):
        if is_pack:
            # skip packages
            continue
        # import module if it has not been imported yet
        mod = importlib.import_module(name)
        # filter mercury members
        mod_members = inspect.getmembers(
            mod,
            predicate=selector
        )
        # for each member
        for member_name, member_obj in mod_members:
            if hasattr(member_obj, "to_swagger"):
                swagger_spec = member_obj.to_swagger(swagger_spec)
            if hasattr(member_obj, "register"):
                member_obj.register(app, api_title)

    # finally register swagger routes
    # Setting CORS due to swagger-ui
    from flask_cors import CORS
    from flask import Blueprint
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Blueprint initialization
    blueprint = Blueprint(
        api_title,
        __name__,
        static_folder="{}/static".format(current_dir),
        template_folder="{}/static/templates".format(current_dir),
        url_prefix=api_title
    )
    CORS(blueprint)
    s = Swagger(swagger_spec.to_dict(), api_title)
    blueprint.add_url_rule('/swagger', view_func=s.index)
    blueprint.add_url_rule('/swagger/swagger.json', endpoint="swagger_json", view_func=s.swagger_json)
    app.register_blueprint(blueprint, url_prefix="/"+blueprint.name, static_folder="{}/static".format(current_dir))
