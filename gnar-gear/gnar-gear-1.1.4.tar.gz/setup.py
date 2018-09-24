from setuptools import setup

setup(
    name='gnar-gear',
    version='1.1.4',
    description='The gnarliest gear in the world 🤙',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/gnaar/gear',
    author='Brien R. Givens',
    author_email='ic3b3rg@gmail.com',
    license='MIT',
    packages=['gnar_gear'],
    install_requires=[
        'argon2_cffi>=18.3.0',
        'boto3>=1.9.3',
        'bjoern>=2.2.2',
        'flask>=1.0.2',
        'flask-jwt-extended>=3.12.1',
        'postgres>=2.2.2',
        'requests>=2.19.1'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest>=3.8.0',
        'pytest-cov>=2.6.0'
    ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Flask'
    ]
)
