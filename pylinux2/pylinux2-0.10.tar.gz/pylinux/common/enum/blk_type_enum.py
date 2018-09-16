# /usr/bin/env python
# coding=utf-8

from enum import Enum


class FileSystemEnum(Enum):
    EXT4 = "ext4"

    @staticmethod
    def from_str(type_string):
        if FileSystemEnum.EXT4 == type_string:
            return FileSystemEnum.EXT4


if __name__ == '__main__':
    pass
    # [attr for attr in dir(obj()) if not callable(getattr(obj(),attr)) and not attr.startswith("__")]
