# /usr/bin/env python
# coding=utf-8

import re

from pylinux.common.file_config.file_config import FileConfig
from pylinux.exception.setting_not_found_exception import SettingNotFoundException


class BaseAccessor(object):

    def __init__(self, lines, file_config=FileConfig()):
        self.lines = lines
        self.file_config = file_config

    def get_setting(self, name):
        """
        根据设置的名字 获取设置的值
        :param name:
        :return:
        """
        setting_line = self.get_setting_line(name)

        if setting_line:
            return self.setting_from_single_line(setting_line)
        return None

    def setting_from_single_line(self, line):
        """
        从设置的单行取到设置的值
        :param line:
        :return:
        """
        first_connector_index = line.find(self.file_config.connector)
        if -1 == first_connector_index:
            return None

        line_setting_value_part = line[first_connector_index + 1:]
        return line_setting_value_part.strip()

    def get_setting_line(self, name):
        """
        获取一行的配置
        :param name:
        """
        occurrence = self.get_setting_occurrence(name)
        return self.lines[occurrence]

    def get_setting_comment_occurrence(self, name):
        """
        获取设置注释的位置
        :param name:
        :return:
        """
        for idx, line in enumerate(self.lines):
            if self.is_line_about_setting_comment(line, name):
                return idx
        return False

    def get_setting_occurrence(self, name):
        """
        获取设置的位置, 在注释的下一行，强制必须有注释
        :param name:
        :return:
        """
        for idx, line in enumerate(self.lines):
            if self.is_line_about_setting_comment(line, name):
                return idx + 1
            if self.__is_line_about_setting(line, name):
                return idx
        return None

    def is_line_about_setting_comment(self, line, name):
        """
        判断这一行是否为某个设置的注释行
        """
        result_list = re.findall(self.file_config.comment_line_pattern, line)
        if not result_list:
            return False

        result = result_list[0]
        return name == result

    def __is_line_about_setting(self, line, name):
        """
        判断该行是不是给定设置项的行
        :param name:
        :param line:
        """
        if name not in line:
            return False

        if self.file_config.connector not in line:
            return False

        for symbol in self.file_config.comment_symbols:
            if line.startswith(symbol):
                return False

        setting_value = self.setting_from_single_line(line)
        return True if setting_value else False

    def setting_exist(self, name):
        """
        判断给定设置是否存在
        :param name:
        :return:
        """
        occurrence = self.get_setting_occurrence(name)
        return True if occurrence else False

    def append_one_line(self, line):
        self.lines.append(line + "\n")

    def add_setting(self, name, value, add_comment):
        if add_comment:
            self.append_one_line(self.file_config.generate_setting_comment(name))

        self.append_one_line(self.file_config.generate_setting_line(name, value))

    def update_setting(self, name, value, occurrence=None):
        if not occurrence:
            occurrence = self.get_setting_occurrence(name)

        if not occurrence:
            return SettingNotFoundException("can not find setting of %s while updating" % name, name)

        line = self.file_config.generate_setting_line(name, value)
        self.lines[occurrence] = line
