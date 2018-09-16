# -*- coding: utf-8 -*-

import abc
import inspect
import random
import re
import string
import uuid
import webob
from datetime import datetime

import netaddr
from dateutil.parser import parse as datetime_parse

from sf_apidesc.i18n import _
from sf_apidesc.paramchecker import runexc as exc
from sf_libs.string import ltrim


class UserType(object):
    name = None
    whitespace = tuple(string.whitespace)

    def __init__(self):
        self.judge = None

    def type_check(self, jdata, key):
        self.verification(jdata[key])

    def verification(self, value):
        # 如果字符串前后包含空字符报错
        if type(value) in (str, unicode):
            if value.endswith(self.whitespace) or value.startswith(
                    self.whitespace):
                raise exc.VisibleExInvalidInput(_(u'请去掉输入两端的空格'))
            # 检测四个字的utf-8编码特殊字符：💩💩💩💩💩💩💩💩💩
            # MySQL的utf-8编码并不支持4个字符的utf-8编码
            # http://hao.caibaojian.com/demo/77762?a=detail
            utf8_str = value.encode('utf-8') \
                if isinstance(value, unicode) else value
            for c in utf8_str:
                if ord(c) >= 0xF0:
                    raise exc.VisibleExInvalidInput(_(u'不支持输入特殊字符'))

        if self.judge.isoutput:
            self.validate_output(value)
        else:
            self.validate(value)

    def set_judge(self, judge):
        self.judge = judge

    @abc.abstractmethod
    def validate(self, value):
        pass

    @abc.abstractmethod
    def sample(self):
        # 文档中显示的示例
        pass

    @abc.abstractmethod
    def tostring(self):
        # 文档中显示的类型
        pass

    @abc.abstractmethod
    def set_return_type(self, value):
        # 与MetaType方法兼容
        pass

    def validate_output(self, value):
        # 与MetaType方法兼容
        self.validate(value)


class IntegerType(UserType):
    """
    A simple integer type. Can validate a value range.

    :param minimum: Possible minimum value
    :param maximum: Possible maximum value

    Example::

        Price = IntegerType(minimum=1)

    """
    name = "Integer"

    allows_types = (int, long)

    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, value):

        if not isinstance(value, self.allows_types):
            raise exc.VisibleExValueError(_(u'值必须是数字'))

        if self.minimum is not None and value < self.minimum:
            error = _(u'值必须大于等于%s') % self.minimum
            raise exc.VisibleExValueError(error)

        if self.maximum is not None and value > self.maximum:
            error = _(u'值必须小于等于%s') % self.maximum
            raise exc.VisibleExValueError(error)

    def sample(self):
        min_value = self.minimum if self.minimum is not None else 0
        max_value = self.maximum if self.maximum is not None else min_value + 2
        if min_value == max_value:
            return min_value
        return random.randrange(min_value, max_value)

    def tostring(self):
        if self.minimum is None and self.maximum is None:
            return "%s" % self.name
        return "%s : [%s, %s]" % (self.name, self.minimum, self.maximum)


class FloatType(IntegerType):
    """
    A simple float type. Can validate a value range.

    :param minimum: Possible minimum value
    :param maximum: Possible maximum value

    Example::

        Price = FloatType(minimum=1)

    """
    name = "Float"

    allows_types = (int, long, float)


