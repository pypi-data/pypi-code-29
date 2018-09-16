# /usr/bin/env python
# coding=utf-8


class FileConfig(object):

    def __init__(self):
        self.connector = "="
        self.comment_symbols = ["#"]
        self.comment_line_template_prefix = self.get_default_comment_symbol() * 6
        self.comment_line_template_suffix = self.get_default_comment_symbol() * 6
        self.comment_line_template = "{0} pylinux setting: [{1}] {2}".format(
            self.comment_line_template_prefix,
            "{}",
            self.comment_line_template_suffix)
        self.comment_line_pattern = "{0} pylinux setting: \\[(.+?)\\] {1}".format(
            self.comment_line_template_prefix,
            self.comment_line_template_suffix)

    def get_default_comment_symbol(self):
        return self.comment_symbols[0]

    def generate_setting_comment(self, name):
        """
        生成一个配置的注释行
        :param name:
        :return:
        """
        return self.comment_line_template.format(name)

    def generate_setting_line(self, name, value):
        """
        生成一个配置行
        :param name:
        :param value:
        :return:
        """
        return name + " " + self.connector + " " + value