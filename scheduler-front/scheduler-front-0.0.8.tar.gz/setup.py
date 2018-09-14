from setuptools import setup


setup(
    name='scheduler-front',
    version="0.0.8",
    author='Julio Gajardo',
    author_email='j.gajardo@criteo.com',
    description='Simple library to create scheduled scripts',
    license='MIT',
    url='https://gitlab.criteois.com/j.gajardo/scheduler_front',
    packages=['scheduler_front'],
    entry_points = {
        'console_scripts': ['create-scheduled-job=scheduler_front.app:start']
    },
    install_requires=['flask'],
package_data={'scheduler_front':['templates/*']}
)

__author__ = 'Julio Gajardo'
