# /usr/bin/env python
# coding=utf-8


from pylinux.common.acessor.base_accessor import BaseAccessor


class LineSettingAccessor(BaseAccessor):
    """
    LineSettingSearcher 对应的系统文件中，每一行的全文内容就是它的value
    它的key/name只能在注释里存在
    """

    def __is_line_about_setting(self, name, line):
        """
        判断该行是不是给定设置项的行
        在这类文件中里, 一行的全部内容，就是设置的全部内容
        因此每一行都是设置，无法从行内本身判断是否和设置项相关
        只能在其他方法中，通过注释位置推测配置项位置
        此方法直接返回False即可
        :param name:
        :param line:
        """
        return False

    def setting_from_single_line(self, line):
        """
        从设置的单行取到设置的值
        在rc.local里, 行就是设置内容
        :param line:
        :return:
        """
        return line.strip()