class _StringType(UserType):
    """
    A simple string type. Can validate a value range.

    :param minlen: Possible minlen value
    :param maxlen: Possible maxlen value

    Example::

        Price = StringType(minlen=1, maxlen=9)

    """
    name = "String"
    sample_str = "sample string"
    sample_max_len = len(sample_str)

    def __init__(self, minlen=None, maxlen=None):
        self.minlen = minlen
        self.maxlen = maxlen

    def validate(self, value):

        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(_(u'值必须是字符串'))

        # 中文字符按3字节算
        str_len = len(value.encode('utf-8')) \
            if isinstance(value, unicode) else len(value)

        if self.minlen is not None and str_len < self.minlen:
            error = _(u'字符串长度必须大于等于%s') % self.minlen
            raise exc.VisibleExValueError(error)

        if self.maxlen is not None and str_len > self.maxlen:
            error = _(u'字符串长度必须小于等于%s') % self.maxlen
            raise exc.VisibleExValueError(error)

    def validate_output(self, value):
        # 由于其他平台（hci,vmware）的输入, 与aCMP限制不匹配
        # string 类型的返回值只做简单检测
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(_(u'值必须是字符串'))

    def sample(self):
        if self.minlen is None and self.maxlen is None:
            sample_str = self.sample_str
        else:
            min_len = self.minlen if self.minlen is not None else 0
            max_len = self.maxlen if self.maxlen is not None else min_len + 2
            if min_len == max_len:
                str_len = min_len
            else:
                str_len = random.randrange(min_len, max_len)

            sample_len = min(self.sample_max_len, str_len)
            sample_num = sample_len / len(self.sample_str) + 1
            sample_str = (self.sample_str * sample_num)[0:sample_len]
        return sample_str

    def tostring(self):
        if self.minlen is None and self.maxlen is None:
            return "%s" % self.name
        return "%s : [%s, %s]" % (self.name, self.minlen, self.maxlen)


class NameString(_StringType):
    name = "NameString"

    def __init__(self, minlen=1, maxlen=100):
        super(NameString, self).__init__(minlen, maxlen)

    def validate(self, value):
        super(NameString, self).validate(value)
        if not value:
            return
        pattern = u"[\.\(\)\[\]\{\}（）【】｛｝@\d\u4E00-\u9FA5a-zA-Z_+|\-\s]+$"
        if not re.match(pattern, u"%s" % value):
            error = _(u"名称只能由中文、数字、字母、()[]{}（）【】｛｝@|._-+以及空格组成")  # noqa: E501
            raise exc.VisibleExValueError(error)


class ContentString(_StringType):
    name = "ContentString"

    def __init__(self, minlen=0, maxlen=100):
        super(ContentString, self).__init__(minlen, maxlen)


class DescString(_StringType):
    name = "DescriptionString"

    def __init__(self, minlen=0, maxlen=100):
        super(DescString, self).__init__(minlen, maxlen)

    def verification(self, value):
        # UserType默认不允许传入空格，Description需要重写放通这个限制
        super(DescString, self).verification(value.strip(' \t\r\n'))


class NullString(_StringType):
    name = "NullString"

    def __init__(self):
        super(NullString, self).__init__(0, 0)


class PasswordString(_StringType):
    name = "Password"

    def __init__(self, minlen=8, maxlen=64):
        super(PasswordString, self).__init__(minlen, maxlen)

    def validate(self, value):
        error = _(u"密码最短为%(minlen)s个字符，最长为%(maxlen)s个字符；"
                  u"且至少应包含大写字母、小写字母、数字和特殊字符中的两项，"
                  u"特殊字符支持~`@#%%&<>\"',;_-^$.*+?=!:|{}()[]/\\") \
            % {'minlen': self.minlen, 'maxlen': self.maxlen}
        super(PasswordString, self).validate(value)
        pattern = u"[~`@#%&<>\"',;_\-\^\$\.\*\+\?=!:|{}()\[\]/\\a-zA-Z0-9_]+$"
        if not re.match(pattern, u"%s" % value):
            raise exc.VisibleExValueError(error)


class IntegerString(UserType):
    """
    整形类型的字符串
    """
    name = "IntegerString"
    stringtype = _StringType()

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.integetype = IntegerType(min_value, max_value)

    def validate(self, value):
        self.stringtype.validate(value)
        errmsg = _(u'值必须为整型字符')
        try:
            # 字符串转换为整形，如果包含非数字字符串会报错
            integer_value = int(value)
        except ValueError:
            raise exc.VisibleExValueError(errmsg)
        self.integetype.validate(integer_value)

    def sample(self):
        return str(self.integetype.sample())

    def tostring(self):
        if self.min_value is None and self.max_value is None:
            return "%s" % self.name
        return "%s : [%s, %s]" % (self.name, self.min_value, self.max_value)


