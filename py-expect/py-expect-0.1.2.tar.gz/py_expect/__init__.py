NORMAL_TYPES = (int, float, bool, str, unicode)
NUMBER_TYPES = (int, float, long, complex)


class ExpectError(RuntimeError):
    pass


class _Expect(object):
    '''
    Base Class
    '''

    def validate(self, val):
        raise NotImplementedError


class ExpectBool(_Expect):
    '''
    bool value expect
    '''

    def __init__(self, value=None, noneable=False):
        self.noneable = noneable
        self.value = value

    def validate(self, val):
        if self.noneable and val is None:
            return
        assert type(val) == bool, u'except `{}`, but got `{}`'.format(bool, type(val))

        if self.value is not None:
            assert val == self.value, u'except `{}`, but got `{}`'.format(self.value, val)


class ExpectNone(_Expect):
    '''
    None value expect
    '''

    def __init__(self):
        pass

    def validate(self, val):
        assert val is None, u'except `{}`, but got `{}`'.format(None, val)


class ExpectNumber(_Expect):
    '''
    number value expect, include int, long, float, complex
    '''

    def __init__(self, type=None, value=None, min=None, max=None, enum=None, noneable=False):
        self.min = min
        self.max = max
        self.enum = enum
        self.value = value
        self.noneable = noneable
        self.types = [type] if type else NUMBER_TYPES

    def validate(self, val):
        if self.noneable and val is None:
            return

        if self.value is not None:
            assert self.value == val, u'expect number `{}`, but got `{}`'.format(self.value, val)

        assert type(val) in self.types, u'except {}, but got {}'.format(self.types if len(self.types) > 1 else self.types[0], type(val))

        if self.min is not None:
            assert val >= self.min, u'value `{}` is less then min value {}'.format(val, self.min)
        if self.max is not None:
            assert val <= self.max, u'value `{}` is great then max value {}'.format(val, self.max)
        if self.enum:
            assert val in self.enum, u'value must be one of {}'.format(self.enum)


class ExpectInt(ExpectNumber):
    def __init__(self, **kws):
        super(ExpectInt, self).__init__(type=int, **kws)


class ExpectLong(ExpectNumber):
    def __init__(self, **kws):
        super(ExpectLong, self).__init__(type=long, **kws)


class ExpectFloat(ExpectNumber):
    def __init__(self, **kws):
        super(ExpectFloat, self).__init__(type=float, **kws)


class ExpectComplex(ExpectNumber):
    def __init__(self, **kws):
        super(ExpectComplex, self).__init__(type=complex, **kws)


class ExpectStr(_Expect):
    '''
    expect str value
    '''

    def __init__(self, value=None, min_length=None, max_length=None, enum=None, noneable=False):
        '''
        :param value: expect the exact str value.
        :param min_length: min length of the str value.
        :param max_length: max length of the str value.
        :param enum: expect one of the value in enum.
        :param noneable: check if none is valid.
        '''
        self.min_length = min_length
        self.max_length = max_length
        self.value = value
        self.enum = enum
        self.noneable = noneable

    def validate(self, val):
        if self.noneable and val is None:
            return

        if self.value is not None:
            assert self.value == val, u'expect str `{}`, but got `{}`'.format(self.value, val)

        assert type(val) in [str, unicode], u'except {}, but got {}'.format(str, type(val))

        if self.min_length is not None:
            assert len(val) >= self.min_length, u'str length {} is less then min length {}'.format(len(val), self.min_length)
        if self.max_length is not None:
            assert len(val) < self.max_length, u'str length {} is great then max length {}'.format(len(val), self.max_length)
        if self.enum:
            assert val in self.enum, u'value must be one of {}'.format(self.enum)


class ExpectDict(_Expect):
    def __init__(self, item={}, strict=False, noneable=False):
        '''
        :param item: match template
        :param strict: if strict is True, target value must match all the keys of item
        :param noneable: check if none is valid
        '''
        self.item = item
        self.strict = strict
        self.noneable = noneable
        if type(self.item) != dict:
            raise Exception('ExpectDict needs dict argumnet')

    def validate(self, val):
        if self.noneable and val is None:
            return
        assert type(val) == dict, 'except dict, but got `{}`'.format(type(val))
        if self.strict:
            assert len(self.item.keys()) == len(val.keys()), u'dict keys `{}` is not match `{}` in strict mode'.format(val.keys(), self.item.keys())
        for k, v in self.item.iteritems():
            if type(v) in NORMAL_TYPES:
                assert type(val.get(k)) == type(v), u'{} except {}({}), but got {}({})'.format(k, v, type(v), val.get(k), type(val.get(k)))
                assert val.get(k) == v, u'{} except {}({}), but got {}({})'.format(k, v, type(v), val.get(k), type(val.get(k)))
            elif v in NORMAL_TYPES:
                error_msg = u'{} except type {}, but got {}'.format(k, v, type(val.get(k)))
                if v == str:
                    assert type(val.get(k)) in [str, unicode], error_msg
                else:
                    assert type(val.get(k)) == v, error_msg
            elif isinstance(v, _Expect):
                try:
                    v.validate(val.get(k))
                except AssertionError as err:
                    raise AssertionError(u'{}.'.format(k) + err.message)


class ExpectList(_Expect):
    def __init__(self, item=None, min_length=None, max_length=None, noneable=False):
        '''
        :param item: list item match template. It can be Python type, Expect instance or constant value.
        :param min_length: min length of list
        :param max_length: max length of list
        :param noneable: check if none is valid
        '''
        self.min_length = min_length
        self.max_length = max_length
        self.noneable = noneable
        self.item = item

        self.expect = None
        if self.item is not None:
            self.expect = Expect(self.item)

    def validate(self, val):
        if self.noneable and val is None:
            return

        assert type(val) in [list, tuple], 'list item except {} or {}, but got {}'.format(list, tuple, type(val))
        if self.min_length is not None:
            assert len(val) >= self.min_length, 'list or tuple length {} is less then min length {}'.format(len(val), self.min_length)
        if self.max_length is not None:
            assert len(val) <= self.max_length, 'list or tuple length {} is great then max length {}'.format(len(val), self.max_length)

        if self.expect:
            for item in val:
                try:
                    self.expect.validate(item)
                except AssertionError as err:
                    raise AssertionError(u'list item error: ' + err.message)


class ExpectInstance(_Expect):
    def __init__(self, _class):
        '''
        :param _class: expect value to be instance of _class
        '''
        self._class = _class

    def validate(self, val):
        assert isinstance(val, self._class), 'expect instance of `{}`, but got `{}`'.format(self._class, type(val))


class Expect(_Expect):
    def __init__(self, value, **kws):
        self.expect = None
        if type(value) == dict:
            self.expect = ExpectDict(value, **kws)
        elif type(value) in [list, tuple]:
            self.expect = ExpectList(value[0] if len(value) else None, **kws)
        elif type(value) in NUMBER_TYPES:
            self.expect = ExpectNumber(type=type(value), value=value, **kws)
        elif type(value) == str:
            self.expect = ExpectStr(value=value, **kws)
        elif type(value) == bool:
            self.expect = ExpectBool(value=value, **kws)
        elif value in NUMBER_TYPES:
            self.expect = ExpectNumber(type=value, **kws)
        elif value == str:
            self.expect = ExpectStr(**kws)
        elif value == bool:
            self.expect = ExpectBool(**kws)
        elif value is None:
            self.expect = ExpectNone(**kws)
        elif isinstance(value, _Expect):
            self.expect = value

    def validate(self, val):
        self.expect.validate(val)
