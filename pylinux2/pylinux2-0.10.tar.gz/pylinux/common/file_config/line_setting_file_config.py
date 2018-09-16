# /usr/bin/env python
# coding=utf-8
from pylinux.common.file_config.file_config import FileConfig


class LineSettingFileConfig(FileConfig):

    def __init__(self):
        super(LineSettingFileConfig, self).__init__()
        self.connector = None

