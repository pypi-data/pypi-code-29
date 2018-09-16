# /usr/bin/env python
# coding=utf-8

from pylinux.common.file_config.rc_local_file_config import RcLocalFileConfig
from pylinux.common.modifier.line_setting_modifier import LineSettingModifier
from pylinux.common.modifier.rc_local_modifier import RcLocalModifier
from pylinux.common.acessor.line_setting_accessor import LineSettingAccessor
from pylinux.common.acessor.rc_local_accessor import RcLocalAccessor
from pylinux.system_file.base_system_file import BaseSystemFile
from pylinux.exception.name_not_valid_exception import NameNotValidException
from pylinux.exception.setting_not_valid_exception import SettingNotValidException


class LineSettingFile(BaseSystemFile):
    """
    rc.local的配置文件类
    """

    def __init__(self, filepath="/etc/rc.local", searcher=LineSettingAccessor, modifier=LineSettingModifier,
                 file_config=LineSe()):
        super(LineSettingFile, self).__init__(filepath, searcher, modifier, file_config=file_config)

    def add_boot_item(self, cmd, name):
        """
        增加启动项
        :param name:
        :param cmd:
        """
        if not name:
            raise NameNotValidException("name not valid while adding boot item")

        if not cmd:
            raise SettingNotValidException("setting not valid while adding boot item")

    def add_multi_line_setting(self, name, value):
        pass
