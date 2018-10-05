# -*- coding: utf-8 -*-
"""
Module resource.py 
---------------------
    The base Api resource implementation.
"""
from flask import request, jsonify
from flask.views import MethodView
from .api_model import ApiModel
from flask import Flask
import inspect
import json
import re
from simple_mappers.object_mapper import JsonObject
from . import utils
from . import exceptions
from io import StringIO
import uuid
from werkzeug import exceptions as http_exceptions
from flask.views import MethodViewType

_verbs = ["get", "post", "put", "delete", "head", "patch"]

# ROUTE_REGEX = re.compile(r"^/\W+/$", re.IGNORECASE)
ROUTE_REGEX = re.compile(
    r"^<int:\W+>|"
    r"<float:\W+>|"
    r"<path:\W+>|"
    r"<any:\W+>|"
    r"<uuid:\W+>|"
    r"<\W+>$",
    re.IGNORECASE
)
# maps flask path route types to python class types
TYPE_MAP = {
        "string": str,
        "int": int,
        "float": float,
        "path": str,
        "any": str,
        "uuid": uuid.UUID
    }


class MetaResource(MethodViewType):
    """
    A Api Resource Meta class.
    """
    def __new__(mcs, what, bases=None, namespace=None):
        """
        Meta Resource constructor function.
        :param what: The resource class name.
        :param bases: A collection of superclasses.
        :param namespace: The namespace __dict__ for the class.
        """
        cls = super(MetaResource, mcs).__new__(mcs, what, bases, namespace)
        for verb in _verbs:
            mcs.get_signature(cls, verb)
        return cls

    def get_signature(cls, name):
        if hasattr(cls, name):
            method = getattr(cls, name)
            signature = inspect.signature(method)
            method_params = list(signature.parameters.values())
            # add the meta attribute __params__ to the method dict
            object.__setattr__(method, "__params__", method_params)
            # add the meta attribute __pdoc__ containing the parsed method doc string
            object.__setattr__(method, "__pdoc__", utils.parse_docstring(method.__doc__))
            # adds the meta attribute __returns__
            object.__setattr__(method, "__returns__", signature.return_annotation)


BaseResource = MetaResource("BaseResource", (MethodView,), dict())


