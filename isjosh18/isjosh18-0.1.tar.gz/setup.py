from setuptools import setup

setup(
    name='isjosh18',
    packages=['isjosh18'],
    version='0.1',
    description='This tool determines if Josh is 18.',
    author='numirias',
    author_email='numirias@users.noreply.github.com',
    url='',
    license='MIT',
    python_requires='>=2.7',
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'isjosh18 = isjosh18.__main__:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
