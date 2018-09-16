# -*- coding: utf-8 -*-

import inspect
import six
from sf_apidesc.paramchecker import runexc as exc
from sf_apidesc.paramchecker.types import filter_inner_type, Mapper

CHECKER_TAG = '_phoenix_checker'


class MetaObject(object):
    """
    属性元类，动态设置属性，初始化只能输入键值对
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def isregistered(cls):
    return inspect.isclass(cls) and hasattr(cls, CHECKER_TAG)


def register(cls):
    if isregistered(cls):
        return getattr(cls, CHECKER_TAG)
    else:
        new_checker = PhoenixChecker(cls)
        setattr(cls, CHECKER_TAG, new_checker)
        return new_checker


def unregister(cls):
    if isregistered(cls):
        checker = getattr(cls, CHECKER_TAG)
        delattr(cls, CHECKER_TAG)
        return checker


class PhoenixChecker(object):

    def __init__(self, cls):
        # all attribute name
        self.attr_names = []
        # map attribute name to typedef
        self.attr_defs = {}
        self.name = cls.__name__
        # class description
        self.desc = None

        # store maptype
        self.mappers = {}
        # store maptype's value tag in json
        self.data = []

    def add_typedef(self, argtag, datatype, desc, required=True,
                    nullable=False):
        """
        定义一个数据字段的名称，类型，描述，是否必填和默认值

        :param argtag: str
        :param datatype:
        :param desc: str
        :param required:
        :param nullable:
        :return:
        """
        self.attr_names.append(argtag)
        datatype = filter_inner_type(datatype)
        if isinstance(datatype, Mapper):
            datatype.set_valuename(argtag)
        self.attr_defs[argtag] = MetaObject(type=datatype, desc=desc,
                                            required=required,
                                            nullable=nullable)

    def add_desc(self, desc):
        self.desc = desc

    def add_mapper(self, typetuple, datatuple, mapper):
        """
        定义一个映射类型

        :param typetuple: tuple
        :param datatuple: tuple
        :param mapper: dict
        :return:None
        """
        from sf_apidesc.paramchecker.types import Enum, Mapper
        keyname = typetuple[0]
        keydesc = typetuple[1]
        valuename = datatuple[0]
        valuedesc = datatuple[1]
        enum_type = Enum(*mapper.keys())
        self.add_typedef(keyname, enum_type, keydesc, {'required': True})
        mapper_object = Mapper(keyname, mapper)
        mapper_object.set_valuename(valuename)
        self.add_typedef(valuename, mapper_object, valuedesc,
                         {'required': True})

        self.data.append(keyname)

    def get_elem_def(self, attr_name):
        """
        获取该字段类型定义。 非映射类型返回类型定义；映射类型，如果是key返回枚举类型，
        如果是value则返回key字段所指类型

        :param jdata: 输入数据
        :param attr_name: 字段名称
        :return:
        """

        if attr_name in self.attr_defs:
            return self.attr_defs[attr_name]


class _BaseMeta(type):
    """
    metaclass
    """

    def __init__(cls, name, bases, dct):
        if bases and bases[0] is MetaType:
            checker = unregister(bases[0])
            setattr(cls, CHECKER_TAG, checker)
            setattr(cls, '_return_type', False)
            if checker:
                checker.name = name


class MetaType(six.with_metaclass(_BaseMeta)):
    """
    暂存子类的属性
    """

    def __init__(self):
        pass

    @classmethod
    def set_return_type(cls, value):
        setattr(cls, '_return_type', value)

    @classmethod
    def get_return_type(cls):
        return getattr(cls, '_return_type')

    @classmethod
    def tostring(cls):
        return cls.__name__


def CHECK(argtag, *args, **kwargs):
    """
    注册参数检测
    :param argtag: 字段名或者字段类型
    :param args: 如果argtag是字段名, args长度是二：字段类型和字符串；如果是字段类型，args
                 长度是一：描述字符串
    :param kwargs: required=True, nullable=False:
    :return:
    """
    # FIXME: 多线程下动态import可能有问题
    requried = kwargs.get('required', True)
    nullable = kwargs.get('nullable', False)
    if isinstance(argtag, str):
        # 在class中使用
        datatype = args[0]
        desc = args[1]
        checker = register(MetaType)
        try:
            checker.add_typedef(argtag, datatype, desc, **kwargs)
        except Exception as e:
            unregister(MetaType)
            raise e
    else:
        # 在param中使用
        datatype = args[0]
        return (argtag, datatype, requried, nullable)


def MULTICHECK(mapdef):
    if not isinstance(mapdef, dict):
        raise exc.SchemaFormatError("MULTICHECK define error")

    try:
        maptag = mapdef['key']
        datatag = mapdef['value']
        mapper = mapdef['mapper']
    except (KeyError, IndexError):
        raise exc.SchemaFormatError("MULTICHECK define error")

    if len(maptag) != 2 or len(datatag) != 2:
        raise exc.SchemaFormatError("MULTICHECK define error")

    checker = register(MetaType)
    try:
        checker.add_mapper(maptag, datatag, mapper)
    except Exception as e:
        unregister(MetaType)
        raise e


def DESC(description):
    checker = register(MetaType)
    try:
        checker.add_desc(description)
    except Exception as e:
        unregister(MetaType)
        raise e


def REQUIRED(argtag, *args, **kwargs):
    kwargs['required'] = True
    kwargs['nullable'] = False
    return CHECK(argtag, *args, **kwargs)


def OPTIONAL(argtag, *args, **kwargs):
    kwargs['required'] = False
    kwargs['nullable'] = False
    return CHECK(argtag, *args, **kwargs)
