import setuptools

import pocket


setuptools.setup(
    name='pocket-dictionary',
    version=pocket.__version__,
    description='Your handy dict',
    url='https://github.com/sunghyunzz/pocket-dictionary',
    author='Sunghyun Hwang',
    author_email='me' '@' 'sunghyunzz.com',
    python_requires='>=3.7',
    py_modules=['pocket'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ]
)
