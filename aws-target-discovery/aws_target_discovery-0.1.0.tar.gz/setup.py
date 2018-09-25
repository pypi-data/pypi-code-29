from setuptools import setup

setup(
    name='aws_target_discovery',
    author='Peiman Jafari',
    author_email='peiman.ja@hotmail.com',
    version='0.1.0',
    description='Discovers AWS EC2 instance targets for Prometheus',
    url='https://github.com/peimanja/aws_target_discovery',
    entry_points={
        'console_scripts': [
            'aws-target-discovery=aws_target_discovery.main:main'
        ],
    },
    packages=['aws_target_discovery'],
    install_requires=[
        'boto3==1.4.7',
    ],
    include_package_data=True,
    zip_safe=False,
)