class Resource(BaseResource):
    """
    A Base API endpoint class implementation.
    """

    __model__ = None
    arg_types = list()
    arg_names = list()

    class Meta:
        """
        Additional meta information for the Resource.
        """
        tag = None
        route = None

    def dispatch_request(self, *args, **kwargs):
        """
        Parses the body of an post request into a Mapping definition object before
        dispatching the request to the endpoint implementation.
        """
        # identify the http request verb
        args = list(args)
        # parse path parameters argument types
        for i in range(len(args)):
            t = self.arg_types[i]
            try:
                args[i] = t(args[i])
            except ValueError:
                raise http_exceptions.BadRequest(
                    "Path parameter '{}' must be '{}' type, "
                    "received '{}' instead.".format(
                        self.arg_names[i],
                        self.arg_types[i],
                        args[i]
                    )
                )

        if request.method.lower() != 'get':
            if request.data is not None:
                # decode the request data body
                data = request.data.decode("utf-8").strip()
                if data != "":
                    data = json.loads(request.data.decode("utf-8"))
                    func = getattr(self, request.method.lower(), None)
                    # sanity check on verb implementation
                    if func is None:
                        raise http_exceptions.MethodNotAllowed(
                            None,
                            "The api endpoint {}, does not support the {} http/https verb.".format(
                                request.path, request.method
                            )
                        )
                    # gets the body api model
                    # TODO: save this information on somewhere to not have perform issubclass check every time
                    if len(func.__params__) > 1 and issubclass(func.__params__[1].annotation, (ApiModel,)):
                        model = func.__params__[1].annotation
                    else:
                        model = None

                    # sanity check on definition errors
                    if model is None and len(data) > 0:
                        raise http_exceptions.InternalServerError(
                            "There is an error on the resource definition. "
                            "Could not parse the request body."
                        )
                    # parse data to a model object
                    if model is not None:
                        data = model.from_dict(data)
                        args.insert(0, data)

        response = super().dispatch_request(*args, **kwargs)
        if isinstance(response, (ApiModel,)):
            response = response.to_json()

        # if isinstance(response, (dict,)):
        response = jsonify(response)

        return response

    @classmethod
    def to_swagger(cls, spec=None):
        """
        Generates the a swagger specification for the endpoints.
        :param spec: the current swagger specification object.
        :return: the swagger specification containing specification for the current resource class.
        """
        serializer = SwaggerSerializer(spec)
        serializer.serialize_resource(cls)
        return serializer.spec

    @classmethod
    def register(cls, app:Flask, api_title):
        """
        Register the resource endpoint route and initialize its path parameters.
        :param app: a reference to the 'flask.Flask' app.
        """
        # get the resource base path
        # checks for route meta data
        base_parameters = list()
        base_type_parameters = list()
        if cls.Meta and cls.Meta.route:
            base_path = cls.Meta.route
            # builds a base path parameter lists
            for p in ROUTE_REGEX.findall(base_path):
                p.replace("<", "").split(":")
                if len(p) > 1:
                    base_parameters.append(p[1])
                    base_type_parameters.append(p[0])
                else:
                    base_parameters.append(p[0])
                    # if no type was given then the default type is string
                    base_type_parameters.append("string")

        else:
            # otherwise uses the module dotted path as path
            mod = cls.__module__.split('.')
            # remove file name from path
            mod.pop()
            if cls.__name__.lower() != mod[-1]:
                mod = "/".join(mod)
                base_path = "/{}/{}".format(mod, cls.__name__.lower())
            else:
                mod = "/".join(mod)
                base_path = "/{}".format(mod)


        # for each http verb performs a sanity check on the path parameters
        # to see if all path parameters match
        p_list = None
        passed = list()
        for verb in _verbs:
            if hasattr(cls, verb):
                impl = getattr(cls, verb)
                # checks path parameters definition
                cls.check_base_param_equality(base_parameters, impl)
                # get list of additional path parameters
                # and compare its definition equality
                if p_list is None:
                    p_list = cls.get_additional_parameters(base_parameters, impl)
                    # track all methods that passed on the equality comparison
                    passed.append(impl.__qualname__)
                else:
                    l = cls.get_additional_parameters(base_parameters, impl)
                    # then both must be equals
                    if not cls.parameters_list_equality_compare(p_list, l):
                        raise exceptions.ResourceSpecError(
                            "All resource verb methods must define the same additional parameters.\n"
                            "Additional parameters for {passed}: \n"
                            "   {p_list}\n"
                            "Additional parameters for {impl}: \n"
                            "   {l}".format(
                                passed=passed,
                                p_list=p_list,
                                impl=impl.__qualname__,
                                l=l
                            )
                        )

                    # track all methods that passed on the equality comparison
                    passed.append(impl.__qualname__)

        if p_list is None:
            raise NotImplementedError(
                "The resource {} does not implements any http verb method.".format(cls.__qualname__)
            )
        # builds final paths
        # for each additional parameter
        # appends to the path
        str_builder = StringIO()
        # base_path must start with the api_title
        if not base_path.startswith(api_title):
            str_builder.write("/"+api_title)
        str_builder.write(base_path)
        has_default = False
        for parameter in p_list:
            # adds path_param to the base_path
            if parameter.annotation is not inspect._empty:
                if parameter.annotation.__name__ == 'str' :
                    param_type = "string"
                else:
                    param_type = parameter.annotation.__name__
                path_param = "/<{}:{}>".format(param_type, parameter.name)
            else:
                path_param = "/<{}>".format(parameter.name)
            if not has_default and parameter.default is not inspect._empty:
                app.add_url_rule(str_builder.getvalue(), view_func=cls.as_view(cls.__name__))
                has_default = True
            str_builder.write(path_param)
        view_name = "{}_full".format(cls.__name__)
        app.add_url_rule(str_builder.getvalue(), view_func=cls.as_view(view_name))

        # build arg_types map for the base_parameters
        for name, t in zip(base_parameters, base_type_parameters):
            cls.arg_types.append(TYPE_MAP[t])
            cls.arg_names.append(name)
            # build arg_types map for the additional parameters
        for p in p_list:
            # sanity check annotation
            if p.annotation is not inspect._empty:
                # cls.arg_types[p.name] = p.annotation
                cls.arg_types.append(p.annotation)
            else:  # str is the default type
                # cls.arg_types[p.name] = str
                cls.arg_types.append(str)
            cls.arg_names.append(p.name)

    @staticmethod
    def check_base_param_equality(base_params, impl):
        """
        checks whether all items in both list of parameters are equals.
        :param base_params: list of base path parameters
        :param impl: a reference to a verb method implementation.
        :return: true if all items in the sequence of both lists are equals.
        :raises: mercury.exceptions.ResourceSpecError
        """
        if base_params is not None:
            # removes args, kwargs and self from the list of impl_params
            params = [
                p.name for p in impl.__params__
                if p.name not in ["args", "kwargs", "self"]
                and not issubclass(p.annotation, (ApiModel,))
            ]
            if len(params) == 0:
                return True
            # check list equality
            for i in range(len(base_params)):
                if params[i] != base_params[i]:
                    # if some divergence is found,
                    # then returns false
                    raise exceptions.ResourceSpecError(
                        "Wrong method parameter definition on '{impl}'. "
                        "The all base_path parameters must be defined in the method signature,"
                        " in the ordering that they appear on the base path. "
                        "Additional parameters may be declared after the ones defined on the base_path."
                        "For more information please refers to the mercury documentation."
                        "Method name: {impl}."
                        "Method declared parameters: {meth_params}."
                        "Base path parameters: {base_params}".format(
                            impl=impl.__qualname__,
                            meth_params=params,
                            base_params=base_params
                        )
                    )
        # return true if every thing is ok
        return True

    @staticmethod
    def get_additional_parameters(base_params, impl):
        """
        builds a list of additional parameters to be added to the base_path.
        :param base_params: a list of base_path parameters.
        :param impl: a verb method implementation.
        :return: a list o additional method parameters.
        """
        if base_params is not None and len(base_params) > 0:
            # removes args, kwargs and self from the list of impl_params
            params = [
                impl.__params__[i]
                for i in range(len(base_params), len(impl.__params__))
                if impl.__params__[i].name not in ["args", "kwargs", "self"]
                and not issubclass(impl.__params__[i].annotation, (ApiModel,))
            ]
        else:
            # removes args, kwargs and self from the list of impl_params
            params = [
                impl.__params__[i]
                for i in range(len(impl.__params__))
                if impl.__params__[i].name not in ["args", "kwargs", "self"]
                and not issubclass(impl.__params__[i].annotation, (ApiModel,))
            ]
        return params

    @staticmethod
    def parameters_list_equality_compare(a, b):
        """
        equality comparison of two list of parameters
        :param a: a list of 'inspect.Parameters'.
        :param b: a list of 'inspect.Parameters'.
        :return: True if both list are equals, False otherwise
        """
        for item_a, item_b in zip(a,b):
            if item_a.name != item_b.name:
                return False
            if item_a.annotation != item_b.annotation:
                return False
            if item_a.default != item_b.default:
                return False
        return True


