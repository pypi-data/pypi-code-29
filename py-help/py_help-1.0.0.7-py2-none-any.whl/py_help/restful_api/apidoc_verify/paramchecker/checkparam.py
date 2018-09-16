# -*- coding: utf-8 -*-
from sf_apidesc.paramchecker.metatype import _BaseMeta, CHECKER_TAG
from sf_apidesc.paramchecker import runexc as exc
from sf_apidesc.paramchecker.types import UserType, NullType, NoneType, Any, \
    Mapper
from sf_apidesc.i18n import _

PASS = True
NULL_T = (NullType, NoneType)


def check_required(typedef, value, key):
    if key not in value:
        if typedef.required:
            raise exc.VisibleExMissingArgument(argname=key, value=value)
        else:
            return PASS


def check_nullable(typedef, value, key):
    if value[key] is not None:
        # 不能PASS，PASS是不进行类型检查
        return

    # typedef.type是instance
    def check_anytype_null(type_def):
        if isinstance(type_def, Any):
            for type_itme in type_def.expect_types:
                if type_itme in NULL_T:
                    return True
    # Any 里面可能有NullType or NoneType
    if check_anytype_null(typedef.type):
        return PASS

    # Mapper 里面可能有NullType or NoneType or Any(NullType, xx)
    if isinstance(typedef.type, Mapper):
        for type_item in typedef.type.mapper.values():
            if type_item in NULL_T or check_anytype_null(type_item):
                # 不返回PASS, 后续还需要检测Mapper对应字段是否一定是None
                return

    if typedef.type in NULL_T:
        return PASS

    if typedef.nullable:
        return PASS

    raise exc.VisibleExInvalidInput(field=key,
                                    value=value,
                                    expect_cls=typedef,
                                    error=_(u'%s不能为null') % key)


CHECK_ITEM = [check_required, check_nullable]


class Judge(object):

    def __init__(self, isoutput=False):
        self.isoutput = isoutput

    def check_typedef(self, typedef, value, key):
        """
        对参数定义项进行检测, 如nullable required
        :param typedef:
        :param value:
        :param key:
        :return:
        """
        for item in CHECK_ITEM:
            if item(typedef, value, key) == PASS:
                return

        datatype = typedef.type
        if isinstance(datatype, _BaseMeta):
            self.check_complex_type(datatype, value[key])
        elif isinstance(datatype, UserType):
            datatype.set_judge(self)
            datatype.type_check(value, key)

    # todo 用户自定义类和字典类统一提供validate接口方法
    def verification(self, datatype, value):
        if isinstance(datatype, _BaseMeta):
            self.check_complex_type(datatype, value)
        else:
            datatype.set_judge(self)
            datatype.verification(value)

    def check_complex_type(self, datatype_def, jdata):
        """
        检测json类型
        :param datatype_def:
        :param jdata:
        :return:
        """
        if not isinstance(jdata, dict):
            raise exc.ValidateError(_(u'参数格式错误'))
        checker = getattr(datatype_def, CHECKER_TAG)
        for attr_name in checker.attr_names:
            # get type
            attr_def = checker.get_elem_def(attr_name)

            try:
                self.check_typedef(attr_def, jdata, attr_name)
            except (exc.VisibleExInvalidInput,
                    exc.VisibleExMissingArgument,
                    exc.VisibleExUnknownArgument):
                raise
            except Exception as e:
                if e.__class__.__name__.startswith('VisibleEx'):
                    raise exc.VisibleExInvalidInput(field=attr_name,
                                                    value=jdata,
                                                    expect_cls=attr_def.type,
                                                    error=e)
                else:
                    raise exc.VisibleExInvalidInput(field=attr_name,
                                                    value=jdata,
                                                    expect_cls=attr_def.type,
                                                    error=_(u'参数错误'))

        # values in json but not in class
        extra_value = []
        for key in jdata:
            if key not in checker.attr_names:
                extra_value.append(key)
        if extra_value:
            raise exc.VisibleExUnknownArgument(argname=extra_value)
        return jdata
