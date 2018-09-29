from setuptools import setup

requires = [
    "pyhcl>=0.3.00",
]


setup(
    name='tf_cop',
    version='0.0.1',
    description='auto terraform review',
    url='https://github.com/ys-tydy/tf_cop',
    author='ys-tydy',
    author_email='',
    license='ys-tydy',
    keywords='terraform hcl review',
    packages=[
        "tf_cop",
    ],
    install_requires=requires,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
    ],
)