class FloatString(UserType):
    """
    浮点类型的字符串，包括整型，浮点，科学计数法
    """
    name = "FloatString"
    stringtype = _StringType()

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.floattype = FloatType(min_value, max_value)

    def validate(self, value):
        self.stringtype.validate(value)
        errmsg = _(u'值必须为浮点数字符')
        try:
            # 字符串转换为浮点数，如果包含非数字字符串会报错
            float_value = float(value)
        except ValueError:
            raise exc.VisibleExValueError(errmsg)
        self.floattype.validate(float_value)

    def sample(self):
        return str(self.floattype.sample())

    def tostring(self):
        if self.min_value is None and self.max_value is None:
            return "%s" % self.name
        return "%s : [%s, %s]" % (self.name, self.min_value, self.max_value)


G_StringType = _StringType()
G_IntegerType = IntegerType()
G_FloatType = FloatType()


def filter_inner_type(datatype):
    """
    将内置类型转换为UserType
    :param datatype:
    :return:
    """
    if datatype in (int, long):
        return G_IntegerType

    if datatype == unicode:
        return G_StringType

    if datatype == float:
        return G_FloatType

    if datatype == datetime:
        return Datetime

    if isinstance(datatype, list):
        return ListType(datatype[0])
    from sf_apidesc.paramchecker.metatype import _BaseMeta
    if isinstance(datatype, (_BaseMeta, UserType)):
        return datatype
    # 注册时暴露类型{} str等类型错误
    raise exc.ValidateError("type %s do not allowed" % datatype)


class _MapperDict(dict):

    def __str__(self):
        # 为dict定制打印格式

        s = "{" + ", ".join("%r: %r" % (key, self[key].tostring()) for key
                            in sorted(self, reverse=True)) + "}"
        return 'Mapper(%s)' % s


class Mapper(UserType):
    name = 'Mapper'

    def __init__(self, keyname, mapper):
        """

        :param mapper:
        :param keyname:
        """
        for key, value in mapper.items():
            mapper[key] = filter_inner_type(value)
        self.mapper = _MapperDict(mapper)
        self.keyname = keyname
        self.valuename = None

    def set_valuename(self, valuename):
        self.valuename = valuename

    def type_check(self, jdata, key):
        self.validate(jdata)

    def sample(self):
        keys = self.mapper.keys()
        return self.mapper[keys[0]]

    def tostring(self):
        return self.mapper

    def validate(self, value):
        # 判断是映射类型
        key = value[self.keyname]
        if key in self.mapper:
            self.judge.verification(self.mapper[key], value[self.valuename])
        else:
            raise exc.VisibleExMissingArgument(argname=key, value=value)


class ListType(UserType):
    name = 'List'

    def __init__(self, elemtype, minlen=None, maxlen=None):
        self.elemtype = filter_inner_type(elemtype)
        self.maxlen = maxlen
        self.minlen = minlen

    def validate(self, value):
        if not isinstance(value, list):
            raise exc.VisibleExValueError(_(u'值必须是列表'))

        if self.minlen is not None and len(value) < self.minlen:
            error = _(u'元素个数必须大于%s') % self.minlen
            raise exc.VisibleExValueError(error)

        if self.maxlen is not None and len(value) > self.maxlen:
            error = _(u'元素个数必须小于%s') % self.maxlen
            raise exc.VisibleExValueError(error)

        for elem in value:
            self.judge.verification(self.elemtype, elem)

    def sample(self):
        return self.elemtype

    def tostring(self):
        return "[%s]" % self.elemtype.tostring()

    def set_return_type(self, value):
        self.elemtype.set_return_type(value)


