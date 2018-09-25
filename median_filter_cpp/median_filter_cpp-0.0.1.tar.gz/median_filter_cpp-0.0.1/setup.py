from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name='median_filter_cpp',
    version = '0.0.1',
    author='jhji',
    author_email='jhji.soochow@gmail.com',
    url='https://www.crowdai.org/challenges/nips-2018-adversarial-vision-challenge',
    ext_modules=[
        CppExtension('median_filter_cpp', ['median_filter.cpp']),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
