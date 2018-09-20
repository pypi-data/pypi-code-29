#me: setup.py
# Author: ma
# Created Time:  2018-09-20
#############################################


from setuptools import setup, find_packages

setup(
    name = "ai_bot",
    version = "0.0.1",
    keywords = ("pip", "BotServer","Callcenter","VoiceBot","ai_bot","callcenter"),
    description = "18-ai_bot0.1.0",
    long_description = "ai_bot0.1.0",
    license = "MIT Licence",
    url = "https://github.com/MaPing01/pipProject",
    author = "MaPing01",
    author_email = "pingpingma001@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)