class SeriesType(ListType):
    name = 'Series'

    def __init__(self, elemtype, separator=',', minlen=None, maxlen=None):
        super(SeriesType, self).__init__(elemtype,
                                         minlen=minlen, maxlen=maxlen)
        self.separator = separator

    def validate(self, value):
        if not isinstance(value, (unicode, str)):
            raise exc.ValidateError(_(u'值必须是字符串，存在多个数据时使用%s拼接')
                                    % self.separator)
        values = value.split(self.separator)
        return super(SeriesType, self).validate(values)

    def sample(self):
        values = [
            str(self.elemtype.sample()),
            str(self.elemtype.sample()),
            str(self.elemtype.sample())
        ]
        return self.separator.join(values)

    def tostring(self):
        values = [
            self.elemtype.tostring(),
            self.elemtype.tostring(),
            self.elemtype.tostring()
        ]
        return self.separator.join(values)


class Any(UserType):
    name = 'Any'

    def __init__(self, *args):
        from sf_apidesc.paramchecker.metatype import MetaType
        len_errmsg = _(u'必须指定两种或以上的类型')
        type_errmsg = _(u'类型必须是UserType子类')
        # 长度必须大于零
        if not len(args) or len(args) < 2:
            raise exc.SchemaFormatError(len_errmsg)
        self.expect_types = []
        dict_class_count = 0
        # 必须是UserType子类
        for type_item in args:
            type_item = filter_inner_type(type_item)
            self.expect_types.append(type_item)
            if isinstance(type_item, UserType):
                continue
            if issubclass(type_item, MetaType):
                dict_class_count += 1
                if dict_class_count > 1:
                    raise exc.SchemaFormatError(type_errmsg)
                continue
            raise exc.SchemaFormatError(type_errmsg)

    def type_check(self, jdata, key):
        from sf_apidesc.paramchecker.metatype import MetaType
        # 覆盖type_check方法, 可以嵌套Mapper类型
        validated = False
        for type_item in self.expect_types:
            try:
                if inspect.isclass(type_item) \
                        and issubclass(type_item, MetaType):
                    self.judge.check_complex_type(type_item, jdata[key])
                else:
                    type_item.set_judge(self.judge)
                    type_item.type_check(jdata, key)
                validated = True
                break
            except Exception:
                pass

        if not validated:
            raise exc.VisibleExValueError(_(u'参数类型错误'))

    def validate(self, value):
        pass

    def sample(self):
        return self.expect_types[0]

    def tostring(self):
        type_names = []
        for t in self.expect_types:
            type_names.append(str(t.tostring()))
        return "Any type in [%s]" % (", ".join(type_names))


class _VmID(UserType):
    """
    VMID type.
    """
    name = "VMID"
    min_value = 100
    max_value = 8796093022207
    int_range = IntegerType(min_value, max_value)

    def validate(self, value):
        errmsg = _(u'值必须是VMID')
        if isinstance(value, (str, unicode)) and value.isdigit():
            return self.int_range.validate(int(value))
        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return str(self.int_range.sample())

    def tostring(self):
        return "%s" % self.name


VmID = _VmID()


class _IPv4AddressType(UserType):
    """
    IPv4 type.
    """
    name = "IPv4"

    def validate(self, value):
        error = _(u'值必须是IP')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(error)

        try:
            netaddr.IPAddress(value, version=4, flags=netaddr.INET_PTON)
        except netaddr.AddrFormatError:
            raise exc.VisibleExValueError(error)

    def sample(self):
        return "1.1.1.1"

    def tostring(self):
        return "%s" % self.name


IPv4Type = _IPv4AddressType()


class _IPv6AddressType(UserType):
    """
    IPv6 type.

    This type represents IPv6 addresses in the short format.
    """
    name = "IPv6"

    def validate(self, value):
        error = _(u'值必须是IP')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(error)

        try:
            netaddr.IPAddress(value, version=6, flags=netaddr.INET_PTON)
        except netaddr.AddrFormatError:
            raise exc.VisibleExValueError(error)

    def sample(self):
        return "0:0:0:0:0:ffff:192.1.56.10"

    def tostring(self):
        return "%s" % self.name


IPv6Type = _IPv6AddressType()


