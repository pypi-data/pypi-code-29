# -*- coding: utf-8 -*-

import inspect
import functools
import copy
from webob import Request

from sf_apidesc.paramchecker.checkparam import Judge
from sf_apidesc.paramchecker.types import filter_inner_type, Mapper
from sf_apidesc.paramchecker.metatype import CHECKER_TAG, MetaObject
from sf_apidesc.paramchecker import runexc as exc
from sf_libs.version import is_beta_version


# 单测环境打不开/sf/version，认为是beta版本进行返回值检查
try:
    _IS_BETA_VERSION = is_beta_version()
except IOError:
    _IS_BETA_VERSION = True


def is_func_registered(func):
    """Return the function weather is registered"""
    return inspect.isfunction(func) and CHECKER_TAG in func.__dict__


def register(func):
    """Register the function which not registered. if registered
    return the checker"""
    if is_func_registered(func):
        return func.__dict__[CHECKER_TAG]
    else:
        new_checker = FuncChecker(func)
        func.__dict__[CHECKER_TAG] = new_checker
        return new_checker


class FuncChecker(object):
    # 一般函数
    NORMAL_METHOD = 0
    # 类方法函数
    CLASS_METHOD = 1
    # phoenix框架服务端的restful api接口函数
    PHOENIX_CONTROLLER = 2

    def __init__(self, func):
        func_args = inspect.getargspec(func)
        self.method_flag = self.NORMAL_METHOD
        self.kwargsname = None
        self._param_names = func_args.args
        # 单独用一个变量保存所有变量名(**body, req.param)，用于生成文档
        self._doc_param_names = []
        self.param_defs = {}
        # restful_api_action's name
        self.name = func.__name__
        self.desc = None
        self.return_type = None
        self.return_desc = None
        self.params_have_default = []
        self.req = None

        # 获取有默认参数的参数名
        default_values = func_args.defaults
        if default_values:
            default_len = len(default_values)
            # 默认参数在函数参数列表的末尾
            self.params_have_default = \
                func_args.args[-default_len:len(func_args.args)]

        if 'self' in func_args.args:
            self.method_flag = self.CLASS_METHOD

    def add_doc_param(self, param_name, param_type):
        # 添加**body 里面的参数，生成文档会用到
        self._doc_param_names.append(param_name)
        # 将mapper的两个参数放一起，生成的文档方便阅读
        if isinstance(param_type, Mapper):
            if param_type.keyname in self._doc_param_names:
                self._doc_param_names.remove(param_type.keyname)
            if param_name in self._doc_param_names:
                self._doc_param_names.remove(param_name)
            self._doc_param_names.append(param_type.keyname)
            self._doc_param_names.append(param_name)

    def add_type_check(self, param_name, param_type, param_desc, required=True,
                       nullable=False):
        """
        添加入参检测， 对于有默认值的参数需要
        :param param_name: 参数名称
        :param param_type: 参数类型
        :param param_desc: 参数描述
        :param required: 是否必填
        :param nullable: 是否可以为空
        :return:
        """
        self.add_doc_param(param_name, param_type)
        if param_name in self.params_have_default:
            required = False
        param_type = filter_inner_type(param_type)
        if isinstance(param_type, Mapper):
            param_type.set_valuename(param_name)
        self.param_defs[param_name] = MetaObject(type=param_type,
                                                 desc=param_desc,
                                                 required=required,
                                                 nullable=nullable)

    def add_desc(self, desc):
        self.desc = desc

    def add_ret(self, r_type, desc):
        """
        添加返回值检测
        :param r_type: 返回值类型
        :param desc: 返回值描述
        :return:
        """
        r_type = filter_inner_type(r_type)
        r_type.set_return_type(True)
        self.return_type = MetaObject(type=r_type,
                                      desc=desc)
        self.return_desc = desc

    def get_elem_def(self, param_name):
        if param_name in self.param_defs:
            return self.param_defs[param_name]

    def get_req_args(self, args):
        """过滤self参数和Request参数， 并获取req.param"""
        if len(args) >= 2 and isinstance(args[1], Request):
            # 如果第二个参数是Request类型, 忽略检测
            self.method_flag = self.PHOENIX_CONTROLLER
            return args[2:], dict(args[1].params)
        if self.method_flag == self.CLASS_METHOD:
            # 如果第一个参数是self, 忽略检测
            return args[1:], {}
        else:
            return args[:], {}

    @property
    def param_names(self):
        """
        获取需要检测参数名称，不包括self参数和Request参数
        :return:
        """
        if self.method_flag == self.PHOENIX_CONTROLLER:
            return self._param_names[2:]
        elif self.method_flag == self.CLASS_METHOD:
            return self._param_names[1:]
        return self._param_names

    @property
    def doc_param_names(self):
        return self._doc_param_names


