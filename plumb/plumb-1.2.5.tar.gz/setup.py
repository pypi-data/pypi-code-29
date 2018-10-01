from setuptools import setup

setup(
    name='plumb',
    packages=[
        'plumb',
        'plumb.aws',
        'plumb.kafka',
        'plumb.redis',
        'plumb.rabbitmq',
        'plumb.factories'
    ],
    version='1.2.5',
    description='Connect systems via many brokers such as Kafka, AWS SQS, RabbitMQ and more.',
    long_description=open('README.rst').read(),

    install_requires=[
        'boto3==1.7.73',
        'botocore==1.10.73',
        'confluent-kafka==0.11.4',
        'pika==0.12.0',
        'python-dateutil==2.7.3',
        'redis==2.10.6'
    ],

    tests_require=[
        'awstestutils==1.0.0',
        'coverage==4.5.1',
        'nose==1.3.7'
    ],

    test_suite='tests',

    author='Spectro Data Engineering Team',
    author_email='data-engineering@spect.ro',

    keywords=['redis', 'AWS', 'queues', 'distributed', 'kafka', 'RabbitMQ', 'AMQP'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: System :: Networking',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Object Brokering',
    ]
)