class _PortType(UserType):
    """
    Port type.
    """
    name = "Port"
    min_value = 0
    max_value = 65535
    value_type = IntegerType(min_value, max_value)

    def validate(self, value):
        self.value_type.validate(value)

    def sample(self):
        return 443

    def tostring(self):
        return "%s : [%s, %s]" % (self.name, self.min_value, self.max_value)


PortType = _PortType()


class _UuidType(UserType):
    """
    UUID type.

    This type allows not only UUID having dashes.
    For example, '6a0a707c-45ef-4758-b533-e55adddba8ce'
    """
    name = "UUID"

    def validate(self, value):
        error = _(u'值必须是UUID格式')
        if len(value) != len("6a0a707c-45ef-4758-b533-e55adddba8ce"):
            raise exc.VisibleExValueError(error)
        try:
            uuid.UUID(value)
        except (TypeError, ValueError, AttributeError):
            raise exc.VisibleExValueError(error)

    def sample(self):
        return "6a0a707c-45ef-4758-b533-e55adddba8ce"

    def tostring(self):
        return "%s" % self.name


UUIDType = _UuidType()


class _UuidNoDash(UserType):
    """
    UUID type.

    This type allows not only UUID having dashes without dash.
    For example, '6a0a707c45ef4758b533e55adddba8ce'
    """
    name = "UUIDNoDash"

    def validate(self, value):
        error = _(u'值必须是不带横杆的UUID格式')
        if len(value) != len("6a0a707c45ef4758b533e55adddba8ce"):
            raise exc.VisibleExValueError(error)
        try:
            uuid.UUID(value)
        except (TypeError, ValueError, AttributeError):
            raise exc.VisibleExValueError(error)

    def sample(self):
        return "6a0a707c45ef4758b533e55adddba8ce"

    def tostring(self):
        return "%s" % self.name


UUIDNoDash = _UuidNoDash()


class _UniqueID(UserType):
    name = "UniqueID"

    def validate(self, value):
        error = _(u'值必须是能保证唯一的字符串')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(error)

        length = len(value)
        # HCI的存储ID有46字符
        if length == 0 or length > 50:
            raise exc.VisibleExValueError(error)

        for c in str(value):
            if not (c.isalpha() or c.isdigit() or c in ('-', '_')):
                raise exc.VisibleExValueError(error)

    def sample(self):
        return "xxxxxxxxxxxxxx"

    def tostring(self):
        return "%s" % self.name


UniqueID = _UniqueID()


class _Datetime(UserType):
    """
    Datetime Type.

    This type allows datetime string of ios format. For example,
    '2017-11-13T19:05:07.824000'
    """
    name = 'Datetime'

    def validate(self, value):
        error = _(u'值必须是日期格式')
        if isinstance(value, datetime):
            return True

        try:
            datetime_parse(value)
        except Exception:
            raise exc.VisibleExValueError(error)

    def sample(self):
        return '2017-11-13T19:05:07.824000'

    def tostring(self):
        return "%s" % self.name


Datetime = _Datetime()


class _DateString(UserType):
    name = 'DateString'

    def validate(self, value):
        error = _(u'值必须是日期格式')
        if isinstance(value, (str, unicode)) \
                and re.match('\d\d\d\d-\d\d-\d\d$', value):
            try:
                datetime_parse(value)
            except Exception:
                raise exc.VisibleExValueError(error)
            return True
        raise exc.VisibleExValueError(error)

    def sample(self):
        return '2018-12-30'

    def tostring(self):
        return "%s" % self.name


DateString = _DateString()


class _TimeString(UserType):
    name = 'TimeString'

    def validate(self, value):
        if isinstance(value, (str, unicode)) \
                and re.match('\d\d:\d\d:\d\d$', value):
            hour, min, sec = value.split(':')
            if (int(hour) >= 0 and int(hour) < 24) and \
                    (int(min) >= 0 and int(min) < 60) and \
                    (int(sec) >= 0 and int(sec) < 60):
                return True
        raise exc.VisibleExValueError(_(u'值必须是时间格式'))

    def sample(self):
        return '23:59:59'

    def tostring(self):
        return '%s' % self.name


