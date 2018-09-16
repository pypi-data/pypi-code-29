# /usr/bin/env python
# coding=utf-8

import os

from pylinux.common.util.command_util import run_cmd
from pylinux.common.enum.blk_type_enum import FileSystemEnum


class Block(object):
    def __init__(self, line):
        self.line = line

        self.name = None
        self.size = None
        self.type = None
        self.mount_point = None
        self.fs = None
        self.partitions = []

    def is_partition(self):
        return self.type == "part"

    def is_disk(self):
        return self.type == "disk"

    def __str__(self):
        return self.line


def parse_lsblk_output(text):
    """
    to ensure the readability, we do not use a better or best algorithm which is better in performance.

    text example:
    NAME  FSTYPE   SIZE TYPE MOUNTPOINT
    xvda           250G disk
    xvda1 ext4     250G part /
    xvdb  ext4    1000G disk /home/admin/name/123
    xvdc  ext4    1000G disk /home/admin/name/123/xxx
    :param text:
    :return:
    """
    block_list = []

    lines = text.split(os.linesep)
    lines = [x.strip() for x in lines]
    lines = [x for x in lines if x]

    length_list = [len(line) for line in lines]
    space_idx_list = [i for i, x in enumerate(lines[0]) if x == " "]
    for idx in space_idx_list[:]:
        for i, line in enumerate(lines):
            if idx >= length_list[i]:
                continue
            if line[idx] != " ":
                space_idx_list.remove(idx)
                break

    i = 0
    while i + 1 <= len(space_idx_list) - 1:
        first = space_idx_list[i]
        second = space_idx_list[i + 1]
        if first + 1 == second:
            space_idx_list.remove(first)
        else:
            i = i + 1
    # merge neighbouring space idx
    if 4 != len(space_idx_list):
        raise ValueError("space idx of heading error")

    for line in lines:
        block = Block(line)
        block.name = line[:space_idx_list[0]].strip()
        block.fs = FileSystemEnum.from_str(line[space_idx_list[0]:space_idx_list[1]].strip())
        block.size = line[space_idx_list[1]:space_idx_list[2]].strip()
        block.type = line[space_idx_list[2]:space_idx_list[3]].strip()
        block.mount_point = line[space_idx_list[3]:].strip()
        block_list.append(block)

    # remove header
    block_list = block_list[1:]

    current_disk = None
    for i, block in enumerate(block_list):
        if block.is_disk():
            current_disk = block
            continue

        if block.is_partition() and current_disk:
            current_disk.partitions.append(block)
            continue

    return block_list


def list_blocks():
    stdout = run_cmd(["sudo", "lsblk", "--output", "NAME,FSTYPE,SIZE,TYPE,MOUNTPOINT", "--list"],
                     print_command=False)
    block_list = parse_lsblk_output(stdout)
    return block_list
