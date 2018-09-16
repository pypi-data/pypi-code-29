# -*- coding: utf-8 -*-

import abc
import string

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