TimeString = _TimeString()


class Enum(UserType):
    """
    A simple enumeration type. Can be based on any non-complex type.

    :param values: A set of possible values

    If nullable, 'None' should be added the values set.

    Example::

        Gender = Enum('male', 'female')
        Specie = Enum('cat', 'dog')

    """
    name = 'Enum'

    def __init__(self, *values):
        self.values = values

    def validate(self, value):
        if value not in self.values:
            str_values = map(lambda a: str(a), self.values)
            error = _(u'值的取值范围：%s') % ','.join(str_values)
            raise exc.VisibleExValueError(error)
        return value

    def sample(self):
        return self.values[0]

    def tostring(self):
        str_values = map(lambda a: str(a), self.values)
        return "%s : [ %s ]" % (self.name, ', '.join(str_values))


ORDER = Enum('ASC', 'DESC')


class _TimeStamp(UserType):
    """
    Datetime Type.

    This type allows TimeStamp format. For example,
    1510626293.403
    """
    name = 'TimeStamp(GMT)'

    def validate(self, value):
        try:
            datetime.fromtimestamp(value)
        except Exception:
            raise exc.VisibleExValueError(_(u'值必须是时间戳'))

    def sample(self):
        return 1510626293

    def tostring(self):
        return "%s" % self.name


TimeStamp = _TimeStamp()


class _TimeStampString(_TimeStamp):
    """
    TimeStampString Type.

    This type allows TimeStamp String format. For example,
    '1510626293.403'
    """
    name = 'TimeStampString'
    stringtype = _StringType()

    def validate(self, value):
        self.stringtype.validate(value)

        try:
            # 字符串转换为浮点形，如果包含非数字字符串会报错
            float_value = float(value)
        except ValueError:
            errmsg = _(u'值必须是时间戳字符串')
            raise exc.VisibleExValueError(errmsg)

        super(_TimeStampString, self).validate(float_value)

    def sample(self):
        return '1510626293'

    def tostring(self):
        return "%s" % self.name


TimeStampString = _TimeStampString()


class _BoolInteger(UserType):
    name = 'Boolean'

    def validate(self, value):
        if not isinstance(value, (int, long)):
            raise exc.VisibleExValueError(_(u'值必须是0或1'))
        if value not in (0, 1):
            raise exc.VisibleExValueError(_(u'值必须是0或1'))

    def sample(self):
        return 1

    def tostring(self):
        return "%s : [0, 1]" % self.name


EnableType = _BoolInteger()
BoolInteger = _BoolInteger()


class _NullType(UserType):
    name = 'null'

    def validate(self, value):
        if value is not None:
            raise exc.VisibleExValueError(_(u'值必须是空值'))

    def sample(self):
        return self.name

    def tostring(self):
        return self.name


NullType = _NullType()
NoneType = _NullType()


class _NetmaskType(UserType):
    name = 'Netmask'

    def validate(self, value):
        errmsg = _(u'值必须是掩码')
        try:
            mask = netaddr.IPAddress(value, version=4, flags=netaddr.INET_PTON)
        except netaddr.AddrFormatError:
            raise exc.VisibleExValueError(errmsg)
        if not mask.is_netmask():
            raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return "255.255.255.0"

    def tostring(self):
        return "%s" % self.name


NetmaskType = _NetmaskType()


class _EMailType(UserType):
    name = 'EMail'

    def validate(self, value):
        if not isinstance(value, (str, unicode)) or "@" not in value:
            raise exc.VisibleExValueError(_(u'值必须是电子邮件地址'))

    def sample(self):
        return "xxxxxx@xxxxx.com"

    def tostring(self):
        return "%s" % self.name


EMailType = _EMailType()


class _VLANID(UserType):
    name = 'VLANID'

    def validate(self, value):
        # HCI上0和4095是保留的VLAN ID
        errmsg = _(u'值必须是VLANID：[1, 4094]')
        if not isinstance(value, int):
            raise exc.VisibleExValueError(errmsg)
        if value not in range(1, 4095):
            raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return 1

    def tostring(self):
        return "%s" % self.name


