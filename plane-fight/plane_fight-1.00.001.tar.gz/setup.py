'''
AUTHOR: wqunlong
VERSION: V1.0.000
DESC: 打包当前python程序包的模块
'''
from distutils.core import setup

# 具体打包信息
setup(
    name="plane_fight",                     # 发布的包文件名称
    description="飞机大战测试版",             # 发布包的描述信息
    version="1.00.001",                     # 发布包的版本号
    author="wqunlong",                      # 发布包的作者信息
    author_email="wqunlong@foxmail.com",    # 作者联系邮箱信息
    py_modules=['__init__', 'demo01', 'resourses']       # 发布的包中的模块文件 列表
)
