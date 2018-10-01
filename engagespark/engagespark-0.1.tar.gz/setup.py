from setuptools import setup

setup(
    name='engagespark',
    version='0.1',
    description='Python integration with engageSPARK',
    url='https://engagespark.com',
    author='engageSPARK',
    author_email='helpteam@engagespark.com',
    license='MIT',
    packages=['engagespark'],
    install_requires=[
        'requests>=2.19.1',
    ],
    zip_safe=True,
    python_requires='>=3',
    project_urls={
        'Source Code': 'https://github.com/engagespark/python-sdk',
    },
    keywords='sms calls engage spark engagespark scale mobile data telco',
)
