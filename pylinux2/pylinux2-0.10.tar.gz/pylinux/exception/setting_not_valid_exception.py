# /usr/bin/env python
# coding=utf-8


class SettingNotValidException(Exception):
    pass


if __name__ == '__main__':
    raise SettingNotValidException("测试异常")
