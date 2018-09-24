from setuptools import setup

setup(
    name='shortesttrack-sdk',
    version='1.1.8',
    description='SDK for work with ShortestTrack API',
    packages=[
        'shortesttrack',
        'shortesttrack.client',
        'shortesttrack.library'
    ],
    install_requires=['URLObject', 'requests', 'setuptools'],
    author='Stanislav Pospelov',
    author_email='stpospelov@shtr.io',
    license='MIT'
)

