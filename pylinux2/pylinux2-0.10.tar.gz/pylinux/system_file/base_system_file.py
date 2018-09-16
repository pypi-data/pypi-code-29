# /usr/bin/env python
# coding=utf-8
from pylinux.common.file_config.file_config import FileConfig
from pylinux.common.acessor.base_accessor import BaseAccessor


class BaseSystemFile(object):
    """
    系统文件的基类
    """

    def __init__(self, filepath, accessor=BaseAccessor, file_config=FileConfig()):
        self.filepath = filepath
        self.lines = []
        self.load()

        self.accessor = accessor(self.lines, file_config=file_config)

    def load(self):
        """
        载入文件
        """
        with open(self.filepath, "rb") as f:
            self.lines = f.readlines()

    def flush(self):
        with open(self.filepath, "wb") as f:
            f.writelines(self.lines)

    def get_setting(self, name):
        return self.accessor.get_setting(name)

    def setting_exists(self, name):
        return self.accessor.setting_exist(name)

    def set_setting(self, name, value, add_comment=True):
        occurrence = self.accessor.get_setting_occurrence(name)
        if occurrence:
            self.accessor.update_setting(name, value)
        else:
            self.accessor.add_setting(name, value, add_comment)
        self.flush()
