#引入构建包信息的模块
from distutils.core import setup

#定义发布的包文件信息
setup(
    name="wang_test",
    version="1.0.00.001",
    description="我的第二个测试包",
    author="人间不值得",
    author_email="1851524312@qq.com",
    py_modules=['__init__','enginer','func','main','name','readme','tools']



)