VLANID = _VLANID()


class _VLANIDRange(UserType):
    name = "VLANID Range"

    def _is_vlanid_string(self, str):
        return str.isdigit() and int(str) in range(1, 4095)

    def validate(self, value):
        errmsg = _(u'值必须是一个VLANID或者VLANID范围')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if value == 'all' or self._is_vlanid_string(value):
            return
        elif re.match('\d+-\d+$', value):
            seq = value.split('-')
            if self._is_vlanid_string(seq[0]) and \
                    self._is_vlanid_string(seq[1]) and \
                    int(seq[0]) < int(seq[1]):
                return

        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return '1-4094'

    def tostring(self):
        return "%s : [ 1, 1-4094, all ]" % self.name


VLANIDRange = _VLANIDRange()


class _CIDR(UserType):
    name = "CIDR"

    def validate(self, value):
        errmsg = _(u'值必须是CIDR格式')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if not re.match('\d+.\d+.\d+.\d+/\d+$', value):
            raise exc.VisibleExValueError(errmsg)

        try:
            netaddr.IPNetwork(value)
        except netaddr.AddrFormatError:
            raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return '192.168.1.0/24'

    def tostring(self):
        return "%s" % self.name


CIDR = _CIDR()


class _IPRange(UserType):
    name = "IPRange"

    def validate(self, value):
        errmsg = _(u'值必须是IP范围')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if re.match('\d+.\d+.\d+.\d+-\d+.\d+.\d+.\d+$', value):
            seq = value.split('-')
            try:
                netaddr.IPRange(seq[0], seq[1])
            except netaddr.AddrFormatError:
                raise exc.VisibleExValueError(errmsg)
            return

        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return '192.168.1.100-192.168.1.200'

    def tostring(self):
        return "%s" % self.name


IPRange = _IPRange()


class _IPGroup(UserType):
    name = "IPGroup"

    def validate(self, value):
        errmsg = _(u'值必须是IP组格式')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if value == 'all':
            return
        elif re.match('\d+.\d+.\d+.\d+$', value):
            try:
                netaddr.IPNetwork(value)
            except netaddr.AddrFormatError:
                raise exc.VisibleExValueError(errmsg)
            return
        elif re.match('\d+.\d+.\d+.\d+-\d+.\d+.\d+.\d+$', value):
            seq = value.split('-')
            try:
                netaddr.IPRange(seq[0], seq[1])
            except netaddr.AddrFormatError:
                raise exc.VisibleExValueError(errmsg)
            return
        elif re.match('\d+.\d+.\d+.\d+/\d+$', value):
            try:
                netaddr.IPNetwork(value)
            except netaddr.AddrFormatError:
                raise exc.VisibleExValueError(errmsg)
            return

        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return '192.168.1.100-192.168.1.200'

    def tostring(self):
        return "%s" % self.name


IPGroup = _IPGroup()


class _PortRange(UserType):
    name = 'PortRange'

    def _is_port_string(self, value):
        return int(value) in range(0, 65536)

    def validate(self, value):
        errmsg = _(u'值必须是端口组格式')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if value == 'all':
            return
        elif value.isdigit() and self._is_port_string(value):
            return
        elif re.match('\d+-\d+$', value):
            seq = value.split('-')
            if self._is_port_string(seq[0]) and \
                    self._is_port_string(seq[1]) and \
                    int(seq[0]) < int(seq[1]):
                return
        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return '0-65535'

    def tostring(self):
        return "%s" % self.name


PortRange = _PortRange()


class _IPProtocolNum(UserType):
    name = 'IPProtocolNumber'

    def validate(self, value):
        errmsg = _(u'值必须是协议号')
        if isinstance(value, (str, unicode)) and value == 'all':
            return
        if isinstance(value, int) and value in range(0, 256):
            return
        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return '6'

    def tostring(self):
        return "%s" % self.name


