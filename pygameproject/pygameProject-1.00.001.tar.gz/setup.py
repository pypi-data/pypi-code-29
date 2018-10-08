#打包当前python程序包的模块

from distutils.core import setup


# 具体打包信息
setup(
    name="pygameProject",# 发布的包文件名称
    version="1.00.001",# 发布的包的版本序号
    description="使用说明",# 发布包的描述信息
    author="大大余",# 发布包的作者信息
    author_email="yhs@163.com",# 作者联系邮箱信息
    py_modules=["__init__","setup","task2"]# 发布的包中的模块文件列表)
)