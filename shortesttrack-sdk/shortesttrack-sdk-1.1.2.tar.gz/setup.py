from setuptools import setup, find_packages

setup(
    name='shortesttrack-sdk',
    version='1.1.2',
    description='SDK for work with ShortestTrack API',
    packages=find_packages(),
    install_requires=['URLObject', 'requests', 'setuptools'],
    author='Stanislav Pospelov',
    author_email='stpospelov@shtr.io',
    license='MIT'
)

