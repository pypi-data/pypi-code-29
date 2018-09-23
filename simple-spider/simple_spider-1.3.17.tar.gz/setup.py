from setuptools import setup

setup(
    name='simple_spider',
    version='1.3.17',
    url='https://www.typechodev.com',
    license='Apache Software License',
    author='leimiu',
    author_email='miuyin@126.com',
    description='simple spider framework',

    long_description="",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3'
    ],
    packages=['simple_spider'],
    install_requires=[
        'requests[socks]',
        'pymongo',
        'pyquery',
        'redis',
        'simplejson',
        'tomd',
        'markdown'
    ]
)

'''
发布步骤：参考 https://packaging.python.org/tutorials/packaging-projects/#create-an-account

# 注意要在项目的虚拟环境中执行
1. pip install --user --upgrade setuptools wheel
2. python setup.py sdist bdist_wheel
3. pip install --upgrade twine #安装上传工具
4. twine upload  dist/* #上传



'''
