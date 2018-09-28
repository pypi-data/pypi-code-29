# -*- coding: utf-8 -*-
# @Time    : 18-9-28 下午1:07
# @Author  : duyongan
# @FileName: utils.py
# @Software: PyCharm
import pickle

def read_pickle(filename):
    with open(filename,'rb') as f:
        return pickle.load(f)

def write_pickle(data,filename):
    with open(filename,'wb') as f:
        return pickle.dump(data,f)

def read_data(filename):
    with open(filename,encoding='utf-8') as f:
        return f.readlines()

def write_data(data,filename):
    with open(filename,'wb',encoding='utf-8') as f:
        f.write(data)

def write_datalist(datalist,filename):
    with open(filename,'wb',encoding='utf-8') as f:
        f.writelines(datalist)