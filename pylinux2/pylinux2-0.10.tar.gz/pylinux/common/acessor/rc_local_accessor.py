# /usr/bin/env python
# coding=utf-8


from pylinux.common.acessor.line_setting_accessor import LineSettingAccessor


class RcLocalAccessor(LineSettingAccessor):
    """
    rc.local文件是 line setting文件的一个典型派生情况
    除了最末尾多了一个exit 0
    """



