from distutils.core import setup                # 导入构建模块
setup(                                          # 调用setup()方法，填写参数
    name = 'mr_bmi',                            # 包的名称（必要参数）
    version = '0.0.1',                          # 版本号（必要参数）
    author="mrsoft",                             # 作者名称
    author_email='mingrisoft@mingrisoft.com',   # 作者的电子邮件地址
    url='https://pypi.org/simple/mr_bmi/',      # 模块或包的主页
    py_modules = ['mr.bmi'],                      # 指定发布的模块名称
    packages = ['mr'])                         # 指定发布的包名称
