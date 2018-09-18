# from distutils.core import setup
from setuptools import setup

setup(
    name='ml_pylib',
    version='0.0.3',
    packages=['pylib', 'pylib.util', 'pylib.matlab', 'pylib.tmux'],
    url='https://github.com/DewMaple/pylib',
    description='A lot of handy python methods encapsulated on many commonly used '
                'build-in modules(os, sys, etc.) or popular libs (numpy, tensorflow, cv2, etc. ).',
    author='dew.maple',
    author_email='dew.maple@gmail.com',
    license='MIT',
    keywords=['computer vision', 'image processing', 'opencv', 'numpy', 'tensorflow', 'plt'],
    classifiers=['Programming Language :: Python :: 3.6'],
    project_urls={
        'Bug Reports': 'https://github.com/DewMaple/pylib/issues',
        'Source': 'https://github.com/DewMaple/pylib',
    },
    zip_safe=True
)
