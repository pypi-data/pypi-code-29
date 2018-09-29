#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-27 15:44:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

'''
'nester.py'model提供嵌套打印功能模块
'''
def print_lol(the_list):
	'''
	函数功能：判断是否list类型，如果是循环执行，否则打印
	'''
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)


