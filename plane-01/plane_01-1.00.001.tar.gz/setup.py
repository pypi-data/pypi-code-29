# 引入构建包信息的模块
from distutils.core import setup

# 定义发布的包文件的信息
setup(
    name="plane_01",  # 发布的包的名称
    version="1.00.001",  # 发布包的版本序号
    description="打飞机小游戏",  # 发布包的描述信息
    author="桔子",  # 发布包的作者信息
    author_email="1847562860@qq.com",  # 作者的联系邮箱
    data_files=['font', 'Images', 'sounds'],
    py_modules=['__init__', 'ariplane']  # 发布包中的模块文件列表
)





















