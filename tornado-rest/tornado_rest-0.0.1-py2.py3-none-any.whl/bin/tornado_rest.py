#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : tornado_rest.py
# @Date : 2018/9/7 17:13
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import os
import sys
from os import path
from shutil import copyfile


def create_project(project_name):
    file_path = os.path.abspath(__file__)
    template_dir = os.path.split(os.path.split(file_path)[0])[0]
    base_dir = project_name
    exclude_dirs = ['__pycache__', 'bin']
    current_dir = os.path.realpath(os.getcwd())

    prefix_length = len(template_dir) + 1

    for root, dirs, files in os.walk(template_dir):
        # 移除排除文件夹
        for exclude_dir in exclude_dirs:
            if exclude_dir in dirs:
                dirs.remove(exclude_dir)

        # 获取文件夹
        relative_dir = root[prefix_length:]

        # 如果当前目录不存在相对目录,创建文件夹
        target_dir = path.join(current_dir, base_dir, relative_dir)
        if not path.exists(path.join(target_dir)):
            os.mkdir(target_dir)

        for filename in files:
            if filename.endswith(('.py',)):
                old_path = path.join(root, filename)
                new_path = path.join(target_dir, filename)
                copyfile(old_path, new_path)


def execute_from_command_line():
    args = sys.argv
    if len(args) == 3 and args[1] == 'startproject':
        project_name = sys.argv[2]
        if len(project_name.strip()) > 0:
            create_project(project_name=project_name)
        else:
            print ("project name can't be blank!")
