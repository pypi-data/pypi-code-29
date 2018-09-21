# -*- coding: utf-8 -*-
#
# This file is part of ProjectBubble.
#
# (c) Giant - MouGuangyi <mouguangyi@ztgame.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import os
import shutil
import subprocess


# 执行shell命令
def shell(cmd):
    print(cmd)
    return subprocess.getoutput(cmd)


# 复制文件
def copyfile(src, dest):
    shutil.copy(src, dest)


# 删除文件
def deletefile(dest):
    if os.path.exists(dest):
        os.remove(dest)


# 复制目录及子目录
def copyfolder(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)

    shutil.copytree(src, dest)


# 删除目录
def deletefolder(dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)


# 移动文件/目录
def move(src, dest):
    shutil.move(src, dest)