IPProtocolNum = _IPProtocolNum()


class _MACAddress(UserType):
    name = "MACAddress"

    def validate(self, value):
        errmsg = _(u'值必须是MAC地址（字母小写，以:号分隔）')
        # MAC地址可能是全数字，所以不能用islower()
        if isinstance(value, (str, unicode)) \
                and netaddr.valid_mac(value) \
                and ':' in value \
                and not value.isupper():
            return
        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return 'fe:fc:fe:f3:77:b8'

    def tostring(self):
        return "%s" % self.name


MACAddress = _MACAddress()


class _HCIHostID(UserType):
    name = "HCIHostID"

    def validate(self, value):
        errmsg = _(u'值必须是HCI主机ID')
        if not (isinstance(value, (str, unicode))
                and value.startswith('host-')
                and len(value) == 17
                and value.islower()):
            raise exc.VisibleExValueError(errmsg)

        for c in str(ltrim(value, 'host-')):
            if not (c.isdigit() or c.isalpha() or c.islower()):
                raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return 'host-4c72b9d27d49'

    def tostring(self):
        return "%s" % self.name


HCIHostID = _HCIHostID()


class _NFVPortID(UserType):
    name = "NFVPortID"

    def validate(self, value):
        errmsg = _(u'值必须是NFV端口ID')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if not re.match('net\d+$', value):
            raise exc.VisibleExValueError(errmsg)

        id = ltrim(value, 'net')
        if id.isdigit() and int(id) in range(0, 25):
            if len(id) > 1 and int(id) < 10:
                raise exc.VisibleExValueError(errmsg)
            return

        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return 'net0'

    def tostring(self):
        return "%s" % self.name


NFVPortID = _NFVPortID()


class _WorkflowID(UserType):
    name = "WorkflowID"

    def validate(self, value):
        errmsg = _(u'值必须是工单编号字符串')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        if not value.isdigit() or len(value) != len("20180103000025"):
            raise exc.VisibleExValueError(errmsg)

        m = re.match('(\d\d\d\d)(\d\d)(\d\d)\d+$', value)
        year = int(m.group(1))
        month = int(m.group(2))
        day = int(m.group(3))
        if not (year >= 2010 and year <= 2099):
            raise exc.VisibleExValueError(errmsg)
        if not (month >= 1 and month <= 12):
            raise exc.VisibleExValueError(errmsg)
        if not (day >= 1 and day <= 31):
            raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return "20180129000001"

    def tostring(self):
        return "%s" % self.name


WorkflowID = _WorkflowID()


class _SnapshotID(UserType):
    name = 'SnapshotID'

    def validate(self, value):
        # 参考HCI的sub verify_snapid()函数
        errmsg = _(u'值必须是快照ID格式的字符串')
        if not isinstance(value, (str, unicode)):
            raise exc.VisibleExValueError(errmsg)

        formats = [
            '^a[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}a$',  # noqa: E501
            '^auto-\d{6}-\d{6}-[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',  # noqa: E501
            # VMware格式，auto+UUID
            '^auto-[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$',  # noqa: E501
        ]
        for fmt in formats:
            if re.match(fmt, value):
                return

        raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return 'auto-180705-203239-cc131774-ee10-44a9-ad43-da912b47849e'

    def tostring(self):
        return "%s" % self.name


SnapshotID = _SnapshotID()


class _OctetStream(UserType):
    name = "application/octet-stream"

    def validate(self, value):
        errmsg = _(u'值必须是webob.Response对象')
        if not isinstance(value, webob.Response):
            raise exc.VisibleExValueError(errmsg)

    def sample(self):
        return "application/octet-stream"

    def tostring(self):
        return "%s" % self.name


OctetStream = _OctetStream()


class _IndescribableType(UserType):
    name = "IndescribableType"

    def validate(self, value):
        pass

    def sample(self):
        return '......'

    def tostring(self):
        return "%s" % self.name


IndescribableType = _IndescribableType()
