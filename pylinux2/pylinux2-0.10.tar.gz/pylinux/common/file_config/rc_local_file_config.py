# /usr/bin/env python
# coding=utf-8
from pylinux.common.file_config.line_setting_file_config import LineSettingFileConfig


class RcLocalFileConfig(LineSettingFileConfig):

    def __init__(self):
        super(RcLocalFileConfig, self).__init__()
        self.connector = None

