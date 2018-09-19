#!/usr/bin/python

import sys
if len(sys.argv)<4:
    print("参数错误：请以python rect.py 10 8")
    sys.exit(-1)
try:
    w=int(sys.argv[1])+1
    h=int(sys.argv[2])
    code=str(sys.argv[3])
    code_two=code+' '
    print(code_two*w)
    for i in range(h-3):
        print(code+' '*(w*2-3)+code)
    print(code_two*w)
except ValueError:
    print("异常")

