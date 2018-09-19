from setuptools import setup
with open("README.md", "r") as readme:
    long_description = readme.read()
setup(name="find_ida_user_dir",
      version="0.2.1",
      py_modules=["find_ida_user_dir"],
      description="Find the user directory for IDA Pro in a platform-independent way",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/Whatang/find_ida_user_dir",
      author="Mike Thomas",
      author_email="ida@whatang.org",
      license="GPLv3",
      classifiers=["Programming Language :: Python :: 2",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: OS Independent",
                   "Topic :: Software Development :: Disassemblers"],
      keywords="IDA")
