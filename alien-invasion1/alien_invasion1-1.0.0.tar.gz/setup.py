# 引入构建包信息的模块
from distutils.core import setup

# 定义发布的包文件的信息
setup(
    name="alien_invasion1",  # 发布的包文件名称
    version="1.0.0",  # 发布的包的版本号
    description="这是我第一阶段的项目",  # 发布包的描述信息
    author="陈亮",  # 发布包的作者的信息
    author_email="chenliang.zzuli@foxmail.com",  # 作者联系邮箱信息
    py_modules=["__init__", "alien", "alien_invasion", "bullet", "button",
                "game_functions", "game_stats", "settings", "ship"]  # 发布的包中的模块文件列表
)
