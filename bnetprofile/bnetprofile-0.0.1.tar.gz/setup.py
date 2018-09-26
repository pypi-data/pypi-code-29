import setuptools

VERSION = "0.0.1"

setuptools.setup(
    name="bnetprofile",
    packages=setuptools.find_packages(),
    package_data={},
    version=VERSION,
    description="SC2 Battle.net profile redirection app for All Inspiration Apps",
    author="Hugo Wainwright",
    author_email="wainwrighthugo@gmail.com",
    url="https://github.com/frugs/allin-bnetprofile",
    keywords=["sc2", "all-inspiration"],
    classifiers=[],
    install_requires=[
        "requests>=2.19.1",
        "requests-toolbelt>=0.8.0",
        "Flask-OAuthlib",
        "flask",
        "google-cloud-datastore",
    ],
)