def register_param(checker, param_schema):
    """
    Register param's type and description

    :param checker:
    :param param_schema:
    :return:
    """
    if not isinstance(param_schema, dict):
        raise exc.SchemaFormatError("schema.param should be dict")

    for param_name, schema in param_schema.items():
        if not isinstance(schema, tuple):
            raise exc.SchemaFormatError("schema.param format error")

        checker.add_type_check(param_name, *schema)


def register_desc(checker, description):
    """
    Register function's description of restful api .

    :param checker:
    :param description: string
    :return:
    """
    if not isinstance(description, (str, unicode)):
        raise exc.SchemaFormatError("schema.desc should be string")

    checker.add_desc(description)


def register_return(checker, return_def):
    """
    Register return type and description

    :param checker:
    :param return_def:
    :return:
    """
    if not isinstance(return_def, tuple):
        raise exc.SchemaFormatError("schema.return should be tuple(2)")

    return_type, return_desc = return_def

    checker.add_ret(return_type, return_desc)


SCHEMA_HANDLE = {
    'param': register_param,
    'return': register_return,
    'desc': register_desc
}


def schema(pattern):
    api_schema_pattern = pattern

    def decorator(func):
        checker = register(func)

        if not isinstance(api_schema_pattern, dict):
            raise exc.SchemaFormatError("schema should be dict")

        # register parameter, return type and description of restful api
        for key, value in api_schema_pattern.items():
            if key not in SCHEMA_HANDLE:
                raise exc.SchemaFormatError(
                    'schema attrs should in [ param, return, desc]')
            # register every element in pattern
            SCHEMA_HANDLE[key](checker, value)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # check parameter value
            validate_input(args, kwargs, checker)

            result = func(*args, **kwargs)

            # 发布版本去掉返回值检查
            if _IS_BETA_VERSION:
                # check return value
                try:
                    return_type = checker.return_type
                    validate_output(return_type, result)
                except exc.ValidateError as e:
                    e.code = 500
                    raise

            return result

        return wrapper

    return decorator


def validate_output(return_type, value):
    """
    检测返回值
    :param return_type: 返回值类型
    :param value: 返回值
    :return:
    """
    if return_type is None and value is None:
        return
    # if return value is not None , return in schema must exist
    if return_type is None and value is not None:
        raise exc.ValidateError("miss return type define in schema ")
    value = {'return': value}
    validate_with_exception_info(return_type, value, 'return', isoutput=True)


def combine_args(args, kwargs, checker):
    """
    将函数参数名称与参数值进行组合
    :param args: 位置参数值
    :param kwargs: 键值对参数值
    :param checker:
    :return:
    """
    args, req_params = checker.get_req_args(args)
    kwargs = copy.deepcopy(kwargs)

    # todo this only fit phoenix
    args_value = args
    param_names = checker.param_names

    # combine args and kwargs and req.params
    args = dict(zip(param_names, args_value))
    if kwargs:
        args.update(kwargs)

    #  参数名和其他参数名不能冲突
    intersection = set(req_params.keys()) & set(args.keys())
    if intersection:
        raise exc.ValidateError(
            "req.params names : %s conflict with others" % list(
                intersection))
    args.update(req_params)

    return args


def validate_input(args, kwargs, checker):
    """
    检测入参
    :param args:位置参数值
    :param kwargs:键值对参数值
    :param checker:参数检测对象
    :return:
    """
    args_dict = combine_args(args, kwargs, checker)

    # 所有入参必须在schema中有注册
    param_names = checker.param_names
    for param_name in param_names:
        if param_name not in checker.param_defs:
            raise exc.VisibleExUnknownArgument(argname=param_name)

    # 所入参必须在schema中有注册
    for param_name in checker.param_defs:

        param_def = checker.get_elem_def(param_name)
        if not param_def:
            raise exc.VisibleExUnknownArgument(argname=param_name)
        validate_with_exception_info(param_def, args_dict, param_name)

    # 检查所入参是否检测到
    for arg_name in args_dict:
        if arg_name not in checker.param_defs:
            raise exc.VisibleExUnknownArgument(arg_name)


def validate_with_exception_info(param_def, dict_param, param_name,
                                 isoutput=False):
    """
    参数检测入口，提供异常信息的处理
    :param param_def: 参数定义
    :param dict_param: 参数所在的字典结构
    :param param_name:参数名
    :return:
    """
    judge = Judge(isoutput=isoutput)
    try:
        judge.check_typedef(param_def, dict_param, param_name)
    except (exc.VisibleExInvalidInput,
            exc.VisibleExMissingArgument,
            exc.VisibleExUnknownArgument):
        raise
    except Exception as e:
        param_value = dict_param[param_name]
        raise exc.VisibleExInvalidInput(field=param_name,
                                        value=param_value,
                                        expect_cls=None,
                                        error=e)
