
from setuptools import setup

setup(
    name='geek-translate',
    version='0.6.0',
    description='sogou',
    install_requires=[
        "requests >= 2.13.0",
        "pinyin == 0.4.4"
    ],
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers'
    ],
    author='chen',
    url='https://github.com/mydu27/deemo',
    author_email='chenjiageng@geekpark.net',
    packages=['geek_translate'],
    include_package_data=False,
    zip_safe=True
)
