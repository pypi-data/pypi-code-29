# /usr/bin/env python
# coding=utf-8

import uuid


def generate_tmp_fp():
    name = uuid.uuid3(uuid.NAMESPACE_DNS, uuid.uuid1().__str__()).__str__()
    return "/tmp/" + "pylinux-" + name + ".txt"
