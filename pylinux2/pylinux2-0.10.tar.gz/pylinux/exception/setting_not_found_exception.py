# /usr/bin/env python
# coding=utf-8


class SettingNotFoundException(Exception):
    pass


if __name__ == '__main__':
    try:
        raise SettingNotFoundException("test raise exception", "123")
    except Exception, e:
        print e.message
        print e.args
