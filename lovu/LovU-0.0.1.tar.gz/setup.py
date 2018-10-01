import setuptools #导入 setuptools ,就是把那位官爷请来,我们需要告诉他很多信息的.

with open("README.md", "r") as fh: #打开readme 文件,一般是用 markdown 写的.
    long_description = fh.read()

setuptools.setup(
    name="LovU", # 你的项目名称填进去
    version="0.0.1", #项目的版本号
    author=" Yaakov Azat", #项目的作者是谁?
    author_email="yaakovazat@gmail.com", #项目的作者邮箱
    description="Say Love in more than 100 languages~", #项目的说明,就是简单讲一下你这个项目(这个程序)实现了什么功能,可以用来怎么装逼的...
    long_description=long_description, # 加长版的说名,如果你能比较啰嗦,就把加长的说明写进readme.md 文件里面.
    long_description_content_type="text/markdown",
    url="https://github.com/yaakovazat/LovU", #项目地址~
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3", #程序语言 我一般都用 Python3 
        "License :: OSI Approved :: MIT License", # 版权说明
        "Operating System :: OS Independent",
    ],
)