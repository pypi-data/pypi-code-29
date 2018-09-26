import sys
from setuptools import setup

PY3 = sys.version_info[0] >= 3

VERSION = "0.3.1"

INSTALL_REQUIRES = (
    'Pillow',
)

TESTS_REQUIRE = (
    'pdfrw',
)

if not PY3:
    INSTALL_REQUIRES += ('enum34',)


setup(
    name="buildr_img2pdf",
    version=VERSION,
    author="",
    author_email="",
    description="",
    long_description="",
    license="",
    keywords="",
    classifiers=[],
    url="",
    package_dir={"": "src"},
    py_modules=['img2pdf', 'jp2'],
    include_package_data=True,
    test_suite='tests.test_suite',
    zip_safe=True,
    install_requires=INSTALL_REQUIRES,
    tests_requires=TESTS_REQUIRE,
    extras_require={
        'test': TESTS_REQUIRE,
    },
    entry_points='''
    [console_scripts]
    img2pdf = img2pdf:main
    ''',
    )
