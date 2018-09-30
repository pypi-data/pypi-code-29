
from setuptools import setup  # 导入构建模块中的setup()方法

with open("README.md", "r") as fh:
    long_description = fh.read()            # 读取项目叙述文件内的信息
setup(  # 调用setup()方法，填写参数
    name='mr_bmi',  # 包的名称（必要参数）
    version='0.0.2',  # 版本号（必要参数）
    author="mrsoft",  # 作者名称
    author_email='mingrisoft@mingrisoft.com',  # 作者的电子邮件地址
    long_description=long_description,         # 设置较长的项目叙述
    url='https://pypi.org/simple/mr_bmi/',     # 项目的主页
    packages=['mr'])                           # 指定发布的包名称