class SwaggerSerializer(object):
    """
    A Resource to swagger spec serialization class.
    """
    # route substring replace map
    ROUTE_REPLACE_MAP = {
        "int": "",
        "float": "",
        "path": "",
        "any": "",
        "uuid": "",
        # Escape all the characters in pattern except ASCII letters, numbers and '_'.
        "\\<": "{",
        "\\>": "}"
    }
    # the route replace regex
    ROUTE_REPLACE_REGEX = re.compile("|".join(ROUTE_REPLACE_MAP.keys()))
    TYPE_MAP = {
        "str": "string",
        "int": "integer",
        "float": "float",
        "any": "string",
        "uuid": "string",
        'bool': 'boolean'
    }

    def __init__(self, spec=None):
        """
        Swagger Serializer initialization function.
        :param spec: A JsonObject or dict like object that is used to store and representing the resource spec.
        """
        if spec is None:
            self.spec = JsonObject()
            # initialize the paths part
            self.spec.paths = dict()
            self.spec.tags = list()
        else:
            self.spec = spec

    def serialize_resource(self, cls):
        """
        Swagger spec serialization function.
        :param cls: The class to be serialized.
        """
        self.get_tags(cls)

        # builds the swagger base_path for the entire resource
        base_path, params = self.build_base_path(cls)

        # each verb builds a swagger path list
        for verb in _verbs:
            paths = self.get_paths(cls, verb, params, base_path)
            # for each path in the paths list
            #  we build the swagger paths part of the schema
            for path, impl in paths:  # impl: reference to the resource method that implements the verb
                verb_spec = JsonObject()
                verb_spec.tags = [cls.__tag__]
                verb_spec.summary = impl.__pdoc__.summary
                verb_spec.description = impl.__pdoc__.description
                verb_spec.consumes = impl.__pdoc__.consumes
                verb_spec.produces = impl.__pdoc__.produces
                verb_spec.parameters = list()
                # foreach parameter defined in the verb implementation
                for i in range(1, len(impl.__params__)):  # starts form 1 because the parameter 0 is a self reference
                    pspec = self.build_param_spec(impl.__params__[i], impl, params)
                    if pspec["in"] == "body" or (pspec["in"] == "path" and pspec["name"] in path):
                        # verb_spec.parameters
                        # append the parameter specification ti the list
                        verb_spec.parameters.append(pspec)

                # finally builds the responses specification
                verb_spec.responses = dict()
                # if it was declared the return type
                if impl.__returns__ is not inspect._empty:
                    if issubclass(impl.__returns__, ApiModel):
                        verb_spec.responses["200"] = {
                            "description":impl.__pdoc__.returns,
                            "schema":{
                                "$ref":"#/definitions/{}".format(impl.__returns__.__name__)
                            }
                        }
                    else:
                        verb_spec.responses["200"] = {
                            "description": impl.__pdoc__.returns,
                            'type': self.TYPE_MAP.get(impl.__returns__.__name__)
                        }
                else:
                    verb_spec.responses["200"] = {"description": impl.__pdoc__.returns}

                for ex, description in impl.__pdoc__.raises.items():
                    # ex is a string containing or the error code
                    # or the dotted path to the exception
                    if not utils.is_integer(ex):  # is it is a dotted path
                        _ex = utils.import_string(ex)
                        # sanity check exception type
                        if not hasattr(_ex, "code"):
                            raise TypeError(
                                "The exception {} specified on the doc sting is no an http exception"
                                "and does not defines a error code."
                                "Exceptions specified on the docstring must by an http exception.".format(ex)
                            )
                        verb_spec.responses[str(_ex.code)] = {"description": description}
                    else:  # otherwise it is just a error code
                        verb_spec.responses[ex] = {"description": description}

                # now adds the verb to path spec
                if path in self.spec.paths:
                    # sanity check for path collision
                    if verb in self.spec.paths[path]:
                        raise AssertionError(
                            "The path '{}' already has a route for the following verb: {}".format(path, verb)
                        )
                    self.spec.paths[path][verb] = verb_spec
                else:
                    self.spec.paths[path] = {
                        verb:verb_spec
                    }

    def get_tags(self, cls):
        """
        Builds the resource tags swagger specification.
        :param cls: the resource class being serialized to the swagger spec json.
        """
        def add_tag(tag_name):
            cls.__tag__ = tag_name
            # otherwise uses the class name as tag
            tag = list(
                filter(
                    lambda x: x["name"] == tag_name,
                    self.spec.tags
                )
            )
            # if the tag name is not in the swagger tags list
            if len(tag) == 0:
                # then adds to the swagger tags list
                tag = dict(
                    name=tag_name,
                    description=cls.__doc__
                )
                self.spec.tags.append(tag)
        # checks for Meta data
        if hasattr(cls, 'Meta'):
            # checks whether a tag meta data is provided
            if hasattr(cls.Meta, 'tag'):
                add_tag(cls.Meta.tag)
            else:
                tag = cls.__module__.split('.')[1]
                add_tag(tag)
        else:  # meta data was not provided
            tag = cls.__module__.split('.')[1]
            add_tag(tag)

    def build_base_path(self, cls):
        """
        Builds the resource base path
        :param cls: a 'mercury.resource.Resource' class implementation
        :return: the base resource path and a path parameters list
        """
        # prepare swagger paths
        params = dict()
        # checks for route meta data
        if cls.Meta and cls.Meta.route:
            swagger_path = cls.Meta.route
            # searches for path parameters on the route
            path_parameters = ROUTE_REGEX.findall(swagger_path)
            # if found any query parameter on the route
            if len(path_parameters) > 0:
                # then formats the parameters correctly
                swagger_path = self.ROUTE_REPLACE_REGEX.sub(
                    lambda match: self.ROUTE_REPLACE_MAP[re.escape(match.group(0))],
                    swagger_path
                )
                swagger_path = swagger_path.replace(":", "")

                for p in path_parameters:
                    p = p.replace("<", "").replace(">", "").split(":")
                    if len(p) > 1:
                        params[p[1]] = p[0]
                    else:
                        params[p[0]] = None
        else:
            # otherwise uses the module dotted path as path
            # otherwise uses the module dotted path as path
            mod = cls.__module__.split('.')

            if len(mod)> 0 and cls.__name__.lower() != mod[-1]:
                mod = "/".join(mod)
                swagger_path = "/{}/{}".format(mod, cls.__name__.lower())
            else:
                mod = "/".join(mod)
                swagger_path = "/{}".format(mod)

        return swagger_path, params

    @staticmethod
    def get_verb(verb, cls):
        """
        Gets and returns the Resource verb implementation
        :param verb: verb method
        :param cls: Resource class
        """
        if hasattr(cls, verb):
            return getattr(cls, verb)
        return None

    def get_paths(self, cls, verb, path_params, base_path):
        """
        returns a list of paths for the verb received as parameter.
        :param verb: a verb name. Allowed values are "get", "post", "put", "delete", "head".
        :param path_params: dictionary mapping parameters and types
        :param base_path: the resource base path
        :return: a list of tuples (path, impl), 
        where *path* is the string path to the endpoint
        and *impl* is a reference for the class resource method that implements the endpoint.
        """
        # initializes the paths list
        paths = list()

        if hasattr(cls, verb):
            method = self.get_verb(verb, cls)
            method_params = method.__params__

            # sanity check in the base_path parameters and method parameters
            p_name = [p.name for p in method_params]
            for param_name in path_params.keys():
                if param_name not in p_name:
                    raise NotImplementedError(
                        "The path parameter '{parameter}' defined on the base_path of the class '{cls}'"
                        "is not defined on the method '{method}' for the verb '{verb}'."
                        "The method '{method}' must receive all path_parameters as its parameters."
                        "".format(parameter=param_name, cls=cls.__qualname__, method=method.__qualname__, verb=verb)
                    )
            # get verb does not have body parameters
            additional_path_params, first_idx = self.__get_additional_params(cls, method_params, path_params, method)
            # dealing with default values
            if first_idx > -1:
                if first_idx == 0:
                    path = base_path
                else:
                    path = "{}/{}".format(
                        base_path,
                        "/".join(
                            [
                                additional_path_params[i][0]
                                for i in range(0, first_idx)
                            ]
                        )
                    )
                # appends the parameter to the path list
                paths.append((path, method))

                # then appends one additional path to the paths list
                # with the paths definition
                path = "{}/{}".format(
                    path,
                    "/".join(
                        [
                            additional_path_params[i][0]
                            for i in range(first_idx, len(additional_path_params))
                        ]
                    )
                )
                paths.append((path, method))
            else:  # otherwise no default values were found
                # then append builds the path and appends to the list
                if len(additional_path_params) > 0:
                    path = base_path + "/" + "/".join(
                        [
                            additional_path_params[i][0]
                            for i in range(0, len(additional_path_params))
                        ]
                    )
                else:
                    path = base_path
                paths.append((path, method))

        return paths

    def __get_additional_params(self, cls, method_params, params, method):
        additional_path_params = list()
        first_default_idx = -1
        # parameters[0] must be the self attribute
        start_index = 1
        # if the verb is NOT get and the first method parameter is
        # a subclass of ApiModel (is a body definition)
        if (
                method.__name__ != "get"
                and len(method_params) > 1
                and method_params[1].annotation is not inspect._empty
                and issubclass(method_params[1].annotation,(ApiModel,))
        ):
            # then the start_index must be 2
            start_index = 2
        # for each parameter defined on the verb method
        for i in range(start_index, len(method_params)):
            # get argument name, default value and type
            name = method_params[i].name
            default = method_params[i].default
            annotation = method_params[i].annotation
            # check whether the parameter is not defined on the base_path
            if name not in params:
                # builds the last part of the path
                p = "{" + name + "}"
                t = None
                d = None
                if annotation is not inspect._empty:
                    # gets the parameter type
                    param_type = annotation.__name__.lower()
                    # sanity check on the parameters allowed types
                    if param_type not in self.TYPE_MAP:
                        raise TypeError(
                            "Invalid path parameter annotation in the following method: {} \n"
                            "\t The parameter named '{}' must be one of the following types: {}"
                            "".format(method.__qualname__, name, self.TYPE_MAP.keys())
                        )
                    else:  # parameter's type is allowed
                        # translate the param type to the swagger format
                        t = self.TYPE_MAP[param_type]
                else:
                    # otherwise annotation is empty
                    # and then the parameter type is string
                    t = "string"
                # if the parameter has a default value
                if default is not inspect._empty:
                    # then
                    d = default
                    if first_default_idx < 0:
                        first_default_idx = len(additional_path_params)
                # appends the tuple formed by (param_name, param_type, param_default_value)
                additional_path_params.append((p, t, d))
        # returns the list of new parameters and the index of the first parameters that has a default value
        return additional_path_params, first_default_idx

    def build_param_spec(self, p, impl, base_params):
        # parameter spec
        pspec = dict()
        pspec['name'] = p.name
        pspec['description'] = impl.__pdoc__.params[p.name]
        if p.default is inspect._empty or p.name in base_params:
            pspec["required"] = True
        else:
            pspec["required"] = False
        # if it is the body parameter
        if issubclass(p.annotation, ApiModel):
            pspec["in"] = "body"
            pspec["schema"] = {"$ref": "#/definitions/{}".format(p.annotation.__name__)}
        else:  # otherwise is a path parameter
            pspec["in"] = "path"
            if p.annotation is inspect._empty:
                pspec["type"] = "string"
            else:
                # maps to swagger typing name convention
                pspec["type"] = self.TYPE_MAP[p.annotation.__name__]
        return pspec
